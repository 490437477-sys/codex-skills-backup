# Ozon FBO / FBS Fee Schedule Reference

Used by: ozon-fbo-fbs-calculator, ozon-profit-analyzer, ozon-niche-finder.

Current Ozon FBO (Fulfilled by Ozon) and FBS (Fulfilled by Seller) fee schedule. Always confirm against Ozon Seller Central as fees update periodically. Values below are typical ranges as of 2026.

## Ozon commission (category-based)

| Category | Commission |
|----------|------------|
| Books | 5-15% |
| Electronics accessories | 5-15% |
| Phones, tablets | 4-8% |
| Computers, laptops | 5-10% |
| Clothing, footwear | 10-20% |
| Beauty, health | 10-20% |
| Home, kitchen | 8-15% |
| Toys, kids | 8-15% |
| Sports, outdoors | 8-15% |
| Auto parts | 10-20% |
| Jewelry | 8-15% |
| Grocery (food) | 5-15% |
| Pet supplies | 10-15% |

## FBO storage fee (per unit per 30 days)

| Tier | Dimensions (cm) | Weight (kg) | Peak (Nov-Jan) | Off-peak (Feb-Oct) |
|------|-----------------|-------------|----------------|---------------------|
| Small | <= 25 x 15 x 10 | <= 0.5 | 5 RUB | 3 RUB |
| Medium | <= 45 x 35 x 25 | <= 3 | 12 RUB | 7 RUB |
| Large | <= 70 x 50 x 50 | <= 15 | 25 RUB | 15 RUB |
| Extra-Large | > 70 OR > 15kg | > 15 | 50 RUB | 30 RUB |

### Storage overage surcharges

- **> 60 days**: storage fee x 1.5
- **> 90 days**: storage fee x 2
- **> 180 days**: storage fee x 3 + potential removal
- **> 365 days**: auto-removal ordered, removal fee applies

## FBO last-mile delivery fee (per order)

| Tier | Moscow / SPB (RUB) | Other regions (RUB) | Remote regions (RUB) |
|------|---------------------|---------------------|----------------------|
| Small | 50-90 | 80-150 | 200-400 |
| Medium | 80-150 | 120-200 | 300-500 |
| Large | 150-300 | 200-400 | 500-1000 |
| Extra-Large | 300-700 | 400-1000 | 1000-2500 |

### Last-mile fee add-ons

- **Cash on delivery (COD) handling**: +20-50 RUB per order
- **Heavy package** (> 25 kg): additional +200-500 RUB
- **Remote area delivery** (Far East, Kamchatka): +500-1500 RUB
- **Express delivery** (where available): +100-300 RUB premium
- **Refrigerated delivery**: 2x delivery fee + special packaging cost

## FBS pick-and-pack fee

| Tier | Fee (RUB) |
|------|-----------|
| Small | 30-50 |
| Medium | 50-80 |
| Large | 80-150 |
| Extra-Large | 150-300 |

## FBS shipping label fee

Ozon provides shipping label service (seller hands over to Ozon Rocket / 3PL). Per-order fee:

| Destination | Small (RUB) | Medium (RUB) | Large (RUB) |
|-------------|-------------|--------------|--------------|
| Moscow / SPB | 80-150 | 120-200 | 200-400 |
| Other regions | 150-300 | 200-400 | 400-800 |
| Remote regions | 400-800 | 600-1000 | 1000-2000 |

## Returns processing fee

- FBO returns: free for most categories; seller charged 30-80 RUB if return is seller-fault (defective, wrong item)
- FBS returns: seller ships back label, ~50-150 RUB per return
- Apparel / footwear highest return rate (15-25%)

## Aged inventory surcharge

Storage fees are tiered by age. Plan inventory to clear before aging surcharges kick in.

| Age | Multiplier |
|-----|------------|
| 0-60 days | 1x |
| 61-90 days | 1.5x |
| 91-180 days | 2x |
| 181-365 days | 3x |
| > 365 days | auto-removal |

## Returns reserve recommendation

| Category | Recommended reserve (% of landed cost) |
|----------|----------------------------------------|
| Apparel | 12-18% |
| Footwear | 12-18% |
| Beauty | 5-10% |
| Electronics | 5-8% |
| Home | 5-8% |
| Grocery (sealed) | 2-5% |
| Toys | 5-10% |

## Cross-border from China

Most cross-border sellers ship to Ozon FBO warehouse in Russia. Cost per kg from CN -> Ozon FBO:

| Route | Mode | Cost per kg | Transit time |
|-------|------|-------------|--------------|
| Guangzhou -> Moscow | Rail | $1.5-3 | 18-25 days |
| Yiwu -> Moscow | Rail | $1.8-3.5 | 20-28 days |
| Shenzhen -> SPB | Sea | $0.5-1.5 | 35-45 days |
| Guangzhou -> Vladivostok | Sea | $0.4-1.0 | 15-20 days |
| Any CN -> Russia | Air | $5-8 | 4-7 days |

Customs duty: 5-15% depending on HS code. EAC conformity certificate required for most categories.

## Russian VAT

- Standard VAT: 20% (Russia, Belarus)
- Reduced VAT: 10% (some food, children items, books)
- Kazakhstan VAT: 12%
- VAT is collected from buyer, remitted by Ozon (FBO) or seller (FBS / cross-border)
- Seller is responsible for VAT registration in each country

## Worked example (Ozon.ru, Apparel, Medium tier, 2000 RUB retail)

```
Retail price                          2000 RUB
- Ozon commission (15%)              -300 RUB
- FBO storage (30 days)                -12 RUB
- FBO last-mile (Medium, Moscow)      -120 RUB
- COD handling                         -30 RUB
- Returns reserve (15% of landed)     -90 RUB
- Promos / Ozon card discount        -100 RUB
- Currency buffer (5% RUB volatility) -100 RUB
= Net revenue                        1248 RUB
- Landed cost                        -600 RUB
- Advertising (ACOS 20%)             -400 RUB
= Contribution margin                 248 RUB
= Contribution margin %              12.4%
```

This shows the SKU is modestly profitable. With higher ACoS or ruble depreciation, it could turn unprofitable.

## Use cases in skills

- **ozon-fbo-fbs-calculator**: full cost calculation
- **ozon-profit-analyzer**: per-SKU waterfall
- **ozon-niche-finder**: reject niches where typical landed cost > 30% of retail
