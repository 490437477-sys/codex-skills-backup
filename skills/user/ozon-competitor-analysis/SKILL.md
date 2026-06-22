---
name: ozon-competitor-analysis
description: "Full-spectrum competitor analysis for the Ozon marketplace. Compares listings, pricing in RUB/KZT/BYN, Russian copy, FBO vs FBS choice, review velocity, advertising strategy, and seasonality positioning against direct competitors. Detects cross-platform overflow from Wildberries, Yandex Market, SberMegaMarket, AliExpress Russia, and Chinese cross-border. Use when the user asks about Ozon competitor analysis, ozon 竞争分析, 锌褉芯写邪胁褑 锌褉芯写邪胁邪褌褜 Russian listings teardown, pricing teardown in CIS, or how to beat a specific Ozon seller."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Competitor Analysis

Outsmart CIS competitors on Ozon by dissecting their listings, pricing, FBO/FBS choice, and seasonal playbooks.

## Capabilities

- **Listing teardown**: Russian copy length and structure, bullet points, rich content usage, image count
- **Pricing waterfall**: RUB / KZT / BYN retail, Ozon discounts, promo card stacking, New Year anchor
- **FBO vs FBS detection**: SKU-level inference from delivery promise, return policy, and warehouse region
- **Review velocity**: monthly review growth, star decay, complaint pattern extraction
- **Ad footprint**: Ozon Performance presence, search-term ownership, brand banner dominance
- **Cross-platform mapping**: Wildberries, Yandex Market, SberMegaMarket, AliExpress Russia overlap
- **Seasonal playbook**: New Year / 3.8 Womens Day / 9.1 Knowledge Day promo cadence
- **Compliance posture**: EAC certificates held, country of origin, Russian importer of record

## Workflow

### 1. Snapshot the competitor set
Pick top 5 by sales rank + 2 long-tail challengers. Use Ozon search autocomplete for ranking signals.

### 2. Listing teardown
For each competitor: title (RU length, ideally <= 80 chars), bullet count, description depth, imagery count, video presence, Rich Content module count.

### 3. Pricing waterfall
Extract 30 / 60 / 90-day price history (where visible). Note anchor prices, Ozon card discounts, coupon stacking, New Year discounts.

### 4. FBO vs FBS signal

- **FBO**: Fulfilled by Ozon badge, 1-2 day delivery to major Russian cities, Ozon Rocket last-mile
- **FBS**: 3-7 day delivery, sold and shipped by [seller]
- **Cross-border (CN -> RU)**: estimated 14-30 day delivery, separate return path, often from CN warehouse

### 5. Review analysis
Pull last 6 months reviews. Compute star decay (rolling 90-day mean), top complaint topics, response rate from seller.

### 6. Ad footprint
Search the head term + 5 long-tail Russian terms on Ozon; record which competitors appear in sponsored slots and how often.

### 7. Compliance posture
Identify brand-registered vs unbranded. EAC numbers if visible. Russian Importer of Record presence.

### 8. Score and gap matrix

| Dimension | You | Comp A | Comp B | Gap |
|-----------|-----|--------|--------|-----|
| Russian title length | 70 chars | 80 | 60 | -10 |
| Fulfillment | FBS | FBO | FBS | mixed |
| Review count | 80 | 500 | 25 | -420 |
| Rich Content | 4 modules | 6 | 0 | -2 |
| Sponsored dominance | low | high | none | opportunity |

## Output

- **One-page competitor card per SKU** (8 fields above)
- **Aggregated gap matrix** across all competitors
- **Top 3 differentiation plays** with expected impact and effort

## Quick Mode

If the user gives one competitor name/URL: return the 8-dimension snapshot only, no aggregation.
