#!/usr/bin/env python3
"""
noon PPC Bid Calculator - Core Engine

Calculates break-even ACoS, target ACoS, max CPC, and recommended bid tiers
for noon Sponsored Products campaigns on:
  - noon.sa (Saudi Arabia, SAR, VAT 15%)
  - noon.ae (United Arab Emirates, AED, VAT 5%)
  - noon.com / noon-eg (Egypt, EGP, VAT 14%)

Features:
  - Marketplace-aware defaults (currency, VAT)
  - Commission rate by category (electronics default 10%)
  - Returns reserve (default 5% of price, industry standard)
  - Optional COD friction
  - Break-even ACoS
  - Target ACoS and max CPC at given CVR
  - Recommended bid per campaign tier (Auto / Manual AR / Manual EN / Brand / B2B)
  - Daily clicks/orders/spend projection at given monthly budget
  - Bilingual output (en / ar) via --ar flag
  - JSON output via --json flag
  - CLI: --marketplace / --price / --cost / --commission / --returns-rate
        / --cod / --vat / --target-acos / --cvr / --monthly-budget
  - Or: positional JSON, stdin JSON, or key=value pairs

Disclaimer:
  noon Ads does not publish public CPC data. All bid recommendations are
  starting points based on MENA benchmark estimates. Validate with your own
  14-day A/B test before scaling.

Version: 1.0.0
Platform: noon
"""

import json
import sys
import io

# Force UTF-8 on stdout/stderr so Arabic output renders on Windows GBK consoles.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, io.UnsupportedOperation):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from dataclasses import dataclass, asdict
from typing import Optional, Dict


# ============================================================
# Marketplace Defaults
# ============================================================

MARKETPLACE_DEFAULTS = {
    "noon-sa": {"currency": "SAR", "vat": 0.15, "symbol": "SAR"},
    "noon-ae": {"currency": "AED", "vat": 0.05, "symbol": "AED"},
    "noon-eg": {"currency": "EGP", "vat": 0.14, "symbol": "EGP"},
    "noon-egypt": {"currency": "EGP", "vat": 0.14, "symbol": "EGP"},
}


# ============================================================
# Bid Tier Definitions
# ============================================================
# (lower_pct, upper_pct) of max_cpc for each campaign tier.

BID_TIERS = {
    "auto_discovery":  {"lower": 0.50, "upper": 0.60, "name_en": "Auto (Discovery)",
                        "name_ar": "\u062d\u0645\u0644\u0629 \u062a\u0644\u0642\u0627\u0626\u064a\u0629 (\u0627\u0643\u062a\u0634\u0627\u0641)"},
    "manual_ar":       {"lower": 0.60, "upper": 0.80, "name_en": "Manual AR (Arabic exact)",
                        "name_ar": "\u062d\u0645\u0644\u0629 \u064a\u062f\u0648\u064a\u0629 \u0639\u0631\u0628\u064a\u0629"},
    "manual_en":       {"lower": 0.50, "upper": 0.65, "name_en": "Manual EN (English exact)",
                        "name_ar": "\u062d\u0645\u0644\u0629 \u064a\u062f\u0648\u064a\u0629 \u0625\u0646\u062c\u0644\u064a\u0632\u064a\u0629"},
    "brand_defense":   {"lower": 0.20, "upper": 0.30, "name_en": "Brand Defense",
                        "name_ar": "\u062d\u0645\u0627\u064a\u0629 \u0627\u0644\u0639\u0644\u0627\u0645\u0629 \u0627\u0644\u062a\u062c\u0627\u0631\u064a\u0629"},
    "institutional":   {"lower": 1.00, "upper": 1.50, "name_en": "Institutional (B2B)",
                        "name_ar": "\u062d\u0645\u0644\u0629 \u0645\u0624\u0633\u0633\u0627\u062a (B2B)"},
}


# ============================================================
# Input / Output Models
# ============================================================

