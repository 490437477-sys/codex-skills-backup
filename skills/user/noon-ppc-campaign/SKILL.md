---
name: noon-ppc-campaign
version: 1.0.0
description: "noon Ads (Sponsored Products) campaign builder and optimizer for noon.sa (KSA) / noon.ae (UAE) / noon.com (Egypt). Two modes: (A) Build — design a complete campaign structure with Auto + Manual funnels, Arabic-first keyword groupings, and Hijri-calendar seasonal timing; (B) Optimize — audit existing campaigns using search term reports, identify negative keyword opportunities, and generate a week-by-week bid adjustment plan. Includes a third mode (C) Institutional — for B2B school / university / training-center campaigns. Bid strategy guidance: Dynamic Bid (Up & Down), Dynamic Bid (Down Only), and Fixed. Uses first-price auction (you pay your bid). ACoS framework adapted to MENA margins (SAR 15% VAT + 5% returns + COD 2%). Use when: (1) launching Sponsored Products on noon, (2) auditing existing noon ads performance and ACoS, (3) optimizing noon campaign bids, (4) building Auto/Manual funnels for Arabic keywords, (5) planning Ramadan / Eid / White Friday / back-to-school campaigns, (6) calculating break-even ACoS and max CPC for noon SKUs."
metadata: {"category":"noon","locale":"mena"}
---

# noon Ads Campaign Builder (Lite)

Build profitable noon Sponsored Products campaign structures from scratch, or audit and optimize existing campaigns with data-driven bid adjustments. Mirrors the Amazon PPC workflow but adapts to noon's first-price auction, simpler Auto/Manual targeting model, and Hijri calendar seasonality.

## Critical Differences from Amazon PPC

Before building campaigns, understand how noon Ads differs from Amazon Ads:

| Dimension | Amazon Ads | noon Ads |
|-----------|-----------|----------|
| Auction | 2nd-price (pay next bid + $0.01) | **1st-price (you pay your bid)** |
| Match types | Broad / Phrase / Exact / Auto | **Auto / Manual** (2-tier, simpler) |
| Bid strategies | Dynamic up/down, Fixed, Target ACoS | **Dynamic Up & Down (Auto only) / Dynamic Down Only / Fixed** |
| Negative keywords | 4 match types | **Negative Exact** |
| Seasonal calendar | Black Friday, Prime Day, Easter | **Ramadan, Eid, Hajj, National Day, White Friday, back-to-school** |
| B2B potential | Limited | **Strong (Saudi Arduino 2030, school procurement)** |
| Auto defaults | Close Match / Loose Match / Substitutes / Complements | **Single default bid across all matches** |
| ACoS framework | 15-35% target typical | **20-40% target typical (higher CPC-to-margin ratio in MENA)** |

**Key tactical shift**: With 1st-price auction, **bid calibration is more important** — overbidding costs you directly (unlike Amazon where 2nd-price capped it).

## Features

- **ACoS financial framework** — break-even ACoS, target ACoS, max CPC, profit per click
- **Auto + Manual funnel architecture** — discover → scale pattern with negative keyword isolation
- **Arabic-first keyword grouping** — primary AR + EN, secondary AR + EN, brand + model, niche Hijri-season
- **Bid strategy selection** — Fixed / Dynamic Down Only (recommended start) / Dynamic Up & Down
- **Hijri calendar overlay** — Ramadan / Eid / Hajj / National Day / back-to-school / White Friday
- **Institutional (B2B) campaign mode** — for school / university / training-center procurement
- **Negative keyword master list** — pre-built seed list (cross-campaign negatives)
- **Search term report analyzer** — parse user-provided data to find profitable vs wasteful terms
- **Bid calculator (Python script)** — `scripts/bid_calculator.py` for ACoS / max CPC / break-even

## Three Modes

