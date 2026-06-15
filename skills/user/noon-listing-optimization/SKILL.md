---
name: noon-listing-optimization
description: "Arabic-first listing builder and optimizer for the noon marketplace (noon.sa / noon.ae / noon.com). Two modes: (A) Create — build keyword-optimized Arabic + English listings from a noon keyword list, product characteristics, and cultural tone; (B) Optimize — audit an existing noon listing, find Arabic coverage gaps, score across 8 dimensions, and rewrite to beat competitors. Mirrors the Amazon listing optimization workflow but adapts to MENA reality: Arabic title leading, RTL-safe imagery, bilingual backend keywords, modest-fashion & family imagery norms, Hijri calendar overlays in A+ content, and noon Brand Store content. Use when: (1) creating a new noon listing, (2) auditing an existing noon listing, (3) checking Arabic keyword coverage in title / bullets / description / backend, (4) generating Arabic listing copy, (5) comparing against noon competitors, (6) preparing a noon listing for Ramadan / White Friday / back-to-school launch."
metadata: {"category":"noon","locale":"mena"}
---

# noon Listing Optimization

Build Arabic-first keyword-optimized noon listings from scratch, or audit and rewrite existing ones. Mirrors the Amazon listing optimization workflow but adapts every section to MENA reality: Arabic title leading, RTL-safe imagery, bilingual backend keywords, cultural tone.

## Installation

This skill is part of the local noon skill set under `C:\Users\Administrator\.codex\skills\noon-listing-optimization\`. No remote install required.

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Create** | Building a new noon listing | Keywords + product info + tone (or competitor noon URLs) | Full Arabic-first listing copy + bilingual keyword coverage score |
| **B — Optimize** | Improving an existing noon listing | Your noon SKU or URL + (optional) keywords or competitor URLs | Optimized listing copy + 8-dimension audit + gap analysis |

## Mode A — Three Ways to Start

| Input Source | How it Works |
|--------------|--------------|
| **Keywords** | User provides keyword list → skill prioritizes Arabic-first then English, then generates listing |
| **Competitor noon URLs** | User provides 1-3 noon listing URLs → skill fetches them, extracts their Arabic + English keywords, then generates a listing that covers more keywords and beats them on tone |
| **Both** | User provides keywords + competitor URLs → merges both sources for maximum Arabic coverage |

## Capabilities

- **Arabic-first listing generation**: Arabic title leads, English brand / model in parentheses
- **Competitor keyword extraction from noon public listings**: Pull real Arabic + English keywords from noon PDPs and bestseller pages
- **8-dimension audit & scoring**: Arabic title, English title, Arabic bullets, English bullets, description, imagery, brand content, SEO coverage
- **Bilingual keyword coverage tracking**: Visual map showing which Arabic / English / transliterated keywords appear where
- **Tone selection**: Professional, Friendly, Premium, Family — affects both Arabic and English copy
- **Cultural compliance check**: Modest-fashion friendly imagery, no alcohol / pork references, family-safe language
- **Hijri calendar awareness**: Optionally bake Ramadan / Eid / National Day into Brand Content / A+ section
- **Multi-marketplace**: noon.sa (KSA, default), noon.ae (UAE), noon.com (Egypt)

## Usage Examples

### Mode A — Create from Keywords

```
Create a noon listing for portable blender. Keywords: خلاط محمول, سماعات بلوتوث, portable blender, mini blender, USB rechargeable, travel blender, ميني خلاط. Material: BPA-free Tritan. Color: White. Capacity: 380ml. Tone: Friendly. Marketplace: noon.sa.
```

```
I have these noon keywords from my research:
[Arabic + English list]. Product: silicone kitchen utensil set, 12 pieces, heat resistant to 480°F. Generate a full Arabic-first noon listing.
```

### Mode A — Create from Competitor URLs

```
I want to sell wireless earbuds on noon.sa. Here are 3 noon competitors I want to beat:
https://www.noon.sa/saudi-en/[slug-1]
https://www.noon.sa/saudi-en/[slug-2]
https://www.noon.sa/saudi-ar/[slug-3]
My product: ENC mic, 36-hour battery, IPX5. Tone: Professional.
```

```
Create a noon listing for my yoga mat. Look at this noon competitor: [noon URL]. Extract their Arabic + English keywords, find what they're missing, and build a listing that beats them on Arabic coverage.
```

### Mode A — Create from Keywords + Competitor URLs

```
Use noon-keyword-research to find keywords for "خلاط محمول", also analyze these noon competitors: [url1, url2]. Combine all and create a listing. Product: 380ml BPA-free, USB-C. Tone: Family.
```

### Mode B — Optimize Existing

```
Audit my noon listing for SKU N12345678 on noon.sa
```

```
Optimize noon listing N12345678 with these keywords: سماعات لاسلكية, earbuds, بلوتوث, ENC — show me what's missing and rewrite in Arabic-first format.
```

```
Optimize my noon listing N12345678 by analyzing these competitors: [url1, url2, url3]. Find what Arabic keywords they have that I don't, and rewrite my listing to beat them.
```

## Mode A Workflow — Create Listing from Keywords

### Step A1: Collect Keywords

Three sources:

1. **From `noon-keyword-research` skill** (recommended): Run keyword research first, then feed results directly. The research output already separates Arabic / English / brand-model / niche.
2. **User-provided list**: Accept any mix; rank Arabic-first if locale is KSA / Egypt.
3. **From noon competitor URLs**: Fetch 1-3 noon PDPs, extract their title (AR + EN), bullet (AR + EN), description, backend search terms.

### Step A2: Rank Keywords by Priority

Bucket the merged keyword pool:

| Tier | Arabic | English | Purpose |
|------|--------|---------|---------|
| 🥇 Primary (title) | top 1-2 Arabic high-volume | top 1 English brand/model | Lead the title |
| 🥈 Secondary (bullets) | top 3-5 Arabic | top 2-3 English | Bullet 1-5 lead phrases |
| 🥉 Tertiary (description) | 5-10 Arabic variants | 3-5 English variants | Description body |
| 🔒 Backend | remaining Arabic + transliterated | remaining English | Backend search terms block |

Use `references/noon-listing-template.md` for the field-by-field structure.

### Step A3: Generate Arabic-first Listing

Produce the listing in this order:

1. **Arabic title** (≤ 70 characters) — primary Arabic keyword first, English brand / model in parentheses if space allows
2. **English title** (≤ 70 characters) — English brand / model first, Arabic keyword at the end in parentheses
3. **Arabic bullets** (5 bullets, ≤ 100 chars each) — each starts with a 2-3 word Arabic benefit header
4. **English bullets** (5 bullets, mirror of Arabic) — each starts with a 2-3 word English benefit header
5. **Arabic description** (≤ 1,500 chars) — paragraphs in MSA; tone matches user selection
6. **English description** (≤ 1,500 chars) — mirror of Arabic; technical specs allowed in English
7. **Backend search terms** (≤ 250 bytes, comma-separated) — bilingual, no duplication with title, no duplication within itself
8. **Brand Content / A+ equivalent** (optional, ≤ 5 modules) — culturally appropriate modules

### Step A4: Score Keyword Coverage

Build a coverage matrix:

```
Keyword Coverage: 87%

