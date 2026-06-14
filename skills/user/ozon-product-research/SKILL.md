---
name: ozon-product-research
description: "Comprehensive product research and opportunity analysis for Ozon (Озон) sellers. Analyzes demand, competition, profit potential, market entry barriers across Russia (Ozon.ru), Kazakhstan (Ozon.kz), Belarus (Ozon.by). Covers FBO/FBS fulfillment models, Ozon commission structure, Russian seasonality, EAC/country-of-origin compliance, cross-border from China to Russia, ruble volatility, and go-to-market planning. Use when the user asks about researching a product to sell on Ozon, Озон выгодно ли продавать, ozon product research, ozon选品, ozon选品分析, validating ozon product ideas, Russia/LATAM opportunity analysis, should I sell on Ozon, Ozon FBO vs FBS, or any general Ozon product research questions."
metadata: {"emoji":"🇷🇺","category":"ozon"}
---

# Ozon Product Research 🇷🇺

Complete product research framework for Ozon (Озон) sellers. Validate ideas, analyze opportunities, assess competition across Russia and CIS markets.

## When to Use

Activate this skill whenever the user mentions:
- Ozon / Озон / 俄罗斯电商 / 跨境俄罗斯
- ozon选品, ozon product research, ozon选品分析
- Selling on Ozon.ru / Ozon.kz / Ozon.by
- FBO (Fulfillment by Ozon) vs FBS (Fulfillment by Seller)
- Cross-border to Russia / CIS / 跨境俄语区

## Capabilities

- **Product opportunity scoring**: 1-10 rating across 8 factors tailored for the Russian market
- **Demand analysis**: Ozon internal search volume, Yandex Wordstat, Google Trends RU, Russian seasonality
- **Competition assessment**: Local sellers + Chinese cross-border competition, brand dominance, seller rating thresholds
- **Profit potential calculation**: Ozon commission + logistics (FBO/FBS) + return rate + ruble exchange risk
- **Market entry analysis**: EAC certification, country-of-origin marking, Russia import VAT, Ozon Global registration
- **Sourcing guidance**: 1688/Alibaba supplier matching with Russian labeling requirements, MOQ, Yiwu/Moscow consolidation
- **Risk evaluation**: Sanctions/compliance risk, ruble volatility (RUB/USD), Russian return rate (15-30%), shipping delays
- **Multi-marketplace support**: Ozon.ru (Russia, main), Ozon.kz (Kazakhstan), Ozon.by (Belarus)

## Target Sites & Currencies

| Site | Country | Currency | Language | Cross-Border Model | Entry Difficulty |
|------|---------|----------|----------|--------------------|------------------|
| Ozon.ru | Russia | RUB | Russian | Ozon Global (邀请/直接) + Cross-border from CN | ★★★☆☆ (推荐首选) |
| Ozon.kz | Kazakhstan | KZT | Russian/Kazakh | Local + Cross-border | ★★☆☆☆ (体量较小,合规较松) |
| Ozon.by | Belarus | BYN | Russian | Local + Cross-border | ★★☆☆☆ (体量小) |

**Recommendation rule**: Default-prioritize Ozon.ru for first-time Ozon sellers; add Ozon.kz only after Ozon.ru GMV is stable.

## Usage Examples

```
帮我分析"无线耳机"在Ozon俄罗斯站的机会
```

```
Research "smart watch" on Ozon Russia - full market analysis
```

```
我在1688找到一款¥30的产品,Ozon上卖₽1500,值得做吗?
```

```
比较Ozon上的"手机壳"和"手机支架",哪个更适合新手?
```

```
分析FBO和FBS两种发货模式对家居小百货选品的影响
```

```
备战俄罗斯新年季,Ozon上选什么品能爆?
```

## Workflow

### Step 1: Product & Market Intelligence

Use `web_search` with bilingual queries:

