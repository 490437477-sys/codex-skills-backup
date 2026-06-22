#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ozon per-order profit calculator for Ozon.ru / Ozon.kz / Ozon.by.

Waterfall: Retail - commission - fulfillment fee - returns reserve -
promo reserve - FX buffer - COD penalty - landed cost - ads spend
= net profit per order. Also computes break-even ACoS.

Usage:
  python ozon_profit_calc.py --retail 4990 --commission 0.15 --fbo-fee 380 --landed-usd 8.50 --fx 92 --acos 0.20 --returns 0.10
  python ozon_profit_calc.py --retail 9900 --commission 0.12 --fbs-fee 250 --landed-usd 12 --fx 95 --acos 0.18 --cod 0.40 --marketplace ru --json
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


MARKET_CCY = {"ru": "RUB", "kz": "KZT", "by": "BYN"}


@dataclass
class ProfitInputs:
    retail: float
    commission: float
    fbo_fee: float
    fbs_fee: float
    fulfillment: str
    landed_usd: float
    fx_usd_local: float
    returns: float
    acos: float
    cod_ratio: float
    promo_pct: float
    fx_buffer: float
    marketplace: str


@dataclass
class ProfitResult:
    marketplace: str
    currency: str
    retail: float
    breakdown: dict
    net_profit: float
    contribution_margin_pct: float
    break_even_acos: float
    verdict: str
    notes: list = field(default_factory=list)


def compute(p: ProfitInputs) -> ProfitResult:
    """Run the waterfall and return a ProfitResult."""
    ccy = MARKET_CCY.get(p.marketplace.lower(), "RUB")
    fee = p.fbo_fee if p.fulfillment.lower() == "fbo" else p.fbs_fee
    landed_local = p.landed_usd * p.fx_usd_local
    commission_amt = p.retail * p.commission
    promo_amt = p.retail * p.promo_pct
    fx_buffer_amt = p.retail * p.fx_buffer
    returns_reserve = landed_local * p.returns
    cod_cost = p.retail * p.cod_ratio * 0.03
    ads_spend = p.retail * p.acos
    total_fees = commission_amt + fee + returns_reserve + promo_amt + fx_buffer_amt + cod_cost
    net_profit = p.retail - total_fees - landed_local - ads_spend
    cm_pct = (net_profit / p.retail) if p.retail > 0 else 0.0
    break_even_acos = ((p.retail - total_fees - landed_local) / p.retail) if p.retail > 0 else 0.0
    if cm_pct >= 0.20:
        verdict = "HEALTHY"
    elif cm_pct >= 0.05:
        verdict = "VIABLE"
    elif cm_pct >= 0.0:
        verdict = "THIN"
    else:
        verdict = "LOSS"
    notes = []
    if p.fx_buffer < 0.05 and p.marketplace == "ru":
        notes.append("Ruble buffer below 5% - RUB has moved 10-20% in recent years.")
    if p.returns > 0.15:
        notes.append("Return rate above 15% - investigate product quality.")
    if p.acos > break_even_acos and break_even_acos > 0:
        notes.append("ACoS exceeds break-even - reduce bids or raise retail.")
    if p.cod_ratio > 0.5:
        notes.append("COD share above 50% - bake bounce cost or push prepaid.")
    breakdown = {
        "retail": round(p.retail, 2),
        "ozon_commission": round(-commission_amt, 2),
        "fulfillment_fee": round(-fee, 2),
        "returns_reserve": round(-returns_reserve, 2),
        "promo_reserve": round(-promo_amt, 2),
        "fx_buffer": round(-fx_buffer_amt, 2),
        "cod_penalty": round(-cod_cost, 2),
        "landed_cost": round(-landed_local, 2),
        "ads_spend": round(-ads_spend, 2),
        "landed_usd": p.landed_usd,
        "fx_rate": p.fx_usd_local,
    }
    return ProfitResult(
        marketplace=p.marketplace, currency=ccy, retail=p.retail,
        breakdown=breakdown, net_profit=round(net_profit, 2),
        contribution_margin_pct=round(cm_pct * 100, 2),
        break_even_acos=round(break_even_acos * 100, 2),
        verdict=verdict, notes=notes,
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Ozon per-SKU profit waterfall + break-even ACoS.")
    p.add_argument("--retail", type=float, required=True, help="Retail price in local currency")
    p.add_argument("--commission", type=float, default=0.15, help="Ozon commission rate (0-0.25)")
    p.add_argument("--fbo-fee", type=float, default=0.0, help="FBO fee in local currency")
    p.add_argument("--fbs-fee", type=float, default=0.0, help="FBS fee in local currency")
    p.add_argument("--fulfillment", choices=["fbo", "fbs"], default="fbo")
    p.add_argument("--landed-usd", type=float, required=True, help="Landed cost in USD")
    p.add_argument("--fx", dest="fx_usd_local", type=float, default=92.0,
                   help="USD -> local ccy rate (default 92 RUB)")
    p.add_argument("--returns", type=float, default=0.08, help="Return rate (0-0.20)")
    p.add_argument("--acos", type=float, default=0.15, help="Advertising ACoS (0-0.50)")
    p.add_argument("--cod", dest="cod_ratio", type=float, default=0.20, help="COD share (0-1)")
    p.add_argument("--promo", dest="promo_pct", type=float, default=0.05, help="Promo reserve")
    p.add_argument("--fx-buffer", type=float, default=0.10, help="Ruble buffer (0-0.20)")
    p.add_argument("--marketplace", choices=["ru", "kz", "by"], default="ru")
    p.add_argument("--json", action="store_true", help="Emit JSON only")
    return p


def render(r: ProfitResult) -> str:
    ccy = r.currency
    keys = ["ozon_commission", "fulfillment_fee", "returns_reserve",
            "promo_reserve", "fx_buffer", "cod_penalty", "landed_cost", "ads_spend"]
    lines = [
        "Ozon Profit Waterfall (" + r.marketplace + " / " + ccy + ")",
        "Retail: " + str(r.retail) + " " + ccy, "", "Deductions:",
    ]
    for k in keys:
        lines.append("  " + k.replace("_", " ") + ": " + str(r.breakdown[k]).rjust(7) + " " + ccy)
    lines.extend([
        "",
        "Net profit / order: " + str(r.net_profit) + " " + ccy,
        "Contribution margin: " + str(r.contribution_margin_pct) + " %  -> " + r.verdict,
        "Break-even ACoS:     " + str(r.break_even_acos) + " %",
    ])
    if r.notes:
        lines.append("Notes:")
        lines.extend("  - " + n for n in r.notes)
    return "\n".join(lines)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    inputs = ProfitInputs(
        retail=args.retail, commission=args.commission,
        fbo_fee=args.fbo_fee, fbs_fee=args.fbs_fee,
        fulfillment=args.fulfillment, landed_usd=args.landed_usd,
        fx_usd_local=args.fx_usd_local, returns=args.returns, acos=args.acos,
        cod_ratio=args.cod_ratio, promo_pct=args.promo_pct,
        fx_buffer=args.fx_buffer, marketplace=args.marketplace,
    )
    result = compute(inputs)
    if args.json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print(render(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
