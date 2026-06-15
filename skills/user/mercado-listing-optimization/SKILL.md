---
name: mercado-listing-optimization
description: "Mercado Libre (美客多) listing builder and optimizer for cross-border sellers. Two modes: (A) Create — build keyword-optimized Spanish/Portuguese listings from scratch using Mercado Libre autocomplete data + ficha técnica + AI copywriting, (B) Optimize — audit existing 美客多 listings, find keyword gaps, score across 8 LATAM-adapted dimensions, and rewrite with missing keywords. Native support for Mexico (MLM), Brazil (MLB), Chile (MLC), Colombia (MCO). Integrates with mercado-keyword-research. Use when: (1) creating a new 美客多 listing from keywords, (2) auditing an existing 美客多 listing for SEO/positioning, (3) checking keyword coverage in título/ficha técnica/descripción, (4) generating Spanish/Portuguese listing copy with target keywords, (5) comparing 美客多 listings against competitors, (6) preparing 美客多 listings for Hot Sale / El Buen Fin / Black Friday, (7) optimizing for Mercado Libre Catalog competition."
metadata: {"emoji":"📝","category":"mercadolibre"}
---

# Mercado Libre Listing Optimization 📝

Build keyword-optimized Spanish/Portuguese listings for 美客多, or audit and optimize existing ones. No API key — works out of the box. Native LATAM localization.

## When to Use

Activate this skill whenever the user mentions:
- 美客多 listing优化, 美客多产品上架, 美客多标题优化
- Mercado Libre listing optimization, 美客多 Listing
- Título / ficha técnica / descripción for 美客多
- Improve position on MercadoLibre, 美客多排名
- Audit my 美客多 listing, 美客多产品页
- Catalog listing optimization, ficha técnica fields
- Hot Sale / Buen Fin / Black Friday listing prep
- Generating Spanish/Portuguese copy for 美客多

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Create** | Building a new 美客多 listing | Keywords (from mercado-keyword-research) + competitor URLs + product info + tone | Full listing copy (西/葡) + keyword coverage score |
| **B — Optimize** | Improving an existing 美客多 listing | Your URL/MLMID (+ optional keywords or competitor URLs) | Optimized listing copy + audit report + gap analysis |

## Mode A — Three Ways to Start

| Input Source | How it Works |
|-------------|-------------|
| **Keywords** | User provides keyword list (preferably from mercado-keyword-research) → skill prioritizes and generates listing |
| **Competitor URLs** | User provides 1-3 MercadoLibre competitor URLs → skill fetches their listings, extracts their keywords, then generates a listing that covers all their keywords and more |
| **Both** | User provides keywords + competitor URLs → skill merges both sources for maximum coverage |

## Capabilities

- **Keyword-driven listing generation**: Import keywords (from mercado-keyword-research, manual list, or extracted from competitor URLs), rank by priority, generate copy that maximizes 美客多 keyword coverage
- **Competitor keyword extraction**: Fetch competitor MercadoLibre listings and automatically extract their title/ficha técnica keywords as your baseline
- **8-dimension 美客多 audit & scoring**: Título, Ficha Técnica, Descripción, Fotos, Video, Precio, Reputación, SEO Coverage
- **Keyword coverage tracking**: Visual map showing which keywords appear in título / ficha técnica / descripción / missing
- **Tone selection**: Professional, Friendly, Urgent, Technical — affects AI copywriting style
- **Competitive benchmarking**: Compare your listing against competitors
- **Multi-marketplace**: Mexico (MXN), Brazil (BRL), Chile (CLP), Colombia (COP)
- **Mercado Pago installments optimization**: Auto-suggest 6/12-cuotas for products $50+ USD
- **Catalog vs Classic detection**: Identify if product should use Catalog (compete for first-purchase) vs Classic listing

## 美客多 Listing Structure Reference

### 核心字段(必须填)

