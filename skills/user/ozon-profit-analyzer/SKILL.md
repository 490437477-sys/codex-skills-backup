---
name: ozon-profit-analyzer
description: "Comprehensive Ozon profit analysis and revenue optimization. Revenue waterfall analysis with Ozon commission, FBO storage and delivery fees, FBS shipping cost, returns reserve, advertising ACoS impact, currency conversion (USD/CNY to RUB/KZT/BYN), and VAT handling (20% Russia, 12% Kazakhstan, 20% Belarus). Identifies hidden fees and ranks SKUs by true contribution margin. Use when the user asks about Ozon profit, Ozon fees breakdown, FBO economics, RUB margin, advertising ACoS impact on Ozon profit, or which Ozon SKUs are actually profitable."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Profit Analyzer

Uncover the true contribution margin of every Ozon SKU after every CIS-specific fee, FX cost, and ruble volatility risk is layered in.

## Capabilities

- **Full fee waterfall**: commission, FBO storage, FBO delivery, FBS shipping, returns reserve, last-mile
- **Advertising overlay**: ACoS impact on contribution margin per SKU
- **Currency conversion**: USD/EUR/CNY landed cost -> RUB / KZT / BYN retail with realistic ruble volatility buffer
- **Ruble volatility modelling**: RUB moves 10-20% in a year; need 5-10% FX buffer
- **Returns reserve**: returns in CIS run 8-15% (similar to mature markets)
- **VAT handling**: 20% KZ-RU / 12% KZ / 20% BY VAT (collected from buyer, not deducted from seller margin but tracked separately)
- **Promo / coupon cost**: Ozon card discounts and coupon stacking eat margin
- **Per-SKU ranking**: rank portfolio by contribution margin %, not just revenue
- **Hidden fee detection**: FBO storage overage, aged inventory, return processing, removal fees
- **Break-even ACoS**: for each SKU, the ACoS at which contribution margin hits zero

## Workflow

### 1. Gather inputs
- Landed cost per SKU (USD or RMB, including manufacturing + freight + duty)
- Ozon commission rate per category (5-25%)
- Fulfillment model (FBO vs FBS) and tier
- Storage days projected
- AOV in local currency
- Advertising spend per SKU
- Historical return rate per SKU

### 2. Build the waterfall
For each SKU:

```
Retail price (RUB)
- Ozon commission (5-25%)
- FBO storage fee (or FBS pick-and-pack)
- FBO delivery fee (or FBS shipping label)
- Returns reserve (return% x landed cost)
- Promos / Ozon card discount
- Currency buffer (5-10% for RUB volatility)
= Net revenue
- Landed cost
- Advertising spend (ACOS x retail)
= Contribution margin (RUB)
= Contribution margin %
```

### 3. Apply VAT
Track VAT separately as a collected-and-remitted liability. Do NOT deduct from seller margin.

### 4. Compute break-even ACoS
ACOS_max = (retail - all fees - landed cost) / retail

Anything above this and the SKU loses money after ads.

### 5. Rank the portfolio
Sort by contribution margin %, not by revenue. A 500K RUB revenue SKU at 5% margin may be worse than a 100K RUB SKU at 25% margin.

### 6. Flag hidden issues
- FBO storage overage (> 180 days)
- Aged inventory (high storage fees)
- Return rate > 15% (quality issue)
- Ozon card discount > 20% (margin collapse)

## Output

- **Per-SKU waterfall** (one row per SKU)
- **Portfolio ranking** by contribution margin
- **Break-even ACoS** per SKU
- **Top 5 hidden-fee recoveries** (concrete actions)
- **Sunset recommendations**: SKUs to delist

## Quick Mode

If user gives one SKU: return only that SKU waterfall + break-even ACoS.
