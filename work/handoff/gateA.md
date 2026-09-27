# Gate A — Plan Review

**Sent:** Sun Sept 27, 2026, 12:50 PM Eastern. **Default applies at:** 6:50 PM Eastern the same day, if the team has not replied.

The agent has finished Phase 0 (setup, reading, analyst extraction, public refresh, and the portfolio and policy streams) and Phase 1 (question tree, hypothesis, titles-only draft, and proposals). The team reviews this page and replies to Chris. **If there is no reply within 6 hours of this package, the agent continues on the defaults below and logs that it did so.**

## Decisions for the team

| # | Decision | Agent's recommendation | Default after 6 hours |
|---|---|---|---|
| 1 | Approve the plan (research streams below) and the first hypothesis | Approve | Continue with both |
| 2 | Simulation add-on: rerun the model 10,000 times to count how often each option wins (`simulation_proposal.md`) | Yes; it costs one agent-day and no money | Yes, and it is dropped automatically if the model audit misses the end of Sept 30 |
| 3 | Deck theme (`../theme/theme_suggestions.pdf`), any time before Oct 1 | Option A | Option A on Oct 1 |
| 4 | Fonts: Source Serif 4 and Open Sans are not installed on Chris's machine, so the theme file shows Georgia and Arial. Georgia prints numbers in an uneven old-style form. | Chris approves installing the two free Google fonts (about 2 minutes; logged in his software inventory). Teammates who edit the PPTX install them too. | Keep Georgia and Arial |
| 5 | One named teammate pulls newer analyst reports through CMU library access into `materials/analyst-reports/updated/` | Owner: Chris, since the files must land on his machine; the team lead can reassign | Chris |
| 6 | Each teammate's strengths (the prompt's open placeholder) | Needed to give each person one model module (funnel, costs, valuation, or risks) and a set of judge questions | Modules assigned alphabetically, to be changed later |
| 7 | Notes from the Sept 22 office hours | Did anyone attend? Anything said there overrides the agent's assumptions | No office-hours input |
| 8 | Interviews: one 15–20 minute conversation each by Sept 30 (`interview_guides.md`): a primary care physician, a nephrologist, a pharma sales or marketing professional, and a patient advocate | Try for all four; only notes the team takes can be quoted | None |

**Theme options (decision 3).** The PDF shows each theme's title slide and one sample content slide with placeholder data.
- **A, sponsor-forward (recommended).** Vertex purple #3E125F, sampled from the logo on the case cover, for titles and the recommendation; gray body text; Carnegie Red only on the title slide. The deck looks native to Vertex readers, and red stays out of the numbers.
- **B, Tepper-forward.** Carnegie Red title slide, titles, and slide numbers; Vertex purple marks the recommendation in charts. It signals Tepper, but readers see red as a loss on financial slides.
- **C, Healthcare Club navy.** Club navy title slide and Weaver Blue titles, with Vertex purple for the recommendation. It is the calmest of the three and the least distinctive.

**Analyst pull details (decision 5).** CMU's public library guides list S&P Capital IQ (Pittsburgh campus only) and Bloomberg (in person: Tepper Quad, Hunt and Sorrells libraries). FactSet, LSEG Workspace, and Morningstar are not listed; check the A–Z list or ask a librarian. Priority: (a) notes dated after Sept 22, 2026 from Oppenheimer, Jefferies, Stifel, William Blair, Morgan Stanley, Truist, and RBC; (b) the same from BMO, Leerink, Guggenheim, Evercore ISI, Goldman Sachs, JPMorgan, or Bernstein; (c) the latest consensus, including any inaxaplin sales line.

## Central question and first hypothesis

**Central question.** Which of the eight allowed combinations of primary care sales and added direct-to-patient advertising should Vertex fund, at what headcount, budget, and timing, to add the most risk-adjusted value by getting more US label-eligible AMKD patients in primary care tested, referred, and treated with inaxaplin?

**First hypothesis (H1).** Vertex contracts a primary care sales force (Option 1b) and adds direct-to-patient testing advertising above today's Power Forward level (Option 2), with spending scaled up in stages at the early-2027 interim analysis and at approval. The model decides; the decision log records any change. Each reason has a test that would disprove it (`../decision_log.md`, entry D-003):
1. A contracted force fits a 50–70% chance of approval, because it starts faster and can shrink. *Disproved if* the hired force (1a) has the higher risk-adjusted NPV after ramp time and exit costs, or contracting starts within 2 months of hiring.
2. Retargeting the nephrology reps (1c) costs more than its cash cost, because those reps are launching povetacicept against two same-pathway drugs. *Disproved if* the displaced calls come from low-value nephrologists, making retargeting cheaper per added patient.
3. Ads and sales calls raise testing more together than apart. *Disproved if* the first $5M of ads added to the contracted force adds no NPV, or analog campaigns cost more per diagnosis than a treated patient is worth.

