---
name: mercado-product-research
description: "Comprehensive product research and opportunity analysis for Mercado Libre (美客多) cross-border sellers. Analyzes demand, competition, profit potential, market entry barriers across Mexico (MX), Brazil (BR), Chile (CL), Colombia (CO). Covers product sourcing, pricing strategy, fee structure (commission + 2026 Brazil CBS/IBS tax), logistics (Mercado Envíos self-shipping vs Full), Mercado Pago installments, and go-to-market planning. Use when the user asks about researching a product to sell on Mercado Libre, validating 美客多 product ideas, LATAM opportunity analysis, 美客多选品, 美客多选品分析, mercado libre product research, product viability, should I sell on 美客多, or any general MercadoLibre product research questions."
metadata: {"emoji":"🌎","category":"mercadolibre"}
---

# Mercado Libre Product Research 🌎

Complete product research framework for 美客多 (Mercado Libre) cross-border sellers. Validate ideas, analyze opportunities, assess competition across LATAM.

## When to Use

Activate this skill whenever the user mentions:
- 美客多 / Mercado Libre / MercadoLibre / MELI / 拉美电商 / LATAM e-commerce
- 美客多选品, mercado libre product research, 美客多选品分析
- Selling on Mercado Libre Mexico / Brazil / Chile / Colombia
- Cross-border to Latin America / 跨境拉美

## Capabilities

- **Product opportunity scoring**: 1-10 rating across 8 factors tailored for LATAM market
- **Demand analysis**: Mercado Libre search volume, Google Trends LATAM, seasonal patterns (Hot Sale, Cyber Day)
- **Competition assessment**: Local sellers + Chinese cross-border competition, brand dominance
- **Profit potential calculation**: Commission + low-price unit fee + 2026 Brazil CBS/IBS + logistics + Mercado Pago 3.99%
- **Market entry analysis**: Site-by-site entry barriers, Global Selling vs local entity, investment required
- **Sourcing guidance**: 1688/Alibaba supplier matching, MOQ, shipping consolidation
- **Risk evaluation**: Regulatory (Anvisa), tax (Brazil 2026 reform), currency (BRL/MXN/CLP/COP) volatility
- **Multi-marketplace support**: MX, BR, CL, CO (the 4 official 跨境站点)

## Target Sites & Currencies

| Site | Currency | Language | Cross-Border Model | Entry Difficulty |
|------|----------|----------|-------------------|------------------|
| Mexico (MLM) | MXN | 西班牙语 | Global Selling + Full China Logistics | ★★☆☆☆ (推荐首选) |
| Brazil (MLB) | BRL | 葡萄牙语 | Global Selling (邀请制) | ★★★★☆ (2026税改复杂) |
| Chile (MLC) | CLP | 西班牙语 | Global Selling | ★★☆☆☆ (体量较小) |
| Colombia (MCO) | COP | 西班牙语 | Global Selling | ★★★☆☆ (物流慢) |

**Recommendation rule**: Default-prioritize Mexico for first-time 美客多 sellers; add Brazil only after Mexico GMV is stable.

## Usage Examples

```
帮我分析"无线耳机"在美客多墨西哥站的机会
```

```
Research "smart watch" on Mercado Libre Mexico and Brazil - full market analysis
```

```
我在1688找到一款$5的产品,美客多上卖$25,值得做吗?
```

```
比较美客多上的"手机壳"和"手机支架",哪个更适合新手?
```

```
分析2026年巴西税改(IBS/CBS)对电子配件类目的影响
```

```
Hot Sale 5月要到了,美客多墨西哥站选什么品能爆?
```

## Workflow

### Step 1: Product & Market Intelligence

Use `web_search` with bilingual queries:

1. **Search volume signals**: `"[product]" site:mercadolibre.com.mx` 或 `"[product]" site:mercadolivre.com.br`
2. **Autocomplete check**: 模拟用户输入`[product]`+`[a-z]`,观察下拉词
3. **Market size**: `"[product]" mercado libre tendencias 2026`
4. **Seasonality**: `"Hot Sale 2026" [product] Mexico`, `"Cyber Day" [product] Chile`
5. **Local terminology**: 拉美用户叫法与英文/中文不同(如墨西哥把"蓝牙耳机"叫"audífonos bluetooth"),先确认本地关键词

