---
name: ozon-keyword-research
description: "Ozon (Озон) keyword research and market opportunity analysis for sellers. Mines long-tail Russian keywords from Ozon autocomplete + Yandex Wordstat + Yandex search suggest, decodes Russian noun declensions (падежи), analyzes competitor listing density on Ozon.ru, and scores market opportunity for any keyword on Ozon.ru / Ozon.kz / Ozon.by. No API key required for the public surface. Use when the user asks: Ozon keyword ideas, ozon关键词研究, как искать ключевые слова на Озоне, Russian product keyword research, finding what to sell on Ozon, niche analysis on Ozon, Ozon autocomplete, long-tail keywords for Ozon listings, Yandex Wordstat lookup, Russian keyword expansion, what are Russian buyers searching for, or any Ozon keyword expansion / market opportunity question."
metadata: {"emoji":"🔎","category":"ozon"}
---

# Ozon Keyword Research 🔎

Free Ozon keyword research for cross-border and Russian sellers. No API key for the public surface — works out of the box.

## Capabilities

- **Long-tail keyword mining**: Extract 100-300 real Russian search terms from Ozon + Yandex autocomplete, with Russian noun declensions (падежи) automatically expanded
- **Russian prefix expansion**: "купить [товар]", "недорогой [товар]", "для дома", "со скидкой", "оптом", "подарить" and other Russian commercial intent qualifiers
- **Yandex Wordstat reference**: Cross-check monthly поисковые показов via Yandex Wordstat (web_fetch)
- **Russian seasonal trend detection**: 12-month Google Trends RU + Yandex Trends
- **Market opportunity scoring**: 1-10 score combining Ozon listing density, price room, demand signals, and Russian commercial intent
- **Multi-marketplace**: Ozon.ru (Russia, main), Ozon.kz (Kazakhstan), Ozon.by (Belarus)
- **Russian keyword categorization**: Group by commercial intent (купить / best / cheap / для / подарить) vs informational vs niche long-tail
- **Declension expansion**: Auto-generate Russian noun cases (именительный, родительный, дательный, винительный, творительный, предложный) and plural forms — critical for Russian SEO coverage

## Usage Examples

Users can ask naturally. Examples:

```
研究 Ozon 上"беспроводные наушники"关键词机会
```

```
Research the keyword "планшет для рисования" on Ozon.ru
```

```
Find long-tail Russian keywords for "электрическая зубная щётка"
```

```
I want to sell "мужские кроссовки" on Ozon. What does the keyword landscape look like?
```

```
Compare "робот-пылесос" vs "вертикальный пылесос" on Ozon — which has more opportunity?
```

```
Analyze "подарок женщине" on Ozon — сезонный спрос?
```

```
Build a Russian keyword list for "беспроводные наушники" with all declensions + commercial prefixes
```

## Why Russian Keywords Are Different

Amazon keyword research is straightforward — one language, one set of buyer behaviors. Ozon keyword research has additional layers:

1. **Russian noun declension (падежи)**: A single noun like "наушники" has 12+ forms used in different query contexts. Missing the right case = missing search volume.
2. **Russian commercial intent qualifiers**: Buyers prefix queries with купить / недорого / со скидкой / оптом / подарить. These qualifiers reveal intent and must be a primary keyword source.
3. **Cyrillic vs transliteration**: Many Chinese / Korean / Japanese products are searched both in Cyrillic ("беспроводные наушники") and transliteration ("блютуз наушники"). Both must be covered.
4. **Yandex dominates over Google**: For Russian-language queries, Yandex Wordstat is more representative than Google Keyword Planner. Always validate Russian volume on Yandex.
5. **Yandex.Direct auction data**: Yandex.Direct "прогноз бюджета" tool reveals approximate monthly shows for any keyword — closer to truth than Google Trends for RU market.

## Workflow

### Step 1: Generate Russian Keyword Variations

Run the bundled script to generate long-tail variations from a Russian seed:

```bash
python <skill>/scripts/ozon_keyword_expand.py "беспроводные наушники" --declensions --prefixes
```

**Parameters:**
- `keyword` (required): Russian seed keyword
- `--marketplace` (optional): `ru` (default), `kz`, `by`
- `--declensions` (flag): auto-add Russian noun cases (падежи) and plurals
- `--prefixes` (flag): add Russian commercial intent prefixes
- `--suffixes a-z` (optional): alphabet suffix expansion
- `--output` (optional): save to JSON / TXT / CSV

**What the script does:**
- Takes your Russian seed keyword
- Optionally expands to all 12+ Russian noun forms (купить наушники / наушников / наушникам / наушниками / о наушниках / наушник / наушники / наушников / etc.)
- Adds commercial intent prefixes: купить / лучший / недорогой / для / со скидкой / оптом / подарить / хороший / качественный / новый
- Adds common Russian qualifiers: для дома / для детей / для женщин / для мужчин / для кухни / для спорта / профессиональный / беспроводной / складной / компактный
- Optionally expands with alphabet suffixes for niche long-tail
- Outputs deduplicated list

**Example:**
```bash
python <skill>/scripts/ozon_keyword_expand.py "беспроводные наушники" --declensions --prefixes
# Returns 100-300 Russian keyword variants
```

### Step 2: Validate Demand with Yandex Wordstat

Use `web_fetch` to verify monthly search volume on Yandex Wordstat:

```
https://wordstat.yandex.ru/?q=беспроводные+наушники
```

What to extract:
- "показов в месяц" (monthly shows) — primary demand signal
- Related searches (похожие запросы) — additional keywords
- Search history (история запросов) — seasonal pattern
- Geographic distribution — Russia / Moscow / Saint Petersburg vs regions

> **Note**: Yandex Wordstat may show "0" or require JS interaction for exact numbers. Use `web_search` as fallback: `"[keyword]" wordstat.yandex.ru показов` or check Yandex.Direct прогноз.

### Step 3: Analyze Ozon Competition

Use `web_search` + `web_fetch` to gather Ozon-specific intelligence:

1. Search `"<keyword>" site:ozon.ru` — note approximate result count for listing density
2. Search `"<keyword>" ozon.ru цена отзывы рейтинг` — extract price patterns, rating averages
3. Search `"купить <keyword>" ozon` — verify the commercial intent query returns Ozon results
4. Check Ozon bestseller / category pages for the keyword

**Competition metrics:**
- Total listings (density on Ozon.ru)
- Price range (мин / средний / макс ₽)
- Average rating (4.0+ is healthy; below 4.0 = weak seller landscape)
- Top brands by visibility
- FBO coverage (FBO listings get Доставка завтра badge — high = competitive)
- Russian-language description quality (Chinese MTL = opportunity for native Russian sellers)

### Step 4: Check Russian Seasonality

Use `web_fetch` on Google Trends RU:

```
https://trends.google.com/trends/explore?q=беспроводные+наушники&geo=RU
```

Or Yandex Wordstat history for the past 24 months.

Identify:
- Russian seasonal peaks (Новый Год Декабрь, 23 февраля, 8 марта, 1 сентября, Black Friday Ноябрь)
- Long cold winter structural tailwind (Ноябрь–Март)
- Summer dip / year-end peak pattern
- Year-over-year growth

### Step 5: Synthesize Report

Combine all data into the structured output below.

## Output Format

Present the final report in this structure:

```
## Ozon Keyword Research Report: [keyword]
**Marketplace:** Ozon.ru
**Date:** [current date]

### 1. Russian Long-tail Keywords ([count] found)

**High Commercial Intent (Russian):**
- купить [keyword]
- [keyword] недорого
- [keyword] со скидкой
- [keyword] оптом
- ...

**Declension Variants (Russian noun cases):**
- Именительный: [keyword]
- Родительный: [keyword+а/я/и/ов]
- Дательный: [keyword+у/ю/ам/ям]
- ...

**Common Russian Qualifiers:**
- [keyword] для дома
- [keyword] для детей
- [keyword] для женщин / мужчин
- [keyword] профессиональный
- ...

**Transliteration / Brand Variants:**
- [transliteration if applicable]
- ...

**Niche / Specific Long-tail:**
- [long specific Russian queries]
- ...

### 2. Demand Validation (Yandex Wordstat)

| Variant | Monthly показов | Trend |
|---------|---------------|-------|
| [keyword] base | XXX,XXX | ↗️ rising |
| купить [keyword] | XX,XXX | → stable |
| [keyword] недорого | XX,XXX | ↘️ declining |
| ... |

### 3. Ozon Competition Landscape

| Metric | Value |
|--------|-------|
| Estimated Ozon listings | [number] |
| Price range | ₽[min] - ₽[max] |
| Average price | ₽[avg] |
| Average rating | [stars] |
| FBO coverage | XX% |
| Top brands | [brand1, brand2, brand3...] |
| Russian content quality | [Strong / Mixed / Weak] |

### 4. Russian Seasonal Trends

[Describe 12-month trend: peaks, valleys, stable periods]
[Note НГ, 23 февраля, 8 марта, 1 сентября, Black Friday peaks]

### 5. Market Opportunity Score: [X/10]

**Score breakdown:**
- Russian demand: [low/medium/high] — [wordstat показов]
- Ozon competition density: [low/medium/high] — [listing count]
- Price room: [low/medium/high] — [price spread analysis]
- Russian commercial intent match: [low/medium/high] — [купить + declension coverage]
- Niche potential: [low/medium/high] — [long-tail gap]

**Recommendation:** [1-2 sentence actionable recommendation]
```

## Multi-Keyword Comparison

When the user asks to compare 2+ keywords:

```
Compare "робот-пылесос" vs "вертикальный пылесос" vs "моющий пылесос" on Ozon
```

Run the full workflow (Steps 1-4) for each, then present:

| Metric | робот-пылесос | вертикальный пылесос | моющий пылесос |
|--------|--------------|---------------------|----------------|
| Russian keyword count | — | — | — |
| Yandex Wordstat baseline | — | — | — |
| Avg Ozon price | — | — | — |
| Top brand dominance | — | — | — |
| Russian trend | — | — | — |
| Opportunity score | — | — | — |

End with **Recommendation**.

## Integration with Other Ozon Skills

- **$ozon-product-research**: Use product research first to identify candidate products, then use this skill for keyword expansion.
- **$ozon-listing-optimization**: Feed the keyword list from this skill into listing creation for maximum coverage in Russian listings.

## Limitations

This skill uses publicly available data (Yandex Wordstat + Ozon search + web search). It does not provide Ozon-internal search volume or Ozon advertising analytics. For deeper analytics, integrate with MPStats, Moneyplace, or SellerExpert.
