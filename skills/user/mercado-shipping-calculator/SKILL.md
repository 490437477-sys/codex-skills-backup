---
name: mercado-shipping-calculator
description: "Mercado Libre shipping cost calculator covering Mercado Envios standard, Mercado Envios Flex, Mercado Envios Full pick-pack, and cross-border air-freight from China to LATAM. Computes dimensional weight surcharge, regional zone pricing (capital vs interior), free-shipping subsidy thresholds, last-mile carrier rates (Correios, Estafeta, Mercado Envios partner carriers in MX/BR/CL/CO/AR/PE). Use when user asks about 美客多运费计算, 美客多包邮阈值, Mercado Envios cost, Flex shipping rate, 美客多物流多少钱, calcular envio Mercado Libre, calcular frete Mercado Livre, custo envio Mercado Livre, Mercado Envios Flex tarifa, 美客多运费对比."
metadata: {"category":"mercado","emoji":"馃嚰馃嚭"}
---

# Mercado Libre Shipping Calculator 馃嚰馃嚭

Standalone shipping cost calculator for Mercado Libre cross-border sellers. Quote Mercado Envios, Flex, Full, and cross-border air-freight against dimensional weight, regional zone, and free-shipping subsidy rules per LATAM site.

## When to Use

Activate when the user mentions:
- 美客多运费计算 / 美客多运费多少钱 / Mercado Envios cost / 美客多包邮阈值
- Mercado Envios Flex rate / Flex tarifa same-city / 美客多同城配送
- Free shipping subsidy Mercado Libre / envio gratis threshold / frete gratis
- Dimensional weight surcharge Mercado Libre / peso dimensional / peso cubico
- Cross-border air-freight China to LATAM / 跨境拉美头程物流
- Carrier comparison Estafeta Correios Chilexpress Servientrega OCA

## Capabilities

- **Dimensional weight model**: volumetric weight divisor per site, chargeable weight = max actual vs volumetric
- **Zone pricing**: capital vs interior region rate split for MX BR CL CO AR PE
- **Free-shipping threshold**: per-category and per-site minimum list price that unlocks Mercado Envios subsidy
- **Flex per-km pricing**: distance-based rate from seller hub to buyer postal code
- **Cross-border air-freight**: CN to LATAM per-kg rate by airport pair (MEX GIG GRU EZE SCL BOG LIM)
- **Last-mile carrier split**: rate shop across platform partner carriers (Estafeta, Correios, Mercado Envios local partner)
- **Rural surcharge**: detect interior postal codes, apply remote-area surcharge
- **Bulk tier discount**: estimate unit shipping cost at 50 / 200 / 1000 unit monthly volume

## Workflow

1. **Pick site**: MLM MXN / MLB BRL / MLC CLP / MCO COP / MLA ARS / MPE PEN
2. **Collect package facts**: actual weight kg, length cm, width cm, height cm, declared value
3. **Compute chargeable weight**: max of actual weight vs LxWxH / dimensional divisor
4. **Identify buyer zone**: capital metropolitan vs interior region; detect rural surcharge
5. **Apply free-shipping test**: if list price meets site threshold, Mercado Envios subsidy reduces carrier cost
6. **Quote Mercado Envios**: platform carrier rate by zone and weight tier
7. **Quote Flex**: per-km rate if seller hub within Flex radius of buyer
8. **Quote cross-border**: air-freight per-kg + last-mile carrier rate for self-shipped orders
9. **Output**: cheapest per-order shipping cost by mode + bulk tier projection + free-shipping unlock hint

## Output Schema

| Field | Description |
|-------|-------------|
| Site | MLM / MLB / MLC / MCO / MLA / MPE |
| Chargeable weight | Actual vs volumetric, max wins |
| Buyer zone | Capital / interior / rural |
| Envios cost | Platform carrier rate local currency |
| Flex cost | Per-km base + distance |
| Cross-border cost | Air-freight per-kg + last-mile |
| Free-ship unlock | Threshold price + subsidy amount |
| Bulk projection | Cost at 50 / 200 / 1000 units / month |
| Cheapest mode | Recommended for this buyer zone |

## Usage Examples

```
Calculate 美客多 Mexico shipping: 1.5 kg, 30x20x15 cm, buyer in Guadalajara, list price 499 MXN
```

```
Mercado Envios Brasil custo: 0.8 kg, interior Sao Paulo, frete gratis threshold reached?
```

```
美客多墨西哥运费: 2 公斤, 买家在蒙特雷, 包邮阈值要多少才能解锁
```

```
Calcular envio Mercado Libre Chile: 1 kg, Santiago metro vs interior Temuco, comparar tarifas
```

```
Air-freight CN to MEX GIG: 200 kg consolidated, compare per-kg rate to last-mile Mercado Envios
```

## Quick Mode

Inputs: site + weight kg + dimensions cm + buyer postal code prefix + list price.
Output: cheapest shipping cost + free-shipping unlock recommendation + 1-line note.

## Key Thresholds

- Volumetric divisor tightens below package size 30 cm in MLB BR
- Free shipping unlock most valuable in MX BR where buyers filter envio gratis first
- Flex only applies when seller registered and within 1-2 hour SLA radius
- Cross-border air-freight break-even vs Mercado Envios at roughly 0.5-1.5 kg per parcel
- Rural surcharge in MCO CO and MPE PE can be 2-3x capital rate
