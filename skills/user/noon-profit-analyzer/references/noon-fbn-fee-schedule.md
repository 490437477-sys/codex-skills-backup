# noon FBN Fee Schedule Reference

Used by: noon-profit-analyzer, noon-shipping-calculator, noon-niche-finder.

Current noon FBN (Fulfilled by Noon) fee schedule. Always confirm against noon Seller Central as fees update periodically. Values below are typical ranges as of 2026.

## Commission (category-based)

| Category | Commission |
|----------|------------|
| Mobiles & tablets | 6-8% |
| Electronics (consumer) | 8-12% |
| Computers & accessories | 8-10% |
| Fashion (apparel) | 12-18% |
| Fashion (footwear) | 12-15% |
| Beauty & perfumes | 12-18% |
| Home & kitchen | 10-15% |
| Toys & games | 10-15% |
| Sports & outdoors | 10-15% |
| Grocery (food) | 8-15% |
| Baby products | 10-15% |
| Books | 12-15% |
| Automotive | 10-15% |
| Health & personal care | 12-18% |

## FBN storage fee (per unit per 30 days)

| Tier | Dimensions (cm) | Weight (kg) | Peak (Sep-Feb) | Off-peak (Mar-Aug) |
|------|-----------------|-------------|----------------|---------------------|
| Small | <= 30 x 30 x 30 | <= 1 | 2.5 SAR | 1.5 SAR |
| Medium | <= 45 x 45 x 45 | <= 5 | 4.5 SAR | 3.0 SAR |
| Large | <= 60 x 60 x 60 | <= 15 | 7.0 SAR | 4.5 SAR |
| Extra-Large | > 60 OR > 15kg | > 15 | 12 SAR | 8.0 SAR |

UAE equivalents are roughly 1 AED = 1 SAR (AED pegged to SAR). Egypt is EGP at separate rates.

### Storage overage surcharges

- **> 180 days**: storage fee x 2
- **> 365 days**: storage fee x 3 + removal order may be auto-issued
- **High-volume sellers**: tiered pricing may apply; check Seller Central

## FBN delivery fee (per order)

| Tier | KSA (SAR) | UAE (AED) | Egypt (EGP) |
|------|-----------|-----------|-------------|
| Small | 7-10 | 7-10 | 25-40 |
| Medium | 12-18 | 12-18 | 45-70 |
| Large | 20-35 | 20-35 | 80-150 |
| Extra-Large | 35-70 | 35-70 | 150-300 |

### Delivery fee add-ons

- **COD handling**: +0.5 to +1.5 SAR/AED/EGP per order
- **Heavy package** (> 30 kg): additional +10-30 SAR
- **Remote area delivery**: +5-15 SAR (KSA rural / UAE remote)
- **Same-day delivery** (where available): +10-25 SAR premium
- **Refrigerated delivery**: 2x delivery fee + special packaging cost

## Removal order fee

| Tier | Fee |
|------|-----|
| Small | 3-5 SAR |
| Medium | 5-10 SAR |
| Large | 10-20 SAR |
| Extra-Large | 20-40 SAR |

If the SKU is sold to a liquidation partner instead, fees may be waived but revenue is ~10-20% of original value.

## Disposal fee

Similar to removal but the inventory is destroyed. Slightly higher fee than return-to-seller (10-25% higher). Use only for unsellable / damaged / expired stock.

## Returns processing fee

- Most categories: returns are free for the buyer; noon charges the seller a handling fee (3-8 SAR per return) if the return is seller-fault (defective, wrong item)
- If return is buyer-remorse (no defect), noon absorbs the cost in most cases
- **Apparel / footwear** has the highest return rate (15-25%); budget accordingly

## Aged inventory surcharge

Storage fees are tiered by age. Plan inventory to clear before aging surcharges kick in.

| Age | Multiplier |
|-----|------------|
| 0-90 days | 1x |
| 91-180 days | 1.5x |
| 181-365 days | 2x |
| > 365 days | 3x + potential removal order |

## Returns reserve recommendation

Set aside returns reserve per category in your margin model:

| Category | Recommended reserve (% of landed cost) |
|----------|----------------------------------------|
| Apparel | 12-18% |
| Footwear | 12-18% |
| Beauty | 5-10% |
| Electronics | 5-8% |
| Home | 5-8% |
| Grocery (sealed) | 2-5% |
| Toys | 5-10% |

## Payment gateway fee

noon processes payments through local gateways. Standard fee: **2.0-2.5% of order value**. COD orders additionally carry COD bounce risk reserve (10-25% of COD-eligible order value, since MENA COD bounce rates are high).

## COD bounce impact

- COD bounce rate by category:
  - Apparel: 15-25%
  - Footwear: 15-20%
  - Beauty: 10-15%
  - Electronics: 8-15%
  - Home: 5-10%
  - Grocery: 5-10%
- Cost per bounce: shipping cost (non-recoverable) + restocking labor
- Recommended reserve: COD% of orders x bounce% x 0.7 x shipping cost

## Worked example (KSA, Apparel, Medium tier, 100 SAR retail)

```
Retail price               100.00 SAR
- noon commission (15%)    -15.00 SAR
- FBN storage (30 days)     -4.50 SAR
- FBN delivery (Medium)    -15.00 SAR
- COD handling              -1.00 SAR
- Payment gateway (2.5%)    -2.50 SAR
- Returns reserve (15%)     -7.50 SAR (on 50 SAR landed)
- COD bounce reserve (10%)  -1.50 SAR
- Promos / coupons          -5.00 SAR
= Net revenue              48.00 SAR
- Landed cost              -30.00 SAR
- Advertising (ACOS 25%)   -25.00 SAR
= Contribution margin      -7.00 SAR
= Contribution margin %    -7.0%
```

This shows the SKU is unprofitable at 100 SAR retail with 25% ACOS. Either reduce landed cost, raise price, lower ACOS, or sunset.

## Use cases in skills

- **noon-profit-analyzer**: full waterfall per SKU
- **noon-shipping-calculator**: per-order shipping cost
- **noon-niche-finder**: reject niches where typical landed cost > 30% of retail
