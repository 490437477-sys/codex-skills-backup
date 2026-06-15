#!/usr/bin/env python3
"""
noon FBN Calculator - Core Engine

Calculates FBN (Fulfilled by noon) fees and profit margins for sellers on:
  - noon.sa (Saudi Arabia, SAR, VAT 15%)
  - noon.ae (United Arab Emirates, AED, VAT 5%)
  - noon.com (Egypt, EGP, VAT 14%)

Features:
  - Size tier detection (5 tiers, metric: cm / kg)
  - Marketplace-aware fulfillment fee
  - Storage fee with off-peak / peak / long-term logic
  - Commission by category
  - VAT cash-flow line (15% KSA / 5% UAE / 14% EGY)
  - Returns reserve by category
  - COD friction (optional)
  - Marketing per order (optional)
  - Profit, margin, ROI
  - Optimization suggestions
  - Bilingual output (en / ar) via --ar flag
  - JSON output via --json flag

Disclaimer:
  Rate cards are approximate mid-points based on noon public rate sheets
  ~2024-2025. Verify against noon Seller Central before committing P&L.

Version: 1.0.0
Platform: noon
"""

import json
import sys
import io

# Force UTF-8 on stdout/stderr so Arabic output renders on Windows GBK consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
except (AttributeError, io.UnsupportedOperation):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")  # type: ignore[arg-type]
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")  # type: ignore[arg-type]

from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple
from enum import Enum


# ============================================================
# Enums
# ============================================================

class SizeTier(Enum):
    SMALL_ENVELOPE = "small_envelope"
    SMALL_PARCEL = "small_parcel"
    STANDARD_PARCEL = "standard_parcel"
    LARGE_PARCEL = "large_parcel"
    OVERSIZE = "oversize"


class Marketplace(Enum):
    KSA = "noon-sa"   # SAR, VAT 15%
    UAE = "noon-ae"   # AED, VAT 5%
    EGY = "noon-eg"   # EGP, VAT 14%


# ============================================================
# Rate Tables
# ============================================================

# Size tier detection (metric: cm / kg)
# Tuple order: (weight_kg_max, dim1_cm_max, dim2_cm_max, dim3_cm_max)
SIZE_TIER_LIMITS = [
    (SizeTier.SMALL_ENVELOPE, (0.25, 30, 20, 3)),
    (SizeTier.SMALL_PARCEL,    (1.0,  30, 22, 12)),
    (SizeTier.STANDARD_PARCEL, (5.0,  45, 35, 20)),
    (SizeTier.LARGE_PARCEL,    (15.0, 60, 45, 50)),
    (SizeTier.OVERSIZE,        (999,  999, 999, 999)),
]

# FBN fulfillment fee by marketplace and tier (approximate mid-range, 2024-2025)
FBN_FULFILLMENT_FEE = {
    Marketplace.KSA: {
        SizeTier.SMALL_ENVELOPE: 5.0,
        SizeTier.SMALL_PARCEL:    8.5,
        SizeTier.STANDARD_PARCEL: 12.5,
        SizeTier.LARGE_PARCEL:    23.0,
        SizeTier.OVERSIZE:        35.0,
    },
    Marketplace.UAE: {
        SizeTier.SMALL_ENVELOPE: 5.0,
        SizeTier.SMALL_PARCEL:    8.5,
        SizeTier.STANDARD_PARCEL: 12.5,
        SizeTier.LARGE_PARCEL:    23.0,
        SizeTier.OVERSIZE:        35.0,
    },
    Marketplace.EGY: {
        SizeTier.SMALL_ENVELOPE: 25.0,
        SizeTier.SMALL_PARCEL:    45.0,
        SizeTier.STANDARD_PARCEL: 65.0,
        SizeTier.LARGE_PARCEL:    120.0,
        SizeTier.OVERSIZE:        180.0,
    },
}