| Keyword | Lang | Volume | Title | Bullets | Description | Backend | Status |
|---------|------|--------|-------|---------|-------------|---------|--------|
| سماعات لاسلكية | AR | H | ✅ | ✅ | ✅ | — | 🟢 |
| wireless earbuds | EN | M | ✅ (parens) | ✅ | ✅ | — | 🟢 |
| بلوتوث | AR | M | — | ✅ | — | ✅ | 🟡 |
| earbuds with mic | EN | L | — | — | ✅ | ✅ | 🟡 |
| ENC ميكروفون | AR+EN | L | — | — | — | ✅ | 🟢 |
```

🟢 = in two or more fields; 🟡 = in one field; 🔴 = not used yet.

### Step A5: Cultural Compliance Check

Before handing over the listing, verify:

- [ ] No alcohol / pork / gambling references (auto-fail on noon)
- [ ] No mixed-gender close-contact imagery (modesty norms)
- [ ] No astrology / fortune-telling references
- [ ] No politically charged references (regional sensitivities)
- [ ] Arabic copy uses MSA, not Egyptian dialect (unless marketplace = noon.com)
- [ ] Brand / model in Arabic title uses parentheses correctly (RTL-safe)
- [ ] Dates mentioned use both Gregorian and Hijri if seasonal (Ramadan, Eid, National Day)

If any check fails, rewrite the affected field before producing the final output.

### Step A6: Emit Final Listing (Standalone Deliverable)

Output must be copy-paste-ready into noon Seller Central. Never produce only the diagnostic — the listing itself is the deliverable.

## Mode A Output Template

```markdown
# ✅ noon Listing — Ready to Use

**Marketplace:** noon.sa (KSA) | noon.ae (UAE) | noon.com (EGY)
**Tone:** [Professional / Friendly / Premium / Family]
**Keywords imported:** [count] (Arabic: [X], English: [Y])

---

## Title (Arabic) — paste into "العنوان"
[Arabic title ≤ 70 chars]

