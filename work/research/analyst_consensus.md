# Analyst Consensus on Inaxaplin (sponsor reports, Feb–Jun 2026)

Written Sept 27, 2026 from the seven extraction files in this folder. Every figure carries the report's PDF page. **Every figure below predates the Sept 22, 2026 AMPLIFIED results.** Newer figures from the public refresh and from any reports the team pulls will be added, with dates, and the model will use the newest figure for each variable.

Terms: PoS is the probability of success (the chance the drug reaches approval). Risk-adjusted sales are forecast sales multiplied by the PoS. "Unadjusted (calculated)" divides a printed risk-adjusted figure by its printed PoS.

## 1. Launch year and approval path

| Report (date) | Launch or first revenue | Approval path | Page |
|---|---|---|---|
| Oppenheimer (Feb 13) | Launch 2027; $14.4M in 2027, $51.4M in 2028, probability-adjusted | Accelerated approval on the 48-week interim | p.19, p.21, p.12 |
| Jefferies (Mar 10) | First revenue 2027 ($141M) | AMPLITUDE is "the registrational trial for accelerated approval"; interim reads UPCR and eGFR slope at 48 weeks | PDF p.85, p.74, p.72 |
| William Blair (Mar 26) | Not stated | FDA "requiring eGFR for AMKD currently" | p.2 |
| Morgan Stanley (Apr 19) | Not stated | "Per VRTX, eGFR (not UPCR) data is FDA's focus" of the interim | p.12 |
| Truist (May 26) | "Accelerated approval/ launch in primary AMKD by early 2028"; first revenue 2028 ($40.2M) | Accelerated approval | p.2, p.5 |
| RBC (Jun 4) | First revenue 2027 ($22.7M, US); accelerated filing in 2027 | Interim tests proteinuria and eGFR slope; KOLs say eGFR separation may need at least 2 years; full approval on 2-year eGFR data, available early to mid 2028 | p.7, p.8, p.5, p.6 |

**Model proposal.** Base: accelerated approval with US launch in 2028 (Truist, the latest report to state a launch date, matches an early-2027 readout, a mid-2027 filing, and a priority review). Range: late 2027 (Oppenheimer, RBC) to 2029 on the full-approval path (RBC). The full-approval path is modeled as its own branch, not as a sensitivity.

## 2. Price and gross-to-net

| Report | Figure | Page |
|---|---|---|
| Morgan Stanley | $135K net price per year; geography not labeled | p.5 |
| Morgan Stanley | Analog: Filspari list price (WAC) about $150K; gross-to-net "mid-20%" | p.5 |
| Jefferies | Sibeprenlimab (Otsuka, IgA nephropathy) launched at $390K per year; list or net not stated | PDF p.3, p.13, p.50 |
| All others | No inaxaplin price | — |

Calculated: Filspari's net price at a 25% discount is $150,000 × 0.75 = $112,500. Morgan Stanley's $135,000 is $22,500 above that analog net price.
**Model proposal.** Base net price $135K per year (Morgan Stanley, the only inaxaplin figure), with a range of $110K–$160K until WS-F returns payer-channel discounts. Povetacicept's net price for the retargeting cost is an assumption anchored on the sibeprenlimab price, with list-versus-net left open.

## 3. Patients on therapy

| Report | Figure | Page |
|---|---|---|
| Morgan Stanley | About 38,000 on therapy in 2035, 25% of 150,000 **US-plus-Europe** primary AMKD patients | p.5 |
| All others | None | — |

The 38,000 is a US-plus-Europe count and cannot be used as a US count.

## 4. Sales

