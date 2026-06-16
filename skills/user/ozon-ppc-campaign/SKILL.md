---
name: ozon-ppc-campaign
description: "Ozon Performance (Продвижение / Трафареты / Product Targeting) campaign builder and optimizer for Russian-market sellers. Two modes: (A) Build — design campaign structure with Russian keyword groupings (from $ozon-keyword-research), bid calculations using ДРР (Ozon ACoS), НДС-aware budgets, Russian negative keyword lists; (B) Optimize — audit campaigns via search term reports, find Russian keyword funnel opportunities, calculate bid adjustments, generate weekly action plans. Covers all Ozon campaign types (Поиск / Категория / Трафареты / Карточка товара), match types (Уточнение / Фраза / Авто), bid strategies (Максимум показов / Минимальная цена / Manual). Use when: Ozon PPC setup, Ozon Performance реклама, продвижение на Озоне, Ozon search promotion, Ozon ДРР optimization, Ozon ad campaign audit, Ozon трафареты, Ozon product targeting, как настроить рекламу на Озоне."
metadata: {"emoji":"📢","category":"ozon"}
---

# Ozon PPC Campaign Optimization 📢

Build profitable Ozon Performance campaign structures from scratch, or audit and optimize existing campaigns with data-driven bid adjustments. No API key — works out of the box.

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Build** | Launching Ozon Performance for a new product | Product info + Russian keywords (from $ozon-keyword-research) + margins | Complete campaign blueprint + Russian keyword groupings + initial bids + ДРР-based budget |
| **B — Optimize** | Improving existing Ozon Performance campaigns | Campaign data + search term reports + current ДРР | Optimization plan + bid adjustments + Russian negative keyword list |

## Capabilities

- **ДРР financial framework**: Calculate break-even ДРР (Доля рекламных расходов = ACoS), target ДРР, Max CPC from product margins + НДС handling — the foundation for every bid decision
- **Campaign architecture design**: Build a structured Russian-language campaign funnel:
  - **Поиск (Search Promotion)** — keyword-targeted, appears in Ozon search results
  - **Категория (Category Promotion)** — appears in category pages
  - **Трафареты (Banner/Display)** — banners across search, category, home, product pages
  - **Карточка товара (Product Page Promotion)** — competitor product pages (similar to Amazon Product Targeting)
- **Russian keyword grouping**: Organize Russian long-tail keywords (output of $ozon-keyword-research) into campaign buckets by commercial intent
- **Bid optimization**: Apply ДРР-based bid adjustment rules using Russian CPC ranges per category (Electronics, Home, Beauty, Fashion, Toys, etc.)
- **Lifecycle phase bidding**: Different ДРР targets for launch / growth / mature / defense phases
- **Keyword funnel analysis**: Identify migration opportunities from auto-targeting → exact keyword campaigns
- **Negative keyword management**: Russian-language seed lists (cross-campaign, irrelevant terms, Russian waste modifiers like "бесплатно", "б/у", "ремонт")
- **Search term report analysis**: Parse user-provided Ozon campaign data to find profitable terms, wasteful terms, optimization gaps
- **Competitor SKU targeting**: Build product targeting campaigns aimed at competitor product pages
- **Integration chain**: Works with $ozon-keyword-research for keyword input and $ozon-listing-optimization for pre-launch listing quality checks

## Usage Examples

### Mode A — Build New Campaigns

```
I'm launching a portable blender on Ozon. Price: ₽3500. Product cost: ¥180. Commission 12%. Here are my Russian keywords: блендер портативный, блендер для смузи, USB блендер. Build me an Ozon Performance campaign structure.
```

```
Use $ozon-keyword-research to find Russian keywords for "электрическая зубная щётка", then build an Ozon Performance campaign. Product costs ¥60, sells for ₽1500. Brand new launch.
```

```
Хочу рекламировать мужскую футболку (SKU 123456789) на Озоне. Цена ₽1500, себестоимость ¥50. Посмотри конкурентов https://www.ozon.ru/product/... и https://www.ozon.ru/product/..., извлеки их ключевые слова и построй кампанию.
```

### Mode B — Optimize Existing Campaigns

```
Мой ДРР на Озоне 45% а хочу 20%. У меня 3 кампании: Поиск (₽30k/мес, ДРР 55%), Категория (₽20k, ДРР 35%), Трафареты (₽10k, ДРР 60%). Маржа 25%. Помоги оптимизировать.
```

```
Here's my Ozon search term report [paste data]. Break-even ДРР is 15%. Find wasted spend, tell me what to negate and what to migrate from auto to exact.
```

```
Weekly Ozon PPC check: here are this week's search terms with clicks and sales [data]. Add negatives for 10+ clicks with no sales, move 2+ orders to Поиск Exact.
```

