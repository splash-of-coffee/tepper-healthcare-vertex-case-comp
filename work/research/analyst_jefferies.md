# Jefferies initiation on Vertex, March 10, 2026: extraction for the inaxaplin case

This file extracts one sell-side report for the team. Every item carries its PDF page, written "PDF p.N". Items marked "calculated" are this file's arithmetic, not the report's. The report is licensed for competition use only. This file does not reproduce the licensing line printed on each page. In this file, $M means millions of US dollars, $B means billions, and K means thousands.

## 1. Header

| Field | Value | Page |
|---|---|---|
| Firm | Jefferies (Jefferies LLC / Jefferies Research Services, LLC) | PDF p.1 |
| Report title | "IgAN Data Looks In Line - We're Still Bullish on Oppty - Initiate BUY, PT $580" | PDF p.1 |
| Slide-deck title | "VRTX: IgAN Data Looks In Line – We're Still Bullish on the Opportunity (BUY Rating, PT $580)" | PDF p.8 |
| Report type | Initiation of coverage | PDF p.1 |
| Report date as printed | March 10, 2026 (recommendation published 5:32 A.M.) | PDF p.1, p.109 |
| Analysts | Akash Tewari and Amy Li, PharmD (Equity Analysts); Manoj Eradath, MBBS, Ph.D.; Phoebe Tan; Katherine Wang; Anastasia Parafestas; Albert Zhang, CPA; Alexi Kalsi, MBBS MSc (Equity Associates) | PDF p.1 |
| Rating | Buy | PDF p.1 |
| Price target | $580 per share, 26% above the $460.87 close on 3/9/2026 | PDF p.1, p.9 |
| Scenario values | Upside $700 (+52%); downside $380 (−18%) | PDF p.2 |
| Sponsor's tag in the file name | "overview" | File name |

This report predates the Sept 22, 2026 AMPLIFIED results, the Crinetics acquisition (July–Sept 2026), and the Aug 3, 2026 guidance raise.

### How the extraction was done

- This file draws on PDF pages 2, 4, 9, 14, and 71–85, read in full, plus the pages that the keyword scan flagged.
- PyMuPDF supplied the text layer. Charts and tables that exist only as images were read from page renders (PDF p.7, 14, 17, 68, 69, 72, 77, 80, 85).
- The slide-deck pages (PDF p.8–108) print a page number 7 lower than the PDF page. The note pages (PDF p.1–7) and the disclosure pages (PDF p.109–115) print the PDF page number itself.
- The text layer returned no hits on any of the 115 pages for "primary care", "PCP", "sales force", "rep" or "reps", "gross-to-net", "discount rate", or "probability". "WACC" appears only inside the DCF image on PDF p.7. The report writes probability of success as "POS" or "PoS".

These pages were read beyond the required set.

| PDF page | Reason for reading | AMKD commercial content |
|---|---|---|
| p.1, p.3 | Front-page summary and price target | Inaxaplin sales and PoS; povetacicept pricing |
| p.6, p.7 | Financial model and DCF | Company discount rate (WACC) |
| p.13, p.15–p.17 | Povetacicept case, pain, other pipeline, SOTP chart | Kidney pipeline value per share |
| p.18 (repeated on p.37, 70, 86, 98) | Summary slide | Diagnosis-rate bullets |
| p.24, p.30, p.33, p.34 | Hits on "prior auth", "genotype", and "net price" | None; all four pages cover cystic fibrosis |
| p.38–p.69 | Povetacicept section | IgAN pricing, sales, and biopsy comments |
| p.106 | Catalyst table | Inaxaplin interim readout timing |
| p.107 | Management biographies, including the CEO | CEO is a practicing nephrologist |
| p.108, p.109 | Rating risks; valuation summary | AMKD Phase 3 risk; pipeline value per share |
| p.110, p.112 | Disclosures | Labcorp, Natera, and Maze named |

## 2. AMKD details

The report describes AMKD (APOL1-mediated kidney disease) as "a genetic condition where 2 copies of the risk variant leads to accelerated kidney function decline" (PDF p.72). Inaxaplin (VX-147) is Vertex's APOL1 channel inhibitor (PDF p.72).

### Launch year

- The report does not state a launch year for inaxaplin.
- The Jefferies revenue chart shows $0 in 2026 and $141M in 2027 (PDF p.85; the same chart appears on PDF p.14). The model's first revenue year is 2027.
- The consensus series on the same chart shows $0 in 2026 and $56M in 2027 (PDF p.85). The chart's source line names Visible Alpha, a consensus data provider.

### Approval path

- The report calls AMPLITUDE (trial NCT05312879) "the registrational trial for accelerated approval" (PDF p.74). Accelerated approval is an FDA pathway that approves a drug on a surrogate endpoint, a lab measure expected to predict clinical benefit, and requires a later confirmatory result.
- AMPLITUDE "aims to have evaluate UPCR reduction & eGFR slope at 48wks (interim filing data)" (PDF p.72). UPCR (urine protein-to-creatinine ratio) measures protein leaking into the urine. eGFR (estimated glomerular filtration rate) measures kidney function, and the eGFR slope is its rate of change over time.
- The report does not say which endpoint the FDA requires for accelerated approval or for full approval.
- Inaxaplin "has FDA breakthrough designation" (PDF p.72). Breakthrough designation is an FDA status that gives a promising drug more frequent FDA guidance during development.
- AMPLITUDE is an adaptive Phase 2/3, double-blind, placebo-controlled trial with 466 patients, about 233 per arm (PDF p.71, p.74). Its estimated primary completion date is 5/31/2026, and its estimated study completion date is 6/30/2026 (PDF p.71).
- The report gives two timings for interim data. PDF p.71 says "interim data exp YE'26/early'27". PDF p.2 and p.106 list the interim readout in 1H26.
- Jefferies forecasts a 64–70% UPCR reduction at 48 weeks (PDF p.4, p.14, p.74). Jefferies also forecasts eGFR near 48 mL/min/1.73m² at 48 weeks, a decline of about 3 mL/min/1.73m² (PDF p.74).
- The Phase 2a trial showed a 47.6% UPCR reduction at 13 weeks (PDF p.73).
- The AMKD KOL "stated UPCR is important, but clinically meaningful endpoint is preserving/slowing eGFR decline" (PDF p.79). A KOL (key opinion leader) is an outside physician expert the analysts interviewed.
- The same KOL said an approval on UPCR alone would meet "limited academic resistance" because no approved alternatives exist (PDF p.79).

