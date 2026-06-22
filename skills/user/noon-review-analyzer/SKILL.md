---
name: noon-review-analyzer
description: "Deep noon review analysis for competitive intelligence and product improvement. Extract Arabic + English review sentiment, recurring complaints, MENA-specific feature requests (e.g. voltage 220V, Arabic packaging, halal certification), star decay over rolling 90-day windows, competitor weaknesses from negative reviews, and Ramadan/Eid seasonal review patterns. Distinguishes between FBN and FBM review patterns (FBM reviews often mention shipping). Use when the user asks about noon review analysis, Arabic review mining, MENA customer feedback patterns, noon competitor weaknesses from reviews, what MENA buyers complain about, or how to improve a product based on noon reviews."
metadata: {"category":"noon","locale":"mena"}
---

# noon Review Analyzer

Turn Arabic + English noon reviews into actionable product, listing, and supply-chain improvements.

## Capabilities

- **Bilingual sentiment extraction**: Arabic (MSA + dialect) and English sentiment scoring
- **Topic clustering**: group reviews by complaint / praise topic (shipping, quality, sizing, voltage, smell, taste, packaging)
- **Star decay detection**: rolling 90-day mean rating; flag SKUs where rating is trending down
- **MENA-specific feature requests**: extract demands for voltage 220V, Arabic packaging, halal certification, family-size variants
- **FBN vs FBM pattern detection**: FBM reviews more likely to mention shipping delays, damaged packaging; FBN reviews focus on product itself
- **Competitor weakness mining**: extract negative-review topics of competitors as opportunity signals
- **Reviewer profile inference**: distinguish verified buyer, repeat buyer, top reviewer (helpful-vote weight)
- **Photo / video review mining**: extract visual complaints (color difference, sizing issue, damaged arrival)
- **Hijri-aware seasonal patterns**: review sentiment often shifts around Ramadan / Eid / White Friday

## Workflow

### 1. Pull the review corpus
Last 12 months of reviews for target SKU + top 3 competitors. Include review body (AR + EN), star rating, date, verified-buyer flag, helpful votes.

### 2. Normalize Arabic
- Strip diacritics
- Normalize alef variants
- Detect dialect (KSA / UAE / EG / MSA)
- Translate dialect to MSA before NLP clustering (or cluster in dialect then merge)

### 3. Topic clustering
Common MENA-relevant clusters:
- Size / fit (كبير, صغير, مقاس)
- Color difference (لون, صورة, مختلف)
- Quality (جودة, رخيص, ممتاز)
- Shipping speed (توصيل, شحن, تأخير)
- Packaging (تغليف, علبة, كسر)
- Voltage / plug (فيش, كهرباء, 220)
- Smell / taste (ريحة, طعم, عطر)
- Authenticity (أصلي, تقليد, مزيف)
- Seller response (بائع, رد, خدمة)

### 4. Star decay analysis
Compute rolling 30 / 60 / 90-day mean rating. Flag if 90-day mean is ≥ 0.3 stars below lifetime mean.

### 5. FBN vs FBM pattern
- FBN: praise for speed, criticism for product defects
- FBM: criticism for shipping and packaging, praise for product value

### 6. MENA-specific feature requests
Extract:
- Voltage / plug type (UK 3-pin vs EU 2-pin vs US 2-pin)
- Arabic on packaging / manual
- Halal certification
- Family-size variants
- Local-language customer service

### 7. Competitor weakness mining
Pull negative reviews of top 3 competitors. Cluster top complaints. These are positioning opportunities.

## Output

- **Sentiment summary**: % positive / neutral / negative, AR vs EN split
- **Top 5 complaint topics** with example quotes
- **Top 3 feature requests** with demand estimate
- **Star decay report** (if trending)
- **Competitor weakness matrix**: top 3 complaints per competitor → your positioning
- **Actionable recommendations**: 5 concrete improvements (product, listing, supply chain)

## Quick Mode

If user gives one SKU URL: return sentiment + top 3 complaints + 3 actions only.
