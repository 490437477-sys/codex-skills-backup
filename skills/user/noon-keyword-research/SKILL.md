---
name: noon-keyword-research
description: "Keyword research and market opportunity analysis for the noon marketplace (noon.sa Saudi Arabia, noon.ae UAE, noon.com Egypt). Mines bilingual Arabic + English long-tail keywords via web search, Google Trends with MENA geo, and competitor listing extraction. Scores demand and competition across noon-specific factors (Arabic ratio, FBN coverage, Ramadan seasonality, Hijri calendar overlays). Use when the user asks about noon关键词研究, noon Arabic keywords, noon选词, what people search on noon.sa/ae/com, comparing noon keywords, evaluating product demand in KSA/UAE/Egypt, finding bilingual keyword opportunities, or any general MENA cross-border keyword research. Triggers on phrases like 'noon关键词', '沙特阿拉伯语关键词', 'UAE选品词', 'MENA long-tail keywords', 'noon autocomplete', 'noon Arabic demand', 'Ramadan keyword lift', 'Hijri seasonality'."
metadata: {"category":"noon","locale":"mena"}
---

# noon Keyword Research

Bilingual keyword research for the noon marketplace. Mirrors the Amazon keyword research workflow but adapts every step to MENA reality: Arabic + English dual mining, Google Trends with KSA/UAE/Egypt geo, Hijri seasonality overlays, and competitor extraction from noon public listings.

## Capabilities

- **Bilingual keyword mining**: Arabic + English long-tail keywords (Arabic transliterations, MSA, GCC dialect variants, brand + model combinations)
- **noon public listing extraction**: Pull real search terms from noon category pages, bestseller pages, and "customers also searched" rails
- **Competitor landscape analysis**: noon listings only — exclude Amazon / Namshi noise
- **Seasonality with Hijri overlay**: Ramadan, Eid, Hajj, White Friday, back-to-school, National Day
- **Market opportunity scoring**: 1-10 score blending competition density, Arabic ratio, price room, demand trend
- **Multi-marketplace**: noon.sa (default), noon.ae, noon.com
- **Keyword comparison**: Side-by-side scoring of multiple seed keywords
- **Refinement queries for chain use**: Output drops cleanly into `noon-listing-optimization`

## When to Use

- User says "noon关键词", "沙特阿拉伯语关键词", "MENA long-tail keywords"
- User asks what people search for on noon.sa / noon.ae
- User wants Arabic keyword volume estimate or Arabic demand validation
- User wants to compare two product ideas on noon
- User asks about Ramadan / White Friday keyword uplift
- User wants bilingual title / backend keywords for an existing noon listing
- User mentions Hijri calendar, back-to-school KSA, UAE summer slow-season

## Marketplace Defaults

| Locale | URL | Currency | VAT | Notes |
|--------|-----|----------|-----|-------|
| KSA (default) | noon.sa | SAR | 15% | Largest noon market, Arabic-first |
| UAE | noon.ae | AED | 5% | English + Arabic, expat-heavy |
| Egypt | noon.com | EGP | 14% | Price-sensitive, COD-heavy |

If the user does not specify, default to **noon.sa (KSA)**.

## Quick Mode vs Full Mode

| Mode | When | Output |
|------|------|--------|
| **Quick** | "Is 'wireless earbuds' a good keyword on noon?" | One-screen verdict: count, Arabic ratio, top 3 opportunities |
| **Full** | "Research wireless earbuds on noon.sa — full keyword report" | Full 4-section report below |
| **Compare** | "Compare wireless earbuds vs bluetooth speaker on noon.ae" | Side-by-side scoring table |

Default to **Full** unless the user explicitly asks for a quick check.

## Workflow

### Step 1: Pin Locale & Seed

Confirm:
1. Marketplace (default KSA)
2. Seed keyword in Arabic and English
3. Category context if known (e.g. "consumer electronics / headphones")

If the user provides only one language, infer the other. Reference `references/noon-arabic-keyword-cheatsheet.md` for transliteration hints.

### Step 2: Mine Bilingual Long-tail Keywords

noon does not expose a public autocomplete API the way Amazon does. Use these four sources in parallel:

#### 2a. noon's own on-page search

Fetch the noon search page and parse the "Popular suggestions" and "Suggestions" rail:

```
web_fetch https://www.noon.sa/search?q=<seed-english>
web_fetch https://www.noon.sa/search?q=<seed-arabic>
```

For each result, collect every autocomplete / related-search term. These are real, fresh demand signals directly from noon.

#### 2b. Prefix & suffix expansion

Manually generate query variations:

| Pattern | Arabic example | English example |
|---------|----------------|-----------------|
| Best | أفضل سماعات لاسلكية | best wireless earbuds |
| Cheap / under price | سماعات لاسلكية رخيصة | cheap wireless earbuds |
| Top | أفضل 10 سماعات | top 10 wireless earbuds |
| For [user] | سماعات لاسلكية للرياضة | wireless earbuds for running |
| With [feature] | سماعات بميكروفون | earbuds with mic |
| Brand X + product | AirPods Pro 2 | AirPods Pro 2 |
| Model number | Earbuds BT-509 | Earbuds BT-509 |
| Year | أفضل سماعات 2025 | best earbuds 2025 |
| A–Y first-letter suffixes | سماعات لاسلكية أ / ب / ت ... | earbuds a / b / c ... |

Run at least the top 8 patterns × Arabic + English to land 60-120 candidate keywords.

#### 2c. Category bestseller pages

Fetch the relevant noon category page and extract the top 20 bestsellers. From each, capture:

- Title (Arabic + English where both present)
- Brand
- Price
- Review count
- Sub-category / filter applied

Mine titles for compound keywords (color + product, brand + model, capacity + product).

#### 2d. People Also Searched rail on PDPs

Fetch 3-5 bestseller product detail pages and extract the "customers also viewed / searched for" rail. These are noon-curated cross-sells and reflect adjacent demand.

#### Output of Step 2

```
Candidate pool: 80-150 keywords
- Arabic: 60-70% of total (typical KSA ratio)
- English / transliterated: 30-40%
- Brand + model combos: 5-10%
```

### Step 3: Validate Demand

For each high-potential candidate from Step 2, run a quick demand check.

#### 3a. Google Trends with MENA geo

```
web_fetch https://trends.google.com/trends/explore?q=<keyword>&geo=SA
web_fetch https://trends.google.com/trends/explore?q=<keyword>&geo=AE
web_fetch https://trends.google.com/trends/explore?q=<keyword>&geo=EG
```

If Google Trends 429s, fall back to:

```
web_search "<keyword>" demand trend Saudi Arabia 2024
web_search "<keyword>" most searched noon KSA
```

Capture: 12-month trend direction (rising/stable/declining), peak months, Hijri season overlay.

#### 3b. noon search-result density

For each candidate, count noon listings:

```
web_search "<keyword>" site:noon.sa
web_search "<keyword>" site:noon.ae
```

Rules of thumb:
- < 200 results → niche, low direct competition, may signal low demand
- 200-2,000 results → healthy mid-tail, sweet spot
- 2,000-10,000 results → competitive, need differentiation
- > 10,000 results → saturated, only strong brand wins

#### 3c. Bilingual ratio check

Healthy KSA ratio: ~70% Arabic / 30% English
Healthy UAE ratio: ~55-60% Arabic / 40-45% English

If Arabic demand is low for a candidate, flag it as English-only — still valid but missing the Arabic-market lift.

### Step 4: Competition Landscape

Analyze noon-specific competitors (exclude Amazon / Namshi unless the user explicitly wants cross-platform view):

1. **Total competitors**: noon search-result count from 3b
2. **Price range**: scan top 20 bestsellers → min / median / max / IQR
3. **Rating distribution**: how many listings have 4.0+, 4.3+, 4.5+
4. **Top brands**: count occurrences among top 20
5. **FBN coverage**: ratio of "fulfilled by noon" (FBN) vs seller-fulfilled (FB) in top 20
6. **Arabic listing quality**: how many top 20 have Arabic title + Arabic bullets?
7. **Review depth**: distribution of 100+, 1,000+, 5,000+ reviews

### Step 5: Synthesize Report

Roll up Steps 2-4 into the output format below.

## Output Format

