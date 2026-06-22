# noon Arabic Dialect Variants Reference

Used by: noon-backend-keywords, noon-keyword-research, noon-negative-keywords, noon-listing-optimization, noon-review-analyzer.

MENA shoppers search in multiple Arabic variants. noon.sa (Saudi Arabia) skews toward KSA dialect and MSA; noon.ae (UAE) is more Levantine-influenced with English mixing; noon.com (Egypt) is Egyptian Arabic. A complete noon keyword strategy must cover all four.

## Dialect overview

| Variant | Region | Search character | Example for "mobile phone" |
|---------|--------|------------------|----------------------------|
| MSA (فصحى) | Pan-Arab | Most common in titles, official listings | هاتف محمول, جوال |
| KSA | Saudi Arabia | Largest volume, family-friendly | جوال, موبايل, تليفون |
| UAE | UAE | English-mixing common | موبايل, تلفون, موبايل ايفون |
| Egypt | Egypt | Distinctly Egyptian | موبايل, تليفون محمول |

## Common product category variants

### Electronics

| English | MSA | KSA | UAE | Egypt |
|---------|-----|-----|-----|-------|
| Mobile phone | هاتف محمول | جوال, موبايل | موبايل | موبايل, تليفون |
| Laptop | لابتوب | لابتوب | لابتوب | لاب توب |
| Headphones | سماعات | سماعات, إيربودز | سماعات | سماعات |
| Charger | شاحن | شاحن | شاحن, كيبل | شاحن |
| Power bank | باور بانك | باور بانك, بطارية متنقلة | باور بانك | باور بانك |
| Smart watch | ساعة ذكية | ساعة ذكية, سمارت واتش | ساعة ذكية | ساعة ذكية |

### Home & kitchen

| English | MSA | KSA | UAE | Egypt |
|---------|-----|-----|-----|-------|
| Air fryer | قلاية هوائية | قلاية هوائية, إير فراير | قلاية هوائية | قلاية هوائية |
| Blender | خلاط | خلاط | خلاط | خلاط كهربائي |
| Pressure cooker | قدر ضغط | قدر ضغط, حلة ضغط | قدر ضغط | حلة ضغط |
| Coffee maker | ماكينة قهوة | مكينة قهوة, صانعة القهوة | ماكينة قهوة | ماكينة قهوة |
| Vacuum cleaner | مكنسة كهربائية | مكنسة | مكنسة | مكنسة كهربائية |

### Fashion

| English | MSA | KSA | UAE | Egypt |
|---------|-----|-----|-----|-------|
| Abaya | عباية | عباية | عباية | عباية |
| Hijab | حجاب | حجاب | حجاب | حجاب |
| Jalabiya | جلابية | جلابية, ثوب | جلابية, قندورة | جلابية |
| Kaftan | قفطان | قفطان | قفطان | قفطان |
| Modest dress | فستان محتشم | فستان طويل, فستان محتشم | فستان محتشم | فستان محتشم |

### Beauty & personal care

| English | MSA | KSA | UAE | Egypt |
|---------|-----|-----|-----|-------|
| Perfume | عطر | عطر | عطر | عطر, برفان |
| Oud | عود | عود | عود | عود |
| Lipstick | أحمر شفاه | أحمر شفاه, روج | أحمر شفاه | روج |
| Foundation | كريم أساس | فاونديشن | كريم أساس | كريم أساس |
| Hair dryer | مجفف شعر | سيشوار, مجفف الشعر | سيشوار, مجفف شعر | سيشوار |
| Shampoo | شامبو | شامبو | شامبو | شامبو |

### Baby & kids

| English | MSA | KSA | UAE | Egypt |
|---------|-----|-----|-----|-------|
| Diapers | حفاضات | حفاضات, بامبرز | حفاضات | حفاضات |
| Stroller | عربة أطفال | عربة أطفال, استroller | عربة أطفال | عربة أطفال |
| Baby formula | حليب أطفال | حليب أطفال, تركيبة | حليب أطفال | لبن أطفال |
| Pacifier | مصاصة | لهاية, مصاصة | مصاصة | لهاية |

## Transliteration patterns

Latin script transliteration is common in MENA search. Cover these patterns:

- Phone → فون (often combined, e.g. ايفون for iPhone)
- Power → باور (e.g. باور بانك)
- Air → إير (e.g. إيربودز)
- Smart → سمارت (e.g. سمارت واتش)
- Bluetooth → بلوتوث
- Wireless → وايرلس, لاسلكي

## Tips for noon backend keywords

1. **Include at least 1 MSA form** for pan-Arab search.
2. **Include at least 1 dialect form** for the target marketplace (KSA for noon.sa, UAE for noon.ae, EG for noon.com).
3. **Include English/Latin form** if commonly used (especially UAE).
4. **Avoid mixing Arabic and Latin in the same keyword** — noon treats them as separate tokens.
5. **Use the most-searched dialect first** for the target market (e.g. for noon.sa, prioritize جوال then موبايل then هاتف).
6. **Strip diacritics, normalize alef (إأآا → ا), taa marbuta (ة → ه)** before counting bytes.

## Verification

Before finalizing any keyword set:
- Check noon autocomplete for the seed term in AR and EN
- Cross-reference Google Trends for SA / AE / EG separately
- Mine buyer-language from existing reviews of competitor SKUs

## Use cases in skills

- **noon-backend-keywords**: build the keyword string from this table
- **noon-keyword-research**: estimate search volume by dialect variant
- **noon-negative-keywords**: detect dialect over-firing
- **noon-listing-optimization**: choose title language mix (Arabic primary for noon.sa)
- **noon-review-analyzer**: normalize dialect before NLP clustering