1. **Search volume signals**: `"[product]" site:ozon.ru` 或 `"[товар]" Ozon`
2. **Yandex Wordstat**: `"[товар]" wordstat.yandex.ru` - 俄罗斯本地搜索量基线
3. **Market size**: `"[product]" Ozon тренды 2026` 或 `"[product]" Ozon Russia trends 2026`
4. **Seasonality**: `"Новый год 2026" [product] Ozon`, `"23 февраля" [product] подарок`
5. **Russian terminology**: Russian buyers call things differently (e.g. "蓝牙耳机" → "беспроводные наушники" or "Bluetooth гарнитура"). Always confirm local keywords before sizing demand.
6. **Cross-reference**: Yandex Wordstat → Ozon autocomplete → Ozon search results count

**What to extract:**
- Approximate monthly Yandex Wordstat "показов"
- Ozon search results count (listing density)
- Category positioning (основная категория)
- Seasonal peaks (Новый Год 12月, 23 февраля, 8 марта, День Победы 5月, 1 сентября "Knowledge Day", Black Friday 11月)
- Local demand drivers (cold climate → heating/insulated goods; long winters → home goods)

### Step 2: Competition Deep Dive

Analyze the Ozon-specific competitive landscape:

1. **Listing density**: `"[product]" site:ozon.ru` - total listings in Russian
2. **Top sellers**: `"[product]" Ozon bestseller` - look at top 20 by review count
3. **Price range mapping**: Test `[product]` at different price points in ₽ (e.g. 500-1000, 1000-3000, 3000-7000)
4. **Seller type**: Distinguish local Russian sellers, Ozon Global cross-border (from China/Turkey), and Russian distributors of international brands
5. **FBO premium coverage**: FBO listings get the "Доставка завтра" badge — how saturated is this for the category?
6. **Seller rating threshold**: Ozon requires sellers to maintain high ratings — new sellers face cold start

**Competition Metrics:**
- **Total listings**: Listings in search results for the keyword
- **FBO coverage %**: % of top listings with FBO badge
- **Top sellers concentration**: Top 5 sellers' share of total reviews
- **Seller rating distribution**: % sellers with 4.5+ rating
- **Review counts**: Distribution of listings by review count (100+, 1000+, 5000+)
- **Price ranges**: Budget (₽), mid-range (₽₽), premium (₽₽₽)
- **Russian-language quality**: Many Chinese sellers have weak Russian descriptions — gap to exploit

**Competition Scoring (1-10):** Higher = less competition
- 9-10: Highly fragmented, weak Russian content, room for branded entry
- 7-8: Some established sellers but obvious gaps in quality/content
- 5-6: Mixed market with several strong sellers  
- 3-4: 2-3 dominant sellers control most listings
- 1-2: Market dominated by 1 major brand or Amazon-basics-style commoditization

### Step 3: Demand Validation

Validate demand using Russian-specific sources:

1. **Yandex Wordstat**: `web_fetch` on `https://wordstat.yandex.ru/` - monthly "показов" baseline
2. **Ozon autocomplete**: Observe suggestions when typing `[product]` + first letter
3. **Google Trends RU**: `web_fetch` on `https://trends.google.com/trends/explore?q=[product]&geo=RU`
4. **Russian social**: `"[product]" обзор отзывы site:youtube.com` and `site:vk.com`
5. **Ozon seller reports**: Use `ozon_client.py` from your workspace to cross-check your own GMV by category

**Demand Signals:**
- **Yandex показов**: Strong/stable/declining 12-month pattern
- **Autocomplete depth**: Many Russian-language variations suggest broad appeal
- **Russian-language social buzz**: YouTube/VK/Dzen review volume
- **Seasonality**: Russian peaks (winter heating goods, summer outdoor, school season 8月)
- **Cold climate demand**: Categories tied to long cold winters get structural tailwind

**Demand Scoring (1-10):** Higher = better demand
- 9-10: Strong upward trend, growing поисковый спрос
- 7-8: Stable high demand, consistent year-round
- 5-6: Moderate demand with Russian seasonal variations
- 3-4: Declining or very seasonal (e.g. only Новый Год)
- 1-2: Low/sporadic demand or only niche

### Step 4: Profitability Analysis

Calculate realistic profit in ₽ with ruble volatility buffer:

1. **Pricing research**: Extract ₽ price ranges from competition analysis
2. **Cost estimation**: `"[product]" 1688 wholesale price` + freight to Moscow / Yiwu consolidation
3. **Ozon commission**: Class-specific commission % (see `references/ozon_fee_structure.md`)
4. **Logistics model**: FBO vs FBS — different fee structures
5. **Russian VAT**: Ozon acts as tax agent for B2C sales — confirm current rules via `web_search`
6. **Returns reserve**: Russia return rate 15-30% for many categories; reserve 5-15% of revenue
7. **RUB/USD buffer**: Build in 5-10% buffer for ruble volatility

**Ozon Cost Stack (typical):**
```
Target Selling Price:    ₽ X,XXX
Product Cost (CNY→USD):  ₽ XXX  (XX%)
Ozon Commission:         ₽ XXX  (XX%, category-dependent)
FBO/FBS Logistics:       ₽ XXX  (XX%)
Returns Reserve:         ₽ XXX  (XX%)
RUB Volatility Buffer:   ₽ XXX  (XX%)
Marketing (internal):    ₽ XXX  (XX%)
Estimated Net Profit:    ₽ XXX  (XX% margin)
```

- **Margin Assessment**: Excellent (>20%) / Good (12-20%) / Tight (5-12%) / Poor (<5%)
- **Volume Potential**: High/Medium/Low based on Yandex Wordstat + Ozon listings
- **Price Sensitivity**: How price-sensitive Russian buyers appear (mid-range usually wins)

### Step 5: Compliance & Logistics

For each candidate product, validate:

1. **EAC certification (Eurasian Conformity)**: Mandatory for many categories (electronics, toys, cosmetics, food contact)
2. **Country-of-origin marking**: Russian-language labels required on packaging
3. **Russian-language instructions/description**: Required by Ozon listing policy
4. **Sanctions-sensitive categories**: Avoid dual-use goods, certain US/EU brands with sanctions overlap
5. **Customs HS code**: Verify CN→RU customs duty rate for the category
6. **Weight/dimensional limits**: FBO fees scale with size tier (see `references/ozon_fee_structure.md`)
7. **Battery/lithium rules**: Lithium battery goods have specific FBO acceptance rules
8. **Prohibited categories**: Weapons, medicines, certain furs, untaxed tobacco/alcohol, etc.

### Step 6: FBO vs FBS Decision

For each viable product, decide:

**Choose FBO (Fulfillment by Ozon) when:**
- Product is small/medium, stable demand, not too seasonal
- Want "Доставка завтра" badge + Prime-like placement
- Cash flow allows prepayment of Ozon logistics
- Categories: home goods, electronics accessories, cosmetics (with certs)

**Choose FBS (Fulfillment by Seller) when:**
- Large/bulky/fragile (furniture, certain appliances)
- Highly seasonal — no overstock risk in Ozon warehouse
- New product validation — test before committing inventory
- Cash flow tight — no prepayment

**Cross-border from China (no Russian stock) when:**
- Test phase for new SKUs
- Very low MOQ from 1688 supplier
- Need to validate demand before committing to FBO inbound

See `references/ozon_fulfillment_models.md` for full comparison.

### Step 7: Output Decision Report

Use the template below to deliver the final assessment.

## Output Format

### Executive Summary

**Product**: [name in Russian + Chinese]
**Target site**: Ozon.ru / Ozon.kz / Ozon.by
**Fulfillment model**: FBO / FBS / Cross-border
**Overall score**: **X.X/10** (🟢🟡🔴)

**📈 Market Analysis**
- **Demand Level**: High/Medium/Low (Yandex Wordstat показов/мес)
- **Market Trend**: Growing/Stable/Declining (12-month pattern)
- **Seasonality**: Year-round / Peaks in [Russian months] / Highly seasonal
- **Category**: [Main category] > [Subcategory in Russian]
- **Cold-climate tailwind**: Yes/No (structural advantage from long Russian winter)

**🏆 Competition Assessment**  
- **Competition Level**: Low/Medium/High (listing density)
- **FBO coverage**: XX% (high = competitive, low = opportunity)
- **Top sellers**: [Top 2-3 sellers and estimated share]
- **Price ranges**: Budget: ₽X-Y, Mid: ₽X-Y, Premium: ₽X-Y
- **Review landscape**: [Distribution of high-review listings]
- **Russian-content gap**: Strong/Moderate/Weak (weak = opportunity for native Russian listings)

