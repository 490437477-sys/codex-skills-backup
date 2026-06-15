---
name: mercado-keyword-research
description: "Mercado Libre (美客多) keyword research and market opportunity analysis for cross-border sellers. Retrieve autocomplete & trending searches from official tendencias.mercadolibre.com.*, extract long-tail Spanish/Portuguese keywords with a-z expansion, analyze competition density across Mexico (MLM), Brazil (MLB), Chile (MLC), Colombia (MCO) sites, validate demand with Google Trends LATAM, score market opportunity 1-10. Use when the user asks about 美客多关键词, 美客多选词, mercado libre keyword research, palabras clave mercado libre, what to sell on 美客多, 美客多流量关键词, 美客多大词, search term analysis, autocomplete mining, niche analysis for 美客多, mercado libre niche finder, or 美客多蓝海词."
metadata: {"emoji":"🔍","category":"mercadolibre"}
---

# Mercado Libre Keyword Research 🔍

Free keyword research and market opportunity analysis for 美客多 (Mercado Libre) cross-border sellers. No API key — works out of the box. Native Spanish & Portuguese support.

## When to Use

Activate this skill whenever the user mentions:
- 美客多关键词, 美客多选词, 美客多流量词, 美客多大词, 美客多长尾词
- Mercado Libre keyword research, 美客多选品
- palabras clave mercado libre, palavras-chave mercado livre
- What people search on 美客多, autocomplete, MELI Trends
- Comparing niches on Mercado Libre, market opportunity
- LATAM keyword research, 拉美关键词

## Capabilities

- **Official trending data** (核心数据源): Pull from `tendencias.mercadolibre.com.{mx,br,cl,ar,co}` — Mercado Libre's official weekly trending searches
- **MELI Trends annual report**: Mexico 3B+ searches/year analyzed; top 10 search terms are 80% generic in MX/AR/BR
- **Autocomplete mining**: Seed + a-z suffix + Spanish/Portuguese prefix expansion ("mejor", "barato", "para", "kit", "comprar")
- **Local terminology mapping**: 拉美西语/葡语叫法 ≠ 英文 ≠ 中文
- **Competition analysis**: Per-site listing count, price range, dominant brands, Full coverage
- **Seasonal trends**: Google Trends LATAM geo-targeting (`&geo=MX/BR/CL/CO`)
- **Market opportunity scoring**: 1-10 score combining competition, demand, profit potential
- **Multi-marketplace support**: Mexico (MLM), Brazil (MLB), Chile (MLC), Colombia (MCO), Argentina (MLA)

## Target Sites & Language Mapping

| Site | TLD | Search URL | Language | Geo for Google Trends |
|------|-----|-----------|----------|---------------------|
| Mexico | mercadolibre.com.mx | listado.mercadolibre.com.mx | 🇪🇸 西班牙语 | `geo=MX` |
| Brazil | mercadolivre.com.br | lista.mercadolivre.com.br | 🇧🇷 葡萄牙语 | `geo=BR` |
| Chile | mercadolibre.cl | listado.mercadolibre.cl | 🇪🇸 西班牙语 | `geo=CL` |
| Colombia | mercadolibre.com.co | listado.mercadolibre.com.co | 🇪🇸 西班牙语 | `geo=CO` |
| Argentina | mercadolibre.com.ar | listado.mercadolibre.com.ar | 🇪🇸 西班牙语 | `geo=AR` |

**🌎 推荐优先研究**: Mexico (首选, 大盘) → Brazil (高潜) → 西班牙语共享的Chile/Colombia

## Usage Examples

```
研究"brazo robótico"在美客多墨西哥站的关键词机会
```

```
Find long-tail Spanish keywords for "audífonos bluetooth" on Mercado Libre Mexico
```

```
我想做"手机壳"在美客多,关键词机会怎么样?
```

```
Compare "soporte para celular" vs "cargador portátil" on Mercado Libre Mexico — which has more opportunity?
```

```
分析"fone de ouvido bluetooth"(蓝牙耳机)在美客多巴西站的搜索热度
```

```
研究"kit robótica educativa"在墨西哥和巴西的差异
```

```
Use MELI Trends 2025 data to find trending electronic categories on Mercado Libre Mexico
```

## Workflow

### Step 1: 拉取美客多官方趋势数据 ⭐(独家)

Mercado Libre 官方提供了**公开的周度趋势数据**,这是最权威的关键词源:

| 站点 | 官方趋势URL |
|------|------------|
| Mexico | `https://tendencias.mercadolibre.com.mx` |
| Brazil | `https://tendencias.mercadolivre.com.br` |
| Chile | `https://tendencias.mercadolibre.cl` |
| Colombia | `https://tendencias.mercadolibre.com.co` |
| Argentina | `https://tendencias.mercadolibre.com.ar` |

**通过 `mcp__tavily__tavily_extract` 拉取**,提取:
1. **Productos más buscados (最热搜产品)** — 拉美周度Top热搜
2. **搜索按字母分类** — 输入a-z,看每个首字母下用户搜什么
3. **Temporadas (季节性节点)** — 官方标注的即将到来的需求节点

**Why this matters**: 这是**直接来自美客多搜索框的实时数据**,比任何第三方工具都准确,而且**完全免费**。

### Step 2: Autocomplete扩展(西语/葡语优化版)

美客多搜索框的autocomplete是**黄金关键词源**。通过 `mcp__tavily__tavily_search` 模拟用户行为:

#### 西班牙语前缀(用于MX/CL/CO/AR):
```
mejor [keyword]
mejor [keyword] 2025
barato [keyword]
[keyword] barato
[keyword] oferta
[keyword] descuento
[keyword] envío gratis
[keyword] calidad
[keyword] profesional
[keyword] para [use case]
[keyword] para niños
[keyword] para mujer / hombre
comprar [keyword]
kit [keyword]
set [keyword]
[keyword] inalámbrico
[keyword] recargable
[keyword] portátil
```

#### 葡萄牙语前缀(用于BR):
```
melhor [keyword]
[keyword] melhor
barato [keyword]
[keyword] em oferta
[keyword] com desconto
[keyword] frete grátis
[keyword] profissional
[keyword] portátil
[keyword] recarregável
[keyword] sem fio
comprar [keyword]
kit [keyword]
```

#### 字母后缀(a-z扩展):
```
[keyword] a
[keyword] b
[keyword] c
...
[keyword] z
```

**What to extract:**
- 真实用户搜索词(去重)
- 长尾关键词(3+词)
- 本地化叫法差异(关键!)

**Example**:
```
"audífonos bluetooth" MX autocomplete:
→ audífonos bluetooth inalambricos
→ audífonos bluetooth para iphone
→ audífonos bluetooth baratos
→ audífonos bluetooth samsung
→ audífonos bluetooth pequeños
```

### Step 3: 本地化术语映射(关键步骤!)

**拉美西/葡语叫法 ≠ 英文 ≠ 中文**。在美客多上,你的listing和关键词必须用**当地用户实际搜的词**。

#### 翻译陷阱示例:

| 中文 | 英文 | **美客多MX实际叫法** | 美客多BR叫法 |
|------|------|-------------------|------------|
| 蓝牙耳机 | Bluetooth earbuds | **audífonos bluetooth** / auriculares inalambricos | **fone de ouvido bluetooth** |
| 手机壳 | Phone case | **funda para celular** / estuche celular | **capa para celular** |
| 手机支架 | Phone stand | **soporte para celular** | **suporte para celular** |
| 充电宝 | Power bank | **cargador portátil** / powerbank | **carregador portátil** |
| 智能手表 | Smart watch | **reloj inteligente** | **relógio inteligente** |
| 数据线 | USB cable | **cable usb** | **cabo usb** |
| 机械臂 | Robotic arm | **brazo robótico** / brazo robot | **braço robótico** |
| 3D打印机 | 3D printer | **impresora 3d** | **impressora 3d** |
| 空气炸锅 | Air fryer | **freidora de aire** | **airfryer** / fritadeira elétrica |
| 婴儿车 | Stroller | **carriola** / coche para bebé | **carrinho de bebê** |
| 化妆刷 | Makeup brush | **brochas de maquillaje** | **kit de pincéis** |
| 行李箱 | Suitcase | **maleta** / equipaje | **mala de viagem** |
| 电动牙刷 | Electric toothbrush | **cepillo de dientes eléctrico** | **escova de dente elétrica** |

### Step 4: 竞争分析

通过 `mcp__tavily__tavily_search` 拉取竞争数据:

1. **Listing密度**: `"[keyword]" site:mercadolibre.com.mx` — 总结果数
2. **价格区间**: `"mejor [keyword]" mercadolibre precio` — Top结果的价位
3. **品牌主导**: `"[keyword]" mercadolibre marca popular` — 是否有Xiaomi/Anker/Samsung等大牌
4. **Full覆盖**: 抽样看Top 20结果中,带"Mercado Envíos Full"标签的占比
5. **评分分布**: Top结果的星级和评价数

**Why this matters**: 拉美消费者高度价格敏感,且Full商品有显著转化优势,这两个数据点直接影响你的定价和物流策略。

### Step 5: 季节性验证

1. **Google Trends LATAM**: 用对应站点geo参数
   - `https://trends.google.com/trends/explore?q=[keyword]&geo=MX`
   - `https://trends.google.com/trends/explore?q=[keyword]&geo=BR`
   - 同时拉过去12个月和过去5年趋势(看长期方向)

2. **美客多大促日历匹配**:
   - 🇲🇽 Mexico: Hot Sale (5月底-6月初), El Buen Fin (11月), Buen Fin延伸到12月圣诞
   - 🇧🇷 Brazil: Dia das Mães (5月), Black Friday (11月), Natal (12月)
   - 🇨🇱 Chile: Cyber Day (6月初), Black Friday (11月)
   - 🇨🇴 Colombia: Black Friday (11月), Día sin IVA (3次/年)

3. **拉美独有节日**:
   - Día de la Madre (5月10日 MX) - 美妆/家居流量高峰
   - Día del Padre (6月第三个周日 MX) - 电子产品流量
   - Día de Muertos (11月1-2日 MX) - 装饰类
   - Día de Reyes (1月6日 MX) - 玩具
   - Volta às Aulas (1-2月 BR) - 开学季

### Step 6: 综合评分(1-10)

**MercadoLibre-Adapted Scoring**:

| 维度 | 权重 | 评分逻辑 |
|------|------|---------|
| 搜索热度 | 25% | autocomplete丰富度+trending出现频次 |
| 竞争密度(反) | 25% | listing数 + Top 3品牌集中度(反) |
| 价格空间 | 15% | 平均价 vs 1688供货价(毛利空间) |
| 需求趋势 | 15% | Google Trends 12个月方向(上升/稳定/下降) |
| 季节性(反) | 10% | 越常年得分越高 |
| Mercado Pago适配(反) | 5% | 商品价格是否>$50(分期可启用) |
| 跨站点复用 | 5% | 是否能多站点共用listing |
| 合规风险(反) | 5% | 需认证类目扣分 |

**总分 ≥ 7.0**: 优质词
**5.0-7.0**: 需进一步研究
**< 5.0**: 红海或需求不足

## Output Format

```markdown
## 关键词研究报告: [keyword]
**站点:** MercadoLibre [Mexico/Brazil/Chile/Colombia]
**日期:** [current date]
**语言:** [Spanish/Portuguese]

### 1. 长尾关键词 ([count] 找到)

**高商业意图 (购买导向):**
- [包含"mejor"/"barato"/"comprar"/"oferta"等的词]
- ...

**信息性/研究型:**
- [包含"que es"/"como"/"opiniones"/"review"等的词]
- ...

**本地化特色:**
- [拉美本地叫法、节日相关、用户群体相关]
- ...

**细分类目:**
- [3+词的长尾精准词,明确购买意图]
- ...

### 2. 竞争格局

| 指标 | 数值 |
|------|------|
| 估计竞品listing数 | [数字] |
| 价格区间 | $[min] - $[max] (MXN/BRL) |
| 平均价格 | $[avg] (MXN/BRL) |
| 平均评分 | [stars] |
| Full商品占比 | [X]% |
| Top 5品牌 | [brand1, brand2, ...] |

### 3. 季节性趋势

**Google Trends (12个月):**
- 方向: [上升/稳定/下降]
- 旺季: [月份]
- 与大促节点匹配度: [高/中/低]

**美客多大促日历匹配:**
- 下一波流量节点: [节日名] ([日期])
- 备战建议: [动作]

### 4. 拉美本地化洞察

**关键术语映射:**
- 官方/技术名: [English term]
- 拉美用户实际搜索: [Spanish/Portuguese term]
- 简写/口语叫法: [variant]

**文化适配点:**
- [节日/颜色/尺寸/文化禁忌等]

### 5. 市场机会评分: [X/10] ⭐

**评分明细:**
- 搜索热度: [高/中/低] — [原因]
- 竞争密度(反): [低/中/高] — [原因]
- 价格空间: [高/中/低] — [预估毛利]
- 需求趋势: [上升/稳定/下降] — [原因]
- 季节性(反): [常年/中等/强季节] — [原因]
- 跨站点复用: [高/中/低] — [原因]

**推荐:** [1-2句可执行建议]
```

