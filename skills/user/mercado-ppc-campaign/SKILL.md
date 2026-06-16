---
name: mercado-ppc-campaign
description: "Mercado Ads (美客多广告) campaign builder and optimizer for cross-border sellers. Two modes: (A) Build — design a complete Mercado Ads structure (Product Ads + Brand Ads + Display Ads) with ROAS-target bidding and budget allocation for Mexico/Brazil/Chile/Colombia, (B) Optimize — audit existing Mercado Ads campaigns, calculate target ROAS (2025-2026 ACoS→ROAS pivot), identify wasted spend, generate bid adjustment plan. Integrates with mercado-keyword-research (for keyword input) and mercado-listing-optimization (for pre-launch listing quality). Use when: (1) launching Mercado Ads for a new 美客多 product, (2) setting up Product Ads / Brand Ads / Display Ads, (3) calculating target ROAS / break-even ROAS, (4) optimizing existing campaigns, (5) preparing for Hot Sale / El Buen Fin / Black Friday, (6) managing PML (Product Listing Ads) budgets, (7) migrating from ACoS to ROAS-first strategy."
metadata: {"emoji":"📢","category":"mercadolibre"}
---

# Mercado Ads (美客多广告) Campaign Optimization 📢

Build profitable Mercado Ads campaign structures from scratch, or audit and optimize existing ones. Native ROAS-first framework (2025-2026 pivot). No API key required.

## ⚠️ 2025-2026 重大变化: 从 ACoS 到 ROAS

Mercado Ads 正在从 ACoS 转向 **ROAS (Return on Ad Spend)** 作为核心指标。这是2025下半年开始的**重大算法更新**。

| 指标 | 公式 | 解读 | 状态 |
|------|------|------|------|
| **ACoS** (旧) | Ad Spend / Ad Revenue × 100% | 广告占总销售成本 | 🔴 **正在被淘汰** |
| **ROAS** (新) | Ad Revenue / Ad Spend | 每$1广告费带来多少销售额 | 🟢 **2025+主推** |

**简单换算**: ROAS = 1 / ACoS (作为小数)
- 25% ACoS = 4.0x ROAS
- 50% ACoS = 2.0x ROAS
- 75% ACoS = 1.33x ROAS

**Mexican agency共识 (2025-2026)**: ROAS比ACoS更精确,因为它直接告诉你**每花$1广告能回收多少**,而ACoS告诉你**广告吃掉多少毛利**。本skill默认使用ROAS框架,旧ACoS数据用括号标注便于对比。

## When to Use

Activate this skill whenever the user mentions:
- 美客多广告, 美客多付费推广, Mercado Ads, Publicidad MercadoLibre
- 美客多 PML, Product Listing Ads, Product Ads
- 投放美客多广告, 美客多ROAS, 美客多ACoS
- 美客多大促广告, Hot Sale广告, El Buen Fin广告
- 优化美客多广告, 降低美客多ACoS
- 美客多DSP, Brand Ads, Display Ads

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Build** | 启动新美客多产品广告 | 产品信息 + 关键词 + 利润率 | 完整广告蓝图 + 预算分配 + 初始ROAS目标 |
| **B — Optimize** | 优化已有广告 | 广告数据 + 搜索词报告 + 当前ROAS/ACoS | 优化方案 + 出价调整 + 否词列表 + 周计划 |

## Capabilities

- **ROAS财务框架**: 计算 break-even ROAS、target ROAS、Max CPC — 每次出价决策的基础
- **Campaign架构设计**: Product Ads + Brand Ads + Display Ads 三层漏斗,带层级预算分配
- **Product Ads优化**: 手动CPC vs 自动化ROAS目标两种策略对比
- **Catalog竞争型广告**: 利用"首购选项"竞争机制
- **预算分配规则**: Hot Sale / El Buen Fin 旺季预算翻倍策略
- **Brand Ads防御**: 品牌词 + 竞品词 (LATAM品牌战非常有效)
- **Display Ads再营销**: 平台内再营销 + 外部流量
- **负向管理**: 跨campaign的浪费词/不相关词
- **搜索词报告分析**: 找出高效词和浪费词
- **2025-2026 ACoS→ROAS迁移路径**: 自动换算历史数据
- **Multi-marketplace**: MX, BR, CL, CO, AR