### Short Prompts Work Too

```
Help me set up Ozon Performance for my product
```
```
My ДРР is too high on Ozon, help me fix it
```
```
Хочу запустить рекламу на Озоне
```

---

## Mode A Workflow — Build New Campaigns

### Step A1: Collect Input

Progressive information gathering — extract what's available, ask for the rest:

**Required:**
- Selling price (₽) and product cost (CNY or ₽)
- Ozon commission % (from $ozon-product-research or seller panel)
- Russian keyword list (from $ozon-keyword-research) — most important
- Target ДРР % (or use defaults based on lifecycle phase)

**Optional:**
- Lifecycle phase (launch / growth / mature / defense)
- Monthly order target
- Competitor SKU URLs (for product targeting)
- Existing Ozon seller data (for optimization mode)

### Step A2: Calculate ДРР Framework

Run the bundled bid calculator:

```bash
python <skill>/scripts/ozon_ppc_bid_calc.py --interactive
# or
python <skill>/scripts/ozon_ppc_bid_calc.py --json '{"selling_price_rub":1500,"product_cost_cny":50,...}'
```

The calculator outputs:
- Break-even ДРР % (max ДРР before losing money)
- Max CPC ceiling from target ДРР
- Recommended bid per category CPC range
- Phase-tuned daily budget

**Critical math:**

```
Max CPC = (Target ДРР × Price × Conversion Rate) / 100

Example: 20% ДРР × ₽1500 × 2% conv = ₽6 max CPC
```

### Step A3: Group Russian Keywords into Campaign Buckets

Organize the keyword list from $ozon-keyword-research into:

| Bucket | Keyword type | Initial bid | Match type |
|--------|--------------|-------------|------------|
| **High-intent Exact** | купить [товар], [товар] цена, [товар] заказать | 100% of max CPC | Уточнение (Exact) |
| **Brand / Category** | [бренд] + [модель] | 90% of max CPC | Уточнение (Exact) |
| **Long-tail Phrase** | [товар] для [назначение], [товар] + 2-3 слова | 70% of max CPC | Фраза (Phrase) |
| **Auto-discovery** | All other long-tail + declensions | 50% of max CPC | Автоматическая (Auto) |
| **Excluded** | б/у, бесплатно, ремонт, инструкция | Negative only | — |

**Russian-specific grouping notes:**
- Always group by **commercial intent** (купить, цена, заказать → high intent)
- Group by **declension forms** together (наушник + наушники + наушников all in same ad group)
- Group by **qualifier** (для дома, для спорта → separate ad groups for each)
- Group by **transliteration** (bluetooth наушники separately from беспроводные наушники)

### Step A4: Build Campaign Structure

A typical Ozon Performance launch structure has 3-4 campaigns:

#### Campaign 1: Поиск Exact (Priority 1)
- **Goal**: Convert high-intent buyers
- **Bid**: Max CPC ceiling (target ДРР)
- **Budget**: ₽800-1500/day
- **Keywords**: All "купить [товар]" + brand + model exact matches

#### Campaign 2: Поиск Phrase + Auto (Priority 2)
- **Goal**: Discovery + long-tail harvesting
- **Bid**: 50-70% of max CPC
- **Budget**: ₽500-1000/day
- **Keywords**: Long-tail Russian variations + auto-discovery

#### Campaign 3: Категория + Трафареты (Priority 3)
- **Goal**: Visibility on category + browse pages
- **Bid**: CPM-based for Трафареты, CPC for Категория
- **Budget**: ₽300-800/day
- **Targeting**: Top 3-5 relevant categories

#### Campaign 4: Карточка товара (Priority 4)
- **Goal**: Intercept competitor buyers
- **Bid**: ₽5-30 (typical)
- **Budget**: ₽300-500/day
- **Targets**: 5-10 competitor SKUs with similar products

### Step A5: Build Negative Keyword Master List

Russian negative keyword categories:

**Waste modifiers** (always negate):
- бесплатно, бесплатный, даром
- б/у, бу, подержанный, авито (suggesting used market)
- ремонт, запчасти, инструкция
- своими руками, самодельный
- оптом (B2B for B2C sellers)
- промокод, скидка 90%, акция (deal hunters)

**Irrelevant verticals**:
- [товар] аналог, [товар] замена, [товар] обзор
- [товар] скачать, [товар] торрент
- [товар] вакансия, [товар] работа

**Foreign / transliteration conflicts**:
- When targeting "наушники", exclude "headphones"
- When targeting Cyrillic, exclude English brand variants unless intentional

### Step A6: Output — Ready-to-Launch Blueprint