# Storage fee per cubic meter per month (off-peak / peak / long-term 180+ days)
STORAGE_FEE_PER_CUBIC_METER = {
    Marketplace.KSA: {"standard": 17.0, "peak": 50.0, "long_term": 170.0},
    Marketplace.UAE: {"standard": 17.0, "peak": 50.0, "long_term": 170.0},
    Marketplace.EGY: {"standard": 100.0, "peak": 250.0, "long_term": 800.0},
}

# Commission rate by category (% of selling price)
COMMISSION_RATES = {
    "default":      0.12,
    "mobiles":      0.06,
    "electronics":  0.10,
    "fashion":      0.15,
    "footwear":     0.15,
    "beauty":       0.16,
    "home":         0.12,
    "kitchen":      0.12,
    "toys":         0.12,
    "baby":         0.12,
    "sports":       0.12,
    "books":        0.13,
    "grocery":      0.10,
    "automotive":   0.11,
    "health":       0.13,
}

# Returns reserve by category (% of selling price)
RETURNS_RESERVE = {
    "default":      0.05,
    "fashion":      0.12,
    "footwear":     0.12,
    "beauty":       0.05,
    "electronics":  0.03,
    "home":         0.05,
    "kitchen":      0.05,
    "toys":         0.05,
    "baby":         0.05,
    "sports":       0.05,
    "books":        0.03,
    "grocery":      0.02,
    "mobiles":      0.03,
    "automotive":   0.03,
    "health":       0.04,
}

# VAT rates (cash-flow line; noon collects from buyer, seller remits)
VAT_RATES = {
    Marketplace.KSA: 0.15,
    Marketplace.UAE: 0.05,
    Marketplace.EGY: 0.14,
}

CURRENCY = {
    Marketplace.KSA: "SAR",
    Marketplace.UAE: "AED",
    Marketplace.EGY: "EGP",
}

# COD friction when cash-on-delivery is enabled
COD_FRICTION_RATE = 0.02


# ============================================================
# Data Classes
# ============================================================

@dataclass
class ProductInput:
    sku: str = "SKU001"
    name: str = "Product"
    length_cm: float = 0.0
    width_cm: float = 0.0
    height_cm: float = 0.0
    weight_kg: float = 0.0
    selling_price: float = 0.0
    product_cost: float = 0.0
    inbound_shipping_cost: float = 0.0
    category: str = "default"
    marketplace: str = "noon-sa"
    monthly_units_sold: int = 100
    inventory_days: int = 45
    inventory_age_days: int = 60
    returns_rate_override: Optional[float] = None
    cod_enabled: bool = False
    marketing_per_order: float = 0.0


@dataclass
class OptimizationTip:
    category: str
    tip_en: str
    tip_ar: str
    potential_savings: float = 0.0


# ============================================================
# Calculation
# ============================================================

def detect_size_tier(length_cm: float, width_cm: float, height_cm: float, weight_kg: float) -> Tuple[SizeTier, str]:
    """Detect FBN size tier from dimensions (cm) and weight (kg)."""
    dims = sorted([length_cm, width_cm, height_cm], reverse=True)
    longest, middle, shortest = dims

    for tier, (w_max, d1_max, d2_max, d3_max) in SIZE_TIER_LIMITS:
        if weight_kg <= w_max and longest <= d1_max and middle <= d2_max and shortest <= d3_max:
            return tier, (
                f"Weight {weight_kg}kg and dimensions "
                f"{length_cm}x{width_cm}x{height_cm}cm fit within {tier.value} limits."
            )
    return SizeTier.OVERSIZE, (
        "Dimensions or weight exceed all standard tier limits; classified as oversize."
    )


