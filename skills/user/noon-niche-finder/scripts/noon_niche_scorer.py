#!/usr/bin/env python3
"""
noon Niche Scorer.

Score a product niche opportunity on the noon marketplace (1-10).
Five weighted dimensions: Demand, Supply gap, Margin, Compliance ease,
FBO/FBS fit. Accepts CLI flags or a JSON payload via --json or stdin.

Score = Demand*0.30 + Supply_gap*0.25 + Margin*0.20
      + Compliance_ease*0.15 + FBO_FBS_fit*0.10

Example:
    python noon_niche_scorer.py --product "Air Fryer 5L" --market .sa ^
        --aov 250 --monthly-demand 8000 --compliance low ^
        --fbn-tier standard --competitor-count 25 --landed-cost 90
"""
import argparse
import json
import sys
from dataclasses import dataclass


COMPLIANCE_WEIGHT = {
    "low": 1.0,
    "medium": 0.6,
    "high": 0.25,
}
FBN_TIER_SCORE = {
    "standard": 0.7,
    "premium": 0.9,
    "oversized": 0.4,
}
MARKETS = [".sa", ".ae", ".com"]


@dataclass
class NicheInput:
    product: str
    market: str
    aov: float
    monthly_demand: int
    compliance: str
    fbn_tier: str
    competitor_count: int = 30
    landed_cost: float = 0.0


def demand_score(monthly_demand: int) -> float:
    if monthly_demand < 100:
        return 1.0
    if monthly_demand < 500:
        return 4.0
    if monthly_demand < 2000:
        return 7.0
    if monthly_demand < 10000:
        return 9.0
    return 8.0


def supply_gap_score(monthly_demand: int, competitor_count: int) -> float:
    if competitor_count <= 0:
        return 10.0
    ratio = monthly_demand / max(competitor_count, 1)
    if ratio > 200:
        return 10.0
    if ratio > 100:
        return 8.0
    if ratio > 50:
        return 6.0
    if ratio > 20:
        return 4.0
    return 2.0


def margin_score(aov: float, landed_cost: float) -> float:
    if aov <= 0:
        return 0.0
    if landed_cost <= 0:
        return 5.0
    margin_pct = (aov - landed_cost) / aov
    if margin_pct >= 0.5:
        return 10.0
    if margin_pct >= 0.35:
        return 8.0
    if margin_pct >= 0.25:
        return 6.0
    if margin_pct >= 0.15:
        return 4.0
    return 2.0


def score_niche(inp: NicheInput) -> dict:
    d = demand_score(inp.monthly_demand)
    s = supply_gap_score(inp.monthly_demand, inp.competitor_count)
    m = margin_score(inp.aov, inp.landed_cost)
    c = COMPLIANCE_WEIGHT.get(inp.compliance.lower(), 0.5) * 10.0
    f = FBN_TIER_SCORE.get(inp.fbn_tier.lower(), 0.5) * 10.0
    total = d * 0.30 + s * 0.25 + m * 0.20 + c * 0.15 + f * 0.10
    return {
        "product": inp.product,
        "market": inp.market,
        "total_score": round(total, 2),
        "breakdown": {
            "Demand": round(d, 2),
            "Supply_gap": round(s, 2),
            "Margin": round(m, 2),
            "Compliance_ease": round(c, 2),
            "FBO_FBS_fit": round(f, 2),
        },
        "verdict": "go" if total >= 7 else "test" if total >= 5 else "skip",
    }


def from_json(payload: str) -> NicheInput:
    return NicheInput(**json.loads(payload))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="noon_niche_scorer",
        description="Score a noon niche opportunity (1-10) across 5 dimensions.",
    )
    p.add_argument("--json", help="JSON payload with NicheInput fields")
    p.add_argument("--product", help="Product name")
    p.add_argument("--market", choices=MARKETS, help="noon market")
    p.add_argument("--aov", type=float, help="Average order value in local currency")
    p.add_argument("--monthly-demand", type=int, help="Estimated monthly search demand")
    p.add_argument("--compliance", choices=list(COMPLIANCE_WEIGHT), help="Compliance risk")
    p.add_argument("--fbn-tier", choices=list(FBN_TIER_SCORE), help="FBN tier")
    p.add_argument("--competitor-count", type=int, default=30, help="Active competitor listings")
    p.add_argument("--landed-cost", type=float, default=0.0, help="Landed unit cost (optional)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.json:
        inp = from_json(args.json)
    elif (
        args.product
        and args.market
        and args.aov is not None
        and args.monthly_demand
        and args.compliance
        and args.fbn_tier
    ):
        inp = NicheInput(
            product=args.product,
            market=args.market,
            aov=args.aov,
            monthly_demand=args.monthly_demand,
            compliance=args.compliance,
            fbn_tier=args.fbn_tier,
            competitor_count=args.competitor_count,
            landed_cost=args.landed_cost,
        )
    elif not sys.stdin.isatty():
        inp = from_json(sys.stdin.read())
    else:
        build_parser().print_help()
        return 1
    print(json.dumps(score_niche(inp), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
