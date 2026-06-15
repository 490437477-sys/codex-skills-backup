---
name: ozon-listing-optimization
description: "Ozon (Озон) listing builder and optimizer for Russian-market sellers. Two modes: (A) Create — build keyword-optimized Russian listings using keyword lists + product info + AI copywriting; (B) Optimize — audit existing Ozon listings, find Russian keyword gaps, score across 8 dimensions (title, rich content, attributes, images, pricing, reviews, SEO, localization), and rewrite with missing keywords. Integrates with $ozon-keyword-research. Respects Ozon-specific rules: 200-char title limit, rich content module, обязательные атрибуты, EAC compliance. Use when the user asks: Ozon listing create, ozon怎么写标题, ozon listing audit, Ozon rich content, оптимизация карточки Озон, как создать листинг на Озоне, listing rewrite Russian, Russian product description for Ozon, Ozon SEO, Ozon атрибуты, or any Ozon listing creation/optimization task."
metadata: {"emoji":"📝","category":"ozon"}
---

# Ozon Listing Optimization 📝

Build Russian keyword-optimized Ozon listings from scratch, or audit and optimize existing ones. No API key — works out of the box.

## Two Modes

| Mode | When to Use | Input | Output |
|------|-------------|-------|--------|
| **A — Create** | Building a new Ozon listing | Russian keywords and/or competitor URLs/SKUs + product info + tone | Full Russian listing copy + keyword coverage score |
| **B — Optimize** | Improving an existing Ozon listing | Ozon SKU or URL (+ optional keywords or competitor URLs) | Optimized Russian listing + audit report + gap analysis |

## Mode A — Three Ways to Start

| Input Source | How it Works |
|-------------|-------------|
| **Russian Keywords** | User provides Russian keyword list → skill prioritizes and generates listing |
| **Competitor URLs/SKUs** | User provides 1-3 competitor Ozon URLs → skill fetches their listings, extracts their Russian keywords, then generates a listing that covers all their keywords and more |
| **Both** | User provides keywords + competitors → skill merges both sources for maximum coverage |

## Capabilities

- **Russian keyword-driven listing generation**: Import keywords (from $ozon-keyword-research, manual list, or extracted from competitor Ozon listings), rank by priority, generate Russian copy that maximizes keyword coverage
- **Competitor keyword extraction**: Fetch competitor Ozon listings and automatically extract their title/description/attribute keywords as your baseline
- **8-dimension audit & scoring**: Title, Rich Content (HTML-описание), Bullet points, Attributes (атрибуты), Images, Pricing, Reviews, Russian SEO coverage
- **Russian keyword coverage tracking**: Visual map showing which Russian keywords appear in title / rich-content / bullets / attributes / missing
- **Ozon-specific attribute filling**: Detects and reminds about обязательные атрибуты per category (бренд, страна производства, состав, размер, цвет, etc.)
- **Tone selection**: Профессиональный / Дружелюбный / Срочный / Премиум — affects AI copywriting style in Russian
- **Competitive benchmarking**: Compare your Ozon listing against competitors
- **Multi-marketplace**: Ozon.ru (main), Ozon.kz (Kazakhstan), Ozon.by (Belarus)

## Usage Examples

### Mode A — Create from Keywords

```
Create an Ozon listing for a portable blender. Keywords: портативный блендер, блендер для смузи, USB аккумулятор, дорожный блендер, персональный блендер. Material: BPA-free Tritan. Color: Белый. Capacity: 380 мл. Tone: Дружелюбный.
```

```
У меня есть эти ключевые слова из исследования: [список]. Товар: силиконовый набор кухонных принадлежностей, 12 предметов, термостойкость до 260°C. Создай полный листинг для Ozon.
```

### Mode A — Create from Competitor Listings

```
Хочу продавать мужскую футболку на Ozon. Вот 3 конкурента: https://www.ozon.ru/product/..., https://www.ozon.ru/product/..., https://www.ozon.ru/product/.... Мой товар: 100% хлопок, 6 цветов, XS-XL, принт. Проанализируй их листинги и создай лучше. Тон: Дружелюбный.
```

### Mode A — Create from Keywords + Competitors

```
Используй $ozon-keyword-research для ключевых слов "портативный блендер", также проанализируй этих конкурентов: https://www.ozon.ru/product/.... Объедини все ключевые слова и создай листинг. Товар: 380 мл, USB-C, BPA-free Tritan. Тон: Профессиональный.
```

