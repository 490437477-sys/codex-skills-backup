---
name: noon-product-research
description: "Comprehensive product research and opportunity analysis for the noon marketplace (noon.sa Saudi Arabia, noon.ae UAE, noon.com Egypt). Analyzes demand, competition, profit potential, FBN feasibility, Arabic-market localization, Ramadan seasonality, and regulatory compliance (SASO/SFDA/ESMA). Use when the user asks about researching a product for noon, validating a MENA e-commerce idea, comparing noon vs Amazon.sa/Amazon.ae, calculating noon FBN fees, checking Arabic keyword demand, evaluating Ramadan product opportunities, assessing SFDA/SASO compliance requirements, or any general MENA cross-border product research questions."
metadata: {"category":"noon","locale":"mena"}
---

# noon Product Research

Complete product research framework for the noon marketplace. noon is a Middle East e-commerce platform operating primarily in Saudi Arabia (noon.sa), UAE (noon.ae), and Egypt (noon.com), founded with Saudi PIF backing. This skill mirrors the Amazon product research workflow but adapts every step to MENA reality: Arabic-first listings, FBN logistics, Ramadan seasonality, religious and regulatory compliance, COD payment mix, and SAR/AED/EGP pricing.

## Capabilities

- **Marketplace-aware scoring** across noon.sa / noon.ae / noon.com
- **Demand analysis** including Google Trends for the relevant MENA geo and Arabic / English keyword splits
- **Competition mapping** against noon private label, regional brands, and cross-border sellers (Amazon.ae / Amazon.sa, Namshi, Ounass, 6thStreet)
- **FBN fee & profit calculation** with Saudi / UAE / Egypt fee schedules
- **Localization audit** for Arabic copy, RTL imagery, bilingual title optimization
- **Seasonality modelling** including the Ramadan / Eid / Hajj / back-to-school / White Friday windows
- **Compliance pre-check** for SASO (Saudi Standards), SFDA (Saudi Food & Drug), ESMA / MOIAT (UAE), and Egypt GOEIC
- **COD vs prepaid risk** modelling
- **Currency & VAT** handling: 15% KSA VAT, 5% UAE VAT, 14% Egypt VAT

## When to Use

- User asks "should I sell X on noon", "noon选品", "中东卖什么", "noon沙特"
- User provides a product and wants a noon-specific go / no-go
- User wants to compare noon vs Amazon.ae / Amazon.sa for a category
- User asks about noon FBN fees, FBN size tiers, or noon commission rates
- User wants Arabic keyword demand or Arabic listing guidance
- User wants to know if a product needs SASO / SFDA / ESMA certification
- User wants a Ramadan / White Friday / back-to-school opportunity brief

## Quick Mode vs Full Mode

| Mode | When | Output |
|------|------|--------|
| **Quick** | User asks a yes/no about one product | One-page verdict: Score 1-10, top 3 risks, top 3 actions |
| **Full** | User asks for full research, comparison, or a launch plan | 8-section report following the workflow below |

Default to **Full** unless the user explicitly asks for a quick check.

## Workflow

### Step 1: Confirm Marketplace & Locale

Always pin the marketplace before researching. Defaults if the user does not specify:

- Arabic-only or "Saudi" → **noon.sa** (KSA, SAR, VAT 15%)
- "UAE" / "Dubai" / "Emirates" → **noon.ae** (UAE, AED, VAT 5%)
- "Egypt" → **noon.com** (EGP, VAT 14%)
- "MENA" / "Middle East" / unspecified → lead with **noon.sa**, then **noon.ae**

Record the locale. The rest of the analysis pivots on it.

### Step 2: Demand Analysis

Use `web_search` and `web_fetch`. MENA-specific queries:

