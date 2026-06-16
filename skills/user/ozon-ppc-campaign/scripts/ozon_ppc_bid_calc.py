#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ozon_ppc_bid_calc.py — Ozon PPC bid calculator with ДРР (ACoS) framework.

Calculates for an Ozon product:
- Break-even ДРР (Доля рекламных расходов) — same concept as ACoS
- Target ДРР based on desired profit margin
- Max CPC ceiling from unit economics
- Recommended bid ranges per category (in ₽)
- Phase-based daily budget (Launch / Growth / Mature)
- VAT-aware profit calculation

Usage:
  python ozon_ppc_bid_calc.py
  python ozon_ppc_bid_calc.py --interactive
  python ozon_ppc_bid_calc.py --json @params.json

Design notes:
- ДРР = Рекламный расход / Выручка от рекламы × 100%  (same as ACoS)
- Russian CPC defaults are based on Ozon industry averages, not official rates.
  Use web_search to verify current category CPC ranges before launch.
- All rates/percentages MUST be verified via web_search before live bidding.
"""

import argparse
import json
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


# ---------- Default Russian CPC ranges by category (RUB per click) ----------
# Format: (low, median, high)
# Sources: aggregated from seller forums + Ozon Performance help (2025-2026)
# IMPORTANT: verify with web_search before bidding — these are ballpark only
CATEGORY_CPC_RANGES = {
    "books":          (2, 8, 20),
    "electronics":    (15, 50, 150),
    "home":           (10, 30, 80),
    "beauty":         (20, 60, 200),
    "fashion":        (12, 40, 120),
    "toys":           (10, 30, 90),
    "auto":           (15, 45, 130),
    "furniture":      (20, 70, 250),
    "sports":         (10, 30, 90),
    "supplements":    (25, 80, 300),
    "jewelry":        (15, 50, 180),
    "kids":           (10, 35, 100),
    "pet":            (10, 30, 90),
    "default":        (10, 30, 100),
}


# ---------- Default Russian ДРР targets by lifecycle phase ----------
PHASE_DRR_TARGETS = {
    "launch":   (30, 50),
    "growth":   (15, 25),
    "mature":   (8, 15),
    "defense":  (5, 10),
}


def get_cpc_range(category):
    return CATEGORY_CPC_RANGES.get(category, CATEGORY_CPC_RANGES["default"])


def calculate_drr(product_cost_cny, selling_price_rub,
                  commission_pct=12.0, vat_pct=20.0,
                  usd_rub=90.0, cny_usd=7.2,
                  fbo_fees_rub=95.0,
                  returns_reserve_pct=5.0,
                  other_costs_pct=2.0):
    """Calculate unit economics + break-even ДРР."""
    product_cost_rub = product_cost_cny / cny_usd * usd_rub
    price = selling_price_rub
    vat_rub = price * (vat_pct / 100.0)
    price_excl_vat = price - vat_rub
    commission_rub = price * (commission_pct / 100.0)
    logistics_rub = fbo_fees_rub
    returns_rub = price * (returns_reserve_pct / 100.0)
    other_rub = price * (other_costs_pct / 100.0)

    contribution_profit = price_excl_vat - (product_cost_rub + commission_rub
                                             + logistics_rub + returns_rub + other_rub)
    breakeven_drr_pct = (contribution_profit / price * 100.0) if price > 0 else 0.0

    return {
        "selling_price_rub": round(price, 2),
        "product_cost_rub": round(product_cost_rub, 2),
        "vat_rub": round(vat_rub, 2),
        "price_excl_vat": round(price_excl_vat, 2),
        "commission_rub": round(commission_rub, 2),
        "logistics_rub": round(logistics_rub, 2),
        "returns_rub": round(returns_rub, 2),
        "other_rub": round(other_rub, 2),
        "contribution_profit": round(contribution_profit, 2),
        "breakeven_drr_pct": round(breakeven_drr_pct, 2),
    }


def max_cpc_for_drr(target_drr_pct, selling_price_rub, conversion_rate_pct=2.0):
    """Max CPC ceiling for given target ДРР and conversion rate.
    Formula: Max CPC = (Target ДРР × Price × Conversion Rate) / 100
    """
    if conversion_rate_pct <= 0:
        return 0.0
    return target_drr_pct * selling_price_rub * (conversion_rate_pct / 100.0) / 100.0


def recommend_bid(category, target_drr_pct, selling_price_rub,
                  conversion_rate_pct=2.0, phase="growth"):
    cpc_low, cpc_med, cpc_high = get_cpc_range(category)
    max_cpc = max_cpc_for_drr(target_drr_pct, selling_price_rub, conversion_rate_pct)

    phase_multiplier = {
        "launch": 1.0,
        "growth": 0.8,
        "mature": 0.6,
        "defense": 0.7,
    }.get(phase, 0.8)

    recommended_bid = min(max_cpc * phase_multiplier, cpc_high)
    safe_bid = min(max_cpc * 0.6, cpc_med)

    return {
        "max_cpc_ceiling": round(max_cpc, 2),
        "recommended_bid": round(recommended_bid, 2),
        "safe_starter_bid": round(safe_bid, 2),
        "category_cpc_low": cpc_low,
        "category_cpc_median": cpc_med,
        "category_cpc_high": cpc_high,
        "phase": phase,
        "phase_multiplier": phase_multiplier,
    }


def recommend_budget(category, selling_price_rub, phase="launch", monthly_orders_target=30):
    cpc_low, cpc_med, cpc_high = get_cpc_range(category)

    phase_budgets = {
        "launch":  (500, 1500),
        "growth":  (800, 3000),
        "mature":  (300, 1200),
        "defense": (500, 2000),
    }
    budget_low, budget_high = phase_budgets.get(phase, phase_budgets["growth"])

    orders_per_day = monthly_orders_target / 30.0
    est_clicks_per_day = orders_per_day / 0.02
    est_cost_per_day = est_clicks_per_day * cpc_med

    return {
        "phase_budget_range_low": budget_low,
        "phase_budget_range_high": budget_high,
        "estimated_cost_per_day_at_target": round(est_cost_per_day, 2),
        "estimated_clicks_per_day": round(est_clicks_per_day, 1),
        "estimated_orders_per_day": round(orders_per_day, 2),
    }


def render_report(unit, bid_rec, budget_rec, category, target_drr_pct, conversion_rate_pct, phase):
    print("")
    print("=== Ozon PPC Bid & Budget Calculator ===")
    print("Category: " + category + "    Phase: " + phase.upper())
    print("Target ДРР: " + str(target_drr_pct) + "%    Conversion: " + str(conversion_rate_pct) + "%")
    print("")
    print("--- Unit Economics ---")
    print("Selling price:        " + str(unit["selling_price_rub"]) + " RUB")
    print("Price excl. VAT:      " + str(unit["price_excl_vat"]) + " RUB")
    print("Product cost:         " + str(unit["product_cost_rub"]) + " RUB")
    print("Ozon commission:      " + str(unit["commission_rub"]) + " RUB")
    print("FBO logistics:        " + str(unit["logistics_rub"]) + " RUB")
    print("Returns reserve:      " + str(unit["returns_rub"]) + " RUB")
    print("Other reserves:       " + str(unit["other_rub"]) + " RUB")
    print("Contribution profit:  " + str(unit["contribution_profit"]) + " RUB (before ads)")
    print("Break-even ДРР:       " + str(unit["breakeven_drr_pct"]) + "%")
    print("")
    print("--- Bid Recommendations ---")
    print("Max CPC ceiling (target ДРР):     " + str(bid_rec["max_cpc_ceiling"]) + " RUB")
    print("Recommended bid (phase-tuned):    " + str(bid_rec["recommended_bid"]) + " RUB")
    print("Safe starter bid (60% of ceiling): " + str(bid_rec["safe_starter_bid"]) + " RUB")
    print("Category CPC range:               " + str(bid_rec["category_cpc_low"]) + " - "
          + str(bid_rec["category_cpc_median"]) + " - " + str(bid_rec["category_cpc_high"]) + " RUB")
    print("Phase multiplier:                 " + str(bid_rec["phase_multiplier"]) + "x")
    print("")
    print("--- Daily Budget Recommendation (" + phase + ") ---")
    print("Phase budget range:               " + str(budget_rec["phase_budget_range_low"]) + " - "
          + str(budget_rec["phase_budget_range_high"]) + " RUB/day")
    print("Est. cost per day at target:      " + str(budget_rec["estimated_cost_per_day_at_target"]) + " RUB")
    print("Est. clicks per day needed:       " + str(budget_rec["estimated_clicks_per_day"]))
    print("Est. orders per day target:       " + str(budget_rec["estimated_orders_per_day"]))
    print("")
    print("[WARN] All CPC ranges + ДРР targets are ballpark. Verify with web_search before live bidding.")
    print("[WARN] VAT (НДС) is pass-through — Ozon withholds from gross price; seller receives price excl. VAT.")
    print("")


def parse_interactive():
    print("=== Ozon PPC Calculator (Interactive) ===")
    print("")
    name = input("Product name: ").strip() or "Demo product"
    cat = input("Category (electronics/home/beauty/fashion/toys/sports/auto/furniture/books/supplements/jewelry/kids/pet): ").strip() or "home"
    price = float(input("Selling price RUB [1500]: ") or 1500)
    cost_cny = float(input("Product cost CNY [50]: ") or 50)
    comm = float(input("Ozon commission % [12]: ") or 12)
    phase = input("Phase (launch/growth/mature/defense) [launch]: ").strip() or "launch"
    target_drr = float(input("Target ДРР % [25]: ") or 25)
    conv = float(input("Conversion rate % [2]: ") or 2)
    monthly_target = int(input("Monthly order target [30]: ") or 30)
    return {
        "name": name, "category": cat, "selling_price_rub": price,
        "product_cost_cny": cost_cny, "commission_pct": comm,
        "phase": phase, "target_drr_pct": target_drr,
        "conversion_rate_pct": conv, "monthly_orders_target": monthly_target,
    }


def main():
    parser = argparse.ArgumentParser(description="Ozon PPC bid + budget calculator with ДРР framework")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--json", type=str, help="JSON params (string or @file)")
    parser.add_argument("--category", default="home", choices=list(CATEGORY_CPC_RANGES.keys()))
    parser.add_argument("--phase", default="launch", choices=list(PHASE_DRR_TARGETS.keys()))
    parser.add_argument("--target-drr", type=float, default=25.0, help="Target ДРР (ACoS) %")
    parser.add_argument("--conversion", type=float, default=2.0, help="Conversion rate %")
    parser.add_argument("--price", type=float, default=1500.0)
    parser.add_argument("--cost-cny", type=float, default=50.0)
    parser.add_argument("--commission", type=float, default=12.0)
    parser.add_argument("--monthly-orders", type=int, default=30)
    args = parser.parse_args()

    if args.interactive:
        params = parse_interactive()
        category = params["category"]
        phase = params["phase"]
        target_drr = params["target_drr_pct"]
        conversion = params["conversion_rate_pct"]
        price = params["selling_price_rub"]
        cost_cny = params["product_cost_cny"]
        commission = params["commission_pct"]
        monthly_target = params["monthly_orders_target"]
    elif args.json:
        raw = args.json
        if raw.startswith("@"):
            with open(raw[1:], "r", encoding="utf-8-sig") as f:
                raw = f.read()
        params = json.loads(raw)
        category = params.get("category", args.category)
        phase = params.get("phase", args.phase)
        target_drr = params.get("target_drr_pct", args.target_drr)
        conversion = params.get("conversion_rate_pct", args.conversion)
        price = params.get("selling_price_rub", args.price)
        cost_cny = params.get("product_cost_cny", args.cost_cny)
        commission = params.get("commission_pct", args.commission)
        monthly_target = params.get("monthly_orders_target", args.monthly_orders)
    else:
        category = args.category
        phase = args.phase
        target_drr = args.target_drr
        conversion = args.conversion
        price = args.price
        cost_cny = args.cost_cny
        commission = args.commission
        monthly_target = args.monthly_orders

    unit = calculate_drr(product_cost_cny=cost_cny, selling_price_rub=price, commission_pct=commission)
    bid_rec = recommend_bid(category, target_drr, price, conversion, phase)
    budget_rec = recommend_budget(category, price, phase, monthly_target)

    render_report(unit, bid_rec, budget_rec, category, target_drr, conversion, phase)


if __name__ == "__main__":
    main()