| 字段 | 字符限制 | 用途 | 优化重点 |
|------|---------|------|---------|
| **Título** | 60字符(显示)/ 完整可更长 | ⭐ **SEO 头号因素** | 品牌+品类+核心特性+型号+尺寸+颜色 |
| **Ficha Técnica** | 字段数视类目(常见15-40个) | ⭐ 分类匹配 + 站内搜索 | 填全所有属性,ean/gtin必填 |
| **Descripción** | 5000字符 | 转化 | 卖点+规格+FAQ+使用场景 |
| **Fotos** | 1-12张 | 转化 | 第1张:白底主图;后续:多角度+场景+尺寸对照 |
| **Video** | 可选,1个 | 转化+SEO | 30-60秒展示功能 |
| **Precio** | — | 流量+转化 | 参考Top竞品+Full免运费补足 |
| **Stock** | — | 算法权重 | 保持>10,Full>50 |
| **Envío** | 选择Mercado Envíos模式 | 流量+转化 | **Full > 自发货25天**(流量倾斜) |
| **Condición** | Nuevo/Usado/Reacondicionado | 信任 | Nuevo + 库存多=加权 |

### Listing类型选择

| 类型 | 佣金 | 优势 | 适用场景 |
|------|------|------|---------|
| **Gratuita** (免费) | 0固定 | 基础曝光 | 利润薄、不追求排名 |
| **Clásica** | 12.5%-18% (类目相关) | 无固定费用($299+ MXN时) | 利润中等、起步阶段 |
| **Premium** | 16.5% | ✅ 曝光高 ✅ 可参加大促 ✅ 12期分期 ✅ MercadoLíder加权 | 利润足够、追求爆款 |
| **Catalog (竞争型)** | 跟随类目 | 争夺"首购选项"位 | 与现有卖家同款竞争时 |

**推荐路径**: 新品从 Clásica 起步 → 验证后转 Premium → 旺季入 Full + Mercado Pago 12期免息

## Usage Examples

### Mode A — Create from Keywords

```
为"蓝牙耳机"创建美客多墨西哥站 listing
关键词: audífonos bluetooth, audífonos inalambricos, audífonos bluetooth baratos
产品: 蓝牙5.3, 40小时续航, IPX5防水, 黑色
语调: Friendly
```

```
Create a Mercado Libre Mexico listing for a 6-DOF robotic arm. 
Keywords from research: brazo robótico, brazo robot arduino, brazo robótico 6 ejes
Material: 铝合金 + 6 servos MG996R
Tone: Technical
```

### Mode A — Create from Competitor URLs

```
分析这个美客多竞品并做一个更好的: https://articulo.mercadolibre.com.mx/MLM-123456
我的产品: 相同蓝牙耳机,但续航更长(50h vs 40h),加了主动降噪
```

### Mode A — Keywords + Competitors

```
Use mercado-keyword-research output for "soporte para celular" on Mercado Libre Mexico,
also analyze these competitors: [URL1, URL2, URL3]. 
Combine all keywords and create a listing. Product: aluminum phone stand, 360° rotation, 3 colors.
```

### Mode B — Optimize Existing

```
Audit my MercadoLibre listing: https://articulo.mercadolibre.com.mx/MLM-XXXXX
```

```
Optimize my 美客多 listing (MLMID: MLM123456) using these keywords: soporte celular, soporte teléfono, holder celular
```

### Mode B — Competitive

```
Optimize my 美客多 listing by analyzing these 3 top competitors: [URL1, URL2, URL3]
Find what keywords they have that I'm missing.
```

---

## Mode A Workflow — Create Listing from Keywords

### Step A1: 收集关键词(可多个来源)

1. **From `mercado-keyword-research` skill** (推荐): 跑关键词研究后,直接喂结果
2. **From competitor URLs**: 抓1-3个Top竞品listing,提取其título + ficha técnica关键词
3. **Manual list**: 用户直接提供
4. **Auto-discovery**: 用户只提供产品名,skill自动用tavily拉取美客多autocomplete