1. **Arabic keyword volume**: `"[product Arabic name]" موقع نون` and `"[product Arabic name]" الأكثر مبيعاً`
2. **English / transliterated search**: `"[product] noon.sa"`, `"[product] buy online KSA"`
3. **Google Trends with MENA geo**: fetch `https://trends.google.com/trends/explore?q=[product]&geo=SA` (default) or `geo=AE` / `geo=EG`
4. **Category best-sellers**: `web_fetch` on `https://www.noon.sa/[category]/b/[category-slug]` to capture bestseller rank, prices, review counts
5. **Seasonality**: include year-over-year trend, plus flag Ramadan/Eid/Hajj spikes if applicable
6. **Cross-platform validation**: `"[product]" Amazon.sa bestseller`, `"[product]" Namshi best sellers`

Demand indicators to capture:

- Arabic search interest vs English (healthy ratio is roughly 70% Arabic / 30% English in KSA; 60/40 in UAE)
- Ramadan uplift vs baseline (many categories lift 25-60% in the 30 days before Eid)
- COD-heavy categories (fashion, beauty, baby) vs prepaid-heavy (electronics, gaming)
- Mobile vs desktop split (noon is ~75%+ mobile in KSA)

**Demand scoring (1-10):**

- 9-10: Strong upward Arabic + English interest, growing 12-month trend
- 7-8: Stable high demand, clear seasonality peaks
- 5-6: Moderate demand, clear seasonal windows only
- 3-4: Declining trend or hyper-seasonal
- 1-2: Niche or weak Arabic demand

### Step 3: Competition Mapping

noon's competitive landscape differs from Amazon:

