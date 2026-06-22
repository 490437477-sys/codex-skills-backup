#!/usr/bin/env python3
"""Mercado Libre niche scorer.

Score a product idea across the five Mercado Libre marketplaces (MLM, MLB,
MLC, MCO, MLA). The output is a 1-10 total score with a per-dimension
breakdown so a seller can quickly compare niches and pick the best
market to launch in.

Usage:
    python mercado_niche_scorer.py --product "audifonos bluetooth" ^
        --market MLM --aov 599 --demand 1200 --compliance light ^
        --fulfillment full
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field


MARKETS: dict[str, dict[str, object]] = {
    "MLM": {"currency": "MXN", "iva": 0.16, "tax_id": "RFC"},
    "MLB": {"currency": "BRL", "iva": 0.17, "tax_id": "CNPJ"},
    "MLC": {"currency": "CLP", "iva": 0.19, "tax_id": "RUT"},
    "MCO": {"currency": "COP", "iva": 0.19, "tax_id": "NIT"},
    "MLA": {"currency": "ARS", "iva": 0.21, "tax_id": "CUIT"},
}

COMPLIANCE_WEIGHT: dict[str, float] = {
    "none": 1.00,
    "light": 0.85,
    "moderate": 0.60,
    "heavy": 0.30,
}

FULFILLMENT_WEIGHT: dict[str, float] = {
    "flex": 0.70,
    "envios": 0.85,
    "full": 1.00,
}

SEASONAL_BONUS: dict[str, float] = {
    "none": 1.00,
    "hot_sale": 1.18,
    "buen_fin": 1.20,
    "black_friday": 1.15,
    "navidad": 1.12,
}


@dataclass
class NicheInput:
    product: str
    market: str
    aov: float
    demand: int
    compliance: str
    fulfillment: str
    seasonality: str = "none"


@dataclass
class NicheScore:
    total: float = 0.0
    dimensions: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)


def score_demand(demand: int) -> float:
    if demand <= 0:
        return 1.0
    if demand >= 5000:
        return 10.0
    if demand >= 2000:
        return 8.5
    if demand >= 800:
        return 6.5
    if demand >= 300:
        return 4.5
    return 2.5


def score_margin(aov: float, market: str) -> float:
    threshold = {
        "MXN": 800.0,
        "BRL": 350.0,
        "CLP": 30000.0,
        "COP": 150000.0,
        "ARS": 25000.0,
    }.get(market, 500.0)
    if aov <= 0:
        return 1.0
    if aov >= threshold * 2.0:
        return 10.0
    if aov >= threshold:
        return 8.0
    if aov >= threshold * 0.6:
        return 5.5
    if aov >= threshold * 0.3:
        return 3.5
    return 2.0


def score_competition(market: str) -> float:
    density = {
        "MLM": 4.5,
        "MLB": 4.0,
        "MLC": 7.0,
        "MCO": 7.5,
        "MLA": 5.0,
    }
    return float(density.get(market, 5.0))


def evaluate(spec: NicheInput) -> NicheScore:
    out = NicheScore()
    demand = score_demand(spec.demand)
    margin = score_margin(spec.aov, spec.market)
    competition = score_competition(spec.market)
    compliance = COMPLIANCE_WEIGHT.get(spec.compliance, 0.6) * 10.0
    fulfillment = FULFILLMENT_WEIGHT.get(spec.fulfillment, 0.7) * 10.0
    season = SEASONAL_BONUS.get(spec.seasonality, 1.0)

    out.dimensions = {
        "demanda": demand,
        "margen": margin,
        "competencia": competition,
        "cumplimiento": round(compliance, 2),
        "logistica": round(fulfillment, 2),
    }
    weights = {
        "demanda": 0.25,
        "margen": 0.30,
        "competencia": 0.20,
        "cumplimiento": 0.10,
        "logistica": 0.15,
    }
    base = sum(out.dimensions[k] * weights[k] for k in out.dimensions)
    out.total = round(min(10.0, base * season), 2)
    if spec.demand < 300:
        out.notes.append("Demanda baja: validar con Mercado Libre Trends.")
    if competition < 5.0:
        out.notes.append("Categoria saturada, considerar diferenciacion.")
    if spec.fulfillment == "full" and spec.aov < 300:
        out.notes.append("Full puede no ser rentable con AOV tan bajo.")
    return out


def render(spec: NicheInput, score: NicheScore) -> str:
    market_meta = MARKETS[spec.market]
    lines = [
        f"Producto:        {spec.product}",
        f"Mercado:         {spec.market} ({market_meta['currency']}, IVA {market_meta['iva'] * 100:.0f}%)",
        f"AOV:             {spec.aov:.2f} {market_meta['currency']}",
        f"Demanda mensual: {spec.demand} unidades",
        f"Cumplimiento:    {spec.compliance} (impuesto: {market_meta['tax_id']})",
        f"Logistica:       {spec.fulfillment}",
        f"Temporada:       {spec.seasonality}",
        "",
        "Desglose (1-10):",
    ]
    for name, value in score.dimensions.items():
        lines.append(f"  - {name:<14}: {value:.2f}")
    lines.append(f"  - {'TOTAL':<14}: {score.total:.2f} / 10")
    if score.notes:
        lines.append("")
        lines.append("Notas:")
        for note in score.notes:
            lines.append(f"  * {note}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Puntua un nicho de Mercado Libre (1-10)."
    )
    parser.add_argument("--product", required=True, help="Nombre del producto")
    parser.add_argument(
        "--market",
        choices=list(MARKETS.keys()),
        required=True,
        help="Mercado: MLM, MLB, MLC, MCO o MLA",
    )
    parser.add_argument(
        "--aov",
        type=float,
        required=True,
        help="Ticket promedio en moneda local",
    )
    parser.add_argument(
        "--demand",
        type=int,
        required=True,
        help="Demanda mensual estimada (unidades)",
    )
    parser.add_argument(
        "--compliance",
        choices=list(COMPLIANCE_WEIGHT.keys()),
        default="light",
        help="Carga regulatoria: none, light, moderate, heavy",
    )
    parser.add_argument(
        "--fulfillment",
        choices=list(FULFILLMENT_WEIGHT.keys()),
        default="envios",
        help="Modalidad logistica: flex, envios o full",
    )
    parser.add_argument(
        "--seasonality",
        choices=list(SEASONAL_BONUS.keys()),
        default="none",
        help="Temporada pico: hot_sale, buen_fin, black_friday, navidad",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec = NicheInput(
        product=args.product,
        market=args.market,
        aov=args.aov,
        demand=args.demand,
        compliance=args.compliance,
        fulfillment=args.fulfillment,
        seasonality=args.seasonality,
    )
    score = evaluate(spec)
    print(render(spec, score))


if __name__ == "__main__":
    main()
