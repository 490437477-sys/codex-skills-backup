# noon FBN Fee Schedule & Profit Reference

Use this sheet when running Step 4 of the noon-product-research workflow. Verify the current rates in noon Seller Central before committing P&L numbers — these are defaults and approximations as of 2024-2025.

## 1. Commission by Category (approximate)

| Category | KSA (noon.sa) | UAE (noon.ae) | Egypt (noon.com) |
|----------|---------------|---------------|-----------------|
| Mobiles & Tablets | 5-8% | 5-8% | 5-8% |
| Consumer Electronics | 8-12% | 8-12% | 8-12% |
| Fashion (Apparel) | 12-18% | 12-18% | 12-18% |
| Footwear | 12-18% | 12-18% | 12-18% |
| Beauty & Personal Care | 12-20% | 12-20% | 12-20% |
| Home & Kitchen | 10-15% | 10-15% | 10-15% |
| Toys & Baby | 10-15% | 10-15% | 10-15% |
| Sports & Outdoors | 10-15% | 10-15% | 10-15% |
| Books | 12-15% | 12-15% | 12-15% |
| Grocery (FBN-eligible) | 8-15% | 8-15% | 8-15% |
| Automotive | 10-12% | 10-12% | 10-12% |
| Health (SFDA regulated) | 12-15% | 12-15% | 12-15% |

Confirm category-specific rate inside noon Seller Central — some subcategories differ.

## 2. FBN Size Tiers (approximate)

| Tier | Max Weight | Max Dimensions |
|------|------------|----------------|
| Small envelope | 250 g | 30 × 20 × 3 cm |
| Small parcel | 1 kg | 30 × 22 × 12 cm |
| Standard parcel | 5 kg | 45 × 35 × 20 cm |
| Large parcel | 15 kg | 60 × 45 × 50 cm |
| Oversize | 30+ kg | > 60 cm on any side |

## 3. FBN Fulfillment Fee (approximate SAR / AED)

| Tier | KSA (SAR) | UAE (AED) |
|------|-----------|-----------|
| Small envelope | 4-6 | 4-6 |
| Small parcel | 7-10 | 7-10 |
| Standard parcel | 10-15 | 10-15 |
| Large parcel | 18-28 | 18-28 |
| Oversize | 30+ | 30+ |

Verify per-marketplace rate card — fees adjust with weight, not just dimensions.

## 4. FBN Storage Fee

- Off-peak (Jan-Sep): ~SAR/AED 0.50-1.00 per cubic foot per month
- Peak (Oct-Dec): ~SAR/AED 1.50-3.00 per cubic foot per month
- Long-term storage (>180 days): ~SAR/AED 5+ per cubic foot per month

Keep inventory turns high; Q4 deadstock is the most common profit leak.

## 5. VAT (carrying cost only — noon collects from buyer)

| Country | VAT Rate | Notes |
|---------|----------|-------|
| KSA | 15% | Collected at order; remit monthly or quarterly |
| UAE | 5% | Collected at order; remit quarterly |
| Egypt | 14% | Collected at order; remit per local tax rules |

Model VAT as a cash-flow line, not a margin line. Late filing penalties are steep in KSA.

## 6. Returns Reserve (gross margin haircut)

| Category | Expected return rate |
|----------|---------------------|
| Apparel / Footwear | 8-15% |
| Beauty | 3-6% |
| Consumer Electronics | 2-5% |
| Home & Kitchen | 3-6% |
| Toys | 3-6% |

Reserve the median number against every order's gross margin.

## 7. COD Friction

If COD is enabled (default in many categories):

- Higher return-to-origin rate (5-10% of COD orders)
- Slower cash collection (T+7 to T+21 settlement in KSA/UAE)
- Reconcile against bank statements monthly

Switch to prepaid-only if the category permits and the conversion uplift is clear.

## 8. Quick Profit Formula

```
Net = Price
    − Price × Commission%
    − FBN_Fulfillment
    − FBN_Storage (prorated to expected sell-through)
    − Product_Cost
    − Inbound_Shipping_to_FBN_Warehouse
    − Price × Returns_Rate%
    − Marketing_per_Order
    − FX_Hedge_Cost (if selling SAR/AED revenue from a CNY/USD cost base)
```

Healthy net margin targets:

- Apparel: 18-30%
- Beauty: 20-35%
- Electronics: 8-18% (volume compensates)
- Home: 20-30%
- Toys: 20-30%

If the math lands below 8% net, the product is unlikely to clear noon’s ad cost and returns drag — pick another SKU.

## 9. Inbound Logistics Hint

- China → KSA by sea: 25-35 days to Dammam / Jeddah port
- China → UAE by sea: 20-28 days to Jebel Ali
- Airfreight: 5-9 days, use only for samples or Ramadan rush replenishment
- Customs duty in KSA: 5-15% depending on HS code (verify per SKU)

Plan FBN inbound 60-90 days before the peak sales window.
