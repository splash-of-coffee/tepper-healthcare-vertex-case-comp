# Decision Log — Tepper Healthcare Case Competition (Vertex / inaxaplin / AMKD)

Each entry records a decision or a hypothesis change, the date and time (Eastern), and the reason. Entries are added in time order and never deleted. A reversed decision gets a new entry that names the entry it replaces.

---

## D-001 — Run started on agent prompt v4 with three placeholders unfilled
**When:** Sun Sept 27, 2026, 11:51 AM Eastern.
**Decision:** The agent started Phase 0 from `prompts/agent-prompt-v4.md` as written. Chris started the run in a fresh session.
**Placeholder handling:**
- The start-date placeholder is set to Sun Sept 27, 2026, 11:51 AM Eastern. The calendar in the prompt already assumes a Sept 27–28 start, so no dates move.
- The team-strengths placeholder stays open. The Gate A package asks the team to fill it, as the prompt directs. Until then, model modules and judge questions carry no owner.
- The office-hours placeholder stays open. No notes from the Sept 22 session exist in the project folder. The Gate A package asks whether anyone attended.
**Reason:** None of the three placeholders blocks Phase 0 or Phase 1. The prompt routes the strengths request through Gate A.

## D-002 — Central question
**When:** Sept 27, 2026, 11:55 AM Eastern.
**Decision:** The central question for the engagement is: "Which of the eight allowed combinations of primary care sales and added direct-to-patient advertising should Vertex fund, at what headcount, budget, and timing, to add the most risk-adjusted value by getting more US label-eligible AMKD patients in primary care tested, referred, and treated with inaxaplin?"
**Reason:** The case asks two questions, the primary care strategy and its financial evaluation. One question that names the choice set, the sizing, the timing, and the value measure covers both. "US label-eligible" keeps the sizing on the patients a first label would cover (the second analytical trap in the prompt).

## D-003 — First hypothesis (H1)
**When:** Sept 27, 2026, 11:55 AM Eastern.
**Hypothesis:** Vertex should contract a supplemental primary care sales force (Option 1b) and add direct-to-patient testing advertising above the current Power Forward level (Option 2). Spending scales up in stages tied to the AMPLITUDE interim analysis (early 2027) and to approval.
**Reasons expected to hold, each with the evidence that would disprove it:**
1. **A contracted force matches the approval risk.** Analysts put inaxaplin's probability of success at 50–70%, and a contract force can start faster and shrink if the interim analysis or approval fails. *Disproof:* the response curve gives the hired force (Option 1a) a higher risk-adjusted NPV after ramp time and exit costs are counted, or contract start-up is within 2 months of the time to hire a full-time team.
2. **Retargeting the nephrology reps (Option 1c) costs more than its cash cost.** Displaced nephrology calls in 2027–2028 fall in povetacicept's first launch years, and one lost povetacicept patient is worth about 2.2–2.9 inaxaplin patients on net price (the ratio comes from list and modeled net prices in the sponsor reports and still needs checking). The same reps must also carry inaxaplin to the nephrologists who prescribe it. *Disproof:* the displaced calls come from low-potential nephrologists, so the retargeting cost per added treated patient is below the contracted force's cost per added treated patient.
3. **Advertising and sales calls raise testing more together than apart.** A patient prompted by an advertisement still needs a primary care physician (PCP) who orders the free APOL1 test and refers to nephrology. *Disproof:* adding Option 2 to Option 1b gives zero or negative added NPV at the first $5M budget step, or analog campaigns show a cost per added confirmed diagnosis above the value of an added treated patient.
**Reason for this starting point:** The value of primary care work sits in testing and referral, which the free-testing programs already pay for and which unbranded messages can support before approval. The approval risk argues for commitments that can be reversed. This is a starting hypothesis only. The model decides the recommendation, and any change is logged here with its reason.

## D-004 — Corrections to the prompt's fact seed from the analyst extractions
**When:** Sept 27, 2026, 12:25 PM Eastern.
**Decision:** The model and deck use the corrected figures below. Each comes from the extraction files in `work/research/`, which cite PDF pages; an independent check of the load-bearing figures against the PDFs runs before any of them reaches a slide.
1. **RBC's 2035 figure.** RBC's 2035 risk-adjusted inaxaplin sales are $1,355.8M worldwide and $1,070.5M US (RBC p.7). The "~$3.3B WW out-year opportunity" (RBC p.5) has no stated basis, so it is not a scenario bound. The 2035 risk-adjusted range across the reports is $1.36B (RBC) to $2.73B (Jefferies).
2. **Morgan Stanley's patient count.** The 38,000 patients on therapy in 2035 are 25% of 150,000 US-plus-Europe patients (MS p.5). The model does not use 38,000 as a US count.
3. **The $390K kidney-drug price.** The price is sibeprenlimab's launch price for IgA nephropathy; Jefferies does not say whether it is list or net (PDF p.3, p.13, p.50). The retargeting cost treats povetacicept's net price as an assumption with a range.
4. **Discount rates.** The seven reports use 7.5% (Jefferies) to 10% (Morgan Stanley), not 8–10%.
5. **Probability of success.** The printed values are 50% (Morgan Stanley), 60% (Jefferies, Oppenheimer), and 70% (Truist, raised from 50%). RBC prints none.
6. **Trial floor.** AMPLITUDE admits eGFR 25 to under 75 and UPCR 0.7 to under 10 g/g (MS p.12), so the label-eligible definition uses an eGFR floor of 25.
**Reason:** Operating rule 2 requires tracing each claim to the original document. These six items differ from the prompt text, and the prompt tells the agent to check each seed fact before use.

