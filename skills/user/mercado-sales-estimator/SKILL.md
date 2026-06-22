---
name: mercado-sales-estimator
description: "Mercado Libre sales volume estimator using search rank position, category best-seller rank, listing health score (MercadoLider bronze/silver/gold), and seasonal multipliers. Estimates monthly units and revenue across MLM MXN, MLB BRL, MLC CLP, MCO COP, MLA ARS, MPE PEN. Models Hot Sale May MX, Buen Fin Nov MX, Black Friday BR, Dia de las Madres 5月, Navidad December, Carnaval February spike. Use when user asks about 美客多销量预估, 美客多一个月能卖多少, Mercado Libre sales estimate, 美客多日出单, estimar ventas Mercado Libre, estimar vendas Mercado Livre, faturamento Mercado Livre, monthly revenue LATAM cross-border, MELI sales forecast."
metadata: {"category":"mercado","emoji":"馃嚰馃嚭"}
---

# Mercado Libre Sales Estimator 馃嚰馃嚭

Estimate monthly units and revenue for a Mercado Libre listing using search rank position, category best-seller rank, MercadoLider badge tier, and LATAM seasonal multipliers.

## When to Use

Activate when the user mentions:
- 美客多销量预估 / 美客多能卖多少 / 美客多日出单 / 美客多一个月出多少
- Mercado Libre sales estimate / estimar ventas / estimar vendas / faturamento
- Hot Sale sales forecast / Buen Fin revenue projection / Black Friday BR sales spike
- MercadoLider badge impact on conversion / bronze silver gold tier
- Cross-border LATAM monthly revenue forecast / 美客多GMV预测
- Sales estimator from category rank / 美客多BSR-like rank

## Capabilities

- **Rank-based estimation**: pull search-page rank and category position; map to expected monthly impressions and CTR
- **Conversion modeling**: 1-4% conversion band by category, MercadoLider badge lifts conversion 15-30%
- **Seasonal multiplier**: Hot Sale May MX 3-5x, Buen Fin Nov MX 2-4x, Black Friday BR 2-3x, Dia de las Madres 2-3x, Navidad 2-4x
- **Multi-site projection**: same SKU forecast for MX / BR / CL / CO / AR / PE simultaneously
- **Listing health scoring**: complete MercadoLider badge trajectory, photos, description, shipping speed impact
- **Currency revenue output**: estimate in BRL MXN CLP COP ARS PEN plus USD-equivalent at current FX
- **Scenario bands**: pessimistic / baseline / optimistic monthly units + revenue
- **New-listing ramp**: model first 30 / 60 / 90 day sales curve for new SKU

## Workflow

1. **Collect signals**: search-page rank, category best-seller position, MercadoLider tier, listing age days
2. **Estimate impressions**: category traffic band x rank position share
3. **Model CTR**: by position (page 1 top vs page 2+); MercadoLider badge boosts CTR
4. **Model conversion**: by category base 1-4%, MercadoLider adds 15-30%
5. **Apply seasonal multiplier**: select month from LATAM event calendar
6. **Multiply by site volume weight**: MX and BR dominate LATAM GMV
7. **Output monthly units**: pessimistic / baseline / optimistic bands
8. **Convert to revenue**: units x list price local currency; add USD-equivalent
9. **Recommend action**: if pessimistic under threshold, suggest price drop, badge push, or category exit

## Output Schema

| Field | Description |
|-------|-------------|
| Site | MLM / MLB / MLC / MCO / MLA / MPE |
| Rank inputs | Search-page rank + category rank |
| MercadoLider tier | None / Bronze / Silver / Gold |
| Monthly impressions | Estimated listing views |
| CTR estimate | Click-through rate band |
| Conversion band | 1-4% category baseline + badge lift |
| Seasonal multiplier | Hot Sale / Buen Fin / Black Friday etc |
| Monthly units | Pessimistic / baseline / optimistic |
| Monthly revenue | Local currency + USD-equivalent |
| Ramp curve | Days 30 / 60 / 90 unit forecast |

## Usage Examples

```
Estimate 美客多 Mexico sales: page 1 rank 8, electronics, MercadoLider Bronce, Hot Sale May
```

```
Mercado Livre Brazil forecast: rank 25 in beleza, full seller, Black Friday week
```

```
美客多墨西哥月销量预估: 搜索第 3 页, 手机配件类目, 无 MercadoLider, Buen Fin 月份
```

```
Estimar ventas Mercado Libre Chile: rank 15, deportes, MercadoLider Plata, Navidad
```

```
New listing 0-30 day ramp curve forecast for SKU on MLM MXN first month
```

## Quick Mode

Inputs: site + category + search rank + list price + MercadoLider tier.
Output: monthly units baseline + monthly revenue local + 1-line seasonal tip.

## Key Thresholds

- Below page 1 rank 48: expect sub-100 monthly impressions; relist or boost
- MercadoLider Bronze conversion lift roughly 15%; Silver 22%; Gold 30%+
- Hot Sale window: lift listing 2-3 weeks prior with PADS budget
- New listing 0-30 days: expect 20-40% of full rank potential; ramp to baseline by day 60
- Below 50 monthly units baseline: consider Full vs Envios cost trade-off
