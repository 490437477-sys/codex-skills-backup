---
name: temu-listing-optimization
description: "TEMU listing builder and optimizer for cross-border sellers. Two modes: (A) Create — build keyword-optimized title + bullets + Rich Description from a keyword list (from temu-keyword-research) and product specs; (B) Optimize — audit an existing TEMU listing by URL, find keyword gaps, score across 8 dimensions (title length, attribute fill, image count, video presence, price positioning, rating, return-rate signal, SEO coverage), and rewrite with missing keywords. Use when: (1) creating a new TEMU listing, (2) auditing an existing TEMU listing, (3) checking TEMU keyword coverage in title/attributes, (4) generating TEMU-compliant title and bullet copy, (5) improving CTR for a TEMU listing, (6) preparing a listing for TEMU launch. Strongly recommend chaining with temu-keyword-research for keyword input."
metadata: {"category":"cross-border-ecommerce","platform":"temu"}
---

# TEMU Listing Optimization

Build keyword-optimized TEMU listings from scratch, or audit and optimize existing ones. No API key required.

## When to Use This Skill

Use this skill whenever the user:
- Has a product ready and wants to write the TEMU listing (title, bullets, description)
- Has an existing TEMU listing URL and wants SEO/conversion improvements
- Wants to compare their TEMU listing against competitors
- Asks about TEMU title optimization, TEMU bullet points, TEMU Rich Description
- Mentions TEMU上架 / TEMU listing 优化 / TEMU 标题 / TEMU 主图

Do NOT use this skill for: Amazon listings (use `amazon-listing-optimization`), product selection (use `temu-product-research`), keyword discovery (use `temu-keyword-research`).

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Create** | Building a new listing | Keywords + product info + tone | Full listing copy + coverage score + suggestions |
| **B — Optimize** | Improving existing listing | TEMU URL or product ID (+ optional keywords/competitors) | Optimized listing + audit report + gap analysis |

## TEMU-Specific Listing Structure (Critical)

Unlike Amazon''s 200-char title and 5 bullets, TEMU has its own structure:

| Field | Limit | Weight | Notes |
|---|---|---|---|
| **Title** | **60-100 chars** (strict) | 60% of SEO | Primary keyword must be in first 30 chars |
| **Bullets (key selling points)** | 5-8 lines, 30-50 chars each | 20% | Front-loaded benefits, not features |
| **Rich Description** | 500-1000 chars + 3-5 images | 15% | Text + image combo, not A+ Content |
| **Category attributes** | 30-50+ structured fields | Hidden 30%+ | Often skipped, big SEO miss |
| **Images** | 6-9 (1:1 ratio, 800x800+) | CTR driver | First image is THE most important |
| **Video** | 15-30 sec optional | Algo boost 3-5x | Strongly recommended |
| **Backend keywords** | DOES NOT EXIST | n/a | All SEO goes in title + attributes |
| **A+ Content** | No | n/a | Use Rich Description instead |

## Mode A — Create Listing

### Step A1: Collect Inputs

Need from user (ask if missing):
- **Product name and category** (e.g. "4DOF robotic arm kit, category: Toys & Hobbies > STEM")
- **5-20 target keywords** (ideally from `temu-keyword-research`; user can paste list)
- **Key specs**: dimensions, material, color, count, age range
- **Target marketplace** (us/uk/de/...) and target audience
- **Tone**: Professional / Friendly / Urgent (TEMU default is Friendly)
- **Competitor URLs** (optional, 1-3 for cross-validation)

### Step A2: Generate Title

Apply the formula:
```
[Brand or blank] + [Primary keyword] + [Key modifier] + [Key modifier] + [Spec] + [Audience/use case]
```

Constraints:
- **60-100 chars** (strict — TEMU truncates over 100)
- **No keyword stuffing** (no "robot arm robotic arm")
- **No promotional words** ("best", "#1", "sale", "free shipping")
- **No emoji or ALL CAPS** (trust penalty)
- **First 30 chars must include the primary keyword**

Generate 3 title candidates ranked by keyword coverage + readability. Pick the best.

### Step A3: Generate Bullets (Key Selling Points)

5-8 short bullets, each 30-50 chars. Format: `[Benefit]: [Feature]`

Examples:
- `STEM Learning: 4DOF mechanical arm kit`
- `4 Servo Motors: MG90S metal gear stable`
- `Joystick Control: Plug-and-play USB wired`
- `DIY Assembly: Improve hands-on skills`
- `Gift for Teens: Ages 13+ educational toy`