## D-005 — Corrections and updates from the public analyst refresh
**When:** Sept 27, 2026, 12:34 PM Eastern.
**Decisions:**
1. **The 45% diabetic probability belongs to Guggenheim, not BMO.** Fierce Biotech (Sept 22) reports a Guggenheim note dated Aug 3 with 65% for primary AMKD and 45% for AMKD with type 2 diabetes. BMO's Sept 22 note, as quoted publicly, gives no probability. The prompt, the audit, and the timeline file credited BMO. The timeline file now carries the corrected row with a dated correction note; the prompt file is left unchanged because prompt versions are edited only as new versions.
2. **Probability-of-success base moves from 60% to 65%.** Guggenheim's 65% is the newest public figure for primary AMKD, and the prompt tells the model to use the newest figure for each variable. The range stays 50–70%.
3. **The interim analysis's primary endpoint is one-year eGFR.** The CEO said on the Aug 3 call that the FDA agreed to consider accelerated approval on that endpoint. The main approval risk is therefore whether eGFR separates within one year, which RBC's experts doubt (RBC p.5). The model keeps the full-approval branch at about 2029.
4. **Vertex's renal field force is fully hired** (about 90% with nephrology experience, headcount undisclosed; Q2 call). WS-B must estimate its size for the retargeting cost.
5. **A September 2027 launch remark is unconfirmed.** An AI-assisted summary quotes investor relations on Sept 9: "Potentially September 2027, getting close to a second launch potentially." The launch base stays at 2028 until WS-F confirms the wording from the webcast replay.
**Reason:** These items come from public sources dated after every sponsor report; each has a URL and a confidence rating in `work/research/analyst_public_refresh.md`.

## D-006 — Design rules for every option, from WS-H (pending Vertex legal review)
**When:** Sept 27, 2026, 12:46 PM Eastern.
**Decisions:** Every combination the model and the deck consider follows these rules, and the costs of following them sit inside the option:
1. Before approval, reps in any sales option make unbranded "test and refer" calls only; drug questions go to Medical Affairs (21 CFR 312.7).
2. Reps never see sponsored-test orders or results, and no goal or pay depends on tests ordered or positive results (OIG AO 22-06 and 24-12; QOL Medical, 2024).
3. A contract sales organization is paid fixed, fair-market-value fees for activity such as calls and reach, never for sales or tests (United States v. Mallory, 2021).
4. Added advertising stays unbranded before approval and visually separate from branded material after it. Paid media tells patients to ask a clinician about APOL1 testing and does not offer the free test until counsel clears it.
5. No Vertex-paid EHR alert or lab-report prompt. Any EHR element is a protocol a health system builds and owns from independent guidelines (Practice Fusion, $145M, 2020).
6. The launch-timing base stays at early 2028 (a mid-2027 filing plus an 8-month priority review). A national priority voucher (base probability 15%) would move the decision to about Sept–Oct 2027; the model carries it as an upside scenario.
**Reason:** WS-H found each rule in federal law, FDA regulation, OIG opinions, or DOJ settlements (`work/research/WS-H_policy.md`, sections 3–6). The rules narrow the design elements the organizers allowed, so the deck shows the legally safer version of each one.

## D-007 — Facts from the market and competitor profile that change the model or the deck
**When:** Sept 27, 2026, 1:55 PM Eastern.
**Decisions:**
1. **Competitor entry year.** The model's base year for a second APOL1 drug moves from "about 2029–2030" (the prompt's team projection) to Nov 2031, with a range of Nov 2030 to Nov 2032. The market profile builds these dates from Maze's planned pivotal trial start (first half of 2027) plus enrollment, treatment, filing, and review times (`notes/profile-market-and-competitors.md`, Part A3). All three dates are team projections.
2. **APOL1-FSGS has an approved drug.** The FDA approved Travere's Filspari (sparsentan) for FSGS without nephrotic syndrome on Apr 13, 2026 (Travere release). APOL1-FSGS is about 4% of AMKD (Morgan Stanley p.1). The deck keeps Vertex's wording that no therapy is approved for AMKD, and no slide says APOL1-FSGS patients lack a treatment.
3. **IgA nephropathy is crowded.** Six branded drugs hold US approval for IgA nephropathy, and povetacicept would be the seventh (Drugs@FDA). The retargeting cost (Option 1c) uses this fact.
4. **Share after a competitor enters.** The market profile's scenario shares (Vertex keeps 58%, 75%, or 85% of US APOL1-drug patients in 2035) are team projections with no published analog; the model carries them as an assumption with that range.
**Reason:** These facts come from Drugs@FDA, Travere's and Maze's releases, and ClinicalTrials.gov, as cited in the market profile, and each changes a model input or a slide's wording.

## D-008 — Two findings from the disease profile
**When:** Sept 27, 2026, 2:06 PM Eastern.
**Decisions:**
1. **The 2021 race-in-eGFR decision did not rest on APOL1.** The disease profile read both NKF–ASN task force reports and found no mention of APOL1 (`notes/profile-amkd-disease.md`, section 8). The prompt's trap 11 implied the debate "included APOL1." Slides and Q&A answers say only that race was removed from the eGFR equation in 2021, and never that APOL1 drove the decision.
2. **Where screening happens changes what it finds.** In a 2026 screening program, queries of electronic health records found high-risk genotypes in 46% of people tested, against 12% at community events (disease profile, section 12, fact 10, source [34]). WS-D tests this finding when it designs the added advertising (Option 2): outreach aimed at people already known to have kidney damage may yield more diagnoses per dollar than broad awareness.
**Reason:** Both findings change the deck's wording or the design of an option, and each carries a cited source in the disease profile.