def calculate(inp: ProductInput) -> Dict:
    tier, tier_reason = detect_size_tier(
        inp.length_cm, inp.width_cm, inp.height_cm, inp.weight_kg
    )
    mp = Marketplace(inp.marketplace)
    currency = CURRENCY[mp]

    commission_rate = COMMISSION_RATES.get(inp.category, COMMISSION_RATES["default"])
    returns_rate = (
        inp.returns_rate_override
        if inp.returns_rate_override is not None
        else RETURNS_RESERVE.get(inp.category, RETURNS_RESERVE["default"])
    )
    vat_rate = VAT_RATES[mp]

    commission = inp.selling_price * commission_rate
    fbn_fee = FBN_FULFILLMENT_FEE[mp][tier]

    # Storage: cubic meters -> monthly fee -> prorated to inventory_days
    cubic_m = (inp.length_cm * inp.width_cm * inp.height_cm) / 1_000_000
    storage_table = STORAGE_FEE_PER_CUBIC_METER[mp]
    if inp.inventory_age_days > 180:
        storage_monthly_rate = storage_table["long_term"]
        storage_band = "long_term"
    elif inp.inventory_age_days > 90:
        storage_monthly_rate = storage_table["peak"]
        storage_band = "peak"
    else:
        storage_monthly_rate = storage_table["standard"]
        storage_band = "standard"
    storage_total = storage_monthly_rate * cubic_m * (inp.inventory_days / 30.0)

    returns_reserve = inp.selling_price * returns_rate
    cod_friction = inp.selling_price * COD_FRICTION_RATE if inp.cod_enabled else 0.0
    vat_carry = inp.selling_price * vat_rate

    fees = {
        "product_cost": inp.product_cost,
        "commission": commission,
        "fbn_fulfillment": fbn_fee,
        "storage": storage_total,
        "storage_band": storage_band,
        "storage_monthly_rate_per_m3": storage_monthly_rate,
        "returns_reserve": returns_reserve,
        "cod_friction": cod_friction,
        "vat_carry": vat_carry,
        "inbound_shipping": inp.inbound_shipping_cost,
        "marketing": inp.marketing_per_order,
    }

    total_fees = sum(
        v for k, v in fees.items()
        if k not in ("product_cost", "storage_band", "storage_monthly_rate_per_m3")
    )
    total_cost = inp.product_cost + total_fees
    net_profit = inp.selling_price - total_cost
    net_margin = net_profit / inp.selling_price if inp.selling_price > 0 else 0.0
    gross_profit = inp.selling_price - inp.product_cost - inp.inbound_shipping_cost
    gross_margin = gross_profit / inp.selling_price if inp.selling_price > 0 else 0.0
    roi = net_profit / inp.product_cost if inp.product_cost > 0 else 0.0

    tips = generate_optimization_tips(inp, fees, tier, mp, net_margin)

    return {
        "sku": inp.sku,
        "name": inp.name,
        "marketplace": mp.value,
        "currency": currency,
        "category": inp.category,
        "size_tier": tier.value,
        "tier_reason": tier_reason,
        "cubic_meters": round(cubic_m, 6),
        "selling_price": round(inp.selling_price, 2),
        "fees": {k: round(v, 2) if isinstance(v, (int, float)) else v for k, v in fees.items()},
        "total_fees": round(total_fees, 2),
        "total_cost": round(total_cost, 2),
        "net_profit": round(net_profit, 2),
        "net_margin_pct": round(net_margin * 100, 2),
        "gross_profit": round(gross_profit, 2),
        "gross_margin_pct": round(gross_margin * 100, 2),
        "roi_pct": round(roi * 100, 2),
        "commission_rate_pct": round(commission_rate * 100, 2),
        "returns_rate_pct": round(returns_rate * 100, 2),
        "vat_rate_pct": round(vat_rate * 100, 2),
        "monthly_units_sold": inp.monthly_units_sold,
        "monthly_net_profit": round(net_profit * inp.monthly_units_sold, 2),
        "optimization_tips": [
            {"category": t.category, "tip_en": t.tip_en, "tip_ar": t.tip_ar,
             "potential_savings": round(t.potential_savings, 2)}
            for t in tips
        ],
    }