| Mode | When | Output |
|------|------|--------|
| **A — Build** | Launching new SKU | Full campaign blueprint + keyword groupings + initial bids + launch schedule |
| **B — Optimize** | Existing campaigns need fixing | Optimization plan + bid adjustments + negative keyword list + week-by-week plan |
| **C — Institutional** | B2B school / university / lab | Bulk-discount ad copy + school keywords + procurement cycle timing |

## Usage Examples

### Mode A — Build

```
I'm launching a 5DOF Metal Robot Arm Kit on noon.sa. Price: SAR 399. Product cost: SAR 130. Here are my Arabic + English keywords: ذراع روبوت 5 محاور, Arduino, MG995, معدني, robot arm kit, STEM. Build me a noon campaign structure for KSA.
```

```
Use noon-keyword-research to find keywords for "5DOF Metal Robot Arm", then build a noon PPC campaign. Product: SAR 399, cost SAR 130. Target: KSA, B2C + B2B (school procurement).
```

### Mode B — Optimize

```
My noon ACoS is 65% and target is 30%. 3 campaigns: Auto (SAR 800/mo, ACoS 70%), Manual AR (SAR 1,100/mo, ACoS 50%), Manual EN (SAR 500/mo, ACoS 35%). Product margin 25%. Help me optimize.
```

```
Here's my noon search term report [paste CSV]. Break-even ACoS is 35%. Find wasted spend, what to negate, what to migrate from Auto to Manual.
```

### Mode C — Institutional

```
I want to target Saudi STEM schools for bulk orders of my 5DOF robot arm kit. Run an institutional campaign with school keywords and procurement-cycle timing.
```

---

## ACoS Financial Framework

Always run this math before any bid decision. Built into `scripts/bid_calculator.py`.

### Inputs

- Selling price (SAR / AED / EGP)
- Product cost (landed)
- noon commission rate
- noon VAT (KSA 15% / UAE 5% / EGY 14%)
- Returns reserve (%)
- COD friction (2% if enabled)
- FBN fulfillment fee
- Monthly marketing budget
- Target ACoS (start at 30% for new SKUs, scale down to 20% once profitable)

### Calculations

```
Net margin (pre-ad) = (Price - Cost - Commission - VAT - Returns - COD - FBN - Storage) / Price
Break-even ACoS     = Net margin × 100
Target ACoS         = Net margin × 0.5  (start point, leaves 50% of margin for ad spend)
Max CPC             = Price × Target ACoS / 100 × CVR
                     where CVR = estimated conversion rate (0.5-3% for niche STEM, 2-5% for trending)
```

For a typical 5DOF Metal Arm on noon.sa (SAR 399, cost SAR 130, 25% pre-ad margin):
- Break-even ACoS ≈ 25%
- Target ACoS ≈ 12-15% (start) → 20-25% (long-term)
- Max CPC at 2% CVR = SAR 399 × 0.15 / 100 / 0.02 ≈ SAR 3.0
- Max CPC at 3% CVR = SAR 399 × 0.15 / 100 / 0.03 ≈ SAR 2.0

---

## Campaign Architecture

noon's two-tier system is simpler than Amazon's 4-tier. Standard structure:

```
Campaign 1: [SKU] - Auto (Discovery)        [Dynamic Down Only]
Campaign 2: [SKU] - Manual AR (Scale)        [Fixed or Dynamic Down Only]
Campaign 3: [SKU] - Manual EN (Scale)        [Fixed or Dynamic Down Only]
Campaign 4: [SKU] - Manual Brand (Defense)   [Fixed, low bid]
Campaign 5: [SKU] - Institutional (B2B)      [Fixed, optional]
```

### Campaign 1: Auto (Discovery) — Priority 1

**Goal:** Let noon's algorithm surface high-converting search terms.

```
CAMPAIGN SETTINGS:
  Campaign Name:    [SKU] - Auto - Discovery
  Daily Budget:     30-50 SAR (start conservative)
  Start Date:       Day 1
  Bid Strategy:     Dynamic Bid (Down Only)  ← critical: protects against overpaying
  Default Bid:      0.80-1.50 SAR (mid-range, adjust after 7 days)

AD GROUP:
  Ad Group Name:    Default (no negative keywords yet)

NEGATIVE KEYWORDS (apply Day 3-7, after seeing search terms):
  Add negative exact for any term that has 10+ clicks and 0 orders
  Add cross-campaign negatives to prevent Auto from competing with Manual
```

