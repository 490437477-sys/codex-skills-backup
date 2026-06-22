#!/usr/bin/env python3
"""TEMU Niche Scorer.

Score a product niche opportunity on TEMU across US/UK/DE/FR/MX/BR/JP/KR
markets. Combines demand, AOV, compliance burden, fulfillment speed and
seasonality into a single 1-10 score with per-dimension breakdown.

Local-to-local (3P) fulfillment is weighted highest because TEMU boosts
visibility for faster local delivery. Semi-managed beats fully-managed for
the same reason. Heavy compliance markets (CE/PSE/KC) reduce the score.

Usage:
    python temu_niche_scorer.py --product "phone stand" --market US \\
        --aov 12.50 --aov-currency USD --monthly-demand 8000 \\
        --compliance medium --fulfillment semi_managed
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field

MARKETS = ("US", "UK", "DE", "FR", "MX", "BR", "JP", "KR")

COMPLIANCE_WEIGHT = {"low": 1.0, "medium": 0.75, "high": 0.5}

FULFILLMENT_WEIGHT = {
    "local": 1.0,
    "semi_managed": 0.75,
    "fully_managed": 0.55,
}

SEASONAL_BONUS = {
    "black_friday": 1.20,
    "christmas": 1.15,
    "mothers_day": 1.10,
    "fathers_day": 1.08,
    "easter": 1.05,
    "back_to_school": 1.10,
}


@dataclass
class NicheInput:
    product: str
    market: str
    aov: float
    aov_currency: str
    monthly_demand: int
    compliance: str
    fulfillment: str
    seasonality: str = "none"


@dataclass
class NicheScore:
    total: float
    dimensions: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)


def score_demand(demand: int) -> float:
    if demand >= 50000:
        return 10.0
    if demand >= 20000:
        return 8.5
    if demand >= 8000:
        return 7.0
    if demand >= 3000:
        return 5.5
    if demand >= 1000:
        return 4.0
    return 2.0


def score_aov(aov: float, currency: str) -> float:
    sweet_spots = {
        "USD": (10.0, 35.0), "EUR": (10.0, 35.0), "GBP": (8.0, 30.0),
        "MXN": (180.0, 600.0), "BRL": (50.0, 180.0),
        "JPY": (1500.0, 5000.0), "KRW": (14000.0, 45000.0),
    }
    lo, hi = sweet_spots.get(currency.upper(), (10.0, 35.0))
    if lo <= aov <= hi:
        return 9.0
    if aov < lo:
        return max(2.0, 9.0 - (lo - aov) / lo * 8.0)
    return max(3.0, 9.0 - (aov - hi) / hi * 6.0)


def score_market(market: str) -> float:
    base = {
        "US": 9.0, "UK": 8.0, "DE": 8.5, "FR": 7.5,
        "MX": 7.0, "BR": 7.5, "JP": 8.0, "KR": 7.5,
    }
    return base.get(market.upper(), 6.0)


def score_compliance(level: str) -> float:
    return 2.0 + 8.0 * COMPLIANCE_WEIGHT.get(level.lower(), 0.5)


def evaluate(niche: NicheInput) -> NicheScore:
    if niche.market.upper() not in MARKETS:
        raise ValueError(f"unsupported market: {niche.market}")
    if niche.compliance.lower() not in COMPLIANCE_WEIGHT:
        raise ValueError("compliance must be low/medium/high")
    if niche.fulfillment.lower() not in FULFILLMENT_WEIGHT:
        raise ValueError("fulfillment must be local/semi_managed/fully_managed")

    demand = score_demand(niche.monthly_demand)
    aov = score_aov(niche.aov, niche.aov_currency)
    market = score_market(niche.market)
    compliance = score_compliance(niche.compliance)
    fulfillment = 10.0 * FULFILLMENT_WEIGHT[niche.fulfillment.lower()]

    weighted = (
        demand * 0.30 + aov * 0.20 + market * 0.15
        + compliance * 0.15 + fulfillment * 0.20
    )
    season_mult = SEASONAL_BONUS.get(niche.seasonality.lower(), 1.0)
    total = min(10.0, round(weighted * season_mult, 2))

    notes = [
        f"demand={niche.monthly_demand} -> {demand}",
        f"aov={niche.aov} {niche.aov_currency} -> {aov}",
        f"fulfillment={niche.fulfillment} -> {fulfillment}",
        f"seasonality={niche.seasonality} x{season_mult}",
    ]
    return NicheScore(
        total=total,
        dimensions={
            "demand": round(demand, 2),
            "aov_fit": round(aov, 2),
            "market": round(market, 2),
            "compliance": round(compliance, 2),
            "fulfillment": round(fulfillment, 2),
        },
        notes=notes,
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="TEMU niche scorer")
    p.add_argument("--product", required=True)
    p.add_argument("--market", required=True, choices=MARKETS)
    p.add_argument("--aov", type=float, required=True)
    p.add_argument("--aov-currency", default="USD")
    p.add_argument("--monthly-demand", type=int, required=True)
    p.add_argument("--compliance", default="medium",
                   choices=list(COMPLIANCE_WEIGHT))
    p.add_argument("--fulfillment", default="semi_managed",
                   choices=list(FULFILLMENT_WEIGHT))
    p.add_argument("--seasonality", default="none",
                   choices=list(SEASONAL_BONUS) + ["none"])
    return p.parse_args()


def main() -> None:
    args = parse_args()
    niche = NicheInput(
        product=args.product, market=args.market, aov=args.aov,
        aov_currency=args.aov_currency, monthly_demand=args.monthly_demand,
        compliance=args.compliance, fulfillment=args.fulfillment,
        seasonality=args.seasonality,
    )
    result = evaluate(niche)
    print(f"Niche: {niche.product} ({niche.market})")
    print(f"TOTAL SCORE: {result.total} / 10")
    for k, v in result.dimensions.items():
        print(f"  {k:12s} = {v}")
    for n in result.notes:
        print(f"  note: {n}")


if __name__ == "__main__":
    main()