def generate_optimization_tips(
    inp: ProductInput, fees: Dict, tier: SizeTier, mp: Marketplace, net_margin: float
) -> List[OptimizationTip]:
    tips: List[OptimizationTip] = []

    # Tier downgrade potential
    if tier == SizeTier.LARGE_PARCEL:
        savings = FBN_FULFILLMENT_FEE[mp][tier] - FBN_FULFILLMENT_FEE[mp][SizeTier.STANDARD_PARCEL]
        longest = max(inp.length_cm, inp.width_cm, inp.height_cm)
        if longest > 45:
            tips.append(OptimizationTip(
                category="tier",
                tip_en=f"Reduce the longest side by {longest - 45:.1f}cm to drop from large_parcel to standard_parcel. "
                       f"Estimated saving: {fees['fbn_fulfillment']:.2f} -> {FBN_FULFILLMENT_FEE[mp][SizeTier.STANDARD_PARCEL]:.2f} per unit.",
                tip_ar=f"قلّل أطول ضلع بمقدار {longest - 45:.1f} سم للانتقال من large_parcel إلى standard_parcel. "
                       f"التوفير المتوقع: من {fees['fbn_fulfillment']:.2f} إلى {FBN_FULFILLMENT_FEE[mp][SizeTier.STANDARD_PARCEL]:.2f} لكل وحدة.",
                potential_savings=savings,
            ))
    elif tier == SizeTier.STANDARD_PARCEL:
        savings = FBN_FULFILLMENT_FEE[mp][tier] - FBN_FULFILLMENT_FEE[mp][SizeTier.SMALL_PARCEL]
        if inp.weight_kg > 1.0:
            tips.append(OptimizationTip(
                category="weight",
                tip_en=f"Reduce weight by {inp.weight_kg - 1.0:.2f}kg to drop from standard_parcel to small_parcel. "
                       f"Estimated saving: {fees['fbn_fulfillment']:.2f} -> {FBN_FULFILLMENT_FEE[mp][SizeTier.SMALL_PARCEL]:.2f} per unit.",
                tip_ar=f"قلّل الوزن بمقدار {inp.weight_kg - 1.0:.2f} كجم للانتقال من standard_parcel إلى small_parcel. "
                       f"التوفير المتوقع: من {fees['fbn_fulfillment']:.2f} إلى {FBN_FULFILLMENT_FEE[mp][SizeTier.SMALL_PARCEL]:.2f} لكل وحدة.",
                potential_savings=savings,
            ))

    # Long-term storage warning
    if inp.inventory_age_days > 180:
        tips.append(OptimizationTip(
            category="inventory",
            tip_en=f"Inventory age {inp.inventory_age_days} days triggers long-term storage band. "
                   "Move deadstock via noon removals or run a clearance promo before month 7.",
            tip_ar=f"عمر المخزون {inp.inventory_age_days} يومًا يُفعّل شريحة التخزين طويل الأمد. "
                   "حرّك المخزون الراكد عبر خدمة الإزالة أو أطلق عرض تصفية قبل الشهر السابع.",
            potential_savings=fees["storage"] * 0.4,
        ))
    elif inp.inventory_age_days > 90:
        tips.append(OptimizationTip(
            category="inventory",
            tip_en="Inventory age > 90 days moves you into the peak storage band. "
                   "Run a promo or liquidate slow SKUs before Q4.",
            tip_ar="عمر المخزون > 90 يومًا ينقلك إلى شريحة التخزين في موسم الذروة. "
                   "أطلق عرضًا أو صفّق المخزون الراكد قبل الربع الرابع.",
            potential_savings=fees["storage"] * 0.2,
        ))

    # COD warning
    if inp.cod_enabled and inp.category in ("electronics", "mobiles", "home"):
        tips.append(OptimizationTip(
            category="payment",
            tip_en="COD enabled on a low-return category adds 2% friction with no conversion upside. "
                   "Switch to prepaid-only if category allows.",
            tip_ar="تفعيل الدفع عند الاستلام في فئة منخفضة المرتجعات يضيف 2٪ احتكاكًا دون رفع التحويل. "
                   "انتقل إلى الدفع المسبق فقط إذا كانت الفئة تسمح.",
            potential_savings=fees["cod_friction"],
        ))

    # Margin warning
    if net_margin < 0.08:
        tips.append(OptimizationTip(
            category="margin",
            tip_en=f"Net margin {net_margin * 100:.1f}% is below the 8% safety floor. "
                   "Renegotiate product cost, raise price, or pick a different SKU.",
            tip_ar=f"صافي هامش الربح {net_margin * 100:.1f}٪ أقل من عتبة الأمان 8٪. "
                   "أعد التفاوض على تكلفة المنتج أو ارفع السعر أو اختر وحدة حفظ مخزون مختلفة.",
            potential_savings=inp.selling_price * 0.05,
        ))

    # VAT cash-flow hint
    if mp in (Marketplace.KSA, Marketplace.EGY):
        tips.append(OptimizationTip(
            category="cashflow",
            tip_en="High-VAT market. Set aside the VAT line in a separate account; "
                   "late VAT filing penalties in KSA are severe.",
            tip_ar="سوق ذو ضريبة قيمة مضافة مرتفعة. اجعل بند ضريبة القيمة المضافة في حساب منفصل؛ "
                   "غرامات التأخر في تقديم الإقرارات في المملكة العربية السعودية شديدة.",
            potential_savings=0.0,
        ))

    return tips


