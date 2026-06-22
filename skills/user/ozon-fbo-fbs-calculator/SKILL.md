---
name: ozon-fbo-fbs-calculator
description: "Ozon FBO (Fulfilled by Ozon) and FBS (Fulfilled by Seller) cost calculator. Computes FBO storage and last-mile fees by tier, FBS pick-and-pack and shipping label cost, inbound shipping cost from CN to Ozon warehouses in Russia, returns fees, and FBO vs FBS breakeven analysis. Includes CIS-specific factors: ruble volatility, EAC certification cost, Russian customs duty, cross-border consolidation, and RUB/KZT/BYN normalization. Use when the user asks about Ozon FBO fees, Ozon storage cost, FBS vs FBO breakeven, Ozon inbound shipping, or how much Ozon actually charges per fulfilled order."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon FBO / FBS Cost Calculator

Compute every Ozon fulfillment-related cost across FBO (Fulfilled by Ozon) and FBS (Fulfilled by Seller), with CIS-specific inbound and customs treatment.

## Capabilities

- **FBO storage fee** by tier and season (peak vs off-peak)
- **FBO last-mile fee** by size tier and destination region (Moscow, SPB, regions)
- **FBS pick-and-pack fee** charged to the seller for self-shipped orders
- **FBS shipping label** cost for seller-fulfilled orders
- **Inbound shipping**: ocean freight + last-mile to Ozon warehouses in Khovrino, Tver, St Petersburg
- **Returns processing fee** (FBO and FBS differ)
- **Aged inventory surcharge** (> 180 days)
- **Cross-border duty**: Russian Customs 5-15% depending on HS code + EAC conformity certificate
- **Currency normalization**: cost in CNY / USD / INR -> RUB
- **FBO vs FBS breakeven**: orders/month where FBO becomes cheaper than FBS

## Workflow

### 1. Confirm marketplace and SKU dimensions
- Marketplace: Ozon.ru / Ozon.kz / Ozon.by
- SKU dimensions (cm) and weight (kg)
- Tier: Small / Medium / Large / Extra-Large

### 2. Compute FBO storage
Default 30-day storage window:

| Tier | Peak (Nov-Jan) | Off-peak (Feb-Oct) |
|------|----------------|---------------------|
| Small | 5 RUB/unit | 3 RUB/unit |
| Medium | 12 RUB/unit | 7 RUB/unit |
| Large | 25 RUB/unit | 15 RUB/unit |
| XL | 50 RUB/unit | 30 RUB/unit |

(Adjust per current Ozon fee schedule; user can override.)

### 3. Compute FBO last-mile
Per-order delivery fee by tier + destination region. Moscow / SPB are cheaper than remote regions.

### 4. Add FBS alternatives
FBS pick-and-pack: 30-50 RUB per order (varies by tier)
FBS shipping label: 60-300 RUB per order depending on destination and weight

### 5. Add inbound shipping
CN -> Russia sea freight typically $2-5 per kg (LCL bulk). Air freight $5-10 per kg for urgent restock.

### 6. Customs + conformity
- HS code lookup -> duty rate (5-15%)
- EAC conformity certificate: 5000-30000 RUB per SKU depending on category
- GOST-R test report: 10000-50000 RUB per SKU

### 7. Returns reserve
CIS returns run 8-15%. Reserve 10% of landed cost.

### 8. FBO vs FBS breakeven
FBO works when:
- High order volume (> 100/month/SKU)
- Fast-moving inventory
- Willing to commit to Russian warehouse inventory

FBS works when:
- Low order volume
- Slow-moving or test inventory
- Cross-border direct from CN
- Avoid ruble exposure on warehouse inventory

## Output

- **Per-order fulfillment cost** for FBO vs FBS
- **Monthly storage cost** by season
- **Inbound shipping + customs** per shipment
- **Returns reserve**
- **FBO vs FBS recommendation** + breakeven order volume

## Quick Mode

If user gives dimensions + weight + monthly orders: return only the per-order cost + recommendation.
