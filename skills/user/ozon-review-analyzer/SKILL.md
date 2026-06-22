---
name: ozon-review-analyzer
description: "Deep Ozon review analysis for competitive intelligence and product improvement. Extract Russian-language review sentiment, recurring complaints, CIS-specific feature requests (e.g. voltage 220V, Cyrillic packaging, cold-weather variants), star decay over rolling 90-day windows, competitor weaknesses from negative reviews, and seasonal review patterns. Distinguishes between FBO and FBS review patterns. Use when the user asks about Ozon review analysis, Russian review mining, 芯褌蟹褘胁褘 蟹邪泻邪蟹褔懈泻芯胁 analysis, what Russian buyers complain about, or how to improve a product based on Ozon reviews."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Review Analyzer

Turn Russian + CIS reviews into actionable product, listing, and supply-chain improvements.

## Capabilities

- **Russian sentiment extraction**: handle transliterated Russian, mixed-language reviews, sarcasm
- **Topic clustering**: group reviews by complaint / praise topic
- **Star decay detection**: rolling 90-day mean rating; flag SKUs where rating is trending down
- **CIS-specific feature requests**: extract demands for Cyrillic packaging, cold-weather variants, dual-voltage, etc.
- **FBO vs FBS pattern detection**: FBM reviews more likely to mention shipping delays, damaged packaging
- **Competitor weakness mining**: extract negative-review topics of competitors as opportunity signals
- **Reviewer profile inference**: distinguish verified buyer, repeat buyer, top reviewer (helpful-vote weight)
- **Photo / video review mining**: extract visual complaints (color difference, sizing issue, damaged arrival)
- **Seasonal patterns**: review sentiment often shifts around New Year / 3.8 / 9.1

## Workflow

### 1. Pull the review corpus
Last 12 months of reviews for target SKU + top 3 competitors. Include review body (RU), star rating, date, verified-buyer flag, helpful votes.

### 2. Normalize Russian
- Handle soft sign (褜) and hard sign (褜) consistently
- Detect transliterated Russian (Latin chars used to write Russian words)
- Normalize yo (械 vs 械) variations
- Translate slang to standard Russian before NLP clustering

### 3. Topic clustering
Common Russian-relevant clusters:
- Size / fit (褉邪蟹屑械褉, 屑邪谢, 斜芯谢褜褕芯泄)
- Color difference (褑胁械褌, 芯褌谢懈褔邪械褌褋褟)
- Quality (泻邪褔械褋褌胁芯, 写械褕械胁芯, 锌谢芯褏芯泄)
- Shipping speed (写芯褋褌邪胁泻邪, 写芯谢谐芯, 斜褘褋褌褉芯)
- Packaging (褍锌邪泻芯胁泻邪, 泻芯褉芯斜泻邪, 锌芯胁褉械卸写械薪芯)
- Voltage / plug (胁懈谢泻邪, 褉芯蟹械褌泻邪, 220)
- Smell / taste (蟹邪锌邪褏, 胁泻褍褋, 邪褉芯屑邪褌)
- Authenticity (芯褉懈谐懈薪邪谢, 锌芯写写械谢泻邪, 褉械锌谢懈泻邪)
- Seller response (锌褉芯写邪胁械褑, 芯褌胁械褌, 芯斜褋谢褍卸懈胁邪薪懈械)

### 4. Star decay analysis
Compute rolling 30 / 60 / 90-day mean rating. Flag if 90-day mean is >= 0.3 stars below lifetime mean.

### 5. FBO vs FBS pattern
- **FBO**: praise for speed, criticism for product defects
- **FBS**: criticism for shipping and packaging, praise for product value
- **Cross-border from CN**: criticism for long shipping, praise for low price

### 6. CIS-specific feature requests
Extract:
- Voltage / plug type (EU 2-pin / Type C / Type F)
- Cyrillic on packaging / manual / app
- Cold-weather variants (-20C capable)
- Russian-language customer service
- Local warranty service centers
- Family-size variants (Russian households average 2.5-3 people but often buy larger)

### 7. Competitor weakness mining
Pull negative reviews of top 3 competitors. Cluster top complaints. These are positioning opportunities.

## Output

- **Sentiment summary**: % positive / neutral / negative, RU vs other language split
- **Top 5 complaint topics** with example quotes
- **Top 3 feature requests** with demand estimate
- **Star decay report** (if trending)
- **Competitor weakness matrix**: top 3 complaints per competitor -> your positioning
- **Actionable recommendations**: 5 concrete improvements (product, listing, supply chain)

## Quick Mode

If user gives one SKU URL: return sentiment + top 3 complaints + 3 actions only.
