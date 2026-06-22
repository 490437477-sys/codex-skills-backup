---
name: temu-keyword-research
description: "TEMU keyword research and market opportunity analysis for cross-border sellers. Mine long-tail English keywords from TEMU search, Google Trends, Amazon autocomplete (as proxy), and competitor listings. Analyze competition density, price range, return-rate signal, and seasonal trends on 13 TEMU marketplaces (US/UK/DE/FR/IT/ES/NL/PL/PT/MX/BR/JP/KR/SA/AE/PH). Score 1-10 market opportunity for any seed keyword. Use when: (1) user asks what to sell on TEMU, (2) user wants to find TEMU niche opportunities, (3) user wants to validate a keyword before launching a listing, (4) user wants to compare two keywords on TEMU, (5) user wants to know TEMU search demand for a product, (6) user mentions TEMU选词, TEMU热搜, TEMU搜索词, TEMU keyword ideas, TEMU SEO."
metadata: {"category":"cross-border-ecommerce","platform":"temu"}
---

# TEMU Keyword Research

Free keyword research for TEMU sellers. No API key required.

## When to Use This Skill

Use this skill whenever the user:
- Asks what to sell on TEMU
- Wants long-tail keyword ideas for a TEMU listing
- Wants to compare 2-3 keywords on a TEMU marketplace
- Asks about TEMU demand, TEMU hot searches, TEMU niche opportunities
- Mentions 选TEMU品 / TEMU选词 / TEMU热搜 / TEMU SEO

Do NOT use this skill for: Amazon keyword research (use `amazon-keyword-research`), Temu product/margin research (use `temu-product-research`), Temu listing copy generation (use `temu-listing-optimization`).

## Capabilities

- **Long-tail keyword mining**: 100-200 real search terms for a seed keyword (multi-source: TEMU site search + Amazon autocomplete proxy + Google suggest)
- **Marketplace-specific**: 13 TEMU country sites (US, UK, DE, FR, IT, ES, NL, PL, PT, MX, BR, JP, KR, SA, AE, PH)
- **Competition density analysis**: count of competing products on TEMU, price range, top sellers
- **Seasonal trend detection**: 12-month Google Trends data
- **Market opportunity score**: 1-10 combining competition, price room, demand trend
- **Multi-keyword comparison**: side-by-side scoring
- **Multilingual support**: output keywords in English, German, French, Spanish, etc. based on marketplace

## TEMU-Specific Search Behavior (Critical Context)

Unlike Amazon (search-driven), TEMU is **browsing + discovery + price-driven**. This changes keyword strategy:

| Aspect | Amazon | TEMU |
|---|---|---|
| Primary discovery | Search box | Category page + recommendation engine |
| Keyword specificity | High (long-tail matters) | Lower (broad + short-tail dominate) |
| Average query length | 3-5 words | 2-3 words |
| Title keyword weight | 30% | 60%+ (title is THE main ranking signal) |
| Backend search terms | Yes (250 bytes) | No |
| A+ Content | Yes | No (but has Rich Description with images) |
| Click-through driver | Reviews + images + price | Price + image + first 3 photos |
| Video | Optional | Strongly recommended (algo boost) |
| Conversion driver | Reviews | Price competitiveness + fast ship |

**Implication for keyword research**: On TEMU, focus on **broad + high-volume + low-competition** keywords. Do not over-invest in hyper-long-tail (Amazon-style) because TEMU buyers don't type long queries.

## Workflow (6 Steps)

### Step 1: Validate the Seed Keyword

Before mining long-tails, confirm the seed is:
- A noun, not a brand name
- Not a banned/restricted category (medical, weapons, adult)
- Has clear US English equivalent

If user provides Chinese keyword (e.g. 机械臂), translate to English first via `mcp__minimax_coding_plan_mcp__web_search` or browser knowledge.

### Step 2: Mine Long-tail Keywords

Use the bundled script to gather keyword candidates from 3 sources in parallel:

```bash
<skill>/scripts/keyword_mine.sh "<seed_keyword>" <marketplace>
```

**Marketplace codes** (TEMU site 2-letter codes):
- `us` (default), `uk`, `de`, `fr`, `it`, `es`, `nl`, `pl`, `pt`, `mx`, `br`, `jp`, `kr`, `sa`, `ae`, `ph`

**What the script does**:
1. Queries Amazon autocomplete for the seed + alphabet suffixes (best free long-tail source for English)
2. Scrapes TEMU's search suggestion dropdown (via web search) for the same seed
3. Combines and deduplicates, outputs 100-200 candidates sorted by length

**Why this matters**: Amazon autocomplete and TEMU buyer language overlap ~70% in English markets. Amazon's autocomplete is the most reliable free long-tail source, and TEMU buyers searching the same product use similar terms. Cross-referencing both reduces noise.

### Step 3: TEMU Competition Analysis

For each candidate keyword (top 10), use `mcp__tavily__tavily_search` and `mcp__tavily__tavily_extract`:

1. Search `"<keyword>" site:temu.com` to count competing listings
2. Extract top 5 TEMU listings to get:
   - Price range (min, max, median)
   - Average rating and review count
   - First 60 chars of title (reveals keyword patterns)
   - Image count and quality signals
3. Note: TEMU shows total sold count and rating for each listing