## Multi-Keyword Comparison

When user asks to compare 2+ keywords, run the full workflow for each, then present side-by-side:

| 指标 | [keyword A] | [keyword B] | [keyword C] |
|------|-------------|-------------|-------------|
| 长尾词数 | ... | ... | ... |
| 平均价格(MXN) | ... | ... | ... |
| Top品牌集中度 | ... | ... | ... |
| Full覆盖 | ... | ... | ... |
| 趋势方向 | ... | ... | ... |
| 季节性 | ... | ... | ... |
| 跨站点 | ... | ... | ... |
| **机会评分** | **X/10** | **X/10** | **X/10** |

最后给 **推荐**: 哪个关键词机会最好,为什么。

## LATAM-Specific Heuristics

### 🌎 本地化三大陷阱

1. **巴西必须是葡萄牙语** — 用西语上巴西站 = 0搜索权重,即使你懂西语
2. **本地叫法≠翻译** — 翻译"蓝牙耳机"得到"auriculares bluetooth",但墨西哥人搜"audífonos bluetooth"
3. **复数形式重要** — 拉美用户更倾向搜复数("audífonos"比"audífono"多3-5倍)

### 📅 拉美独有流量节点

| 节日 | 国家 | 日期 | 适用类目 |
|------|------|------|---------|
| Día de Reyes | MX | 1月6日 | 玩具、儿童用品 |
| Día del Cariño | MX | 2月14日 | 礼品、珠宝 |
| Día de la Madre | MX/CO/AR | 5月10日 | 美妆、家居、时尚 |
| Hot Sale | MX | 5月底-6月初 | 全部 |
| Cyber Day | CL | 6月初 | 全部 |
| Dia das Mães | BR | 5月第2周日 | 美妆、家居 |
| Volta às Aulas | BR | 1-2月 | 书包、文具、3C |
| Día del Padre | MX | 6月第3周日 | 3C、工具 |
| El Buen Fin | MX | 11月中旬 | 全部(全站最大) |
| Black Friday | 全站 | 11月底 | 全部 |
| Cyber Monday | 全站 | 12月初 | 3C、电器 |
| Navidad | 全站 | 12月 | 礼品、装饰 |
| Año Nuevo | 全站 | 12月31日 | 礼品、时尚 |
| Día sin IVA | CO | 3次/年 | 大宗3C电器 |

### 💡 美客多搜索行为特征

- **60%的美客多买家用关键词搜索**(非类目浏览)
- **8/10 美客多Top 10搜索词是通用词**(如"soporte para celular"而非品牌+型号)
- **品牌词搜索弱于Amazon** — 拉美用户更倾向搜品类+特性
- **长尾词转化率高于大词** — 拉美买家搜索意图更明确
- **拼写错误普遍** — 自动建议很有价值

## Integration with Other Skills

**与 `mercado-listing-optimization` 联动**:
1. 本skill输出关键词清单(按优先级)
2. 直接喂给 `mercado-listing-optimization` Mode A
3. 生成完整西/葡语listing

**与 `mercado-product-research` 联动**:
1. 本skill找候选关键词(10-20个)
2. `mercado-product-research` 跑8因子评分选最终品类
3. 回到本skill深挖top 3关键词的autocomplete

## Limitations

This skill uses publicly available data:
- Official tendencias.mercadolibre.com.* trending data
- MercadoLibre public search autocomplete (via web search)
- Google Trends (geo-targeted LATAM)
- Web search for competitor intelligence

**无法提供**:
- 精确月搜索量(美客多不公开,需用蓝鲸BI/UpSeller等付费工具)
- 真实订单量(只能估算)
- 广告竞价数据(需用Mercado Ads后台)

**For deeper analytics**: 蓝鲸BI (`lingdongsz.com`), UpSeller ERP (`upseller.com`)

---

*基于公开美客多官方数据 + 拉美本地化经验设计。对于精确搜索量和订单预估,推荐搭配蓝鲸BI/UpSeller使用。*
