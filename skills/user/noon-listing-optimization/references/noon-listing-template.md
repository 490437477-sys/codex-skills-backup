# noon Listing Field Template

Use this when generating Mode A listings or rewriting in Mode B. Field limits are approximate and should be verified against the current noon Seller Central schema.

## 1. Field Limits

| Field | Arabic limit | English limit | Notes |
|-------|--------------|---------------|-------|
| Title | 70 chars | 70 chars | Primary keyword leads Arabic |
| Bullet (each) | 100 chars | 100 chars | Benefit header + body |
| Description | 1,500 chars | 1,500 chars | Optional on some categories |
| Backend search terms | 250 bytes total (bilingual) | 250 bytes total (bilingual) | Comma-separated, no duplication |
| Brand Content modules | up to 5 | up to 5 | Optional, recommended for top 20% ASINs |

## 2. Arabic Title Pattern

```
[Primary Arabic keyword] [English brand / model in parentheses] [key modifier]
```

Examples:

- `سماعات لاسلكية (AirPods Pro 2) مع علبة شحن` — primary AR + EN brand
- `خلاط محمول (Portable Blender) USB-C سعة 380 مل` — primary AR + EN descriptor + capacity
- `ساعة ذكية (Smart Watch) مقاومة للماء IP68` — primary AR + EN descriptor + feature

Title rules:

- Primary Arabic keyword first (matches Arabic search)
- English brand / model in parentheses (captures branded English search)
- Modifier (color, capacity, count) at the end
- Avoid emoji, exclamation marks, ALL CAPS, promotional language (e.g. "خصم", "تخفيض" — these get rejected)
- Avoid redundant repetition of the same Arabic keyword twice

## 3. English Title Pattern

```
[English brand / model] [English modifier] [Arabic keyword in parentheses]
```

Examples:

- `AirPods Pro 2 Wireless Earbuds with MagSafe (سماعات لاسلكية)`
- `Portable Blender USB-C 380ml BPA-Free (خلاط محمول)`
- `Smart Watch IP68 Waterproof Fitness Tracker (ساعة ذكية)`

English title rules:

- Brand / model first (matches branded English search)
- Modifiers next
- Arabic keyword at the end in parentheses (captures Arabic search via the English field)

## 4. Arabic Bullet Pattern

```
[2-3 word Arabic benefit header] — [supporting Arabic text, ≤ 80 chars after header]
```

Five bullets, each hitting a different angle:

1. **Main benefit** — what does the product do?
2. **Differentiation** — what makes it special vs. competitors?
3. **Quality / material** — what is it made of?
4. **Use case** — when / where / how to use it?
5. **Package / warranty / trust** — what's in the box, return policy, warranty?

Avoid:

- "Best" / "أفضل" claims without proof (noon's compliance rejects unsubstantiated superlatives)
- Price claims ("أرخص", "أقل سعر")
- Medical / health claims not supported by SFDA registration

## 5. English Bullet Pattern

Mirror of Arabic. Same five angles, English headers + body. English bullets carry technical specs (wattage, voltage, dimensions) that Arabic bullets cannot easily accommodate.

## 6. Arabic Description Pattern

Three paragraphs:

1. **Hook** — 1-2 sentences in MSA, evocative, culturally relevant (e.g. seasonal hook during Ramadan)
2. **Feature walkthrough** — 2-3 sentences, structured, weaving primary + secondary + tertiary keywords
3. **Trust + CTA** — 1-2 sentences, FBN delivery promise, return policy, brand assurance

Tone follows the user-selected preset (Professional / Friendly / Premium / Family).

## 7. English Description Pattern

Mirror of Arabic. English allows longer technical content (specs, certifications, compatibility). Keep the warm opening and trust-closing similar to Arabic.

## 8. Backend Search Terms Pattern

- Bilingual block, comma-separated, no spaces between commas, ≤ 250 bytes total
- No duplication with title (Arabic OR English)
- No duplication within the block
- No brand names (noon has a separate brand field)
- No subjective claims (best, cheap, original — these are not search terms)
- Include transliterations (e.g. both "سماعات لاسلكية" and "لاسلكية" if both are used in search)

Example (approximate, do not exceed 250 bytes):

```
خلاط,خلاط يدوي,خلاط محمول,سفر,رياضة,USB-C,شحن,BPA,Tritan,ميني,blender,mini,portable,travel,USB,rechargeable
```

## 9. Brand Content / A+ Module Patterns

Optional but recommended. up to 5 modules, each with:

- **Module 1: Hero** — product hero shot + 1-line Arabic headline + 1-line English headline
- **Module 2: Feature 1** — image + 30-word Arabic paragraph + 30-word English paragraph
- **Module 3: Feature 2** — same shape
- **Module 4: Comparison chart** (if relevant) — features vs. competitor product
- **Module 5: Trust / lifestyle** — family or lifestyle image + Arabic reassurance + English reassurance

Hijri / seasonal overlays (Ramadan, Eid, Hajj, National Day) live in modules 4-5. Keep them tasteful — explicit "Ramadan Sale" copy is a compliance risk.

## 10. Imagery Brief

When generating recommendations, ask for:

- **Hero image**: product on white background, RTL-safe (logos not mirrored), ≥ 1,500 × 1,500 px
- **Lifestyle image 1**: family / couple / solo user in modest attire, indoor Gulf / Levantine setting
- **Feature image 2**: close-up of key feature (port, button, fabric)
- **Scale image 3**: product held in hand or next to common object
- **Infographic image 4**: feature callouts (3-5 Arabic labels + English labels)
- **Packaging image 5**: in-box contents

Avoid:

- Mixed-gender close-contact imagery
- Alcohol / pork / gambling references
- Suggestive imagery
- Politically charged symbols (regional sensitivities)

## 11. Pre-publish Checklist

- [ ] Arabic title ≤ 70 chars, primary Arabic keyword leads
- [ ] English title ≤ 70 chars, brand first, Arabic keyword at end in parens
- [ ] 5 Arabic bullets, each ≤ 100 chars, no superlative claims
- [ ] 5 English bullets, mirror of Arabic
- [ ] Arabic description ≤ 1,500 chars, MSA tone (or Egyptian if EGY)
- [ ] English description ≤ 1,500 chars
- [ ] Backend search terms ≤ 250 bytes, no duplication
- [ ] ≥ 5 images, RTL-safe, modesty-compliant
- [ ] Brand Content modules present (recommended for top SKUs)
- [ ] Arabic + English keyword coverage ≥ 80%
- [ ] Cultural compliance check passed
