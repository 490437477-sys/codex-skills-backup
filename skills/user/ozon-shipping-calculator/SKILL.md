---
name: ozon-shipping-calculator
description: "Ozon shipping cost calculator for FBO and FBS fulfillment, including inbound shipping from China to Russian Ozon warehouses, last-mile delivery costs, returns processing, and cross-border consolidation routes. Includes CIS-specific factors: ruble volatility, EAC certification, Russian customs duty, BRICS trade routes, and RUB/KZT/BYN normalization. Use when the user asks about Ozon shipping cost, Ozon inbound from China, last-mile delivery cost on Ozon, 写芯褋褌邪胁泻邪 shipping to Russia, or CN to Russia freight for Ozon. **Default cross-border channel for this project: GUOO 官方合作物流, piecewise function 3.05+0.026x (x<500g) and 16.64+0.0364x (500≤x<2000g), CNY quoted.**"
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Shipping Calculator

Compute every Ozon shipping-related cost across FBO, FBS, and cross-border from China to Russia.

## Capabilities

- **FBO storage fee** by tier and season
- **FBO last-mile fee** by size tier and destination
- **FBS pick-and-pack + shipping label** cost
- **Inbound shipping (本项目默认)**: **GUOO 官方合作物流**（分段函数 3.05+0.026x / 16.64+0.0364x，CNY 报价）
- **Inbound shipping (备用)**: sea freight from Guangzhou / Yiwu / Shenzhen to Russian Ozon warehouses
- **Cross-border routes**: direct to Ozon, or via Kazakhstan / Belarus
- **Customs clearance**: Russian Customs duty + EAC conformity
- **Returns processing fee** for FBO and FBS
- **Currency normalization**: CNY / USD / INR -> RUB
- **Aged inventory surcharge** at Ozon FBO

## Workflow

### 1. Confirm marketplace and SKU dimensions
- Marketplace: Ozon.ru / Ozon.kz / Ozon.by
- SKU dimensions (cm) and weight (kg)
- Tier: Small / Medium / Large / XL

### 2. Compute FBO last-mile
Per-order delivery fee by tier + destination region. Moscow / SPB are cheaper than remote regions like Far East.

### 3. Compute FBS shipping
FBS shipping label: 60-300 RUB per order depending on destination and weight.
FBS pick-and-pack: 30-50 RUB per order.

### 4. Add inbound shipping

### From China via GUOO (Official partner, default for this project)

> **本项目默认跨境渠道 = GUOO 官方合作物流**（俄区 FBS 跨境直发）
> 详项目内权威源：[[Ozon物流计费规则卡（GUOO官方合作版·v1.0）]]

**分段计费函数（CNY，x = 计费重量 g）**

| 重量区间 | 公式 | 适用 |
| --- | --- | --- |
| x < 500 g | **3.05 + 0.026x** | 首饰/小配件/小工具 |
| 500 g ≤ x < 2000 g | **16.64 + 0.0364x** | 厨具/小家电/中等货 |
| x ≥ 2000 g | 大件单独询价 | 走 GUOO 大件渠道 |

**计费重量判定**

- 计费重量 = max(实重, 体积重)
- 体积重 = L×W×H cm / 6000（轻泡品 5000）
- 最低一票 3.05 CNY 起

**速算表（高频重量档）**

| 包裹重量 | 所在段 | GUOO 运费 (CNY) | 折 RUB（×12） |
| --- | --- | --- | --- |
| 100 g | 轻小件 | 5.65 | 67.8 |
| 300 g | 轻小件 | 10.85 | 130.2 |
| 500 g | 中件段（含） | 34.84 | 418.1 |
| 700 g | 中件段 | 42.12 | 505.4 |
| 1000 g | 中件段 | 53.04 | 636.5 |
| 1500 g | 中件段 | 71.24 | 854.9 |
| 1999 g | 中件段 | 89.40 | 1072.8 |

**SLA 时效（CN → RU 买家）**