### Mode B — Optimize Existing

```
Проведи аудит листинга https://www.ozon.ru/product/... на Ozon.ru
```

```
Оптимизируй листинг https://www.ozon.ru/product/... используя эти ключевые слова: беспроводные наушники, bluetooth гарнитура, наушники для спорта — покажи что отсутствует и перепиши
```

---

## Mode A Workflow — Create Listing from Keywords

### Step A1: Collect Russian Keywords

Keywords can come from four sources (use one or combine multiple):

1. **From $ozon-keyword-research** (recommended): Run Russian keyword research first, then feed results directly. Output is Russian long-tail keywords with declensions + commercial prefixes.
2. **From competitor Ozon listings**: Fetch 1-3 competitor URLs, extract title + description + attributes, mine Russian keywords.
3. **Manual list**: User pastes Russian keywords directly.
4. **Combined**: Run keyword research + competitor analysis, merge & dedupe.

### Step A2: Generate Russian Listing Copy

For each listing section, follow Ozon-specific rules:

#### Title (Заголовок)

- **Max 200 characters** (Ozon hard limit, but target 120-160 for best mobile display)
- Russian only — title is the most important SEO field
- Structure: **[Бренд] [Тип товара] [Модель/Ключевая характеристика 1] [Характеристика 2] [Целевое использование]**
- Example: **"Беспроводные наушники XIAOMI Redmi Buds 5 Pro Bluetooth 5.3 с активным шумоподавлением для спорта и путешествий"**
- Place top 3 Russian keywords (highest search volume) within first 80 characters
- Avoid emoji, ALL-CAPS, English-only titles
- Numbers & units use Russian conventions (380 мл, not 380ml)

#### Rich Content (HTML-описание / Rich content)

- Ozon supports HTML in the description field
- Recommended structure:
  - H2 with main keyword
  - 2-3 short paragraphs of product benefits (in Russian, native quality)
  - Bullet list (use `<ul><li>`) of key features
  - Specifications table (use `<table>`)
  - FAQ section (3-5 questions buyers actually ask)
- Length: target 800-1500 characters; max ~3000 (mobile readability)
- **Russian language quality is critical** — many Chinese sellers have weak MTL Russian. Native-quality is a clear competitive advantage.

#### Bullet Points (Характеристики / Ключевые особенности)

- Ozon uses structured attribute fields, not freeform bullets like Amazon
- "Ключевые особенности" (key features) — 5-7 short Russian phrases
- Each: 50-80 chars
- Cover remaining high-priority Russian keywords

#### Attributes (Атрибуты / Характеристики товара)

- **Mandatory per category**: бренд, страна производства, состав, цвет, размер (varies by category)
- Use $ozon-compliance-checklist to verify required attributes
- Fill ALL available attributes — incomplete listings rank lower
- Use full official Russian terms (e.g. "Синий" not "СИН"; "Хлопок 100%" not "Cotton")

### Step A3: Keyword Coverage Scoring

After generating copy, score keyword coverage:

| Russian Keyword | In Title | In Rich Content | In Attributes | Status |
|-----------------|----------|-----------------|---------------|--------|
| беспроводные наушники | ✅ | ✅ | ✅ | 🟢 Covered |
| bluetooth гарнитура | ✅ | ❌ | ❌ | 🟡 Partial |
| наушники для спорта | ❌ | ✅ | ❌ | 🟡 Partial |
| шумоподавление | ❌ | ✅ | ✅ | 🟢 Covered |
| IPX4 защита | ❌ | ❌ | ❌ | 🔴 Missing |

### Step A4: Compliance Pre-check

Before publishing, verify:

- [ ] EAC mark mentioned (if required category)
- [ ] Country of origin in attributes (Страна производства)
- [ ] All mandatory attributes filled
- [ ] Russian-language descriptions (no English/Chinese left)
- [ ] No prohibited claims (e.g. "лечит", "100% безопасно" without certification)
- [ ] Image requirements met (1000x1000 min, white background for main)

### Output (Mode A)