@dataclass
class BidInput:
    marketplace: str = "noon-sa"
    price: float = 399.0
    cost: float = 130.0
    commission: float = 0.10
    returns_rate: float = 0.05
    cod: bool = False
    cod_rate: float = 0.02
    vat: float = 0.15
    target_acos: float = 0.30
    cvr: float = 0.025
    monthly_budget: Optional[float] = None


SAMPLE_INPUT = {
    "marketplace": "noon-sa",
    "price": 399.0,
    "cost": 130.0,
    "commission": 0.10,
    "returns_rate": 0.05,
    "cod": False,
    "cod_rate": 0.02,
    "vat": 0.15,
    "target_acos": 0.30,
    "cvr": 0.025,
    "monthly_budget": None,
}


# ============================================================
# Calculation
# ============================================================

def calculate(inp: BidInput) -> Dict:
    """Run full bid calculation. Returns dict with all metrics + bid tiers."""
    # Resolve marketplace defaults
    mp = MARKETPLACE_DEFAULTS.get(inp.marketplace, MARKETPLACE_DEFAULTS["noon-sa"])
    currency = mp["currency"]
    symbol = mp["symbol"]

    # Per-sale fees (before ads)
    commission_amt = inp.commission * inp.price
    returns_amt = inp.returns_rate * inp.price  # returns_rate is % of price (industry standard)
    cod_amt = inp.cod_rate * inp.price if inp.cod else 0.0
    vat_amt = inp.vat * inp.price  # pass-through, included for display

    # Net per sale (before ads, after fees + cost)
    net_per_sale = inp.price - commission_amt - returns_amt - cod_amt - inp.cost

    # Break-even ACoS: at break-even, ad spend = net contribution
    break_even_acos = net_per_sale / inp.price if inp.price > 0 else 0.0

    # Max CPC at target ACoS and given CVR
    # 1 sale = 1/cvr clicks
    # ad spend per sale = target_acos * price
    # max CPC = target_acos * price * cvr
    max_cpc = inp.target_acos * inp.price * inp.cvr
    break_even_cpc = break_even_acos * inp.price * inp.cvr

    # Bid tiers
    bid_tiers = {}
    for key, tier in BID_TIERS.items():
        bid_tiers[key] = {
            "name_en": tier["name_en"],
            "name_ar": tier["name_ar"],
            "lower_bid": round(max_cpc * tier["lower"], 2),
            "upper_bid": round(max_cpc * tier["upper"], 2),
            "lower_pct_of_max": tier["lower"],
            "upper_pct_of_max": tier["upper"],
        }

    # Budget pacing
    pacing = None
    if inp.monthly_budget and inp.monthly_budget > 0:
        daily_budget = inp.monthly_budget / 30.0
        # Assume average CPC = 60% of max CPC (typical for mature campaign)
        avg_cpc = max_cpc * 0.60
        daily_clicks = daily_budget / avg_cpc if avg_cpc > 0 else 0
        daily_orders = daily_clicks * inp.cvr
        daily_ad_spend = daily_clicks * avg_cpc
        daily_revenue = daily_orders * inp.price
        pacing = {
            "monthly_budget": inp.monthly_budget,
            "daily_budget": round(daily_budget, 2),
            "avg_cpc_assumed": round(avg_cpc, 2),
            "daily_clicks": round(daily_clicks, 1),
            "daily_orders": round(daily_orders, 2),
            "daily_ad_spend": round(daily_ad_spend, 2),
            "daily_revenue": round(daily_revenue, 2),
            "projected_acos": round(daily_ad_spend / daily_revenue, 4) if daily_revenue > 0 else 0.0,
        }

    # Health verdict
    # ACoS = ad spend / revenue. Break-even ACoS = max ad spend / revenue.
    # If target ACoS < break-even ACoS, we have profit room after ads.
    if inp.target_acos < break_even_acos:
        verdict = "VIABLE"
        verdict_note = "Target ACoS is below break-even - room for profit after ads."
        verdict_note_ar = "\u0645\u0633\u062a\u0647\u062f\u0641 ACoS \u0623\u0642\u0644 \u0645\u0646 \u062d\u062f \u0627\u0644\u062a\u0639\u0627\u062f\u0644 - \u0645\u0633\u0627\u062d\u0629 \u0644\u0644\u0631\u0628\u062d \u0628\u0639\u062f \u0627\u0644\u0625\u0639\u0644\u0627\u0646\u0627\u062a"
    elif inp.target_acos < break_even_acos * 1.15:
        verdict = "TIGHT"
        verdict_note = "Target ACoS is within 15% of break-even - tight margin, monitor returns."
        verdict_note_ar = "\u0645\u0633\u062a\u0647\u062f\u0641 ACoS \u0636\u0645\u0646 15% \u0645\u0646 \u062d\u062f \u0627\u0644\u062a\u0639\u0627\u062f\u0644 - \u0647\u0627\u0645\u0634 \u0636\u064a\u0642\u060c \u0631\u0627\u0642\u0628 \u0627\u0644\u0645\u0631\u062a\u062c\u0639\u0627\u062a"
    else:
        verdict = "UNVIABLE"
        verdict_note = "Target ACoS exceeds break-even - either raise price, lower cost, or accept a loss."
        verdict_note_ar = "\u0645\u0633\u062a\u0647\u062f\u0641 ACoS \u064a\u062a\u062c\u0627\u0648\u0632 \u062d\u062f \u0627\u0644\u062a\u0639\u0627\u062f\u0644 - \u0627\u0631\u0641\u0639 \u0627\u0644\u0633\u0639\u0631 \u0623\u0648 \u0627\u062e\u0641\u0636 \u0627\u0644\u062a\u0643\u0644\u0641\u0629 \u0623\u0648 \u0627\u0642\u0628\u0644 \u062e\u0633\u0627\u0631\u0629"

    return {
        "inputs": {
            "marketplace": inp.marketplace,
            "currency": currency,
            "price": inp.price,
            "cost": inp.cost,
            "commission": inp.commission,
            "returns_rate": inp.returns_rate,
            "cod_enabled": inp.cod,
            "cod_rate": inp.cod_rate,
            "vat": inp.vat,
            "target_acos": inp.target_acos,
            "cvr": inp.cvr,
            "monthly_budget": inp.monthly_budget,
        },
        "per_sale_fees": {
            "commission": round(commission_amt, 2),
            "returns_reserve": round(returns_amt, 2),
            "cod": round(cod_amt, 2),
            "vat_pass_through": round(vat_amt, 2),
        },
        "profitability": {
            "net_per_sale_before_ads": round(net_per_sale, 2),
            "break_even_acos": round(break_even_acos, 4),
            "break_even_cpc": round(break_even_cpc, 2),
            "target_acos": inp.target_acos,
            "max_cpc_at_target": round(max_cpc, 2),
            "verdict": verdict,
            "verdict_note": verdict_note,
            "verdict_note_ar": verdict_note_ar,
        },
        "bid_tiers": bid_tiers,
        "budget_pacing": pacing,
    }


