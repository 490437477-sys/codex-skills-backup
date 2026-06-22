---
name: ozon-shipping-calculator
description: "Ozon shipping cost calculator for FBO and FBS fulfillment, including inbound shipping from China to Russian Ozon warehouses, last-mile delivery costs, returns processing, and cross-border consolidation routes. Includes CIS-specific factors: ruble volatility, EAC certification, Russian customs duty, BRICS trade routes, and RUB/KZT/BYN normalization. Use when the user asks about Ozon shipping cost, Ozon inbound from China, last-mile delivery cost on Ozon, 写芯褋褌邪胁泻邪 shipping to Russia, or CN to Russia freight for Ozon."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Shipping Calculator

Compute every Ozon shipping-related cost across FBO, FBS, and cross-border from China to Russia.

## Capabilities

- **FBO storage fee** by tier and season
- **FBO last-mile fee** by size tier and destination
- **FBS pick-and-pack + shipping label** cost
- **Inbound shipping**: sea freight from Guangzhou / Yiwu / Shenzhen to Russian Ozon warehouses
- **Cross-border routes**: direct to Ozon, or via Kazakhstan / Belarus
- **Customs clearance**: Russian Customs duty + EAC conformity
- **Returns processing fee** for FBO and FBS
- **Currency normalization**: CNY / USD / INR -> RUB
- **Aged inventory surcharge** at Ozon FBO

## Workflow

### 1. Confirm marketplace and SKU dimensions
- Marketplace: Ozon.ru / Ozon.kz / Ozon.by
- SKU dimensions (cm) and weight (kg)
- Tier: Small / Medium / Large / XL

### 2. Compute FBO last-mile
Per-order delivery fee by tier + destination region. Moscow / SPB are cheaper than remote regions like Far East.

### 3. Compute FBS shipping
FBS shipping label: 60-300 RUB per order depending on destination and weight.
FBS pick-and-pack: 30-50 RUB per order.

### 4. Add inbound shipping

### From China (Guangzhou / Yiwu / Shenzhen)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Guangzhou -> Moscow (rail) | Rail via Manzhouli | 18-25 days | $80-150 |
| Yiwu -> Moscow (rail) | Rail | 20-28 days | $90-160 |
| Shenzhen -> St Petersburg (sea) | Sea (LCL) | 35-45 days | $60-100 |
| Guangzhou -> Vladivostok (sea) | Sea (LCL) | 15-20 days | $50-90 |
| Any China -> Russia (air) | Air (urgent) | 4-7 days | $5-8/kg |

### 5. Customs + conformity
- HS code lookup -> duty rate (5-15%)
- EAC conformity certificate: 5000-30000 RUB per SKU
- Russian import VAT (20%): reclaimable if seller is VAT-registered

### 6. Returns reserve
CIS returns run 8-15%. Reserve 10% of landed cost.

### 7. Total cost formula

```
Total landed cost = FOB (CN)
                  + freight (sea / rail / air)
                  + Russian customs duty
                  + EAC certification (amortized)
                  + FBO storage (or FBS pick)
                  + FBO last-mile (or FBS shipping)
                  + Returns reserve
```

## Output

- **Per-order shipping cost** for FBO vs FBS
- **Inbound shipping + customs** per shipment
- **Returns reserve**
- **FBO vs FBS recommendation**

## Quick Mode

If user gives dimensions + weight + monthly orders: return only the per-order cost + recommendation.