- 国内揽收 → GUOO 集运仓：1-3 天
- 国际干线（铁路/卡航）：12-18 天
- 俄仓清关 + 入库 Ozon Rocket：3-7 天
- Ozon Rocket 尾程：1-4 天
- **全程 17-32 天**，旺季 +5-10 天
- 描述口径建议：`Доставка из Китая 18-30 дней`

**旺季加价**：春节 / 双 11 / 黑五前 30 天与 GUOO 客服确认是否上浮 5-15%

**币种换算**：GUOO 报价 CNY；按 1 CNY ≈ 12 ₽ 折算 RUB（项目默认汇率）；实际取实时 + 5% 缓冲

### From China (Guangzhou / Yiwu / Shenzhen)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Guangzhou -> Moscow (rail) | Rail via Manzhouli | 18-25 days | $80-150 |
| Yiwu -> Moscow (rail) | Rail | 20-28 days | $90-160 |
| Shenzhen -> St Petersburg (sea) | Sea (LCL) | 35-45 days | $60-100 |
| Guangzhou -> Vladivostok (sea) | Sea (LCL) | 15-20 days | $50-90 |
| Any China -> Russia (air) | Air (urgent) | 4-7 days | $5-8/kg |

### 5. Customs + conformity
- HS code lookup -> duty rate (5-15%)
- EAC conformity certificate: 5000-30000 RUB per SKU
- Russian import VAT (20%): reclaimable if seller is VAT-registered

### 6. Returns reserve
CIS returns run 8-15%. Reserve 10% of landed cost.

### 7. Total cost formula

```
Total landed cost (RUB) = FOB (CN) * RUB/CNY
                        + freight (GUOO 分段函数 → CNY → ×12)  ← 本项目默认
                          或 (sea / rail / air)  ← 备用方案
                        + Russian customs duty
                        + EAC certification (amortized)
                        + FBO storage (or FBS pick)
                        + FBO last-mile (or FBS shipping)
                        + Returns reserve
```

> [!IMPORTANT] **本项目默认 freight 项 = GUOO 分段函数**（详上节「From China via GUOO」）
> 不再用「占位 ₽200」「按 SKU 取均值」等粗略估算。x≥2000g 时必须先与 GUOO 客服议价再回填。

## Output

- **Per-order shipping cost** for FBO vs FBS
- **Inbound shipping + customs** per shipment
- **Returns reserve**
- **FBO vs FBS recommendation**

## Quick Mode

If user gives dimensions + weight + monthly orders: return only the per-order cost + recommendation.

**GUOO 一键调用模板**

```markdown
$ozon-shipping-calculator
项目: GUOO 跨境运费测算
输入:
  - 产品净重（含内包装）: X g
  - 包装尺寸: L × W × H cm
输出（按 GUOO 分段函数）:
  1) 体积重 = L*W*H / 6000 = V g（轻泡品用 5000）
  2) 计费重量 = max(X, V) = x g
  3) GUOO 运费 CNY:
     - x < 500:  3.05 + 0.026*x
     - 500≤x<2000: 16.64 + 0.0364*x
     - x ≥ 2000: 大件询价
  4) 折算 RUB = GUOO_CNY * 12
  5) 折算 USD = GUOO_CNY / 7.2
  6) 全程时效 17-32 天
```

**多 SKU 批量对比**

```markdown
$ozon-shipping-calculator
对以下重量分别测算 GUOO 运费：[100, 300, 500, 700, 1000, 1500] g，
按本项目分段函数：x<500g → 3.05+0.026x；500≤x<2000g → 16.64+0.0364x；
输出每档的 CNY 与 RUB（×12）。
```

**定价反推用法**

```markdown
$ozon-shipping-calculator
已知 Ozon 售价 ₽Y，Ozon 佣金 c%，VAT 20%，FOB CN¥Z，
SKU 实重 X g，包装尺寸 L×W×H。
按 GUOO 分段函数倒推：净收入、净利润、净利率。
```

---

## GUOO 模式自动识别（v2.0 · 2026-06 ARM4 实战沉淀）

**何时自动调用 GUOO 分段函数**：

