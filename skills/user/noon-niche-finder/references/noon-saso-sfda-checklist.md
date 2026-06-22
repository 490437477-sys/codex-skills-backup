# noon MENA Compliance Checklist (SASO, SFDA, ESMA, GOEIC, IECEE)

Used by: noon-niche-finder, noon-product-research, noon-listing-optimization.

Quick reference for product compliance requirements across noon marketplaces. Always verify with the latest Saudi/UAE/Egypt regulation; rules update frequently.

## Saudi Arabia (noon.sa)

### SASO (Saudi Standards, Metrology and Quality Org)

Most non-food products require a SASO Certificate of Conformity (CoC) or Product Safety Certificate. Apply via SABER platform.

| Category | Requirement | Lead time | Cost (SAR) |
|----------|-------------|-----------|------------|
| Electrical appliances | SASO IECEE + CoC | 4-8 weeks | 1500-5000 |
| Toys | SASO + GCC conformity | 4-8 weeks | 2000-6000 |
| Textiles & apparel | Care label + CoO | 1-2 weeks | 200-500 |
| Cosmetics | SFDA notification (see below) | 6-12 weeks | 3000-8000 |
| Food contact | SFDA + SASO | 8-16 weeks | 4000-12000 |
| Auto parts | SASO + GCC | 6-10 weeks | 2500-7000 |

### SFDA (Saudi Food and Drug Authority)

Mandatory for:
- Food and beverages
- Cosmetics and personal care
- Medical devices
- Pharmaceuticals
- Dietary supplements

Notification process: SFDA portal, requires ingredient list, label artwork, manufacturer authorization letter. Lead time 6-12 weeks. Cost 3000-12000 SAR per SKU.

### IECEE (for electrical products)

CB scheme test report accepted. Apply via SASO. Required for: phone chargers, batteries, kitchen appliances, lighting, AV equipment.

## UAE (noon.ae)

### ESMA / MOIAT (Emirates Authority for Standardization)

ECAS (Emirates Conformity Assessment Scheme) certificate required for most regulated products. Process is generally faster than Saudi:

| Category | Requirement | Lead time | Cost (AED) |
|----------|-------------|-----------|------------|
| Electrical | ECAS + IECEE | 2-6 weeks | 1500-4000 |
| Toys | ECAS + GCC | 3-6 weeks | 1500-4000 |
| Cosmetics | MoHAP notification | 4-8 weeks | 2500-6000 |
| Food | Abu Dhabi/Dubai Municipality | 4-10 weeks | 3000-8000 |
| Perfume (alcohol-based) | Special license | 6-12 weeks | 5000-15000 |

### MoHAP (Ministry of Health and Prevention)

Cosmetic and health product registration. UAE is generally more lenient than KSA for cosmetics (faster, cheaper), making it a good first market.

### TRA (Telecommunications and Digital Government)

Required for: phones, tablets, smartwatches, WiFi/Bluetooth devices, radio equipment. Type approval via TRA portal.

## Egypt (noon.com)

### GOEIC (General Organization for Export and Import Control)

Required for many imported manufactured goods. Factories must be registered with GOEIC; specific products require pre-shipment inspection.

| Category | Requirement | Lead time | Cost (EGP) |
|----------|-------------|-----------|------------|
| Most manufactured goods | GOEIC registration | 8-16 weeks | 15000-40000 |
| Food | NFSA registration | 12-20 weeks | 25000-60000 |
| Cosmetics | EDA notification | 6-12 weeks | 15000-35000 |
| Toys | EOS conformity | 6-10 weeks | 10000-25000 |

### NFSA (National Food Safety Authority)

Food and beverage registration. Long lead time; plan 4-6 months ahead.

### EDA (Egyptian Drug Authority)

Cosmetic and supplement notification.

## Practical recommendations

1. **Default for cross-border sellers without local importer**: ship to noon FBN only after local importer secures compliance. noon does not provide import services for restricted categories.

2. **Faster market entry path**: launch first on noon.ae (cheaper, faster compliance for most categories), then expand to noon.sa once SASO/SFDA is in place. Egypt is the slowest entry market.

3. **Documentation to keep ready**:
   - Commercial Invoice
   - Packing List
   - Certificate of Origin (COO)
   - Manufacturer Authorization Letter
   - Product Compliance Certificate (SASO CoC, ECAS, etc.)
   - Test Reports (per category)
   - SFDA notification letter (for cosmetics/food)
   - SFDA-approved Arabic label artwork

4. **Categories to AVOID if you do not have local compliance partner**:
   - Cosmetics (high friction)
   - Food (very high friction)
   - Medical devices (effectively impossible without local partner)
   - Anything with lithium batteries (special handling required)

5. **Categories with LOW compliance friction** (good for first-time cross-border):
   - Apparel and textiles
   - Home decor (non-electrical)
   - Stationery
   - Non-powered kitchenware
   - Bags and luggage

## Use cases in skills

- **noon-niche-finder**: reject niches with > 6-week compliance lead time unless user has local importer
- **noon-product-research**: include compliance cost and lead time in margin calculation
- **noon-listing-optimization**: ensure listing mentions all compliance certifications (builds trust)