# ============================================================
# Output Formatters
# ============================================================

def format_report_en(result: Dict) -> str:
    inp = result["inputs"]
    fees = result["per_sale_fees"]
    prof = result["profitability"]
    tiers = result["bid_tiers"]
    pacing = result["budget_pacing"]
    cur = inp["currency"]

    lines = []
    lines.append("=" * 64)
    lines.append("  noon's PPC Bid Calculator - Report")
    lines.append("=" * 64)
    lines.append("")
    lines.append(f"  Marketplace:        {inp['marketplace']} ({cur})")
    lines.append(f"  Selling price:      {inp['price']:.2f} {cur}")
    lines.append(f"  Landed cost:        {inp['cost']:.2f} {cur}")
    lines.append(f"  Commission:         {inp['commission']*100:.1f}%  ({fees['commission']:.2f} {cur})")
    lines.append(f"  Returns reserve:    {inp['returns_rate']*100:.1f}% of price  ({fees['returns_reserve']:.2f} {cur})")
    lines.append(f"  COD:                {'on' if inp['cod_enabled'] else 'off'}  ({fees['cod']:.2f} {cur})")
    lines.append(f"  VAT (pass-through): {inp['vat']*100:.1f}%  ({fees['vat_pass_through']:.2f} {cur})")
    lines.append("")
    lines.append("-" * 64)
    lines.append("  Profitability")
    lines.append("-" * 64)
    lines.append(f"  Net per sale (before ads):  {prof['net_per_sale_before_ads']:.2f} {cur}")
    lines.append(f"  Break-even ACoS:            {prof['break_even_acos']*100:.2f}%")
    lines.append(f"  Break-even CPC (@ {inp['cvr']*100:.1f}% CVR):  {prof['break_even_cpc']:.2f} {cur}")
    lines.append(f"  Target ACoS:                {prof['target_acos']*100:.2f}%")
    lines.append(f"  Max CPC at target:          {prof['max_cpc_at_target']:.2f} {cur}")
    lines.append("")
    lines.append(f"  Verdict: {prof['verdict']}  -  {prof['verdict_note']}")
    lines.append("")
    lines.append("-" * 64)
    lines.append("  Recommended Bids by Campaign Tier")
    lines.append("-" * 64)
    for key, tier in tiers.items():
        lines.append(f"  [{tier['name_en']}]")
        lines.append(f"    Range: {tier['lower_bid']:.2f} - {tier['upper_bid']:.2f} {cur}")
        lines.append(f"    ({tier['lower_pct_of_max']*100:.0f}-{tier['upper_pct_of_max']*100:.0f}% of max CPC)")
        lines.append("")
    if pacing:
        lines.append("-" * 64)
        lines.append("  Budget Pacing (monthly_budget given)")
        lines.append("-" * 64)
        lines.append(f"  Monthly budget:     {pacing['monthly_budget']:.2f} {cur}")
        lines.append(f"  Daily budget:       {pacing['daily_budget']:.2f} {cur}")
        lines.append(f"  Avg CPC assumed:    {pacing['avg_cpc_assumed']:.2f} {cur}")
        lines.append(f"  Daily clicks:       {pacing['daily_clicks']:.1f}")
        lines.append(f"  Daily orders:       {pacing['daily_orders']:.2f}")
        lines.append(f"  Daily ad spend:     {pacing['daily_ad_spend']:.2f} {cur}")
        lines.append(f"  Daily revenue:      {pacing['daily_revenue']:.2f} {cur}")
        lines.append(f"  Projected ACoS:     {pacing['projected_acos']*100:.2f}%")
        lines.append("")
    lines.append("=" * 64)
    lines.append("  Tip: Start at the LOWER end of each tier, scale up after 14d")
    lines.append("=" * 64)
    return "\n".join(lines)