### Step A4: Generate Rich Description

500-1000 chars combining:
- Opening hook (1 sentence)
- 3-4 product benefit paragraphs (50-100 chars each)
- Specs line (dimensions, material, weight)
- Compliance positioning (age range, safety notes)
- Call to action

Recommend 3-5 image ideas to pair with text (lifestyle, exploded view, in-use, comparison, package contents).

### Step A5: Recommend Attributes

Based on category, recommend the 5-10 most important attributes to fill:
- Color
- Material
- Brand
- Age range (for STEM/toys)
- Dimensions (LxWxH)
- Weight
- Power source (battery / USB / AC)
- Package includes
- Country of origin
- Certification (FCC, CE)

Tell the user to fill ALL available attributes in TEMU Seller Center (not just the recommended ones).

### Step A6: Output Format

```markdown
# ? TEMU Listing — Ready to Use

## Title
[optimized title, 60-100 chars]

## Key Selling Points (Bullets)
1. [30-50 chars]
2. [30-50 chars]
3. [30-50 chars]
4. [30-50 chars]
5. [30-50 chars]

## Rich Description
[500-1000 chars, with [IMAGE 1], [IMAGE 2]... placeholders]

## Recommended Attributes to Fill
- [Attribute 1]: [value]
- [Attribute 2]: [value]
- ...

## Image Brief (6-9 photos, 1:1 ratio)
1. [Main image — product on white, 1:1, 800x800+]
2. [Lifestyle — product in use]
3. [Exploded view — parts labeled]
4. [Scale reference — held in hand or next to coin]
5. [Package contents laid out]
6. [Comparison or feature callout]

## Video Brief (15-30 sec, optional but recommended)
[30-second video script: hook → feature demo → result → CTA]

---

# ?? Diagnostic

**Marketplace**: TEMU [XX] | **Title length**: [X] chars | **Primary keyword**: [kw]
**Keyword coverage**: [X]%

| Keyword | In Title | In Bullets | In Description | Status |
|---------|----------|------------|----------------|--------|
| [kw1] | ? | ? | ? | ?? |
| [kw2] | ? | ? | ? | ?? |
| [kw3] | ? | ? | ? | ?? |

?? Covered in 3+ fields | ?? Covered in 1-2 | ?? Only in description | ?? Missing
```

## Mode B — Optimize Existing Listing

### Step B1: Fetch Listing Data

Use the bundled script to extract data from a TEMU product URL:

```bash
<skill>/scripts/fetch_listing.sh "<temu_product_url>"
```

Extracts:
- Title (length + keyword check)
- Price + currency
- Rating + review count
- Sold count (if visible)
- Bullet points / key selling points
- Rich Description
- Image count
- Video presence
- Category breadcrumb
- Visible attributes

### Step B2: Run 8-Dimension Audit

Score 0-100 across 8 dimensions:

| Dimension | Weight | What to Check |
|---|---|---|
| Title SEO | 20 | 60-100 chars, primary keyword first, no stuffing |
| Bullet effectiveness | 15 | 5-8 bullets, benefit-driven, 30-50 chars each |
| Description completeness | 10 | 500-1000 chars, includes spec + use case + age |
| Image quality + count | 15 | 6-9 images, 1:1, first image clean |
| Video presence | 5 | Yes/No + 15-30 sec |
| Attribute fill rate | 15 | X/30+ filled |
| Price competitiveness | 10 | vs category median |
| Rating + reviews | 10 | ≥4.5 with 50+ reviews ideal |

Total: 100

### Step B3: Identify Keyword Gaps

Compare the listing''s title/bullets/description against:
1. Top 5 competing TEMU listings (extracted via `tavily_extract`)
2. The 10 highest-value keywords from `temu-keyword-research` (if user has it)

Output a table: which keywords are missing, which are weak.

### Step B4: Output Optimized Listing + Audit Report

