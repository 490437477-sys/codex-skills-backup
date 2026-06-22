---
name: mercado-review-analyzer
description: "Mercado Libre review analysis for competitive intelligence and product improvement. Extracts sentiment patterns, recurring complaints, feature requests from Spanish and Portuguese reviews across MLM MLB MLC MCO MLA MPE. Detects MercadoLider eligibility signals, star rating drift over time, defect complaint clusters (product quality, shipping damage, description mismatch, sizing issues, language localization gaps). Use when user asks about 美客多评论分析, 美客多差评分析, Mercado Libre review analysis, 分析美客多评价, reputacion vendedor Mercado Libre, reputacao vendedor Mercado Livre, analisis de opiniones, 美客多怎么提升评分, MELI reviews."
metadata: {"category":"mercado","emoji":"馃嚰馃嚭"}
---

# Mercado Libre Review Analyzer 馃嚰馃嚭

Deep review-mining skill for Mercado Libre cross-border sellers. Turn Spanish and Portuguese customer feedback into listing fixes, sourcing pivots, and MercadoLider badge improvements.

## When to Use

Activate when the user mentions:
- 美客多评论分析 / 美客多差评分析 / 分析美客多评价 / 美客多怎么提升评分
- Mercado Libre review analysis / analisis de opiniones / analise de avaliacoes
- Reputacion vendedor / reputacao vendedor / MercadoLider eligibility
- Recurring complaint pattern / defect cluster in reviews / 美客多质量问题反馈
- Star rating drift over time / calificacion trend / evolucao das estrelas
- Cross-language sentiment Spanish Portuguese reviews

## Capabilities

- **Sentiment extraction**: classify Spanish Portuguese reviews into positive neutral negative with theme tags
- **Complaint clustering**: group recurring defects (quality, shipping damage, sizing, color mismatch, description gap, language localization)
- **Feature request mining**: pull buyer-suggested improvements from 3-4 star neutral reviews
- **Star rating drift**: track rating evolution month by month, flag sharp drops in 7-day windows
- **MercadoLider signal**: correlate rating + volume + claims rate to badge eligibility timeline
- **Photo review analysis**: extract buyer-uploaded image complaints (broken parts, color gap, sizing proof)
- **Language localization gap**: detect complaints citing Spanish Portuguese translation or manual missing
- **Competitor review scrape**: side-by-side sentiment compare vs top 3 competing listings in same category

## Workflow

1. **Collect review set**: pull all reviews for target ASIN-equivalent listing across site, paginated
2. **Split positive vs negative**: bucket 1-2 stars as defect pool; 3 stars as neutral improvement pool; 4-5 stars as praise pool
3. **Tag themes**: classify each review by defect theme (quality, shipping, sizing, color, description, language, etc)
4. **Cluster recurring complaints**: rank themes by frequency and severity (return risk vs cosmetic)
5. **Detect rating drift**: compute 30 / 60 / 90 day rolling average; flag 0.3+ star drop
6. **Evaluate MercadoLider path**: rating + volume + claims rate threshold check; recommend action to reach next tier
7. **Mine feature requests**: extract suggestion phrases from 3-4 star reviews for product roadmap
8. **Compare competitor reviews**: pull top 3 competitor review themes; find weak spots they exploit
9. **Output**: defect priority list + MercadoLider action plan + listing copy fix suggestions + sourcing pivot signals

## Output Schema

| Field | Description |
|-------|-------------|
| Site | MLM / MLB / MLC / MCO / MLA / MPE |
| Total reviews | Count and average star rating |
| Defect clusters | Top 5 complaint themes ranked by frequency |
| Severity score | Return-risk weighted per theme |
| Rating drift | 30 / 60 / 90 day rolling average |
| MercadoLider status | Current tier and gap to next |
| Feature requests | Top buyer-suggested improvements |
| Competitor gap | Themes where competitors score worse |
| Action items | Listing copy / sourcing / photo fixes |

## Usage Examples

```
Analyze 美客多 Mexico reviews for my electronics listing: 350 reviews, 4.3 stars, drops last 30 days?
```

```
Mercado Livre Brasil reviews: clustering 1-2 star complaints in beleza category
```

```
美客多墨西哥差评分析: 200 条评价, 找出质量问题和尺码反馈的聚类
```

```
Analisis reputacion Mercado Libre Argentina: gap to MercadoLider Plata tier, claims rate check
```

```
Compare sentiment vs top 3 competitor listings in MLB electronics category, find exploit
```

## Quick Mode

Inputs: site + category + listing ID or URL.
Output: top 3 defect clusters + MercadoLider gap + 1-line priority fix.

## Key Thresholds

- Rating drop over 0.3 stars in 7 days: trigger listing pause review
- Negative review above 8% of monthly volume: claims rate risk to MercadoLider
- Sizing complaints above 15% of 1-2 star pool: update size chart and photo proof
- Spanish Portuguese keyword gap in 1-2 star reviews: localization sprint needed
- MercadoLider Gold requires typically 4.8+ rating and low claims rate over rolling 60 days