## Title (English) — paste into "Title"
[English title ≤ 70 chars]

## Bullet 1 (Arabic)
[ARABIC HEADER] — [Arabic text ≤ 100 chars]

## Bullet 1 (English)
[ENGLISH HEADER] — [English text ≤ 100 chars]

(repeat for bullets 2-5)

## Description (Arabic)
[Arabic paragraph ≤ 1,500 chars — copy directly]

## Description (English)
[English paragraph ≤ 1,500 chars — copy directly]

## Backend Search Terms — paste into "Search Terms"
[comma-separated bilingual block ≤ 250 bytes]

## Brand Content (optional, ≤ 5 modules)

**Module 1 — [HEADER]**
[Arabic + English text]

**Module 2 — [HEADER]**
[Arabic + English text]

(continue up to 5 modules)

---

# 📊 How We Built This Listing (Diagnostic)

**Title characters (AR):** [X] / 70 | **(EN):** [Y] / 70
**Description characters (AR):** [X] / 1500 | **(EN):** [Y] / 1500
**Backend bytes used:** [X] / 250

## Keyword Coverage: [X]%

[Coverage matrix from Step A4]

## Keyword Priority Breakdown

🥇 Primary (Title):
- AR: [list]
- EN: [list]

🥈 Secondary (Bullets):
- AR: [list]
- EN: [list]

🥉 Tertiary (Description):
- AR: [list]
- EN: [list]

🔒 Backend:
- bilingual block: [summary]

## Cultural Compliance: [PASS / FIX]

- ✅ / ❌ Alcohol-free copy
- ✅ / ❌ Modesty-safe imagery suggestions
- ✅ / ❌ MSA Arabic (or Egyptian dialect if EGY)
- ✅ / ❌ No politically sensitive references
- ✅ / ❌ Hijri dates noted where seasonal
```

## Mode B Workflow — Audit + Optimize Existing

### Step B1: Fetch Current Listing

Get the current noon listing (Arabic title, English title, bullets, description, backend search terms if accessible, imagery count, Brand Content modules if any).

If the user provides only a noon SKU, search noon public site for the matching PDP.

### Step B2: Pull Competitor noon Listings

Ask the user for 1-3 noon competitor URLs, or auto-pick the top 3 bestsellers from the same category.

### Step B3: 8-Dimension Audit

| Dimension | Weight | What to Score |
|-----------|--------|---------------|
| Arabic title quality | 15 | Arabic first, primary keyword, brand in parens, ≤ 70 chars |
| English title quality | 10 | Brand / model first, Arabic keyword at end, ≤ 70 chars |
| Arabic bullets | 15 | 5 bullets, benefit headers, primary + secondary keywords |
| English bullets | 10 | Mirror of Arabic, technical specs allowed |
| Description (AR + EN) | 10 | Storytelling tone, primary + tertiary keywords, ≤ 1,500 chars each |
| Imagery | 15 | RTL-safe, lifestyle photos, modesty-compliant, ≥ 5 images |
| Brand Content / A+ | 10 | Optional modules, cultural fit, Hijri overlays where seasonal |
| SEO coverage | 15 | Bilingual keyword coverage across title / bullets / description / backend |

Total: 100 points.

### Step B4: Gap Analysis

For each keyword present on competitors but missing on the user's listing, mark it as 🔴 Gap.

### Step B5: Rewrite the Listing

Apply Mode A workflow to produce the optimized listing in Arabic-first format.

## Mode B Output Template

```markdown
# ✅ Optimized noon Listing — Ready to Use

## Title (Arabic)
[optimized Arabic title]

## Title (English)
[optimized English title]

## Bullets (Arabic 1-5)
[AR] [HEADER] — [text]
[AR] [HEADER] — [text]
[AR] [HEADER] — [text]
[AR] [HEADER] — [text]
[AR] [HEADER] — [text]

## Bullets (English 1-5)
[EN] [HEADER] — [text]
[EN] [HEADER] — [text]
[EN] [HEADER] — [text]
[EN] [HEADER] — [text]
[EN] [HEADER] — [text]

## Description (Arabic)
[optimized Arabic description]

## Description (English)
[optimized English description]

## Backend Search Terms
[optimized bilingual backend block]

## Brand Content (optional)
[optimized modules]

---

# 📊 Audit Report: [SKU / URL]

**Product:** [title] | **Brand:** [brand]
**Price:** [currency] [price] | **Rating:** [stars] ([count] reviews)
**Marketplace:** [noon.sa / noon.ae / noon.com]

## Score: [X/100] → [Y/100] (after optimization)

