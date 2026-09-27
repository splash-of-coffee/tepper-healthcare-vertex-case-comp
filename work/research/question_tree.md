# Question Tree and Research Plan

Written Sept 27, 2026. The central question and the first hypothesis are logged in `work/decision_log.md` (entries D-002 and D-003).

## Central question

Which of the eight allowed combinations of primary care sales and added direct-to-patient advertising should Vertex fund, at what headcount, budget, and timing, to add the most risk-adjusted value by getting more US label-eligible AMKD patients in primary care tested, referred, and treated with inaxaplin?

## Sub-questions

The tree has four branches. The first three branches do not overlap: branch 1 sizes the patients and their value, branch 2 measures what each option buys, and branch 3 tests fit and constraints. Branch 4 combines the three branches in the model. Each sub-question has one owning stream; a second stream appears only where it supplies one named input.

### Branch 1: How many patients can the options reach, and what is each one worth?

| # | Sub-question | Owner | Input from |
|---|---|---|---|
| 1.1 | How many US patients would a first label cover (two APOL1 variants, no diabetes, proteinuria at the trial threshold, eGFR at or above the trial floor), and what share sees only a primary care clinician? | WS-A | — |
| 1.2 | Where do those patients drop out between a primary care visit and treatment: testing, referral, the nephrology visit, biopsy or workup, prior authorization, starting the drug, and staying on it? | WS-A | WS-F (payer criteria) |
| 1.3 | How many of them would the baseline (the nephrology reps plus Vertex's current programs) reach anyway, and how many years earlier does each option find them? | WS-A | the model |
| 1.4 | What is one added treated patient-year worth after net price by payer channel, persistence, eligibility loss from eGFR decline, competitor entry, and Medicare negotiation? | WS-F | WS-H (policy), analyst extracts |

### Branch 2: What does each option buy, and at what cost?

| # | Sub-question | Owner | Input from |
|---|---|---|---|
| 2.1 | What does a hired or a contracted primary care rep cost, how fast can each start, and how many added tests and referrals does each call produce by physician decile? | WS-C | WS-I (analog response rates) |
| 2.2 | What does retargeting the nephrology reps displace: povetacicept and inaxaplin calls to nephrologists, valued net price to net price, by year? | WS-C | WS-B (force size and call plan) |
| 2.3 | How many added tests and confirmed diagnoses does added direct-to-patient spend produce per dollar, above the Power Forward and American Kidney Fund campaigns, and through which channels? | WS-D | WS-I (analog campaigns) |
| 2.4 | What do EHR prompts, lab-report prompts, family (cascade) testing, and a fast-track referral path add, what do they cost, and which option can carry each one? | WS-D | WS-H (legal limits) |
| 2.5 | What did comparable launches achieve when they pushed genetic testing or kidney care into primary care? | WS-I | — |

### Branch 3: Which option fits Vertex, and what constrains it?

| # | Sub-question | Owner | Input from |
|---|---|---|---|
| 3.1 | What does Vertex have today: field forces and their call points, the povetacicept launch plan, the Journavx force build, the Crinetics integration, the free-testing programs, and its launch history? | WS-B, WS-G | — |
| 3.2 | When could inaxaplin launch, under which approval path, and what may Vertex say and do in primary care before approval? | WS-F, WS-H | — |
| 3.3 | Which rules on drug pricing, advertising, and manufacturer-sponsored programs change the value or the legality of each option? | WS-H | — |
| 3.4 | What do patients and communities need for genetic testing to be trusted and private, and how must slides describe race and genetics? | WS-E | — |

### Branch 4: The decision (Phase 3 model and Phase 4 decision)

| # | Sub-question | Owner |
|---|---|---|
| 4.1 | Which combination has the highest risk-adjusted NPV, and does it still win when the decision weights and the model inputs move across their ranges? | Model (mba_finance build, mba_optimizer sensitivity) |
| 4.2 | At what headcount (steps of 10 reps) and advertising budget (steps of $5M) does the last rep's or last dollar's added NPV reach zero? | Model |
| 4.3 | Which results from the interim analysis and approval trigger scale-up, hold, or stop, and how much is waiting for that information worth? | Model, then the engagement lead |

## Research plan

| Stream | Scope | Subagent type | Starts | Output |
|---|---|---|---|---|
| Analyst extraction (2 subagents) | The seven sponsor reports | general-purpose | Sept 27 (running) | `work/research/analyst_*.md` |
| Public analyst refresh | Analyst actions after each report; firms missing from the sponsor set | general-purpose | Sept 27 (running) | `work/research/analyst_public_refresh.md` |
| WS-G | Vertex portfolio | mba_strategist | Sept 27 (running) | `work/research/WS-G_vertex_portfolio.md` |
| WS-H | Pricing policy, FDA rules, advertising and promotion rules, legal limits on sponsored programs | mba_economist | Sept 27 (running) | `work/research/WS-H_policy.md` |
| WS-A | Patient numbers and the funnel (sub-questions 1.1–1.3) | mba_marketing | After Gate A (Sept 28–29) | `work/research/WS-A.md` |
| WS-B | Vertex capabilities, history, and competitors (3.1) | mba_strategist | After Gate A | `work/research/WS-B.md` |
| WS-C | Sales force costs and response, and the retargeting cost (2.1, 2.2) | mba_optimizer | After Gate A | `work/research/WS-C.md` |
| WS-D | Direct-to-patient advertising, testing, and channel design (2.3, 2.4) | mba_marketing | After Gate A | `work/research/WS-D.md` |
| WS-E | Equity, trust, and ethics (3.4) | mba_ethicist | After Gate A | `work/research/WS-E.md` |
| WS-F | Coverage, net price, approval timing (1.4, 3.2) | general-purpose | After Gate A | `work/research/WS-F.md` |
| WS-I | Primary care launch examples (2.5) | mba_strategist | After Gate A | `work/research/WS-I_analogs.md` |

All nine streams report by the end of Sept 30. The model build starts on Sept 30 from the streams that have reported, and the model audit finishes by the end of Sept 30, as the calendar in the prompt requires.

## Data the team can get and the agent cannot

1. Newer analyst reports through CMU library databases (the request is in the Gate A package).
2. Notes from the Sept 22 office-hours session, if anyone attended.
3. One conversation each with a primary care physician, a nephrologist, a pharma sales or marketing professional, and a patient advocate (guides in `work/handoff/interview_guides.md`).
4. Each teammate's strengths, so model modules and likely judge questions get owners.
