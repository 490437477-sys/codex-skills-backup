---
name: noon-shipping-calculator
description: "noon FBN (Fulfilled by Noon) and FBM shipping cost calculator. Computes storage fees by tier (Small / Medium / Large / XL) and season (peak vs off-peak), delivery fees by size tier and destination country, inbound shipping cost from CN/IN/TR to noon warehouses in KSA/UAE/EG, removal and disposal fees, and FBN vs FBM breakeven analysis. Includes MENA-specific factors: cross-border consolidation, Saudi Customs duty, GCC conformity surcharges, and SAR/AED/EGP normalization. Use when the user asks about noon FBN fees, noon storage cost, FBM vs FBN breakeven on noon, noon inbound shipping, SAR shipping cost, or how much noon actually charges per fulfilled order."
metadata: {"category":"noon","locale":"mena"}
---

# noon Shipping Calculator

Compute every noon shipping-related cost across FBN (Fulfilled by Noon) and FBM (Fulfilled By Merchant), with MENA-specific inbound and customs treatment.

## Capabilities

- **FBN storage fee** by tier (Small / Medium / Large / Extra-Large) and season (peak Sep-Feb vs off-peak Mar-Aug)
- **FBN delivery fee** by size tier and destination country (KSA, UAE, EG, KW, BH, OM)
- **FBM delivery fee** charged to the seller for self-shipped orders
- **Inbound shipping**: ocean freight + last-mile to noon warehouses in Riyadh / Jeddah / Dubai / Cairo
- **Removal order fee** (FBN stock removal)
- **Disposal fee** (FBN stock disposal / liquidation)
- **Aged inventory surcharge** (> 180 days: 2x storage; > 365 days: removal ordered)
- **Cross-border duty**: Saudi Customs 5-15% depending on HS code + GCC conformity certificate
- **Currency normalization**: cost in CNY / USD / INR → SAR / AED / EGP
- **FBN vs FBM breakeven**: orders/month where FBN becomes cheaper than FBM

## Workflow

### 1. Confirm marketplace and SKU dimensions
- Marketplace: noon.sa / noon.ae / noon.com
- SKU dimensions (cm) and weight (kg)
- Tier: Small (≤ 30x30x30, ≤ 1kg) / Medium (≤ 45x45x45, ≤ 5kg) / Large (≤ 60x60x60, ≤ 15kg) / Extra-Large (> that)

### 2. Compute FBN storage
Default 30-day storage window:

| Tier | Peak (Sep-Feb) | Off-peak (Mar-Aug) |
|------|----------------|---------------------|
| Small | 2.5 SAR/unit | 1.5 SAR/unit |
| Medium | 4.5 SAR/unit | 3.0 SAR/unit |
| Large | 7.0 SAR/unit | 4.5 SAR/unit |
| XL | 12 SAR/unit | 8.0 SAR/unit |

(Adjust per current noon fee schedule; user can override.)

### 3. Compute FBN delivery
Per-order delivery fee by tier + destination country. Add 0.5-1.5 SAR for COD handling.

### 4. Add inbound shipping
CN → SA/AE sea freight typically 8-15 SAR/unit for Small tier (bulk, FCL/LCL). Air freight 25-50 SAR/unit for urgent restock.

### 5. Customs + conformity
- HS code lookup → duty rate (5-15%)
- GCC conformity certificate: 300-1500 SAR per SKU depending on category
- SASO test report: 1000-5000 SAR per SKU
- SFDA notification: 2000-8000 SAR per SKU

### 6. Returns reserve
MENA returns run 8-15%. Reserve 10% of landed cost.

### 7. FBN vs FBM breakeven
FBM costs:
- Pickup fee: 5-15 SAR per order
- Packaging: 2-5 SAR
- Self-warehouse storage: 0
- Self-shipment courier: 15-40 SAR per order

FBN becomes cheaper when monthly orders exceed the breakeven point (typically 30-80 orders/month/SKU depending on tier).

## Output

- **Per-order shipping cost** for FBN vs FBM
- **Monthly storage cost** by season
- **Inbound shipping + customs** per shipment
- **Returns reserve**
- **FBN vs FBM recommendation** + breakeven order volume

## Quick Mode

If user gives dimensions + weight + monthly orders: return only the per-order cost + recommendation.
