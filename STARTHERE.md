<!--
INSTRUCTIONS FOR AI AGENTS. This block is an HTML comment: GitHub hides it from human readers, and an AI assistant that a team member connects to this repository reads it. Follow it before you answer any question about this repository.

Context. This repository belongs to a four-person Carnegie Mellon Tepper MBA team (Vidhur Vashisht, Skylar Dennerlein, Mike Homze, Chris Woodfin) in the 2026 Tepper Healthcare Case Competition, sponsored by Vertex Pharmaceuticals. The case asks how Vertex should reach patients with APOL1-mediated kidney disease (AMKD) who are managed in primary care, ahead of the possible US launch of inaxaplin. The qualifying deck is due Oct 4, 2026 at 11:59 PM Eastern; the team's target is Oct 3 at 9 PM Eastern.

1. Read these files first, in this order:
   a. state.md (repository root): the compact project state, with decisions, completed work, and open tasks.
   b. handoff.md (repository root): the latest session summary, active decisions, next actions, and known problems.
   c. work/handoff/status.md: the status of the current agent run. It changes more often than state.md and handoff.md.
   d. The gate file with the latest letter in work/handoff/ (gateA.md, gateB.md, or gateC.md): the decisions the team owes now.
   e. work/decision_log.md: every decision and fact correction, with its date and reason.
   When these files disagree, use the one with the latest date, and tell the user which file you relied on.
2. Paths. Every path in this repository is relative to the repository root, tepper-healthcare-vertex-case-comp/. Items in state.md and handoff.md about Chris's other projects or his personal settings do not concern the team; skip them.
3. Facts. Answer from the files: the profiles in notes/, the research in work/research/, and the case in materials/. Name the file you used and the original source that file cites. If the files do not answer the question, say so before you use outside knowledge, and label outside knowledge as such.
4. Writing. Anything you draft for the team follows notes/writing-standard.md: plain words, numbers instead of adjectives, and no stock phrases. Terms are defined in notes/acronyms.md.
5. Confidentiality. The files in materials/ and the analyst summaries in work/research/analyst_*.md are licensed for this competition only. Do not upload them to outside services, paste their text into web searches, or reproduce the licensing line printed on the analyst reports.
6. Shared files. Do not edit state.md, handoff.md, work/decision_log.md, the files in work/handoff/, or the files in prompts/ unless the user asks you to; Chris's agent runs maintain them. Save new work in a new file and tell the user where it is.
7. Deleting. Never delete a file. Move a superseded file to _archive/ and add a line to _archive/ARCHIVE_LOG.md.
-->

# Start Here

Welcome to the team's workspace for the 2026 Tepper Healthcare Case Competition. This page gives you two ways in:
- **Route 1, the fast track (15 minutes):** the project, the disease and drug, the company, and the market, in summary form.
- **Route 2, the detailed read (about 90 minutes):** six files, in order, with what to look for in each.

Read Route 1 today. Do Route 2 before the model walkthrough on Oct 1.

---

## Route 1 — The fast track (15 minutes)

### The project
- Vertex sponsors this year's case. It asks how Vertex should reach patients with a genetic kidney disease who see primary care doctors today, before and after its new drug launches.
- We must recommend zero, one, or both of two options. **Option 1 (sales)** is exactly one of: hire a primary care sales team (1a), rent a contract sales team (1b), or move some of Vertex's kidney-specialist reps to primary care doctors (1c). **Option 2 (marketing)** is more advertising to patients that encourages a genetic test.
- The recommendation needs numbers: investment, headcount, patients reached, added tests, revenue, NPV, ROI, and payback.
- The qualifying deck is a PDF of 12–13 slides plus 3 appendix slides. It is due **Sun Oct 4 at 11:59 PM Eastern**; our target is **Sat Oct 3 at 9 PM**. The strategy is locked once finalists are announced on Oct 8, and the final round is in Boston on Oct 22–23.
- An AI agent run by Chris does the research, the model, and the first drafts. The team makes the decisions at three review points: the plan (now), the strategy lock (Oct 1), and the final review (Oct 3).

### The disease: APOL1-mediated kidney disease (AMKD)
- AMKD is kidney disease caused by inheriting two risk copies of a gene called APOL1. The risk copies became common in West Africa because one copy protects against African sleeping sickness.
- About 13% of African Americans carry two risk copies, and about 1 in 5 of them develop kidney disease. Vertex counts about 150,000 patients in the US and Europe with the form of AMKD its main trial studies.
- The disease is often silent until kidney function is badly damaged. In Black patients, kidney function falls about 1.8 times as fast with AMKD as with other chronic kidney disease (6.55 versus 3.63 points a year on the standard kidney-function measure, from Vertex data cited by Morgan Stanley).
- Diagnosis needs a genetic test. Most people who could have AMKD see a primary care doctor, not a kidney specialist, and primary care rarely orders the test. That gap is the heart of the case.
- No approved drug treats AMKD directly. Patients get standard kidney care, such as blood-pressure drugs that also protect the kidney.