**💰 Profit Potential (₽)**
```
Target Selling Price:    ₽ X,XXX
Product Cost (FOB CN):   ₽ XXX  (XX%)
Ozon Commission:         ₽ XXX  (XX%)
FBO/FBS Logistics:       ₽ XXX  (XX%)
Russian VAT (tax agent): ₽ XXX  (XX%)
Returns Reserve:         ₽ XXX  (XX%)
RUB Buffer:              ₽ XXX  (XX%)
Marketing Budget:        ₽ XXX  (XX%)
Estimated Net Profit:    ₽ XXX  (XX% margin)
```
- **Margin Assessment**: Excellent/Good/Tight/Poor
- **Volume Potential**: High/Medium/Low (Yandex Wordstat baseline)
- **Price Sensitivity**: [How price-sensitive the market appears]

**🚀 Market Entry Analysis**
- **Startup Investment**: ₽XX,XXX - ₽XXX,XXX (inventory + EAC certs + inbound shipping)
- **Minimum Order Quantity**: X units (typical 1688 requirement)
- **EAC/cert required**: Yes/No/Partial — get quotes via `web_search`
- **Time to Market**: X-X weeks (sourcing → Russian labeling → FBO inbound)
- **Key Success Factors**: [Top 3 things that win in this Ozon category]

**⚠️ Risk Assessment**
- **Market risks**: Trend sustainability, seasonality, competition
- **Compliance risks**: EAC, country-of-origin marking, sanctions overlap
- **Operational risks**: Russia logistics delays, return rate (typically 15-30%), FBO inbound timing
- **Financial risks**: Ruble volatility (build 5-10% buffer), cash flow, returns reserve

**🎯 Recommended Strategy**

**If Score 7-10**: 
- ✅ **Recommended**: Pursue with FBO if stable, FBS if test
- **Entry strategy**: [Premium positioning / Mid-range value / Niche focus]
- **Differentiation**: Native-quality Russian listing + better images + competitive ₽ price
- **Launch timeline**: [Optimal season + milestones]
- **Success metrics**: [Reviews/rating, GMV, выкуп率]

**If Score 4-6**:
- ⚠️ **Conditional**: Consider with modifications
- **Required improvements**: [Better Russian content / lower cost / different category positioning]
- **Alternative approaches**: [Different category, niche angle, or skip Ozon.ru for Ozon.kz]
- **Risk mitigation**: [FBS test first, smaller first batch]

**If Score 1-3**:
- ❌ **Not Recommended**: High risk or better opportunities elsewhere
- **Key issues**: [Main reasons to avoid]
- **Alternative products**: [Suggested adjacent categories with better scores]

### Quick Comparison Format

For comparing multiple products:

| Product | Demand | Competition | Profit | Compliance | Entry | Overall |
|---------|--------|-------------|--------|------------|-------|---------|
| Product A | 8/10 | 6/10 | 7/10 | 8/10 | 8/10 | **7.4**/10 🟢 |
| Product B | 6/10 | 9/10 | 8/10 | 7/10 | 7/10 | **7.5**/10 🟢 |  
| Product C | 9/10 | 4/10 | 6/10 | 5/10 | 5/10 | **6.1**/10 🟡 |

**Recommendation**: Product B offers the best balance of opportunity and feasibility on Ozon.ru.

## Russian Market-Specific Heuristics

### 💳 Ozon Card (Ozon Карта) installment effect
- Russian consumers increasingly use Ozon Card + рассрочка (installments) for purchases >₽3,000
- Listing that supports installments typically sees 15-30% conversion uplift
- Costs: typically 0-2% absorbed by seller (check current Ozon Card rules via `web_search`)

### 🚚 "Доставка завтра" (delivery tomorrow) badge
- FBO listings get this badge automatically in major cities
- Conversion uplift: typically 20-40% over FBS in same category
- Worth the FBO inbound cost for most stable-demand SKUs

