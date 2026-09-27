# APOL1-Mediated Kidney Disease (AMKD): Disease Profile for the Team

Written Sept 27, 2026. Read time about 20–25 minutes. Every fact carries a source. Numbered sources sit in section 13. Analyst figures cite the report and page as recorded in `work/research/`. Items I derived myself are marked "inference." Items I could not verify after two different searches are marked "not verified."

## Status

| Section | State |
|---|---|
| 1. Summary | Complete |
| 2. The cause | Complete |
| 3. Who is affected | Partial |
| 4. The disease spectrum | Complete |
| 5. Symptoms and course | Partial |
| 6. Diagnosis | Partial |
| 7. Underdiagnosis | Complete |
| 8. What medical societies say | Partial |
| 9. Treatment today | Complete |
| 10. Inaxaplin and the pipeline | Complete |
| 11. Equity, trust, and privacy | Complete |
| 12. Ten facts for judge Q&A | Complete |
| 13. Sources | Complete |

Nine sections are complete, four are partial, and none is unstarted. What remains:

- **Section 3:** find a published two-variant genotype frequency for Afro-Caribbean populations. Two searches returned only allele frequencies [58] and the HCHS/SOL figure for Caribbean-background Hispanic and Latino adults [12]. Also trace the "70% of excess risk" figure to a primary study; it currently rests on a 2018 review [14].
- **Section 5:** add per-patient-per-year Medicare spending for hemodialysis, peritoneal dialysis, and kidney transplant from the USRDS Annual Data Report expenditures chapter. Two fetches of USRDS returned no figures.
- **Section 6:** record the eligibility text verbatim from the Labcorp and Natera APOL1 program pages. Four URL attempts returned 404 or a connection reset, so only the Arkana page [44] and the Vertex graphic reproduced at Jefferies PDF p.80 are sourced.
- **Section 8:** confirm whether the American Society of Nephrology has any standalone position on APOL1 genetic testing. Two approaches found none. Also read the British Transplantation Society donor-testing page directly; it is cited here at one remove through the KDIGO conference paper [2].

**Terms used throughout.** AMKD means APOL1-mediated kidney disease. A *variant* is a spelling change in a gene. *Podocytes* are the cells that form the kidney's filter. *Proteinuria* means protein leaking into the urine. *eGFR* (estimated glomerular filtration rate) is a blood-test estimate of how much blood the kidneys clean per minute, reported in mL/min/1.73 m². *CKD* (chronic kidney disease) means abnormal kidney structure or function lasting at least 3 months [26]. *ESKD* (end-stage kidney disease) means kidney function low enough to need dialysis or a transplant.

---

## 1. Summary: five facts with their numbers

1. **AMKD needs two copies of a variant gene.** About 13% of African Americans, roughly 6 million people, carry two high-risk APOL1 variants [1; Morgan Stanley, Apr 19, 2026, p.5].
2. **Most carriers never get kidney disease.** The KDIGO conference report states that approximately 15% of people with a high-risk genotype will develop kidney failure [2]; Vertex and the analysts model 20% developing kidney disease [1; Morgan Stanley p.5].
3. **When it strikes, it moves fast.** African American AMKD patients lose 6.55 mL/min/1.73 m² of eGFR per year, against 3.63 for African Americans with CKD and no risk variants [Morgan Stanley p.4]. Patients with two G1 copies started dialysis at a mean age of 49.0 years, against 61.8 years for patients with no risk variant [8].
4. **Almost nobody knows they have kidney disease.** CDC reports that 87% of US adults aged 20 or older with CKD did not know they had it [30]. A laboratory-database study of 28.3 million at-risk adults found that 80.3% did not receive guideline-concordant kidney testing, and only 21.0% had a urine albumin test [31].
5. **No treatment targets the disease today.** Vertex's Sept 22, 2026 release states "There are no therapies currently approved for AMKD" [41]. Inaxaplin's Phase 2a trial cut urine protein 47.6% in 13 adherent patients (95% CI −60.0 to −31.3) [9].

---

## 2. The cause

### What the APOL1 gene and its protein normally do

The APOL1 gene tells cells how to build a protein called apolipoprotein L1. The liver makes most of the protein that circulates in blood, where it rides on HDL particles [1; 19]. The protein kills trypanosomes, the single-celled parasites that cause African sleeping sickness [1; 3].