### Step A2: 关键词优先级排序

按 **MercadoLibre 2026算法权重** 排序:

| 优先级 | 位置 | 算法权重 |
|-------|------|---------|
| 🔴 **Primary** | **Título**(必须包含前3词) | 最高(标题是SEO头号因素) |
| 🟡 **Secondary** | **Ficha Técnica** 属性 | 高(站内搜索+Catalog匹配) |
| 🟢 **Tertiary** | **Descripción** | 中(转化+长尾覆盖) |
| ⚪ **Backend** | 不存在(美客多不暴露backend keywords给第三方) | — |

**重要**: 不同于Amazon,**美客多没有"backend search terms"字段**。所有关键词必须自然地融入título + ficha técnica + descripción。

### Step A3: 标题(Título)生成 ⭐ 关键

**美客多标题公式** (60字符以内为佳,完整可至120):
```
[品牌] + [品类词] + [核心特性1] + [核心特性2] + [型号/SKU] + [尺寸/颜色/容量]
```

**Example**:
- ❌ `Audífonos Bluetooth` (裸奔,无信息量)
- ✅ `Audífonos Bluetooth Inalámbricos, 5.3, 40h Batería, IPX5, Negro` (信息密度高,SEO友好)

**5 Tips from MercadoLibre官方**:
1. **品类词在最前** — 算法优先匹配品类
2. **使用"compatible con"或"para"** — 兼容设备词很重要(如"para iPhone Samsung")
3. **写明品牌or通用** — 明确标注"samsung"/"genérico"
4. **不要写"nuevo"或"envío gratis"** — 系统自动添加,占字符
5. **首次售卖后不可改** — ⚠️ 警告!上架前必须确认

### Step A4: Ficha Técnica填充

**类目相关属性** (skill应根据用户品类给模板):
- Marca (品牌) — **必填**
- Modelo (型号) — **必填**
- GTIN/EAN (国际条码) — **强烈建议**(Catalog匹配关键)
- Color, Tamaño, Material, Peso
- 通用属性: País de origen, Garantía, Conectividad

**Example for Bluetooth Earbuds (MLM类目)**:
```
Marca: TuMarca
Modelo: TWS-2026
Color: Negro
Conectividad: Bluetooth 5.3
Autonomía: 40 horas (con estuche de carga)
Resistencia al agua: IPX5
Incluye: Estuche de carga, cable USB-C, 3 pares de almohadillas
Garantía: 90 días
País de origen: China
```

**🎯 关键**: Ficha Técnica 越完整,Catalog 匹配概率越高,首购选项竞争越有力。

### Step A5: Descripción(描述)生成

**结构模板** (西语):
```
1. 钩子(2-3行) — 解决用户核心痛点
2. 核心卖点(5-7个 bullet) — 关键词密度高
3. 技术规格表 — 复读ficha técnica(为长尾词)
4. 使用场景(2-3个) — 覆盖应用场景关键词
5. 包装清单
6. 售后/FAQ
7. 品牌信任元素
```

### Step A6: Foto + Video 规划

**图片规范** (美客多官方):
- 格式: JPG/PNG
- 尺寸: 至少 500x500px,推荐 1200x1200px
- 数量: 1-12张(推荐8-10张)
- 第1张(封面): **白底 + 产品占80%+**
- 后续: 多角度+场景图+尺寸参照+细节特写
- ⚠️ 禁止: 文字水印、价格、其他品牌产品、模糊图

**Video规范**:
- 格式: MP4(.mpg, .avi 也接受)
- 时长: 30-60秒最佳(短于30秒可能不展示)
- 内容: 产品功能演示+使用场景
- 配音: 西班牙语/葡萄牙语(无配音视频权重低)

### Step A7: 价格 + Mercado Pago分期策略

**智能定价建议**:
- 参考 Top 10 竞品价格(中位数)
- 包含 Mercados Envíos 运费(免运费产品需自补贴)
- 利润率 ≥ 20%(美客多平均)