# ============================================================
# Formatting
# ============================================================

def format_report_en(r: Dict) -> str:
    cur = r["currency"]
    f = r["fees"]
    lines = [
        "noon FBN Fee Calculation Report (Lite)",
        "",
        f"Product:        {r['name']} ({r['sku']})",
        f"Marketplace:    {r['marketplace']} ({cur})",
        f"Category:       {r['category']}",
        f"Size tier:      {r['size_tier']} (cubic: {r['cubic_meters']} m^3)",
        f"  {r['tier_reason']}",
        f"Selling price:  {cur} {r['selling_price']:.2f}",
        "",
        "-" * 60,
        f"{'Line item':<28}  {'Amount (' + cur + ')':>14}  {'%':>6}",
        "-" * 60,
        f"{'Product cost':<28}  {f['product_cost']:>14.2f}  {f['product_cost']/r['selling_price']*100:>5.1f}%",
        f"{'Commission (' + str(r['commission_rate_pct']) + '%)':<28}  {f['commission']:>14.2f}  {f['commission']/r['selling_price']*100:>5.1f}%",
        f"{'FBN fulfillment':<28}  {f['fbn_fulfillment']:>14.2f}  {f['fbn_fulfillment']/r['selling_price']*100:>5.1f}%",
        f"{'Storage (' + f['storage_band'] + ')':<28}  {f['storage']:>14.2f}  {f['storage']/r['selling_price']*100:>5.1f}%",
        f"{'Returns reserve (' + str(r['returns_rate_pct']) + '%)':<28}  {f['returns_reserve']:>14.2f}  {f['returns_reserve']/r['selling_price']*100:>5.1f}%",
        f"{'COD friction':<28}  {f['cod_friction']:>14.2f}  {f['cod_friction']/r['selling_price']*100:>5.1f}%",
        f"{'VAT carry (' + str(r['vat_rate_pct']) + '%)':<28}  {f['vat_carry']:>14.2f}  {f['vat_carry']/r['selling_price']*100:>5.1f}%",
        f"{'Inbound shipping':<28}  {f['inbound_shipping']:>14.2f}  {f['inbound_shipping']/r['selling_price']*100:>5.1f}%",
        f"{'Marketing / order':<28}  {f['marketing']:>14.2f}  {f['marketing']/r['selling_price']*100:>5.1f}%",
        "-" * 60,
        f"{'Total fees':<28}  {r['total_fees']:>14.2f}",
        f"{'Total cost':<28}  {r['total_cost']:>14.2f}",
        "-" * 60,
        f"{'Gross profit':<28}  {r['gross_profit']:>14.2f}  {r['gross_margin_pct']:>5.1f}%",
        f"{'Net profit':<28}  {r['net_profit']:>14.2f}  {r['net_margin_pct']:>5.1f}%",
        f"{'ROI':<28}  {r['roi_pct']:>13.1f}%",
        "-" * 60,
        f"Monthly units (assumed): {r['monthly_units_sold']}",
        f"Monthly net profit:      {cur} {r['monthly_net_profit']:.2f}",
    ]
    if r["optimization_tips"]:
        lines.extend([
            "",
            "-" * 60,
            "Optimization tips",
            "-" * 60,
        ])
        for i, t in enumerate(r["optimization_tips"], 1):
            lines.append(f"{i}. [{t['category']}] {t['tip_en']}")
            if t["potential_savings"] > 0:
                lines.append(f"   Potential saving: {cur} {t['potential_savings']:.2f} per unit")
            lines.append("")
    return "\n".join(lines)