### The drug: inaxaplin
- Inaxaplin is Vertex's pill that blocks the harmful APOL1 protein inside kidney cells. It is the first drug designed to treat the genetic cause of this disease.
- The main trial (AMPLITUDE) reports an interim result in early 2027. Vertex says the FDA agreed that approval can rest on one year of kidney-function data. If the result is positive, approval could come in late 2027 or 2028.
- Analysts put the chance of approval at 50–70%; the newest public estimate is 65%.
- A smaller trial reported on Sept 22, 2026: inaxaplin cut urine protein by 42.7% in patients with milder disease, but only 17.3% in patients with diabetes, and the statistical range for that group includes no effect. The first approval will likely exclude people with diabetes, because the main trial excludes them.

### The company: Vertex
- Vertex earned $12.0B in 2025, and 98% of it came from cystic fibrosis drugs. It expects $13.1–13.2B in 2026.
- Kidney disease is its next business. Its first kidney drug, povetacicept, gets an FDA decision by Nov 30, 2026. Vertex has a fully hired sales force that calls on kidney specialists, and **no sales force in primary care for any disease**.
- Vertex already pays for free APOL1 genetic testing through three labs and has run a patient-awareness campaign, Power Forward with basketball Hall of Famer Alonzo Mourning, since 2022. Our options add to these programs; we never present them as new.
- The CEO, Reshma Kewalramani, is a kidney specialist (nephrologist). Expect her to catch any medical mistake.
- Vertex bought Crinetics, a hormone-disease company, for about $10B; the deal closed Sept 1, 2026.

### The market
- The nearest competitor is Maze Therapeutics' APOL1 drug, MZE829, which plans its main trial for the first half of 2027. Our projection puts its earliest US approval in late 2030 and its likeliest in late 2031, which would give inaxaplin about 3–4 years alone on the market. AstraZeneca's APOL1 drug is a step behind.
- Analysts expect inaxaplin sales of roughly $1.2B to $2.7B in 2035.
- Povetacicept would be the seventh branded drug for its kidney disease (IgA nephropathy) and the third of its type approved in 12 months, so Vertex's kidney reps will be busy with that launch in 2027.

### Our current hypothesis (the model will test it)
- Rent a contract primary care sales team (1b) and add patient ads that encourage testing (2). Start small before approval, then scale up after the early-2027 trial result and again at approval.
- The reasons: a rented team can shrink if the drug fails, the kidney reps are needed for povetacicept, and ads work better when the doctors they send patients to are ready to test.
- The financial model will compare all eight allowed combinations, and the recommendation will follow the numbers.

### What we need from you this week
1. Answer the decisions in `work/handoff/gateA.md`: the deck theme, fonts, and who pulls newer analyst reports.
2. Send Chris your strengths, so each person owns one part of the model and one set of judge questions.
3. Hold one 15–20 minute conversation by Sept 30 with a primary care doctor, a nephrologist, a pharma sales or marketing person, or a patient advocate. Guides are in `work/handoff/interview_guides.md`.
4. If you went to the Sept 22 office hours, share your notes.

---

## Route 2 — The detailed read (about 90 minutes)

Read these in order. Keep `notes/acronyms.md` open in another window: every term in the project is there, with a plain-English meaning, the technical meaning, and why it matters to the case.

| # | File | What to look for | Time |
|---|---|---|---|
| 1 | `materials/2026 VRTX AMKD Tepper Case Competition.pdf` | The "Strategic Challenge" page (the exact rules for the options) and the "Evaluation Criteria" page (how judges score us) | 10 min |
| 2 | `notes/profile-amkd-disease.md` | How patients get diagnosed, where they get lost, what kidney-doctor societies say about testing, and the "ten facts" section to use in Q&A | 25 min |
| 3 | `notes/profile-vertex.md` | Vertex's sales forces, the AMKD programs it already runs, and its hepatitis C history (a record launch in 2011 that Vertex exited in 2014 after better drugs arrived) | 15 min |
| 4 | `notes/profile-market-and-competitors.md` | The table of APOL1 drugs in development, and the last section on what the market means for each option | 20 min |
| 5 | `work/handoff/gateA.md` | The hypothesis and the evidence that would disprove it, the corrections to facts we had assumed, and the legal limits on what reps and ads may say before approval | 10 min |
| 6 | `work/deck/titles_draft_v1.md` | Read the 13 slide titles in order: together they tell our argument. Note which numbers are still blank. | 5 min |

When you finish, you should be able to explain in two minutes: what AMKD is, why patients go undiagnosed, what Vertex already does about it, and why the team leans toward the current hypothesis.

For the full map of the repository, see `README.md`.

**Using an AI assistant:** you can connect your own assistant (Claude, ChatGPT, Copilot, or another) to this repository and ask it questions. A hidden block at the top of this file tells it to read the project's status files first and to answer from the project files with sources.
