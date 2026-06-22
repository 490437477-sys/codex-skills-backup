---
name: noon-sales-estimator
description: "noon sales volume estimator for sellers and product researchers. Estimate monthly sales and revenue for a SKU on noon.sa, noon.ae, or noon.com from BSR-equivalent (noon best-seller rank), category-level demand signals, review velocity, and Arabic search volume. Three modes: (A) BSR-style rank calculator, (B) ASIN-style SKU lookup, (C) Arabic keyword demand estimator. Accounts for MENA-specific factors: COD mix, Ramadan / White Friday spikes, three-marketplace split, and SAR/AED/EGP pricing. Use when the user asks about noon sales estimate, noon revenue forecast, how many units a SKU sells on noon, BSR-equivalent on noon, or whether noon demand justifies a launch."
metadata: {"category":"noon","locale":"mena"}
---

# noon Sales Estimator

Estimate monthly unit sales and revenue for any noon SKU or category using noon-specific signals (no public BSR, so we infer).

## Capabilities

- **BSR-equivalent inference**: noon does not expose a public BSR. Estimate from review count, review velocity, ranking in search, and category placement
- **Review velocity as proxy**: 1 review per ~10-15 sales is a reasonable MENA benchmark (vs ~15-25 in mature markets because MENA buyers review more often)
- **Category-level demand**: top-of-category SKUs in a 50,000-SKU category sell 800-1500 units/month on noon.sa
- **Arabic keyword volume**: Google Trends for AR + EN seed → rough demand index
- **Marketplace split**: noon.sa typically 65-75% of cross-market GMV; UAE 20-25%; Egypt 5-10%
- **Seasonality overlay**: Ramadan / Eid / White Friday / back-to-school spikes
- **COD vs prepaid**: COD SKUs may show higher sales counts but lower realized revenue (bounce)
- **Currency normalization**: SAR / AED / EGP to USD
- **Three estimation modes**: rank-based, SKU-lookup, keyword-demand

## Workflow

### Mode A: BSR-equivalent rank calculator

User inputs: category on noon + estimated rank position (1-1000).

```
For each category, calibrate from public noon bestseller lists:

Rank 1-10 in category   → 3000-6000 units/month (noon.sa)
Rank 11-50              → 800-3000 units/month
Rank 51-200             → 200-800 units/month
Rank 201-500            → 50-200 units/month
Rank 501-1000           → 10-50 units/month
```

Multiply by marketplace split and apply seasonality multiplier.

### Mode B: SKU lookup

User inputs: noon SKU URL or competitor name.

1. Fetch current review count + listing age (when possible)
2. Estimate monthly sales from review velocity:
   - If 500 reviews over 18 months: ~28 reviews/month ≈ 280-420 sales/month
3. Apply COD bounce adjustment (-15% to -20%)
4. Multiply by AOV for revenue estimate

### Mode C: Arabic keyword demand

User inputs: seed keyword in Arabic or English.

1. Pull Google Trends (geo: SA, AE, EG, last 12 months)
2. Pull noon autocomplete suggestions (count and breadth)
3. Estimate daily searches × CTR × CVR × marketplace share
4. Result: monthly demand pool for SKUs targeting this keyword

### Seasonality adjustments

| Period | Multiplier |
|--------|------------|
| Ramadan (30 days) | 2.0x - 4.0x (food, gifting) / 1.5x (general) |
| White Friday week | 3.0x - 5.0x |
| Eid al-Fitr | 1.5x - 2.0x |
| Back-to-school | 1.3x - 1.8x |
| National Day KSA | 1.2x - 1.5x |
| Other months | 1.0x baseline |

## Output

- **Monthly unit estimate** (low / mid / high range)
- **Monthly revenue estimate** in SAR / AED / EGP + USD equivalent
- **Confidence interval** (low / medium / high based on input quality)
- **Seasonality curve** showing 12-month projection

## Quick Mode

If user gives just a category: return a midpoint estimate with a wide range. If user gives a specific SKU URL: return Mode B output only.