```markdown
# ? Optimized Listing — Ready to Use

## New Title
[improved title, 60-100 chars, with primary keyword + missing terms]

## New Bullets
1. [improved]
...

## New Description
[improved, with image placeholders]

## New Attributes
[attributes that were missing, with suggested values]

---

# ?? Audit Report: [URL/ID]

**Product**: [title] | **Marketplace**: TEMU [XX]
**Current Price**: $[X] | **Rating**: [stars] ([count] reviews) | **Sold**: [N]

## Score: [X/100] → [Y/100] (after optimization)

| Dimension | Before | After | Key Change |
|---|---|---|---|
| Title SEO | /20 | /20 | +[change] |
| Bullet effectiveness | /15 | /15 | +[change] |
| Description | /10 | /10 | +[change] |
| Images | /15 | /15 | recommendation only |
| Video | /5 | /5 | recommendation only |
| Attribute fill | /15 | /15 | +[N] attributes added |
| Price position | /10 | — | observation only |
| Rating + reviews | /10 | — | observation only |
| **Total** | **/100** | **/100** | |

## Keyword Gaps Found: [N]

| Missing Keyword | Search Volume Est | Recommendation |
|---|---|---|
| [kw1] | [H/M/L] | Add to title |
| [kw2] | [H/M/L] | Add to bullet 3 |
| [kw3] | [H/M/L] | Add to description + attribute |

## What Changed (Before → After)

**Title**: ? [original] → ? [optimized — added: +kw1, +kw2]
**Bullets**: ? [original] → ? [optimized — added: +kw3, +kw4]
**Attributes**: Added 8 missing fields including [color], [material], [age range]

## ?? Issues Fixed
1. Title was 142 chars (truncated) → reduced to 88 chars with stronger keyword front-loading
2. No bullet points visible → added 5 benefit-driven bullets
3. Only 3 images → recommend uploading 6+ (lifestyle, scale, exploded view)
4. Missing 12 category attributes → recommended fill-in

## ?? Recommendations (requires seller action)
1. [Image improvements: 1:1 ratio, white background, lifestyle shot]
2. [Video: 15-30 sec product demo, increases impressions 3-5x]
3. [A/B test price: current $29.99 vs category median $25.99]

## ? What Was Already Working
1. [Positive aspects preserved]
```

## Competitive Comparison Mode

If user provides 1-3 competitor TEMU URLs, run comparison:

| Dimension | Your Listing | Competitor 1 | Competitor 2 | Competitor 3 |
|---|---|---|---|---|
| Title score | /20 | /20 | /20 | /20 |
| Bullets score | /15 | /15 | /15 | /15 |
| Image count | 4 | 8 | 6 | 7 |
| Video | No | Yes | No | No |
| Attribute fill | 8/30 | 22/30 | 18/30 | 25/30 |
| Price | $29.99 | $24.99 | $27.99 | $32.99 |
| Rating | 4.2 (35) | 4.5 (210) | 4.3 (89) | 4.7 (340) |
| **Total** | **/100** | **/100** | **/100** | **/100** |

End with: **"To beat the leader [competitor X], focus on: [top 2-3 actions]"**

## Multilingual Output

Output language MUST match target marketplace:
- TEMU US/UK/CA/AU → English
- TEMU DE/AT → German
- TEMU FR → French
- TEMU IT → Italian
- TEMU ES → Spanish
- TEMU NL → Dutch
- TEMU PL → Polish
- TEMU PT → Portuguese
- TEMU JP → Japanese
- TEMU KR → Korean
- TEMU MX → Spanish (Latin American)
- TEMU BR → Portuguese (Brazilian)

User can speak in any language, but the OUTPUT listing copy and audit must be in the marketplace language.

## Integration with temu-keyword-research

Strongly recommended chain:

```
Step 1: "Research keywords for robotic arm on TEMU US"
   → temu-keyword-research returns 100-200 candidates + top 10 ranked

Step 2: "Create a TEMU listing for my 4DOF robotic arm kit
         using these top 10 keywords: [list]
         Product: MG90S servos, 3D printed, ages 13+, USB wired
         Tone: Friendly"
   → temu-listing-optimization Mode A generates full listing

Step 3: "Audit my live TEMU listing: <URL>
         Compare against these competitors: <URLs>"
   → temu-listing-optimization Mode B returns audit + rewrite
```

## Limitations

- Cannot access TEMU Seller Center directly (no public API for listings)
- Attribute recommendations are category-best-guesses; user must verify in Seller Center
- Image and video recommendations are text briefs, not generated assets (use `imagegen` skill for actual images)
- Some TEMU pages are JS-rendered; the script falls back to a basic extraction

## Resources

- `scripts/fetch_listing.sh`: Extract data from a TEMU product URL
- `references/temu_listing_anatomy.md`: Detailed field-by-field structure guide
- `references/temu_attribute_checklist.md`: Common attributes by category
- `assets/title_formula.md`: Title templates by category
