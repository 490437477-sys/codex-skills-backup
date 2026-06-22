---
name: noon-competitor-analysis
description: "Full-spectrum competitor analysis for the noon marketplace. Compares listings, pricing in SAR/AED/EGP, Arabic/English copy, FBN vs FBM choice, review velocity, advertising strategy, and White Friday/Ramadan positioning against direct competitors. Detects cross-border overflow from Amazon.ae/Amazon.sa, Namshi, Ounass, 6thStreet. Use when the user asks about noon competitor analysis, ASIN-style SKU comparison on noon, pricing teardown in MENA, Arabic listing teardown, or how to beat a specific noon seller."
metadata: {"category":"noon","locale":"mena"}
---

# noon Competitor Analysis

Outsmart MENA competitors on noon by dissecting their listings, pricing, FBN choice, and seasonal playbooks.

## Capabilities

- **Listing teardown**: Arabic + English copy, imagery, Rich Content usage, bullet structure
- **Pricing waterfall**: SAR/AED/EGP retail, COD vs prepaid, discounts, White Friday anchor
- **FBN vs FBM detection**: SKU-level inference from delivery promise and return policy
- **Review velocity**: monthly review growth, star decay, complaint pattern extraction
- **Ad footprint**: Sponsored Products presence, search-term ownership, brand store signals
- **Cross-border mapping**: Amazon.ae / Amazon.sa / Namshi / Ounass / 6thStreet overlap
- **Seasonal playbook**: Ramadan / White Friday / back-to-school promo cadence
- **Compliance posture**: SASO/SFDA certifications held, brand registry status

## Workflow

### 1. Snapshot the competitor set
Pick top 5 by BSR-equivalent + 2 long-tail challengers. Use noon search autocomplete for ranking signals.

### 2. Listing teardown
For each competitor: title (AR + EN length), bullet count, description depth, imagery count, video presence, Rich Content module count.

### 3. Pricing waterfall
Extract 30 / 60 / 90-day price history (where visible). Note anchor prices, coupon stacking, White Friday discounts, COD surcharges.

### 4. FBN vs FBM signal
- **FBN**: noon-fulfilled badge, 1-2 day delivery promise, free returns
- **FBM**: 3-7 day promise, sold and shipped by [seller]
- **Cross-border**: estimated shipping from CN / IN / TR; longer delivery, separate return path

### 5. Review analysis
Pull last 6 months reviews. Compute star decay (rolling 90-day mean), top complaint topics, response rate from seller.

### 6. Ad footprint
Search the head term + 5 long-tail Arabic terms on noon; record which competitors appear in sponsored slots and how often.

### 7. Compliance posture
Identify brand-registered vs unbranded. SFDA / SASO numbers if visible. Local Importer of Record presence (KSA).

### 8. Score and gap matrix

| Dimension | You | Comp A | Comp B | Gap |
|-----------|-----|--------|--------|-----|
| Arabic title length | 60 chars | 90 | 70 | -30 |
| FBN fulfillment | Yes | Yes | No | even |
| Review count | 120 | 800 | 35 | -680 |
| Rich Content | 4 modules | 6 | 0 | -2 |
| Sponsored dominance | low | high | none | opportunity |

## Output

- **One-page competitor card per SKU** (8 fields above)
- **Aggregated gap matrix** across all competitors
- **Top 3 differentiation plays** with expected impact and effort

## Quick Mode

If the user gives one competitor name/URL: return the 8-dimension snapshot only, no aggregation.