**What to extract:**
- Approximate search volume (ML公共搜索页可见)
- Listing density (search results count)
- Category positioning (categoría principal)
- Seasonal peaks (Hot Sale 5月, Cyber Day 6月, Black Friday 11月, Dia das Mães 5月 BR)
- Local demand signals (Mercado Pago分期付款的需求)

### Step 2: Competition Deep Dive

Analyze the competitive landscape:

1. **Competition density**: `"[product]" site:mercadolibre.com` - 总listing数
2. **Top sellers**: `"más vendido [product]" mercado libre` - 看热销榜
3. **Price range mapping**: 测试`[product]`在不同价位(墨西哥比索/巴西雷亚尔)的分布
4. **Brand dominance**: 识别是国际大牌(Xiaomi/Samsung/Anker)还是本土卖家还是中国跨境卖家
5. **Mercado Envíos Full覆盖率**: Full商品(<3-5天到货)占比 — 这是核心竞争力

**Competition Metrics:**
- **Total listings**: 该关键词总listing数
- **Mercado Envíos Full占比**: Full商品比例(高=竞争激烈)
- **Top sellers集中度**: 前3名销量占比
- **Review分布**: 100+评价/1000+评价/5000+评价的商品数
- **价格段**: 经济型/中端/高端(MXN/BRL区间)
- **评分**: 平均星级、常见差评关键词

**Competition Scoring (1-10):**
- 9-10: 极度碎片化,无主导品牌,新卖家容易切入
- 7-8: 有几个国际大牌但有差异化空间
- 5-6: 国际大牌+本土卖家混战
- 3-4: 2-3个大牌或本土强势卖家垄断
- 1-2: Amazon Basics级别或本土巨头垄断

### Step 3: Demand Validation

1. **Google Trends LATAM**: 用`https://trends.google.com/trends/explore?q=[product]&geo=MX`(或BR/CL/CO)
2. **Mercado Libre autocomplete**: 在目标站点搜索框逐字母输入,看长尾建议
3. **Social validation**: `"[product]" reddit LATAM`, `"[product]" TikTok Mexico reviews`
4. **Cross-platform buzz**: `"[product]" Amazon Mexico` 看是否多平台同热

**LATAM-Specific Demand Signals:**
- **分期付款需求**: 标价越高的商品,Mercado Pago cuotas的需求越强 — 影响转化率
- **免运费门槛**: 拉美买家极看重"envío gratis"(通常>299 MXN / >79 BRL触发)
- **品牌信任**: 拉美买家对中国新品牌信任度低,有品牌或本地仓的溢价空间
- **季节性**: 比欧美更强 — Hot Sale / Cyber Day / 黑五 / 圣诞 / 春节

**Demand Scoring (1-10):**
- 9-10: 强劲上升趋势,搜索量高,有持续增长
- 7-8: 稳定高需求,常年热销
- 5-6: 中等需求,有明显季节性
- 3-4: 需求下滑或仅限旺季
- 1-2: 需求低迷或极小众

### Step 4: Profitability Analysis (LATAM-Adapted)

Calculate real profit — 美客多费用结构比Amazon更复杂:

**Formula:**
```
售价 (MXN/BRL)
- 平台佣金 (Classic 12.5%-22.5% | Premium 16.5%)
- 低价位附加费 (BR: ≤BRL 79加BRL 9.6/件 | CL: ≤CLP 15,650加CLP 1,650/件)
- 2026巴西税改CBS+IBS (2026年4月起0.9%+0.1%试点,2027年1月起~27%综合)
- Mercado Pago手续费 (国际卡3.99%,本地卡较低)
- 头程+尾程运费 (自发货约25天,Full<5天)
- 产品成本 (1688/AliExpress)
= 净利润
```