**分期 (Cuotas) 启用规则**:
- 商品价格 > $50 USD等值 → 建议启用 12期免息
- 价格 > $100 USD等值 → 建议启用 18期免息
- **Cuotas启用后,客单价平均提升30-50%**

### Output: 完整listing包

```markdown
# ✅ 美客多 Listing — Ready to Use

## Título (60字符显示 / 完整版)
[optimized title — copy this directly to 美客多 Listing form]

## Ficha Técnica
[Brand]: [value]
[Model]: [value]
[GTIN/EAN]: [value]
[Color]: [value]
[属性1]: [value]
[属性2]: [value]
...

## Descripción
[description text — 西语或葡语,copy this directly to 美客多]

## Fotos Plan
1. [Image 1 plan - 白底主图]
2. [Image 2 plan - 侧面图]
3. [Image 3 plan - 场景图]
4. ...

## Video Script (optional)
[30-60秒西语/葡语脚本]

## Precio Sugerido
- Precio: $[amount] [MXN/BRL]
- Cuotas: [6/12/18] x $[amount] sin interés
- Competencia mediana: $[X]
- Full recomendado: Sí/No

---

# 🔬 Diagnostic — How We Built This Listing

**Marketplace:** 美客多 Mexico | **Tone:** [tone] | **Keywords imported:** [count]
**Título characters:** [X]/60 (display limit) / [X]/120 (full)
**Ficha Técnica fields:** [X]/[Y] (覆盖率[X]%)

## Keyword Coverage: [X]%

| Keyword | In Título | In Ficha Técnica | In Descripción | Status |
|---------|-----------|------------------|----------------|--------|
| [kw] | ✅/❌ | ✅/❌ | ✅/❌ | 🔴/🟡/🟢 |

## Keyword Priority Breakdown
🔴 Primary (Título): [list]
🟡 Secondary (Ficha Técnica): [list]
🟢 Tertiary (Descripción): [list]
```

## Mode B Workflow — Audit + Optimize Existing Listing

### Step B1: 拉取目标listing

用户提供: 
- 美客多 URL(推荐),或
- MLMID(MLM-123456),或
- 完整listing截图

### Step B2: 拉取竞品listing(可选但推荐)

1-3个Top竞品URL(同关键词排名Top 5)。

### Step B3: 8维度美客多专项审计

#### 维度1: Título (15分)
- [ ] 字符使用(60/120)
- [ ] 品类词前置
- [ ] 品牌词明确
- [ ] 兼容设备词("para iPhone"等)
- [ ] 关键长尾词覆盖(2-3个)
- [ ] 无"nuevo"/"envío gratis"等冗余词
- [ ] 无拼写错误

#### 维度2: Ficha Técnica (15分)
- [ ] 必填字段100%填全
- [ ] EAN/GTIN已填
- [ ] 类目属性覆盖率 ≥ 80%
- [ ] 关键属性(Marca/Modelo/Color)准确
- [ ] 与Top竞品对比属性差异点突出

#### 维度3: Fotos (15分)
- [ ] 数量(推荐8-12张,最低3张)
- [ ] 首图:白底、产品占比80%+
- [ ] 包含多角度(正/侧/背/顶)
- [ ] 包含场景图(产品在用)
- [ ] 包含尺寸对照
- [ ] 包含品牌/型号展示
- [ ] 无水印/价格/竞品logo

#### 维度4: Video (10分)
- [ ] 是否有视频
- [ ] 时长(30-60秒)
- [ ] 西班牙语/葡萄牙语配音
- [ ] 展示核心功能(不是静态画面)

#### 维度5: Descripción (10分)
- [ ] 长度(>500字符为佳,>1500字符优秀)
- [ ] 钩子开头
- [ ] 卖点bullet化
- [ ] 规格表
- [ ] FAQ/常见问题
- [ ] 品牌故事/信任元素
- [ ] 自然融入长尾关键词(2-3%密度)