| Dimension | Before | After | Key Change |
|-----------|--------|-------|------------|
| Arabic title | /15 | /15 | [what changed] |
| English title | /10 | /10 | [what changed] |
| Arabic bullets | /15 | /15 | [what changed] |
| English bullets | /10 | /10 | [what changed] |
| Description | /10 | /10 | [what changed] |
| Imagery | /15 | — | [recommendation only] |
| Brand Content | /10 | — | [recommendation only] |
| SEO Coverage | /15 | /15 | [what changed] |

## Keyword Coverage: [X]% → [Y]%

[Coverage matrix]

## 🔴 Gaps Closed

| Keyword | Lang | Where Added |
|---------|------|-------------|
| [kw] | AR | Title + Bullet 2 |
| [kw] | EN | Title (parens) + Description |
| ... | ... | ... |

## 📈 What Changed (Before → After)

**Arabic Title:**
> ❌ [original]
> ✅ [optimized — added: +[kw1], +[kw2]]

**Arabic Bullets:**
> ❌ 1. [original]
> ✅ 1. [optimized — added: +[kw1], +[kw2]]

**Backend:**
> ❌ [original — X bytes]
> ✅ [optimized — Y bytes]

## 🟢 Issues Fixed
1. [what was wrong → how we fixed it]

## 🟡 Recommendations (requires seller action)
1. [image improvements, Brand Content additions, pricing — things the skill can't rewrite]

## 🟢 What Was Already Working
1. [positive aspects preserved]
```

### Competitive Comparison (if requested)

| Dimension | Your Listing | Competitor 1 | Competitor 2 | Competitor 3 |
|-----------|-------------|-------------|-------------|-------------|
| Arabic title score | /15 | /15 | /15 | /15 |
| English title score | /10 | /10 | /10 | /10 |
| Arabic bullets | /15 | /15 | /15 | /15 |
| English bullets | /10 | /10 | /10 | /10 |
| Description | /10 | /10 | /10 | /10 |
| Imagery | /15 | /15 | /15 | /15 |
| Brand Content | /10 | /10 | /10 | /10 |
| SEO Coverage | /15 | /15 | /15 | /15 |
| **Total** | **/100** | **/100** | **/100** | **/100** |

### Key Principles

1. The seller's workflow is: **copy the listing → paste into noon Seller Central → done.** The diagnostic explains WHY those specific words were chosen, but the listing itself must stand alone as a complete, ready-to-use deliverable. Never output only a report without the actual listing copy.

2. **Output language must match the target marketplace.**
   - noon.sa (KSA) → Arabic-first, MSA, English secondary
   - noon.ae (UAE) → Arabic + English roughly balanced, MSA + Gulf-friendly English
   - noon.com (EGY) → Arabic-first, Egyptian dialect acceptable in body copy, English secondary
   The entire output (listing copy AND diagnostic section) must follow this rule, regardless of what language the user is speaking in the conversation.

3. **Arabic title leads.** Reverse-order listings (English-first on noon KSA) systematically underperform in Arabic search; the language preference ratio on noon.sa is roughly 70% Arabic / 30% English.

## Integration with noon-keyword-research

This skill works best when chained with `noon-keyword-research`:

```
Step 1: "Research keywords for portable blender on noon.sa"
   → noon-keyword-research returns bilingual keyword list with Arabic ratio + competitors

Step 2: "Now create a noon listing using those keywords. Product: 380ml BPA-free, USB-C. Tone: Family."
   → noon-listing-optimization Mode A generates Arabic-first listing with full coverage
```

## Tone Presets

| Tone | Arabic register | English register | Use when |
|------|------------------|-------------------|----------|
| Professional | فصحى معاصرة, no colloquial | Crisp, technical | Electronics, B2B, premium |
| Friendly | فصحى مبسطة with light Gulf warmth | Conversational | Home, kitchen, kids, beauty |
| Premium | فصحى راقية, luxurious vocabulary | Editorial, evocative | Luxury fashion, perfume, jewelry |
| Family | فصحى آمنة مع لمسة خليجية | Warm, family-safe | Kids, baby, family hygiene, modest fashion |

## Limitations

This skill uses publicly available data from noon product pages and web search. It cannot:

- Access noon Seller Central backend search-term analytics
- Confirm exact keyword search volumes for noon
- See conversion rate or PPC performance
- Validate FBN eligibility for the SKU

When the user needs precise data, recommend pairing with noon's own Seller Central brand analytics, or a paid MENA market intelligence tool.

---

_Built for the noon marketplace — KSA, UAE, Egypt. Default locale noon.sa unless the user specifies otherwise._