```
# ✅ Ozon Performance Campaign Blueprint — Ready to Launch

## Phase: LAUNCH | Target ДРР: 25%

## Campaign 1: Поиск — Высокочастотные Exact
BUDGET:  ₽1,000/day
BID:     ₽X.XX (max CPC ceiling for 25% ДРР)

AD GROUP 1.1: [Бренд] + [Модель]
  KEYWORDS (Уточнение):
    [keyword 1]    ₽X.XX
    [keyword 2]    ₽X.XX
    [declension 1] ₽X.XX
    [declension 2] ₽X.XX

AD GROUP 1.2: Купить [товар]
  KEYWORDS (Уточнение):
    купить [товар]       ₽X.XX
    [товар] цена          ₽X.XX
    [товар] заказать      ₽X.XX
    ...

NEGATIVE KEYWORDS (campaign-wide):
  б/у, бесплатно, ремонт, оптом, ...

## Campaign 2: Поиск — Long-tail Phrase
BUDGET:  ₽700/day
BID:     ₽X.XX (70% of max CPC)

AD GROUP 2.1: [Товар] для [назначение]
AD GROUP 2.2: [Товар] + качественные прилагательные
...

## Campaign 3: Категория + Трафареты
BUDGET:  ₽500/day
BID:     ₽X.XX (CPC) or ₽XXX CPM (Трафареты)

CATEGORIES:
  [Category 1]
  [Category 2]
  [Category 3]

## Campaign 4: Карточка товара
BUDGET:  ₽400/day
BID:     ₽10/click (typical)

TARGET SKUs:
  [Competitor SKU 1] | [competitor title]
  [Competitor SKU 2] | [competitor title]
  ...

## Budget Summary
| Campaign | Priority | Daily | Monthly | Role |
|----------|:--------:|-------|---------|------|
| Поиск Exact | P1 | ₽1,000 | ₽30,000 | Convert high-intent |
| Поиск Phrase | P2 | ₽700 | ₽21,000 | Discover long-tail |
| Категория+Трафареты | P3 | ₽500 | ₽15,000 | Visibility |
| Карточка товара | P4 | ₽400 | ₽12,000 | Intercept competitors |
| **TOTAL** |  | **₽2,600** | **₽78,000** |  |

## Launch Schedule
Day 1:  Create P1 + P2. Verify ads are showing.
Day 3:  Check impressions. If low, increase bids toward category median.
Day 7:  Add P3 + P4. Review search terms — add obvious negatives.
Day 14: Migrate winners (2+ orders) from P2 Auto → P1 Exact with higher bid.
Day 21: Bid optimization — adjust bids for keywords with 20+ clicks.
Day 30: Full review — pause keywords with 30+ clicks and 0 orders.

---

# 📊 Campaign Design Rationale

## ДРР Framework
Max CPC ceiling: ₽X.XX (based on 25% target ДРР × ₽X price × 2% conversion)
Break-even ДРР: XX% (calculated from unit economics)
Recommended launch bid: ₽X.XX (max CPC for max visibility)

## Keyword Sources
From $ozon-keyword-research: [N] Russian keywords across 4 intent buckets.
Total keywords after dedup: [N].

## Russian-Specific Notes
- Падежи: All 6 Russian noun cases included as separate keywords.
- Commercial prefixes: купить / цена / заказать prioritized.
- Qualifiers: для дома / для спорта / для женщин in separate ad groups.
- Negative keywords: б/у, бесплатно, ремонт excluded across all campaigns.
```

### Mode B Output — Optimization Report