**Pricing Research:**
- `"[product]" mercado libre precio` 拉取同款价格段
- 用第三方工具(蓝鲸BI、UpSeller)看竞品真实成交价(不要只看标价)

**Cost Estimation:**
- `"[product]" 1688 批发价` 或 Alibaba报价
- 头程: 按重量/体积,美客多Full中心仓有官方报价

**Margin Benchmarks (按站点差异):**
- **Mexico**: 健康净利率 18-25% (人民币结算后)
- **Brazil**: 健康净利率 22-30% (雷亚尔结算+IBSTAX扣除后更复杂)
- **Chile**: 健康净利率 20-28%
- **Colombia**: 健康净利率 20-26%

### Step 5: Logistics & Fulfillment Decision

**Decision tree:**

```
Q1: 单SKU月销量预期是否 >200件?
  ├─ Yes → Full (海外仓)更优,享受3-5天送达+免费物流标签
  └─ No → 自发货(Mercado Envíos Direct)起步,25工作日交付
```

**Logistics Models Comparison:**

| 模型 | 时效 | 适用场景 | 费用 |
|------|------|---------|------|
| Mercado Envíos Direct (自发货) | 25工作日 | 新品测试、小批量、长尾品 | 平台指定物流商,按重量计费 |
| Mercado Envíos Flex | 1-3天本地 | 仅限本地卖家 | — |
| Full (海外仓) | 3-5天 | 热销品、稳定供应链 | 仓储费+拣货费,Full仓免运费补贴 |
| Full China Logistics | 头程+本地+尾程 | 中国工厂直发 | 打包定价,跨境全链路 |

**2025 Mexico新重量段**: 0-2kg / 2-5kg / >5kg,每段运费上浮约12%

### Step 6: Market Entry Assessment

**Per-site entry analysis:**

**Mexico (推荐首选) 🌟**
- ✅ 中国卖家友好,Global Selling开放
- ✅ 西班牙语内容门槛低
- ✅ 物流成熟(Full China Logistics可用)
- ⚠️ 2025年4月部分类目佣金上调至22.5%
- 💡 推荐类目: 3C配件、家居小件、美妆个护、汽摩配件

**Brazil (高潜力高风险) ⚠️**
- ✅ 体量大(美客多最大市场),BRL支付习惯好
- ⚠️ 2026/2027税改复杂(CBS+IBS)
- ⚠️ 葡萄牙语门槛
- ⚠️ 邀请制Global Selling
- 💡 推荐类目: 时尚、家居、3C配件
- 🔴 风险: 未适应税改的卖家可能在2027被罚

**Chile (适合做品牌测试) ⭐**
- ✅ 体量小但成熟
- ✅ 物流稳定,3-5天
- ✅ 西班牙语,与墨西哥可复用listing
- 💡 推荐类目: 科技产品、家居

**Colombia (成长中) 🌱**
- ✅ 增速快,竞争较低
- ⚠️ 物流时效慢
- ⚠️ COP汇率波动
- 💡 推荐类目: 时尚、美妆

### Step 7: Risk Evaluation

**Market Risks:**
- 平台政策变动(墨西哥2025年4月调整就是先例)
- 巴西2026税改落地风险
- 本土卖家竞争加剧(Shopee/Temu在巴西/墨西哥高速增长)
- 拉美货币贬值(BRL、ARS、CLP都有波动历史)

**Operational Risks:**
- 25天自发货时效→差评风险
- Full仓库存滞销→仓储费累积
- 跨境退货成本高(平均>$15/件)
- 物流旺季(Hot Sale/黑五)Full仓爆仓

**Regulatory Risks:**
- 🇨🇳 中国出口: 跨境电商合规出口
- 🇧🇷 巴西: CBS(0.9%→8.8%)+IBS(0.1%→17.7%)两阶段税改
- 🇲🇽 墨西哥: 部分品类需NOM认证、IFETEL(电子产品)
- 🇧🇷🇲🇽 通用: 禁售药品/烟草/枪支/侵权品
- 🇧🇷 巴西: ANVISA食品/化妆品/医疗器械注册