## What Phase 0 found

**Analyst reports.** None of the seven sponsor reports is current; all predate the Sept 22 AMPLIFIED results (`../research/analyst_staleness.md`). Six firms have raised price targets since, and none changed its rating. Five facts in the prompt were corrected (decision log D-004 and D-005):
- RBC's 2035 inaxaplin forecast is $1.36B worldwide, risk-adjusted; its $3.3B is an unlabeled "opportunity." The 2035 risk-adjusted range across reports is $1.36B to $2.73B.
- Morgan Stanley's 38,000 patients on therapy in 2035 are a US-plus-Europe count.
- The 45% probability for the diabetic group is Guggenheim's (Aug 3 note), not BMO's. Guggenheim's 65% for the first label is the newest public figure, so the model's base moves to 65% (range 50–70%).
- The seven reports discount at 7.5% to 10%, not 8% to 10%.
- Vertex's CEO said on Aug 3 that the FDA agreed accelerated approval can rest on one-year eGFR at the interim analysis. Whether one year is long enough is the main approval risk (RBC's experts expect two years).

**Vertex portfolio (WS-G).** Vertex has no primary care sales force in any of its five business lines, and every acquisition since 2019 treats a disease that specialists manage. Suzetrigine for diabetic nerve pain, the only other late-stage drug with primary care prescribers, reads out about mid-2027 and would more likely use the 300-rep Journavx force than an AMKD team. That lowers the future value of hiring a permanent team (Option 1a). The renal force is fully hired and, from Dec 2026, launches povetacicept as the third new APRIL-pathway drug for IgA nephropathy in 12 months; pulling its calls into primary care (Option 1c) would come out of that contested launch. Povetacicept moved from interim readout to FDA decision date in 8.7 months, so an inaxaplin decision in Q4 2027 is the earliest plausible date. ASN Kidney Week (Oct 21–25) overlaps the final round.

**Policy and promotion rules (WS-H).** Before approval, any rep, hired or contracted, may make unbranded "test and refer" calls and hand out sponsored-testing materials. The rep may not name inaxaplin, see which physicians ordered tests, or earn pay tied to tests (21 CFR 312.7; OIG Advisory Opinions 22-06 and 24-12; QOL Medical's $47M settlement in 2024). A pre-approval force therefore earns its return only through added tests, which favors a small start that scales after approval. A contract sales organization must be paid fixed, activity-based fees, because volume-based pay to contractors falls outside the Anti-Kickback Statute safe harbors (United States v. Mallory, 2021). Unbranded testing ads fall outside FDA's drug-ad rules and outside the broadcast rule FDA plans to propose in December 2026. Paid ads that offer Vertex's free test go beyond the facts OIG approved, so the ads say "ask your clinician about APOL1 testing" until Vertex counsel clears more. Vertex-paid EHR or lab-report prompts have no safe harbor: an EHR vendor, Practice Fusion, paid $145M in 2020 over an alert a drug maker funded. Any EHR element must therefore be a protocol the health system builds and owns. A mid-2027 filing with priority review points to an FDA decision about 8 months later, in early 2028. Medicare price negotiation would start about 2037–2038, and most-favored-nation pricing would cut the blended net price by an estimated 0–10%. Both effects scale with every option, so neither changes the ranking.

## Research plan (starts on approval of this page)

Seven streams run in parallel from Sept 28: patient numbers and the funnel (WS-A), Vertex capabilities and competitors (WS-B), sales-force cost and response (WS-C), advertising, testing, and channel design (WS-D), equity and trust (WS-E), coverage, net price, and approval timing (WS-F), and primary care launch examples (WS-I). Sub-questions and owners are in `../research/question_tree.md`. The model build starts Sept 29 on draft inputs and fills in values as streams report; the independent model audit finishes by the end of Sept 30, which keeps the strategy lock (Gate B) on Oct 1.

## Attachments

- `../deck/titles_draft_v1.md` — 13 main-slide titles stating H1, and the gaps each title exposes
- `../research/question_tree.md` — sub-questions, owners, research plan
- `../theme/theme_suggestions.pdf` — three themes, two slides each
- `simulation_proposal.md`, `interview_guides.md`, `ai_disclosure.md` (draft)
- `../research/analyst_staleness.md`, `../research/analyst_consensus.md`, `../research/analyst_public_refresh.md`
- `../research/WS-G_vertex_portfolio.md`, `../research/WS-H_policy.md`
- `../model/model_spec.md` — the model structure for Phase 3