## Mercado Ads vs Amazon PPC 关键差异

| 维度 | Amazon PPC | Mercado Ads | 启示 |
|------|-----------|-------------|------|
| Ad类型 | Sponsored Products/Brands/Display | Product Ads / Brand Ads / Display Ads | 概念对应 |
| 关键词匹配 | Broad/Phrase/Exact | **无显式匹配类型** — 算法基于相关性 | 简化,但不能锁精准 |
| Auto campaign | ✅ (Amazon特有) | ❌ 不存在 | 需要用户自己提供关键词 |
| 出价模型 | Manual / Dynamic bids down/up | Manual CPC / **Automated ROAS target** | ROAS目标更优 |
| 核心指标 | ACoS | **ROAS** (2025+主推) | 必须掌握换算 |
| A/B Testing | ✅ 官方Manage Your Experiments | ❌ 不存在 | 一次到位 |
| 品牌广告 | Sponsored Brands | Brand Ads (低成本) | 拉美品牌战利器 |
| 外部流量 | 几乎不可 | ✅ Display Ads可投外部 | 站外引流 |
| 货币 | 12种 | MXN/BRL/CLP/COP/ARS | 拉美本地化 |

**重要启示**: Mercado Ads比Amazon PPC**更简单**(无Auto/Broad/Exact)但**算法黑盒更强**(无官方匹配类型)。需要**更高质量的listing + 关键词清单**作为输入。

## Usage Examples

### Mode A — Build New Campaigns

```
我是新卖家,准备给"创客机械臂"(brazo robótico)在美客多墨西哥站投广告
售价 1899 MXN, 产品成本 550 MXN, 佣金 16.5% Premium, 物流 80 MXN
预算 1500 MXN/月,目标是7个月内盈利
给我建一个完整 Mercado Ads 结构
```

```
Use mercado-keyword-research output for "audífonos bluetooth" on Mercado Libre Mexico
Product: 蓝牙5.3 40h续航 IPX5
Margin: 25% (含佣金+物流+MP)
Build me a Product Ads + Brand Ads structure
```

### Mode B — Optimize Existing

```
我的美客多广告ACoS是48%,target应该30%。3个Product Ads campaigns总预算$800/月
产品毛利率22%。帮我优化到ROAS 4.5x
```

```
Hot Sale前3个月,我的Product Ads ROAS从5.2掉到2.8,怎么办
```

### Short Prompts Work Too

```
帮我建美客多广告 for my product
```
```
我的美客多ROAS太低,帮我优化
```

---

## How This Skill Collects Information

**Progressive information gathering** approach:

**Step 1**: 从用户prompt抽取已有信息(价格、ROAS、campaign数等)

**Step 2**: Auto-discover(用 tavily / web search):
- 品类在美客多的建议CPC区间
- Top竞品广告位分析
- 类目平均ROAS benchmark
- 当季流量峰值预判

**Step 3**: 询问最少必要信息(避免无意义问答)

## Mode A Workflow — Build New Mercado Ads Campaigns

### Step A1: 计算关键财务指标 ⭐ 必做

**输入: 产品经济模型** (用户必须提供)

```
售价 (MXN/BRL)
- 产品成本 (1688/工厂)
- 美客多佣金 (Classic 12.5% / Premium 16.5%)
- 低价位附加费 (BR ≤R$79, CL ≤$15,650)
- Mercado Pago 3.99%
- 物流 (自发货 25天 vs Full)
- 包装+杂费
= 净利率 %
```

**计算公式**:

```
毛利金额 = 售价 - 产品成本 - 平台佣金 - 物流 - 杂费
净利率 = 毛利金额 / 售价

Break-even ROAS = 1 / 净利率 (假设广告费 = 全部毛利)
Target ROAS = Break-even ROAS × 1.5~2.0 (留安全垫)

Max CPC = 售价 × 净利率 × 目标CTR × 目标CVR
(经验值: 大部分类目目标CTR 1-3%, 目标CVR 2-5%)
```

**Example: 创客机械臂 (Mexico)**
- 售价 1899 MXN, 产品成本 550, 佣金 16.5% (313), MP 3.99% (76), Full物流 80, 杂费 30
- 毛利 = 1899 - 550 - 313 - 76 - 80 - 30 = **850 MXN**
- 净利率 = 850 / 1899 = **44.8%** ✓
- Break-even ROAS = 1 / 0.448 = **2.23x**
- Target ROAS = 2.23 × 1.7 = **3.8x** (安全垫 70%)
- Max CPC = 1899 × 0.448 × 0.02 × 0.03 = **5.1 MXN** (CTR 2%, CVR 3%)

### Step A2: 选择Campaign结构(三大类组合)

**3大产品/3大站点 矩阵**:

| 站点 | 起步结构 | 成熟期结构 | 旺季结构 |
|------|---------|-----------|---------|
| **Mexico** | Product Ads x1 | Product Ads x2 + Brand Ads x1 + Display x1 | + Display外部 |
| **Brazil** | Product Ads x1 | Product Ads x2 + Brand Ads x1 | + Display |
| **Chile** | Product Ads x1 | Product Ads + Brand Ads | 单一 |
| **Colombia** | Product Ads x1 | Product Ads + Brand Ads | 单一 |

**Campaign结构详解**:

#### 🅰️ Product Ads (主要转化器)
- **类型**: 类Amazon Sponsored Products — 在搜索结果中显示带"Publicidad"/"Sponsor"标签的商品
- **核心目标**: 直接销售
- **适用阶段**: 全周期

**两种Bidding策略**:
- **Manual CPC**: 卖家手动出价,平台优化有限
- **Automated ROAS target** (推荐): 平台基于target ROAS自动调价
  - 新品起步: target ROAS = break-even × 1.5
  - 成熟期: target ROAS = 行业top 25%水平
  - 大促期: 临时降低target ROAS抢量

#### 🅱️ Brand Ads (品牌防御 + 关键词)
- **类型**: 类Amazon Sponsored Brands — 关键词+品牌logo+多商品
- **核心目标**: 品牌曝光 + 竞品防御
- **适用阶段**: 已有品牌词的成熟期

**LATAM特色**:
- 拉美用户**品牌搜索弱于Amazon**,所以Brand Ads CPC通常很低(0.5-2 MXN)
- 强烈建议**所有新卖家都开Brand Ads**,即使品牌不响,也能低价抢曝光

#### 🅲️ Display Ads (再营销 + 外部流量)
- **类型**: 类Amazon DSP — 平台内+平台外banner广告
- **核心目标**: 触达 / 再营销 / 品牌认知
- **适用阶段**: 成熟期+旺季

**两种用法**:
- **平台内再营销**: 看过/加购/未购买的用户 (高ROAS)
- **外部流量**: Mercado Libre的ad network (Google, Facebook, etc.) (低ROAS但拉新)

### Step A3: 产品分组(关键决策)

Mercado Ads允许**按产品分组**做campaign,分组逻辑:

| 分组维度 | 适用场景 | 优劣势 |
|---------|---------|--------|
| **按SKU单组** | 新品测试 / 高客单 | 精准控,数据干净,管理成本高 |
| **按品类分组** | 多SKU成熟期 | 效率高,数据交叉污染 |
| **按价格段分组** | 高/中/低三档 | 匹配不同客群,优化细分 |
| **按Full仓库存** | 旺季优先 | 突出Full物流优势 |
| **按Catalog竞争** | 抢"首购选项" | 跟其他卖家直接竞争展示位 |

**推荐路径**:
- 新品: 1 Product = 1 Campaign
- 多SKU: 同品类(3-15 SKU)= 1 Campaign
- 旺季节: Full仓产品单独Campaign (享受流量倾斜)