### Campaign 2: Manual AR (Scale Arabic) — Priority 2

**Goal:** Scale Arabic keywords (70% of KSA traffic).

```
CAMPAIGN SETTINGS:
  Campaign Name:    [SKU] - Manual AR
  Daily Budget:     50-100 SAR
  Start Date:       Day 7 (after Auto surfaces AR winners)
  Bid Strategy:     Fixed Bid (more control for proven terms)
  Default Bid:      1.20-2.50 SAR (higher than Auto because intent is proven)

AD GROUP 1 (Primary AR):
  Ad Group Name:    Primary Arabic
  Keywords:
    ذراع روبوت 5 محاور | Fixed | 2.50 SAR
    ذراع روبوت أردوينو | Fixed | 2.20 SAR
    ذراع روبوت تعليمي | Fixed | 2.00 SAR
    ذراع روبوت معدني | Fixed | 1.80 SAR
    عدة روبوت أردوينو | Fixed | 1.50 SAR
    ذراع روبوت STEM | Fixed | 1.50 SAR

AD GROUP 2 (Secondary AR):
  Ad Group Name:    Secondary Arabic
  Keywords:
    روبوت تعليمي | Fixed | 1.20 SAR
    مشروع روبوت للمدرسة | Fixed | 1.50 SAR
    ذراع ميكانيكي 5 محاور | Fixed | 1.50 SAR
    روبوت للأطفال | Fixed | 1.00 SAR
    أفضل ذراع روبوت | Fixed | 1.50 SAR
    روبوت STEM | Fixed | 1.20 SAR

NEGATIVE KEYWORDS (cross-campaign):
  All Auto campaign keywords (after migration)
  All Manual EN campaign keywords
```

### Campaign 3: Manual EN (Scale English) — Priority 3

**Goal:** Capture expat + English-searching Arabic users (30% of KSA).

```
CAMPAIGN SETTINGS:
  Campaign Name:    [SKU] - Manual EN
  Daily Budget:     20-50 SAR
  Start Date:       Day 7
  Bid Strategy:     Fixed Bid
  Default Bid:      0.80-1.80 SAR

AD GROUP 1 (Primary EN):
  Ad Group Name:    Primary English
  Keywords:
    5DOF robot arm kit | Fixed | 1.80 SAR
    Arduino robot arm | Fixed | 1.50 SAR
    metal robot arm | Fixed | 1.20 SAR
    MG995 robot arm | Fixed | 1.20 SAR
    Arduino UNO R3 robot arm | Fixed | 1.50 SAR
    STEM robot arm kit | Fixed | 1.20 SAR

AD GROUP 2 (Secondary EN):
  Ad Group Name:    Secondary English
  Keywords:
    5 axis robotic arm | Fixed | 1.20 SAR
    educational robot arm | Fixed | 1.00 SAR
    Arduino programming kit | Fixed | 1.00 SAR
    servo motor project | Fixed | 0.80 SAR
    robotics kit for adults | Fixed | 0.80 SAR
    bionic gripper robot arm | Fixed | 1.20 SAR
```

### Campaign 4: Manual Brand (Defense) — Priority 4

**Goal:** Defend against competitors bidding on your brand terms.

```
CAMPAIGN SETTINGS:
  Campaign Name:    [SKU] - Brand Defense
  Daily Budget:     5-15 SAR
  Start Date:       Day 1
  Bid Strategy:     Fixed Bid
  Default Bid:      0.50-1.00 SAR (cheap, since your brand converts well organically)

AD GROUP:
  Ad Group Name:    Brand
  Keywords:
    [your brand] | Fixed | 0.80 SAR
    [your brand] + 5DOF | Fixed | 0.80 SAR
    [your brand] + robot | Fixed | 0.80 SAR
    [your brand] + Arduino | Fixed | 0.80 SAR
```