| Report (date) | 2035 risk-adjusted | 2035 unadjusted | Peak | PoS | Page |
|---|---|---|---|---|---|
| Oppenheimer (Feb 13) | Not given for inaxaplin alone | Not given | $6,163M, basis and geography not labeled | 60% | p.19 |
| Jefferies (Mar 10) | $2,729M (chart; geography and unit not printed) | Not given | About $3B risk-adjusted ($3,057M in 2037–38) | 60% | PDF p.85, p.14 |
| Morgan Stanley (Apr 19) | $2.6B (US-plus-Europe patient base) | $5.2B (calculated) | Not given | 50% | p.1, p.5 |
| Truist (May 26) | $1,421.7M (no US split) | $2,031M (calculated) | Not given; primary AMKD market "~$5B+" | 70% (up from 50%) | p.1, p.5, p.2 |
| RBC (Jun 4) | $1,355.8M worldwide; $1,070.5M US | Not given | "~$3.3B WW out-year opportunity," basis not labeled | Not printed | p.7, p.5 |
| Consensus (Visible Alpha, as shown by Jefferies, Mar 2026) | $1,637M | — | $2.2B | — | Jefferies PDF p.85 |

**Correction to the prompt's scenario bounds.** The prompt lists RBC as "about $3.3B worldwide out-year." RBC's printed 2035 risk-adjusted forecast is $1,355.8M worldwide ($1,070.5M US; RBC p.7). The $3.3B is an unlabeled "opportunity" (RBC p.5) and is not a comparable 2035 figure. The 2035 risk-adjusted range across the reports is $1.36B (RBC) to $2.73B (Jefferies); Morgan Stanley's $2.6B rests on a US-plus-Europe patient base.

RBC's US series is the only one split by geography: $22.7M (2027), $109.2M (2028), $240.2M (2029), $369.9M (2030), $514.6M (2031), $667.0M (2032), $827.4M (2033), $950.7M (2034), $1,070.5M (2035), all risk-adjusted (RBC p.7). US sales are 79.0% of RBC's 2035 worldwide figure (calculated).

## 5. Probability of success

| Report | PoS | Page |
|---|---|---|
| Morgan Stanley | 50% | p.1, p.5 |
| Jefferies | 60% | PDF p.4, p.14 |
| Oppenheimer | 60% | p.19 |
| Truist | 70% (prior 50%) | p.1 |
| RBC | Not printed. Its fair-value sensitivities imply about 40% if value scales with PoS (calculated; an inference) | p.5, p.6 |
| Guggenheim (note dated Aug 3, 2026; reported by Fierce Biotech on Sept 22) | 65% primary AMKD; 45% AMKD with type 2 diabetes | `analyst_public_refresh.md`, section 6. The prompt credited the 45% to BMO; BMO's public note gives no figure. |

**Model proposal.** Base 65% for the primary-AMKD label: Guggenheim's Aug 3 figure is the newest public value, and the prompt tells the model to use the newest figure. Range 50–70% (Morgan Stanley to Truist). The diabetic population keeps its own probability of 45% (Guggenheim), which predates the weak Sept 22 diabetes result and is therefore an upper value for that upside.

## 6. Discount rates (all whole-company DCF rates; no report gives an inaxaplin-specific rate)

| Report | Rate | Terminal growth | Page |
|---|---|---|---|
| Jefferies | 7.5% WACC | 1.0% | PDF p.7 |
| Oppenheimer | 8% WACC | −1% | p.2, p.20 |
| Truist | 8% ("our standard for lower-risk cash-flow positive, large-cap biopharmaceutical companies") | 2% | p.1, p.9 |
| Stifel | 8.5% | 1% | p.2 |
| RBC | 9.0% | 2.5% | p.9, p.14 |
| Morgan Stanley | 10% WACC | 2% after 2040 | p.14 |

The prompt's 8–10% range leaves out Jefferies' 7.5%. The full range is 7.5–10%. The mba_finance subagent justifies the project rate in Phase 3.

## 7. Population definitions

| Source (as reported) | Definition and count | Geography | Page |
|---|---|---|---|
| Vertex, via Morgan Stanley | 150,000 primary AMKD plus 100,000 AMKD with moderate proteinuria or diabetes = 250,000 | US plus Europe | MS p.1, p.5 |
| Truist | About 150,000 primary AMKD plus about 150,000 comorbid | US plus Europe | p.2 |
| RBC | 150,000 AMPLITUDE population plus "+100K" diabetic, "as per company" | Not labeled | p.5 |
| Jefferies build | 212,500 US AMKD (85% of 250,000); 127,500 US primary AMKD (60%); 85,000 US moderate proteinuria or diabetes; 30% diagnosed today, 60% at "market maturity" (assumptions) | US | PDF p.80 |
| Maze, via Morgan Stanley | At least 250,000 US AMKD patients, 40% with diabetes | US | MS p.5 |
| Bottom-up lifetime (Morgan Stanley; Jefferies) | About 1.2M (6M two-variant carriers × 20%) | US | MS p.5; Jefferies PDF p.80 |

