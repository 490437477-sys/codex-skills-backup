# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
TEMU Ads (商品推广) Bid Calculator

Calculates break-even ROAS, target ROAS, max CPC, and recommends
the appropriate ROAS tier (快速跑量/效益均衡/稳定增长) for a TEMU product.

Usage examples:
    # Basic — recommended starting point
    python bid_calculator.py --price 109.99 --cost 76.50

    # Full Mode A — break-even + tier recommendation + 4-week ramp
    python bid_calculator.py --price 109.99 --cost 76.50 \
        --commission 0.10 --return-rate 0.15 \
        --cvr 0.02 --budget 50 --mode full

    # Mode B — audit existing ad performance
    python bid_calculator.py --mode audit \
        --price 109.99 --cost 76.50 \
        --impressions 12000 --clicks 240 --orders 4 --ad-spend 235 \
        --commission 0.10

All amounts in USD. Output in Chinese-friendly mixed CN/EN.
"""

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class BidResult:
    mode: str
    inputs: dict
    # Financial framework
    revenue_per_unit: float
    cost_per_unit: float
    commission_per_unit: float
    return_loss_per_unit: float
    net_profit_per_unit_no_ad: float
    # ROAS framework
    break_even_roas: float
    target_roas: float
    target_acos: float
    # CPC framework
    max_cpc_at_cvr: float
    expected_daily_clicks: float
    expected_daily_orders: float
    # Tier recommendation
    recommended_tier: str
    tier_reasoning: str
    # 4-week ramp
    ramp_schedule: list
    # Audit (mode B only)
    audit: Optional[dict] = None
    # Diagnostics
    warnings: list = None

    def __post_init__(self):
        if self.warnings is None:
            self.warnings = []


def calc_financial(price, cost, commission, return_rate):
    """Compute per-unit economics."""
    commission_amt = price * commission
    return_loss = (cost + commission_amt) * return_rate
    net_profit = price - cost - commission_amt - return_loss
    return {
        "revenue": round(price, 2),
        "cost": round(cost, 2),
        "commission_amt": round(commission_amt, 2),
        "return_loss_amt": round(return_loss, 2),
        "net_profit_no_ad": round(net_profit, 2),
        "margin_no_ad_pct": round(net_profit / price * 100, 2) if price else 0,
    }


def calc_roas_framework(price, cost, commission, return_rate, cvr):
    """Compute break-even ROAS, target ROAS, max CPC."""
    fin = calc_financial(price, cost, commission, return_rate)
    net_profit = fin["net_profit_no_ad"]

    # Break-even ROAS: at what ROAS does ad spend = ad profit
    # ad_spend / ad_sales = 1 / break_even_roas
    # If ad_sales = break_even_roas * ad_spend
    # Then ad_profit = ad_sales * margin - ad_spend
    # Set ad_profit = 0: ad_sales * margin = ad_spend
    # ROAS * ad_spend * margin = ad_spend → ROAS = 1 / margin
    margin_pct = net_profit / price if price else 0
    break_even_roas = 1 / margin_pct if margin_pct > 0 else 999
    target_roas = break_even_roas * 1.3  # 30% safety margin
    target_acos = 1 / target_roas if target_roas else 0

    # Max CPC = (price * CVR) / break_even_roas
    # At max CPC, profit per click = 0; below = profit
    max_cpc = (price * cvr) / break_even_roas if break_even_roas < 999 else 0

    return {
        "break_even_roas": round(break_even_roas, 2),
        "target_roas": round(target_roas, 2),
        "target_acos_pct": round(target_acos * 100, 2),
        "max_cpc_at_cvr": round(max_cpc, 4),
        "cvr_used": cvr,
    }


def recommend_tier(reviews, monthly_sales, target_roas, break_even_roas):
    """Recommend one of 3 ROAS tiers based on product maturity."""
    if reviews < 10 or monthly_sales < 100:
        return "快速跑量", (
            f"新链接 (评论 {reviews} / 月销 {monthly_sales})，"
            f"需要初始销量+评价积累，建议用低ROAS档(目标{target_roas:.1f})跑量"
        )
    elif reviews < 50 or monthly_sales < 500:
        return "效益均衡", (
            f"成长期 (评论 {reviews} / 月销 {monthly_sales})，"
            f"平衡流量与利润，建议中ROAS档(目标{target_roas:.1f})"
        )
    else:
        return "稳定增长", (
            f"成熟期 (评论 {reviews} / 月销 {monthly_sales})，"
            f"高效率扩展，建议高ROAS档(目标{target_roas:.1f})"
        )


def build_ramp_schedule(budget, target_roas, break_even_roas):
    """4-week ramp from low budget to scaling."""
    return [
        {"week": 1, "daily_budget": round(budget * 0.6, 2),
         "monthly_total": round(budget * 0.6 * 7, 2),
         "tier": "快速跑量",
         "goal": "初始销量+评价积累",
         "stop_loss": f"ROAS < {break_even_roas * 0.5:.2f} 连续2天则暂停"},
        {"week": 2, "daily_budget": round(budget * 0.8, 2),
         "monthly_total": round(budget * 0.8 * 7, 2),
         "tier": "效益均衡",
         "goal": "根据Week 1数据优化",
         "stop_loss": f"ROAS < {break_even_roas * 0.7:.2f} 调整listing"},
        {"week": 3, "daily_budget": round(budget, 2),
         "monthly_total": round(budget * 7, 2),
         "tier": "效益均衡",
         "goal": "起量阶段(若ROAS达标)",
         "stop_loss": f"ROAS < {break_even_roas:.2f} 降档"},
        {"week": 4, "daily_budget": round(budget * 1.2, 2),
         "monthly_total": round(budget * 1.2 * 7, 2),
         "tier": "稳定增长",
         "goal": "锁定高效关键词",
         "stop_loss": f"维持ROAS ≥ {target_roas:.2f}"},
    ]


def run_audit(args):
    """Audit existing TEMU ad performance."""
    impressions = args.impressions or 0
    clicks = args.clicks or 0
    orders = args.orders or 0
    ad_spend = args.ad_spend or 0
    ctr = (clicks / impressions * 100) if impressions else 0
    cvr = (orders / clicks * 100) if clicks else 0
    ad_revenue = orders * args.price
    roas = (ad_revenue / ad_spend) if ad_spend else 0
    cpc = (ad_spend / clicks) if clicks else 0
    aov = (ad_revenue / orders) if orders else 0

    fin = calc_financial(args.price, args.cost, args.commission, args.return_rate)
    roas_fw = calc_roas_framework(args.price, args.cost, args.commission, args.return_rate, 0.02)

    # 4-dimension diagnosis
    diagnosis = []
    if impressions < 5000:
        diagnosis.append({
            "issue": "曝光不足",
            "severity": "??" if impressions < 2000 else "??",
            "cause": "出价过低 / listing评分低 / 类目错放",
            "fix": "提升ROAS档位(降低ROAS目标) / 优化listing / 检查类目归属"
        })
    if ctr < 2.0:
        diagnosis.append({
            "issue": "点击率低",
            "severity": "??" if ctr < 1.0 else "??",
            "cause": "主图弱 / 价格不具竞争力 / 标题不够吸引",
            "fix": "换主图(测款A/B) / 调价 / 测试新标题"
        })
    if cvr < 2.0:
        diagnosis.append({
            "issue": "转化率低",
            "severity": "??" if cvr < 1.0 else "??",
            "cause": "详情页弱 / 价格过高 / 评价数少",
            "fix": "丰富详情页 / 调价 / 引导更多评价"
        })
    if roas < roas_fw["break_even_roas"]:
        diagnosis.append({
            "issue": "ROAS不达标",
            "severity": "??",
            "cause": "CPC过高 / CVR过低 / 档位选择错误",
            "fix": "降档(改用低ROAS档) / 暂停 / 修复listing"
        })

    return {
        "performance": {
            "impressions": impressions,
            "clicks": clicks,
            "ctr_pct": round(ctr, 2),
            "orders": orders,
            "cvr_pct": round(cvr, 2),
            "ad_spend": round(ad_spend, 2),
            "cpc": round(cpc, 4),
            "aov": round(aov, 2),
            "ad_revenue": round(ad_revenue, 2),
            "roas": round(roas, 2),
        },
        "vs_targets": {
            "ctr_target_pct": 2.0,
            "cvr_target_pct": 2.0,
            "roas_target": roas_fw["target_roas"],
            "break_even_roas": roas_fw["break_even_roas"],
        },
        "diagnosis": diagnosis,
    }


def build_parser():
    p = argparse.ArgumentParser(description="TEMU Ads Bid Calculator")
    p.add_argument("--mode", choices=["build", "full", "audit"], default="build",
                   help="build=basic ROAS / full=with ramp schedule / audit=optimize existing")
    p.add_argument("--price", type=float, required=True, help="Selling price USD")
    p.add_argument("--cost", type=float, required=True, help="Product cost USD (FOB+freight)")
    p.add_argument("--commission", type=float, default=0.10,
                   help="Platform commission rate (default 0.10 = 10%%)")
    p.add_argument("--return-rate", type=float, default=0.15,
                   help="Return rate (default 0.15 for electronics)")
    p.add_argument("--cvr", type=float, default=0.02,
                   help="Expected conversion rate (default 0.02 = 2%%)")
    p.add_argument("--budget", type=float, default=50,
                   help="Daily ad budget USD (default $50)")
    p.add_argument("--reviews", type=int, default=0, help="Current review count")
    p.add_argument("--monthly-sales", type=int, default=0, help="Current 30d sales")
    # Audit-only
    p.add_argument("--impressions", type=int, help="[audit] impressions")
    p.add_argument("--clicks", type=int, help="[audit] clicks")
    p.add_argument("--orders", type=int, help="[audit] orders")
    p.add_argument("--ad-spend", type=float, help="[audit] ad spend USD")
    return p


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = build_parser().parse_args()

    fin = calc_financial(args.price, args.cost, args.commission, args.return_rate)
    roas_fw = calc_roas_framework(args.price, args.cost, args.commission,
                                   args.return_rate, args.cvr)
    tier, tier_reason = recommend_tier(args.reviews, args.monthly_sales,
                                       roas_fw["target_roas"],
                                       roas_fw["break_even_roas"])
    ramp = build_ramp_schedule(args.budget, roas_fw["target_roas"],
                                roas_fw["break_even_roas"])

    expected_daily_clicks = args.budget / roas_fw["max_cpc_at_cvr"] \
        if roas_fw["max_cpc_at_cvr"] else 0
    expected_daily_orders = expected_daily_clicks * args.cvr

    warnings = []
    if roas_fw["break_even_roas"] > 10:
        warnings.append("?? 毛利率过低(<10%)，广告ROAS要求>10，投放风险极高")
    if args.budget < 20:
        warnings.append("?? 日预算<$20，平台分配流量有限，建议至少$30起")
    if roas_fw["max_cpc_at_cvr"] < 0.1:
        warnings.append("?? Max CPC < $0.10，平台可能不愿意给曝光")
    if fin["net_profit_no_ad"] <= 0:
        warnings.append("?? 不投广告都已亏损 — 先解决成本/定价问题")

    audit = None
    if args.mode == "audit":
        audit = run_audit(args)

    result = BidResult(
        mode=args.mode,
        inputs={k: v for k, v in vars(args).items() if v is not None},
        revenue_per_unit=fin["revenue"],
        cost_per_unit=fin["cost"],
        commission_per_unit=fin["commission_amt"],
        return_loss_per_unit=fin["return_loss_amt"],
        net_profit_per_unit_no_ad=fin["net_profit_no_ad"],
        break_even_roas=roas_fw["break_even_roas"],
        target_roas=roas_fw["target_roas"],
        target_acos=roas_fw["target_acos_pct"] / 100,
        max_cpc_at_cvr=roas_fw["max_cpc_at_cvr"],
        expected_daily_clicks=round(expected_daily_clicks, 1),
        expected_daily_orders=round(expected_daily_orders, 2),
        recommended_tier=tier,
        tier_reasoning=tier_reason,
        ramp_schedule=ramp,
        audit=audit,
        warnings=warnings,
    )

    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))

    print()
    print("== 摘要 ==")
    print(f"模式: {result.mode}")
    print(f"售价: ${result.revenue_per_unit}  成本: ${result.cost_per_unit}")
    print(f"无广告净利: ${result.net_profit_per_unit_no_ad} "
          f"({fin['margin_no_ad_pct']}%)")
    print(f"盈亏平衡 ROAS: {result.break_even_roas}")
    print(f"目标 ROAS (30%安全垫): {result.target_roas}")
    print(f"目标 ACoS: {result.target_acos*100:.1f}%")
    print(f"Max CPC (CVR {args.cvr*100:.1f}%): ${result.max_cpc_at_cvr}")
    print(f"推荐档位: {result.recommended_tier}")
    print(f"理由: {result.tier_reasoning}")
    print()
    print(f"日预算 ${args.budget}: 预期 {result.expected_daily_clicks} 点击 / "
          f"{result.expected_daily_orders} 单")
    if result.warnings:
        print()
        for w in result.warnings:
            print(w)

    if audit:
        print()
        print("== 审计结果 ==")
        perf = audit["performance"]
        print(f"ROAS: {perf['roas']} (目标 {audit['vs_targets']['roas_target']}, "
              f"盈亏平衡 {audit['vs_targets']['break_even_roas']})")
        for d in audit["diagnosis"]:
            print(f"{d['severity']} {d['issue']}: {d['cause']} → {d['fix']}")


if __name__ == "__main__":
    main()