### List price, net price, and gross-to-net

- The report gives no US list price, net price, or gross-to-net discount for inaxaplin. Gross-to-net is the gap between list price and the price the maker keeps after rebates and discounts.
- The AMKD KOL "believes VRTX unlikely to price unreasonably given duration, volume, and health equity considerations" (PDF p.79).
- The only kidney-drug price in the report is sibeprenlimab's IgAN price of $390K per year (PDF p.3, p.13). The povetacicept section of this file (section 3) covers that price.

### Patients on therapy by year

- The report gives no count of treated patients for any year.
- The report sizes patient pools only, as shown in the population subsection below.

### Peak and 2035 sales

| Measure | Jefferies | Consensus | Page |
|---|---|---|---|
| Peak sales in the text | "~$3Bn risk adjusted peak sales" | "$2.2Bn" | PDF p.85; also p.2, p.4, p.14 |
| Highest bar in the 2026–2040 chart | $3,057M in 2037 and in 2038 | $2,193M in 2040 | PDF p.85 |
| 2035 | $2,729M | $1,637M | PDF p.85 |
| 2040 | $1,788M | $2,193M | PDF p.85 |

- The chart does not print a unit, a geography, or whether its bars are risk-adjusted. Risk-adjusted sales are forecasts scaled down for the chance that the drug fails in development.
- This file reads the Jefferies bars as risk-adjusted $M. That reading is an inference. The same page calls the ~$3Bn peak "risk adjusted", and the tallest Jefferies bar is 3,057.
- The Jefferies series falls from $3,057M in 2038 to $1,987M in 2039 (PDF p.85). The report does not explain the drop.
- The report gives no unadjusted sales figure and no split between US and worldwide sales.
- Jefferies attributes its above-consensus ramp to "the early mover advantage for VRTX being first to market" (PDF p.85).
- The number table in section 5 lists the full 2026–2040 series for Jefferies and for consensus.

### Probability of success and discount rate

- Jefferies assigns inaxaplin a 60% probability of success (PoS), meaning the chance that the drug reaches approval (PDF p.4, p.14).
- The company-wide DCF (discounted cash flow valuation) uses a 7.5% WACC (weighted average cost of capital, the discount rate) and 1.0% perpetuity growth (PDF p.7).
- The DCF uses a valuation date of 12/31/2025 and 256M shares, and it yields $580 per share (PDF p.7).
- The DCF sensitivity grid runs from $500.09 per share (8.5% WACC, 0% growth) to $711.33 per share (6.5% WACC, 2.0% growth) (PDF p.7).
- The report states no separate discount rate for inaxaplin or AMKD.
- The SOTP (sum-of-the-parts) chart assigns $30 per share to "Other Kidney Pipeline Products (VX-147 + VX-407)" (PDF p.17). VX-407 is Vertex's drug for ADPKD (autosomal dominant polycystic kidney disease). The report does not split the $30 between the two drugs.
- This file calculates $30 × 256M shares = $7.68B for inaxaplin and VX-407 combined, using the DCF share count (PDF p.7, p.17).
- The SOTP bars sum to the price target (calculated: $48 net cash + $376 cystic fibrosis + $81 povetacicept + $25 pain + $30 kidney pipeline + $20 other = $580; PDF p.17).
- PDF p.109 values "pipeline diversification (pove + AMKD + ADPKD; ~$131/sh)". The povetacicept and kidney-pipeline SOTP bars sum to $111 (calculated: $81 + $30). Adding the $20 "Other Products/Pipeline" bar gives $131 (calculated). The report does not show how it built the $131.

### Population definitions

#### US and US-plus-Europe

- Vertex estimates about 250K AMKD patients in the US and EU (PDF p.4, p.14, p.80). PDF p.80 cites a 2025 Vertex presentation at ASN (American Society of Nephrology) as the source.
- Jefferies builds a US estimate on PDF p.80. The table below reproduces it and checks each printed calculation.

| Row as printed (PDF p.80) | Value | Source note as printed | Arithmetic check (calculated) |
|---|---|---|---|
| US Black/African American Population | 48,300,000 people | US Census 2023 | No calculation shown |
| APOL1 High-Risk Genotype Prevalence | 13.0% | Pollak 2023 | No calculation shown |
| US High-Risk APOL1 Population | 6,279,000 people | Calculated | 48,300,000 × 13.0% = 6,279,000 |
| Disease Penetrance (% developing kidney disease) | 20.0% | "Pollak 2023: ~20% develop overt disease" | No calculation shown |
| Total AMKD Patient Pool (US) – Bottom-Up | 1,255,800 patients | Calculated | 6,279,000 × 20.0% = 1,255,800 |
| VRTX Total AMKD (US+EU) | 250,000 patients | VRTX ASN Presentation 2025 | No calculation shown |
| Estimated US Share of Total | 85% | "US has ~83% of US+EU Black pop" | No calculation shown |
| VRTX Implied US AMKD Patients | 212,500 patients | Calculated | 250,000 × 85% = 212,500 |
| US Patient Estimate (Average) | 734,150 patients | Average of bottom-up & VRTX estimate | (1,255,800 + 212,500) ÷ 2 = 734,150 |
| VRTX US AMKD Estimate (base) | 212,500 patients | VRTX-based estimate | Equals the implied US figure |
| Currently Diagnosed (%) | 30% | "VRTX: 'majority not diagnosed'" | No calculation shown |
| Currently Diagnosed Patients (US) | 63,750 patients | Calculated | 212,500 × 30% = 63,750 |
| Future Diagnosis Rate (improved awareness) | 60% | "With genetic testing adoption" | No calculation shown |
| Future Diagnosed Patients (US) | 127,500 patients | "At market maturity" | 212,500 × 60% = 127,500 |
| Primary AMKD (AMPLITUDE trial target) | 127,500 patients | "Est. 60% primary AMKD" | 212,500 × 60% = 127,500 |
| AMKD w/ Moderate Proteinuria or Diabetes | 85,000 patients | "VRTX AMPLIFIED trial target" | Equals 212,500 − 127,500 |
| Total Addressable US Patients | 212,500 patients | Sum of segments | 127,500 + 85,000 = 212,500 |