### Step A4: 预算分配规则

**月度总预算拆分**(总预算 = $X):

| Campaign | 占比 | 月预算 | 角色 |
|----------|------|--------|------|
| Product Ads - 主力 | 50-60% | $X | 主转化器 |
| Product Ads - 拓品 | 15-20% | $X | 测试新品/长尾 |
| Brand Ads | 15-20% | $X | 品牌词 + 防御 |
| Display Ads | 5-10% | $X | 再营销 |
| **合计** | 100% | $X | |

**季节调整**:
- 旺季前1月: 总预算 × 1.5-2.0
- 旺季当月: 总预算 × 2.0-3.0 (Hot Sale / El Buen Fin / Black Friday)
- 淡季: 总预算 × 0.6-0.8

**起步预算建议**(按产品周期):
- Week 1-2: $5-10 USD/天 (测试,50+ impressions)
- Week 3-4: $10-20 USD/天 (加码表现好campaign)
- Month 2+: $20-50 USD/天 (基于ROAS)

### Step A5: 关键词/定向策略

**Product Ads的"关键词"概念不同于Amazon**:
- Product Ads基于listing的相关性自动匹配搜索
- 卖家**不能直接选择关键词**(无Exact/Broad/Phrase)
- 但可以通过**listing优化**间接影响匹配

**间接优化方法**:
1. **Título优化**: 把核心关键词放最前(来自mercado-keyword-research)
2. **Ficha Técnica填全**: 类目属性100%填满
3. **Negative listing**: 把效果差的listing退出campaign
4. **Brand Ads补充**: Brand Ads可显式选词,补充长尾

**Brand Ads关键词选择**(用mercado-keyword-research输出):
- 品牌词 (Tu marca): "TuMarca" / "Tu Marca"
- 变体: 拼写错误 / 复数形式
- 竞品品牌词(仅成熟期)
- 长尾词: 用高商业意图词

### Output: 完整Campaign蓝图

```markdown
# ✅ Mercado Ads 蓝图 — Ready to Launch

## 产品经济模型
| 项目 | MXN | % |
|------|-----|---|
| 售价 | [X] | 100% |
| 产品成本 | [X] | [X]% |
| 平台佣金 | [X] | [X]% |
| Mercado Pago | [X] | [X]% |
| 物流 | [X] | [X]% |
| 杂费 | [X] | [X]% |
| **净利率** | **[X]** | **[X]%** |

## 关键ROAS指标
- **Break-even ROAS**: [X]x (广告费 = 全部毛利)
- **Target ROAS**: [X]x (安全垫 [X]%)
- **Max CPC**: [X] MXN
- **ACoS等同**: [X]% (公式 1/ROAS × 100)

## Campaign 1: [品牌] - Product Ads 主力
**Type**: Product Ads
**Bidding**: Automated ROAS Target = [X]x
**Daily Budget**: [X] MXN
**Monthly**: [X] MXN

**Ad Group**: [品类/价格段]
- 包含产品: [SKU列表]
- 默认Bid: [X] MXN (Max CPC × 0.7-0.9)
- Negative listings: [效果差的SKU]

## Campaign 2: [品牌] - Brand Ads 防御
**Type**: Brand Ads
**Daily Budget**: [X] MXN
**Monthly**: [X] MXN

**Keywords**:
- [品牌词] | Manual bid [X] MXN
- [品牌词变体] | Manual bid [X] MXN
- [竞品品牌词] | Manual bid [X] MXN
- [Top 5 长尾词] | Manual bid [X] MXN

**Negative keywords**:
- [不相关词] | [无关品类]
- [incompatible products]

## Campaign 3: [品牌] - Display 再营销
**Type**: Display Ads
**Daily Budget**: [X] MXN
**Monthly**: [X] MXN

**Audience**:
- 看过我产品: [30天]
- 加购未买: [14天]
- 平台内相似用户: [lookalike]

## 预算汇总
| Campaign | Type | Daily | Monthly | ROAS目标 |
|----------|------|-------|---------|---------|
| Product Ads 主力 | PML | $X | $X | [X]x |
| Brand Ads | Brand | $X | $X | [X]x |
| Display | Retarget | $X | $X | [X]x |
| **总计** | | **$X** | **$X** | **[X]x** |

## 启动时间表
**Week 1**: 创建 Campaign 1 (Product Ads) + 设置 ROAS target,观察48小时
**Week 2**: 检查impressions,若<1000/天则提高bid
**Week 3**: 加 Campaign 2 (Brand Ads) — 用西/葡语品牌词
**Week 4**: 第一次ROAS检查,调整target + 加 Campaign 3 (Display)
**Week 5+**: 持续监控,看下面 Mode B 的周计划

## ROI预估
- 月度广告投入: $X
- 预计月销售额: $X (按target ROAS)
- 预计月毛利贡献: $X (净利 - 广告费)
- 预计月订单数: $X
```

