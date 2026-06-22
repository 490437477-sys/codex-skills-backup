#!/usr/bin/env python3
"""TEMU Profit Calculator.

Compute per-order net profit, contribution margin, break-even ACOS, and a
nuclear-price-pressure score for a TEMU listing across all three
fulfillment modes (fully_managed, semi_managed, local). Handles multi-
currency landed cost and TEMU-specific risk: forced price-down rounds,
15-25% returns, 5-10% category commission plus base service fee.

Usage:
    python temu_profit_calc.py --price 19.99 --currency USD \\
        --commission 0.07 --base-fee 1.20 --fulfillment semi_managed \\
        --return-rate 0.18 --landed-cost 4.50 --exchange 1.0 \\
        --advertising-share 0.10
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

FULFILLMENT_FEE = {
    "fully_managed": 0.08,
    "semi_managed": 0.12,
    "local": 0.06,
}

RETURN_DEDUCTION_RATE = {
    "fully_managed": 0.20,
    "semi_managed": 0.18,
    "local": 0.15,
}


@dataclass
class ProfitBreakdown:
    revenue: float
    commission_fee: float
    base_fee: float
    fulfillment_fee: float
    return_cost: float
    landed_cost: float
    ad_cost: float
    net_profit: float
    margin: float
    break_even_acos: float
    price_pressure: float


def calc(
    price: float,
    currency: str,
    commission: float,
    base_fee: float,
    fulfillment: str,
    return_rate: float,
    landed_cost: float,
    exchange: float,
    ad_share: float,
) -> ProfitBreakdown:
    if fulfillment not in FULFILLMENT_FEE:
        raise ValueError(f"fulfillment must be one of {list(FULFILLMENT_FEE)}")
    if not 0 <= commission <= 0.20:
        raise ValueError("commission rate looks unrealistic (0-0.20)")
    if not 0 <= return_rate <= 1.0:
        raise ValueError("return_rate must be 0-1")

    price_local = price * exchange
    landed_local = landed_cost * exchange

    commission_fee = price_local * commission
    fulfillment_fee = price_local * FULFILLMENT_FEE[fulfillment]
    return_cost = price_local * return_rate * RETURN_DEDUCTION_RATE[fulfillment]
    ad_cost = price_local * ad_share

    cogs_and_fees = (
        commission_fee + base_fee + fulfillment_fee
        + return_cost + landed_local + ad_cost
    )
    net = price_local - cogs_and_fees
    margin = net / price_local if price_local > 0 else 0.0

    ad_room = ad_cost / price_local if price_local > 0 else 0.0
    break_even_acos = ad_room + max(0.0, -margin)

    pressure_inputs = [
        1.0 - margin,
        return_rate,
        RETURN_DEDUCTION_RATE[fulfillment],
        FULFILLMENT_FEE[fulfillment] * 4,
    ]
    pressure = round(sum(pressure_inputs) / len(pressure_inputs) * 10, 2)
    pressure = max(1.0, min(10.0, pressure))

    return ProfitBreakdown(
        revenue=round(price_local, 2),
        commission_fee=round(commission_fee, 2),
        base_fee=round(base_fee, 2),
        fulfillment_fee=round(fulfillment_fee, 2),
        return_cost=round(return_cost, 2),
        landed_cost=round(landed_local, 2),
        ad_cost=round(ad_cost, 2),
        net_profit=round(net, 2),
        margin=round(margin, 4),
        break_even_acos=round(break_even_acos, 4),
        price_pressure=pressure,
    )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="TEMU profit calculator")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--currency", default="USD")
    p.add_argument("--commission", type=float, required=True,
                   help="TEMU category commission 0.05-0.10")
    p.add_argument("--base-fee", type=float, default=0.0,
                   help="flat per-order service fee")
    p.add_argument("--fulfillment", required=True,
                   choices=list(FULFILLMENT_FEE))
    p.add_argument("--return-rate", type=float, default=0.18)
    p.add_argument("--landed-cost", type=float, required=True,
                   help="factory+ship+pack in USD base currency")
    p.add_argument("--exchange", type=float, default=1.0,
                   help="local currency per USD")
    p.add_argument("--advertising-share", type=float, default=0.0,
                   help="ad cost as fraction of revenue")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    r = calc(
        price=args.price,
        currency=args.currency,
        commission=args.commission,
        base_fee=args.base_fee,
        fulfillment=args.fulfillment,
        return_rate=args.return_rate,
        landed_cost=args.landed_cost,
        exchange=args.exchange,
        ad_share=args.advertising_share,
    )
    print(f"Revenue:        {r.revenue:>9.2f} {args.currency}")
    print(f"Commission:     {r.commission_fee:>9.2f}")
    print(f"Base fee:       {r.base_fee:>9.2f}")
    print(f"Fulfillment:    {r.fulfillment_fee:>9.2f}")
    print(f"Return cost:    {r.return_cost:>9.2f}")
    print(f"Landed cost:    {r.landed_cost:>9.2f}")
    print(f"Ad cost:        {r.ad_cost:>9.2f}")
    print(f"NET PROFIT:     {r.net_profit:>9.2f}")
    print(f"Contribution:   {r.margin*100:>8.2f} %")
    print(f"Break-even ACOS:{r.break_even_acos*100:>8.2f} %")
    print(f"Price pressure: {r.price_pressure:>9.2f} / 10")


if __name__ == "__main__":
    main()
