# TEMU Keyword Data Sources (Free + Paid)

## Free Sources

### 1. Amazon Autocomplete (Best Free English Source)
- **How**: Type seed + space + letter a-z at amazon.com/search
- **Why**: Amazon buyer language overlaps 70%+ with TEMU buyers in English markets
- **Coverage**: 12 marketplaces
- **Limitation**: Not TEMU-specific

### 2. TEMU Site Search Suggestion
- **How**: Type in TEMU search bar, observe dropdown
- **How to scrape**: Open https://www.temu.com/search.html?search_key=<keyword> in browser, extract suggestions
- **Limitation**: TEMU doesn''t expose autocomplete via public API; requires browser observation or web search

### 3. Google Trends
- **URL**: https://trends.google.com/trends/explore?q=<keyword>
- **Use**: Detect seasonality, rising vs declining, related queries
- **Limit**: US/global only, not TEMU-specific

### 4. Google "People also ask" + Related Searches
- **How**: Search "<keyword>" on Google, scroll to bottom
- **Use**: Discover question-based long-tails
- **Limit**: Buyer intent may be informational, not purchase

### 5. TEMU Search Page Counts
- **How**: `site:temu.com "<keyword>"` on Google
- **Use**: Approximate competition density
- **Limit**: Only indexed pages, not full catalog

### 6. 1688 (Chinese Wholesale) Category Browsing
- **Use**: Discover trending Chinese products that may move to TEMU
- **Limit**: Chinese language, mostly bulk

### 7. Reddit r/FulfillmentByAmazon, r/ecommerce, r/dropship
- **Use**: Real seller experiences with TEMU categories
- **Limit**: Anecdotal, dated

## Paid Sources (Optional, for serious sellers)

- **Helium 10** (Amazon-focused, partial TEMU coverage)
- **Temu Seller Center Keyword Tool** (official, free for sellers)
- **Noxinfluencer / Modash** (creator + niche research)
- **Google Keyword Planner** (volume estimates)

## Cross-Validation Strategy

To improve confidence, use this 3-source rule:

```
For any keyword candidate:
  1. Amazon autocomplete returns it     → high confidence (real buyer query)
  2. TEMU site has < 500 products       → high opportunity
  3. Google Trends shows growth         → rising demand

If 2 of 3 are positive → pursue
If only 1 of 3 → observe
If 0 of 3 → skip
```

## Per-Marketplace Tips

| Marketplace | Language | Special Notes |
|---|---|---|
| US/UK/CA/AU | English | Amazon autocomplete is best proxy |
| DE/AT | German | Use amazon.de + Idealo + Google.de |
| FR | French | Use amazon.fr + Cdiscount suggestions |
| IT/ES | Italian/Spanish | Use local Amazon |
| JP | Japanese | Use amazon.co.jp + Yahoo Shopping Japan |
| KR | Korean | Use Naver Shopping + Coupang |
| MX | Spanish | Use amazon.com.mx + Mercado Libre |
| BR | Portuguese | Use amazon.com.br + Mercado Livre |
