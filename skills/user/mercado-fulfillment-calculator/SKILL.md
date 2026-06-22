---
name: mercado-fulfillment-calculator
description: "Mercado Libre fulfillment cost calculator comparing Mercado Full vs Mercado Envios vs Mercado Envios Flex vs cross-border self-shipping. Computes pick-pack fee, storage fee by size tier, inbound freight to Full warehouse, returns handling, dimensional weight surcharge, slow-mover penalty (60+ days), Cold Storage surcharge in MX/BR. Use when user asks about 美客多物流费用, 美客多仓储备货, Full vs Envios, 跨境拉美物流, Mercado Full warehouse, Mercado Envios Flex same-day, fulfillment fee Mercado Libre, costo de fulfillment Mercado Libre, custo fulfillment Mercado Livre, tarifa Full armazem, 美客多发货方式对比."
metadata: {"category":"mercado","emoji":"馃嚰馃嚭"}
---

# Mercado Libre Fulfillment Calculator 馃嚰馃嚭

Compare every Mercado Libre fulfillment path side-by-side: Mercado Full (platform warehouse), Mercado Envios (carrier network), Mercado Envios Flex (seller self-delivery same-city), and cross-border self-shipping from China.

## When to Use

Activate when the user mentions:
- 美客多物流费用 / Mercado Libre fulfillment cost / 美客多发货方式
- Mercado Full vs Mercado Envios vs Flex / Full vs Envios comparison
- Full warehouse fee / 仓储备货 cost / costo almacenaje / custo armazenagem
- Flex same-day delivery / 美客多同城配送 costo Flex
- Cross-border self-shipping from China / 跨境拉美物流
- Slow-mover penalty / Cold Storage / storage surcharge Mercado Libre

## Capabilities

- **Full cost breakdown**: monthly storage by size tier (XS/S/M/L/XL), pick-and-pack fee per order, returns handling
- **Envios standard cost**: dimensional weight by zone, package size tier, free-shipping subsidy policy
- **Flex cost model**: per-km rate, 1-2 hour SLA, same-city coverage, motorcycle vs bicycle rider cost
- **Self-shipping cross-border**: air-freight CN to LATAM, last-mile carrier quote, customs clearance fee
- **Slow-mover penalty**: detect 60+ day inventory, project penalty fee, suggest liquidation
- **Cold Storage surcharge**: MX/BR temperature-controlled categories surcharge
- **Returns reverse logistics**: defective vs customer-remorse cost split, return shipping refund
- **Multi-site comparison**: run the same SKU through MX / BR / CL / CO fulfillment stack

## Workflow

1. **Pick site**: MLM / MLB / MLC / MCO / MLA / MPE
2. **Collect SKU facts**: weight kg, dimensions cm, declared value, category, fragility flag
3. **Classify size tier**: match to Full storage grid (XS under 150g, S/M/L/XL by volume)
4. **Quote each path**: compute Full pick-pack + storage; Envios by zone + weight; Flex per-km; self-ship air-freight
5. **Layer storage time**: estimate days-in-warehouse from rotation; add 60+ day penalty if applicable
6. **Add returns reserve**: category returns rate 6-15% times reverse logistics cost
7. **Compare total cost per order**: rank paths; pick cheapest at given SLA tier
8. **Output**: cheapest path + total fulfillment cost per order + storage projection + penalty alerts

## Output Schema

| Field | Description |
|-------|-------------|
| Site | MLM / MLB / MLC / MCO / MLA / MPE |
| Size tier | XS / S / M / L / XL / XXL |
| Full pick-pack | Per order pick-pack fee local currency |
| Full storage | Monthly storage fee by tier |
| Envios quote | Carrier rate by zone and weight |
| Flex quote | Per-km rate + base fee |
| Self-ship | Air-freight + last-mile estimate |
| Returns reserve | Category % times reverse cost |
| Cheapest path | Recommended fulfillment mode |
| Penalty alerts | 60+ day storage / Cold Storage flags |

## Usage Examples

```
Compare Full vs Envios vs Flex for 美客多 Mexico: 1.2 kg, 30x20x10 cm, home decor, 200 units/mo
```

```
Mercado Livre Full armazenagem cost: 0.5 kg, eletronicos, 90 days storage, penalty risk?
```

```
美客多 Full 仓 vs 自发货对比: 0.8 公斤 25x15x8 厘米 美妆类目
```

```
Costo fulfillment Mercado Libre Argentina: 2 kg, electrodomesticos, Flex viable en CABA?
```

```
Detect 60+ day slow movers in my Mercado Full MX inventory and suggest liquidation
```

## Quick Mode

Inputs: site + weight + dimensions + category + expected monthly units.
Output: cheapest fulfillment path + per-order cost + 1-line penalty warning.

## Key Thresholds

- Storage beyond 60 days: penalty zone starts, drain inventory or pull
- Cold Storage SKU in MX/BR without cold plan: 2x surcharge, switch site or category
- Flex below 5 km from buyer: usually cheapest SLA tier
- Cross-border self-ship below 1 kg: ocean + last-mile often cheaper than air
- Full only worth it when monthly sell-through above 30 units per SKU