## Mode B Workflow — Optimize Existing Mercado Ads

### Step B1: 拉取并解析数据

用户提供:
- 当前所有 Product Ads / Brand Ads / Display campaigns 的数据(尽量提供)
- 或者: 截图 Mercado Ads 后台 (从图表提取关键数据)
- 关键指标: impressions, clicks, CTR, CPC, conversions, ROAS, ACoS(换算), spend, revenue

### Step B2: 计算当前vs目标ROAS gap

| 指标 | 当前 | 目标 | Gap |
|------|------|------|-----|
| Overall ROAS | [X]x | [X]x | [±] |
| Spend efficiency | [X] | [X] | — |
| 单SKU ROAS Top 3 | [X]/[X]/[X] | — | — |
| 单SKU ROAS Bottom 3 | [X]/[X]/[X] | — | — |

### Step B3: ROAS分段诊断

| ROAS范围 | 评估 | 行动 |
|---------|------|------|
| **> 5.0x** (ACoS <20%) | 🟢 优秀 | 加预算 20-30% |
| **3.5-5.0x** (ACoS 20-28%) | 🟢 健康 | 保持,小幅扩量 |
| **2.5-3.5x** (ACoS 28-40%) | 🟡 中性 | 优化listing/bid,测试 |
| **1.5-2.5x** (ACoS 40-67%) | 🟠 偏亏 | 大幅优化或暂停 |
| **< 1.5x** (ACoS >67%) | 🔴 亏损 | 立即暂停,复盘 |

### Step B4: Bid调整规则

**Product Ads的Bid调整 (Manual CPC)**:

| 当前ROAS | 调整方向 | 调整幅度 |
|---------|---------|---------|
| > 5.0x | ↑ 加价 | +20% |
| 3.5-5.0x | ↑ 略加 | +10% |
| 2.5-3.5x | → 保持 | 0% |
| 1.5-2.5x | ↓ 降价 | -15% |
| < 1.5x | ↓↓ 大降 | -30% (评估是否暂停) |
| 0 | ⏸ 暂停 | — |

**Automated ROAS target调整**:
- ROAS > target: 调低target 0.3-0.5x (抢更多量)
- ROAS ≈ target: 保持
- ROAS < target × 0.8: 调高target 0.5-1.0x
- ROAS < break-even: 立即关掉target或暂停campaign

### Step B5: 搜索词/Listing分析(若为Brand Ads)

针对Brand Ads的搜索词报告(类似Amazon的Search Term Report):

**找出3类词**:
1. **高转化词** (2+ conversions): 移到专用Ad Group
2. **高曝光低点击** (CTR < 0.5%): 检查是否相关,否词
3. **高点击0转化** (clicks > 20, orders = 0): 立即否词

### Step B6: 周计划生成

```markdown
## Week 1 行动 (立即执行)
- [ ] [具体动作] 预期影响 [X]

## Week 2 行动
- [ ] [具体动作] 预期影响 [X]

## Week 3 行动
- [ ] [具体动作] 预期影响 [X]

## Week 4 复盘
- [ ] 重新跑Step B1-B5
- [ ] 决定是否大促准备
```