def format_report_ar(result: Dict) -> str:
    inp = result["inputs"]
    fees = result["per_sale_fees"]
    prof = result["profitability"]
    tiers = result["bid_tiers"]
    pacing = result["budget_pacing"]
    cur = inp["currency"]

    lines = []
    lines.append("=" * 64)
    lines.append("  \u062d\u0627\u0633\u0628 \u0639\u0631\u0648\u0636 noon - \u062a\u0642\u0631\u064a\u0631")
    lines.append("=" * 64)
    lines.append("")
    lines.append(f"  \u0627\u0644\u0633\u0648\u0642:             {inp['marketplace']} ({cur})")
    lines.append(f"  \u0633\u0639\u0631 \u0627\u0644\u0628\u064a\u0639:        {inp['price']:.2f} {cur}")
    lines.append(f"  \u0627\u0644\u062a\u0643\u0644\u0641\u0629:           {inp['cost']:.2f} {cur}")
    lines.append(f"  \u0627\u0644\u0639\u0645\u0648\u0644\u0629:         {inp['commission']*100:.1f}%  ({fees['commission']:.2f} {cur})")
    lines.append(f"  \u0627\u062d\u062a\u064a\u0627\u0637\u064a \u0627\u0644\u0645\u0631\u062a\u062c\u0639\u0627\u062a:  {inp['returns_rate']*100:.1f}% \u0645\u0646 \u0627\u0644\u0633\u0639\u0631  ({fees['returns_reserve']:.2f} {cur})")
    lines.append(f"  \u0627\u0644\u062f\u0641\u0639 \u0639\u0646\u062f \u0627\u0644\u0627\u0633\u062a\u0644\u0627\u0645:  {'\u0645\u0641\u0639\u0644' if inp['cod_enabled'] else '\u0645\u0639\u0637\u0644'}  ({fees['cod']:.2f} {cur})")
    lines.append(f"  \u0636\u0631\u064a\u0628\u0629 \u0627\u0644\u0642\u064a\u0645\u0629 \u0627\u0644\u0645\u0636\u0627\u0641\u0629:   {inp['vat']*100:.1f}%  ({fees['vat_pass_through']:.2f} {cur})")
    lines.append("")
    lines.append("-" * 64)
    lines.append("  \u0627\u0644\u0631\u0628\u062d\u064a\u0629")
    lines.append("-" * 64)
    lines.append(f"  \u0635\u0627\u0641\u064a \u0627\u0644\u0631\u0628\u062d \u0644\u0643\u0644 \u0628\u064a\u0639\u0629:   {prof['net_per_sale_before_ads']:.2f} {cur}")
    lines.append(f"  ACoS \u062d\u062f \u0627\u0644\u062a\u0639\u0627\u062f\u0644:           {prof['break_even_acos']*100:.2f}%")
    lines.append(f"  CPC \u062d\u062f \u0627\u0644\u062a\u0639\u0627\u062f\u0644:           {prof['break_even_cpc']:.2f} {cur}")
    lines.append(f"  ACoS \u0627\u0644\u0645\u0633\u062a\u0647\u062f\u0641:            {prof['target_acos']*100:.2f}%")
    lines.append(f"  CPC \u0627\u0644\u0623\u0642\u0635\u0649:                 {prof['max_cpc_at_target']:.2f} {cur}")
    lines.append("")
    lines.append(f"  \u0627\u0644\u062d\u0643\u0645: {prof['verdict']}  -  {prof['verdict_note_ar']}")
    lines.append("")
    lines.append("-" * 64)
    lines.append("  \u0639\u0631\u0648\u0636 \u0627\u0644\u0645\u0632\u0627\u062f \u0627\u0644\u0645\u0648\u0635\u0649 \u0628\u0647\u0627")
    lines.append("-" * 64)
    for key, tier in tiers.items():
        lines.append(f"  [{tier['name_ar']}]")
        lines.append(f"    \u0627\u0644\u0646\u0637\u0627\u0642: {tier['lower_bid']:.2f} - {tier['upper_bid']:.2f} {cur}")
        lines.append(f"    ({tier['lower_pct_of_max']*100:.0f}-{tier['upper_pct_of_max']*100:.0f}% \u0645\u0646 \u0623\u0642\u0635\u0649 CPC)")
        lines.append("")
    if pacing:
        lines.append("-" * 64)
        lines.append("  \u062a\u0648\u0632\u064a\u0639 \u0627\u0644\u0645\u064a\u0632\u0627\u0646\u064a\u0629")
        lines.append("-" * 64)
        lines.append(f"  \u0627\u0644\u0645\u064a\u0632\u0627\u0646\u064a\u0629 \u0627\u0644\u0634\u0647\u0631\u064a\u0629:  {pacing['monthly_budget']:.2f} {cur}")
        lines.append(f"  \u0627\u0644\u0645\u064a\u0632\u0627\u0646\u064a\u0629 \u0627\u0644\u064a\u0648\u0645\u064a\u0629:    {pacing['daily_budget']:.2f} {cur}")
        lines.append(f"  CPC \u0627\u0644\u0645\u062a\u0648\u0633\u0637:           {pacing['avg_cpc_assumed']:.2f} {cur}")
        lines.append(f"  \u0627\u0644\u0646\u0642\u0631 \u0627\u0644\u064a\u0648\u0645\u064a:         {pacing['daily_clicks']:.1f}")
        lines.append(f"  \u0627\u0644\u0637\u0644\u0628\u0627\u062a \u0627\u0644\u064a\u0648\u0645\u064a\u0629:        {pacing['daily_orders']:.2f}")
        lines.append(f"  \u0625\u0646\u0641\u0627\u0642 \u0627\u0644\u0625\u0639\u0644\u0627\u0646:      {pacing['daily_ad_spend']:.2f} {cur}")
        lines.append(f"  \u0627\u0644\u0625\u064a\u0631\u0627\u062f\u0627\u062a \u0627\u0644\u064a\u0648\u0645\u064a\u0629:    {pacing['daily_revenue']:.2f} {cur}")
        lines.append(f"  ACoS \u0627\u0644\u0645\u062a\u0648\u0642\u0639:        {pacing['projected_acos']*100:.2f}%")
        lines.append("")
    lines.append("=" * 64)
    lines.append("  \u0646\u0635\u064a\u062d\u0629: \u0627\u0628\u062f\u0623 \u0645\u0646 \u062d\u062f \u0623\u062f\u0646\u0649 \u0641\u064a \u0643\u0644 \u0641\u0626\u0629\u060c \u0648\u0627\u0631\u0641\u0639 \u0628\u0639\u062f 14 \u064a\u0648\u0645\u064b\u0627")
    lines.append("=" * 64)
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def _read_stdin() -> str:
    """Read all of stdin if data is piped in; return empty string otherwise."""
    try:
        if not sys.stdin.isatty():
            return sys.stdin.read()
    except (OSError, ValueError):
        return ""
    return ""


