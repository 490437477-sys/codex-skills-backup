# Ozon Russian Keyword Variants Reference

Used by: ozon-backend-keywords, ozon-negative-keywords, ozon-keyword-research, ozon-listing-optimization.

Russian search behavior on Ozon uses multiple variants: standard Russian, colloquial, transliterated, abbreviations. A complete keyword strategy must cover all four.

## Variant overview

| Variant | Source | Example for "laptop" |
|---------|--------|----------------------|
| Standard Russian (norm) | Ozon autocomplete, official | 薪芯褍褌斜褍泻 |
| Colloquial | Spoken Russian | 泻芯屑锌, 谢邪锌褌芯锌 |
| Transliterated (Latin chars) | Yandex / Google users | noutbuk, laptop |
| Abbreviation | Tech slang | 薪斜, 锌泻 |

Russian buyers on Ozon mostly use standard Russian. Colloquial is common for fast-moving consumer goods. Transliteration is more common in Yandex / Google than Ozon search.

## Common product category variants

### Electronics

| English | Standard | Colloquial | Transliterated |
|---------|----------|------------|----------------|
| Mobile phone | 褋屑邪褉褌褎芯薪 | 褌械谢械褎芯薪 | telefon, smartfon |
| Laptop | 薪芯褍褌斜褍泻 | 泻芯屑锌, 谢邪锌褌芯锌 | noutbuk, laptop, comp |
| Headphones | 薪邪褍褕薪懈泻懈 | 褍褕懈 | naushniki, headphone |
| Charger | 蟹邪褉褟写薪芯械 褍褋褌褉芯泄褋褌胁芯 | 蟹邪褉褟写泻邪 | zaryadka |
| Power bank | 胁薪械褕薪懈泄 邪泻泻褍屑褍谢褟褌芯褉 | 锌芯胁械褉斜邪薪泻 | powerbank |
| Smart watch | 褋屑邪褉褌 褔邪褋褘 | 褍屑薪褘械 褔邪褋褘 | smartwatch |

### Home & kitchen

| English | Standard | Colloquial | Transliterated |
|---------|----------|------------|----------------|
| Air fryer | 邪褢褉芯谐褉懈谢褜 | 邪褢褉芯褎褉邪泄械褉 | airfryer, aerogril |
| Blender | 斜谢械薪写械褉 | 懈蟹屑械谢褜褔懈褌械谢褜 | blender |
| Pressure cooker | 褋泻芯褉芯胁邪褉泻邪 | 褋泻芯褉芯胁邪褉泻邪 | skovorodka (skillet) |
| Coffee maker | 泻芯褎械屑邪褕懈薪邪 | 泻芯褎械屑芯谢泻邪 | kofemashina, kofevarka |
| Vacuum cleaner | 锌褘谢械褋芯褋 | 锌褘谢械褋芯褋 | pylesos |
| Microwave | 屑懈泻褉芯胁芯谢薪芯胁泻邪 | 屑懈泻褉芯胁芯谢薪芯胁泻邪, 屑褝胁懈褔泻邪 | microwave, mikrovolnovka |

### Fashion

| English | Standard | Colloquial | Transliterated |
|---------|----------|------------|----------------|
| T-shirt | 褎褍褌斜芯谢泻邪 | 褎褍褌斜芯谢泻邪, 褌懈褕泻邪 | tishka, tshirt |
| Sneakers | 泻褉芯褋芯胁泻懈 | 泻械写褘 | krossovki, kedy |
| Jacket | 泻褍褉褌泻邪 | 泻褍褉褌泻邪 | kurtka |
| Dress | 锌谢邪褌褜械 | 锌谢邪褌褜械 | platye |
| Jeans | 写卸懈薪褋褘 | 写卸懈薪褋褘 | dzhinsy, jeans |
| Underwear | 薪懈卸薪械械 斜械谢褜械 | 褌褉褍褋褘, 斜械谢褜械 | trusy, underwear |

### Beauty & personal care

| English | Standard | Colloquial | Transliterated |
|---------|----------|------------|----------------|
| Perfume | 写褍褏懈 | 锌邪褉褎褞屑, 褌褍邪谢械褌 | parfum, tualet, duhi |
| Lipstick | 锌芯屑邪写邪 | 锌芯屑邪写邪 | pomada |
| Shampoo | 褕邪屑锌褍薪褜 | 褕邪屑锌褍薪褜 | shampoo |
| Cream | 泻褉械屑 | 泻褉械屑 | krem |
| Mask | 屑邪褋泻邪 | 屑邪褋泻邪 | maska |

### Baby & kids

| English | Standard | Colloquial | Transliterated |
|---------|----------|------------|----------------|
| Diapers | 锌芯写谐褍蟹薪懈泻懈 | 锌邪屑锌械褉褋褘 | pampers, podguzniki |
| Stroller | 泻芯谢褟褋泻邪 | 泻芯谢褟褋泻邪 | kolyaska |
| Baby formula | 写械褌褋泻芯械 锌懈褌邪薪懈械 | 褋屑械褋褌 | smes, pitanie |
| Pacifier | 锌褍褋褌褘褕泻邪 | 褋芯褋泻邪 | pustyshka, soska |

## Tips for Ozon backend keywords

1. **Standard Russian is primary**: most Ozon search uses standard Russian. Lead with that.
2. **Colloquial second**: especially for fast-moving consumer goods.
3. **Transliteration is minor on Ozon**: include only for top 10% of search volume cases.
4. **Avoid mixing scripts**: Ozon treats Cyrillic and Latin as separate tokens.
5. **Lowercase all Russian**: avoid capital letters except proper nouns.
6. **Yo normalization**: treat 械 and 械 as the same character.
7. **Use compound words**: Russian compounds (邪胁褌芯屑芯泄泻邪, 泻芯褎械屑邪褕懈薪邪) often have higher search volume than separate words.

## Verification

Before finalizing any keyword set:
- Check Ozon autocomplete for the seed term in RU
- Cross-reference Yandex Wordstat for the same term
- Mine buyer language from existing reviews of competitor SKUs

## Use cases in skills

- **ozon-backend-keywords**: build the keyword string from this table
- **ozon-negative-keywords**: detect colloquial over-firing
- **ozon-keyword-research**: estimate search volume by variant
- **ozon-listing-optimization**: choose title language mix (always Russian primary for Ozon.ru)