### Output: Mode B 优化报告

```markdown
# ✅ Mercado Ads Optimization — Ready to Implement

## 当前状态
- 总月预算: $X
- 总月花费: $X
- 总ROAS: [X]x
- 总ACoS: [X]%
- 订单数: $X
- 状态: 🟢/🟡/🟠/🔴

## Priority 1: 立即行动(24h内)
- Campaign [X]: [action] — 预计影响 [X]
- Campaign [X]: [action] — 预计影响 [X]

## Priority 2: 本周调整
- [action with target ROAS change]

## Priority 3: 4周复盘目标
- ROAS [X]x → [Y]x
- Spend efficiency [X] → [Y]
- 利润改善 +[X] MXN/月

## Bid调整明细
| Campaign | SKU | 当前ROAS | 调整 | 新Bid/Target |
|----------|-----|---------|------|------------|
| ... | ... | ... | ↑20% | ... |

## Negative keywords(Brand Ads)
- [词] | 原因: 高曝光低转化
- [词] | 原因: 不相关

## 大促准备清单(若适用)
- [ ] 旺季前4周: 预算 × 1.5
- [ ] 旺季前2周: 入Full仓 (享受流量倾斜)
- [ ] 旺季当周: 调低target ROAS × 0.7 (抢量)
- [ ] 旺季后: 立即回到normal ROAS
```

## LATAM-Specific Best Practices

### 🇲🇽 Mexico Specific
- **货币**: MXN
- **CPC区间**: 大部分3C类目 0.5-5 MXN
- **ACoS健康值**: 20-35%
- **旺季**: Hot Sale 5月底, El Buen Fin 11月(全年最大)
- **官方佣金**: Classic 12.5-22.5%, Premium 16.5%
- **特殊**: 拉美最大广告市场,Mercado Ads功能最全

### 🇧🇷 Brazil Specific
- **货币**: BRL
- **CPC区间**: 大部分3C类目 0.2-3 BRL
- **ACoS健康值**: 15-30%
- **旺季**: Dia das Mães 5月, Black Friday 11月
- **官方佣金**: Classic 12.5%, Premium 16.5%
- **特殊**: 美客多最大GMV市场,但ROI要求高(税改后)
- **💡 2025新**: 巴西新增$19 BRL免运费门槛,带动了广告流量(同比+34% GMV)

### 🇨🇱 Chile / 🇨🇴 Colombia
- **CPC**: 通常 < 1 CLP/COP 单位
- **旺季**: Cyber Day 6月, Black Friday 11月
- **总预算建议**: < 100 USD/月 起步

### ⚡ 拉美广告主独有心法

1. **品牌词CPC极低** — 拉美品牌搜索弱,即使新品牌也能低价抢曝光
2. **分期免息对ROAS影响** — 启用12期免息后,转化率提升30-50%,但客单价也涨,ROAS需重新算
3. **Full仓加权** — Full商品在Product Ads中**自动加权**,建议旺季前入Full
4. **季节波动巨大** — El Buen Fin当周ROAS可以是淡季的1.5x,CPC也会涨,需提前规划
5. **葡语西语严格区分** — 巴西Product Ads标题可以是葡语,但西语keywords在巴西无效
6. **同步Instagram/Facebook引流** — Display Ads可投站外,与社媒联动

### 📅 大促广告预算时间表

| 节点 | 国家 | T-4周 | T-2周 | T-1周 | 当周 | 后1周 |
|------|------|------|------|------|------|------|
| Hot Sale | MX | ×1.3 | ×1.5 | ×2.0 | ×2.5-3.0 | ×1.5 |
| Cyber Day | CL | ×1.3 | ×1.5 | ×1.8 | ×2.5 | ×1.3 |
| El Buen Fin | MX | ×1.5 | ×2.0 | ×2.5 | ×3.0-4.0 | ×1.8 |
| Dia das Mães | BR | ×1.2 | ×1.4 | ×1.5 | ×1.8 | ×1.0 |
| Black Friday | 全站 | ×1.5 | ×2.0 | ×2.5 | ×3.0-3.5 | ×1.8 |
| 圣诞/新年 | 全站 | ×1.2 | ×1.3 | ×1.5 | ×1.8 | ×1.3 |

