---
name: noon-negative-keywords
description: "Optimize noon Sponsored Products campaigns by identifying and managing negative keywords in Arabic + English. Reduce wasted ad spend on irrelevant MENA search terms while protecting converting Arabic-dialect queries. Distinguishes between exact and phrase negatives, KSA/UAE/EG dialect variants, and competitor brand terms. Use when the user asks about noon negative keywords, MENA PPC waste reduction, Arabic search-term negatives, sponsored products optimization on noon, or ACoS reduction on noon ads."
metadata: {"category":"noon","locale":"mena"}
---

# noon Negative Keywords

Cut wasted noon ad spend by blocking irrelevant Arabic + English search terms while preserving every converting query.

## Capabilities

- **Bilingual mining**: pull Arabic + English search-term reports from noon Seller Central
- **Dialect-aware filtering**: recognize MSA vs KSA/UAE/EG variants (e.g. عطر vs كولونيا vs برفان) so negatives do not over-fire
- **Intent classification**: separate browse / compare / buy-intent queries; only block non-buy-intent
- **Three match types**: exact, phrase, broad for both Arabic and Latin
- **Brand protection**: detect competitor brand names (Apple, Samsung, Namshi, etc.) and add as exact negatives unless the user sells OEM
- **Hijri/seasonal pause**: flag seasonal negatives (Ramadan decor in non-Ramadan months) instead of permanent removal
- **Spend vs conversion ranking**: prioritize negatives by wasted spend, not just by clicks
- **Bulk negative upload**: generate a noon-compatible negative-keyword CSV per ad group

## Workflow

### 1. Pull the search-term report
Last 30 days from noon Sponsored Products. Required columns: search term, impressions, clicks, spend, orders, ACOS.

### 2. Compute waste per term
Waste = spend - (orders x AOV). A term with 50 clicks, 0 orders, 50 SAR spend is higher priority than one with 100 clicks, 1 order, 80 SAR spend.

### 3. Classify intent
- **Buy-intent** (e.g. buy, سعر, شراء, [brand] + [model]): NEVER negative
- **Compare/browse** (e.g. vs, مقارنة, أفضل, best, review): consider negative unless conversion rate is healthy
- **Irrelevant** (e.g. free, used, refurbished, مستعمل, مجانا): usually negative
- **Wrong category** (e.g. shoes when selling laptops): always negative

### 4. Decide match type

| Wasted spend (30d) | Impressions | Match type |
|--------------------|-------------|------------|
| > 200 SAR          | > 500       | exact      |
| > 100 SAR          | > 200       | phrase     |
| low                | high        | leave      |

For Arabic: prefer exact match (phrase is unreliable across diacritics).

### 5. Build the negative list
One CSV per ad group:
- campaign_name, ad_group_name, negative_keyword, match_type, locale

### 6. Apply and verify
Upload to noon Seller Central. Wait 7 days, then re-pull search-term report. Confirm wasted spend dropped without cannibalizing converting terms.

## Output

- **Negative-keyword CSV** (noon-compatible format)
- **Summary**: total wasted spend blocked, total spend retained, expected ACOS reduction
- **Watchlist**: 5 borderline terms to monitor (not negative yet, but candidates)

## Quick Mode

If user pastes a search-term report: return only the ranked negative list (no CSV formatting needed).