#### 维度6: Precio (10分)
- [ ] 价位 vs Top竞品(中位数±15%内)
- [ ] 是否含免运费(>299 MXN)
- [ ] 是否启用 Mercado Pago 分期
- [ ] 利润率 ≥ 20%

#### 维度7: Reputación (15分)
- [ ] 卖家等级(MercadoLíder → 流量加权)
- [ ] 历史评分(>4.5⭐)
- [ ] 完整售后率(>95%)
- [ ] 售出/取消比
- [ ] 多久在售(>3个月)

#### 维度8: SEO Coverage (10分)
- [ ] 核心关键词在 Título 出现
- [ ] 长尾词在 Ficha Técnica
- [ ] 自然词在 Descripción
- [ ] 无关键词堆砌(美客多严打)
- [ ] 同义词覆盖(本地化叫法)

**总分 = 100分,按维度加权求和**。

### Output: Mode B — Audit + Optimized Listing

```markdown
# ✅ Optimized 美客多 Listing — Ready to Use

## Título
[optimized title — copy directly]

## Ficha Técnica
[optimized ficha técnica fields]

## Descripción
[optimized description]

---

# 🔬 Audit Report: [MLMID]

**Producto:** [title] | **Marca:** [brand]
**Precio:** [price] | **Rating:** [stars] ([count] reviews)

## Score: [X/100] → [Y/100] (after optimization)

| Dimension | Before | After | Key Change |
|-----------|--------|-------|-----------|
| Título | /15 | /15 | [what changed] |
| Ficha Técnica | /15 | /15 | [what changed] |
| Fotos | /15 | — | [recommendation only] |
| Video | /10 | — | [recommendation only] |
| Descripción | /10 | /10 | [what changed] |
| Precio | /10 | — | [observation] |
| Reputación | /15 | — | [observation] |
| SEO Coverage | /10 | /10 | [what changed] |

## Keyword Coverage: [X]% → [Y]%

| Keyword | Before | After | Where Added |
|---------|--------|-------|-------------|
| [kw] | ❌ | ✅ | Título + Ficha Técnica |
| [kw] | ✅ Título only | ✅ Título + Ficha | Ficha Técnica field X |

## What Changed (Before → After)

**Título:**
> ❌ [original]
> ✅ [optimized]

**Ficha Técnica:**
> ❌ Color: Negro (only field filled)
> ✅ [10+ fields filled, including EAN, model, garantía]

## 🔴 Issues Fixed
1. [what was wrong → how we fixed it]

## 🟡 Recommendations (requires seller action)
1. [image improvements, video, pricing — things the skill can't rewrite]

## 🟢 What Was Already Working
1. [positive aspects preserved]
```

### Competitive Comparison (if requested)

| Dimension | Tu Listing | Competidor 1 | Competidor 2 | Competidor 3 |
|-----------|-----------|-------------|-------------|-------------|
| Título score | /15 | /15 | /15 | /15 |
| Ficha Técnica score | /15 | /15 | /15 | /15 |
| Fotos | [count] | [count] | [count] | [count] |
| Video | Yes/No | Yes/No | Yes/No | Yes/No |
| Keyword coverage | X% | X% | X% | X% |
| Precio | [X] | [X] | [X] | [X] |
| Rating | [X] | [X] | [X] | [X] |
| **Total** | **/100** | **/100** | **/100** | **/100** |

## LATAM-Specific Best Practices

### 🇲🇽 Mexico Specific
- **语言**: 西班牙语(中性,不夹杂"vosotros"等阿根廷用法)
- **敬语**: "Usted" 形式更专业
- **节日**: Día de la Madre, El Buen Fin, Hot Sale
- **价格档**: <$299 MXN触发运费(需Full免运费)

### 🇧🇷 Brazil Specific
- **语言**: 葡萄牙语(必须,西语无效)
- **称呼**: "você" 而非"tu"
- **节日**: Dia das Mães, Black Friday, Natal
- **价格档**: <R$79触发附加费;免费包邮>79
- **付款**: 巴西用户重分期(installments)

