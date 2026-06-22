---
name: noon-profit-analyzer
description: "Comprehensive noon profit analysis and revenue optimization. Revenue waterfall analysis with noon commission, FBN storage and delivery fees, payment gateway fees, COD bounce cost, advertising ACoS impact, return cost (high in MENA), currency conversion (USD cost to SAR/AED/EGP retail), and VAT handling (15% KSA, 5% UAE, 14% Egypt). Identifies hidden fees and ranks SKUs by true contribution margin. Use when the user asks about noon profit, noon fees breakdown, FBN economics, COD cost impact on noon, SAR/AED/EGP margin, advertising ACoS impact on noon profit, or which noon SKUs are actually profitable."
metadata: {"category":"noon","locale":"mena"}
---

# noon Profit Analyzer

Uncover the true contribution margin of every noon SKU after every MENA-specific fee, FX cost, and COD bounce risk is layered in.

## Capabilities

- **Full fee waterfall**: commission, FBN storage, FBN delivery, payment gateway, COD surcharge, returns reserve, VAT
- **Advertising overlay**: ACOS impact on contribution margin per SKU
- **Currency conversion**: USD/EUR/CNY landed cost → SAR/AED/EGP retail with realistic FX buffer
- **COD bounce modelling**: COD bounce rate in MENA runs 10-25%; cost varies by item value
- **Returns reserve**: returns in MENA run 8-15% (vs 5-8% in mature markets); factor into margin
- **VAT handling**: 15% KSA / 5% UAE / 14% Egypt VAT (VAT is collected from buyer, not deducted from seller margin but must be tracked)
- **Promo / coupon cost**: White Friday and Ramadan promos eat margin; calculate true net
- **Per-SKU ranking**: rank portfolio by contribution margin %, not just revenue
- **Hidden fee detection**: storage overage fees, aged inventory surcharges, FBN removal fees, removal order fees
- **Break-even ACOS**: for each SKU, the ACOS at which contribution margin hits zero

## Workflow

### 1. Gather inputs
- Landed cost per SKU (USD or RMB, including manufacturing + freight + duty)
- noon commission rate per category (5-20%)
- FBN tier (Small / Medium / Large / Extra-Large) and weight
- Storage days projected
- AOV in local currency
- Advertising spend per SKU
- COD mix %
- Historical return rate per SKU

### 2. Build the waterfall
For each SKU:

```
Retail price (SAR)
- noon commission (5-20%)
- FBN storage fee
- FBN delivery fee
- Payment gateway fee (~2.5%)
- COD bounce cost (COD% x bounce% x AOV)
- Returns reserve (return% x landed cost)
- Promos / coupons
= Net revenue
- Landed cost
- Advertising spend (ACOS x retail)
= Contribution margin (SAR)
= Contribution margin %
```

### 3. Apply VAT
Track VAT separately as a collected-and-remitted liability. Do NOT deduct from seller margin.

### 4. Compute break-even ACOS
ACOS_max = (retail - all fees - landed cost) / retail

Anything above this and the SKU loses money after ads.

### 5. Rank the portfolio
Sort by contribution margin %, not by revenue. A 200K SAR revenue SKU at 5% margin may be worse than a 50K SAR SKU at 25% margin.

### 6. Flag hidden issues
- Storage overage (> 180 days → 2x fee)
- Aged inventory (> 365 days → removal fee + storage surcharge)
- Return rate > 15% → quality issue
- COD bounce > 25% → customer acquisition failure

## Output

- **Per-SKU waterfall** (one row per SKU)
- **Portfolio ranking** by contribution margin
- **Break-even ACOS** per SKU
- **Top 5 hidden-fee recoveries** (concrete actions)
- **Sunset recommendations**: SKUs to delist

## Quick Mode

If user gives one SKU: return only that SKU waterfall + break-even ACOS.