Kidney cells make their own APOL1 as well. Immunofluorescence of non-diseased human kidney found APOL1 protein "markedly enriched in podocytes" and present in lower amounts in tubule cells, with APOL1 messenger RNA in podocytes, glomerular endothelial cells (the cells lining the filter's blood vessels), and tubules [18]. The protein is not required for healthy kidneys: a person with two inactivating APOL1 mutations had normal kidney function [6].

### The G1 and G2 variants, and why they became common

G1 carries two amino-acid substitutions, S342G and I384M. G2 carries a two-amino-acid deletion, del388N389Y [1].

**Correction to the engagement lead's summary.** The lead's note says the variants "spread in West Africa because they protect against Trypanosoma brucei rhodesiense." The geography does not line up. T. b. rhodesiense causes sleeping sickness in East Africa; T. b. gambiense causes it in West Africa [4]. Genovese and colleagues showed in 2010 that plasma carrying the variants lysed East African T. b. rhodesiense in a laboratory dish, while normal APOL1 did not [3]. A later field study in Uganda and Guinea found that G2 carried a five-fold lower susceptibility to T. b. rhodesiense infection (odds ratio 0.20, 95% CI 0.07–0.48, p = 0.0001), and that G1 was associated with symptom-free carriage of West African T. b. gambiense (odds ratio 0.33, p = 0.0005), while G2 was associated with progression to clinical disease in gambiense infection (odds ratio 3.08, p = 0.0025) [4]. The safe statement for a slide: the variants restore the ability to kill sleeping-sickness parasites that had evolved resistance, they show signatures of recent positive selection on African chromosomes, and they arose within roughly the last 10,000 years [3; 13].

### Inheritance: two copies, and what that means for a family

A person inherits one APOL1 copy from each parent. AMKD risk rises sharply only when both copies carry a variant, in any of three pairings: G1/G1, G2/G2, or G1/G2 [Jefferies, Mar 10, 2026, PDF p.71].

What this means for relatives follows standard inheritance arithmetic (inference from the recessive pattern):
- Both parents of a patient with two variants carry at least one variant each.
- When both parents carry exactly one variant, each full sibling has a 25% chance of carrying two.
- Every child of a patient with two variants inherits at least one variant, and inherits two only if the other parent also passes one.

**Correction to the lead's summary.** The lead's note says one copy carries "little kidney risk." That holds for US studies, where the effect is recessive. The H3Africa study of 8,355 people in Ghana and Nigeria found a smaller but measurable effect for one copy: CKD odds ratio 1.18 (95% CI 1.04–1.33) and FSGS odds ratio 1.61 (95% CI 1.04–2.48), against 1.25 and 1.84 for two copies [10]. Say "the large risk requires two copies," not "one copy carries no risk."

### How the variant protein injures podocytes, and what stays unknown

The leading explanation: APOL1 can punch a pore, an ion channel, through cell membranes, and the G1 and G2 variants make that pore behave abnormally inside the person's own kidney cells. The KDIGO conference report states that APOL1 "can act as an ion channel (pore)" and that the variants "alter the normal pore-forming function… leading to increased pore activity," and that risk genotypes overexpressed in podocytes "play a crucial role in podocyte injury" [2]. Ions then leak in or out, the podocyte is stressed, the filter leaks protein, and scar tissue forms.

The uncertainty is real and a nephrologist judge will probe it:
- Evidence conflicts on which ion the pore lets through. One model has it switching with acidity, chloride-selective at lower pH and potassium-selective at neutral pH [1].
- Other mechanisms have supporting data: mitochondrial dysfunction that appears before potassium loss, inflammasome activation, and Golgi dysfunction through reduced PI(4)P [1].
- Most of the data come from cells engineered to overexpress APOL1, not from human kidneys. The review states that "mechanistic insights remain limited because data significantly relies on exogenous expression of APOL1 in cell cultures" [1]. The KDIGO report adds that cell death is the standard laboratory readout, "though it is not fully clear whether cell death is important in vivo" [2].
- Do not claim one pathway is settled. Pollak and Friedman write: "We should not assume that one and only one pathway drives APOL1-associated toxicity" [6].

### The "second hit": why only a minority get sick

Two variants set the stage; something else usually has to happen. The KDIGO report lists non-genetic second hits as "high interferon states, viral infections (HIV and COVID-19), exposure to alpha, beta, or gamma interferon," with high-interferon states carrying "the strongest evidence" [2]. Interferons are immune-signaling proteins that raise APOL1 production inside kidney cells. The Kidney Medicine review adds parvovirus B19, systemic lupus erythematosus, APOL1 duplications, APOL3 deletions, and fine-particulate air pollution [1].

Two documented examples:
- Untreated HIV infection. Two APOL1 risk alleles raised the odds of HIV-associated nephropathy 29-fold (95% CI 13–68), and untreated HIV-infected people with two variants carry an estimated 50% risk of developing it [5].
- COVID-19. A 2020 case series reported 6 Black patients with COVID-19 and collapsing glomerulopathy; all 6 carried two APOL1 risk alleles, and 5 of 6 needed hemodialysis [16].

Genetics also modify penetrance in the protective direction. The p.N264K variant, inherited alongside G2, "substantially reduces the penetrance" of the G1G2 and G2G2 genotypes and renders them low-risk [17].

### Why the kidney's own APOL1 drives the injury, not the blood's

Three independent lines of evidence point at kidney-made APOL1:
1. Plasma APOL1 levels do not track with genotype or with CKD status in HIV-infected African Americans [20].
2. The liver makes most circulating APOL1, shown by genotyping circulating protein in liver-transplant recipients whose own genotype differed from their donor's [19].
3. Transplant outcomes split by organ. Deceased-donor kidneys carrying two APOL1 risk variants fail sooner (hazard ratio 2.26, p = 0.001, across 675 transplanted kidneys) [22], while deceased-donor APOL1 risk variants had minimal effect on liver transplant outcomes in 639 transplants from Black donors [21]. The recipient's own genotype has not been shown to affect graft survival [6].

The one-sentence version for the room: the kidney is injured by the APOL1 the kidney itself makes, which is why a transplanted kidney carries its donor's risk and a transplanted liver does not transfer the disease.

---

## 3. Who is affected

### Two-variant frequency by ancestry

| Population | Two-variant frequency | Source | Confidence |
|---|---|---|---|
| African Americans (US) | About 13%, roughly 6 million people | [1]; Morgan Stanley p.5 citing Srinivasan 2025 | High |
| African Americans (US), other estimates | 12–14% | [14] | High |
| Ghana and Nigeria, pooled | 29.7% across 8,355 people; 25.7% among 2,777 controls | [10] | High |
| Igbo, Nigeria | 50.1% | [10; 11] | High |
| Hausa/Fulani, Ghana | 11.4% | [10; 11] | High |
| Sub-Saharan Africa total | More than 100 million people may carry two high-risk alleles | [2] | Medium (modeled estimate) |
| Kenya (Luhya), allele level | G1 about 5%, G2 about 7% of chromosomes | [13] | High |
| Ethiopia | Four sampled populations show neither G1 nor G2 | [13] | High |
| Europe | Zero across 8 sampled populations | [13] | High |
| Hispanic or Latino adults, US | 60 of 12,226 carried two alleles; 1.0% of Caribbean-background participants and 0.1% of Mainland-background participants | [12] | High |
| Afro-Caribbean populations | **Not verified.** No published two-variant genotype frequency found after two searches. The 1000 Genomes African-Caribbean-in-Barbados sample shows a G1 allele frequency of 26.0% [58]. The AST expert panel groups Afro-Caribbeans with other African-ancestry populations for testing purposes without giving a frequency [24] | Low |

The variants are found on African chromosomes and are essentially absent from European ones [5; 13]. Vertex states plainly that AMKD "occurs in people of African ancestry" [41].

### The share who develop kidney disease

| Figure | Source | Confidence |
|---|---|---|
| About 15% of people with a high-risk genotype will develop kidney failure | [2] (KDIGO conference report, 2025) | High |
| 15% estimated lifetime risk of kidney disease for healthy two-variant carriers | AJKD life-course review, 2024 [59] | High |
| "About a 15-20% chance of developing kidney disease in their lifetime"; about 80% do not | NKF patient page, updated Feb 8, 2024 [37] | Medium (patient-education page) |
| 20% develop kidney disease | [1]; Morgan Stanley p.5; used in the Jefferies bottom-up build, Jefferies PDF p.80 | Medium |
| 4% lifetime risk of FSGS specifically; 50% risk of HIV-associated nephropathy if HIV is untreated | [5] | High |

Use the range 15–20% and name the source for whichever number goes on a slide. Vertex's own funnel uses 20%, so 20% is the figure a Vertex judge will recognize.

### How much of the higher kidney-failure rate in Black Americans APOL1 explains

Black Americans are "more than 4 times more likely to develop ESKD than White people" [38]. APOL1 explains a large part of that gap, not all of it.

- The most-quoted figure: genetic risk "accounts for 70% of the excess risk for end stage renal disease (ESRD) and FSGS among African Americans" [14]. **Flag:** this appears in a 2018 review citing Genovese 2010 and Kopp 2008; I did not find a primary paper stating 70% as its own result. Attribute it to the review, not to a primary study.
- A primary attributable-fraction calculation: two APOL1 risk alleles explain 18% of FSGS and 35% of HIV-associated nephropathy, and removing the effect "would reduce FSGS and HIVAN by 67%" [5].
- The clearest evidence that APOL1 is not the whole story comes from the CRIC study. Compared with white participants, Black participants with the high-risk genotype had a composite kidney-outcome hazard ratio of 2.68 without diabetes and 1.95 with diabetes, while Black participants with the low-risk genotype still had higher ratios of 1.57 and 1.40 [7]. The residual risk in low-risk-genotype Black participants is the part APOL1 does not explain.

### The patient counts the case uses, kept separate

Three things get confused in this case: geography (US versus US-plus-Europe), definition (primary AMKD versus the added AMPLIFIED populations), and time frame (lifetime risk versus people who have the disease now).

| Count | What it counts | Geography | Time frame | Source | Confidence |
|---|---|---|---|---|---|
| 150,000 | Primary AMKD, the AMPLITUDE population | US plus Europe | Current disease | Vertex via Morgan Stanley p.1, p.5; Vertex graphic, Jefferies PDF p.72 | High |
| 100,000 | AMKD with moderate proteinuria or diabetes, the AMPLIFIED populations | US plus Europe | Current disease | Morgan Stanley p.1, p.5; Jefferies PDF p.72 | High |
| 250,000 | The two above added together | US plus Europe | Current disease | Morgan Stanley p.1, p.5 | High |
| About 150,000 | "AMKD affects approximately 150,000 people in the U.S. and Europe" | US plus Europe | Current disease | Vertex release, Sept 22, 2026 [41] | High |
| 212,500 | Jefferies' US share, 85% of 250,000 | US | Current disease | Jefferies PDF p.80 | Medium (analyst build) |
| 127,500 | Jefferies' US primary AMKD, 60% of 212,500 | US | Current disease | Jefferies PDF p.80 | Medium |
| 85,000 | Jefferies' US moderate-proteinuria-or-diabetes segment | US | Current disease | Jefferies PDF p.80 | Medium |
| 63,750 | Jefferies' currently diagnosed US patients, at an assumed 30% diagnosis rate | US | Current disease | Jefferies PDF p.80 | Low (the 30% is an assumption with no cited data) |
| At least 250,000, 40% with diabetes | Maze's US AMKD estimate | US | Current disease | Maze via Morgan Stanley p.5 | Medium |
| More than 1 million | Maze's broader US AMKD figure, "a subset of chronic kidney disease estimated to affect over one million people in the United States alone" | US | Current disease | Maze Q2 2026 release, Aug 11, 2026 [52] | Medium |
| About 1.2 million | 6 million two-variant carriers multiplied by 20% | US | Lifetime risk | Morgan Stanley p.5; Jefferies PDF p.80 | Medium |

**Two conflicts the team must handle before judges find them.**
1. Vertex's Sept 22, 2026 release gives about 150,000 for AMKD in the US and Europe with no sub-segment label, while the earlier Vertex graphic splits 150,000 primary plus 100,000 added [41; Jefferies PDF p.72]. Quote whichever you use and label its date.
2. UBS reported after the AMPLIFIED data that about 80% of AMKD patients have modest proteinuria (`analyst_consensus.md`, section 8). If that share is right, most AMKD patients sit outside the AMPLITUDE proteinuria threshold, which does not reconcile with a 150,000/100,000 split. Treat the 80% as unconfirmed.

Never divide a US lifetime number by a US-plus-Europe current number. The 1.2 million and the 250,000 differ in both geography and time frame.

---

## 4. The disease spectrum

Two APOL1 variants do not produce one single disease. They raise the risk of several kidney patterns, at very different strengths.

| Pattern | What it is | Odds ratio with two variants | Source | Confidence |
|---|---|---|---|---|
| FSGS (focal segmental glomerulosclerosis) | Scarring in parts of some filtering units | 17 (95% CI 11–26) | [5] | High |
| HIV-associated nephropathy (HIVAN) | Rapid kidney failure in untreated HIV | 29 (95% CI 13–68) in the US; 87 reported in sub-Saharan Africa | [5]; [1] | High |
| Hypertension-attributed ESKD | Kidney failure previously blamed on high blood pressure | 7.3 (95% CI 5.6–9.5) in the original report; 7–10 in review | [3]; [6] | High |
| Non-diabetic CKD generally | Chronic kidney disease without diabetes as the cause | 2- to 4-fold | [6] | High |
| COVID-associated nephropathy (COVAN) | Collapsing glomerulopathy after COVID-19 | No odds ratio published; all 6 patients in the first case series carried two variants | [16] | Medium (small series) |
| Sickle cell disease and lupus nephritis kidney failure | Kidney disease in these settings | Listed as APOL1-associated by KDIGO's living-donor guideline | [25] | Medium |

APOL1-FSGS is the subgroup inaxaplin's first trial studied, and Morgan Stanley reports that APOL1-FSGS "only represents 4% of the AMKD population" [Morgan Stanley p.1]. That single number explains why the AMPLITUDE and AMPLIFIED trials matter commercially: the proven population is a sliver of the treatable one.

### Why AMKD was long misattributed to high blood pressure

Kidney failure in Black patients was routinely recorded as caused by hypertension. Two facts overturned that:
- Blood-pressure control behaves differently. KDIGO's living-donor guideline states that "at least a portion of kidney failure previously attributed to hypertensive nephrosclerosis in persons of African descent may be genetically mediated by coding variants in the gene for APOL1 and not modifiable by antihypertensive therapy" [25].
- In the AASK trial of 693 Black patients with hypertension-attributed CKD, the primary outcome occurred in 58.1% of the high-risk-genotype group against 36.6% of the low-risk group (hazard ratio 1.88, p < 0.001), and the effect "was not confounded by levels of blood pressure" [7].

About 50% of Black patients with hypertension-attributed ESKD carry a high-risk APOL1 genotype, and a high-risk genotype is present in about 75% of Black patients with FSGS [6]. The practical consequence for primary care: high blood pressure in these patients may be a consequence of the kidney disease rather than its cause, and treating blood pressure alone has not stopped the decline.

---

## 5. Symptoms and course

**Early disease is silent.** Nothing hurts. The patient feels normal while protein leaks into the urine and filters scar. This is why the disease is found by a test and not by a complaint.

**Signs, when they appear** [37]:
- Foamy urine, which is protein in the urine.
- Swelling in the legs, ankles, or around the eyes, called edema.
- Tiredness.
- High blood pressure, which may be a result of the kidney disease.

**Speed of decline.** AMKD moves roughly twice as fast as CKD without the variants.

| Measure | AMKD or high-risk genotype | Comparison group | Source | Confidence |
|---|---|---|---|---|
| eGFR loss per year | 6.55 mL/min/1.73 m² | 3.63 for African Americans with CKD and no risk variants | Morgan Stanley p.4 (Vertex data) | Medium |
| eGFR slope, CRIC, patients without diabetes | −2.9 (Black, high-risk) | −1.0 (Black, low-risk); −0.7 (white) | [7] | High |
| eGFR slope, CRIC, patients with diabetes | −4.3 (Black, high-risk) | −2.7 (Black, low-risk); −1.5 (white) | [7] | High |
| Reaching dialysis by 5 years | 34.1% | 23.3% for matched CKD patients | Shah et al., ASN 2025, via Oppenheimer p.10 | Medium |
| Reaching dialysis by 10 years | 50.6% | 31.5% | Same | Medium |
| Kidney transplant by 10 years | 60.5% | 36.9% | Same | Medium |
| Mean age at starting hemodialysis, two G1 copies | 49.0 ± 14.9 years | 61.8 ± 17.1 years with no risk allele (n = 407, p = 6.2 × 10⁻⁷) | [8] | High |
| Years earlier to dialysis | About 9–12 years earlier than people without the genotype | — | Jefferies PDF p.72 | Medium |

FSGS with two risk alleles also starts earlier and progresses faster to ESKD than FSGS without them (p = 0.01 and p < 0.01) [5].

**What kidney failure means for the patient.** More than 808,000 people in the US live with ESKD, 68% on dialysis and 32% with a kidney transplant [38]. In-center hemodialysis runs three times a week, about 4 hours per session, and replaces part but not all of kidney function [39]. Medicare spending on ESKD beneficiaries reached $52.3 billion in 2021 [38]. I did not find per-patient-per-year dialysis and transplant costs in a primary source after two attempts; treat per-patient cost figures as **not verified** until someone pulls the USRDS expenditures chapter.

---

## 6. Diagnosis

### The lab tests, in plain words

- **UACR** (urine albumin-to-creatinine ratio) measures albumin, the main blood protein, in urine, divided by creatinine so that a random urine sample can stand in for a 24-hour collection. KDIGO's categories: A1 is under 30 mg/g (normal to mildly increased), A2 is 30–300 mg/g (moderately increased), A3 is above 300 mg/g (severely increased) [26].
- **UPCR** (urine protein-to-creatinine ratio) measures total protein rather than albumin only, in the same way. AMKD trials use UPCR in g/g; AMPLITUDE required 0.7 to under 10 g/g [43].
- **eGFR** estimates filtration from a blood creatinine level, with cystatin C as a confirmatory marker. KDIGO categories run G1 (90 or above) to G5 (under 15, kidney failure) [26]. KDIGO's practice point 1.2.4.2 states that "use of race in the computation of eGFR should be avoided" [26].

One blood test and one urine test identify almost every patient who should then be genotyped. The urine test is the one that gets skipped: 89.6% of at-risk adults had an eGFR but only 21.0% had a UACR [31].

### The APOL1 genetic test

| Attribute | What the source says | Source | Confidence |
|---|---|---|---|
| Sample | Blood in a lavender-top EDTA tube, at least 2 mL, shipped overnight at room temperature; paraffin blocks, unstained slides, or buccal swabs also accepted (Arkana) | [44] | High |
| Turnaround | "Test Turnaround: 24hrs" (Arkana) | [44] | High |
| Cost | "No Cost to Patient APOL1 Genotyping Program," sponsored by Vertex, for "eligible*" patients; the page does not define eligibility, and directs providers to support@arkanalabs.com or 866-736-2529 | [44] | High for the wording, Low for eligibility rules |
| Genetic counseling | Pre-test counseling is described as part of the process (Arkana) | [44] | High |
| Labcorp program | Single-gene APOL1 test with free genetic counseling "for patients with confirmed APOL1 risk variants" | Vertex web graphic reproduced at Jefferies PDF p.80 | Medium (secondary reproduction) |
| Natera program | A renal panel test covering 397 genes, including APOL1, with free counseling before and after | Jefferies PDF p.80 | Medium |

**Not verified:** the Labcorp and Natera program pages themselves. Four URL attempts returned 404 or a connection reset. The eligibility rules "as each program page states them" therefore remain open. A teammate should open the three program pages in a browser and record the eligibility text verbatim; that text decides whether a primary care physician can order the test for an undiagnosed patient or only for a patient already known to have kidney disease. This is a load-bearing gap for the direct-to-patient option, because a campaign that drives patients to ask for a test fails if the free program requires a confirmed diagnosis first.

Cost as a barrier is documented in general: surveyed nephrologists ranked high cost as the top barrier to genetic testing, called "extremely significant" by 46% of those who order tests and 69% of those who do not [35].

### Who current guidance says should be tested

See section 8 for each body's exact position. In short, testing is recommended for people who already have kidney disease or are living-donor candidates, and no body recommends population screening.

### The role of kidney biopsy

A biopsy takes a small piece of kidney for microscope review. It names the pattern, such as FSGS, which genotyping cannot do.

- The Phase 2a inaxaplin trial required biopsy-proven APOL1-mediated FSGS [9; Jefferies PDF p.71].
- AMPLITUDE's registry entry criteria list genotype and proteinuric kidney disease, not a biopsy [43].
- Jefferies' AMKD expert "favors genetics + biopsy together" and sees microscope review as complementary standard of care in advanced proteinuria [Jefferies PDF p.79].
- The same expert expects payers to require a high-risk genotype, biopsy findings consistent with AMKD-spectrum lesions, and clinical activity, and says "Genotype alone unlikely sufficient" [Jefferies PDF p.79]. If that holds, every patient found in primary care still needs a nephrologist, and possibly a biopsy, before treatment starts. That makes referral capacity part of the case, not an afterthought.

### The AMKD diagnosis codes

Both codes appear in the CDC's FY2026 ICD-10-CM files, in the addenda list of additions, and FY2026 codes take effect Oct 1, 2025 [40]. The file text reads:

- **N07.B** — "Hereditary nephropathy, not elsewhere classified with APOL1-mediated kidney disease [AMKD]"
- **Z84.11** — "Family history of APOL1-mediated kidney disease [AMKD]"

Morgan Stanley records the same effective date: "CMS also approved ICD-10 codes for AMKD, effective 10/1/2025" [Morgan Stanley p.5]. N07.B finds only patients already diagnosed. Z84.11 exists to record a family history, which is what cascade testing of relatives runs on.

---

## 7. Underdiagnosis

### How many people do not know

- CDC: "About 9 in 10 (87%) adults aged 20 or older with CKD did not know they have CKD," from *Chronic Kidney Disease in the United States, 2026* [30]. CDC also reports CKD in 22% of non-Hispanic Black adults against 13% of non-Hispanic white adults and 12% of Hispanic adults [30].
- Testing behavior explains part of it. Among 28.3 million at-risk US adults in a national laboratory database, 80.3% did not receive guideline-concordant assessment; testing reached 28.7% of patients with diabetes, 10.5% of patients with hypertension, and 41.4% of those with both; the national rate rose only from 10.7% in 2013 to 15.2% in 2018 [31].
- NKF's working group notes that about 10% or more of adult kidney disease is expected to have a genetic cause, and that "genetic testing in nephrology lags behind other medical fields" [27].

### Published data on APOL1 testing rates

No published rate of APOL1 test ordering in primary care turned up after two search approaches. Treat any specific "X% of PCPs order APOL1 tests" claim as **not found**. What exists:

- Nephrologists: 72% of 149 surveyed had ordered any genetic test, on average for 3.8% of their patients, and 49% tested fewer than 1% of patients. The survey reports no APOL1-specific ordering rate [35].
- Primary care providers: among 488 surveyed in New York City, 74% considered genetic testing clinically useful, but only 40% felt knowledgeable about the genetic basis of common diseases, 14% were confident interpreting results, and 25% felt ready to manage patients after testing; 53% worried about insurance discrimination [36].
- Two randomized trials show what happens when testing is delivered in primary care. In GUARDD (2,050 adults, 15 practices, results published 2022), systolic pressure fell 6 mm Hg at 3 months in the high-risk group against 3 mm Hg in controls (p = .01), and urine kidney testing rose 12 percentage points in the high-risk group against 7 in controls [33]. In GUARDD-US (6,754 enrolled across 14 institutions and 54 sites, published March 5, 2026), 954 participants (14.1%) had a high-risk genotype; the primary blood-pressure endpoint showed no difference overall (−0.3 mm Hg, 95% CI −2.7 to 2.1, p = 0.78), but urine albumin screening rose to 35.7% against 18.5% (difference 17.3 points, p < 0.001) and new CKD diagnoses rose to 8.9% against 3.2% (p = 0.002) [32].
- Where you find patients changes the yield enormously. In a 2026 community-and-EHR screening program, 764 people were genotyped: high-risk genotypes were 12% at community events but 46% from electronic health record queries and 58% from physician referral, and albuminuria at or above 300 mg/g was 1% at community events against 61% from EHR queries. The number needed to screen to enroll one trial participant was 3.7 for EHR queries and 657 for community events [34].

That last finding is the single most useful piece of published evidence for this case (inference): unselected outreach produces genotype-positive people without disease, while targeting people whose records already show kidney findings produces treatable patients roughly 170 times more efficiently.

### What the experts in the analyst reports say

Jefferies interviewed Dr. Peter Czarnecki, a nephrologist at Brigham and Women's Hospital and Harvard Medical School who directs a kidney genetics clinic (Jefferies PDF p.79):

| Topic | Figure | Quote as recorded |
|---|---|---|
| Share eventually diagnosed | About 75% | "~75% ultimately receive correct dx (timing heterogeneous)" |
| Poor courses from delay | 15–25% | "~15-25% have unfavorable courses partly driven by delay/misdirection, some progressing to ESRD pre-dx" |
| Time to diagnosis | 3–6 months ideal | "ideal pathway (~3-6 mo) vs real-world delays often spanning years, w/ irreversible damage accruing" |
| Visit length | About 15 minutes | "community time constraints (~15 min visits) make extra labs/screening a deterrent" |
| His own clinic's volume | About 25 new AMKD diagnoses per year | — |
| Adoption order | — | "academic centers to adopt first, w/ community uptake driven by education diffusion" |

Morgan Stanley states the demand-side fact in one line: "Majority of these patients are not diagnosed. VRTX offers free APOL1 genotyping" [Morgan Stanley p.5]. Jefferies assumes 30% of US AMKD patients are diagnosed today and 60% at "market maturity," with no supporting data beyond one-line source notes and no year attached to maturity [Jefferies PDF p.80]. Label both as assumptions if either appears on a slide.

### The reasons underdiagnosis persists

1. Early disease produces no symptoms, so nothing prompts a visit [37].
2. The urine albumin test is ordered far less often than the blood test, even in patients with diabetes or hypertension [31].
3. A 15-minute community visit leaves no room for extra labs or screening conversations [Jefferies PDF p.79].
4. Kidney failure in Black patients was attributed to hypertension for decades, so the diagnostic habit points away from a genetic cause [25; 7].
5. Physicians report low confidence in genetics: 14% confident interpreting results, 25% ready to manage patients afterward [36].
6. Until now, a positive genotype changed little, because no therapy targeted the disease [41]. The KDIGO criteria make "results could change management" a condition for testing [2], which is exactly the condition an inaxaplin approval would satisfy.
7. Referral and lab recognition lag. The Jefferies expert ties underdiagnosis to "delayed lab recognition and referral," and describes his clinic as functioning "largely as a 2nd-opinion referral hub, often w/o clear initial dx" [Jefferies PDF p.79].

---

## 8. What medical societies say

| Body | Position | Date | Source | Confidence |
|---|---|---|---|---|
| KDIGO Controversies Conference on APOL1 kidney disease | "At population levels, there is insufficient evidence to guide recommendations for APOL1 routine testing or screening." Box 1 sets conditions for clinical testing: informed consent; membership in a population with known or suspected high prevalence of risk variants (self-identified recent African ancestry, or a population with high genetic admixture); the person has kidney disease, or is a prospective living kidney donor, or has a relative with a high-risk genotype; CKD care and screening are available; results could change management; testing does not present unacceptable risk of harm as the person judges it; qualified counseling is available | Conference April 2024, Accra; published June 23, 2025 | [2] | High |
| KDIGO 2017 living-donor guideline | Recommendation 14.8: "Apolipoprotein L1 (APOL1) genotyping may be offered to donor candidates with sub-Saharan African ancestors. Donor candidates should be informed that having 2 APOL1 risk alleles increases the lifetime risk of kidney failure but that the precise kidney failure risk for an affected individual after donation cannot currently be quantified." | 2017 | [25] | High |
| KDIGO 2024 CKD guideline | Lists APOL1 in the genetic tests relevant to CKD diagnosis and lists high-prevalence APOL1 areas and APOL1-mediated kidney disease among CKD risk factors. Gives no APOL1-specific testing recommendation. States that "use of race in the computation of eGFR should be avoided" (practice point 1.2.4.2) | 2024 | [26] | High |
| National Kidney Foundation working group on genetic testing | Recommendation 16: "APOL1 should be included in gene panel assessments of chronic kidney disease and offered to patients having clinical manifestation or biopsy findings suspected to be related to APOL1 regardless of race and ethnicity" (81% consensus). Recommendation 17: "APOL1 genetic testing should not be limited or recommended by race or ethnicity of the patient" (78.6%). Recommendation 19: the medical community should be educated on the indication for APOL1 testing (98.8%). Recommendation 55: living donors related to patients with high-risk variants "should be considered for genetic testing" (93.2%). Recommendation 56 did not reach consensus: "There is currently not enough evidence to make firm recommendations for or against APOL1 testing to predict which donors would be at increased risk of CKD following kidney donation" (71.2%) | Published in AJKD 2024; announced Aug 8, 2024 | [27; 57] | High |
| National Kidney Foundation patient guidance | "Genetic testing can be considered for living kidney donor candidates depending on the individual situation." States two-variant carriers have "about a 15-20% chance of developing kidney disease in their lifetime" and that "There are no treatments specifically targeting AMKD" | Updated Feb 8, 2024 | [37] | Medium |
| American Society of Nephrology | **No standalone ASN position on APOL1 genetic testing found after two search approaches.** ASN co-sponsored the NKF–ASN task force on race in eGFR, and ASN journals published much of the underlying science. Say "no formal ASN position statement located" rather than implying one exists | — | Searches of ASN properties and the literature | Medium (absence of evidence) |
| American Society of Transplantation, 2017 statement | Recommends supporting NIH research "to learn more about the impacts of this gene on the African American population." Frames APOL1 as a research need, not a testing mandate | Approved by the AST Executive Committee April 4, 2017 | [50] | High |
| AST consensus meeting | Concluded that "the presence of APOL1 risk variants could not be used in isolation for determining the management of either living kidney donors or kidney transplant recipients," and that the information should inform education and shared decision-making | Meeting Dec 17–18, 2015; posted Feb 2016 | [51] | Medium |
| AST Living Donor Community of Practice expert panel | Interim recommendations: "All potential LKD candidates who self-report African ancestry (including AA, Afro-Caribbeans, and Hispanic/Latinx Blacks, Africans) should be informed about the APOL1 gene and risk of ESKD." Candidates with added risk factors "may be considered for testing" after counseling; testing should come after the preliminary medical and psychosocial evaluation, "preferably not during the initial screening"; the panel "supports shared decision making" when two variants are found | Published Oct 1, 2021 | [24] | High |
| British Transplantation Society | Recommends offering APOL1 genotyping to all potential donors of African heritage under 60 years old, as reported in the KDIGO conference paper. **The BTS page itself returned 403; cited here at one remove** | As cited in the 2025 KDIGO paper | [2] | Medium |

### The 2021 NKF–ASN task force on race in eGFR, and where APOL1 fit

The task force was charged with examining the inclusion of race in eGFR estimation [29]. Its final recommendations were: immediate adoption of "the CKD-EPI creatinine equation refit without the race variable in all laboratories" for US adults; national efforts to increase routine, timely use of cystatin C for confirmatory testing; and funding for research on new filtration markers and on interventions to eliminate disparities [28].

I checked both the interim report and the final report for APOL1. **Neither mentions APOL1 or apolipoprotein.** The interim report addresses the genetics question only at the level of ancestry: "Although race and genetic ancestry are related, race captures factors beyond genetic," "The relation between race, ancestry, and observed biology is poorly understood," and "Studies have not examined the relation of genetic ancestry to measured GFR. These studies are desired" [29].

So the accurate framing is the opposite of a common shortcut. APOL1 was not the task force's basis for removing race, and the task force did not propose APOL1 as a replacement variable. The connection between the two debates is thematic: both concern whether a racial category or a measurable biological variable belongs in a clinical algorithm. Where that substitution has been tested is in transplant allocation: replacing donor race with APOL1 genotype in the Kidney Donor Risk Index, across 622 deceased Black donors, produced comparable survival prediction and "substantially improves KDRI score for 85-90% of kidneys offered" [49]. Separately, OPTN approved a waiting-time modification in December 2022, in effect January 2023, for Black candidates disadvantaged by race-inclusive eGFR, where the race variable had been estimated to delay listing by 1.3 to 1.9 years [53].

---

## 9. Treatment today

**No approved therapy targets AMKD.** Vertex states it in the Sept 22, 2026 release [41], and NKF states it for patients: "There are no treatments specifically targeting AMKD" [37].

Standard CKD care applies, from the KDIGO 2024 guideline [26]:
- **ACE inhibitors or ARBs** (renin-angiotensin-system inhibitors), blood-pressure drugs that also lower urine protein: recommended for CKD with severely increased albuminuria without diabetes (1B), suggested for moderately increased albuminuria without diabetes (2C), recommended for moderate-to-severe albuminuria with diabetes (1B), and any combination of the two drug classes plus a direct renin inhibitor should be avoided (1B).
- **SGLT2 inhibitors**, originally diabetes drugs that protect kidneys: recommended for type 2 diabetes with CKD and eGFR 20 or above (1A), and for adults with CKD at eGFR 20 or above with UACR 200 mg/g or above, or heart failure at any albuminuria level (1A).
- **Blood-pressure target:** "a target systolic blood pressure (SBP) of <120 mm Hg, when tolerated, using standardized office BP measurement" (2B).

In the inaxaplin Phase 2a population, 50% were taking an ACE inhibitor and 44% an ARB at baseline [Morgan Stanley p.6], so background therapy is the comparator, not nothing.

**Immunosuppression in APOL1-associated FSGS.** Immunosuppressants are drugs that damp the immune system, used in many forms of FSGS. The evidence says genotype does not predict response:
- Kopp and colleagues found FSGS with two risk alleles had earlier onset and faster progression to ESKD but "similar sensitivity to steroids compared with other subjects" [5].
- In the FSGS Clinical Trial, 23 of 32 self-identified African American participants (72%) carried two risk alleles; there were "no differences in complete remission (CR) rate or CR plus partial remission (PR) rate" (p = 0.45), yet carriers had lower baseline eGFR, more proteinuria, and were more likely to progress to ESRD (p < 0.01) [60].
- Friedman and Pollak summarize: "there is no evidence that response to treatment with standard immunosuppression regimens differs between those with and without the APOL1 risk genotype" [6].

**Dialysis and transplant.** Section 5 covers what dialysis involves. On transplant and donor genotype:
- Deceased-donor kidneys with two APOL1 risk variants fail sooner: hazard ratio 2.26 (p = 0.001) across 675 kidneys, and 2.71 (p = 0.06) in the 221-transplant Alabama subset [22].
- The recipient's own APOL1 genotype has not been shown to affect graft survival [6].
- Among 136 Black living donors followed a median of 12 years, 2 of the 19 with two risk variants developed ESKD against 0 of 117 with zero or one variant; eGFR at follow-up was 57 ± 18 against 67 ± 15 mL/min/1.73 m² (p = 0.02) [23].
- Pollak and Friedman's practical read: "Kidneys from APOL1 high-risk donors fare worse than those with low-risk genotypes, but still seem preferable to dialysis" [6].

---

## 10. Inaxaplin and the pipeline, briefly

**How it works, in plain words.** The variant APOL1 protein opens an abnormal channel in kidney cell membranes. Inaxaplin blocks that channel function, so the podocyte stops leaking ions and the filter leaks less protein. Egbuna and colleagues showed that inaxaplin "selectively inhibited APOL1 channel function" in engineered human kidney cells and reduced proteinuria in a G2-homologous transgenic mouse before the human trial [9]. Oppenheimer describes the same mechanism as inhibiting "APOL1 protein-mediated induction of channel formation in podocytes" [Oppenheimer p.11]. It is an oral drug, and Vertex's AMKD expert notes that an oral, well-tolerated drug lowers the friction of treatment [Jefferies PDF p.79].

**Phase 2a (NEJM, March 1, 2023).** Single-group, open-label. Participants had two APOL1 variants, biopsy-confirmed FSGS, UPCR 0.7 to under 10, and eGFR 27 or above. Sixteen enrolled; 13 met the adherence threshold. Dosing ran 13 weeks: 15 mg daily for 2 weeks, then 45 mg daily for 11 weeks, on top of standard care. Mean UPCR change at week 13 was −47.6% (95% CI −60.0 to −31.3). Adverse events were mild or moderate and none caused discontinuation [9]. Morgan Stanley's safety table records 15 of 16 patients (94%) with any adverse event, 1 (6%) serious, and 4 (25%) with headache [Morgan Stanley p.8].

**AMPLITUDE Phase 2/3.** Adaptive, double-blind, placebo-controlled, 466 participants, ages 10 to 65, genotype G1/G1, G2/G2, or G1/G2, UPCR 0.7 to under 10 g/g, eGFR 25 to under 75 mL/min/1.73 m². It excludes transplant recipients, uncontrolled hypertension, any history of diabetes, and other known causes of kidney disease. Primary outcomes are percent change in UPCR at week 48 and eGFR slope at the interim analysis, with eGFR slope at final analysis over at least 2 years. Registry primary completion is June 2, 2028; the record was updated Sept 17, 2026 [43]. Enrollment is complete and the interim analysis is expected in early 2027 [41].

**The approval bar.** On the Aug 3, 2026 earnings call the CEO said: "The agency has provided and we have an agreement with the agency for a potential accelerated approval based on the primary endpoint at the time of the IA, which is 1 year GFR" [42]. Morgan Stanley records the same emphasis from Vertex: "Per VRTX, eGFR (not UPCR) data is FDA's focus of the Ph2/3 interim analysis" [Morgan Stanley p.12]. The eGFR requirement is the main approval risk, because kidney-function separation takes longer to appear than protein reduction, and Jefferies' expert expects eGFR to lag proteinuria "w/ uncertain timing" [Jefferies PDF p.79].

**AMPLIFIED results, Sept 22, 2026.** Forty-one people were enrolled and dosed for 13 weeks in two cohorts that do not overlap AMPLITUDE's population [41; Morgan Stanley p.1]:

| Cohort | Definition | Enrolled / analyzed | UACR change | Read |
|---|---|---|---|---|
| Modest proteinuria | UACR 0.1 to under 0.42 g/g | 23 / 22 | −42.7% (95% CI −58.3% to −21.1%) | Positive; the interval excludes no effect |
| Type 2 diabetes with proteinuria | UACR 0.1 to under 6 g/g | 18 / 17 | −17.3% (95% CI −36.3% to +7.2%) | The interval includes no effect |

Safety: no serious adverse events related to inaxaplin, all adverse events mild or moderate, headache most common at 7.3%, and five participants had asymptomatic transaminase elevations that resolved [41]. Vertex had said before the readout that the biology of AMKD with type 2 diabetes "is less clear" [Morgan Stanley p.1], and the diabetes result is consistent with that caution.

**Competitors, in one paragraph** (another file covers them in depth). Maze's MZE829 reported a 35.6% mean proteinuria reduction in 12 evaluable patients at 12 weeks in March 2026, expects updated Phase 2 data in late 2026 or early 2027, and plans a pivotal trial in the first half of 2027 subject to regulatory feedback [52]. AstraZeneca's AZD2373, an antisense drug, is in a 96-patient Phase 2b with an August 2027 primary completion date, and Lilly collaborates on an exploratory Phase 2 of baricitinib; Vertex's own VX-840 has completed Phase 1 [Jefferies PDF p.72, p.78]. See `notes\vertex-timeline-2026-2028.md` for every dated milestone and its source.

---

## 11. Equity, trust, and privacy

### GINA and its gaps

The Genetic Information Nondiscrimination Act of 2008 bars health insurers from using genetic information to decide eligibility, coverage, underwriting, or premiums, and bars employers from using it in hiring, firing, promotion, pay, and job assignment, and from requesting or requiring genetic tests [45].

The gaps matter to a patient deciding whether to be tested [45]:
- It does not cover life insurance, disability insurance, or long-term care insurance.
- It does not apply to employers with fewer than 15 employees.
- Standard employment protections do not apply to US military personnel.
- State laws may add protections, and the Affordable Care Act separately bars coverage denial for pre-existing conditions.

The AST panel treats genetic-discrimination protections as a required counseling topic for donor candidates [24], and the KDIGO criteria require that testing "does not present an unacceptable risk of harm as determined by the individual" [2]. Any campaign that asks people to get genotyped should state the GINA limits plainly rather than promise blanket protection.

### Documented mistrust and its history

- The US Public Health Service study at Tuskegee ran from 1932 to 1972, enrolling 399 men with late-latent syphilis and 201 men without it. Participants were not offered available treatment even after penicillin became widely available, and community members "thought it was a special government health care program." The study ended in 1972 after an advisory panel recommendation [47].
- Sickle cell trait screening offers the closer analogy, because it was also a genetic test aimed at one ancestry group. After the National Sickle Cell Anemia Control Act was signed in 1972, "Many blacks felt forced to undergo testing and experienced employment, health insurance, and marriage discrimination," and people "were often not informed or were incompletely educated about their SCT carrier status, resulting in confusion about health risks and mistrust of the underlying intentions for screening" [48].
- The KDIGO conference names the specific present-day risk: "APOL1 testing has the potential to reinforce racialized medicine given the historical and ongoing conflation between race, ethnicity, and ancestry" [2].
- Analysts build mistrust-adjacent assumptions into their models without measuring them. Jefferies keeps "conservative penetration given the lower socio-economic status of these pts" [Jefferies PDF p.4, p.14]. That is an assumption, not a finding, and the team can say so.

Evidence also runs the other way, and the team should carry it into Q&A. In GUARDD-US, 95.9% of participants (821 of 856) found the APOL1 information sufficient, 92.1% found it easy to understand, 94.1% would be tested again, and 0.7% of those with a high-risk genotype expressed distress [32]. In GUARDD, 97% would accept testing again, while 8% of high-risk participants worried they would develop kidney problems against 1% of low-risk participants [33]. In the 2026 community screening program, 789 of 1,052 people approached (75%) consented and only 4% refused, with church leaders volunteering first to encourage their congregations [34]. The record says people accept this test when it is offered with counseling and respect.

### How to talk about race, ancestry, and genetics on slides and in the room

1. **Write "recent African ancestry," not a racial category, when describing who carries the variants.** KDIGO states that "consistent use of clear terminology is very important to prevent conflation among race, ethnicity, ancestry, and APOL1 genotype," and uses "recent African ancestry" and "self-identified recent African ancestry" [2].
2. **Do not make race the test criterion.** NKF's recommendation 17 says APOL1 testing "should not be limited or recommended by race or ethnicity of the patient," and recommendation 16 offers testing to patients whose clinical or biopsy findings suggest APOL1 involvement "regardless of race and ethnicity" [27].
3. **Follow the National Academies framing.** Its 2023 report, *Using Population Descriptors in Genetics and Genomics Research: A New Framework for an Evolving Field*, asks researchers to "rethink and justify how and why race, ethnicity and ancestry labels are used," and notes that race "should not be used for analysis in most genomics studies" [46].
4. **Name the mechanism, not the group.** "Two APOL1 variants cause the disease" is accurate; "a Black disease" is not, since about 80–85% of two-variant carriers never develop kidney disease [2; 37].
5. **Say what the campaign asks of people.** A test that names a lifetime risk carries privacy and insurance consequences outside health coverage [45]. Presenting those limits is part of an honest patient-facing plan, and a nephrologist CEO who chairs work on kidney health equity will notice if they are missing.
6. **Do not present APOL1 as the reason race left the eGFR equation.** Neither NKF–ASN task force report mentions APOL1 [28; 29].

---

## 12. Ten facts every teammate should be able to state in judge Q&A

1. AMKD requires two high-risk APOL1 variants, and about 13% of African Americans, roughly 6 million people, carry two [1; Morgan Stanley p.5].
2. Between 15% and 20% of two-variant carriers develop kidney disease, so a positive genotype alone is not a diagnosis; KDIGO puts kidney failure at about 15% and Vertex's models use 20% [2; 1; Morgan Stanley p.5].
3. AMKD patients lose 6.55 mL/min/1.73 m² of eGFR per year against 3.63 for African Americans with CKD and no risk variants, and reach dialysis about 9 to 12 years earlier [Morgan Stanley p.4; Jefferies PDF p.72].
4. Vertex's population figures are 150,000 for primary AMKD plus 100,000 for the AMPLIFIED populations, and both cover the US and Europe together, not the US alone [Morgan Stanley p.1, p.5; Vertex release, Sept 22, 2026].
5. A US lifetime figure of about 1.2 million comes from 6 million carriers multiplied by 20%, and it cannot be compared with the 250,000 current US-plus-Europe figure [Morgan Stanley p.5; Jefferies PDF p.80].
6. CDC reports that 87% of US adults with CKD do not know they have it, and only 21.0% of at-risk adults get the urine albumin test that would find it [30; 31].
7. AMKD has had its own diagnosis codes since Oct 1, 2025: N07.B for the disease and Z84.11 for family history, which is the code cascade testing of relatives runs on [40; Morgan Stanley p.5].
8. Inaxaplin cut urine protein 47.6% at 13 weeks in the Phase 2a trial (95% CI −60.0 to −31.3, 13 adherent patients), and on Sept 22, 2026 the AMPLIFIED modest-proteinuria cohort fell 42.7% while the type 2 diabetes cohort's 17.3% reduction had a confidence interval that includes no effect [9; 41].
9. Accelerated approval rests on kidney function, not protein: the CEO said on Aug 3, 2026 that the FDA agreement covers accelerated approval "based on the primary endpoint at the time of the IA, which is 1 year GFR," with the interim analysis due early 2027 [42; 41].
10. Where you look changes what you find: in a 2026 screening program, electronic health record queries produced high-risk genotypes in 46% of those genotyped and albuminuria at or above 300 mg/g in 61%, against 12% and 1% at community events, with 3.7 versus 657 people needing screening per trial enrollment [34].

---

## 13. Sources

1. Srinivasan V, So PN, Kwakyi EPK, Lerma EV, Wiegley N. "APOL1 Mediated Kidney Disease: A Review and Look Toward the Future." *Kidney Medicine* 7(9):101062. Published July 3, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12361766/
2. Ojo AO, Adu D, Bramham K, et al. "APOL1 kidney disease: conclusions from a Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference." *Kidney International* 108(5):763–779. Conference April 2024, Accra, Ghana; published June 23, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC13266834/
3. Genovese G, Friedman DJ, Ross MD, et al. "Association of trypanolytic ApoL1 variants with kidney disease in African Americans." *Science* 329(5993):841–845. Aug 1, 2010. https://europepmc.org/article/MED/20647424
4. Cooper A, Ilboudo H, Alibu VP, et al. "APOL1 renal risk variants have contrasting resistance and susceptibility associations with African trypanosomiasis." *eLife*. May 24, 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5495568/
5. Kopp JB, Nelson GW, Sampath K, et al. "APOL1 genetic variants in focal segmental glomerulosclerosis and HIV-associated nephropathy." *JASN* 22(11):2129–2137. Nov 1, 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3231787/
6. Friedman DJ, Pollak MR. "APOL1 Nephropathy: From Genetics to Clinical Applications." *CJASN*. Published July 2, 2020; issue Feb 8, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7863644/
7. Parsa A, Kao WH, Xie D, et al. "APOL1 Risk Variants, Race, and Progression of Chronic Kidney Disease." *NEJM*. Nov 9, 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3969022/
8. Kanji Z, Powe CE, Wenger JB, et al. "Genetic variation in APOL1 associates with younger age at hemodialysis initiation." *JASN* 22(11):2091–2097. Nov 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3231784/
9. Egbuna O, Zimmerman B, Manos G, et al. "Inaxaplin for Proteinuric Kidney Disease in Persons with Two APOL1 Variants." *NEJM* 388(11):969–979. March 1, 2023. https://pubmed.ncbi.nlm.nih.gov/36920755/
10. Gbadegesin RA, Ulasi I, Ajayi S, et al. (H3Africa Kidney Disease Research Network). "APOL1 Bi- and Monoallelic Variants and Chronic Kidney Disease in West Africans." *NEJM* 392(3):228–238. Print Oct 26, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11735277/
11. Martinelli E, Westland R, Olabisi OA, Sanna-Cherchi S. "Prevalence and Impact of APOL1 Kidney Risk Variants in West Africa." *JASN* 36(3). Published Nov 27, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11888956/
12. Kramer HJ, Stilp AM, Laurie CC, et al. "African Ancestry–Specific Alleles and Kidney Disease Risk in Hispanics/Latinos." *JASN* 28(3):915–922. Sept 20, 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC5328161/
13. Limou S, Nelson GW, Kopp JB, Winkler CA. "APOL1 kidney risk alleles: population genetics and disease associations." *Advances in Chronic Kidney Disease*. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4157456/
14. Reidy KJ, Hjorten R, Parekh RS. "Genetic risk of APOL1 and kidney disease in children and young adults of African ancestry." *Current Opinion in Pediatrics* 30(2):252–259. April 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6002812/
15. *(Reserved. The AJKD review "APOL1-Associated Nephropathy: A Key Contributor to Racial Disparities in CKD," Freedman et al. 2018, PMC6200346, was identified but not read; its figures are not used here.)*
16. Wu H, Larsen CP, Hernandez-Arroyo CF, et al. "AKI and Collapsing Glomerulopathy Associated with COVID-19 and APOL1 High-Risk Genotype." *JASN*. June 19, 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7460910/
17. Gupta Y, Friedman DJ, McNulty MT, et al. "Strong protective effect of the APOL1 p.N264K variant against G2-associated focal segmental glomerulosclerosis and kidney disease." *Nature Communications* 14:7836. Nov 30, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10689833/
18. Ma L, Shelness GS, Snipes JA, et al. "Localization of APOL1 protein and mRNA in the human kidney." *JASN* 26(2):339–348. Feb 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4310650/
19. Shukha K, Mueller JL, Chung RT, et al. "Most ApoL1 Is Secreted by the Liver." *JASN* 28(4):1079. April 2017. https://pubmed.ncbi.nlm.nih.gov/27932478/
20. Bruggeman LA, O'Toole JF, Ross MD, et al. "Plasma Apolipoprotein L1 Levels Do Not Correlate with CKD." *JASN* 25(3):634–644. March 2014. https://pubmed.ncbi.nlm.nih.gov/24231663/
21. Dorr CR, Reule SA, Murugan R, et al. "Deceased-Donor Apolipoprotein L1 Renal-Risk Variants Have Minimal Effects on Liver Transplant Outcomes." *PLoS One*. April 7, 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4824450/
22. Freedman BI, Julian BA, Pastan SO, et al. "Apolipoprotein L1 gene variants in deceased organ donors are associated with renal allograft failure." *American Journal of Transplantation*. 2015. https://pubmed.ncbi.nlm.nih.gov/25809272/
23. Doshi MD, Ortigosa-Goggins M, Garg AX, et al. "APOL1 Genotype and Renal Function of Black Living Donors." *JASN*. Jan 16, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5875947/
24. Doshi MD, Gordon EJ, Freedman BI, Glover C, Locke JE, Thomas CP. "Integrating APOL1 Kidney-risk Variant Testing in Live Kidney Donor Evaluation: An Expert Panel Opinion." *Transplantation* 105(10):2132–2134. Oct 1, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8994118/
25. KDIGO. *Clinical Practice Guideline on the Evaluation and Care of Living Kidney Donors*, recommendation 14.8 and chapter 14 rationale. 2017. https://kdigo.org/wp-content/uploads/2017/07/2017-KDIGO-LD-GL.pdf
26. KDIGO. *2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease*. *Kidney International* 105(4S):S117–S314. 2024. https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf
27. Franceschini N, Feldman DL, Berg JS, et al. "Advancing Genetic Testing in Kidney Diseases: Report From a National Kidney Foundation Working Group." *AJKD* 84(6):751–766. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11585423/
28. Delgado C, Baweja M, Crews DC, et al. "A Unifying Approach for GFR Estimation: Recommendations of the NKF-ASN Task Force on Reassessing the Inclusion of Race in Diagnosing Kidney Disease." *JASN*. Sept 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8638402/
29. Delgado C, Baweja M, Burrows NR, et al. "Reassessing the Inclusion of Race in Diagnosing Kidney Diseases: An Interim Report From the NKF-ASN Task Force." April 9, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8238889/
30. CDC. Chronic Kidney Disease Data and Research, citing *Chronic Kidney Disease in the United States, 2026*. Page dated March 31, 2026. https://www.cdc.gov/kidney-disease/php/data-research/index.html
31. Alfego D, Ennis J, Gillespie B, et al. "Chronic Kidney Disease Testing Among At-Risk Adults in the U.S. Remains Low: Real-World Evidence From a National Laboratory Database." *Diabetes Care*. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8740927/
32. Eadon MT, Cavanaugh KL, She L, et al. "Genetic Testing for APOL1 in Adults With Hypertension: The GUARDD-US Randomized Clinical Trial." *JAMA Network Open*. March 5, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12964156/
33. Nadkarni GN, Fei K, Ramos MA, et al. "Effects of Testing and Disclosing Ancestry-Specific Genetic Risk for Kidney Failure on Patients and Health Care Professionals." *JAMA Network Open*. March 4, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8897752/
34. Barrett N, Odera JO, Bethea K, et al. "Hybrid Community-Electronic Health Record Approaches to Apolipoprotein L1 Kidney Disease Screening and Clinical Trials among Black Individuals." *JASN*. March 3, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13406261/
35. Mrug M, Bloom MS, Seto C, et al. "Genetic Testing for Chronic Kidney Diseases: Clinical Utility and Barriers Perceived by Nephrologists." *Kidney Medicine* 3(6). Oct 5, 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8664736/
36. Hauser D, Obeng AO, Fei K, Ramos MA, Horowitz CR. "Views Of Primary Care Providers On Testing Patients For Genetic Risks For Common Chronic Diseases." *Health Affairs*. May 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6503526/
37. National Kidney Foundation. "APOL1-Mediated Kidney Disease (AMKD)." Patient page, last updated Feb 8, 2024. https://www.kidney.org/kidney-topics/apol1-mediated-kidney-disease-amkd
38. NIDDK. "Kidney Disease Statistics for the United States." Last reviewed Sept 2024, citing the USRDS 2023 Annual Data Report. https://www.niddk.nih.gov/health-information/health-statistics/kidney-disease
39. NIDDK. "Hemodialysis." Last reviewed January 2018. https://www.niddk.nih.gov/health-information/kidney-disease/kidney-failure/hemodialysis
40. CDC/NCHS. FY2026 ICD-10-CM code descriptions and addenda files (`icd10cm-codes-2026.txt`, `icd10cm-codes-addenda-2026.txt`), posted June 2025; FY2026 codes effective Oct 1, 2025. https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2026/
41. Vertex Pharmaceuticals. "Vertex Announces Positive Results From Phase 2b AMPLIFIED Study of Inaxaplin…" Boston, Business Wire, Sept 22, 2026. https://www.biospace.com/press-releases/vertex-announces-positive-results-from-phase-2b-amplified-study-of-inaxaplin-in-additional-populations-of-people-with-apol1-mediated-kidney-disease-amkd-and-completion-of-enrollment-in-the-phase-2-3-amplitude-trial
42. Vertex Pharmaceuticals Q2 2026 earnings call transcript, Aug 3, 2026. https://www.fool.com/earnings/call-transcripts/2026/08/10/vertex-vrtx-q2-2026-earnings-call-transcript/
43. ClinicalTrials.gov. NCT05312879, AMPLITUDE Phase 2/3 study of VX-147 (inaxaplin). Record last updated Sept 17, 2026. https://clinicaltrials.gov/study/NCT05312879
44. Arkana Laboratories. "APOL1 Genotyping Assay" and the No Cost to Patient APOL1 Genotyping Program sponsored by Vertex. Accessed Sept 27, 2026. https://www.arkanalabs.com/apol1/
45. National Human Genome Research Institute. "Genetic Discrimination" (GINA). Page dated Jan 6, 2022. https://www.genome.gov/about-genomics/policy-issues/Genetic-Discrimination
46. National Academies of Sciences, Engineering, and Medicine. *Using Population Descriptors in Genetics and Genomics Research: A New Framework for an Evolving Field*. 2023. https://www.nationalacademies.org/publications/26902
47. CDC. "The Untreated Syphilis Study at Tuskegee." Page dated Sept 4, 2024. https://www.cdc.gov/tuskegee/about/index.html
48. Naik RP, Haywood C. "Sickle cell trait diagnosis: clinical and social implications." *Hematology ASH Education Program*. Dec 5, 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4697437/
49. Julian BA, Gaston RS, Brown WM, et al. "Effect of Replacing Race With Apolipoprotein L1 Genotype in Calculation of Kidney Donor Risk Index." *American Journal of Transplantation* 17(6):1540–1548. June 2017. https://pubmed.ncbi.nlm.nih.gov/27862962/
50. American Society of Transplantation. "Research on the Apolipoprotein L1 (APOL1) Gene and Its Impact on African Americans." Approved by the AST Executive Committee April 4, 2017. https://www.myast.org/research-on-the-apolipoprotein-l1-apol1-gene-and-its-impact-on-african-americans
51. American Society of Transplantation. "Partnering to Address a Critical Issue in Transplantation: APOL1." Posted Feb 15, 2016, on the Dec 17–18, 2015 consensus meeting. https://www.myast.org/blog/partnering-to-address-a-critical-issue-in-transplantation-apol1
52. Maze Therapeutics. "Maze Therapeutics Reports Second Quarter 2026 Financial Results and Recent Highlights." Aug 11, 2026. https://www.globenewswire.com/news-release/2026/08/11/3343141/0/en/maze-therapeutics-reports-second-quarter-2026-financial-results-and-recent-highlights.html
53. Pavlakis M. "A Restorative Justice Project in Kidney Allocation." *JASN*. July 25, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10561813/
54. Internal extraction files, competition-licensed and not to be shared: `work\research\analyst_morgan_stanley.md` (Morgan Stanley, Apr 19, 2026), `work\research\analyst_jefferies.md` (Jefferies, Mar 10, 2026), `work\research\analyst_oppenheimer.md` (Oppenheimer, Feb 13, 2026), `work\research\analyst_consensus.md`.
55. Shah S, et al., retrospective dialysis and transplant outcomes in AMKD versus matched CKD, presented at ASN 2025, as reported in Oppenheimer p.10 (645 patients per group).
56. National Kidney Foundation and NephCure. Externally Led Patient-Focused Drug Development meeting on APOL1 kidney disease, Nov 6, 2026, Hyattsville, MD. https://www.kidney.org/externally-led-patient-focused-drug-development-el-pfdd-meeting-apol1-kidney-disease
57. National Kidney Foundation. "National Kidney Foundation Unveils Recommendations for Genetic Testing in Kidney Disease." Press release, Aug 8, 2024. https://www.kidney.org/press-room/national-kidney-foundation-unveils-recommendations-genetic-testing-kidney-disease
58. Ensembl REST API, variant rs73885319 (APOL1 G1 missense variant), 1000 Genomes phase 3 population allele frequencies, including the African-Caribbean-in-Barbados sample at 26.0%. Accessed Sept 27, 2026. https://rest.ensembl.org/variation/human/rs73885319?pops=1;content-type=application/json
59. Hjorten R, et al. "APOL1 Nephropathy Risk Variants Through the Life Course: A Review." *AJKD*. 2024. https://www.ajkd.org/article/S0272-6386(24)00597-3/fulltext
60. Kopp JB, Winkler CA, Zhao X, et al. "Clinical Features and Histology of Apolipoprotein L1-Associated Nephropathy in the FSGS Clinical Trial." *JASN*. Published Jan 8, 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4446865/

---

## Open items for a teammate with a browser

1. **The three testing-program pages.** Record the eligibility text verbatim from the Labcorp, Natera, and Arkana APOL1 program pages. Four fetch attempts failed here. The rule that decides whether a primary care physician can order a free test for an undiagnosed patient is the single most important unverified fact in this file.
2. **Per-patient dialysis and transplant costs.** Pull the USRDS Annual Data Report expenditures chapter for per-person-per-year Medicare spending.
3. **An ASN position on APOL1 testing.** I found none after two approaches. If a teammate finds one, add it to section 8 with its date.
4. **The 70% attributable-risk figure.** Trace it to a primary source or keep attributing it to the 2018 review [14].