**Financial Risks:**
- BRL/MXN汇率波动(对人民币结算的卖家影响)
- 平台回款周期: 通常15-30天
- Mercado Pago分期利息(平台代收,但影响客单价)

### Step 8: Score & Recommendation

**8-Factor Scoring (1-10 each):**

1. **需求强度 (Demand)**: 搜索量+增长率
2. **竞争密度 (Competition)**: 反向计分(分数越高=竞争越低)
3. **利润空间 (Profit)**: 净利率
4. **准入门槛 (Entry)**: 认证/语言/物流难度
5. **供应链 (Supply)**: 1688货源稳定性
6. **季节性 (Seasonality)**: 反向计分(分数越高=越常年)
7. **合规风险 (Compliance)**: 反向计分(分数越高=风险越低)
8. **可扩展性 (Scalability)**: 是否能多站点复用

**Overall Score**: 8项平均分

## Output Template

生成完整选品报告时使用以下结构(中文/英文/西语/葡语可混合):

```markdown
# 美客多选品报告: [产品名]

## 🎯 核心结论
- 推荐度: ⭐⭐⭐⭐⭐ (X.X/10)
- 推荐站点: [MX/BR/CL/CO,可多选]
- 预估净利率: XX%
- 建议模式: [自发货 / Full / Full China Logistics]
- 主要风险: [1-2条]

## 🌎 市场分析
- 需求强度: 高/中/低
- 市场趋势: 上升/稳定/下滑
- 季节性: 全年/旺季[月份]/强季节
- 类目归属: [一级] > [二级]
- 市场规模: [大/中/小众]

## ⚔️ 竞争评估
- 竞争强度: 低/中/高
- 市场领导者: [前2-3品牌+份额估算]
- 价格段: 经济型 MXN XX-YY / 中端 XX-YY / 高端 XX-YY
- Full覆盖: XX% (高=竞争激烈)
- 市场空白: [未被满足的细分或价格点]

## 💰 利润潜力
```
目标售价:        R$ XX,XX / MXN XXX
产品成本:        R$ XX,XX (XX%)
平台佣金:        R$ XX,XX (XX%)
低价位附加费:    R$ XX,XX (X%) [仅BR/CL]
2026税改预留:    R$ XX,XX (X%) [仅BR]
Mercado Pago:   R$ XX,XX (X%)
头程+尾程:       R$ XX,XX (X%)
预估净利润:      R$ XX,XX (XX% 净利率)
```
- 利润率评级: 优秀/良好/紧张/差
- 量级潜力: 高/中/低

## 🚀 市场进入分析
- 启动资金: R$ X,XXX - X,XXX (库存+setup)
- 最小起订量: X 件 (1688常规)
- 认证要求: [无 / 标准 / 复杂]
- 上架周期: X-X 周
- 关键成功因素: [最重要的3点]

## ⚠️ 风险评估
- 市场风险: 趋势可持续性、季节性、竞争
- 运营风险: 供应链、质量控制、物流
- 合规风险: 平台政策、关税、本地法规
- 财务风险: 库存、现金流、汇率

## 🛒 推荐策略

### 如果总分7-10:
- ✅ **推荐入手**
- 进入策略: [高端定位 / 性价比路线 / 细分聚焦]
- 差异化: [核心差异化点]
- 上架时间表: [最优时机+里程碑]
- 成功指标: [跟踪KPI]

### 如果总分4-6:
- ⚠️ **有条件推荐**
- 需改进: [需调整的点]
- 替代方案: [不同定位或站点]
- 风险缓解: [如何降低风险]

### 如果总分1-3:
- ❌ **不推荐**
- 主要问题: [避免原因]
- 替代产品: [相关更好的机会]

## 🛠️ 推荐工具(辅助数据)
- 蓝鲸BI: 全维度美客多数据透视,盯盘、关键词、广告分析
- UpSeller ERP: 免费版支持多店管理、批量改价、利润计算
- Trendyol/MercadoLibre官方: Global Selling 招商经理对接
```

