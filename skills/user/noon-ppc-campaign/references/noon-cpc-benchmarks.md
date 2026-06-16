---
name: noon-cpc-benchmarks
version: 1.0.0
description: "CPC and ACoS benchmarks for noon Ads across KSA, UAE, and Egypt by category. Covers Auto vs Manual bid ranges, ACoS targets by phase (launch / scale / mature), B2B CPC premium, and Hijri-season inflation factors. Use when setting initial bids, calibrating ACoS targets, or evaluating campaign performance against MENA-market norms. Disclaimer: noon does not publish public CPC data; ranges are mid-2024 to 2025 estimates from third-party MENA ad reports and practitioner surveys."
metadata: {"category":"noon","locale":"mena"}
---

# noon Ads CPC & ACoS Benchmarks (MENA)

> noon does **not** publish public CPC data. These ranges are mid-2024 to 2025 estimates from third-party MENA e-commerce ad reports, practitioner surveys, and noon Seller Central observations. Use as **starting reference points**, not absolute truth. Always validate with your own 14-day A/B test before scaling.

## Why MENA Benchmarks Differ from Amazon

| Dimension | Amazon (US) | noon (KSA/UAE/EGY) | Why it matters |
|-----------|-------------|---------------------|----------------|
| Avg CPC (Electronics) | $0.80-1.50 USD | SAR 0.50-2.00 (USD 0.13-0.53) | Lower CPCs = can be profitable at lower AOV |
| Avg CPC (Toys/Hobby) | $0.50-1.20 USD | SAR 0.30-1.20 (USD 0.08-0.32) | Same |
| ACoS target | 15-30% | **20-40%** | Lower CVR + higher returns reserve |
| CVR baseline | 8-12% | **2-5%** | Browsing-heavy, lower trust |
| Search volume | High (millions) | Medium (10K-500K per term) | Smaller keyword universe |
| Arabic vs English split | English only | 60-70% Arabic, 30-40% English | Bilingual required |
| Auction type | 2nd-price | **1st-price** | Bid calibration matters more |

**Key tactical shift:** noon CVR is 2-3x lower than Amazon. A 5% ACoS on Amazon often means 15-25% ACoS on noon for the same product, just due to lower conversion efficiency.

## CPC Ranges by Category (SAR / AED / EGP)

> Ranges shown as **min - typical - max** (in local currency). Multiply by 1.0 for SAR/AED (1:1 peg), divide by ~13 for EGP approximation.

### Electronics & DIY (your category)

| Sub-category | KSA (SAR) | UAE (AED) | EGY (EGP) | Notes |
|--------------|-----------|-----------|-----------|-------|
| Arduino / MCU kits | 0.80 - 1.80 - 3.50 | 0.80 - 1.80 - 3.50 | 12 - 25 - 50 | Niche Arabic = high CPC |
| Robotics arms / kits | 1.00 - 2.50 - 5.00 | 1.00 - 2.50 - 5.00 | 15 - 35 - 70 | Premium positioning |
| STEM / educational toys | 0.50 - 1.20 - 2.50 | 0.50 - 1.20 - 2.50 | 8 - 18 - 35 | Back-to-school surge |
| 3D printers | 2.00 - 4.00 - 8.00 | 2.00 - 4.00 - 8.00 | 25 - 50 - 100 | Premium buyer, low volume |
| Soldering / tools | 0.30 - 0.80 - 1.50 | 0.30 - 0.80 - 1.50 | 5 - 12 - 25 | Generic, broad traffic |
| Mobiles / accessories | 1.50 - 3.50 - 8.00 | 1.50 - 3.50 - 8.00 | 20 - 45 - 100 | **Highest CPC on noon** |
| Laptops / computers | 1.00 - 2.50 - 6.00 | 1.00 - 2.50 - 6.00 | 15 - 35 - 80 | High AOV, lower CVR |
| Smart home / IoT | 0.80 - 2.00 - 4.00 | 0.80 - 2.00 - 4.00 | 12 - 25 - 50 | Growing category |
| Wearables | 1.00 - 2.50 - 5.00 | 1.00 - 2.50 - 5.00 | 15 - 35 - 70 | Crowded |

### Other Common Categories