```
## noon Keyword Report: [seed keyword]
**Marketplace:** noon.sa (KSA, SAR) | noon.ae (UAE, AED) | noon.com (EGY, EGP)
**Category:** [main > sub]
**Date:** YYYY-MM-DD

### 1. Long-tail Keywords ([count] mined)

**High Commercial Intent (Arabic):**
- [kw] — est. demand: H/M/L
- ...

**High Commercial Intent (English / transliterated):**
- [kw] — est. demand: H/M/L
- ...

**Informational / Research:**
- [kw]
- ...

**Brand + Model:**
- [kw]
- ...

**Niche / Specific (low competition):**
- [kw]
- ...

### 2. Bilingual Demand

| Metric | Value |
|--------|-------|
| Arabic candidate count | [X] |
| English / transliterated count | [Y] |
| Arabic ratio | [X/(X+Y)]% |
| Top Arabic keyword | [kw] |
| Top English keyword | [kw] |
| Healthy ratio match (Y/N) | [Y/N + note] |

### 3. Competition Landscape

| Metric | Value |
|--------|-------|
| Estimated noon listings | [number] |
| Price range | [currency min] - [currency max] |
| Median price | [currency] |
| Average rating | [stars] |
| Top brands | [brand1, brand2, brand3] |
| FBN coverage (top 20) | [X]% |
| Arabic listing quality (top 20) | [X]% have Arabic title + bullets |
| Review depth — 1,000+ reviews | [X] listings |

### 4. Seasonal Trend

| Window | Expected lift | Action |
|--------|---------------|--------|
| Ramadan | +X% | List by [date] |
| White Friday | +X% | Inventory ramp by [date] |
| Back-to-school | +X% | N/A or relevant |
| Hajj season | +X% | N/A or relevant |

Google Trends (geo=SA, 12mo): Rising / Stable / Declining
Hijri seasonality flag: Yes (Ramadan / Hajj dependent) / No

### 5. Market Opportunity Score: [X/10]

**Score breakdown:**
- Competition density (noon listings): Low / Medium / High — [why]
- Arabic demand ratio: Healthy / Skewed — [why]
- Price room: Low / Medium / High — [why]
- Demand trend: Growing / Stable / Declining — [why]
- Niche potential: Low / Medium / High — [why]

**Recommendation:** [1-2 sentence actionable next step]

### 6. Hand-off to noon-listing-optimization

Top 5 keywords (Arabic-first, with bilingual backend suggested):
1. [AR] | [EN] — Primary title candidate
2. ...
3. ...
4. ...
5. ...
Backend search terms block: [comma-separated, no duplication with title]
```

## Multi-Keyword Comparison

When the user asks to compare two or more keywords, run Steps 2-4 for each, then present:

| Metric | Keyword A | Keyword B | Keyword C |
|--------|-----------|-----------|-----------|
| Long-tail count | — | — | — |
| Arabic ratio | % | % | % |
| noon listings (density) | — | — | — |
| Median price | — | — | — |
| Top brand dominance | — | — | — |
| FBN coverage | % | % | % |
| Trend direction | — | — | — |
| Opportunity score | /10 | /10 | /10 |

End with **Recommendation**: which keyword to pursue, which to abandon, and what entry angle.

## Refinement Rules

When pruning the candidate pool to the final top 5:

- Keep all 70%+ Arabic candidates that score ≥ 6/10
- Drop pure-English candidates unless the bilingual ratio is already skewed
- Always keep the brand + model combo for the winning keyword (capture branded search)
- Always keep one Hijri-season anchor if the category is Ramadan-sensitive
- Always keep one price-modifier keyword ("رخيص" / "best cheap") for paid-search hand-off

## Limitations & When to Escalate

This skill uses publicly available data (web search, Google Trends, noon public pages). It cannot:

- Access noon's actual search-volume backend
- Confirm exact BSR-to-units conversion for noon
- Verify real-time FBN capacity per warehouse
- See competitor PPC bid or ACoS data

When the user needs precise volumes, recommend pairing with noon's own Seller Central brand analytics, or a paid MENA market intelligence tool.

## Related Skills

- `noon-product-research` — for full product-level opportunity analysis
- `noon-listing-optimization` — for turning these keywords into an Arabic-first listing
- `amazon-keyword-research` — for cross-platform validation (Amazon.sa / Amazon.ae)

---

_Built for the noon marketplace — KSA, UAE, Egypt. Default locale KSA unless the user specifies otherwise._
