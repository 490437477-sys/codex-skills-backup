---
name: mercado-negative-keywords
description: "Optimize Mercado Ads campaigns on Mercado Libre 美客多 by identifying and managing negative keywords. Reduce wasted ad spend on PADS (Productos Ads), Display retargeting, and Brand ads (MLB only) by eliminating irrelevant Spanish and Portuguese search terms while protecting high-converting terms. Includes brand-defense negatives to block competitor bidding, color and size mismatches, free-shipping-misquery negatives, and seasonal negative cleanup before Hot Sale, Buen Fin, Black Friday, Navidad, Dia de las Madres, Carnaval. Use when the user mentions 美客多否定关键词, 美客多否词, palabras clave negativas mercado ads, palavras-chave negativas mercado ads, reduce wasted spend PADS, exclude irrelevant searches Mercado Libre, Mercado Ads ACoS too high, 美客多广告ROI, exclude brand competitor MLM MLB."
metadata: {"category":"mercado","emoji":"🌎🌎"}
---

# Mercado Libre Negative Keywords 🌎🌎

Cut wasted spend on Mercado Ads by blocking irrelevant Spanish and Portuguese search terms before they drain budget. Protect every keyword that actually converts.

## When to Use

Activate this skill whenever the user mentions:
- 美客多否定关键词, 美客多否词, 美客多广告否词, 美客多否定
- Mercado Libre negative keywords, Mercado Ads negatives
- Palabras clave negativas mercado ads, excluir terminos Mercado Libre
- Palavras-chave negativas mercado ads, excluir buscas MLB
- Reduce wasted spend PADS, ACoS too high Mercado Libre
- My Mercado Ads campaign is bleeding budget on wrong searches
- Brand-defense negatives, exclude competitor brand MLM MLB
- Seasonal cleanup before Hot Sale, Buen Fin, Black Friday

## Capabilities

- **Search-term mining**: Pull the last 90-day search-term report from seller.mercadolibre.com and bucket terms by impressions, clicks, CTR, conversions, CPA
- **Zero-converter detector**: Flag terms with 200+ impressions and 0 conversions over 30 days as primary negative candidates
- **Intent-mismatch negatives**: Exclude free-shipping-misquery terms (gratis, free, envio gratis when product is not Mercado Envios gratis), wrong color, wrong size, wrong gender, wrong model variants
- **Brand-defense negatives**: Add competitor brand names, OEM brand, and top-3 seller nicknames as exact-match negatives so your ads never serve on their brand searches
- **Cross-locale negatives**: Separate Spanish and Portuguese stop-word sets (que, para, con, com, para, sem) and locale-specific false-intent phrases
- **Seasonal negatives**: Before Hot Sale Mexico, Buen Fin, Black Friday, Navidad, Dia de las Madres, Carnaval pre-emptively exclude bargain-only terms that burn budget on non-buyers
- **Match-type discipline**: Choose exact, phrase, or broad negatives. Default exact. Promote to phrase only when intent-mismatch spans word variants

## Workflow

### Step 1: Pull Search-Term Report

Inside seller.mercadolibre.com open Mercado Ads campaign manager. Export the last 90-day search-term report per PADS campaign. Add Display and Brand ads reports if active.

### Step 2: Bucket by Performance

Sort terms into four quadrants:
1. High impressions, 0 conversions (waste)
2. High impressions, low conversion rate under 2 percent (mismatch)
3. Conversions present, ACoS above category ceiling (over-bid)
4. Strong converters (protected, do not negate)

### Step 3: Compose Negative Lists

For each quadrant build the matching negative list:
- Quadrant 1: exact-match negatives
- Quadrant 2: phrase-match negatives to catch inflections
- Quadrant 3: keep but lower bid, do not negate
- Quadrant 4: protected, document why

### Step 4: Apply Localization

For each negative term generate Spanish + Portuguese inflections, accent variants, and country-specific synonyms (audifonos vs auriculares vs cascos). Apply per-marketplace since MLM and MLC share Spanish but differ in usage.

### Step 5: Brand-Defense Layer

Add exact-match negatives for your top 5 brand competitors in the category. Add your own brand variations only if running a separate brand-defense campaign.

### Step 6: Seasonal Cleanup

Two weeks before Hot Sale, Buen Fin, Black Friday, Navidad, Dia de las Madres, Carnaval add seasonal false-intent negatives (barato, gratis, regalo, oferta, liquidacion when you are not running a deal). Lift them again after the event.

### Step 7: Refresh Cadence

Re-pull the search-term report every 14 days. Any term crossing 500 impressions with 0 conversions moves to the negative list automatically.

## Output Format

| Negative term | Match type | Locale | Reason | Source |
|---|---|---|---|---|
| audifonos gamer | exact | MLM | Wrong intent | Search-term report |
| frete gratis sp | phrase | MLB | Free-shipping misquery | Manual |
| Samsung OEM | exact | MLB | Brand defense | Competitor list |
| barato | phrase | MLM | Seasonal pre-Hot Sale | Event calendar |
| audifonos rosa | exact | MLM | Wrong color variant | Listing data |

## Quick Mode

Provide the marketplace (MLM / MLB / MLC / MCO) and product category. Output a starter negative keyword list of 30-50 terms covering intent-mismatch, brand-defense, and seasonal patterns in under 45 seconds.