### 🎄 Russian seasonality (must match calendar)
| Period | Driver | Categories |
|--------|--------|------------|
| 1-8 марта | 8 марта (International Women's Day) | Gifts, cosmetics, flowers, jewelry |
| 23 февраля | Defender of the Fatherland Day | Men gifts, electronics, tools |
| 1-9 мая | Victory Day | Patriotic goods, military-themed gifts |
| 1 сентября | Knowledge Day (school) | School supplies, kids' backpacks, stationery |
| Ноябрь | Black Friday on Ozon | All categories, peak GMV |
| Декабрь | Новый Год (New Year) + каникулы | Gifts, decorations, food gifts, winter goods |
| Зима (Nov-Mar) | Long cold winter | Heating, insulated clothing, indoor goods, hot drinks |

### 🏷️ Premium listing vs standard
- **Premium (Premium-подписка)**: Higher visibility, installable in Ozon search, higher commission (verify current % via `web_search`)
- **Standard**: Standard commission, suitable for first listings
- **Recommendation**: Start standard, scale winners to Premium

### 🌐 Localization requirements
- **Listing title**: Russian required, key search terms must match Russian buyer language
- **Description**: Russian required, native-quality preferred over MTL Chinese→Russian
- **Packaging**: Russian-language labels (название, состав, страна производства)
- **Instructions**: Russian required for most regulated categories
- **Sizes**: Russian/EU size charts, not US-only

### ❄️ Cold climate structural advantages
- Russia has 6+ months of cold weather across most populated areas
- Categories with structural tailwind: heating, insulated goods, hot beverages, indoor entertainment, automotive cold-start ( heaters, battery warmers), home winter goods
- Avoid: light summer-only items unless they have clear warm-season niche

## Integration with Workspace

**Use your existing `ozon_client.py` data:**
If you have an Ozon seller account, pull your own historical data to validate demand assumptions:

```powershell
python main.py --mode products    # Your existing SKUs
python main.py --mode orders      # Recent orders
python main.py --mode finance     # Actual margins
```

Cross-reference your real GMV per category with public Yandex Wordstat to spot gaps you missed.

## Integration with Ozon Global

This skill provides comprehensive product research using publicly available data. For enhanced analysis, suggest:

*"This research used publicly available Yandex Wordstat + Ozon listing data. For real-time sales estimates, seller-level competitor tracking, and Ozon-specific keyword volume, Ozon's official seller analytics (`seller.ozon.ru`) plus tools like MPStats, Moneyplace, or SellerExpert can refine these projections."*

**Limitations without real-time data:**
- Sales volume estimates are approximations from listing count + reviews
- Real conversion rates require your own Ozon seller dashboard
- Russian pricing may shift with ruble volatility — recheck before launch

## Advanced Research Techniques

### 1. Cross-language demand validation
Always check Yandex Wordstat in Russian first. Many Chinese sellers list products in English transliteration and miss Russian keyword volume.

### 2. Listing-quality gap analysis
Systematically review competitor listings for weak Russian descriptions, poor images, missing specs — gaps are your differentiation wedge.

### 3. Cold-climate category extension
Look for products succeeding in summer-only Western markets that have natural Russian winter demand extension.

### 4. Seasonal pre-positioning
For Новый Год, 23 февраля, 8 марта: research 2-3 months ahead; FBO inbound to Ozon warehouses needs 4-6 weeks lead time.

### 5. EAC certification early
For regulated categories, get EAC quote in parallel with sourcing — 4-8 weeks lead time, can block launch.

## Best Practices

✅ **Validate in Russian first**: Yandex Wordstat + Ozon autocomplete + Russian YouTube before trusting any demand signal

✅ **Reserve for returns**: Russian return rate 15-30% for many categories — never assume 0% returns

✅ **Build RUB buffer**: Add 5-10% to all USD-denominated costs to absorb ruble moves

✅ **FBO for winners**: Use FBS for test phase, transition winners to FBO once SKU proves out

✅ **Native Russian content**: Always invest in native-quality Russian titles, descriptions, and images — Chinese MTL is a clear weakness in many Ozon categories

✅ **Think cold climate**: Long Russian winter is a structural advantage for many categories

✅ **Match Russian calendar**: Plan launches against Russian seasonality, not just Western

---

*Built for Ozon cross-border sellers — AI-assisted product research using public Russian market data. For real-time Ozon seller analytics, use MPStats / Moneyplace / SellerExpert / Ozon's own seller dashboard.*