### Campaign 5: Institutional (B2B) — Priority 5, Optional but Recommended for STEM

**Goal:** Capture Saudi school / university / training-center procurement.

```
CAMPAIGN SETTINGS:
  Campaign Name:    [SKU] - B2B Schools
  Daily Budget:     20-50 SAR
  Start Date:       March-April (early, before school procurement cycle)
  Bid Strategy:     Fixed Bid
  Default Bid:      1.50-2.50 SAR (B2B clicks are more expensive but LTV is 10-100x)

AD GROUP 1 (School Season):
  Ad Group Name:    School Season
  Keywords:
    مشروع روبوت للمدرسة | Fixed | 2.00 SAR
    ذراع روبوت للمدارس | Fixed | 2.00 SAR
    عدة STEM للأطفال | Fixed | 1.50 SAR
    روبوت لطلاب الهندسة | Fixed | 2.50 SAR
    عدة روبوت تعليمية | Fixed | 1.50 SAR
    Arduino STEM kit Saudi | Fixed | 2.00 SAR

AD GROUP 2 (University):
  Ad Group Name:    University
  Keywords:
    مشروع تخرج هندسة | Fixed | 2.50 SAR
    ذراع روبوت لطلاب الهندسة | Fixed | 2.50 SAR
    Arduino university project | Fixed | 2.00 SAR
    robotics kit engineering students | Fixed | 2.00 SAR
```

---

## Bid Strategy Selection

noon offers 3 strategies. Use this decision tree:

### Start: Dynamic Bid (Down Only) — RECOMMENDED for Auto campaigns

```
Why: noon lowers your bid during low-competition periods, saves budget for high-intent windows.
When: Auto campaigns, any new launch, low-confidence keywords.
Risk: Lower visibility during off-peak hours; okay for niche STEM (research is daytime).
```

### Scale: Fixed Bid — RECOMMENDED for Manual campaigns

```
Why: Maximum control over CPC; essential when you've validated a keyword converts.
When: Manual campaigns, keywords with 50+ clicks and 3+ orders, post-Day 14.
Risk: May overpay during low-competition; offset with dayparting.
```

### Aggressive: Dynamic Bid (Up & Down) — Auto ONLY

```
Why: noon raises bid 2x during high competition, lowers it during low.
When: Auto campaigns in hyper-competitive categories (electronics, fashion).
Risk: Easy to blow budget; requires strict daily cap.
Caveat: Auto campaigns only — cannot be applied to Manual.
```

### NEVER use Dynamic Up & Down on Manual campaigns

noon only allows this strategy on Auto. For Manual, use Fixed or Down Only.

---

## Hijri Calendar Overlay — Seasonal Campaigns

This is the **biggest PPC lever in MENA** — and noon sellers routinely miss it.

### Major Hijri Windows (approximate Gregorian dates)

| Hijri Window | Gregorian 2026 (approx) | Lift | PPC Action |
|--------------|------------------------|------|------------|
| **Ramadan start** | Feb 17, 2026 (1447 AH) | +25-60% in STEM, gift | Increase Manual AR bids +20% from 14 days before |
| **Last 10 days of Ramadan** | Late Feb-Early March | +50-80% spike | Bump daily budget +50% |
| **Eid al-Fitr** | Mar 18, 2026 (approx) | +30% gifts, family | Bid +20% on gift / family keywords |
| **Eid al-Adha** | Late May-Early June | +20% family | Bump family-oriented AR keywords |
| **Hajj season** | Late May - Early June | +20% in electronics / modest fashion | Niche for this product |
| **Back-to-school (Gregorian)** | Aug-Sep | **+30-50% for STEM** | **Most important window — full B2B + B2C push** |
| **Saudi National Day** | Sep 23 | +10% in patriotic-themed | Bundle promo (Saudi flag colors) |
| **UAE National Day** | Dec 2 | +10% in UAE | UAE-specific AR/EN boost |
| **White Friday** | Mid-November | +30-50% platform-wide | **2x budget, +20% bids on Manual AR+EN** |