### 🇨🇱 Chile / 🇨🇴 Colombia Specific
- **语言**: 西班牙语(可与MX共用listing翻译)
- **量级**: 较MX小,但竞争低

## Output Language Rules (CRITICAL)

**Output language must match the target marketplace, NOT the user's conversation language**:
- 🇲🇽 Mexico / 🇨🇱 Chile / 🇨🇴 Colombia / 🇦🇷 Argentina → **西班牙语 (Spanish)**
- 🇧🇷 Brazil → **葡萄牙语 (Portuguese)**

如果用户用中文对话但要生成美客多Mexico listing,整个 listing (título + ficha técnica + descripción) **必须用西班牙语**,而 diagnostic 部分可用中文/英文说明。

## Integration with Other Skills

### 与 `mercado-keyword-research` 联动(强烈推荐):

```
Step 1: "研究'audífonos bluetooth'在美客多墨西哥站的关键词"
   → mercado-keyword-research 返回 100+ 长尾关键词(西语)

Step 2: "用这些关键词给我做一个完整 listing,产品: 蓝牙5.3 40h续航, 语调:Friendly"
   → mercado-listing-optimization Mode A 生成完整西语 listing
```

### 与 `mercado-product-research` 联动:
- 用选品报告的"竞品URL"作为 Mode A 的竞品输入
- 用选品报告的目标价位作为 Mode B 优化参考

## 美客多 vs Amazon Listing 关键差异(警告!)

| 维度 | Amazon | 美客多 | 后果 |
|------|--------|--------|------|
| Backend keywords | ✅ 250字节独立字段 | ❌ 不存在 | 必须自然融入ficha técnica |
| Title可编辑性 | ✅ 可改 | ⚠️ 首次售卖后不可改 | 上架前必须确认 |
| 标题字符显示 | 80(移动)/ 200(完整) | 60(显示)/ 120+ | 拉美更短,密度更高 |
| A+ Content | ✅ 富文本 | ❌ 不存在(只Ficha Técnica) | 转化手段靠ficha + descripción |
| A/B Test | ✅ 官方 | ❌ 不存在 | 一次到位,无试错 |
| 语言本地化 | 12种市场 | 西/葡(巴西必须葡) | 拉美本地化更严格 |
| 关键算法 | A9 | **Título (60%)** + Ficha (30%) + Desc (10%) | 标题为王 |
| 分期付款 | ❌ 不存在 | ✅ Mercado Pago核心 | 高客单必备 |

## 美客多大促listing备战 checklist

### Hot Sale 5月底(墨西哥)
- [ ] Premium listing 升级完成
- [ ] Full 海外仓入仓(3-5天送达)
- [ ] 12期免息启用
- [ ] 标题添加 "Hot Sale" (部分类目允许)
- [ ] 库存 ≥ 旺季 3倍
- [ ] 价格折扣 10-30%

### El Buen Fin 11月(墨西哥全年最大)
- [ ] 同上 + 库存 ≥ 5倍
- [ ] 提前 9月 Full 备货
- [ ] 报名官方优惠券活动
- [ ] 视频素材提前1月拍好

### Black Friday 11月(全站)
- [ ] 多站点同步listing
- [ ] 葡萄牙语版本同步更新(巴西)
- [ ] 库存全Full仓

## Limitations

This skill uses publicly available data from MercadoLibre product pages, official trends site, and web search. It cannot:
- Access exact search volume data (需蓝鲸BI/UpSeller)
- Modify existing listing fields directly (需手动粘贴到美客多后台)
- Access real-time competitor pricing (需监控工具)
- Predict exact ranking changes (需A/B测试,美客多不支持)

---

*基于美客多官方文档 + 2026算法解读 + 拉美本地化经验设计。对于实时数据和批量listing管理,推荐搭配蓝鲸BI/UpSeller ERP使用。*