| 触发条件 | 是否走 GUOO | 备注 |
| --- | --- | --- |
| 卖家模式 = **Ozon Global 跨境店**（方案 D） | ✅ **强制走 GUOO** | 跨境店唯一指定物流 |
| 卖家模式 = 中国公司 / 俄公司 / 香港公司 + **履约 = FBS** | ✅ 默认走 GUOO | 本项目首选 |
| 卖家模式 = 中国公司 / 俄公司 / 香港公司 + **履约 = FBO** | ❌ 不走 GUOO | FBO 走 Ozon Rocket（俄仓 → 买家） |
| 包裹重量 ≥ 2000g | ⚠️ GUOO 大件渠道 | 须先与 GUOO 客服议价再回填 |

**跨境店 GUOO 强制校验（不可绕过）**：

- **描述必含**：`Доставка из Китая 18-30 дней`（详 GUOO 规则卡 §四）
- **时效承诺**：17-32 天（旺季 +5-10 天）
- **计费币种**：GUOO 报 CNY；折 RUB 按 1 CNY ≈ 12 ₽（项目默认汇率，实际取实时 + 5% 缓冲）

**ARM4 v2.0 实战用例**：

```markdown
$ozon-shipping-calculator
项目: ARM4 预装 5 轴机械臂套件（Ozon Global 跨境店）
输入:
  - SKU: ARM4-2026-003
  - 实重: 900 g（含包装）
  - 包装尺寸: 25 × 18 × 12 cm
  - 履约模式: 永久 FBS 跨境直发（方案 D）
输出:
  - 体积重 = 25*18*12/6000 = 900 g
  - 计费重量 = max(900, 900) = 900 g（中件段）
  - GUOO 运费 CNY = 16.64 + 0.0364*900 = 49.40 CNY
  - 折 RUB = 49.40 * 12 = 592.80 ₽（取整 593 ₽）
  - 折 USD = 49.40 / 7.2 = 6.86 USD
  - 全程时效 17-32 天（旺季 +5-10 天）
  - 描述必含: "Доставка из Китая 18-30 дней"
```

**PC4-M6 实战用例（轻小件段）**：

```markdown
$ozon-shipping-calculator
项目: MAKEREAL PC4-M6 4 件套
输入:
  - SKU: MK-PC4M6-2026-002
  - 实重: 80 g
  - 包装尺寸: 12 × 8 × 3 cm
  - 履约模式: FBS 自发货（90 天后转 FBO）
输出:
  - 体积重 = 12*8*3/6000 = 48 g
  - 计费重量 = max(80, 48) = 80 g（轻小件段）
  - GUOO 运费 CNY = 3.05 + 0.026*80 = 5.13 CNY
  - 折 RUB = 5.13 * 12 = 61.56 ₽（取整 62 ₽）
  - 净利率上修 +16 个百分点（vs 原 Ozon Rocket 占位 86 ₽）
```

**俄式厨刀 6 件套 实战用例（中件段临界）**：

```markdown
$ozon-shipping-calculator
项目: MAKEREAL 俄式厨刀 6 件套
输入:
  - SKU: MK-KN-2026-001
  - 实重: 1200 g
  - 包装尺寸: 35 × 25 × 8 cm
  - 履约模式: FBS 自发货（90 天后转 FBO）
输出:
  - 体积重 = 35*25*8/6000 = 1167 g
  - 计费重量 = max(1200, 1167) = 1200 g（中件段）
  - GUOO 运费 CNY = 16.64 + 0.0364*1200 = 60.32 CNY
  - 折 RUB = 60.32 * 12 = 723.84 ₽（取整 724 ₽）
  - 替代原 Ozon Rocket 占位 ¥25 / 180 ₽（差异 +¥35 / +544 ₽）
```

> [!info] 跨工具一致性
> - **GUOO 权威源**：`G:\ozon产品listing制作\99 - 元数据\Ozon物流计费规则卡（GUOO官方合作版·v1.0）.md`
> - **本 skill 公式**：与权威源 100% 一致
> - **9 档速算表**：与权威源 §二 100% 一致
> - **任何 GUOO 调价 / 抛比调整 / 时效变动都必须同步更新两边**