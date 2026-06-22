# Ozon Russian & CIS Seasonal Calendar

Used by: ozon-niche-finder, ozon-advertising-strategy, ozon-sales-estimator, ozon-profit-analyzer.

Annual retail peaks on the Ozon marketplace. Plan inventory, ad budget, and category selection around these dates. All dates are Gregorian; Ozon.ru is the dominant market.

## Major retail peaks (annual)

| Event | Approx date | Demand lift | Top categories |
|-------|-------------|-------------|----------------|
| New Year / Orthodox Christmas | Dec 25 - Jan 8 | 3.0x - 5.0x | Electronics, home, gifts, fashion, toys |
| Defender of the Fatherland Day | Feb 23 | 1.5x - 2.0x | Mens gifts, gadgets, tools, car accessories |
| Womens Day 8 March | Mar 8 | 2.5x - 4.0x | Flowers, jewelry, cosmetics, gifts |
| Spring / May holidays | May 1-9 | 1.3x - 1.7x | Garden, outdoors, picnic, gifts |
| Victory Day | May 9 | 1.2x - 1.5x | Patriotic, gifts, military-themed |
| Russia Day | Jun 12 | 1.1x - 1.3x | Patriotic, leisure |
| Knowledge Day (school start) | Sep 1 | 1.5x - 2.5x | School, kids, electronics, stationery |
| Unified Russia Day | Nov 4 | 1.1x - 1.3x | Patriotic |
| Black Friday Ozon | last week Nov | 3.0x - 5.0x | Everything (Ozon flagship event) |
| Singles Day 11.11 | Nov 11 | 1.5x - 2.0x | Electronics, fashion, beauty |
| New Year prep | mid Nov - Dec 25 | ramping | All categories |

## Orthodox / post-Soviet calendar context

- Orthodox Christmas: Jan 7 (bigger than Dec 25 in Russia)
- Maslenitsa (pancake week): late Feb - early Mar (food, kitchen)
- Easter (Orthodox): Apr / May (varies; food, gifts)
- Trinity Sunday: late May / early Jun (decor, flowers)
- Ivan Kupala: Jul 7 (decor, gifts, summer)

## Seasonality adjustments for sales forecasting

| Period | Demand multiplier |
|--------|-------------------|
| Pre-New Year (mid Nov - Dec 24) | 1.5x - 2.5x ramping |
| New Year (Dec 25 - Jan 8) | 3.0x - 5.0x |
| Post-New Year (Jan 9 - Feb 14) | 0.7x - 0.9x (slow) |
| Pre-23 Feb (Feb 1-22) | 1.3x - 1.7x ramping |
| Pre-8 March (Feb 25 - Mar 7) | 2.0x - 3.0x ramping |
| 8 March week | 2.5x - 4.0x |
| Post-8 March (Mar 9 - May 1) | 0.9x - 1.0x |
| May holidays (May 1-9) | 1.3x - 1.7x |
| Summer (Jun-Aug) | 0.9x - 1.0x (vacation season, slow) |
| Pre-1 September (Aug 1-31) | 1.5x - 2.0x ramping |
| Knowledge Day week | 1.5x - 2.5x |
| Pre-Black Friday (mid Nov) | 1.2x - 1.5x |
| Black Friday (last week Nov) | 3.0x - 5.0x |

## Lead-time guidance

- **New Year inventory must land at FBO 60-90 days before Dec 25** (FBO at Russian warehouse needs 30-45 days for customs + freight, then 15-30 days for QA / categorization)
- **8 March inventory: 45-60 days before Mar 8**
- **Knowledge Day (1 Sept) inventory: 30-45 days before Sep 1** (school supplies, kids items)
- **Black Friday inventory: 30-45 days before Black Friday** (last week of Nov)

## Category-specific winners

### New Year
- Electronics: smartphones, tablets, smartwatches, headphones
- Home: small appliances, decor, lighting, kitchen gadgets
- Fashion: winter coats, knitwear, accessories
- Toys: kids, board games, puzzles
- Gifts: jewelry, perfumes, watches

### 8 March (Womens Day)
- Flowers (cut and artificial, dried)
- Jewelry (costume and precious)
- Cosmetics, perfumery
- Sweets, gift baskets
- Kitchen appliances
- Spas / beauty devices

### 23 February (Mens Day)
- Tools, gadgets
- Car accessories
- Fishing / hunting gear
- Shaving accessories
- Watches, wallets
- Beer / alcohol accessories (note Russia alcohol regulations)

### Knowledge Day (1 September)
- Stationery, backpacks
- Laptops, tablets
- School uniforms
- Kids books
- Educational toys
- Kids sports gear

## Currency volatility consideration

RUB moves 10-20% in a year. Forecast in USD/EUR and convert at planning time, not at order time. Add 5-10% FX buffer to margin projections.

## Use cases in skills

- **ozon-niche-finder**: score niche on seasonal lift potential
- **ozon-advertising-strategy**: budget multiplier per peak; bid +30% during 2 weeks before each major event
- **ozon-sales-estimator**: annual sales = baseline x weighted sum of monthly multipliers
- **ozon-profit-analyzer**: storage cost adjustment based on seasonal stock-up cycles
