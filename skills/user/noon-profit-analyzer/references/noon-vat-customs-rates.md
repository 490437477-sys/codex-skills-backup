# noon VAT & Customs Duty Reference

Used by: noon-profit-analyzer, noon-product-research, noon-shipping-calculator.

Quick reference for VAT rates and customs duty bands across noon marketplaces. Important: VAT is collected from the buyer and remitted to the tax authority; it does NOT reduce seller margin but must be tracked separately.

## VAT rates

| Country | Rate | Effective | Notes |
|---------|------|-----------|-------|
| Saudi Arabia | 15% | Jul 2020 | Standard rate; some essentials 0% |
| UAE | 5% | Jan 2018 | Standard rate; some healthcare/education 0% |
| Egypt | 14% | Jul 2026 (planned) | Currently 14% with food at lower rate |
| Kuwait | 0% (no VAT yet) | - | No VAT currently |
| Bahrain | 10% | Jan 2022 | Standard rate |
| Oman | 5% | Apr 2021 | Standard rate |

### VAT handling on noon

- noon adds VAT to the displayed buyer price
- Seller sets the VAT-inclusive price
- noon remits VAT to the tax authority on the seller's behalf (for FBN) or the seller remits directly (for FBM / cross-border)
- Seller is responsible for VAT registration in each country they sell in

## Customs duty bands (Saudi Arabia)

| HS code range | Goods | Duty rate |
|---------------|-------|-----------|
| 61-62 | Apparel, knitted / woven textiles | 5% |
| 64 | Footwear | 5% |
| 71 | Jewelry, precious metals | 0-5% |
| 84 | Machinery, computers | 5% |
| 85 | Electronics, phones | 5% (with IECEE certificate) |
| 90 | Optical, medical | 5% |
| 94 | Furniture, bedding | 5-15% |
| 95 | Toys | 5% |
| 33 | Cosmetics, perfumes | 5% (with SFDA notification) |
| 39 | Plastics | 5% |
| 73 | Iron/steel articles | 5-15% |
| 87 | Vehicles, parts | 5-15% |

Plus 15% VAT on the (CIF + duty) value.

## Customs duty bands (UAE)

UAE follows the GCC common external tariff. Standard duty 5% for most goods, with some exemptions.

| HS code range | Goods | Duty rate |
|---------------|-------|-----------|
| Most categories | Standard | 5% |
| 09 | Coffee, spices | 0% |
| Some food staples | Food | 0-5% |
| Tobacco, alcohol | Restricted | 100% (effectively banned) |

Plus 5% VAT on (CIF + duty).

## Customs duty bands (Egypt)

Egypt applies a more complex tariff schedule.

| HS code range | Goods | Duty rate |
|---------------|-------|-----------|
| 61-62 | Apparel | 20-40% (varies by garment) |
| 64 | Footwear | 20-40% |
| 85 | Electronics | 5-25% |
| 84 | Computers | 5-10% |
| 95 | Toys | 20-40% |
| 33 | Cosmetics | 20-40% |
| 71 | Jewelry | 5-10% |
| Most other manufactured goods | 5-40% |

Plus 14% VAT on (CIF + duty).

Egypt has additional fees:
- Development fee: 1-3%
- Port fees: 1-2% of CIF
- GOEIC inspection fee for restricted categories

## Landed cost formula

```
Landed cost = FOB price
            + ocean freight (or air freight)
            + insurance (typically 0.5% of FOB)
            + CIF = FOB + freight + insurance
            + customs duty (Duty% x CIF)
            + VAT (VAT% x (CIF + Duty))
            + port / handling fees
            + local inland transport to FBN warehouse
```

## Worked example (KSA, $20 FOB China consumer goods, sea freight)

```
FOB price (CN factory)              $20.00
Ocean freight (LCL, 1 unit share)    $3.00
Insurance (0.5% FOB)                 $0.10
CIF                                  $23.10
Customs duty (5% of CIF)             $1.16
Subtotal                            $24.26
VAT 15% (on CIF + duty)              $3.64
Subtotal                            $27.90
Local transport to FBN               $1.50
Other port fees                      $0.50
LANDED COST (USD)                   $29.90
```

Convert to SAR: $29.90 x 3.75 = ~112 SAR.

If retail on noon.sa is 199 SAR, gross margin before noon fees = 199 - 112 = 87 SAR (~44%).

## Tariff optimization tips

1. **Re-classify where possible**: HS code choice can move 5% to 40%. Consult a customs broker for high-value categories.
2. **Use Free Trade Zones**: Jebel Ali (UAE), KAEC (KSA), Suez (Egypt) allow duty-free storage. Re-export from FTZ avoids duty.
3. **Consolidate shipments**: LCL is cheaper per unit than small parcels, but slower (20-35 days).
4. **Pre-clear with Saudi customs (FASAH)**: cuts port dwell time from days to hours.

## Use cases in skills

- **noon-profit-analyzer**: include duty + VAT in waterfall (VAT as separate tracking line)
- **noon-product-research**: total landed cost comparison
- **noon-shipping-calculator**: inbound cost module
- **noon-niche-finder**: penalize niches where duty > 30% (margin collapse)