```
# ✅ Ozon Performance Optimization Actions — Ready to Implement

## Priority 1: Immediate Negative Keywords (Do Today)
Add these as Negative Уточнение (Exact) in respective campaigns:
  Campaign "Поиск Phrase": "б/у", "ремонт", "бесплатно", ...
  Campaign "Поиск Auto": "запчасти", "инструкция", "скачать", ...
Expected savings: ₽X,XXX/month

## Priority 2: Keyword Migrations (This Week)
Move to Поиск Exact (and add as negative in source):
  "[keyword]" from Auto → Exact, bid: ₽X.XX (2+ orders last 7d)
  "[keyword]" from Phrase → Exact, bid: ₽X.XX (profitable at ДРР XX%)

## Priority 3: Bid Adjustments (This Week)
  "[keyword]": ₽X.XX → ₽X.XX (ДРР XX% → target XX%)
  "[keyword]": ₽X.XX → ₽X.XX (increase — profitable at XX%)
  "[keyword]": PAUSE (XX clicks, 0 orders)

## Priority 4: Budget Reallocation (Next Week)
  Поиск Exact: ₽X/day → ₽X/day (increase — best ДРР)
  Поиск Auto: ₽X/day → ₽X/day (reduce — high waste)
  Трафареты: ₽X/day → ₽X/day (cut — ДРР 60%)

---

# 📊 Full Audit Report

## Performance Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Overall ДРР | XX% | XX% | 🔴🟡🟢 |
| TACoS (ДРР от всей выручки) | XX% | <XX% | 🔴🟡🟢 |
| Monthly Ad Profit | ₽X,XXX | ₽X,XXX | 🔴🟡🟢 |
| Budget Utilization | XX% | >90% | 🔴🟡🟢 |

## Keyword Funnel Analysis
| Keyword | Campaign | Clicks | Orders | ДРР | Action |
|---------|----------|--------|--------|-----|--------|
| [kw 1] | Поиск Auto | 50 | 0 | ∞ | NEGATE |
| [kw 2] | Поиск Phrase | 30 | 3 | 12% | MIGRATE to Exact |
| [kw 3] | Поиск Exact | 25 | 5 | 18% | INCREASE bid |
| [kw 4] | Поиск Phrase | 40 | 0 | ∞ | NEGATE |

## Bid Adjustment Details  
| Keyword | Current Bid | Recommended Bid | Reason |
|---------|-------------|-----------------|--------|
| [kw 1] | ₽X.XX | ₽X.XX | ДРР XX% < target XX% |
| [kw 2] | ₽X.XX | PAUSE | 30+ clicks, 0 orders |

## Week-by-Week Action Plan
**Week 1:**
- Add 8 negative keywords across 3 campaigns (savings ₽3,200/month)
- Migrate 4 profitable search terms from Auto → Exact
- Pause 3 keywords with 30+ clicks and 0 orders
- Expected impact: ДРР -8%, savings ₽5K/month

**Week 2:**
- Increase Exact campaign budget by 30% (profitable keywords found)
- Decrease Auto campaign budget by 40% (high waste)
- Add 5 new negative keywords based on weekly search terms
- Expected impact: ДРР -5%, sales +15%

**Week 3-4:**
- Test product targeting on top 3 competitor SKUs
- Expand keyword coverage to 2nd-tier Russian long-tail
- Review and finalize ДРР target for next month

## Expected Results After 4 Weeks
ДРР: XX% → XX%
Monthly ad spend savings: ₽X,XXX
Sales increase: +XX% (from better targeting)
```

### Key principles

1. The seller's workflow is: **copy the campaign structure → paste into Ozon seller panel → set bids → launch.** The diagnostic section explains WHY those specific bids were chosen, but the campaign blueprint itself must stand alone as a complete, ready-to-use deliverable. Never output only a report without the actual campaign configuration.

2. **Output language must match the marketplace.** Ozon.ru → Russian (default). Ozon.kz → Russian/Kazakh. Ozon.by → Russian. Campaign names, keyword groupings, negative keyword lists, and rationale must all be in Russian. The diagnostic summary can mix English (for the user) but campaign-specific content (ad group names, keywords, negatives) must be Russian.

3. **ДРР > ACoS terminology**: Use "ДРР" (Доля рекламных расходов) by default in Ozon context. Amazon ACoS and Ozon ДРР are mathematically identical, but Russian sellers expect Russian terminology.

4. **НДС (VAT) handling**: Ozon withholds 20% VAT from gross price as tax agent. Sellers receive price excl. VAT. All bid/budget calculations should be on the seller's effective revenue, not gross price.

## Integration with Other Ozon Skills

Recommended chain (do in this order):

```
Step 1: $ozon-product-research
   → Validate product opportunity, get commission %, FBO/FBS decision, margin baseline

Step 2: $ozon-keyword-research
   → Generate Russian long-tail keywords with declensions + commercial prefixes

Step 3: $ozon-listing-optimization (optional but recommended)
   → Optimize listing title + rich content with target keywords BEFORE spending on ads

Step 4: $ozon-ppc-campaign (this skill)
   → Build campaign structure with the keywords from Step 2 + unit economics from Step 1

Step 5: (after 14+ days) $ozon-ppc-campaign Mode B
   → Optimize based on real search term reports + ДРР performance
```

**Always check listing quality before spending on ads.** A poorly-optimized listing will burn ad budget without converting.

## References

- `references/ozon_ppc_campaign_types.md` — Поиск / Категория / Трафареты / Карточка товара — 详细规则与差异
- `references/ozon_ppc_bid_strategy.md` — Bid strategies + ДРР 公式 + 各类目 CPC 默认值

## Limitations

This skill uses publicly available data, user-provided campaign reports, and category-level CPC defaults. It cannot:
- Access Ozon seller panel directly
- Pull real-time auction data or live CPC bids
- Automate bid changes via Ozon Performance API

For deeper analytics with automated bid management and live auction data, integrate with MPStats, Moneyplace, or SellerExpert — the leading Russian-marketplace analytics platforms.
