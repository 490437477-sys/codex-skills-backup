---
name: ozon-niche-finder
description: "Profitable niche discovery for the Ozon marketplace. Identifies underserved CIS markets across Ozon.ru, Ozon.kz, and Ozon.by with high Russian-language demand but low seller competition. Analyzes demand vs supply, Russian seasonality, FBO vs FBS fit, EAC compliance friction, COD vs online payment, and RUB price elasticity. Use when the user asks about finding niches on Ozon, Russian blue ocean opportunities, 袨蟹芯薪 胁褘谐芯写薪芯 谢懈 锌褉芯写邪胁邪褌褜, ozon product niche, what to sell on Ozon, CIS market gaps, or 9.1 / New Year seasonal opportunities."
metadata: {"emoji":"馃嚪馃嚭","category":"ozon"}
---

# Ozon Niche Finder

Discover underserved niches across the Ozon marketplace (Ozon.ru, Ozon.kz, Ozon.by). Every evaluation is tuned for CIS reality: Russian-language discovery, FBO/FBS logistics, ruble volatility, EAC certification, and Orthodox / post-Soviet seasonality.

## Capabilities

- **Demand scanning** via Russian Yandex Wordstat, Google Trends (geo: RU / KZ / BY), and Ozon autocomplete
- **Supply density analysis** counting active SKUs per subcategory, Russian private label vs noobrand share
- **Price band mapping** in RUB / KZT / BYN with COD-friendly sweet spot detection
- **FBO vs FBS viability scoring** (size tier, weight, hazmat, cross-border feasibility)
- **Compliance friction check** (EAC certification, GOST-R, country of origin, dual-use items)
- **Seasonality overlay** (New Year, 3.8 Womens Day, 5.9 Victory Day, 9.1 Knowledge Day, 11.11, Black Friday)
- **Competition moat rating** (Wildberries, Yandex Market, SberMegaMarket, AliExpress Russia overflow)
- **Currency arbitrage flags** (CNY / USD cost vs RUB retail, ruble volatility buffer)
- **Cross-border vs local supplier signal** (delivery promise difference indicates origin)

## When to Use

- "Ozon 选品", "ozon 选品", "ozon 选品分析"
- "find niches for Ozon.ru / Ozon.kz / Ozon.by"
- "袨蟹芯薪 胁褘谐芯写薪芯 谢懈 锌褉芯写邪胁邪褌褜"
- "what to sell on Ozon", "Russian market gaps"
- "New Year product ideas Ozon"
- User wants a one-page niche brief for a CIS launch

## Workflow

### Step 1: Pin the Marketplace

Default to **Ozon.ru** (largest GMV, > 90% of Ozon volume) unless the user specifies KZ or BY.

| Market | Currency | VAT | Default locale |
|--------|----------|-----|----------------|
| Ozon.ru | RUB | 20% | ru-RU |
| Ozon.kz | KZT | 12% | ru-KZ / kk-KZ |
| Ozon.by | BYN | 20% | ru-BY / be-BY |

### Step 2: Demand Signal

Run Russian-first queries:

```
[product Russian name] Yandex Wordstat
[product Russian name] Ozon.ru 褌芯锌 锌褉芯写邪卸
Google Trends: filter to RU / KZ / BY, last 12 months
```

Demand threshold: **>= 300 weekly Russian searches** OR clear Yandex Wordstat inflection.

### Step 3: Supply Density

Count active listings in the Ozon subcategory:

- **< 50 active SKUs** -> blue ocean candidate
- **50-300** -> viable with differentiation
- **> 300** -> commodity, skip unless you have a moat

Cross-reference with Wildberries and Yandex Market to detect cross-platform overflow.

### Step 4: Compliance Friction

| Category | Risk | Required |
|----------|------|----------|
| Electronics, appliances | Medium | EAC + GOST-R |
| Toys, kids products | Medium | EAC + Customs Union TR |
| Cosmetics, personal care | Medium | EAC + safety assessment |
| Food, supplements | High | EAC + Rosselkhoznadzor (vet) / Rospotrebnadzor |
| Apparel, textiles | Low | EAC label + country of origin |
| Jewelry, precious metals | High | Assay chamber + GOST |
| Auto parts | Medium | EAC + vehicle type approval |
| Software, media | High | EAC + content rating |

Reject niches with EAC + Rospotrebnadzor gating unless the user has a local compliance partner.

### Step 5: FBO vs FBS Viability

Default to **FBS** (Fulfilled by Seller) for cross-border sellers shipping from China. FBO requires inventory in Russian warehouses, which adds complexity and ruble exposure.

Reject categories where FBS economics break:

- **Too large / heavy** (> 25 kg) -> only FBO with pallet
- **Perishable / hazmat** -> need special FBO storage
- **Customs-sensitive** (food, supplements) -> FBO at Russian warehouse after customs clearance

### Step 6: Seasonality Overlay

Map demand peaks. **New Year (Dec 25 - Jan 8)** is the largest retail spike in Russia, often 3-5x normal. Plan inventory 60-90 days before. **3.8 Womens Day** is the second-biggest spike, dominated by flowers, jewelry, cosmetics, gifts.

### Step 7: Niche Score

Each niche gets a score 1-10:

```
Score = (Demand x 0.30) + (Supply_gap x 0.25)
      + (Margin x 0.20) + (Compliance_ease x 0.15)
      + (FBO_FBS_fit x 0.10)
```

**>= 7.5** -> top-tier launch candidate
**6.0-7.5** -> viable, needs differentiation
**< 6.0** -> skip

## Output

A one-page brief per niche:

| Field | Content |
|-------|---------|
| Niche name (RU + EN) | e.g. 蟹邪褉褟写薪邪褟 锌谢懈褌邪 / charging station |
| Best market | Ozon.ru / Ozon.kz / Ozon.by |
| Demand signal | Yandex Wordstat volume + trend direction |
| Supply density | Active SKU count + top 5 competitors |
| Compliance | EAC category, time + cost |
| FBO/FBS tier | recommendation + reasoning |
| Estimated margin | After Ozon commission, FBO fees, returns, COD bounce |
| Seasonality | Peak months, New Year effect |
| Score | 1-10 with breakdown |
| Risks | Top 3 blockers |
| Next steps | First 3 actions |

## Quick Mode

If the user only asks "is X a good niche on Ozon?", deliver:

1. Score 1-10
2. Top 3 risks
3. Top 3 actions to de-risk

Skip the full brief unless the user asks for it.
