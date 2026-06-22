#!/usr/bin/env python3
"""Mercado Libre profit calculator.

Compute the per-order net profit, contribution margin, break-even ACOS,
and the cost of offering cuotas sin interes through Mercado Pago for a
Mercado Libre listing. Supports MLM, MLB, MLC, MCO, MLA.

Usage:
    python mercado_profit_calc.py --price 1299 --commission 0.13 ^
        --envios 129 --full 25 --cuotas 6 --market MLM ^
        --landed 480 --acos 0.15
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass


CUOTAS_RATE: dict[int, float] = {
    1: 0.0,
    3: 0.045,
    6: 0.080,
    12: 0.140,
}

MARKET_IVA: dict[str, float] = {
    "MLM": 0.16,
    "MLB": 0.17,
    "MLC": 0.19,
    "MCO": 0.19,
    "MLA": 0.21,
}


@dataclass
class ProfitInput:
    price: float
    commission: float
    envios: float
    full_storage: float
    cuotas: int
    market: str
    landed: float
    acos: float


@dataclass
class ProfitResult:
    revenue_net: float = 0.0
    commission_cost: float = 0.0
    cuotas_cost: float = 0.0
    iva_net: float = 0.0
    ads_cost: float = 0.0
    net_profit: float = 0.0
    margin: float = 0.0
    break_even_acos: float = 0.0
    iva_rate: float = 0.0


def cuotas_fee(price: float, installments: int) -> float:
    rate = CUOTAS_RATE.get(installments, 0.0)
    return price * rate


def net_vat(price: float, landed: float, rate: float) -> float:
    collected = price * rate / (1.0 + rate)
    paid = landed * rate / (1.0 + rate)
    return collected - paid


def ads_spend(price: float, acos: float) -> float:
    return price * acos


def evaluate(spec: ProfitInput) -> ProfitResult:
    out = ProfitResult()
    out.iva_rate = MARKET_IVA.get(spec.market, MARKET_IVA["MLM"])
    out.commission_cost = spec.price * spec.commission
    out.cuotas_cost = cuotas_fee(spec.price, spec.cuotas)
    out.iva_net = net_vat(spec.price, spec.landed, out.iva_rate)
    out.ads_cost = ads_spend(spec.price, spec.acos)
    out.revenue_net = spec.price - out.commission_cost - out.cuotas_cost
    costs = (
        spec.envios
        + spec.full_storage
        + spec.landed
        + out.ads_cost
        + out.iva_net
    )
    out.net_profit = out.revenue_net - costs
    out.margin = out.net_profit / spec.price if spec.price else 0.0
    gross = (
        spec.price
        - out.commission_cost
        - out.cuotas_cost
        - spec.envios
        - spec.full_storage
        - spec.landed
        - out.iva_net
    )
    out.break_even_acos = max(0.0, gross / spec.price) if spec.price else 0.0
    return out


def render(spec: ProfitInput, res: ProfitResult) -> str:
    cuota_label = f"{spec.cuotas} cuotas"
    return (
        f"Precio bruto:           {spec.price:>10.2f}\n"
        f"Comision ML:            {res.commission_cost:>10.2f}\n"
        f"Cuotas ({cuota_label}):    {res.cuotas_cost:>10.2f}\n"
        f"Mercado Envios:         {spec.envios:>10.2f}\n"
        f"Full storage:           {spec.full_storage:>10.2f}\n"
        f"IVA neto ({res.iva_rate * 100:.0f}%):     {res.iva_net:>10.2f}\n"
        f"Costo landed:           {spec.landed:>10.2f}\n"
        f"Publicidad (ACOS):      {res.ads_cost:>10.2f}\n"
        f"------------------------------\n"
        f"Ganancia neta:          {res.net_profit:>10.2f}\n"
        f"Margen contribucion:    {res.margin * 100:>9.2f}%\n"
        f"ACOS de equilibrio:     {res.break_even_acos * 100:>9.2f}%"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calcula la ganancia neta por venta en Mercado Libre."
    )
    parser.add_argument("--price", type=float, required=True, help="Precio de venta")
    parser.add_argument(
        "--commission",
        type=float,
        required=True,
        help="Comision ML (0.11 a 0.17)",
    )
    parser.add_argument(
        "--envios",
        type=float,
        default=0.0,
        help="Costo Mercado Envios por unidad",
    )
    parser.add_argument(
        "--full",
        type=float,
        default=0.0,
        help="Costo de almacenamiento Full por unidad",
    )
    parser.add_argument(
        "--cuotas",
        type=int,
        choices=sorted(CUOTAS_RATE.keys()),
        default=1,
        help="Cuotas sin interes ofrecidas (1, 3, 6 o 12)",
    )
    parser.add_argument(
        "--market",
        choices=list(MARKET_IVA.keys()),
        default="MLM",
        help="Mercado para tasa de IVA",
    )
    parser.add_argument(
        "--landed",
        type=float,
        required=True,
        help="Costo puesto en bodega (landed cost)",
    )
    parser.add_argument(
        "--acos",
        type=float,
        default=0.0,
        help="ACOS de publicidad (0 a 1)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec = ProfitInput(
        price=args.price,
        commission=args.commission,
        envios=args.envios,
        full_storage=args.full,
        cuotas=args.cuotas,
        market=args.market,
        landed=args.landed,
        acos=args.acos,
    )
    res = evaluate(spec)
    print(render(spec, res))


if __name__ == "__main__":
    main()
