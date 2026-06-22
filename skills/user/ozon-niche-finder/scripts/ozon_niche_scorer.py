#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ozon niche scorer (1-10) for Ozon.ru / Ozon.kz / Ozon.by.

Score = Demand*0.30 + Supply_gap*0.25 + Margin*0.20
      + Compliance_ease*0.15 + FBO_FBS_fit*0.10

Usage:
  python ozon_niche_scorer.py "wireless earbuds" --aov 2990 --demand 8500 --compliance medium --fulfillment fbs
  python ozon_niche_scorer.py "car seat" --aov 12500 --demand 3200 --compliance high --fulfillment fbo --json
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict, field

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


MARKET_VAT = {"ru": 0.20, "kz": 0.12, "by": 0.20}
MARKET_CCY = {"ru": "RUB", "kz": "KZT", "by": "BYN"}
COMP_BASE = {"low": 8.5, "medium": 6.0, "high": 3.0}
DEMAND_BENCH = 15000


@dataclass
class NicheInput:
    product_name: str
    marketplace: str
    aov: float
    monthly_demand: int
    compliance: str
    fulfillment: str
    active_skus: int = 80
    margin_pct: float = 0.35
    fx_buffer_pct: float = 0.10


@dataclass
class NicheScore:
    product_name: str
    marketplace: str
    currency: str
    total: float
    band: str
    demand: float
    supply_gap: float
    margin: float
    compliance_ease: float
    fbo_fbs_fit: float
    notes: list = field(default_factory=list)


def score_demand(n: int) -> float:
    """15k+ monthly searches = 10/10. Sub-linear credit for small markets."""
    if n <= 0:
        return 1.0
    r = n / float(DEMAND_BENCH)
    return 10.0 if r >= 1.0 else round(1.0 + 9.0 * (r ** 0.5), 2)


def score_supply(skus: int) -> float:
    """<50 SKUs = blue ocean (10/10), >1200 = commodity (1/10)."""
    if skus < 50: return 10.0
    if skus < 150: return 8.0
    if skus < 300: return 6.0
    if skus < 600: return 4.0
    if skus < 1200: return 2.5
    return 1.0


def score_margin(margin_pct: float, fx_buf: float, vat: float) -> float:
    """Net of VAT drag and ruble volatility buffer. 35%+ = 10/10."""
    net = margin_pct - vat * 0.10 - fx_buf
    if net <= 0:
        return 1.0
    return round(min(10.0, 1.0 + 9.0 * (net / 0.35)), 2)


def score_compliance(level: str) -> float:
    """EAC friction proxy. Low=8.5 / Medium=6.0 / High=3.0."""
    return COMP_BASE.get(level.lower(), 5.0)


def score_fulfillment(model: str, aov: float) -> float:
    """FBS=8.0 default, FBO=7.0. High AOV under FBS gets a +1.0 bump."""
    base = 8.0 if model.lower() == "fbs" else 7.0
    if model.lower() == "fbs" and aov > 8000:
        base = min(10.0, base + 1.0)
    return base


def evaluate(niche: NicheInput) -> NicheScore:
    vat = MARKET_VAT.get(niche.marketplace.lower(), 0.20)
    ccy = MARKET_CCY.get(niche.marketplace.lower(), "RUB")
    demand = score_demand(niche.monthly_demand)
    supply = score_supply(niche.active_skus)
    margin = score_margin(niche.margin_pct, niche.fx_buffer_pct, vat)
    compliance = score_compliance(niche.compliance)
    fulfill = score_fulfillment(niche.fulfillment, niche.aov)
    total = round(demand * 0.30 + supply * 0.25 + margin * 0.20
                  + compliance * 0.15 + fulfill * 0.10, 2)
    band = "TOP_TIER" if total >= 7.5 else ("VIABLE" if total >= 6.0 else "SKIP")
    notes = []
    if compliance <= 4.0:
        notes.append("EAC compliance heavy - budget 4-8 weeks and a local partner.")
    if margin <= 4.0:
        notes.append("Margin thin after VAT + FX buffer - raise AOV or cut landed cost.")
    if niche.marketplace == "ru" and niche.fx_buffer_pct < 0.10:
        notes.append("Ruble buffer below 10% - add buffer for recent RUB swings.")
    return NicheScore(
        product_name=niche.product_name, marketplace=niche.marketplace,
        currency=ccy, total=total, band=band, demand=demand,
        supply_gap=supply, margin=margin, compliance_ease=compliance,
        fbo_fbs_fit=fulfill, notes=notes,
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Score an Ozon niche 1-10 across 5 dimensions.")
    p.add_argument("product_name", help="Product name in Russian or English")
    p.add_argument("--marketplace", choices=["ru", "kz", "by"], default="ru")
    p.add_argument("--aov", type=float, default=2500.0, help="AOV in local currency")
    p.add_argument("--demand", type=int, default=3000, help="Monthly demand (Yandex + Ozon)")
    p.add_argument("--skus", type=int, default=120, help="Active SKU count on Ozon")
    p.add_argument("--compliance", choices=["low", "medium", "high"], default="medium")
    p.add_argument("--fulfillment", choices=["fbo", "fbs"], default="fbs")
    p.add_argument("--margin", type=float, default=0.35, help="Gross margin before ads (0-1)")
    p.add_argument("--fx-buffer", type=float, default=0.10, help="Ruble buffer (0-0.20)")
    p.add_argument("--json", action="store_true", help="Emit JSON only")
    return p


def render(score: NicheScore, niche: NicheInput) -> str:
    out = [
        "Ozon Niche Score: " + score.product_name,
        "Marketplace: Ozon." + score.marketplace + " (" + score.currency + ")",
        "AOV: " + str(round(niche.aov, 2)) + " " + score.currency,
        "", "Total: " + str(score.total) + " / 10  -> " + score.band, "", "Breakdown:",
        "  Demand       (0.30): " + str(score.demand),
        "  Supply_gap   (0.25): " + str(score.supply_gap),
        "  Margin       (0.20): " + str(score.margin),
        "  Compliance   (0.15): " + str(score.compliance_ease),
        "  FBO_FBS_fit  (0.10): " + str(score.fbo_fbs_fit),
    ]
    if score.notes:
        out.append(""); out.append("Notes:")
        out.extend("  - " + n for n in score.notes)
    return "\n".join(out)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    niche = NicheInput(
        product_name=args.product_name, marketplace=args.marketplace,
        aov=args.aov, monthly_demand=args.demand,
        compliance=args.compliance, fulfillment=args.fulfillment,
        active_skus=args.skus, margin_pct=args.margin, fx_buffer_pct=args.fx_buffer,
    )
    score = evaluate(niche)
    if args.json:
        blob = asdict(score); blob["inputs"] = asdict(niche)
        print(json.dumps(blob, ensure_ascii=False, indent=2))
    else:
        print(render(score, niche))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