## Integration with Other 美客多 Skills

### 完整工作流:

```
1. mercado-product-research: 选品类 + 利润率
   ↓
2. mercado-keyword-research: 西/葡语关键词清单
   ↓
3. mercado-listing-optimization: 完整listing (西/葡)
   ↓
4. mercado-ppc-campaign (本skill): 建广告,启动销售 ⬅️
   ↓
5. 监控 → 回到本skill Mode B 优化
```

### Skill Chain 提示:

- 启动广告前, **必须先跑 mercado-listing-optimization** — listing质量差,广告就是烧钱
- 用 mercado-keyword-research 输出作为Brand Ads的关键词
- 利润率数字从 mercado-product-research 的"利润潜力"部分取

## Output: 完整 Sample (创客机械臂 Mexico)

以我们之前分析过的"创客机械臂"(brazo robótico)为例,展示完整输出:

### 财务模型
| 项目 | MXN | % |
|------|-----|---|
| 售价 (Premium listing) | 1899 | 100% |
| 产品成本(1688升级版) | 550 | 29% |
| 平台佣金 Premium 16.5% | 313 | 16.5% |
| Mercado Pago 3.99% | 76 | 4% |
| Full海外仓物流 | 80 | 4.2% |
| 杂费 | 30 | 1.6% |
| **净利率** | **850** | **44.8%** |

### 关键ROAS
- Break-even ROAS = 1/0.448 = **2.23x**
- Target ROAS (新卖家) = 2.23 × 1.7 = **3.8x** (旧ACoS = 26%)
- Max CPC = 1899 × 0.448 × 0.02 × 0.03 = **5.1 MXN**

### 预算分配(月预算 1500 MXN = ~$80 USD)

| Campaign | Type | Daily | Monthly | ROAS目标 |
|----------|------|-------|---------|---------|
| Brazo Robótico MX - Product Ads 主力 | PML | 30 | 900 | 3.5x |
| Brazo Robótico MX - Brand Ads 防御 | Brand | 12 | 360 | 4.0x |
| Brazo Robótico MX - Display 再营销 | Display | 8 | 240 | 5.0x |
| **总计** | | **50** | **1500** | **3.7x blended** |

### 预期(以3.5x target ROAS算)
- 月广告投入: 1500 MXN
- 月广告销售额: 1500 × 3.5 = **5250 MXN**
- 月订单数(单价1899): 5250/1899 = **2.8 单/天** ≈ 84 单/月
- 月毛利贡献(净利 - 广告): 5250 × 0.448 - 1500 = 2352 - 1500 = **852 MXN/月净利**

**🔴 注意**: 这是起点数字,实际需要2-3月数据积累优化。**第1个月ACoS可能到50-80%** (学习期正常),第3个月收敛到target。

## Limitations

This skill uses publicly available data and user-provided campaign data. It cannot:
- 直接访问 Mercado Ads 后台(需用户自己设置)
- 拉取实时竞价数据(需Mercado Ads官方工具)
- 自动化bid调整(无API,需手动或用蓝鲸BI等)
- 预测未来CPC变化(无官方预测工具)

**For deeper analytics**:
- 蓝鲸BI (`lingdongsz.com`): 盯盘 + 关键词竞争分析
- UpSeller ERP (`upseller.com`): 多店批量广告管理
- Mercado Ads Academy (`academy.mercadoads.com`): 官方课程

---

*基于美客多官方文档 + 2025-2026 ACoS→ROAS算法迁移 + 拉美本地化经验设计。配合 mercado-product-research / mercado-keyword-research / mercado-listing-optimization 三个skill形成完整工作流。*
