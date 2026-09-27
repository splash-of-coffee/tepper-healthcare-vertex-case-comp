# Financial Model Specification (draft for Phase 3)

Written Sept 27, 2026 by the engagement lead. The Phase 3 builder (mba_finance) follows this file together with Phase 3 of `prompts/agent-prompt-v4.md`. Values come from `work/model/assumptions_register.xlsx`; this file fixes the structure only. Nothing here is a result.

## 1. Purpose and the one rule that matters most

The model measures what each of the eight combinations adds above the baseline, in patients and in dollars. The baseline is the nephrology sales force plus Vertex's current unbranded programs at today's scale. The model never credits a combination with inaxaplin's total revenue.

## 2. Build approach

- **A Python engine and a matching workbook.** The builder writes the logic once in Python (`work/model/engine.py`), then writes the Excel workbook with live formulas that follow the same logic (`work/model/build_workbook.py` → `amkd_primary_care_model.xlsx`). After Excel recalculates through COM, a check script compares every NPV in Excel with the Python engine; they must match within 0.5%.
- **Why both forms.** The Excel file is what teammates and judges can read. The Python engine runs the headcount and budget response curves, the tornado chart, and the optional Monte Carlo without thousands of Excel recalculations.
- **Recalculate before reading.** openpyxl writes formulas but does not calculate them. Every read of an output follows an Excel COM recalculation and save.

## 3. Time axis

Annual columns from 2026 (first possible spend, Q4 2026 counted as a full year at the stated amount) to 2040. The base case assumes US accelerated approval with launch in a register-set year (the register holds the base year and its range; the analyst range runs from 2027 to early 2028). The full-approval path shifts launch by the register's delay (base 1.5 years, rounded to whole years in the annual model). Mid-year discounting.

## 4. Patient engine (per setting, per year)

Two settings: patients managed by nephrology, and patients managed only in primary care. Each setting runs the same stock-and-flow logic. All counts are US label-eligible patients (two APOL1 variants, no diabetes, proteinuria at the trial threshold, eGFR at or above the trial floor).

| Row | Definition |
|---|---|
| Undiagnosed eligible, start of year (U) | Prior year U − diagnosed − exits + new eligible patients |
| Diagnosed this year (D) | U × diagnosis hazard for that setting, year, and combination |
| Exits (X) | U × exit hazard (eGFR falls below the floor, kidney failure, or death). The exit hazard comes from the eGFR decline rate and the eGFR distribution; register row, not typed. |
| Diagnosed, waiting for launch | Before launch, D accumulates here and loses the exit hazard each year |
| Referred and worked up | D × referral completion (primary care only) × nephrology visit completed × biopsy or workup completed × meets label × prior authorization approved |
| Started | Worked-up patients who start, with the lag in the register |
| On therapy (T) | Prior T × persistence × (1 − death and kidney-failure rate) + started |
| Treated patient-years | Average of start and end T for the year |

**Diagnosis hazard.** Baseline hazards by setting and year come from the register (rising after launch as the nephrology force and medical education work). A combination adds to the primary care hazard only:
- Sales (1a, 1b, 1c): added hazard = coverage share × lift per covered patient. The coverage share is the share of primary-care-only eligible patients whose clinician sits on a rep's target list. It comes from a concentration curve: physicians ranked by expected eligible patients, so the first reps cover the densest deciles. Headcount sets how far down the curve coverage reaches (targets per rep in the register). Hired reps ramp over the register's months; contracted reps ramp faster.
- Advertising (2): added hazard = maximum lift × (1 − exp(−spend ÷ scale)), which gives each added dollar less effect than the one before. Both parameters sit in the register and are calibrated to analog campaigns (WS-D, WS-I).
- Combined (1x + 2): the advertising lift is multiplied by (1 + interaction × coverage share). The interaction term is an explicit assumption with a range, and a check row confirms no patient is counted twice: the combined hazard can never exceed the register's ceiling.

