---
name: ozon-negative-keywords
description: "Optimize Ozon Performance (advertising) campaigns by identifying and managing negative keywords in Russian + English. Reduce wasted ad spend on irrelevant CIS search terms while protecting converting Russian-colloquial queries. Distinguishes between exact and phrase negatives, Russian transliteration variants, and competitor brand terms. Use when the user asks about Ozon negative keywords, Ozon Performance waste reduction, 芯褌褉懈褑邪褌械谢褜薪褘械 泻谢褞褔懈 Russian search-term negatives, or ACoS reduction on Ozon ads."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Negative Keywords

Cut wasted Ozon Performance ad spend by blocking irrelevant Russian + English search terms while preserving every converting query.

## Capabilities

- **Bilingual mining**: pull Russian + English search-term reports from Ozon Seller Central
- **Russian transliteration awareness**: recognize Latin-transliterated Russian (e.g. noutbuk vs 薪芯褍褌斜褍泻) so negatives do not over-fire
- **Intent classification**: separate browse / compare / buy-intent queries; only block non-buy-intent
- **Three match types**: exact, phrase, broad for both Russian and Latin
- **Brand protection**: detect competitor brand names and add as exact negatives unless the user sells OEM
- **Seasonal pause**: flag seasonal negatives (9.1 Knowledge Day items in non-school months) instead of permanent removal
- **Spend vs conversion ranking**: prioritize negatives by wasted spend, not just by clicks
- **Bulk negative upload**: generate an Ozon-compatible negative-keyword list per campaign

## Workflow

### 1. Pull the search-term report
Last 30 days from Ozon Performance. Required columns: search term, impressions, clicks, spend, orders, ACoS.

### 2. Compute waste per term
Waste = spend - (orders x AOV). A term with 50 clicks, 0 orders, 1000 RUB spend is higher priority than one with 100 clicks, 1 order, 800 RUB spend.

### 3. Classify intent

- **Buy-intent** (e.g. 泻褍锌懈褌褜, 褑械薪邪, 蟹邪泻邪蟹邪褌褜): NEVER negative
- **Compare/browse** (e.g. 褋褉邪胁薪械薪懈械, 谢褍褔褕懈泄, 芯褌蟹褘胁褘): consider negative unless CVR is healthy
- **Irrelevant** (e.g. 斜械褋锌谢邪褌薪芯, 斜褍, 斜褍 褋芯褋褌芯褟薪懈褟): usually negative
- **Wrong category** (e.g. 芯斜褍胁褜 when selling clothes): always negative

### 4. Decide match type

| Wasted spend (30d) | Impressions | Match type |
|--------------------|-------------|------------|
| > 2000 RUB         | > 500       | exact      |
| > 1000 RUB         | > 200       | phrase     |
| low                | high        | leave      |

For Russian: prefer exact match (phrase is unreliable across yo/soft-sign variations).

### 5. Build the negative list
One CSV per campaign:
- campaign_name, negative_keyword, match_type, locale

### 6. Apply and verify
Upload to Ozon Seller Central. Wait 7 days, then re-pull search-term report. Confirm wasted spend dropped without cannibalizing converting terms.

## Output

- **Negative-keyword list** (Ozon-compatible format)
- **Summary**: total wasted spend blocked, total spend retained, expected ACoS reduction
- **Watchlist**: 5 borderline terms to monitor (not negative yet, but candidates)

## Quick Mode

If user pastes a search-term report: return only the ranked negative list (no list formatting needed).