**AMPLITUDE entry criteria** (the likely first label): two APOL1 variants; UPCR 0.7 to under 10 g/g; eGFR 25 to under 75 mL/min/1.73m²; no diabetes, no transplant, no other known kidney-disease cause; ages 10 to 65 (MS p.12; Jefferies PDF p.71, p.77). The trial eGFR floor is 25.

**Genotype yield** (Oppenheimer p.10, citing a global genotyping study): 44–50% of FSGS patients and 21–31% of non-diabetic kidney disease patients carry two APOL1 variants. WS-A must confirm the population these shares describe before the model uses them as test-positive rates.

**Disease course.** African American AMKD patients lose 6.55 mL/min/1.73m² of eGFR per year, against 3.63 for African Americans with CKD and no risk variants (MS p.4). AMKD patients reach dialysis at 34.1% by 5 years and 50.6% by 10 years, against 23.3% and 31.5% for matched CKD patients (Shah et al., ASN 2025, via Oppenheimer p.10).

## 8. Public figures after the sponsor reports (from `analyst_public_refresh.md`)

| Date (2026) | Source | Figure | Confidence |
|---|---|---|---|
| Aug 3 | Vertex CEO, Q2 call | FDA agreement for potential accelerated approval on the interim analysis's primary endpoint, "which is 1 year GFR" | High (call transcript) |
| Aug 3 | Vertex CCO, Q2 call | Renal field force fully hired; about 90% have nephrology experience; no headcount given | High (call transcript) |
| Aug 3 | Guggenheim | Probability of success 65% primary AMKD; 45% with type 2 diabetes | Medium (Fierce Biotech) |
| Sept 9 | Vertex investor relations, Wells Fargo conference | "Potentially September 2027, getting close to a second launch potentially. In renal" | Low (AI-assisted summary; confirm from the webcast replay) |
| Sept 22 | Vertex release | AMKD affects about 150,000 people in the US and Europe; interim analysis early 2027 | High |
| Sept 22 | Leerink | Inaxaplin sales $1.2B in 2035 | Medium (BioSpace) |
| Sept 22–24 | UBS | About 80% of AMKD patients have modest proteinuria (studies the analyst cites) | High for the quote; the underlying studies are unchecked |
| Sept 23 | Jefferies | Inaxaplin AMKD peak sales raised from about $3.1B to about $3.6B | Medium (AI-assisted summary) |

**Effect on the model.** The launch-timing base moves only if the September 2027 launch remark is confirmed; WS-F checks it. The UBS share would mean most AMKD patients fall outside the first label's proteinuria threshold, which WS-A must reconcile with Vertex's 150,000 figure. Vertex consensus revenue is $13.25B (2026), $14.55B (2027), and $16.44B (2028) (Yahoo Finance and MarketScreener, Sept 25–27, secondary).

## 9. Diagnosis and payer comments (the only primary-care-relevant content in the seven reports)

- "Majority of these patients are not diagnosed. VRTX offers free APOL1 genotyping." (Morgan Stanley p.5)
- A nephrologist interviewed by Jefferies: about 75% "ultimately receive correct dx (timing heterogeneous)"; about 15–25% "have unfavorable courses partly driven by delay/misdirection, some progressing to ESRD pre-dx"; community visits of about 15 minutes "make extra labs/screening a deterrent"; payers likely to require genotype, biopsy findings, and disease activity; therapy "likely lifelong." (Jefferies PDF p.79)
- No report discusses primary care physicians, sales forces, or referral volumes. WS-A, WS-C, and WS-D must build these inputs from outside sources.
