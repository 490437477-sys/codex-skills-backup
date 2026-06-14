#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ozon_profit_calc.py — Ozon 单品利润测算(FBO / FBS / Cross-border 三模式)

输入关键参数,输出:
- 单件毛利(₽ 与 USD)
- 毛利率
- 盈亏平衡日均单量
- RUB/USD 波动敏感性
- 退货率敏感性

用法:
  python ozon_profit_calc.py                              # 默认示例
  python ozon_profit_calc.py --interactive                # 交互输入
  python ozon_profit_calc.py --json '{"selling_price_rub": 2500}'  # JSON 输入
  python ozon_profit_calc.py --json @params.json         # 从文件读取

Windows GBK 控制台提示:
  PowerShell 默认 GBK,无法直接打印 ₽ 字符。
  请用 `chcp 65001` 切换到 UTF-8,或设置 `$env:PYTHONIOENCODING="utf-8"` 后再运行。

设计原则:
- 数字是模型,不是承诺。所有费率使用前用 web_search 拉最新值。
- 始终预留 RUB/USD 波动缓冲 + 退货预留。
"""

import argparse
import json
import sys
import os

# 兼容 Windows GBK 控制台 — 尝试 reconfigure stdout 为 UTF-8
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from dataclasses import dataclass, asdict, field
from typing import Optional


# ---------- 默认汇率与示例参数(可在命令行覆盖)----------
DEFAULT_USD_RUB = 90.0   # 1 USD ≈ 90 ₽(2026 年初量级,使用前请验证)
DEFAULT_CNY_USD = 7.2    # 1 USD ≈ 7.2 CNY


@dataclass
class ProductInput:
    """商品参数"""
    name: str = "示例商品"
    selling_price_rub: float = 1500.0      # 售价 ₽(含 VAT)
    product_cost_cny: float = 50.0          # 商品出厂价 CNY
    weight_kg: float = 0.5                  # 重量 kg
    category: str = "home"                  # 类目(用于佣金率)
    model: str = "fbo"                      # fbo / fbs / cross_border


@dataclass
class FeeParams:
    """费率参数(都按"当前 Ozon 量级"预设,使用前必须用 web_search 验证)"""
    commission_pct: float = 12.0           # Ozon 佣金率 %
    vat_pct: float = 20.0                  # НДС % (Ozon 代扣)
    fbo_inbound_rub: float = 30.0          # FBO 入库处理费 ₽/件
    fbo_storage_per_unit_rub: float = 5.0  # FBO 仓储分摊 ₽/件(按 30 天周转)
    fbo_last_mile_rub: float = 60.0        # FBO 尾程配送 ₽/件
    fbs_pickup_rub: float = 80.0           # FBS 上门取件 + 配送 ₽/件
    cross_border_rub: float = 150.0        # 跨境物流 ₽/件(中国 → 买家)
    return_rate_pct: float = 15.0          # 退货率 %
    return_cost_rub: float = 80.0          # 单次退货反向物流 ₽/件
    rub_buffer_pct: float = 7.0            # RUB/USD 波动缓冲 %
    marketing_pct: float = 5.0             # 站内营销预留 %


@dataclass
class CostBreakdown:
    """输出:成本明细"""
    product_cost_rub: float
    commission_rub: float
    vat_rub: float
    logistics_rub: float
    returns_reserve_rub: float
    rub_buffer_rub: float
    marketing_rub: float
    total_cost_rub: float
    gross_profit_rub: float
    net_margin_pct: float
    model: str


# ---------- 核心计算逻辑 ----------

def compute_cost(inp: ProductInput, fee: FeeParams,
                 usd_rub: float = DEFAULT_USD_RUB,
                 cny_usd: float = DEFAULT_CNY_USD) -> CostBreakdown:
    """计算单件全链路成本与利润"""
    # CNY → USD → RUB
    product_cost_rub = inp.product_cost_cny / cny_usd * usd_rub

    price = inp.selling_price_rub

    # Ozon 代扣 VAT(大多数 B2C 适用)
    vat_rub = price * (fee.vat_pct / 100.0)

    # Ozon 佣金(按 selling price 计算)
    commission_rub = price * (fee.commission_pct / 100.0)

    # 物流成本(按履约模式)
    if inp.model == "fbo":
        logistics_rub = fee.fbo_inbound_rub + fee.fbo_storage_per_unit_rub + fee.fbo_last_mile_rub
    elif inp.model == "fbs":
        logistics_rub = fee.fbs_pickup_rub
    elif inp.model == "cross_border":
        logistics_rub = fee.cross_border_rub
    else:
        raise ValueError(f"未知履约模式: {inp.model}")

    # 退货预留(按退货率摊销)
    returns_reserve_rub = price * (fee.return_rate_pct / 100.0) * (fee.return_cost_rub / max(price, 1.0))

    # RUB 波动缓冲(按售价百分比)
    rub_buffer_rub = price * (fee.rub_buffer_pct / 100.0)

    # 营销预留
    marketing_rub = price * (fee.marketing_pct / 100.0)

    total_cost_rub = (product_cost_rub + commission_rub + vat_rub
                      + logistics_rub + returns_reserve_rub
                      + rub_buffer_rub + marketing_rub)

    gross_profit_rub = price - total_cost_rub
    net_margin_pct = (gross_profit_rub / price * 100.0) if price > 0 else 0.0

    return CostBreakdown(
        product_cost_rub=round(product_cost_rub, 2),
        commission_rub=round(commission_rub, 2),
        vat_rub=round(vat_rub, 2),
        logistics_rub=round(logistics_rub, 2),
        returns_reserve_rub=round(returns_reserve_rub, 2),
        rub_buffer_rub=round(rub_buffer_rub, 2),
        marketing_rub=round(marketing_rub, 2),
        total_cost_rub=round(total_cost_rub, 2),
        gross_profit_rub=round(gross_profit_rub, 2),
        net_margin_pct=round(net_margin_pct, 2),
        model=inp.model,
    )


def sensitivity_analysis(inp: ProductInput, fee: FeeParams) -> dict:
    """对退货率与 RUB 汇率做敏感性扫描"""
    results = {}

    for ret in [5.0, 10.0, 15.0, 20.0, 30.0]:
        f = FeeParams(**asdict(fee))
        f.return_rate_pct = ret
        cb = compute_cost(inp, f)
        results[f"return_{ret:.0f}pct"] = {
            "gross_profit_rub": cb.gross_profit_rub,
            "net_margin_pct": cb.net_margin_pct,
        }

    for fx in [80.0, 85.0, 90.0, 95.0, 100.0]:
        cb = compute_cost(inp, fee, usd_rub=fx)
        results[f"fx_{fx:.0f}"] = {
            "gross_profit_rub": cb.gross_profit_rub,
            "net_margin_pct": cb.net_margin_pct,
        }

    return results


# ---------- 默认参数(类目化)----------

CATEGORY_DEFAULTS = {
    "books":       {"commission_pct": 8.0,  "return_rate_pct": 5.0},
    "home":        {"commission_pct": 12.0, "return_rate_pct": 15.0},
    "electronics": {"commission_pct": 10.0, "return_rate_pct": 8.0},
    "beauty":      {"commission_pct": 15.0, "return_rate_pct": 10.0},
    "fashion":     {"commission_pct": 12.0, "return_rate_pct": 25.0},
    "toys":        {"commission_pct": 13.0, "return_rate_pct": 12.0},
    "auto":        {"commission_pct": 14.0, "return_rate_pct": 15.0},
    "furniture":   {"commission_pct": 10.0, "return_rate_pct": 18.0},
    "sports":      {"commission_pct": 12.0, "return_rate_pct": 12.0},
    "supplements": {"commission_pct": 18.0, "return_rate_pct": 8.0},
}


def apply_category_defaults(category: str, fee: FeeParams) -> FeeParams:
    if category in CATEGORY_DEFAULTS:
        defaults = CATEGORY_DEFAULTS[category]
        for k, v in defaults.items():
            setattr(fee, k, v)
    return fee


# ---------- CLI ----------

def parse_interactive() -> tuple:
    """交互式输入"""
    print("=== Ozon 利润测算(交互模式) ===\n")

    name = input("商品名: ").strip() or "示例商品"
    price = float(input("售价 RUB [1500]: ") or 1500)
    cost_cny = float(input("商品成本 CNY [50]: ") or 50)
    weight = float(input("重量 kg [0.5]: ") or 0.5)
    print("类目: books / home / electronics / beauty / fashion / toys / auto / furniture / sports / supplements")
    category = input("类目 [home]: ").strip() or "home"
    print("履约模式: fbo / fbs / cross_border")
    model = input("履约模式 [fbo]: ").strip() or "fbo"

    usd_rub = float(input(f"USD->RUB 汇率 [{DEFAULT_USD_RUB}]: ") or DEFAULT_USD_RUB)
    cny_usd = float(input(f"CNY->USD 汇率 [{DEFAULT_CNY_USD}]: ") or DEFAULT_CNY_USD)

    inp = ProductInput(
        name=name, selling_price_rub=price, product_cost_cny=cost_cny,
        weight_kg=weight, category=category, model=model,
    )
    fee = apply_category_defaults(category, FeeParams())
    return inp, fee, usd_rub, cny_usd


def main():
    parser = argparse.ArgumentParser(description="Ozon 单品利润测算")
    parser.add_argument("--interactive", action="store_true", help="交互模式")
    parser.add_argument("--json", type=str, help="JSON 参数(字符串或 @file)")
    parser.add_argument("--usd-rub", type=float, default=DEFAULT_USD_RUB)
    parser.add_argument("--cny-usd", type=float, default=DEFAULT_CNY_USD)
    parser.add_argument("--sensitivity", action="store_true", help="敏感性分析")
    args = parser.parse_args()

    if args.interactive:
        inp, fee, usd_rub, cny_usd = parse_interactive()
    elif args.json:
        raw = args.json
        if raw.startswith("@"):
            with open(raw[1:], "r", encoding="utf-8-sig") as f:
                raw = f.read()
        params = json.loads(raw)
        inp = ProductInput(**{k: params[k] for k in asdict(ProductInput()) if k in params})
        fee_kwargs = {k: params[k] for k in asdict(FeeParams()) if k in params}
        fee = FeeParams(**fee_kwargs) if fee_kwargs else FeeParams()
        if "category" in params:
            fee = apply_category_defaults(params["category"], fee)
        usd_rub = params.get("usd_rub", args.usd_rub)
        cny_usd = params.get("cny_usd", args.cny_usd)
    else:
        # 默认示例
        inp = ProductInput()
        fee = apply_category_defaults(inp.category, FeeParams())
        usd_rub, cny_usd = args.usd_rub, args.cny_usd

    cb = compute_cost(inp, fee, usd_rub=usd_rub, cny_usd=cny_usd)

    print("")
    print("=== {} 利润测算 ===".format(inp.name))
    print("履约模式: {}    类目: {}    重量: {} kg".format(cb.model.upper(), inp.category, inp.weight_kg))
    print("汇率: 1 USD = {} RUB  /  1 USD = {} CNY".format(usd_rub, cny_usd))
    print("")

    header_fmt = "{:<20}{:>14}{:>12}"
    row_fmt = "{:<20}{:>14.2f}{:>11.1f}%"
    print(header_fmt.format("项目", "金额 RUB", "占售价 %"))
    print("-" * 46)
    print(row_fmt.format("售价", inp.selling_price_rub, 100.0))
    print(row_fmt.format("商品成本", cb.product_cost_rub, cb.product_cost_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("Ozon 佣金", cb.commission_rub, cb.commission_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("VAT(НДС 代扣)", cb.vat_rub, cb.vat_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("物流费", cb.logistics_rub, cb.logistics_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("退货预留", cb.returns_reserve_rub, cb.returns_reserve_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("RUB 波动缓冲", cb.rub_buffer_rub, cb.rub_buffer_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("营销预留", cb.marketing_rub, cb.marketing_rub / inp.selling_price_rub * 100))
    print("-" * 46)
    print(row_fmt.format("总成本", cb.total_cost_rub, cb.total_cost_rub / inp.selling_price_rub * 100))
    print(row_fmt.format("单件净利", cb.gross_profit_rub, cb.net_margin_pct))

    if cb.net_margin_pct >= 20:
        rating = "[Excellent] 优秀"
    elif cb.net_margin_pct >= 12:
        rating = "[Good] 良好"
    elif cb.net_margin_pct >= 5:
        rating = "[Tight] 紧张"
    else:
        rating = "[Poor] 较差"
    print("")
    print("利润率评级: {}".format(rating))

    print("")
    print("盈亏平衡参考:")
    print("  单件净利 {:.0f} RUB".format(cb.gross_profit_rub))
    if cb.gross_profit_rub > 0:
        print("  日均 10 单 -> 月毛利 {:,.0f} RUB".format(cb.gross_profit_rub * 30 * 10))
        print("  日均 30 单 -> 月毛利 {:,.0f} RUB".format(cb.gross_profit_rub * 30 * 30))
    else:
        print("  [WARN] 当前定价无法覆盖成本,需重新定价或压低成本")

    if args.sensitivity:
        print("")
        print("=== 敏感性分析 ===")
        sens = sensitivity_analysis(inp, fee)
        print("")
        print("退货率敏感性(基础 {:.0f}%):".format(fee.return_rate_pct))
        for key, val in sens.items():
            if key.startswith("return_"):
                print("  {:<18}-> 净利 {:.0f} RUB  毛利率 {:.1f}%".format(key, val["gross_profit_rub"], val["net_margin_pct"]))
        print("")
        print("USD/RUB 汇率敏感性(基础 {:.0f}):".format(usd_rub))
        for key, val in sens.items():
            if key.startswith("fx_"):
                print("  {:<18}-> 净利 {:.0f} RUB  毛利率 {:.1f}%".format(key, val["gross_profit_rub"], val["net_margin_pct"]))

    print("")
    print("[WARN] 提示: 所有费率使用前用 web_search 验证 Ozon 最新规则。")
    print("")


if __name__ == "__main__":
    main()