| Sub-category | KSA (SAR) | UAE (AED) | EGY (EGP) | Notes |
|--------------|-----------|-----------|-----------|-------|
| Fashion / apparel | 0.20 - 0.60 - 1.50 | 0.20 - 0.60 - 1.50 | 3 - 10 - 25 | Low CPC, high volume |
| Beauty / cosmetics | 0.40 - 1.00 - 2.00 | 0.40 - 1.00 - 2.00 | 6 - 15 - 30 | High CVR |
| Home / kitchen | 0.30 - 0.80 - 1.80 | 0.30 - 0.80 - 1.80 | 5 - 12 - 25 | Strong seasonal |
| Sports / fitness | 0.40 - 1.00 - 2.20 | 0.40 - 1.00 - 2.20 | 6 - 15 - 30 | New Year surge |
| Books / stationery | 0.15 - 0.40 - 0.80 | 0.15 - 0.40 - 0.80 | 3 - 8 - 15 | Back-to-school |
| Auto accessories | 0.50 - 1.20 - 2.50 | 0.50 - 1.20 - 2.50 | 8 - 18 - 35 | Niche buyers |

## ACoS Targets by Phase

| Phase | Timeline | Target ACoS | Strategy | Notes |
|-------|----------|-------------|----------|-------|
| **Launch** | Week 1-2 | 40-60% | High bids to gather data | Spend is investment in learning |
| **Scale** | Week 3-6 | 25-40% | Optimize to profitable range | Daily bid +10/-10 tests |
| **Mature** | Week 7+ | **20-30%** | Maintain efficiency, harvest | Bid only on proven converters |
| **Seasonal peak** | Hijri/Greg events | 30-50% (allow higher) | Volume > efficiency | CPC inflation 40-150% |
| **B2B / Institutional** | School year (Aug-Feb) | 50-80% (acceptable) | LTV-driven, not direct ACoS | One school = 10-50 units |

> **Rule of thumb:** if your break-even ACoS (from `bid_calculator.py`) is 35%, then your target ACoS during scale should be 25-30% to leave room for returns and growth.

## Auto vs Manual Bid Strategy

| Campaign Type | Initial Bid | Day 14 Bid | Strategy |
|---------------|-------------|------------|----------|
| **Auto (Discovery)** | 0.80 SAR | 1.00-1.20 SAR | Start conservative, scale after data |
| **Manual AR (Arabic exact)** | 1.20 SAR | 0.80-1.50 SAR | Bid per keyword by relevance |
| **Manual EN (English exact)** | 1.00 SAR | 0.70-1.20 SAR | Slightly lower, English market is smaller |
| **Brand Defense** | 0.50 SAR | 0.30-0.60 SAR | Low - just defend brand SERP |
| **Institutional (B2B)** | 3.00 SAR | 1.50-4.00 SAR | High - low volume, high LTV |

> noon Auto campaigns have a **single default bid** for all match-type behaviors (close match, loose match, substitutes, complements). Don't try to set per-match-type bids in Auto.

## Bid Strategy Selection (noon Ads)

| Strategy | Best for | Risk |
|----------|----------|------|
| **Fixed bid** | Manual campaigns with proven keywords | No auto-optimization |
| **Dynamic Bid (Down Only)** | Auto campaigns (recommended start) | May underbid in competitive windows |
| **Dynamic Bid (Up & Down)** | Auto campaigns during Hijri peak | **Auto only - never use on Manual** |
| **Don't use Target ACoS** | (noon does not support this) | - |

## Hijri-Season CPC Inflation Factors

| Season | CPC Inflation | Bid Adjustment | Budget Adjustment |
|--------|---------------|----------------|-------------------|
| Ramadan (30 days pre) | +20-30% | +15-20% | +50% |
| Eid al-Fitr (1-2 weeks) | +40-60% | +25-35% | +100% |
| Hajj (3 weeks pre) | +5-10% | No change | No change |
| Eid al-Adha (1 week) | +20-30% | +10-15% | +30% |
| Back-to-school (Aug-Sep) | +30-50% | +20-25% | +80% |
| KSA National Day (Sep 23) | +15-25% | +10-15% | +40% |
| UAE National Day (Dec 2) | +15-25% | +10-15% | +40% |
| White Friday (4-day event) | +80-150% | +30-40% | +200% |
| Islamic New Year | +5-10% | No change | -10 to -20% |

## B2B / Institutional CPC Premium

Institutional (B2B) PPC is a different game:

- **CPC:** 2-3x regular CPCs (e.g., SAR 2.00-5.00 instead of SAR 0.80-1.80)
- **CVR:** 1-3% (lower than B2C)
- **AOV:** 5-20x higher (e.g., SAR 2,000-10,000 for a 10-50 unit school order)
- **LTV:** Recurring annual orders (academic year procurement)

