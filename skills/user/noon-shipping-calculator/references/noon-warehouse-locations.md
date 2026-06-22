# noon FBN Warehouse Locations

Used by: noon-shipping-calculator, noon-profit-analyzer, noon-product-research.

noon operates FBN warehouses in three main hubs, each covering its domestic market. Sellers should plan inbound shipments to the warehouse closest to their demand concentration.

## Primary warehouses

### Saudi Arabia (noon.sa)

| City | Coverage | Notes |
|------|----------|-------|
| Riyadh | Central, Eastern, Northern | Largest warehouse; primary hub |
| Jeddah | Western, Southwestern | Port-adjacent; faster inbound from sea freight |
| Dammam | Eastern province | Secondary; useful for eastern Saudi demand |

Recommended: split inventory 60-70% Riyadh / 25-30% Jeddah / 5-10% Dammam for KSA-wide 2-day delivery coverage.

### UAE (noon.ae)

| City | Coverage | Notes |
|------|----------|-------|
| Dubai (Jebel Ali) | All UAE | Single primary hub; Jebel Ali Free Zone allows duty deferral |

UAE has one main warehouse. All UAE fulfillment flows through Dubai.

### Egypt (noon.com)

| City | Coverage | Notes |
|------|----------|-------|
| Cairo | Greater Cairo, Delta | Primary hub |
| Alexandria | North coast | Secondary; port-adjacent for inbound |

Egypt has two warehouses but Cairo handles most volume.

## Inbound shipping routes

### From China (Guangzhou / Yiwu / Shenzhen)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Guangzhou → Jeddah | Sea (LCL) | 18-25 days | $80-150 |
| Yiwu → Dammam | Sea (LCL) | 22-28 days | $90-160 |
| Shenzhen → Jebel Ali | Sea (LCL) | 14-20 days | $60-120 |
| Guangzhou → Cairo | Sea (LCL) | 25-35 days | $120-200 |
| Any China → Anywhere | Air (urgent) | 4-7 days | $4-8/kg |

### From India (Mumbai / Chennai)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Mumbai → Jebel Ali | Sea (LCL) | 5-8 days | $50-90 |
| Chennai → Jeddah | Sea (LCL) | 8-12 days | $70-120 |
| Mumbai → Cairo | Sea (LCL) | 12-18 days | $80-140 |

### From Turkey (Istanbul)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Istanbul → Jebel Ali | Sea (LCL) | 7-10 days | $70-110 |
| Istanbul → Jeddah | Sea (LCL) | 8-12 days | $80-130 |
| Istanbul → Cairo | Sea (LCL) | 5-8 days | $60-100 |

### From Europe (Germany / Italy)

| Route | Mode | Transit time | Cost (per CBM) |
|-------|------|--------------|----------------|
| Hamburg → Jeddah | Sea (LCL) | 18-22 days | $100-160 |
| Genoa → Jebel Ali | Sea (LCL) | 12-16 days | $90-140 |

## Inbound consolidation strategies

1. **LCL (Less than Container Load)**: best for < 15 CBM. Slow but cheap.
2. **FCL (Full Container Load)**: best for > 20 CBM. 20ft container ~28 CBM, 40ft ~58 CBM.
3. **Cross-dock**: ship to a regional hub (Jebel Ali) and truck to KSA warehouse (5-7 days) to avoid double-port handling.
4. **Air-freight for replenishment**: use air for top 20% of SKUs (high velocity), sea for the rest.
5. **Bonded warehouse (Jebel Ali FTZ)**: store inventory without paying UAE duty; re-export to KSA triggers duty there. Good for serving both markets from one stock pool.

## Customs clearance

| Country | Platform | Lead time | Notes |
|---------|----------|-----------|-------|
| KSA | FASAH | 1-3 days | Pre-clear online; SABER CoC required |
| UAE | Dubai Customs / MIRSAL | 1-2 days | Fast clearance at Jebel Ali |
| Egypt | Nafeza / ACI | 3-7 days | Egypt has GOEIC pre-shipment inspection; longer |

For Egypt, plan an extra 1-2 weeks for GOEIC inspection on first shipment of any new SKU category.

## Cross-border arbitrage opportunity

Many sellers use the UAE warehouse as a regional hub:
- Stock lands in Jebel Ali (fast clearance, FTZ benefits)
- Serve UAE demand directly
- Re-export to KSA via overland (5-7 days, lower cost than separate sea freight)
- Re-export to Egypt via sea (10-15 days)

Cost savings vs separate warehouses per market: typically 20-35% on inbound freight and customs combined.

## Recommended stock split for cross-market sellers

For sellers serving all three noon marketplaces:

| Warehouse | Initial stock split | Reason |
|-----------|---------------------|--------|
| Jebel Ali (UAE) | 40-50% | FTZ benefits, serves UAE, feeds KSA + EG via re-export |
| Riyadh (KSA) | 35-45% | Largest single market (noon.sa = 65-75% of cross-market GMV) |
| Cairo (Egypt) | 5-15% | Egypt is smallest, but customs friction favors local stock |

## Inbound checklist

Before shipping:
- [ ] SASO CoC / SFDA notification / ECAS certificate secured per destination
- [ ] Customs broker appointed in destination country
- [ ] HS codes assigned per SKU
- [ ] Commercial invoice and packing list match physical goods
- [ ] FBN inbound appointment booked via Seller Central
- [ ] Pallet labels printed (noon format) and affixed
- [ ] Mixed-SKU carton plan finalized (noon allows mixed cartons in FBN inbound)

## Use cases in skills

- **noon-shipping-calculator**: compute inbound cost by origin + destination + mode
- **noon-profit-analyzer**: include inbound freight + duty in landed cost
- **noon-product-research**: recommend warehouse strategy based on demand concentration