def format_report_ar(r: Dict) -> str:
    cur = r["currency"]
    f = r["fees"]
    lines = [
        "تقرير حساب رسوم FBN في noon (نسخة لايت)",
        "",
        f"المنتج:           {r['name']} ({r['sku']})",
        f"السوق:            {r['marketplace']} ({cur})",
        f"الفئة:            {r['category']}",
        f"فئة الحجم:        {r['size_tier']} (الحجم: {r['cubic_meters']} م^3)",
        f"  {r['tier_reason']}",
        f"سعر البيع:        {cur} {r['selling_price']:.2f}",
        "",
        "-" * 60,
        f"{'البند':<28}  {'المبلغ (' + cur + ')':>14}  {'%':>6}",
        "-" * 60,
        f"{'تكلفة المنتج':<28}  {f['product_cost']:>14.2f}  {f['product_cost']/r['selling_price']*100:>5.1f}٪",
        f"{'العمولة (' + str(r['commission_rate_pct']) + '٪)':<28}  {f['commission']:>14.2f}  {f['commission']/r['selling_price']*100:>5.1f}٪",
        f"{'رسوم تنفيذ FBN':<28}  {f['fbn_fulfillment']:>14.2f}  {f['fbn_fulfillment']/r['selling_price']*100:>5.1f}٪",
        f"{'التخزين (' + f['storage_band'] + ')':<28}  {f['storage']:>14.2f}  {f['storage']/r['selling_price']*100:>5.1f}٪",
        f"{'احتياطي المرتجعات (' + str(r['returns_rate_pct']) + '٪)':<28}  {f['returns_reserve']:>14.2f}  {f['returns_reserve']/r['selling_price']*100:>5.1f}٪",
        f"{'احتكاك الدفع عند الاستلام':<28}  {f['cod_friction']:>14.2f}  {f['cod_friction']/r['selling_price']*100:>5.1f}٪",
        f"{'حمل ضريبة القيمة المضافة (' + str(r['vat_rate_pct']) + '٪)':<28}  {f['vat_carry']:>14.2f}  {f['vat_carry']/r['selling_price']*100:>5.1f}٪",
        f"{'شحن الوارد':<28}  {f['inbound_shipping']:>14.2f}  {f['inbound_shipping']/r['selling_price']*100:>5.1f}٪",
        f"{'التسويق / الطلب':<28}  {f['marketing']:>14.2f}  {f['marketing']/r['selling_price']*100:>5.1f}٪",
        "-" * 60,
        f"{'إجمالي الرسوم':<28}  {r['total_fees']:>14.2f}",
        f"{'إجمالي التكلفة':<28}  {r['total_cost']:>14.2f}",
        "-" * 60,
        f"{'الربح الإجمالي':<28}  {r['gross_profit']:>14.2f}  {r['gross_margin_pct']:>5.1f}٪",
        f"{'صافي الربح':<28}  {r['net_profit']:>14.2f}  {r['net_margin_pct']:>5.1f}٪",
        f"{'العائد على الاستثمار':<28}  {r['roi_pct']:>13.1f}٪",
        "-" * 60,
        f"الوحدات الشهرية (افتراض): {r['monthly_units_sold']}",
        f"صافي الربح الشهري:        {cur} {r['monthly_net_profit']:.2f}",
    ]
    if r["optimization_tips"]:
        lines.extend([
            "",
            "-" * 60,
            "نصائح التحسين",
            "-" * 60,
        ])
        for i, t in enumerate(r["optimization_tips"], 1):
            lines.append(f"{i}. [{t['category']}] {t['tip_ar']}")
            if t["potential_savings"] > 0:
                lines.append(f"   التوفير المتوقع: {cur} {t['potential_savings']:.2f} لكل وحدة")
            lines.append("")
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

