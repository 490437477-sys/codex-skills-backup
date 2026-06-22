# Ozon EAC / GOST Compliance Checklist

Used by: ozon-niche-finder, ozon-product-research, ozon-listing-optimization.

Quick reference for product compliance requirements for selling on Ozon. Most products entering the Russian market need EAC (Eurasian Conformity) certification. Rules update frequently; verify with the latest regulations.

## What is EAC

EAC (Eurasian Conformity, 械胁褉邪蟹懈泄褋泻懈泄 蟹薪邪泻 褋芯芯褌胁械褌褋褌胁懈褟) is the mandatory conformity mark for products sold in the Eurasian Economic Union (EAEU / 袨卸薪芯胁械褋懈泄褋泻懈泄 褝泻芯薪芯屑懈褔械褋泻懈泄 褋芯褞蟹): Russia, Belarus, Kazakhstan, Armenia, Kyrgyzstan.

## Product categories and requirements

### Electronics and electrical equipment (TR CU 004/2011, TR CU 020/2011)

Required for: phones, tablets, computers, appliances, lighting, batteries, power tools.

| Item | Requirement | Lead time | Cost (RUB) |
|------|-------------|-----------|------------|
| Single-SKU consumer electronics | EAC certificate (single shipment) | 2-6 weeks | 20000-60000 |
| High-volume serial production | EAC certificate (series, 1-3 years) | 4-8 weeks | 50000-150000 |
| Phones, tablets with WiFi/BT | EAC + FSB notification (encryption) | 8-16 weeks | 80000-200000 |

### Toys (TR CU 008/2011)

Required for: kids toys, board games, dolls, soft toys, electric toys.

| Item | Requirement | Lead time | Cost (RUB) |
|------|-------------|-----------|------------|
| Kids toys (age 0-3) | EAC + testing per TR CU 008 | 4-8 weeks | 25000-70000 |
| Older kids toys (3-14) | EAC + testing per TR CU 008 | 4-8 weeks | 20000-60000 |

### Cosmetics and personal care (TR CU 009/2011)

Required for: skincare, haircare, makeup, perfume, deodorant, soap.

| Item | Requirement | Lead time | Cost (RUB) |
|------|-------------|-----------|------------|
| Cosmetics (general) | EAC + safety assessment + notification | 6-12 weeks | 40000-120000 |
| Perfume with alcohol | EAC + special notification | 8-16 weeks | 60000-150000 |

### Food and supplements

Required for: packaged food, beverages, dietary supplements, baby food.

| Item | Requirement | Lead time | Cost (RUB) |
|------|-------------|-----------|------------|
| Packaged food | EAC + Rospotrebnadzor registration | 12-24 weeks | 80000-200000 |
| Dietary supplements | EAC + Roszdravnadzor registration | 16-24 weeks | 100000-300000 |
| Baby food | EAC + extra safety testing | 16-30 weeks | 150000-400000 |

### Apparel and textiles (TR CU 017/2011)

Required for: clothing, footwear, textiles.

| Item | Requirement | Lead time | Cost (RUB) |
|------|-------------|-----------|------------|
| Adult apparel | EAC + GOST labeling | 2-4 weeks | 15000-40000 |
| Kids apparel (0-14) | EAC + extra safety testing | 4-8 weeks | 25000-70000 |
| Footwear | EAC + GOST labeling | 2-4 weeks | 15000-40000 |

### Medical devices (varies)

High friction category. Most medical devices require Roszdravnadzor registration (federal medical device registry). Lead times 6-18 months. Often not viable for cross-border sellers.

### Other regulated categories

| Category | TR CU number | Lead time | Notes |
|----------|--------------|-----------|-------|
| Auto parts | TR CU 018/2011 | 4-8 weeks | Vehicle type approval needed |
| Furniture | TR CU 025/2012 | 2-6 weeks | Adult / kids furniture differ |
| Packaging | TR CU 005/2011 | 2-4 weeks | Mostly label requirement |
| Machinery | TR CU 010/2011 | 4-8 weeks | For industrial / large equipment |
| Low-voltage equipment | TR CU 004/2011 | 4-8 weeks | Same as electronics above |

## Country-specific add-ons

### Belarus (Ozon.by)

Generally follows EAEU rules. Same EAC certificate accepted.

### Kazakhstan (Ozon.kz)

Generally follows EAEU rules. Same EAC certificate accepted. Some categories need additional KZ-specific certification (e.g. alcohol, certain chemicals).

## Practical recommendations for cross-border sellers

1. **Use a Russian certification agent**: certified labs handle testing + paperwork. Examples: ExpertCenter, Certification-Russia, Test-Russia. Cost 15000-100000 RUB per SKU depending on category.

2. **EAC certificate validity**:
   - Single-shipment: valid for one import only
   - Series certificate: 1-5 years depending on category
   - For high-volume sellers, series certificate is cheaper per unit

3. **Russian labeling requirements**:
   - Russian language on package
   - Country of origin
   - Manufacturer / importer info
   - EAC mark on package
   - Care instructions (for apparel)
   - Composition / ingredients (for food, cosmetics)
   - Manufacturing date / batch

4. **Categories to AVOID if you do not have local compliance partner**:
   - Medical devices
   - Food and supplements (especially baby food)
   - Anything with alcohol (perfume, beverages)
   - Anything with lithium batteries (special handling + FSB notification)

5. **Categories with LOW compliance friction** (good for first-time cross-border):
   - Apparel and textiles (TR CU 017/2011, low cost)
   - Home decor (non-electrical)
   - Stationery, bags, accessories
   - Non-powered kitchenware
   - Some electronics accessories (chargers, cables - TR CU 004/2011 but simple)

## Documentation to keep ready

- Commercial Invoice
- Packing List
- Certificate of Origin (COO)
- EAC certificate (or pending application)
- Russian-language product label and manual
- Test reports (per TR CU category)
- Russian Importer of Record details (or local partner)
- Russian-language safety data sheet (for chemicals, cosmetics)

## Use cases in skills

- **ozon-niche-finder**: reject niches with > 6-week compliance lead time unless user has local partner
- **ozon-product-research**: include compliance cost in margin calculation
- **ozon-listing-optimization**: ensure listing mentions all certifications (builds trust)