**Patients found earlier versus patients found only because of the spend.** Because each patient either is diagnosed or exits, a higher hazard finds some patients earlier and some who would never have been found while still eligible. The model reports both:
- added diagnosed patients who would never have been diagnosed while eligible = (combination's cumulative diagnoses) − (baseline's cumulative diagnoses), by cohort;
- the rest of the added treated patient-years come from earlier diagnosis.
A check reconciles the two parts to the total added treated patient-years.

**Testing.** Tests ordered = diagnosed ÷ the share of tested patients who carry two variants and meet the label (register rows by setting). Added tests above baseline = the "genetic testing uplift" the case asks for, reported per year. Every added test costs Vertex the sponsored-test price, because the free programs pay for it.

## 5. Revenue

Revenue = treated patient-years × net price × compliance. Net price is set by payer channel (commercial, Medicare, Medicaid, 340B). Primary-care-found patients carry their own channel mix (more Medicaid and 340B through community health centers), so their blended net price differs from the nephrology-found mix. Medicare negotiation, if it applies, cuts the Medicare net price from its register year; the orphan-exclusion upside is a scenario switch, not the base case. Competitor entry cuts new starts by the register's share-loss from its entry year; patients already on therapy stay.

## 6. Costs by option

| Option | Cost lines |
|---|---|
| 1a hired team | Reps × fully loaded cost; first-line managers at the register ratio; recruiting and training per hire; ramp months at partial productivity; exit cost per rep if a stage gate stops the team |
| 1b contracted team | Reps × contract rate; Vertex oversight staff; start-up fee; termination fee if stopped |
| 1c retargeting | Displaced nephrology calls × value per call; value per call = lost povetacicept and inaxaplin nephrology starts per call × net revenue per start, net price to net price, by year as povetacicept's launch matures; plus added travel cost for primary care calls |
| 2 advertising | Added media by year; creative and agency fees; measurement; added sponsored tests and genetic counseling |
| Design elements | EHR prompts, lab-report prompts, cascade testing, and the referral design, each costed inside the option that carries it |

## 7. Cash flow and valuation

- Added contribution = added revenue × contribution margin (after cost of goods, royalties if any, and patient-support costs).
- Added after-tax cash flow = (added contribution − added costs) × (1 − tax rate).
- **NPV conditional on approval** (accelerated approval, base launch year).
- **Risk-adjusted NPV** = probability-weighted sum over three paths: accelerated approval, full approval about 2029, and failure. Spending that happens before the path is known is counted in every path; spending that the plan would stop is counted only until the stop.
- **Staged versus committed.** The recommended combination runs twice: committed (full spend from the start) and staged (scale-up only after the triggers). The NPV difference is the value of waiting for information.
- **Metrics.** ROI = (present value of added contribution after tax − present value of added costs after tax) ÷ present value of added costs after tax. Simple payback = first year cumulative undiscounted added cash flow turns positive, counted from the first spend. Discounted payback uses discounted cash flow. IRR where cash flows change sign once. Breakeven = added treated patients needed for NPV = 0. The Definitions sheet states each metric and the discount rate, and the deck uses the same definitions.

## 8. Sheets

1. `README` — purpose, structure, how to recalculate, version.
2. `Inputs` — every register value by ID, with low, base, and high, and a scenario selector. No typed numbers anywhere else.
3. `Baseline` and one sheet per combination (`1a`, `1b`, `1c`, `2`, `1a+2`, `1b+2`, `1c+2`) — identical row structure, generated by script.
4. `Staged_vs_Committed` — the recommended combination both ways.
5. `Summary` — outputs for each combination, both valuations, all metrics.
6. `Definitions` — metric definitions, discount rate and its justification, tax rate, horizon.
7. `Checks` — no funnel stage exceeds the stage before it; the found-earlier and found-only parts reconcile to the total; totals match across sheets; units are consistent; every combination's costs are zero in years it does not spend.

## 9. What the optimizer runs on the Python engine (after the audit)

- Headcount response curve in steps of 10 reps; advertising budget curve in steps of $5M; the chosen level is where the last step's added NPV reaches zero or a stated budget cap binds.
- Tornado chart of the eight or so drivers that move NPV most, each between its low and high values.
- Breakeven values for the drivers on the sensitivity slide.
- Driver-based scenarios bounded by the analyst figures in `work/research/analyst_consensus.md`.
