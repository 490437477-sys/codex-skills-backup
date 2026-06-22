---
name: noon-niche-finder
description: "Profitable niche discovery for the noon marketplace. Identifies underserved MENA markets across noon.sa, noon.ae, and noon.com with high Arabic-language demand but low local-seller competition. Analyzes demand vs supply, Ramadan/Eid seasonality, FBN viability, SASO/SFDA/ESMA compliance friction, COD vs prepaid split, and SAR/AED/EGP price elasticity. Use when the user asks about finding niches on noon, MENA blue ocean opportunities, Arabic product demand, White Friday niches, Ramadan product opportunities, Saudi/UAE/Egypt market gaps, or what to sell on noon."
metadata: {"category":"noon","locale":"mena"}
---

# noon Niche Finder

Discover underserved niches across the noon marketplace (noon.sa, noon.ae, noon.com). Every evaluation is tuned for MENA reality: Arabic-first discovery, FBN logistics, religious seasonality, and regulatory friction.

## Capabilities

- **Demand scanning** via Arabic keyword volume, Google Trends (geo: SA/AE/EG), and noon autocomplete
- **Supply density analysis** counting active SKUs per subcategory, private-label vs noobrand share
- **Price band mapping** in SAR / AED / EGP with COD-eligible sweet spot detection
- **FBN viability scoring** (size tier, weight, hazmat, returns rate)
- **Compliance friction check** (SASO, SFDA, ESMA, GOEIC, IECEE)
- **Seasonality overlay** (Ramadan / Eid / Hajj / back-to-school / White Friday / National Day)
- **Competition moat rating** (Amazon.ae/sa cross-border, Namshi, Ounass, 6thStreet overflow)
- **Currency arbitrage flags** (USD cost vs SAR/AED/EGP retail)

## When to Use

- "noon选品", "中东卖什么", "noon 沙特蓝海"
- "find niches for noon.sa / noon.ae / noon.com"
- "斋月卖什么", "White Friday 选品"
- User wants a one-page niche brief for a MENA launch
- User wants to compare opportunity across all three noon markets

## Workflow

### Step 1: Pin the Marketplace

Default to **noon.sa** (largest GMV) unless the user specifies UAE or Egypt. Different VAT and fee schedules apply:

| Market | Currency | VAT | Default locale |
|--------|----------|-----|----------------|
| noon.sa | SAR | 15% | ar-SA |
| noon.ae | AED | 5% | ar-AE / en-AE |
| noon.com | EGP | 14% | ar-EG / en-EG |

### Step 2: Demand Signal

Run Arabic-first queries:

```
"[product Arabic name]" موقع نون
"[product English name]" noon.sa الأكثر مبيعاً
"[product]" buy online KSA
Google Trends: filter to SA / AE / EG, last 12 months
```

Demand threshold: **≥ 200 weekly Arabic searches** OR clear Google Trends inflection.

### Step 3: Supply Density

Count active listings in the noon subcategory:

- **< 30 active SKUs** → blue ocean candidate
- **30–200** → viable with differentiation
- **> 200** → commodity, skip unless you have a moat

Cross-reference with Amazon.ae/sa to detect cross-border overflow.

### Step 4: Compliance Friction

| Category | Risk | Required |
|----------|------|----------|
| Cosmetics, skincare | High | SFDA notification |
| Food, supplements | High | SFDA + SASO |
| Electronics, batteries | Medium | IECEE / SASO IECEE |
| Toys, kids | Medium | SASO + GCC conformity |
| Apparel, textiles | Low | Care label + country of origin |
| Home, kitchen | Low | SASO only for electrical |

Reject niches with SFDA/IECEE gating unless the user has a local importer partner.

### Step 5: FBN Viability

Reject categories where FBN economics break:

- **Too heavy (> 15 kg)** → only FBM
- **Too fragile (glass / liquids)** → high return rate in COD markets
- **Hazmat (perfume, lithium battery)** → FBN restrictions apply
- **Cold chain (chocolate, supplements)** → FBN rejects

### Step 6: Seasonality Overlay

Map demand peaks. **Ramadan** is the largest retail spike in the region — anything food, gifting, home, or family-oriented moves +200–400%. Plan inventory 60 days before Ramadan starts.

### Step 7: Niche Score

Each niche gets a score 1–10:

```
Score = (Demand × 0.30) + (Supply_gap × 0.25)
      + (Margin × 0.20) + (Compliance_ease × 0.15)
      + (FBN_fit × 0.10)
```

**≥ 7.5** → top-tier launch candidate
**6.0–7.5** → viable, needs differentiation
**< 6.0** → skip

## Output

A one-page brief per niche:

| Field | Content |
|-------|---------|
| Niche name (EN + AR) | e.g. Air fryer accessories / إكسسوارات القلاية الهوائية |
| Best market | noon.sa / noon.ae / noon.com |
| Demand signal | Volume + trend direction |
| Supply density | Active SKU count + top 5 competitors |
| Compliance | Required certifications, time + cost |
| FBN tier | Small / Medium / Large / XL |
| Estimated margin | After FBN fees, returns, COD bounce |
| Seasonality | Peak months, Ramadan effect |
| Score | 1–10 with breakdown |
| Risks | Top 3 blockers |
| Next steps | First 3 actions |

## Quick Mode

If the user only asks "is X a good niche on noon?", deliver:

1. Score 1–10
2. Top 3 risks
3. Top 3 actions to de-risk

Skip the full brief unless the user asks for it.