SAMPLE_INPUT = {
    "sku": "DEMO-SKU",
    "name": "Wireless Earbuds",
    "length_cm": 12.0,
    "width_cm": 8.0,
    "height_cm": 4.0,
    "weight_kg": 0.18,
    "selling_price": 199.0,
    "product_cost": 35.0,
    "inbound_shipping_cost": 4.0,
    "category": "electronics",
    "marketplace": "noon-sa",
    "monthly_units_sold": 200,
    "inventory_days": 45,
    "inventory_age_days": 30,
    "cod_enabled": True,
    "marketing_per_order": 8.0,
}


def _read_stdin() -> str:
    """Read all of stdin if data is piped in; return empty string otherwise."""
    try:
        if not sys.stdin.isatty():
            return sys.stdin.read()
    except (OSError, ValueError):
        return ""
    return ""


def parse_args():
    """Return (product dict, output mode). Mode is 'en' / 'ar' / 'json'."""
    args = sys.argv[1:]
    if "--json" in args:
        mode = "json"
        args = [a for a in args if a != "--json"]
    elif "--ar" in args:
        mode = "ar"
        args = [a for a in args if a != "--ar"]
    else:
        mode = "en"

    # 1) Stdin JSON takes precedence (best for shell-escaping issues)
    stdin_payload = _read_stdin().strip()
    if stdin_payload:
        try:
            return json.loads(stdin_payload), mode
        except json.JSONDecodeError:
            pass  # fall through

    # 2) Positional JSON
    if args:
        payload = " ".join(args)
        try:
            return json.loads(payload), mode
        except json.JSONDecodeError:
            pass

    # 3) key=value fallback
    if args:
        data = {}
        for tok in args:
            if "=" in tok:
                k, v = tok.split("=", 1)
                data[k] = v
        for num_key in (
            "length_cm", "width_cm", "height_cm", "weight_kg",
            "selling_price", "product_cost", "inbound_shipping_cost",
            "marketing_per_order", "returns_rate_override",
        ):
            if num_key in data:
                try:
                    data[num_key] = float(data[num_key])
                except ValueError:
                    pass
        for int_key in ("monthly_units_sold", "inventory_days", "inventory_age_days"):
            if int_key in data:
                try:
                    data[int_key] = int(data[int_key])
                except ValueError:
                    pass
        if "cod_enabled" in data:
            data["cod_enabled"] = str(data["cod_enabled"]).lower() in ("1", "true", "yes")
        if data:
            return data, mode

    # 4) Default sample
    return dict(SAMPLE_INPUT), mode


def main():
    data, mode = parse_args()
    inp = ProductInput(**data)
    result = calculate(inp)
    if mode == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif mode == "ar":
        print(format_report_ar(result))
    else:
        print(format_report_en(result))


if __name__ == "__main__":
    main()