1. **noon private label** (noon Basics, branded vertical plays) - check if present in the category
2. **Regional brands** (Namshi private label, Ounass luxury, 6thStreet footwear)
3. **Cross-border Amazon** sellers on Amazon.sa / Amazon.ae
4. **GCC & Levant** local sellers (Aramex-tracked, often 2-5 day delivery)
5. **Chinese cross-border** (AliExpress / SHEIN / Temu now blocked or restricted in KSA)
6. **Brand-owned storefronts** (Samsung, L'Oreal, Philips direct on noon)

For each, capture: price band, review count, FBN vs seller-fulfilled, shipping SLA, Arabic listing quality.

**Competition scoring (1-10):**

- 9-10: Highly fragmented, weak listings, no dominant brand
- 7-8: Some established players but clear gaps (poor Arabic, weak imagery)
- 5-6: 2-3 strong brands, defensible only with clear differentiation
- 3-4: noon Basics or Amazon-like dominance
- 1-2: Single brand or platform-owned control

### Step 4: Profitability & FBN Feasibility

Use the references file `references/noon-fees-and-fbn.md` for the full rate sheet. Quick formula:

```
Net = Price − (Price × Commission%) − FBN_Fulfillment − FBN_Storage − Product_Cost − Inbound_Shipping − Returns_Reserve − VAT_Carrying_Cost − Marketing
```

Approximate defaults (verify with the references file at pricing time):

- **Commission**: 5-25% by category (electronics low, beauty mid, fashion mid, grocery high)
- **FBN fulfillment fee**: AED/SAR scale, weight-tiered (small parcel ~5-9 SAR)
- **FBN storage**: monthly per cubic foot, peak Q4 uplift
- **VAT**: noon collects from buyer; seller remits. Carry as cash-flow cost, not a margin line
- **Returns**: 5-15% expected in fashion; 2-5% in electronics
- **COD**: adds 1-3% reconciliation friction if enabled

Profit scoring (1-10):

- 9-10: Net margin > 25% after all fees
- 7-8: Net margin 15-25%
- 5-6: Net margin 8-15%
- 3-4: Net margin 0-8%
- 1-2: Negative or break-even

### Step 5: Localization Audit (Arabic & RTL)

Listings in Arabic consistently outperform English-only on noon. Audit:

1. **Title**: Arabic title present, primary keyword first, English brand / model in parentheses
2. **Bullets**: Arabic bullets + transliterated English terms
3. **Description**: Arabic paragraph; English allowed below for technical specs
4. **Imagery**: RTL-safe product photos (logos not mirrored); lifestyle shots reflecting local dress, family, prayer / iftar scenes where relevant
5. **Video**: Arabic subtitles preferred for fashion / beauty / electronics demos
6. **Search terms (backend)**: bilingual keyword block, no duplication with title

Localization scoring (1-10):

- 9-10: Full bilingual coverage, RTL imagery, Arabic video
- 7-8: Arabic title + bullets, English supporting copy
- 5-6: English-only with some Arabic keywords
- 1-4: English-only, no Arabic keywords (immediate handicap)

### Step 6: Seasonality & Demand Calendar

Build a 12-month demand curve:

| Window | Category uplift | Notes |
|--------|-----------------|-------|
| **Ramadan (30 days)** | +25-60% in food, beauty, home, fashion | Single biggest sales spike on noon |
| **Eid al-Fitr** | +15-30% in fashion, gifts, toys | Listings must be live 14 days before |
| **Hajj season** | +20-40% in travel, electronics, modest fashion | Late July-early September (lunar) |
| **Back-to-school (Aug-Sep)** | +20-35% in stationery, electronics, uniforms | Calendar-locked |
| **White Friday (Nov)** | +30-50% across most categories | noon equivalent of Black Friday |
| **12.12 / Year-end** | +15-25% across most categories | COD-heavy |
| **National Day (Saudi: Sep 23, UAE: Dec 2)** | +10-20% themed merchandise | Local pride plays well |

If the product has no seasonal story, call that out. If it is Ramadan-driven, model the inventory ramp: stock 60-90 days before, peak by week 2 of Ramadan.

### Step 7: Compliance & Regulatory Pre-check

Load `references/noon-compliance-checklist.md` for the full matrix. Quick gate:

- **KSA**: SASO IECEE for electronics, SFDA for food/cosmetics/medical, CITC for telecom/radio, SASO energy efficiency labels
- **UAE**: ESMA (now MOIAT) for regulated goods, TRA for telecom, ECCA for food
- **Egypt**: GOEIC for imports, NFSA for food, EDA for drugs
- **GCC-wide**: GSO conformity, Arabic label requirement on most consumer goods
- **Restricted on noon KSA**: alcohol, pork, gambling, religious items sold to non-Muslims, weapons, single-use plastics (some categories)

Mark each requirement as Must-Have (launch blocker) / Should-Have (post-launch) / Not Applicable.

### Step 8: Risk & Go / No-Go

Roll up the four pillar scores into an overall verdict:

```
Overall = 0.30 × Demand + 0.25 × Competition + 0.25 × Profit + 0.20 × Localization
```

Adjust weights for compliance-heavy categories (raise compliance to 0.20 by trimming Localization).

**Decision rules:**

- **8-10 — Pursue aggressively**: launch with FBN, Arabic-first listings, Ramadan / White Friday calendar
- **6-7.9 — Pursue with conditions**: address the two lowest-scoring pillars before sourcing
- **4-5.9 — Conditional**: viable only with strong differentiation (bundle, Arabic-native brand, category gap)
- **Below 4 — Pass**: redirect to a related category with better fundamentals

## Output Format

### Full Report Template

```markdown
# noon Product Research: [Product Name]

**Marketplace:** noon.sa (KSA, SAR) | noon.ae (UAE, AED) | noon.com (EGY, EGP)
**Date:** YYYY-MM-DD
**Verdict:** Pursue / Conditional / Pass — Score X.X / 10

## 🛒 Market Snapshot
- Arabic demand: High/Medium/Low
- English demand: High/Medium/Low
- Top Arabic keyword: [keyword] (~[volume])
- Google Trends (geo=SA, 12mo): Rising/Stable/Declining
- Ramadan uplift expected: +X%
- Category: [main] > [sub]

## 🏪 Competition
- noon Basics present: Yes/No
- Dominant regional brand: [name] (~X% share estimate)
- Top 3 sellers: [name, price, review count, FBN/Seller, Arabic quality]
- Defensible gap: [what is missing — Arabic, price band, feature]

## 💵 FBN Profit Model
```
Target price:          SAR/AED/EGP XXX
Commission (~X%):      −XX.XX
FBN fulfillment:       −XX.XX
FBN storage (1 mo):    −XX.XX
Product cost:          −XX.XX
Inbound shipping:      −XX.XX
Returns reserve (~X%): −XX.XX
Marketing:             −XX.XX
Net margin:            XX.XX (XX%)
```
- Margin rating: Excellent / Good / Tight / Poor
- FBN size tier: Small / Large / Oversize (see references)

## 🌐 Localization Audit
- Arabic title: Present / Missing / Weak
- Arabic bullets: Yes / No
- Backend keywords bilingual: Yes / No
- RTL-safe imagery: Yes / No
- Arabic video: Yes / No / N/A

## 🗓️ Seasonality Plan
- Peak windows: [Ramadan week X, White Friday, etc.]
- Inventory ramp: stock by [date]
- Listing freeze: lock Arabic copy by [date]

## 🛡️ Compliance
- SASO IECEE: Required / N/A
- SFDA registration: Required / N/A
- Arabic label: Required / N/A
- Restricted category: Yes / No
- Lead time for certs: X weeks

## ⚠️ Risk Register
- Demand risk: [seasonal / declining]
- Competition risk: [noon Basics / Amazon cross-border]
- Operational risk: [COD returns / heat damage / Saudi customs]
- Financial risk: [VAT cash-flow / FX to CNY]

## 🎯 Recommendation
- **Go / No-Go**: ✅ Pursue / ⚠️ Conditional / ❌ Pass
- **Entry mode**: FBN / Cross-border FB / Brand.com + noon storefront
- **First SKU price**: SAR/AED/EGP XXX
- **Differentiation angle**: [Arabic-native copy / bundling / category gap]
- **Launch milestone**: [date for listing live, FBN inbound, cert ready]
```

### Quick Verdict Format

```
Verdict: Pursue (7.4/10) — FBN-ready, Arabic-first, Ramadan-anchored
Top 3 risks: [COD returns, SASO lead time, noon Basics entry]
Top 3 actions: [Lock Arabic copy, file SASO IECEE, book FBN inbound 75 days pre-Ramadan]
```

## Differentiation Playbook (noon-specific)

These moves routinely outperform on noon:

1. **Arabic-native brand voice** — many competitors transliterate English. Original Arabic copy wins.
2. **Bundle for iftar / back-to-school / Hajj** — themed kits lift AOV by 20-40%.
3. **Pre-Ramadan listing** — listings indexed 60+ days before Ramadan capture the search surge.
4. **FBN over FB** — FBN listings rank higher and ship next-day in Riyadh, Jeddah, Dubai.
5. **Hijri calendar overlays** — convert Gregorian dates to Hijri when planning campaigns.
6. **Local payment mix** — enable Mada (KSA), Apple Pay (UAE), and COD for category-typical conversion lift.
7. **Heat & humidity-safe packaging** — Gulf logistics punish thin packaging; build it into cost.

## Limitations & When to Escalate

This skill uses publicly available data (web search, Google Trends, noon public pages). It cannot:

- Access noon Seller Central backend sales data
- Pull exact BSR-to-units conversion for noon
- Verify real-time FBN capacity per warehouse
- Confirm current commission rates without noon Seller Central login

When the user needs these, recommend pairing with a noon's own Seller Central analytics or a paid MENA market intelligence tool.

## Related Skills

Chain with these where available:

- `amazon-product-research` — for cross-checking against Amazon.sa / Amazon.ae
- `amazon-listing-optimization` — adapt its listing framework to Arabic + RTL
- `amazon-fba-calculator` — adapt math to noon FBN fee table (this skill's references)
- `amazon-keyword-research` — reuse keyword extraction logic, then translate to Arabic

---

_Built for the noon marketplace — KSA, UAE, Egypt. Currency defaults to SAR unless user specifies otherwise._