```
# ✅ Ready-to-Publish Listing — Ozon.ru

## Title (Заголовок)
```
Беспроводные наушники XIAOMI Redmi Buds 5 Pro Bluetooth 5.3 активное шумоподавление IPX4 для спорта и путешествий белый
```
*(180 chars — copy this directly into Ozon seller panel → Title)*

## Rich Content (HTML-описание)
```html
<h2>Беспроводные наушники XIAOMI Redmi Buds 5 Pro</h2>
<p>Наушники с активным шумоподавлением и Bluetooth 5.3 для тех, кто ценит чистый звук...</p>
<ul>
  <li><b>Активное шумоподавление</b> до 35 дБ</li>
  <li><b>Bluetooth 5.3</b> — стабильное соединение без задержек</li>
  <li><b>IPX4</b> — защита от пота и дождя для спорта</li>
  <li><b>До 28 часов</b> работы с зарядным кейсом</li>
  <li><b>Белый цвет</b> — минималистичный дизайн</li>
</ul>
<h3>Технические характеристики</h3>
<table>
  <tr><td>Тип подключения</td><td>Bluetooth 5.3</td></tr>
  <tr><td>Время работы</td><td>до 28 ч (с кейсом)</td></tr>
  <tr><td>Защита</td><td>IPX4</td></tr>
  <tr><td>Вес</td><td>4.5 г (один наушник)</td></tr>
  <tr><td>Страна производства</td><td>Китай</td></tr>
</table>
<h3>Часто задаваемые вопросы</h3>
<p><b>Подходят ли для спорта?</b> Да, защита IPX4 выдерживает пот и дождь.</p>
<p><b>Можно ли подключить к iPhone?</b> Да, поддерживает любые устройства с Bluetooth.</p>
```
*(Copy this HTML into Ozon seller panel → Rich Content)*

## Ключевые особенности (Bullets)
1. Bluetooth 5.3 — стабильное соединение без задержек
2. Активное шумоподавление до 35 дБ
3. До 28 часов работы с зарядным кейсом
4. Защита от воды IPX4 — для спорта и путешествий
5. Белый цвет — минималистичный дизайн

## Атрибуты (заполните в панели)
- Бренд: XIAOMI
- Страна производства: Китай
- Тип подключения: Bluetooth
- Время работы: до 28 ч
- Цвет: Белый
- Степень защиты: IPX4
- Состав: пластик, силикон

## Backend Keywords (Ключевые слова для поиска)
`наушники беспроводные, bluetooth наушники, наушники для спорта, наушники с шумоподавлением, беспроводные наушники для телефона, наушники bluetooth 5.3, наушники IPX4, наушники в кейсе, спортивные наушники, наушники белые`

---

# 📊 How We Built This Listing (Diagnostic)

**Marketplace:** Ozon.ru | **Tone:** Дружелюбный | **Keywords imported:** 47
**Title characters:** 162/200 | **Rich Content characters:** 1240

## Keyword Coverage: 89% (42/47)

| Keyword | Volume | In Title | In Rich Content | In Attributes | Status |
|---------|--------|----------|-----------------|---------------|--------|
| беспроводные наушники | Высокий | ✅ | ✅ | ✅ | 🟢 Covered |
| bluetooth наушники | Высокий | ✅ | ✅ | ✅ | 🟢 Covered |
| ... | ... | ... | ... | ... | ... |
| наушники в кейсе | Низкий | ❌ | ❌ | ✅ | 🟢 Covered |
| наушники белые | Низкий | ✅ | ✅ | ❌ | 🟢 Covered |
| bluetooth 5.3 | Средний | ✅ | ✅ | ✅ | 🟢 Covered |

## Keyword Priority Breakdown
🔴 Primary (Title): беспроводные наушники, bluetooth наушники, шумоподавление
🟡 Secondary (Rich Content): наушники для спорта, IPX4 защита, время работы
🟢 Tertiary (Attributes): страна производства, цвет, тип подключения
⚪ Backend: наушники в кейсе, спортивные наушники, bluetooth 5.3

## ⚠️ Compliance Pre-check
- ✅ EAC mark mentioned (if applicable)
- ✅ Country of origin: Китай
- ✅ All mandatory attributes filled
- ✅ Russian descriptions
- ✅ No prohibited claims
- ✅ Image spec (1000x1000 min) — REMINDER for seller

## 🔴 Issues / Recommendations
1. Missing image of в комплекте (charging case, кабель, инструкция)
2. Consider adding a video review embed (boosts conversion 15-30% on Ozon)
3. A/B test title with "беспроводные наушники для телефона" vs "bluetooth наушники"
```

