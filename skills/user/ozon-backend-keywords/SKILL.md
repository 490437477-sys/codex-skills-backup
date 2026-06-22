---
name: ozon-backend-keywords
description: "Optimize Ozon backend search terms (used in product description and category attributes) for maximum Russian + CIS discoverability. Generate the optimal keyword set by deduplicating from the visible listing, balancing Russian MSA + colloquial variants, removing competitor brand names, and respecting Ozon character limits. Use when the user asks about Ozon backend keywords, Ozon search terms, Russian keyword optimization, Ozon SEO, 芯锌褌懈屑懈蟹邪褑懈褟 泻谢褞褔械胁褘褏 褋谢芯胁, or CIS keyword variants."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Backend Keywords

Tune Ozon hidden search-term fields so Russian-colloquial searchers discover the listing even when the visible Russian copy does not include their exact words.

## Capabilities

- **Locale-aware dedup** vs visible Russian title, bullets, description, brand
- **Russian variant coverage**: MSA + colloquial + transliterated forms
- **Brand safety**: detect competitor brand names that may trigger suppression; flag for removal
- **No-spam compliance**: avoid repeated words, subjective claims (谢褍褔褕懈泄, 写械褕械胁芯), temporary adjectives
- **Character optimization** to fill the backend keyword field efficiently
- **Cross-script handling**: Russian Cyrillic, Latin transliteration, common abbreviations
- **Seasonal terms**: 薪芯胁褘泄 谐芯写, 8 屑邪褉褌邪, 写械薪褜 锌芯斜械写褘, etc.

## Workflow

### 1. Extract visible terms
Pull every word from title + bullets + description in Russian. Normalize yo (械 vs 械), lowercase.

### 2. Generate candidate set
Sources:
- Ozon autocomplete for the seed term (RU)
- Yandex Wordstat related queries
- Buyer language from review mining
- Common misspelling patterns

### 3. Filter
- Drop any word already in visible copy
- Drop competitor brands (Wildberries, Yandex Market, Ozon, Sber, etc.)
- Drop subjective adjectives (谢褍褔褕懈泄, 写械褕械胁芯, 谢褍褔褕懈泄 胁 褋胁芯械屑 泻谢邪褋褋械)
- Drop size/weight/color if not differentiating
- Drop brand names of major electronics/cosmetics (Samsung, Apple, L'Oreal) unless the SKU is OEM

### 4. Normalize
- Convert all to lowercase Cyrillic (do not mix scripts)
- Single space between words, no commas
- No repeated words

### 5. Order
Put highest-volume search terms first. Ozon weights earlier tokens more.

### 6. Length check

| Field | Limit |
|-------|-------|
| Title | 80 characters recommended (up to 200 max) |
| Description | 500-2000 characters |
| Category attributes | varies per category |

## Output

Final backend keyword string + a brief explanation:
- Total characters used
- Variant coverage: MSA / colloquial / transliterated
- Top 5 search-volume terms included
- Words intentionally excluded (with reason)

## Quick Mode

If user pastes visible copy: return only the optimized keyword string.