def parse_args():
    """Return (BidInput, output_mode). Mode is 'en' / 'ar' / 'json'."""
    args = sys.argv[1:]
    if "--json" in args:
        mode = "json"
        args = [a for a in args if a != "--json"]
    elif "--ar" in args:
        mode = "ar"
        args = [a for a in args if a != "--ar"]
    else:
        mode = "en"

    # 1) Stdin JSON takes precedence
    stdin_payload = _read_stdin().strip()
    if stdin_payload:
        try:
            return BidInput(**json.loads(stdin_payload)), mode
        except (json.JSONDecodeError, TypeError):
            pass

    # 2) Positional JSON
    if args and args[0].startswith("{"):
        try:
            return BidInput(**json.loads(" ".join(args))), mode
        except (json.JSONDecodeError, TypeError):
            pass

    # 3) key=value or --key value pairs
    data = dict(SAMPLE_INPUT)
    i = 0
    while i < len(args):
        tok = args[i]
        if tok.startswith("--"):
            key = tok[2:].replace("-", "_")
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                data[key] = args[i + 1]
                i += 2
            else:
                # boolean flag
                data[key] = True
                i += 1
        elif "=" in tok:
            k, v = tok.split("=", 1)
            k = k.replace("-", "_")
            data[k] = v
            i += 1
        else:
            i += 1

    # Coerce types
    for num_key in ("price", "cost", "commission", "returns_rate", "cod_rate",
                    "vat", "target_acos", "cvr", "monthly_budget"):
        if num_key in data and data[num_key] is not None:
            try:
                data[num_key] = float(data[num_key])
            except (ValueError, TypeError):
                pass
    if "cod" in data:
        data["cod"] = str(data["cod"]).lower() in ("1", "true", "yes", "on")

    return BidInput(**data), mode


def main():
    inp, mode = parse_args()
    # If marketplace is given, override VAT default from marketplace
    if inp.marketplace in MARKETPLACE_DEFAULTS and inp.vat == SAMPLE_INPUT["vat"]:
        # user did not override VAT, use marketplace default
        pass  # actually we set vat=0.15 in sample, so this check is moot
    result = calculate(inp)
    if mode == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif mode == "ar":
        print(format_report_ar(result))
    else:
        print(format_report_en(result))


if __name__ == "__main__":
    main()
