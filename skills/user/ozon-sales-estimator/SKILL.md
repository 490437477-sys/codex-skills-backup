---
name: ozon-sales-estimator
description: "Ozon sales volume estimator for sellers and product researchers. Estimate monthly sales and revenue for a SKU on Ozon.ru, Ozon.kz, or Ozon.by from sales rank, category-level demand signals, review velocity, and Yandex Wordstat volume. Three modes: (A) rank-based calculator, (B) SKU lookup, (C) Russian keyword demand estimator. Accounts for Russian-specific factors: FBO vs FBS mix, ruble volatility, New Year / 3.8 / 5.9 / 9.1 spikes, COD vs online payment, and RUB pricing. Use when the user asks about Ozon sales estimate, Ozon revenue forecast, how many units a SKU sells on Ozon, 袨蟹芯薪 锌褉芯写邪卸懈, or whether Ozon demand justifies a launch."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Sales Estimator

Estimate monthly unit sales and revenue for any Ozon SKU or category using Ozon-specific signals.

## Capabilities

- **Rank-based inference**: Ozon exposes category sales rank. Use it with category-specific calibration curves
- **Review velocity as proxy**: 1 review per ~12-20 sales in Russia (Russians review more often than mature markets but less than noon)
- **Category-level demand**: top-of-category SKUs in a 100,000-SKU category sell 1500-3000 units/month on Ozon.ru
- **Russian keyword volume**: Yandex Wordstat for RU seed -> rough demand index (Yandex Wordstat shows monthly searches, not weekly)
- **Marketplace split**: Ozon.ru is > 90% of cross-market GMV; KZ and BY are smaller
- **Seasonality overlay**: New Year / 3.8 Womens Day / 5.9 Victory Day / 9.1 Knowledge Day / Black Friday
- **Currency normalization**: RUB / KZT / BYN to USD
- **Three estimation modes**: rank-based, SKU-lookup, keyword-demand

## Workflow

### Mode A: Rank-based calculator

User inputs: category on Ozon + estimated rank position (1-1000).

```
For each category, calibrate from public Ozon bestseller lists:

Rank 1-10 in category   -> 5000-10000 units/month (Ozon.ru)
Rank 11-50              -> 1500-5000 units/month
Rank 51-200             -> 300-1500 units/month
Rank 201-500            -> 80-300 units/month
Rank 501-1000           -> 15-80 units/month
```

Multiply by marketplace split and apply seasonality multiplier.

### Mode B: SKU lookup

User inputs: Ozon SKU URL or competitor name.

1. Fetch current review count + listing age
2. Estimate monthly sales from review velocity:
   - If 600 reviews over 24 months: ~25 reviews/month -> ~300-500 sales/month
3. Apply COD bounce adjustment (-10% to -15%)
4. Multiply by AOV for revenue estimate

### Mode C: Russian keyword demand

User inputs: seed keyword in Russian.

1. Pull Yandex Wordstat (filter to RU region, last 12 months)
2. Pull Ozon autocomplete suggestions (count and breadth)
3. Estimate daily searches x CTR x CVR x marketplace share
4. Result: monthly demand pool for SKUs targeting this keyword

### Seasonality adjustments

| Period | Multiplier |
|--------|------------|
| New Year (Dec 25 - Jan 8) | 3.0x - 5.0x (gifts, electronics, home) |
| 3.8 Womens Day (2 weeks before) | 2.0x - 3.0x (flowers, jewelry, cosmetics) |
| 5.9 Victory Day | 1.2x - 1.5x (patriotic, gifts) |
| 9.1 Knowledge Day (2 weeks before) | 1.5x - 2.0x (school, kids, electronics) |
| 11.11 Singles Day | 1.5x - 2.0x |
| Black Friday (late Nov) | 2.5x - 4.0x |
| Other months | 1.0x baseline |

## Output

- **Monthly unit estimate** (low / mid / high range)
- **Monthly revenue estimate** in RUB / KZT / BYN + USD equivalent
- **Confidence interval** (low / medium / high based on input quality)
- **Seasonality curve** showing 12-month projection

## Quick Mode

If user gives just a category: return a midpoint estimate with a wide range. If user gives a specific SKU URL: return Mode B output only.