- A highlight box on the page covers part of the 85% cell. The printed 212,500 equals 250,000 × 85% (calculated), which confirms the value.
- The note beside the 85% says the US holds "~83% of US+EU Black pop". At 83%, the US count would be 207,500 (calculated: 250,000 × 83%).
- This file calculates 148,750 US patients undiagnosed today (212,500 − 63,750).
- This file calculates that a move from 30% to 60% diagnosis adds 63,750 diagnosed US patients (127,500 − 63,750). The report gives no year for "market maturity".
- The "Future Diagnosed Patients" row and the "Primary AMKD" row both equal 60% of 212,500 (calculated). The report does not link the two rows.
- The PDF p.80 headline says "~1.2M pts could develop AMKD". The table labels this bottom-up figure (1,255,800) as US. The page text calls it the number "that could benefit from Inaxaplin at some point" (PDF p.80).

#### Primary AMKD versus the AMPLIFIED population

- A Vertex graphic reproduced on PDF p.72 lists "~150K" patients for "Inaxaplin – Primary AMKD" (the AMPLITUDE trial). The same graphic lists "~100K" for "Inaxaplin – AMKD with moderate proteinuria or diabetes" (the AMPLIFIED trial). The graphic prints no geography.
- The two graphic numbers sum to 250K (calculated), the same as the US-plus-EU estimate. The primary share is 60% (calculated: 150 ÷ 250), the same split that the Jefferies US table uses.
- AMPLITUDE enrolls "Adult & pediatric AMKD" patients with genotype G1/G1, G2/G2, or G1/G2 and proteinuric kidney disease (PDF p.71). The trial-registry screenshot on PDF p.77 lists ages 10 to 65.
- AMPLITUDE excludes transplant recipients, patients with uncontrolled hypertension, patients with a history of diabetes mellitus, and patients with another known cause of kidney disease, including sickle cell disease (PDF p.71, p.77).
- AMPLIFIED is a single-arm, open-label Phase 2b with 45 patients who have "proteinuric AMKD ± comorbid CKD drivers incl. diabetes" and eGFR of at least 25 (PDF p.71). CKD means chronic kidney disease.
- AMPLIFIED tests 13 weeks of daily dosing (PDF p.72). Its data are expected in 2H26, and its estimated primary completion date is 12/30/2026 (PDF p.71).
- The Phase 2a trial (16 patients) required biopsy-proven APOL1-mediated FSGS (focal segmental glomerulosclerosis, scarring of the kidney's filters) (PDF p.71).
- Jefferies expects AMPLITUDE's younger patients (under 18) and "lowering the proteinuria threshold (2-3 g/g vs 0.7 g/g)" to add more reversible disease than the Phase 2a had (PDF p.73). Jefferies adds that "allowing eGFR 25-45" brings in more severe patients (PDF p.73).

#### Diabetic versus non-diabetic

- AMPLITUDE excludes patients with a history of diabetes, and AMPLIFIED includes them (PDF p.71, p.77).
- Jefferies says the AMPLITUDE population "does not including diabetics (therefore not being as pretreated for BL eGFR)" (PDF p.4). BL means baseline.
- The report gives no separate count of AMKD patients with diabetes. The 85,000 US figure combines moderate proteinuria and diabetes in one segment (PDF p.80).
- A chart on PDF p.14 and p.77 tracks the share of APOL1 patients free of a composite kidney endpoint over time. The chart shows patients with diabetes reaching the endpoint faster. Jefferies attributes this finding to Maze data (PDF p.77).

### Diagnosis, testing, primary care, referral, biopsy, and payers

#### Diagnosis rates

- Jefferies assumes that 30% of US AMKD patients are diagnosed today and that 60% will be diagnosed at "market maturity" (PDF p.80).
- The 30% row cites "VRTX: 'majority not diagnosed'", and the 60% row cites "With genetic testing adoption" (PDF p.80). The report gives no other evidence for either rate.
- Jefferies expects "dx rates to increase following tx approvals" (PDF p.4). In the report, dx means diagnosis and tx means treatment.
- Jefferies names two sources of higher diagnosis rates (PDF p.80, p.18). The first is awareness carried over from povetacicept's IgAN launch, which the report calls "spillover". The second is growth of Vertex's no-cost testing program after a treatment is approved.
- Jefferies keeps "conservative penetration given the lower socio-economic status of these pts" (PDF p.4, p.14).
- Jefferies expects Vertex's entry to "improve genetic screening for a clearly defined genotype leading to a bigger market size" (PDF p.85).

#### Testing

- The report says "Diagnosis requires APOL1 genetic testing (and sometimes biopsy)" (PDF p.72).
- Vertex offers "no-cost APOL1 genetic testing (partnerships with Arkana, Labcorp, and Natera) for eligible pts" (PDF p.80). Jefferies expects the program "to expand once there would be a proven tx for the disease" (PDF p.80).
- A reproduced Vertex web graphic on PDF p.80 describes each lab's offer. Arkana Laboratories offers a single-gene APOL1 test with free genetic counseling before and after. Labcorp offers a single-gene APOL1 test with free genetic counseling "for patients with confirmed APOL1 risk variants". Natera offers "a renal panel test for 397 genes, including APOL1", with free counseling before and after.
- The report gives no test volumes, turnaround times, eligibility rules, or program costs.

#### Primary care

- The report's text layer does not mention primary care or PCPs on any page. The AMKD page images (PDF p.14, 72, 77, 80, 81, 85) do not mention them either.
- The AMKD KOL speaks of "community" practice (PDF p.79). The report does not say whether "community" means primary care or community nephrology. The same bullet names "CKD clinic + dialysis rounding" as the workflow (PDF p.79).

#### Referral

- The AMKD KOL's clinic "functions largely as a 2nd-opinion referral hub, often w/o clear initial dx" and sees "~25 new AMKD dx/yr" (PDF p.79).
- The AMKD KOL ties underdiagnosis to "delayed lab recognition and referral" (PDF p.79).

#### Biopsy

- The AMKD KOL "favors genetics + biopsy together" (PDF p.79).
- The AMKD KOL "sees histopathology as complementary SOC in advanced proteinuria" (PDF p.79). Histopathology is microscope review of a kidney biopsy, and SOC means standard of care.

#### Payer criteria

- The AMKD KOL expects "payers to require 1) high-risk genotype, 2) histopathology consistent w/ AMKD-spectrum lesions, and 3) clinical activity (proteinuria and/or early eGFR loss)" (PDF p.79).
- The AMKD KOL says "Genotype alone unlikely sufficient" and "expects MAZE to mirror VRTX access strategy in-market" (PDF p.79).

### Expert call on AMKD (PDF p.79)

Jefferies interviewed Dr. Peter Czarnecki, a nephrologist at BWH/HMS (Brigham and Women's Hospital / Harvard Medical School). He directs the PKD/Kidney Genetics Clinic at BIDMC (Beth Israel Deaconess Medical Center) (PDF p.79).

| Topic | Number | Short quote | Page |
|---|---|---|---|
| Share eventually diagnosed | ~75% | "~75% ultimately receive correct dx (timing heterogeneous)" | PDF p.79 |
| Progression before diagnosis | ~15–25% | "~15–25% have unfavorable courses partly driven by delay/misdirection, some progressing to ESRD pre-dx" | PDF p.79 |
| Time to diagnosis | ~3–6 months on the ideal path | "ideal pathway (~3-6 mo) vs real-world delays often spanning years, w/ irreversible damage accruing" | PDF p.79 |
| Likely payer requirements | Genotype, biopsy findings, and disease activity | "Genotype alone unlikely sufficient" | PDF p.79 |
| Who gets treated | No number | "tx reserved for established AMKD (not genotype+ alone)" | PDF p.79 |
| Visit length in community practice | ~15 minutes | "community time constraints (~15 min visits) make extra labs/screening a deterrent" | PDF p.79 |
| Lifelong therapy | No number | "if effective/tolerable, likely lifelong" | PDF p.79 |
| Adoption order | No number | "academic centers to adopt first, w/ community uptake driven by education diffusion" | PDF p.79 |
| Treatment burden | No number | "if inaxaplin remains oral + well-tolerated, friction should be lower" | PDF p.79 |
| Immediate treatable market | ~250K, US and EU | "smaller immediate treatable market (~e.g., ~250k US/EU)" | PDF p.79 |
| Disease trigger | No number | "a 'second hit' (often infection/cytokine surge) can precipitate overt AMKD" | PDF p.79 |

- ESRD means end-stage renal disease, the stage that needs dialysis or a transplant.
- Jefferies separately expects "pts to stay on tx lifelong" (PDF p.81). Jefferies gives two reasons. Inaxaplin does not correct the underlying gene defect, and Alport syndrome, another genetic kidney disease, is treated for life (PDF p.81).

### Other AMKD mentions

- AMKD patients reach dialysis "~9-12 years earlier than those without the genotype" (PDF p.72).
- Jefferies lists competing APOL1 programs (PDF p.72). Maze's MZE829 is in Phase 2 with 56 patients (PDF p.71). Maze's MZ-301 is preclinical. Lilly collaborates on an exploratory Phase 2 of baricitinib.
- AstraZeneca's AZD2373, an antisense drug, is in a Phase 2b with 96 patients and an August 2027 PCD (primary completion date) (PDF p.72, p.78).
- VX-840, another Vertex APOL1 channel blocker, has completed Phase 1 (PDF p.72).
- The report's ESG section poses a management question about "clinical trial diversity when enrolling for diseases such as APOL-1-mediated kidney diseases" (PDF p.2).
- The CEO biography says Reshma Kewalramani "is a practicing nephrologist" (PDF p.107).
- The Chief Commercial Officer biography credits Duncan McKechnie with "preparation for launches in new disease areas" (PDF p.107). Neither biography mentions AMKD launch plans or field teams.
- The disclosures state that Jefferies makes a market in (trades as a dealer) Labcorp Holdings and Maze securities (PDF p.110).
- The list of other companies mentioned shows Jefferies Buy ratings on Labcorp and Natera (PDF p.112).

### Conflicts inside the report

- The AMPLITUDE interim readout appears as 1H26 on PDF p.2 and p.106, and as "YE'26/early'27" on PDF p.71.
- AMPLITUDE appears as "Adult & pediatric" on PDF p.71, with ages 10–65 on PDF p.77, and as a study "in adults" on PDF p.72.
- The US share of the 250K appears as 85% in the value column and as "~83%" in the note on PDF p.80.
- Maze's MZE829 data appear as "exp Q1'26" on PDF p.71 and as 2H26 on PDF p.76 and p.106.
- The $131 per share pipeline value on PDF p.109 exceeds the $111 sum of the povetacicept and kidney-pipeline SOTP bars on PDF p.17 (calculated).

## 3. Povetacicept and the kidney business

### IgAN pricing and class prices

- Otsuka's sibeprenlimab, an anti-APRIL drug, won FDA approval for IgAN (IgA nephropathy) in November 2025 (PDF p.44, p.58).
- Sibeprenlimab launched at $390K per year (PDF p.13, p.50). Consensus had assumed about $200K per year (PDF p.3, p.13, p.50).
- The report does not say whether the $390K is a list price or a net price.
- Jefferies writes that sibeprenlimab's price "paves the way for Pove to match their price assuming efficacy is similar" (PDF p.50).
- The report gives no other IgAN class list prices.
- Sibeprenlimab had "~500 pts starts after launch in late 2025" (PDF p.13).

### Launch timing

- The report does not state a povetacicept FDA decision date or launch date.
- The Jefferies chart shows $0 povetacicept revenue in 2026 and $299M in 2027 (PDF p.68). The consensus series on the same chart shows $1M in 2026 and $120M in 2027 (PDF p.68).
- Jefferies says povetacicept "will enter the market for IgAN first and raise kidney disease awareness" (PDF p.80).
- The RAINIER Phase 3 interim analysis showed a 52% UPCR reduction from baseline at week 36, or 49.8% after placebo adjustment (PDF p.3, p.39).
- RAINIER enrolled about 600 patients in 15 months (PDF p.50).
- Povetacicept's Phase 3 dose is 80 mg (PDF p.38). Vertex is running trials of a 0.46 mL monthly at-home autoinjector (PDF p.38), and Vertex reports a 1.5-second injection time (PDF p.49). Sibeprenlimab uses a 2 mL prefilled syringe (PDF p.49).

### Sales and value

- Jefferies models $8.5B in total risk-adjusted peak sales for povetacicept, against $5.8B for consensus (PDF p.1, p.3, p.68). IgAN contributes $6B of that peak (PDF p.3, p.68).
- The IgAN chart labels its series worldwide, and the Jefferies IgAN series peaks at $5,982M in 2036 and 2037 (PDF p.68).
- Jefferies assigns a PoS of 90% for IgAN, 60% for gMG (generalized myasthenia gravis), 55% for pMN (primary membranous nephropathy), and 50% for wAIHA (warm autoimmune hemolytic anemia) (PDF p.68).
- Jefferies models risk-adjusted peaks of $1B for gMG, about $1B for pMN, and $475M for wAIHA (PDF p.68).
- The Jefferies total povetacicept series peaks at $8,486M in 2038 (PDF p.68).
- Jefferies sizes the IgAN market at "$15-20Bn in size at peak" (PDF p.1).
- Jefferies estimates about 408K IgAN patients in the US and EU, made up of about 214K in the US and 194K in the EU (PDF p.50). Vertex's estimate is about 330K (PDF p.50).
- Jefferies expects povetacicept revenue to reach about 50% of cystic fibrosis revenue (PDF p.1). The chart on PDF p.69 shows 54% in 2038.
- The SOTP assigns povetacicept $81 per share (PDF p.17).
- PDF p.68 also says "For IgAN alone, we model risk adj. ~$8.5Bn" and "~$8.5Bn peak sales by 2037". Both statements conflict with the $6B IgAN figure on the same page and with the 2038 peak of the total series.

### Nephrology sales force

- The report does not state the size or structure of Vertex's nephrology sales force or of any field team.

### IgAN expert (PDF p.53)

- Jefferies cites Dr. Geoff Teehan, Chief of Nephrology at Kidney Care Specialists LLC (PDF p.53).
- The IgAN KOL said "IgAN must be diagnosed by biopsy" (PDF p.53).
- The IgAN KOL "did not think that there would be a significant increase in biopsies being performed" (PDF p.53).
- The IgAN KOL gets referrals "from private practice nephrologists" (PDF p.53).
- The IgAN KOL noted "a lot of paperwork required to put patients on medications" (PDF p.53).
- The IgAN KOL estimated 33% market share for new agents and 30–50%+ for the APRIL/BAFF drug class (PDF p.53).

### Other kidney programs

- VX-407 for ADPKD carries a risk-adjusted peak of about $974M, in line with consensus (PDF p.4, p.14, p.85).
- Vertex management estimates about 30K VX-407 patients (PDF p.82). The VX-407 Phase 1 (159 patients) finished in June 2025 (PDF p.82). The Phase 2a has 24 patients, and the Phase 2 PCD is July 2027 (PDF p.82).
- The VX-407 text says the peak comes "by 2037", but the chart shows $860M in 2037 and $974M in 2039 and 2040 (PDF p.85).
- The OLYMPUS trial tests povetacicept against tacrolimus in pMN, with about 176 patients and a December 2028 PCD (PDF p.61).
- Vertex estimates about 150K pMN patients in the US and EU, and Jefferies models about 119K (PDF p.60).
- VX-840, another Vertex APOL1 channel blocker, has completed Phase 1 (PDF p.72).
- Vertex management said on 12 Feb 2026, "We anticipate that the renal franchise will ultimately rival the scale of our CF business" (PDF p.68, p.85).

## 4. Risks named in the report

### Rating risks (PDF p.9, p.108)

- The report lists "AMKD fails in its Ph.3 trial or competitor program shows better data".
- The report lists "Povetacicept has poor market uptake in IgAN or high rates of chronic safety issues emerge (eg, infection, hypogammaglobulinemia)".
- The report lists "Competitor CF programs take share from VRTX or Alyftrek switch rate is minimal".

### Downside scenario (PDF p.2)

- The $380 downside scenario assumes a weaker cystic fibrosis business or macro risk, such as in the EU.
- The downside scenario also assumes "Lower PoS and limited value from VRTX non-CF pipeline".
- The downside scenario limits pain to acute use, with $1.5B peak sales.

### AMKD risks in the body of the report

- Jefferies holds penetration down because of patients' "lower socio-economic status" (PDF p.4, p.14). PDF p.80 adds that "socio-economic factors could reduce penetration".
- Vertex management said the Phase 2 UPCR benefit "could stay stable at 13 weeks. That could be the maximal effect." (PDF p.73).
- The AMKD KOL said "irreversible structural damage remains the key unknown" (PDF p.79).
- The AMKD KOL expects eGFR to lag proteinuria "w/ uncertain timing" (PDF p.79).
- The AMKD KOL expects payers to require biopsy findings, not genotype alone (PDF p.79).
- The AMKD KOL said short community visits make extra labs and screening "a deterrent" (PDF p.79).
- The AMKD KOL described real-world diagnostic delays "often spanning years" (PDF p.79).
- Competitors include Maze's MZE829, AstraZeneca's AZD2373, and Lilly's baricitinib (PDF p.72). Jefferies writes that it is "not worried" about MZE829 (PDF p.76).

### Povetacicept and IgAN risks

- Povetacicept's overall infection rate rose with dose in IgAN, from 43% at 80 mg to 64% at 240 mg (PDF p.58).
- The earlier IgAN Phase 2 reported 1 severe case of hypogammaglobulinemia (low antibody levels) at 80 mg and 4 severe cases at 240 mg (PDF p.46).
- Jefferies expects sibeprenlimab's live-vaccine warning "could also apply to Pove" (PDF p.44).
- The IgAN KOL's market-share comment calls the biopsy requirement "a key headwind" (PDF p.53).

### General risks

- The disclosure section lists general price-target risks, including economic, political, and currency changes (PDF p.111).

## 5. Every number extracted

| Variable | Value | Unit | Geography | Year | Risk-adjusted? | PDF page |
|---|---|---|---|---|---|---|
| Price target | 580 | $ per share | n/a | 12-month target | n/a | p.1, p.9 |
| Upside to price target | 26 | % | n/a | vs 3/9/2026 close | n/a | p.1, p.9 |
| Share price used | 460.87 | $ per share | n/a | 3/9/2026 close | n/a | p.1, p.9 |
| Upside scenario value | 700 (+52%) | $ per share | n/a | 12-month | n/a | p.2 |
| Downside scenario value | 380 (−18%) | $ per share | n/a | 12-month | n/a | p.2 |
| DCF discount rate (WACC) | 7.5 | % | Company-wide | Valuation date 12/31/2025 | n/a | p.7 |
| DCF perpetuity growth | 1.0 | % | Company-wide | Terminal value | n/a | p.7 |
| DCF share count | 256 | Million shares | n/a | n/a | n/a | p.7 |
| DCF fair value | 580 | $ per share | n/a | n/a | n/a | p.7 |
| DCF sensitivity, low end | 500.09 | $ per share | n/a | 8.5% WACC, 0% growth | n/a | p.7 |
| DCF sensitivity, high end | 711.33 | $ per share | n/a | 6.5% WACC, 2.0% growth | n/a | p.7 |
| SOTP net cash | 48 | $ per share | n/a | n/a | n/a | p.17 |
| SOTP cystic fibrosis | 376 | $ per share | n/a | n/a | Not stated | p.17 |
| SOTP povetacicept | 81 | $ per share | n/a | n/a | Not stated | p.17 |
| SOTP pain | 25 | $ per share | n/a | n/a | Not stated | p.17 |
| SOTP other kidney pipeline (VX-147 + VX-407) | 30 | $ per share | n/a | n/a | Not stated | p.17 |
| SOTP other products/pipeline | 20 | $ per share | n/a | n/a | Not stated | p.17 |
| SOTP total (calculated sum of bars) | 580 | $ per share | n/a | n/a | n/a | p.17 |
| Pipeline diversification value (pove + AMKD + ADPKD) | ~131 | $ per share | n/a | n/a | Not stated | p.109 |
| Povetacicept + kidney pipeline bars (calculated: 81 + 30) | 111 | $ per share | n/a | n/a | Not stated | p.17 |
| VX-147 + VX-407 value (calculated: 30 × 256M) | 7.68 | $B | n/a | n/a | Not stated | p.7, p.17 |
| Inaxaplin PoS | 60 | % | Not stated | n/a | n/a | p.4, p.14 |
| Inaxaplin peak sales, Jefferies (text) | ~3 | $B | Not stated | Not stated | Yes (per text) | p.2, p.4, p.14, p.85 |
| Inaxaplin peak sales, consensus (text) | ~2.2 | $B | Not stated | Not stated | Not stated | p.4, p.14, p.85 |
| Inaxaplin revenue, Jefferies | 0 | $M (unit not printed) | Not stated | 2026 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 141 | $M (unit not printed) | Not stated | 2027 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 436 | $M (unit not printed) | Not stated | 2028 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 871 | $M (unit not printed) | Not stated | 2029 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 1,200 | $M (unit not printed) | Not stated | 2030 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 1,506 | $M (unit not printed) | Not stated | 2031 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 1,811 | $M (unit not printed) | Not stated | 2032 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 2,117 | $M (unit not printed) | Not stated | 2033 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 2,423 | $M (unit not printed) | Not stated | 2034 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 2,729 | $M (unit not printed) | Not stated | 2035 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 3,034 | $M (unit not printed) | Not stated | 2036 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 3,057 | $M (unit not printed) | Not stated | 2037 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 3,057 | $M (unit not printed) | Not stated | 2038 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 1,987 | $M (unit not printed) | Not stated | 2039 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, Jefferies | 1,788 | $M (unit not printed) | Not stated | 2040 | Not labeled on chart | p.85, p.14 |
| Inaxaplin revenue, consensus | 0 | $M (unit not printed) | Not stated | 2026 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 56 | $M (unit not printed) | Not stated | 2027 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 222 | $M (unit not printed) | Not stated | 2028 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 479 | $M (unit not printed) | Not stated | 2029 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 724 | $M (unit not printed) | Not stated | 2030 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 977 | $M (unit not printed) | Not stated | 2031 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,179 | $M (unit not printed) | Not stated | 2032 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,347 | $M (unit not printed) | Not stated | 2033 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,483 | $M (unit not printed) | Not stated | 2034 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,637 | $M (unit not printed) | Not stated | 2035 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,832 | $M (unit not printed) | Not stated | 2036 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,801 | $M (unit not printed) | Not stated | 2037 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 1,855 | $M (unit not printed) | Not stated | 2038 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 2,172 | $M (unit not printed) | Not stated | 2039 | Not stated | p.85, p.14 |
| Inaxaplin revenue, consensus | 2,193 | $M (unit not printed) | Not stated | 2040 | Not stated | p.85, p.14 |
| AMPLITUDE enrollment | 466 (~233 per arm) | Patients | Global | n/a | n/a | p.71, p.74 |
| AMPLITUDE estimated primary completion | 5/31/2026 (text: "May 2026") | Date | Global | 2026 | n/a | p.71, p.72, p.74 |
| AMPLITUDE estimated study completion | 6/30/2026 | Date | Global | 2026 | n/a | p.71 |
| AMPLITUDE interim data timing | YE'26/early'27 | Period | Global | 2026–2027 | n/a | p.71 |
| AMPLITUDE interim readout timing | 1H26 | Period | Global | 2026 | n/a | p.2, p.106 |
| AMPLITUDE eligible ages | 10 to 65 | Years of age | Global | n/a | n/a | p.77 |
| AMPLITUDE analysis timepoint | 48 | Weeks | Global | n/a | n/a | p.72, p.74 |
| AMPLIFIED enrollment | 45 | Patients | Not stated | n/a | n/a | p.71 |
| AMPLIFIED eGFR entry floor | 25 (printed as "eGFR ≥25") | As printed, no unit | Not stated | n/a | n/a | p.71 |
| AMPLIFIED dosing period | 13 | Weeks | Not stated | n/a | n/a | p.72 |
| AMPLIFIED data timing | 2H26 | Period | Not stated | 2026 | n/a | p.71 |
| AMPLIFIED estimated primary completion | 12/30/2026 | Date | Not stated | 2026 | n/a | p.71 |
| Phase 2a enrollment | 16 | Patients | Not stated | n/a | n/a | p.71 |
| Phase 2a UPCR reduction | 47.6 | % | Not stated | Week 13 | n/a | p.73 |
| AMPLITUDE proteinuria threshold vs Phase 2a | "2-3 g/g vs 0.7 g/g" | g/g | Not stated | n/a | n/a | p.73 |
| AMPLITUDE eGFR range admitted | 25–45 | mL/min/1.73m² | Not stated | n/a | n/a | p.73 |
| AMPLITUDE younger patients | Under 18 | Years of age | Not stated | n/a | n/a | p.73 |
| Jefferies UPCR forecast | 64–70 | % reduction | Not stated | Week 48 | n/a | p.4, p.14, p.74 |
| Jefferies eGFR forecast | ~48 | mL/min/1.73m² | Not stated | Week 48 | n/a | p.74 |
| Jefferies eGFR decline forecast | ~3 | mL/min/1.73m² | Not stated | To week 48 | n/a | p.74 |
| Earlier dialysis with the genotype | ~9–12 | Years | Not stated | n/a | n/a | p.72 |
| AMKD patients, Vertex estimate | ~250,000 | Patients | US+EU | Not stated | n/a | p.4, p.14, p.79, p.80 |
| US Black/African American population | 48,300,000 | People | US | 2023 | n/a | p.80 |
| APOL1 high-risk genotype prevalence | 13.0 | % | US Black population | Not stated | n/a | p.80 |
| US high-risk APOL1 population | 6,279,000 | People | US | Not stated | n/a | p.80 |
| Disease penetrance | 20.0 | % | US | Not stated | n/a | p.80 |
| Total AMKD patient pool, bottom-up | 1,255,800 | Patients | US | Not stated | n/a | p.80 |
| Illustrative TAM | ~1.2M | Patients | US (per the p.80 table) | Not stated | n/a | p.80, p.85 |
| US share of the US+EU AMKD total | 85 | % | US | Not stated | n/a | p.80 |
| US share of the US+EU Black population (note) | ~83 | % | US | Not stated | n/a | p.80 |
| US AMKD count at 83% (calculated: 250,000 × 83%) | 207,500 | Patients | US | Not stated | n/a | p.80 |
| Vertex-implied US AMKD patients | 212,500 | Patients | US | Not stated | n/a | p.80 |
| US patient estimate, average | 734,150 | Patients | US | Not stated | n/a | p.80 |
| Currently diagnosed share | 30 | % | US | Today | n/a | p.80 |
| Currently diagnosed patients | 63,750 | Patients | US | Today | n/a | p.80 |
| Undiagnosed patients (calculated: 212,500 − 63,750) | 148,750 | Patients | US | Today | n/a | p.80 |
| Future diagnosis rate | 60 | % | US | "Market maturity" | n/a | p.80 |
| Future diagnosed patients | 127,500 | Patients | US | "Market maturity" | n/a | p.80 |
| Added diagnosed patients (calculated: 127,500 − 63,750) | 63,750 | Patients | US | "Market maturity" | n/a | p.80 |
| Primary AMKD (AMPLITUDE target) | 127,500 | Patients | US | Not stated | n/a | p.80 |
| Primary AMKD share of US total | 60 | % | US | Not stated | n/a | p.80 |
| AMKD with moderate proteinuria or diabetes (AMPLIFIED target) | 85,000 | Patients | US | Not stated | n/a | p.80 |
| Total addressable US patients | 212,500 | Patients | US | Not stated | n/a | p.80 |
| Primary AMKD, Vertex graphic | ~150K | Patients | Not printed | Not stated | n/a | p.72 |
| AMKD with moderate proteinuria or diabetes, Vertex graphic | ~100K | Patients | Not printed | Not stated | n/a | p.72 |
| Vertex graphic total (calculated: 150K + 100K) | 250K | Patients | Not printed | Not stated | n/a | p.72 |
| Vertex graphic primary share (calculated: 150 ÷ 250) | 60 | % | Not printed | Not stated | n/a | p.72 |
| AMKD KOL: new AMKD diagnoses at his clinic | ~25 | Diagnoses per year | One US clinic | Not stated | n/a | p.79 |
| AMKD KOL: share eventually diagnosed correctly | ~75 | % | Not stated | n/a | n/a | p.79 |
| AMKD KOL: share with unfavorable courses | ~15–25 | % | Not stated | n/a | n/a | p.79 |
| AMKD KOL: ideal diagnostic pathway | ~3–6 | Months | Not stated | n/a | n/a | p.79 |
| AMKD KOL: community visit length | ~15 | Minutes | Not stated | n/a | n/a | p.79 |
| AMKD KOL: immediate treatable market | ~250K | Patients | US+EU | n/a | n/a | p.79 |
| Labs in the no-cost testing program | 3 (Arkana, Labcorp, Natera) | Labs | Not stated | At report date | n/a | p.80 |
| Natera renal panel size | 397 | Genes | Not stated | n/a | n/a | p.80 |
| MZE829 Phase 2 enrollment | 56 | Patients | Not stated | n/a | n/a | p.71 |
| MZE829 data timing | Q1'26 (p.71); 2H26 (p.76, p.106) | Period | Not stated | 2026 | n/a | p.71, p.76, p.106 |
| AZD2373 Phase 2b enrollment | 96 | Patients | Not stated | n/a | n/a | p.78 |
| AZD2373 primary completion | August 2027 | Date | Not stated | 2027 | n/a | p.72, p.78 |
| Sibeprenlimab price | 390,000 | $ per patient per year | Not stated | Launch, late 2025 | n/a | p.3, p.9, p.13, p.50 |
| Consensus prior sibeprenlimab price assumption | ~200,000 | $ per patient per year | Not stated | Before launch | n/a | p.3, p.13, p.50 |
| Sibeprenlimab patient starts after launch | ~500 | Patients | Not stated | Late 2025 onward | n/a | p.13 |
| Sibeprenlimab FDA approval | November 2025 | Date | US | 2025 | n/a | p.44 |
| Povetacicept total peak sales, Jefferies | 8.5 | $B | Not stated | Not stated | Yes | p.1, p.3, p.68 |
| Povetacicept total peak sales, consensus | 5.8 | $B | Not stated | Not stated | Not stated | p.1, p.3, p.68 |
| Povetacicept IgAN peak sales, Jefferies | 6 | $B | Not stated | Not stated | Yes (per p.3) | p.3, p.68 |
| Povetacicept IgAN revenue, Jefferies chart peak | 5,982 | $M | Worldwide | 2036 and 2037 | Not labeled on chart | p.68 |
| Povetacicept PoS, IgAN | 90 | % | n/a | n/a | n/a | p.68 |
| Povetacicept PoS, gMG | 60 | % | n/a | n/a | n/a | p.68 |
| Povetacicept PoS, pMN | 55 | % | n/a | n/a | n/a | p.68 |
| Povetacicept PoS, wAIHA | 50 | % | n/a | n/a | n/a | p.68 |
| Povetacicept gMG peak sales | 1 | $B | Not stated | Not stated | Yes | p.68 |
| Povetacicept pMN peak sales | ~1 | $B | Not stated | Not stated | Yes | p.68 |
| Povetacicept wAIHA peak sales | 475 | $M | Not stated | Not stated | Yes | p.68 |
| Povetacicept total revenue, Jefferies | 0 | $M | Not stated | 2026 | Not labeled on chart | p.68 |
| Povetacicept total revenue, Jefferies | 299 | $M | Not stated | 2027 | Not labeled on chart | p.68 |
| Povetacicept total revenue, Jefferies (peak) | 8,486 | $M | Not stated | 2038 | Not labeled on chart | p.68 |
| Povetacicept total revenue, consensus | 1 | $M | Not stated | 2026 | Not stated | p.68 |
| Povetacicept total revenue, consensus | 120 | $M | Not stated | 2027 | Not stated | p.68 |
| Povetacicept revenue as share of cystic fibrosis revenue | ~50 (text); 54 (chart) | % | Not stated | Longer term; 2038 | n/a | p.1, p.69 |
| IgAN market size at peak | 15–20 | $B | Not stated | Peak | n/a | p.1 |
| IgAN patients, Jefferies | ~408K | Patients | US+EU | Not stated | n/a | p.50 |
| IgAN patients, Jefferies | ~214K | Patients | US | Not stated | n/a | p.50 |
| IgAN patients, Jefferies | ~194K | Patients | EU | Not stated | n/a | p.50 |
| IgAN patients, Vertex estimate | ~330K | Patients | Not stated | Not stated | n/a | p.50 |
| RAINIER UPCR reduction from baseline | 52 | % | Global | Week 36 | n/a | p.3, p.39 |
| RAINIER UPCR reduction, placebo-adjusted | 49.8 | % | Global | Week 36 | n/a | p.39 |
| RAINIER recruitment | ~600 in 15 months | Patients | Global | n/a | n/a | p.50 |
| Povetacicept dose | 80 | mg | n/a | n/a | n/a | p.38 |
| Povetacicept injection volume | 0.46 | mL | n/a | Monthly | n/a | p.38, p.49 |
| Povetacicept injection time | 1.5 | Seconds | n/a | n/a | n/a | p.49 |
| Sibeprenlimab injection volume | 2 | mL | n/a | Monthly | n/a | p.49 |
| IgAN KOL: market share for new agents | 33 | % | Not stated | n/a | n/a | p.53 |
| IgAN KOL: APRIL/BAFF class share | 30–50+ | % | Not stated | n/a | n/a | p.53 |
| VX-407 peak sales | ~974 | $M | Not stated | "by 2037" (text) | Yes | p.4, p.14, p.85 |
| VX-407 revenue, Jefferies chart | 860 | $M | Not stated | 2037 | Not labeled on chart | p.85 |
| VX-407 revenue, Jefferies chart | 974 | $M | Not stated | 2039 and 2040 | Not labeled on chart | p.85 |
| VX-407 patients, Vertex estimate | ~30K | Patients | Not stated | Not stated | n/a | p.82 |
| VX-407 Phase 1 enrollment | 159 | Patients | Not stated | Completed June 2025 | n/a | p.82 |
| VX-407 Phase 2a enrollment | 24 | Patients | Not stated | n/a | n/a | p.82 |
| VX-407 Phase 2 primary completion | July 2027 | Date | Not stated | 2027 | n/a | p.82 |
| OLYMPUS enrollment | ~176 | Patients | Not stated | n/a | n/a | p.61 |
| OLYMPUS primary completion | December 2028 | Date | Not stated | 2028 | n/a | p.61 |
| pMN patients, Vertex estimate | ~150K | Patients | US+EU | Not stated | n/a | p.60 |
| pMN patients, Jefferies model | ~119K | Patients | US+EU | Not stated | n/a | p.60 |
| Pain peak sales, downside scenario | 1.5 | $B | Not stated | Peak | Not stated | p.2 |
| Povetacicept overall infection rate, 80 mg | 43 | % | Not stated | IgAN trial | n/a | p.58 |
| Povetacicept overall infection rate, 240 mg | 64 | % | Not stated | IgAN trial | n/a | p.58 |
| Severe hypogammaglobulinemia cases, IgAN Phase 2 | 1 at 80 mg; 4 at 240 mg | Cases | Not stated | n/a | n/a | p.46 |

## 6. Fields not found

The report does not cover the following AMKD fields. This file leaves each one empty.

- The report states no inaxaplin launch year. The 2027 figure in this file is the first year of modeled revenue on the chart (PDF p.85), not a stated launch date.
- The report does not say which endpoints the FDA requires for accelerated approval or for full approval. The report says only that AMPLITUDE evaluates UPCR and eGFR slope at 48 weeks for the interim filing (PDF p.72).
- The report gives no timing or trial plan for full approval after accelerated approval.
- The report gives no US list price for inaxaplin.
- The report gives no US net price for inaxaplin.
- The report gives no gross-to-net discount for inaxaplin.
- The report gives no count of patients on therapy for any year.
- The report gives no unadjusted (not risk-adjusted) peak sales or 2035 sales for inaxaplin.
- The report gives no split of inaxaplin sales between the US and worldwide, for peak or for 2035.
- The inaxaplin revenue chart prints no unit, no geography, and no risk-adjustment label (PDF p.85).
- The report gives no discount rate specific to inaxaplin or AMKD. Only the company-wide 7.5% WACC appears (PDF p.7).
- The report does not split the $30 per share kidney-pipeline SOTP value between inaxaplin and VX-407 (PDF p.17).
- The report gives no year for the "market maturity" at which diagnosis reaches 60% (PDF p.80).
- The report gives no evidence for the 30% and 60% diagnosis rates beyond the one-line source notes on PDF p.80.
- The report gives no separate count of AMKD patients with diabetes.
- The Vertex graphic's ~150K and ~100K segments carry no geography (PDF p.72).
- The report contains no primary care content. It gives no primary care physician counts, no share of AMKD patients managed in primary care, and no primary care testing or referral rates.
- The report gives no test volumes, turnaround times, eligibility rules, or costs for the no-cost testing program.
- The report gives no referral rates or referral volumes.
- The report gives no share of AMKD patients who have had, or would need, a kidney biopsy.
- The report gives no payer mix, coverage rates, or published payer policies for inaxaplin. Only the AMKD KOL's expected criteria appear (PDF p.79).
- The report gives no treatment persistence or compliance rates. Only expectations of lifelong use appear (PDF p.79, p.81).

The report does not cover these fields for the povetacicept and kidney business section.

- The report does not state the size or structure of Vertex's nephrology sales force.
- The report gives no povetacicept FDA decision date or launch date.
- The report gives no IgAN class list prices other than sibeprenlimab's $390K per year.
- The report does not say whether sibeprenlimab's $390K per year is a list price or a net price.