### Mode B Output — Audit + Optimized Listing

```
# ✅ Optimized Listing — Ready to Use

## Title
[optimized Russian title — copy this directly into Ozon seller panel]

## Rich Content (HTML)
[optimized HTML — copy this into Ozon Rich Content field]

## Ключевые особенности
1. [bullet]
2. [bullet]
...

## Атрибуты (suggested)
- [attr1]: [value]
- [attr2]: [value]
...

## Backend Keywords
[comma-separated Russian keywords]

---

# 📊 Audit Report: [Ozon SKU or URL]

**Product:** [title] | **Brand:** [brand]
**Price:** [₽ price] | **Rating:** [stars] ([count] reviews)

## Score: [X/100] → [Y/100] (after optimization)

| Dimension | Before | After | Key Change |
|-----------|--------|-------|------------|
| Title (Russian SEO) | /15 | /15 | [what changed] |
| Rich Content (HTML-описание) | /15 | /15 | [what changed] |
| Атрибуты (Attributes) | /15 | /15 | [what changed] |
| Ключевые особенности (Bullets) | /10 | /10 | [what changed] |
| Images | /15 | — | [recommendation only] |
| Pricing | /10 | — | [observation] |
| Reviews | /15 | — | [observation] |
| Russian SEO Coverage | /10 | /10 | [what changed] |

## Russian Keyword Coverage: [X]% → [Y]%

| Russian Keyword | Before | After | Where Added |
|-----------------|--------|-------|-------------|
| беспроводные наушники | ❌ | ✅ | Title + Rich Content |
| bluetooth наушники | ✅ Title only | ✅ Title + Attributes | Атрибуты |

## What Changed (Before → After)

**Title:**
> ❌ [original]
> ✅ [optimized]

**Rich Content:**
> ❌ [original]
> ✅ [optimized — added: +[kw1], +[kw2]]

## 🔴 Issues Fixed
1. [what was wrong → how we fixed it]

## 🟡 Recommendations (requires seller action)
1. [image improvements, video, pricing — things the skill can't rewrite]

## 🟢 What Was Already Working
1. [positive aspects preserved]
```

### Competitive Comparison (if requested)

```
| Dimension | Your Listing | Competitor 1 | Competitor 2 | Competitor 3 |
|-----------|-------------|-------------|-------------|-------------|
| Title score | /15 | /15 | /15 | /15 |
| Rich Content | /15 | /15 | /15 | /15 |
| Атрибуты completeness | XX% | XX% | XX% | XX% |
| Image count | [N] | [N] | [N] | [N] |
| Russian keyword coverage | X% | X% | X% | X% |
| Price | ₽X | ₽X | ₽X | ₽X |
| Rating | [stars] | [stars] | [stars] | [stars] |
| **Total** | **/100** | **/100** | **/100** | **/100** |
```

### Key principles

1. The seller's workflow is: **copy the listing → paste into Ozon seller panel → done.** The diagnostic section explains WHY those specific words were chosen, but the listing itself must stand alone as a complete, ready-to-use deliverable. Never output only a report without the actual listing copy.

2. **Output language must match the target marketplace.** Ozon.ru → Russian (default). Ozon.kz → Russian/Kazakh. Ozon.by → Russian. The entire output (listing copy AND diagnostic section) must be in Russian, regardless of what language the user is speaking in the conversation.

## Integration with Other Ozon Skills

This skill works best when chained:

```
Step 1: "Research keywords for портативный блендер on Ozon"
   → $ozon-keyword-research returns Russian keyword list with declensions + commercial prefixes

Step 2: "Now create an Ozon listing using those keywords. Product: 380 мл BPA-free блендер, USB-C rechargeable. Tone: Дружелюбный."
   → $ozon-listing-optimization Mode A uses the keywords to generate Russian copy

Step 3: (optional) "$ozon-product-research validate this opportunity vs alternatives"

Step 4: (optional) "$ozon-compliance-checklist verify EAC requirements"
```

## References

- `references/ozon_listing_attributes.md` — обязательные атрибуты по категориям
- `references/ozon_rich_content_html.md` — Ozon Rich Content HTML规范

## Limitations

This skill uses publicly available data from Ozon product pages and Russian SEO patterns. It cannot access Ozon's internal search analytics, advertising data, or seller panel data. For deeper analytics, integrate with MPStats, Moneyplace, or SellerExpert.
