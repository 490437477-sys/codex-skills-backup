# Mercado Libre Tax Regime — LATAM Overview

Reference for VAT, sales tax, and invoicing requirements when selling through Mercado Libre across Latin America. Numbers approximate; always validate against current SAT / SUNAT / AFIP / SII / DIAN regulations.

## 1. Country VAT Snapshot

| Country | VAT rate | Reduced rate | Sales term | Tax authority |
|---|---|---|---|---|
| Mexico | IVA 16% | 0% (essentials), 8% (border zone) | IVA | SAT |
| Brazil | ICMS 17–20% (state), ISS municipal, PIS/COFINS federal | varies by state | ICMS / ISS | SEFAZ + federal |
| Argentina | IVA 21% | 10.5%, 27% | IVA | AFIP / ARCA |
| Chile | IVA 19% | — | IVA | SII |
| Colombia | IVA 19% | 5%, 0% | IVA | DIAN |
| Uruguay | IVA 22% | 10%, 0% | IVA | DGI |
| Peru | IGV 18% | — | IGV | SUNAT |

## 2. Mexico — IVA and CFDI 4.0

- Standard IVA 16%; border zone (Tijuana, Juárez, etc.) IVA 8% with valid address
- RFC required for invoicing above threshold; foreign residents need a tax domicile in MX or use a marketplace withholding
- Every invoice is CFDI 4.0 with cartaporte complement when goods move by road
- Marketplace withholding: Mercado acts as withholding agent for IVA on certain cross-border flows
- Mexican tax residency or permanent establishment (PE) rules apply if inventory is stocked in MX

## 3. Brazil — ICMS, ISS, and the CBS/IBS Reform

- ICMS is state-level (17–20%) plus Difal for interstate sales to consumer
- ISS is municipal service tax (2–5%)
- PIS and COFINS are federal cumulative taxes on revenue
- Tax reform underway: CBS (federal) and IBS (state + municipal) replace ICMS / ISS / PIS / COFINS progressively through 2033 — verify current transition phase
- Every shipment requires an NF-e; modelo 55 for products; CF-e for in-store
- MERCOSUR common external tariff applies for cross-border from Argentina/Uruguay
- Origin state tax registration (IE) needed for most interstate operations

## 4. Argentina — IVA 21% and Withholding Regimes

- Standard IVA 21%; reduced 10.5% (food, medicine); higher 27% on luxury and certain services
- Percepción de IVA and IIBB advance payments common on marketplace sales
- AFIP / ARCA mandates Régimen de Información Compras y Ventas
- Foreign sellers without CUIT face withholding; some categories blocked entirely
- Local entity or trusted 3PL with CUIT recommended for scaling beyond low volumes
- ARS settlement is subject to currency controls; access to USD requires specific regimes (e.g., CCL)

## 5. Chile — IVA 19% Flat

- Single national rate 19%
- RUT required for invoicing; importers must obtain a RUT for the marketplace entity
- Cross-border regime since 2020 lets platforms withhold VAT on small imports
- DTE (Documento Tributario Electrónico) — boleta de honorarios or factura electrónica — required for every sale

## 6. Colombia — IVA 19% + Impuesto al Consumo

- Standard 19%; 5% on certain goods; 0% essentials
- Impuesto Nacional al Consumo applies to certain services and luxury goods
- RUT required for invoicing; FE electrónica is mandatory for large sellers
- Marketplace withholding framework is evolving; verify current threshold before scaling

## 7. Peru — IGV 18%

- IGV 18% includes IPM (municipal promotion tax) 2% within the 18%
- RUC required for invoicing; boleta de venta or factura electrónica
- SUNAT cross-border rules tighten at low thresholds (~$200 USD per shipment for many categories)

## 8. Mercado Envíos Tax Treatment

- Domestic Mercado Envíos: tax handled at checkout; invoice issued to end consumer with IVA / IVA-equivalent broken out
- Mercado Envíos Flex / Full: seller is importer of record if shipping cross-border; tax paid at customs with NF-e / CFDI / DTE supporting the entry
- Marketplace withholding (where in force): Mercado acts as withholding agent and remits the IVA on the seller side; seller receives net of tax
- Tax displayed on Mercado listing pages must reconcile with the electronic invoice; mismatches trigger rep validation

## 9. Cross-Border Invoicing Cheat Sheet

| Origin → Destination | Document | Authority |
|---|---|---|
| China → MLM | CFDI 4.0 issued by importer in MX | SAT |
| China → MLB | NF-e + DI + DU-E | SEFAZ + federal |
| China → MLC | DTE factura electrónica | SII |
| China → MCO | FE electrónica | DIAN |
| China → MPE | Factura electrónica + DAM | SUNAT |
| MLB → MLM | NF-e Brazil + CFDI complement in MX | both authorities |
| MLC → MLA | DTE Chile + despacho argentino | SII + ARCA |

## 10. Common Pitfalls

- Failing to issue CFDI on Mexican orders — immediate SAT warning + claims exposure
- Wrong NF-e model number for product type (model 55 vs 65)
- Mixing up CFDI 3.3 with CFDI 4.0; both have different complement rules
- Missing cartaporte when goods move cross-state in Mexico
- Assuming CBS/IBS replaces ICMS instantly — transition rules still levy ICMS until phase completes
- Ignoring PE risk in Mexico/Argentina/Colombia/Brazil when stocking inventory in-country
- Tax rates change annually in some countries; check AFIP, SAT, SII, SUNAT, DIAN bulletins each January

## 11. Returns and Refunds — Tax Treatment

- Mexico — refund can require CFDI 4.0 cancellation or refund invoice; SAT tracks refund trails
- Brazil — NF-e cancelamento or NF-e de devolução depending on flow
- Argentina — NC (Nota de Crédito) issued against original factura
- Chile — NC electrónica against the DTE
- Colombia — NC electrónica against the FE
- Peru — NC electrónica against the original factura

Mismatch between refund and original invoice is the second most common cause of tax audit after missing invoices.

## 12. Operational Checklist

- Validate RFC / CNPJ / CUIT / RUT / RUC / NIT format before first listing
- Enable electronic invoicing certificate in the country of operation
- Reconcile daily sales against invoices issued; gaps signal tax exposure
- Use a fiscal integration tool (e.g., Bind, Conta Azul, Defontana, Siigo) for scale
- File monthly VAT returns on the calendar set by each tax authority; late filing fines are steep