## Quick Comparison Format

| 产品 | 需求 | 竞争(反) | 利润 | 准入 | 供应 | 季节(反) | 合规(反) | 扩展 | 总分 |
|------|------|---------|------|------|------|---------|---------|------|------|
| 产品A | 8/10 | 6/10 | 7/10 | 8/10 | 7/10 | 8/10 | 7/10 | 8/10 | **7.4** ⭐ |
| 产品B | 6/10 | 9/10 | 8/10 | 7/10 | 8/10 | 7/10 | 8/10 | 7/10 | **7.5** ⭐ |
| 产品C | 9/10 | 4/10 | 6/10 | 5/10 | 6/10 | 9/10 | 6/10 | 9/10 | **6.8** ⚠️ |

**Recommendation**: 产品B在机会与可行性之间取得最佳平衡。

## LATAM Market-Specific Heuristics

### 🎁 Mercado Pago分期付款(关键转化器)
- 拉美消费者对cuotas(分期)依赖极强
- 标价>=$50的商品启用12期免息可显著提升转化
- 公式: 12期免息 = 客单价提升30%-50%(常规)
- 注意: 利息由商家或平台承担,需计入成本

### 📦 免运费(envío gratis)是核心转化点
- 触发门槛: MX > $299 MXN / BR > R$ 79 / CL > $15.650 CLP
- Full商品自动包邮,是巨大优势
- 自发货商品达到门槛后需补贴运费 → 影响定价策略

### 🏷️ Premium Listing vs Classic
- **Premium**: 16.5%佣金,但曝光高、可参加大促、有分期选项
- **Classic**: 12.5%佣金,适合利润率薄的标品
- **新手建议**: 先Classic起步验证,稳定后转Premium抢曝光

### 📅 大促日历必须匹配

| 大促 | 国家 | 日期 | 备战建议 |
|------|------|------|---------|
| Hot Sale | MX | 5月底-6月初 | 提前1个月入Full,预热coupon |
| Cyber Day | CL | 6月初 | Premium listing+3日达 |
| Dia das Mães | BR | 5月第2个周日 | 美妆/家居流量高峰 |
| Black Friday | 全站 | 11月底 | 9月前Full仓备货 |
| 11.11 Singles Day | MX/CO | 11月11日 | 平台coupon补贴 |
| 圣诞/新年 | 全站 | 12月 | 礼品类核心节点 |
| 春节 | 全站华人 | 1-2月 | 国货品牌溢价 |

### 🌐 本地化要点

**Listing语言要求:**
- 墨西哥/智利/哥伦比亚: 西班牙语
- 巴西: 葡萄牙语(不要用西班牙语!)
- 多站点共用listing需翻译,但图片可共用

**文化禁忌:**
- 巴西: 颜色偏好(避免紫色+黄色组合=国旗),尺寸用BR码
- 墨西哥: 西班牙语敬语(usted vs tú),避免黑色为主的页面(丧葬联想)
- 拉美全境: 信用卡分期习惯深植,高价品必须支持cuotas

## Best Practices

✅ **多站点对比**: 同一产品在4个站点分别评估,选最优1-2个切入

✅ **季节性匹配**: 优先做常年需求品,避免纯季节品(如圣诞装饰)

✅ **物流先行**: 选品时同步评估物流成本,小件轻量优先(<2kg最优)

✅ **认证提前**: 选品阶段就查清目标品类的认证要求(NOM/IFETEL/ANVISA),避免上架后被下架

✅ **合规优先**: 不碰药品/保健品/医疗器械/食品,这些品类ANVISA门槛极高

✅ **品牌化**: 拉美对中国白牌信任度低,建议有品牌包装+商标注册(墨西哥IMPI/巴西INPI)

✅ **数据验证**: 至少3个数据源交叉验证需求(ML autocomplete + Google Trends + 社媒)

---

*基于公开市场数据设计。对于实时销量预估、竞品监控、供应商验证,可对接专业BI工具如蓝鲸BI、UpSeller ERP以获得更精确的选品决策支持。*
