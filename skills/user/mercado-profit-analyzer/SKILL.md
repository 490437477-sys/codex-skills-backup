---
name: mercado-profit-analyzer
description: "Comprehensive Mercado Libre profit analysis and revenue optimization for cross-border LATAM sellers. Calculates real unit economics across MLM (MXN), MLB (BRL), MLC (CLP), MCO (COP), MLA (ARS), MPE (PEN). Includes category commission 11-17%, listing fee, low-price unit fee, Mercado Pago 3.99% + installment absorption (cuotas sin interes 3/6/12), Mercado Envios shipping, Full warehouse storage, Brazil 2026 CBS/IBS tax reform, currency volatility drag, Hot Sale Buen Fin seasonal ROI. Use when user asks about mercado libre profit, 美客多利润分析, 美客多净利润, ganancia neta Mercado Libre, lucro liquido Mercado Livre, rentabilidade vendedor, 美客多能赚钱吗, LATAM unit economics, MELI margin."
metadata: {"category":"mercado","emoji":"馃嚰馃嚭"}
---

# Mercado Libre Profit Analyzer 馃嚰馃嚭

End-to-end profit analysis for Mercado Libre cross-border sellers across LATAM. Compute real unit economics after Mercado Pago installments, Full storage, Brazil tax reform, and currency drift.

## When to Use

Activate when the user mentions:
- 美客多利润 / Mercado Libre profit / ganancia neta / lucro liquido / lucro liquido
- 美客多能赚钱吗 / is Mercado Libre profitable / LATAM unit economics / 美客多赚钱吗
- 跨境拉美利润分析 / cross-border LATAM profit / 美客多净利润
- Mercado Pago installments / 分期付款利润 / cuotas sin interes margin impact
- Brazil 2026 tax reform CBS IBS impact on Mercado Livre margin
- Hot Sale Buen Fin Black Friday Mexico Brazil seasonal ROI

## Capabilities

- **Unit economics per site**: landed cost + commission + listing fee + payment fee + shipping + tax per listing
- **Mercado Pago installment absorption**: model how 3 / 6 / 12 cuotas sin interes eats margin when seller absorbs the interest
- **Brazil 2026 CBS/IBS drag**: project tax reform impact on electronics, apparel, beauty, home categories
- **Full vs Envios vs Flex stack**: pick cheapest fulfillment path given size tier and rotation speed
- **Currency volatility layer**: model BRL MXN ARS CLP COP PEN weekly drift against CNY USD landing cost
- **Seasonal ROI multiplier**: Hot Sale May MX, Buen Fin Nov MX, Black Friday BR, Dia de las Madres, Navidad
- **Break-even + payback**: weeks to recover sourcing + air-freight + first-listing investment
- **Tax setup drag**: amortize RFC Mexico, CNPJ Brazil, CUIT Argentina setup over projected sales

## Workflow

1. **Confirm site + currency**: pick MLM MXN / MLB BRL / MLC CLP / MCO COP / MLA ARS / MPE PEN
2. **Gather inputs**: sourcing CNY price, air-freight USD, weight kg, dimensions cm, declared price, category
3. **Apply fee stack**: commission 11-17% by category, listing fee tier, low-price unit fee if price below threshold, Mercado Pago 3.99% + installment absorption %
4. **Apply shipping cost**: Full storage + pick-pack OR Mercado Envios table OR Flex per-km rate
5. **Apply tax layer**: Brazil CBS/IBS if applicable, IVA pass-through, RFC/CNPJ/CUIT setup amortization
6. **Convert to local**: USD CNY to BRL MXN at current FX plus 30-day volatility band
7. **Seasonalize demand**: multiply by Hot Sale Buen Fin Black Friday Navidad demand factor
8. **Output**: net margin %, profit per unit local currency, monthly projection, break-even units, ROI score 1-10

## Output Schema

| Field | Description |
|-------|-------------|
| Site | MLM / MLB / MLC / MCO / MLA / MPE |
| Landed cost | Sourcing + freight + duty in local currency |
| Selling price | Final list price after cuotas split |
| Mercado Pago fee | 3.99% + installment absorption % |
| Commission | Category % 11-17% |
| Shipping cost | Full / Envios / Flex allocation |
| Tax drag | CBS/IBS / IVA / local tax |
| Net margin | % after all costs |
| Break-even units | To recover listing + inbound investment |
| ROI score | 1-10 viability rating |

## Usage Examples

```
Analyze 美客多 Mexico profit: sourcing 25 CNY, selling 599 MXN, weight 0.8 kg, electronics category
```

```
Mercado Livre Brazil lucro: sourcing 18 CNY, listing 199 BRL, beauty, 12 cuotas sem juros
```

```
美客多墨西哥净利: 进货 30 元, 售价 499 比索, 1.2 公斤, 手机配件, Hot Sale 月份
```

```
Ganancia neta Mercado Libre Argentina: costo 20 USD, precio 15000 ARS, electronica
```

```
Compare ROI for same SKU across MLM MXN vs MLB BRL vs MLC CLP at current FX rates
```

## Quick Mode

Inputs: site code + category + sourcing CNY + selling price local + weight kg.
Output: net margin % + profit per unit + 1-line optimization hint.

## Key Thresholds

- Net margin below 12%: revisit pricing or sourcing route
- Full storage over 60 days: penalty zone, raise price or pull inventory
- BRL volatility above 8% week-over-week: hedge FX or reduce exposure
- Installment absorption above 5%: pass through to list price or drop promotion
- Pay-back beyond 16 weeks: reconsider category or site priority