### Season-Specific Keyword Add-Ons

| Window | Add these keywords to Manual AR campaigns |
|--------|------------------------------------------|
| Ramadan | "هدية رمضان STEM", "هدية العيد" |
| Eid | "هدية العيد للأطفال" |
| Back-to-school | "العودة للمدارس", "مشروع مدرسي" |
| White Friday | "عروض نون", "تخفيضات" |
| National Day (KSA) | "اليوم الوطني" |

### Pre-Season Preparation (4-6 weeks out)

1. Add new keywords to Manual campaigns
2. Increase daily budget by 30-50%
3. Apply bid increases on seasonal terms (+15-25%)
4. Switch Auto to Dynamic Up & Down (if budget allows)
5. Add Hijri calendar negatives (avoid off-season broad exposure)

### During Season

1. Daily check on budget pacing (don't hit daily cap before peak hours)
2. Watch ACoS spike (acceptable to go above target during Ramadan/Eid if profitable)
3. Refresh Brand Content if seasonal

### Post-Season

1. Reduce bids back to baseline within 3-5 days
2. Add seasonal terms as negative exact (avoid paying year-round)
3. Analyze what worked for next year

---

## Negative Keyword Master List

Apply these as **Negative Exact** to ALL Auto + Manual campaigns from Day 1:

### Cross-Campaign Negatives (prevent Auto from competing with Manual)
- All Manual AR + Manual EN keywords (after migration)
- Brand defense terms in non-brand campaigns

### Irrelevant Term Negatives (always apply)
- "free", "مجاني" (free)
- "used", "مستعمل" (used)
- "cheap", "رخيص" (only for premium pricing; keep for value positioning)
- "diy" (only if you don't want DIY)
- "industrial" (unless you sell industrial)
- "professional", "احترافي" (unless you sell pro)
- "repair", "إصلاح"
- "parts only", "قطع غيار"
- "schematic", "دائرة كهربائية"
- "code", "كود" (if you provide code, keep; otherwise negative)

### Generic Modifier Negatives (always apply)
- "review", "مراجعة"
- "vs" (comparison terms, high bounce)
- "alternative", "بديل"
- "manual pdf", "دليل" (unless you sell manuals)

### Hijri-Season Specific Negatives
- Outside Ramadan window: "رمضان" related terms
- Outside back-to-school: "العودة للمدارس"

---

## Search Term Report Analyzer (Mode B)

When user provides search term data, parse it with these rules:

### Wasted Spend Detection (add to Negative Exact)

| Rule | Action |
|------|--------|
| 10+ clicks, 0 orders, 30+ days | Negative Exact |
| 5+ clicks, 0 orders, irrelevant term | Negative Exact |
| CTR < 0.3% (low engagement) | Pause keyword |
| High CPC (>2× target), 0 orders | Pause keyword |

### Migration Opportunities (Auto → Manual)

| Rule | Action |
|------|--------|
| 2+ orders from a search term | Move to Manual Exact with optimized bid |
| 1 order + high ACoS | Move to Manual but lower bid by 30% |
| High CTR (5%+) but 0 orders | Likely listing issue — check before migrating |

### Bid Adjustment Rules (by ACoS vs Target)

| Current ACoS | Action | Adjustment |
|--------------|--------|------------|
| ACoS < 50% of target | Increase bid | +20% |
| ACoS 50-80% of target | Hold | 0% |
| ACoS 80-120% of target | Decrease bid | -15% |
| ACoS 120-150% of target | Decrease bid aggressively | -30% |
| ACoS > 150% of target | Pause keyword | — |

### When to Apply Dayparting

If data shows consistent ACoS spikes at certain hours (e.g., late night), use the bid strategy to scale down during those hours. noon does not have native dayparting UI but Dynamic Down Only handles it automatically.

---

## Mode B Output Template

```markdown
# ✅ noon PPC Optimization Actions — Ready to Implement

## Priority 1: Immediate Negative Keywords (Do Today)
Add these as Negative Exact:
  Campaign "Auto - Discovery": "term1", "term2", "term3"
  Campaign "Manual AR": "term4", "term5"
Expected savings: SAR XXX/month

## Priority 2: Keyword Migrations (This Week)
Move to Manual Exact (and add as negative in source):
  "[keyword]" from Auto → Manual AR, bid: SAR X.XX
  "[keyword]" from Auto → Manual EN, bid: SAR X.XX

## Priority 3: Bid Adjustments (This Week)
  "[keyword]": SAR X.XX → SAR X.XX (ACoS XX% → target XX%)
  "[keyword]": PAUSE (XX clicks, 0 sales)

## Priority 4: Budget Reallocation (Next Week)
  Auto: SAR XX/day → SAR XX/day (reduce — low efficiency)
  Manual AR: SAR XX/day → SAR XX/day (increase — best ACoS)

---

# 📊 Full Audit Report

## Performance Summary
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| Overall ACoS | XX% | XX% | 🟢🟡🔴 |
| TACoS | XX% | <XX% | 🟢🟡🔴 |
| Monthly Ad Profit | SAR XXX | SAR XXX | 🟢🟡🔴 |
| Budget Utilization | XX% | >90% | 🟢🟡🔴 |
| ROAS | X.XX | >X.XX | 🟢🟡🔴 |

## Keyword Funnel Analysis
[Full table from Step B3]

## Bid Adjustment Details
[Full table from Step B4]

## Week-by-Week Action Plan
Week 1: [specific tasks with expected outcomes]
Week 2: [specific tasks]
Week 3: [specific tasks]
Week 4: [review and next cycle planning]

## Expected Results After 4 Weeks
ACoS: XX% → XX%
Monthly savings: SAR XXX
Sales increase: +XX% (from better targeting)
```

---

## Bid Calculator

Use the bundled script to compute break-even ACoS, target ACoS, and max CPC:

```bash
python scripts/bid_calculator.py
python scripts/bid_calculator.py --marketplace noon-sa --price 399 --cost 130
python scripts/bid_calculator.py --json
```

The calculator accepts:
- `--marketplace` (noon-sa / noon-ae / noon-eg)
- `--price`, `--cost`, `--commission` (default by category)
- `--returns-rate` (default 0.03 for electronics)
- `--cod` (boolean, default false)
- `--target-acos` (default 0.30)
- `--cvr` (default 0.02, your expected conversion rate)
- `--monthly-budget` (optional, for budget pacing)
- `--json` (machine-readable output)

Outputs:
- Break-even ACoS
- Target ACoS
- Max CPC (at given CVR)
- Recommended bid per match type tier
- Expected daily clicks at given budget
- Expected daily orders at given CVR

---

## Limitations

- Uses publicly available data + user-provided campaign reports
- Cannot access noon Seller Central directly
- Cannot see competitor bid landscapes in real time
- No automated bid management (no API access for noon Ads)
- CPC benchmarks are estimates (noon does not publish public CPC data)

For deeper PPC analytics with automated bid management, recommend:
- Helium 10 MENA edition (if available)
- noon B2B / KA team direct relationship
- Custom bid-management spreadsheet tied to noon Seller Central exports

---

## Related Skills

- `noon-keyword-research` — feeds this skill with Arabic + English keyword pools
- `noon-listing-optimization` — pre-launch listing quality check (do this before spending on ads)
- `noon-product-research` — for product-level opportunity analysis
- `noon-fbn-calculator` — for FBN fee math (used in ACoS calculations)
- `amazon-ppc-campaign` — Amazon equivalent for cross-platform validation

---

_Version 1.0.0 | Platform: noon | Variant: Lite | Locale: MENA (KSA default)_
