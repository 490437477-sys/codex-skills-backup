---
name: mercado-backend-keywords
description: "Optimize Mercado Libre 美客多 backend search terms for maximum discoverability. Mercado Libre backend surfaces in ficha tecnica atributos internos, tags, model number, and brand-line fields. Generate the optimal keyword set by deduplicating against front-end (titulo + ficha tecnica visible), prioritizing Spanish and Portuguese singular + plural + accent variants + synonyms, and formatting for MLM Mexico, MLB Brazil, MLC Chile, MCO Colombia, MLA Argentina. Includes hot-market LATAM events (Hot Sale, Buen Fin, Black Friday, Dia de las Madres, Navidad) embedded as seasonality tags. Use when the user mentions 美客多后台关键词, 美客多搜索词, 美客多 attributes, palabras clave backend mercado libre, palavras-chave backend mercado livre, optimize ficha tecnica tags, hidden keywords MLM, Mercado Libre atributos internos, 美客多关键词补全, backend SEO."
metadata: {"category":"mercado","emoji":"🌎🌎"}
---

# Mercado Libre Backend Keywords 🌎🌎

Fill every hidden search signal on your Mercado Libre listing. Reach buyers who search with synonyms, plurals, regional terms, and seasonal modifiers that never fit in the titulo.

## When to Use

Activate this skill whenever the user mentions:
- 美客多后台关键词, 美客多搜索词, 美客多 attributes, 美客多关键词补全
- Mercado Libre backend keywords, Mercado Libre atributos internos
- Palabras clave backend mercado libre, keywords ocultas MLM
- Palavras-chave backend mercado livre, atributos internos MLB
- Optimize ficha tecnica, hidden keywords Mercado Libre
- My listing does not appear for variant X
- Backend SEO LATAM, MLS search term audit

## Capabilities

- **Front-end dedup**: Compare candidate keywords against existing titulo, ficha tecnica visible fields, and descripcion. Anything already on the front-end is wasted on the backend
- **Singular + plural + accent matrix**: Build the full inflection matrix for Spanish (audifono, audifonos, audifono inalambrico) and Portuguese (fone, fones, fone sem fio). Mercado Libre matches accents as part of the token
- **Synonym expansion per country**: Map regional synonyms across MX CO AR CL PE (audifonos vs auriculares vs cascos) and BR (fone vs headphone vs headset)
- **Modelo / Marca / SKU line enrichment**: Stuff brand-aliases, OEM model numbers, GTIN / EAN, and part numbers into the model and brand-line fields MercadoLibre exposes
- **Ficha tecnica attribute fill**: Recommend the missing ficha tecnica attributes per category (color, material, capacidad, voltaje) which act as secondary search filters
- **Seasonality backend tags**: Embed Hot Sale, Buen Fin, Black Friday, Dia de las Madres, Navidad, Carnaval, Vuelta a Clases so the listing surfaces during LATAM mega-events
- **Character-budget planner**: Stay within Mercado Libre attribute character limits per field (typically 60 chars per ficha tecnica line, 80 chars internal notes) without keyword stuffing

## Workflow

### Step 1: Front-End Audit

Pull current titulo, ficha tecnica, descripcion, and variante names. Build a normalized keyword set already on the front-end. This becomes the dedup blacklist.

### Step 2: Keyword Source Merge

Combine four sources:
1. Output from mercado-keyword-research (autocomplete + MELI Trends)
2. Competitor ficha tecnica mining (top 5 listings for the keyword)
3. Search-term report from Mercado Ads (searchterms report inside seller.mercadolibre.com)
4. Manual seasonal modifier list (Hot Sale, Buen Fin, Navidad, Dia de las Madres)

### Step 3: Inflection & Synonym Expansion

For each base keyword build Spanish + Portuguese inflections, accent-preserved variants, and country-specific synonyms. Dedupe against the front-end blacklist.

### Step 4: Field Allocation

Map keywords to backend-capable fields:
- Modelo / Model: OEM, GTIN, EAN, part number, color code
- Marca / Brand line: brand aliases, OEM brand if reseller
- Atributos internos: generic synonyms, use-case phrases
- Ficha tecnica spec lines: material, capacidad, voltaje, peso, dimensiones
- Compatibilidad / Compatibilidade: device / vehicle / model compatibility list

Stay inside MercadoLibre field character limits. No stuffing.

### Step 5: Seasonality Layer

Before Hot Sale (mid-May MX), Buen Fin (mid-Nov MX), Black Friday, Navidad, Dia de las Madres, Carnaval (BR Feb-Mar) inject the event phrase into a ficha tecnica line so the listing surfaces during mega-event traffic spikes.

### Step 6: Validation & Refresh

Re-list and wait 48-72 hours. Check search-term report inside Mercado Ads seller panel. Drop keywords with zero impressions after 30 days. Refresh quarterly with new MELI Trends data.

## Output Format

| Field | Keyword (example) | Length |
|---|---|---|
| Modelo | Audifono BT-X12 negro OEM | 28 chars |
| Marca line | SoundCore + SoundCore Pro | 24 chars |
| Ficha tecnica line 1 | Inalambrico bluetooth 5.3 | 28 chars |
| Ficha tecnica line 2 | Cancelacion ruido activa ANC | 28 chars |
| Compatibilidad | iPhone Samsung Xiaomi Huawei | 33 chars |
| Seasonal tag | Hot Sale 2026 | 13 chars |

## Quick Mode

Provide the listing URL and target marketplace. Output a complete backend keyword plan in ficha tecnica field-by-field format under 60 seconds.
