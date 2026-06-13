#!/usr/bin/env python3
"""
TEMU 单品利润测算脚本

支持两种模式：
  - fully-managed (全托管): 平台核价、平台跨境/尾程，卖家只负担到国内集运仓
  - semi-managed   (半托管): 卖家自定价、自备海外仓，承担头程 + 海外仓 + 尾程

用法示例：
    # 全托管，目标售价 USD 3.49
    python temu_profit_calc.py fully-managed \
        --supply-price 1.60 --factory-cost 1.05 --pack-cost 0.20 \
        --commission 0.05 --quality-deduction 0.03 --return-rate 0.18 \
        --refund-cost 0.5

    # 半托管，目标售价 USD 19.99
    python temu_profit_calc.py semi-managed \
        --sell-price 19.99 --factory-cost 5.0 --pack-cost 0.5 \
        --headhaul 1.2 --warehouse 0.8 --last-mile 4.5 \
        --commission 0.06 --return-rate 0.15 --refund-cost 6

所有金额默认 USD。脚本只做量级估算，不替代实盘核算。
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict


@dataclass
class ProfitResult:
    mode: str
    inputs: dict
    revenue_per_unit: float
    cost_per_unit: float
    gross_profit_per_unit: float
    gross_margin: float
    breakeven_units_per_day: float | None
    sensitivity: dict


def fully_managed(args):
    # 全托管：卖家收到的是 supply_price，扣除平台佣金 + 质量扣款 + 售后赔付
    supply = args.supply_price
    cost = args.factory_cost + args.pack_cost + args.inland_cost

    commission_amt = supply * args.commission
    quality_amt = supply * args.quality_deduction
    refund_loss = (args.refund_cost + cost) * args.return_rate  # 退货按全损 + 退仓/赔付成本

    net_revenue = supply - commission_amt - quality_amt - refund_loss
    profit = net_revenue - cost
    margin = profit / supply if supply else 0

    return ProfitResult(
        mode="fully-managed",
        inputs={k: v for k, v in vars(args).items() if not callable(v)},
        revenue_per_unit=round(net_revenue, 4),
        cost_per_unit=round(cost, 4),
        gross_profit_per_unit=round(profit, 4),
        gross_margin=round(margin, 4),
        breakeven_units_per_day=(
            round(args.fixed_daily / profit, 2) if profit > 0 and args.fixed_daily else None
        ),
        sensitivity=_sensitivity(supply, cost, args, mode="fully"),
    )


def semi_managed(args):
    sell = args.sell_price
    cost = (
        args.factory_cost
        + args.pack_cost
        + args.headhaul
        + args.warehouse
        + args.last_mile
    )
    commission_amt = sell * args.commission
    refund_loss = (args.refund_cost + cost) * args.return_rate

    net_revenue = sell - commission_amt - refund_loss
    profit = net_revenue - cost
    margin = profit / sell if sell else 0

    return ProfitResult(
        mode="semi-managed",
        inputs={k: v for k, v in vars(args).items() if not callable(v)},
        revenue_per_unit=round(net_revenue, 4),
        cost_per_unit=round(cost, 4),
        gross_profit_per_unit=round(profit, 4),
        gross_margin=round(margin, 4),
        breakeven_units_per_day=(
            round(args.fixed_daily / profit, 2) if profit > 0 and args.fixed_daily else None
        ),
        sensitivity=_sensitivity(sell, cost, args, mode="semi"),
    )


def _sensitivity(price, cost, args, mode):
    """对退货率做敏感性分析。"""
    out = {}
    for r in (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40):
        if mode == "fully":
            commission_amt = price * args.commission
            quality_amt = price * args.quality_deduction
            refund_loss = (args.refund_cost + cost) * r
            net = price - commission_amt - quality_amt - refund_loss
        else:
            commission_amt = price * args.commission
            refund_loss = (args.refund_cost + cost) * r
            net = price - commission_amt - refund_loss
        profit = net - cost
        margin = profit / price if price else 0
        out[f"return_rate={int(r*100)}%"] = {
            "profit_per_unit": round(profit, 4),
            "margin": round(margin, 4),
        }
    return out


def build_parser():
    p = argparse.ArgumentParser(description="TEMU 单品利润测算")
    sub = p.add_subparsers(dest="mode", required=True)

    # --- fully-managed ---
    f = sub.add_parser("fully-managed", help="全托管模式")
    f.add_argument("--supply-price", type=float, required=True, help="给 TEMU 的供货价 USD")
    f.add_argument("--factory-cost", type=float, required=True, help="工厂出厂价 USD")
    f.add_argument("--pack-cost", type=float, default=0.2, help="包装/贴标 USD")
    f.add_argument("--inland-cost", type=float, default=0.15, help="国内到集运仓运费分摊 USD")
    f.add_argument("--commission", type=float, default=0.03, help="平台佣金率, 0.03 = 3%%")
    f.add_argument("--quality-deduction", type=float, default=0.02, help="质量扣款占比")
    f.add_argument("--return-rate", type=float, default=0.15, help="退货率")
    f.add_argument("--refund-cost", type=float, default=0.5, help="单次退货额外赔付/退仓成本 USD")
    f.add_argument("--fixed-daily", type=float, default=0, help="日均固定开销 USD (人工/工具/租金)")
    f.set_defaults(func=fully_managed)

    # --- semi-managed ---
    s = sub.add_parser("semi-managed", help="半托管模式")
    s.add_argument("--sell-price", type=float, required=True, help="终端售价 USD")
    s.add_argument("--factory-cost", type=float, required=True)
    s.add_argument("--pack-cost", type=float, default=0.5)
    s.add_argument("--headhaul", type=float, default=1.0, help="头程到海外仓 USD/件")
    s.add_argument("--warehouse", type=float, default=0.8, help="海外仓仓储 + 操作 USD/件")
    s.add_argument("--last-mile", type=float, default=4.0, help="尾程派送 USD/件")
    s.add_argument("--commission", type=float, default=0.06)
    s.add_argument("--return-rate", type=float, default=0.15)
    s.add_argument("--refund-cost", type=float, default=3.0)
    s.add_argument("--fixed-daily", type=float, default=0)
    s.set_defaults(func=semi_managed)

    return p


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    parser = build_parser()
    args = parser.parse_args()
    result: ProfitResult = args.func(args)
    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))

    # 文字总结
    print()
    print("== 摘要 ==")
    print(f"模式: {result.mode}")
    print(f"单件成本: {result.cost_per_unit}")
    print(f"单件净收入: {result.revenue_per_unit}")
    print(f"单件毛利: {result.gross_profit_per_unit}  毛利率: {result.gross_margin*100:.2f}%")
    if result.breakeven_units_per_day:
        print(f"覆盖日固定成本所需销量: {result.breakeven_units_per_day} 件/天")
    if result.gross_margin < 0.10:
        print("[WARN] 毛利率 < 10%，建议放弃或重新核价")
    elif result.gross_margin < 0.20:
        print("[WARN] 毛利率偏薄，需控好退货与扣款")
    else:
        print("[OK]   毛利率健康")


if __name__ == "__main__":
    main()
