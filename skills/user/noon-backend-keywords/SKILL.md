---
name: noon-backend-keywords
description: "Optimize noon backend search terms (also called search keywords or generic keywords) for maximum Arabic + English discoverability. Generate the optimal backend keyword set by deduplicating from the visible listing, balancing Arabic MSA + dialect (KSA/UAE/EG) variants, removing competitor brand names, and respecting noon character limit per locale. Use when the user asks about noon backend keywords, noon search terms, Arabic keyword optimization, noon SEO, noon hidden keywords field, or MENA keyword variants."
metadata: {"category":"noon","locale":"mena"}
---

# noon Backend Keywords

Tune noon hidden search-term fields so Arabic-dialect searchers discover the listing even when the visible Arabic / English copy does not include their exact words.

## Capabilities

- **Locale-aware dedup** vs visible Arabic title, bullets, description, brand
- **Dialect coverage**: MSA + KSA + UAE + Egypt variants (e.g. mobile vs موبايل vs تليفون vs موبيل)
- **Brand safety**: detect competitor brand names that may trigger suppression; flag for removal
- **No-spam compliance**: avoid repeated words, subjective claims (best, cheap), temporary adjectives (2026 new)
- **Character optimization** to fill the backend keyword field efficiently per marketplace
- **Cross-script handling**: Arabic, Latin, transliteration (e.g. airfryer, قلاية هوائية)
- **Hijri-aware seasonal terms**: رمضان, عيد الفطر, etc. for demand peaks

## Workflow

### 1. Extract visible terms
Pull every word from title + bullets + description in both Arabic and English. Normalize diacritics, alef variants (إ/أآا → ا), taa marbuta (ة → ه).

### 2. Generate candidate set
Sources:
- noon autocomplete for the seed term (AR + EN)
- Google Trends related queries (geo: SA, AE, EG)
- Buyer language from review mining
- Common misspellings (Latin transliteration of Arabic)

### 3. Filter
- Drop any word already in visible copy
- Drop competitor brands (Amazon, Namshi, noon, Carrefour, etc.)
- Drop subjective adjectives (best, cheap, top)
- Drop size/weight/color if not differentiating
- Drop brand names of major electronics/cosmetics (Apple, Samsung, LOreal) unless the SKU is OEM

### 4. Normalize
- Convert all to lowercase Latin OR lowercase Arabic (do not mix)
- Single space between words, no commas
- No repeated words

### 5. Order
Put highest-volume dialect terms first. noon weights earlier tokens more.

### 6. Length check

| Marketplace | Backend field limit |
|-------------|---------------------|
| noon.sa     | 250 bytes           |
| noon.ae     | 250 bytes           |
| noon.com    | 200 bytes           |

UTF-8 Arabic characters = 2 bytes each. Compute accurately.

## Output

Final backend keyword string + a brief explanation:
- Total bytes used / limit
- Dialect coverage: MSA / KSA / UAE / EG
- Top 5 search-volume terms included
- Words intentionally excluded (with reason)

## Quick Mode

If user pastes visible copy: return only the optimized backend string.
