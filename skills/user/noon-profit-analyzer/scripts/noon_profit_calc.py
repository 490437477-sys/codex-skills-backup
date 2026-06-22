#!/usr/bin/env python3
"""
noon Profit Waterfall Calculator.

Compute per-order net profit, contribution margin, and break-even ACOS
for a noon FBN listing. Supports SA, AE, and EG markets with optional
USD to local FX for cross-border sellers.

Waterfall = commission + COD fee + bounce cost + return cost
          + ad spend + landed cost + FBN fulfilment + FBN storage

Example:
    python noon_profit_calc.py --market .sa --retail-price 199 ^
        --commission-pct 12 --fbn-storage 2.5 --fbn-fulfilment 9 ^
        --cod-ratio 0.6 --bounce-rate 0.07 --return-rate 0.05 ^
        --landed-cost 65 --acos 18 --fx 3.75
"""
import argparse
import json
import sys
from dataclasses import dataclass


CURRENCY_SYMBOL = {
    ".sa": "SAR",
    ".ae": "AED",
    ".com": "EGP",
}


@dataclass
class ProfitInput:
    market: str
    retail_price: float
    noon_commission_pct: float
    fbn_storage_fee: float
    fbn_fulfilment_fee: float
    cod_ratio: float
    bounce_rate: float
    return_rate: float
    landed_cost: float
    acos: float
    fx_usd_to_local: float = 3.75
    cod_fee_pct: float = 0.02


def calc_profit(inp: ProfitInput) -> dict:
    revenue = inp.retail_price
    commission = revenue * (inp.noon_commission_pct / 100.0)
    cod_fee = revenue * inp.cod_ratio * inp.cod_fee_pct
    bounce_cost = revenue * inp.bounce_rate * 0.20
    return_cost = (inp.landed_cost + inp.fbn_fulfilment_fee) * inp.return_rate
    ad_cost = revenue * (inp.acos / 100.0)
    landed = inp.landed_cost
    fulfilment = inp.fbn_fulfilment_fee
    storage = inp.fbn_storage_fee
    total_costs = (
        commission
        + cod_fee
        + bounce_cost
        + return_cost
        + ad_cost
        + landed
        + fulfilment
        + storage
    )
    net = revenue - total_costs
    margin_pct = (net / revenue * 100.0) if revenue > 0 else 0.0
    if revenue > 0:
        non_ad_costs = (
            commission
            + cod_fee
            + bounce_cost
            + return_cost
            + landed
            + fulfilment
            + storage
        )
        be_ad_spend = revenue - non_ad_costs
        be_acos = max(0.0, be_ad_spend / revenue * 100.0)
    else:
        be_acos = 0.0
    return {
        "market": inp.market,
        "currency": CURRENCY_SYMBOL.get(inp.market, "USD"),
        "revenue": round(revenue, 2),
        "waterfall": {
            "commission": round(commission, 2),
            "cod_fee": round(cod_fee, 2),
            "bounce_cost": round(bounce_cost, 2),
            "return_cost": round(return_cost, 2),
            "ad_cost": round(ad_cost, 2),
            "landed_cost": round(landed, 2),
            "fbn_fulfilment": round(fulfilment, 2),
            "fbn_storage": round(storage, 2),
        },
        "total_costs": round(total_costs, 2),
        "net_profit_per_order": round(net, 2),
        "contribution_margin_pct": round(margin_pct, 2),
        "break_even_acos_pct": round(be_acos, 2),
        "fx_usd_to_local": inp.fx_usd_to_local,
    }


def from_json(payload: str) -> ProfitInput:
    return ProfitInput(**json.loads(payload))


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="noon_profit_calc",
        description="Compute per-order profit, margin, and break-even ACOS for noon.",
    )
    p.add_argument("--json", help="JSON payload with ProfitInput fields")
    p.add_argument("--market", choices=list(CURRENCY_SYMBOL), help="noon market")
    p.add_argument("--retail-price", type=float, help="Selling price in local currency")
    p.add_argument("--commission-pct", type=float, help="noon commission percent")
    p.add_argument("--fbn-storage", type=float, default=0.0)
    p.add_argument("--fbn-fulfilment", type=float, default=0.0)
    p.add_argument("--cod-ratio", type=float, default=0.5, help="Share of orders paid by COD (0-1)")
    p.add_argument("--bounce-rate", type=float, default=0.05, help="RTO/bounce rate (0-1)")
    p.add_argument("--return-rate", type=float, default=0.05, help="Customer return rate (0-1)")
    p.add_argument("--landed-cost", type=float, default=0.0)
    p.add_argument("--acos", type=float, default=15.0, help="Current advertising ACOS percent")
    p.add_argument("--fx", type=float, default=3.75, help="USD to local FX")
    p.add_argument("--cod-fee-pct", type=float, default=0.02)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.json:
        inp = from_json(args.json)
    elif args.market and args.retail_price is not None and args.commission_pct is not None:
        inp = ProfitInput(
            market=args.market,
            retail_price=args.retail_price,
            noon_commission_pct=args.commission_pct,
            fbn_storage_fee=args.fbn_storage,
            fbn_fulfilment_fee=args.fbn_fulfilment,
            cod_ratio=args.cod_ratio,
            bounce_rate=args.bounce_rate,
            return_rate=args.return_rate,
            landed_cost=args.landed_cost,
            acos=args.acos,
            fx_usd_to_local=args.fx,
            cod_fee_pct=args.cod_fee_pct,
        )
    elif not sys.stdin.isatty():
        inp = from_json(sys.stdin.read())
    else:
        build_parser().print_help()
        return 1
    print(json.dumps(calc_profit(inp), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