| B2B Keyword | Estimated CPC (KSA) | Estimated AOV | Notes |
|-------------|---------------------|---------------|-------|
| "robotics kit for schools" | 2.50-4.00 SAR | 5,000-15,000 SAR | Procurement officer intent |
| "STEM lab equipment" | 3.00-5.00 SAR | 10,000-50,000 SAR | School / lab buyer |
| "Arduino for students bulk" | 1.50-3.00 SAR | 3,000-8,000 SAR | Teacher / student |
| "robotics training equipment" | 2.00-4.00 SAR | 5,000-20,000 SAR | Training center |
| "STEM education supplier KSA" | 4.00-8.00 SAR | 20,000+ SAR | Distributor / MoE |

> B2B should be a **separate campaign with separate budget pool**. Don't mix B2B and B2C keywords in the same campaign - their economics are too different.

## Arabic vs English CPC Comparison

Arabic terms typically have:
- **+20-40% higher CPC** than English equivalents (smaller Arabic keyword universe = less competition but also less data)
- **Lower CVR** (-30-50% vs English) because fewer Arabic-optimized listings
- **Higher AOV** for B2C (gifting events drive premium purchases)
- **Required for Ramadan/Eid** - English alone misses 60-70% of seasonal gift intent

Recommended split:
- **70% Arabic** in Auto + Manual AR campaigns
- **25% English** in Manual EN campaigns
- **5% Bilingual** (mixed) for cross-over shoppers

## CVR (Conversion Rate) Benchmarks by Category

| Category | KSA CVR | UAE CVR | EGY CVR | Notes |
|----------|---------|---------|---------|-------|
| Electronics / DIY | 1.5-3.0% | 2.0-3.5% | 1.0-2.0% | Lower for high-AOV |
| Robotics / STEM kits | 2.0-4.0% | 2.5-4.5% | 1.5-3.0% | Higher intent buyers |
| Fashion | 1.5-3.5% | 2.0-4.0% | 1.0-2.5% | High browse, low buy |
| Beauty | 2.5-5.0% | 3.0-5.5% | 1.5-3.0% | High CVR category |
| Home / kitchen | 1.5-3.0% | 2.0-3.5% | 1.0-2.0% | Considered purchase |
| Books / stationery | 2.0-4.0% | 2.5-4.5% | 1.5-3.0% | Back-to-school surge |

> Use these as the `--cvr` input in `bid_calculator.py` when computing max CPC.

## Worked Example: 5DOF Metal Arm (KSA)

**Inputs:**
- Marketplace: noon-sa (SAR)
- Selling price: 399 SAR
- Landed cost: 130 SAR
- VAT: 15% (KSA)
- Commission: 10% (electronics default)
- Returns reserve: 5% (electronics)
- Target ACoS: 30% (MENA scale phase)
- CVR assumption: 2.5% (Robotics / STEM range)

**Bid calculator outputs (from `bid_calculator.py`):**
- Net per sale (before ads): SAR 209.15
- Break-even ACoS: **52.42%** (this is your ceiling)
- Target ACoS (30%): allows SAR 119.70 / sale on ads (room for 22% profit margin)
- Max CPC @ 2.5% CVR: **SAR 2.99** (your ceiling for Auto + Manual)
- Recommended initial Auto bid: SAR 1.50-1.80 (50-60% of max CPC)
- Recommended initial Manual AR bid: SAR 1.80-2.39 (60-80% of max CPC)
- Recommended initial Manual EN bid: SAR 1.50-1.95 (50-65% of max CPC)
- Recommended Brand Defense bid: SAR 0.60-0.90 (20-30% of max CPC)
- Recommended Institutional B2B bid: SAR 2.99-4.49 (100-150% of max CPC)

**Tactic:** start Auto at SAR 1.50, harvest converting search terms after 14 days, migrate top 20 to Manual AR campaigns at SAR 1.80-2.39.

## Data Sources & Limitations

- MENA e-commerce ad reports (2024-2025)
- Practitioner surveys from noon seller community
- 1st-party campaign data extrapolations
- noon Seller Central rate sheets (for fees, not CPCs)

**Not included:**
- Real-time bid landscape (no public API)
- Competitor-specific CPCs
- Keyword-level search volume
- Hour-of-day bid data (limited)

For deeper data, use:
- Helium 10 MENA (limited) or similar tools
- Manual search volume probes (run a test campaign for 7 days)
- Direct outreach to noon's seller success team for high-volume sellers

---

_Version 1.0.0 | Platform: noon | Locale: MENA | Coverage: KSA / UAE / EGY_