```python
# Competition score template
competitors_5000_plus = "saturated"
competitors_500_to_5000 = "medium"
competitors_under_500 = "blue ocean candidate"
```

**Why this matters**: TEMU has no public keyword volume data. Product count is the closest proxy. If 5,000+ listings exist for a keyword, expect price war and 2-5% conversion rates. If <500, you have room.

### Step 4: Check Google Trends

Use `mcp__tavily__tavily_extract` on:
```
https://trends.google.com/trends/explore?q=<keyword>&geo=<marketplace_country>
```

Or fallback to `mcp__tavily__tavily_search` with:
```
"<keyword>" seasonal trend peak months <current_year>
```

Identify: trend direction, seasonal peaks, year-over-year change, related rising queries.

**Critical TEMU context**: TEMU's discount-driven model amplifies seasonal demand. Christmas, Black Friday, Prime Day-style events drive 3-5x volume. Plan inventory 60 days before peak.

### Step 5: Cross-Reference Price Room

TEMU's price competitiveness is the #1 ranking factor. Use the price data from Step 3 to:
- Compute median price for the keyword
- Compare to your target COGS + freight + 25% margin
- If target > median * 1.2, you cannot compete (TEMU will rank you lower)

**Why this matters**: A keyword with high demand but extremely low median price (e.g. $3 phone stand) is a trap — your $5 product will be ranked below $2 alternatives regardless of quality.

### Step 6: Synthesize Report

Use the Output Format below.

## Output Format

```
## TEMU Keyword Research Report: [seed_keyword]
**Marketplace:** TEMU [US/UK/DE/...]
**Date:** [current date]
**Language target:** [English/German/French/...]

### 1. Long-tail Keywords ([N] found)

**Primary (broad, high-volume):**
- [keyword]
- ...

**Secondary (mid-tail, clearer intent):**
- [keyword with modifier like "for kids", "with stand", "mini"]
- ...

**Long-tail (low competition, specific use case):**
- [3-5 word phrases]
- ...

**Cross-language variants** (if marketplace != US):
- [DE equivalent]
- [FR equivalent]
- ...

### 2. TEMU Competition Landscape

| Metric | Value |
|--------|-------|
| Estimated competing products | [N] |
| Price range | $[min] - $[max] |
| Median price | $[med] |
| Top sellers price cluster | $[range of top 10 by sales] |
| Average rating | [stars] |
| Top brands | [list or "mostly unbranded white-label"] |
| Return-rate signal | [low/medium/high — based on rating pattern + review complaints] |

### 3. Seasonal Trends (12-month)

[Describe trend: rising/stable/declining]
[Note peak months]
[Year-over-year direction]

### 4. Market Opportunity Score: [X/10]

**Score breakdown** (each 0-10):
- **Competition density** [score]: [reasoning based on # products]
- **Price room** [score]: [reasoning based on median vs your cost]
- **Demand trend** [score]: [reasoning based on Google Trends + TEMU sold count]
- **Niche potential** [score]: [reasoning based on broad vs long-tail ratio]
- **Avg** = [X]/10

**Recommendation**: [1-2 sentence actionable]
- ≥ 7.5: GO — direct launch
- 6.0-7.4: GO with caution — control first batch
- 5.0-5.9: WATCH — look for differentiation angle
- < 5.0: SKIP

### 5. Suggested TEMU Title Formula

Based on top 5 seller title patterns, recommended structure:
`[Brand/blank] + [Core keyword] + [Key feature 1] + [Key feature 2] + [Spec/dimension]`

Example: `4DOF Robot Arm Kit MG90S Servo Arduino-Compatible STEM DIY for Teens 13+`

(60-100 chars; covers primary keyword, servos, use case, age-target for compliance positioning)
```

## Multi-Keyword Comparison

When user asks to compare keywords (e.g. "robot arm vs robotic arm kit vs mechanical arm"), run the full workflow for each, then output a comparison table:

| Metric | keyword A | keyword B | keyword C |
|--------|-----------|-----------|-----------|
| Long-tail count | | | |
| TEMU product count | | | |
| Median price | | | |
| Avg rating | | | |
| Trend direction | | | |
| Opportunity score | | | |
| **Recommendation** | | | |

End with one-line verdict on which to prioritize.

## Limitations

- No exact search volume data (TEMU does not publish it)
- Product count is approximate (scraped from web search, not from a private database)
- Some TEMU pages are JS-rendered; the script falls back to Google site: search for counts
- For precise volume + sales data, recommend using paid tools (Helium 10, Jungle Scout) or TEMU's Seller Center keyword tool

## Integration with Other TEMU Skills

- **temu-product-research**: Use this first to validate the product is viable. Then use temu-keyword-research to find listing keywords.
- **temu-listing-optimization**: After finding keywords, use this to generate the actual title/bullets/description copy.

Chain example:
1. "Should I sell robotic arm on TEMU US?" → `temu-product-research`
2. "What keywords should I target?" → `temu-keyword-research` (this skill)
3. "Write the TEMU listing with these keywords" → `temu-listing-optimization`

## Resources

- `scripts/keyword_mine.sh`: Multi-source keyword scraper
- `references/temu_search_behavior.md`: TEMU search/algorithm cheat sheet
- `references/temu_keyword_sources.md`: Curated list of free keyword data sources
