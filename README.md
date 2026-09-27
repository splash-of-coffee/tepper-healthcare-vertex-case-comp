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

# Tepper Healthcare Case Competition 2026 — Vertex / AMKD

**If you are new to the project, read [`STARTHERE.md`](STARTHERE.md) first.** It gives a 15-minute summary and a reading path. This README is the full reference map.

This repository holds the team's work for the 5th Annual Tepper Healthcare Case Competition, sponsored by Vertex Pharmaceuticals. The team is Vidhur Vashisht (team lead), Skylar Dennerlein, Mike Homze, and Chris Woodfin. An AI agent (Anthropic's Claude, run by Chris) does the research, the financial model, and the first drafts; the team makes every strategy and design decision at set review points.

**Deadlines:** qualifying deck (PDF) due **Sun Oct 4, 2026, 11:59 PM Eastern**; the team's internal target is **Sat Oct 3, 9 PM Eastern**. Finalists are announced Oct 8, and the strategy cannot change after that date. The final round is at Vertex in Boston on Oct 22–23.

---

## 1. The case, summarized

**The drug.** Vertex is preparing to launch **inaxaplin**, a pill for **APOL1-mediated kidney disease (AMKD)**. AMKD is kidney disease caused by inheriting two risk copies of the APOL1 gene, which is most common in people with recent West African ancestry. No approved drug treats it directly. Inaxaplin is still in trials; a positive interim result in early 2027 could lead to US approval in late 2027 or 2028.

**The problem.** Most people who could take inaxaplin do not know they have AMKD. Diagnosis needs a genetic test, and the primary care doctors who see most of these patients rarely order it. Vertex has a sales force that calls on kidney specialists (nephrologists) but none that calls on primary care.

**The task.** Recommend zero, one, or both of two options, with the investment, headcount, patient reach, testing increase, revenue, NPV, ROI, and payback:
- **Option 1, sales**, as exactly one of: **1a** hire a full-time primary care sales team; **1b** rent a contract sales team; **1c** move some of the existing kidney reps' calls to top primary care doctors.
- **Option 2, marketing:** spend more on direct-to-patient advertising that encourages APOL1 genetic testing, above what Vertex already spends.

That gives eight legal answers: none, 1a, 1b, 1c, 2, 1a+2, 1b+2, 1c+2. Recommending two versions of Option 1 breaks the rules.

**How it is judged (qualifying round):** strategic acumen, financial analysis, and written communication. The judges read the PDF with no one presenting it, so every slide must explain itself.

---

## 2. Reading order for your first session (about 90 minutes)

Keep **`notes/acronyms.md`** open in another window while you read. Every term and acronym in the project is there, with a plain-English meaning, the technical meaning, and why it matters to the case.

| Step | Read | What you will understand | Time |
|---|---|---|---|
| 1 | **The case**: `materials/2026 VRTX AMKD Tepper Case Competition.pdf` (7 pages) | The exact task, the rules, and the scoring criteria | 10 min |
| 2 | **The disease and the drug**: `notes/profile-amkd-disease.md` | What causes AMKD, who gets it, its symptoms, how it is diagnosed, why most patients are undiagnosed, what medical societies say, and how inaxaplin works | 25 min |
| 3 | **The company**: `notes/profile-vertex.md` | Vertex's revenue, strategy, leaders, history, sales forces, and the programs it already runs for AMKD (free testing, the Power Forward campaign) | 15 min |
| 4 | **The market and competitors**: `notes/profile-market-and-competitors.md` | Other APOL1 drugs in development (Maze, AstraZeneca, others), the kidney drugs doctors use today, who already promotes kidney care to primary care, and Vertex's competitors in each business | 20 min |
| 5 | **Where the project stands**: `work/handoff/gateA.md` | The plan, the first hypothesis, what the research found, and the **decisions the team owes** | 10 min |
| 6 | **The draft storyline**: `work/deck/titles_draft_v1.md` | The 13 slide titles that state our current argument, and the evidence each one still needs | 5 min |
| 7 | **Why we believe what we believe**: `work/decision_log.md` | Every decision and fact correction, with the date and reason | 10 min |

If you have only 15 minutes, read section 1 of this file, the "Summary" bullets at the top of each profile in steps 2–4, and the decisions table in `work/handoff/gateA.md`.

---

## 3. Going deeper (read when your topic needs it)

| Topic | File | What is in it |
|---|---|---|
| Dates, past and expected | `notes/vertex-timeline-2026-2028.md` | Vertex events from May to Sept 27, 2026, and expected milestones through 2028, each labeled reported, company guidance, analyst expectation, or team projection |
| What the analysts say | `work/research/analyst_consensus.md` | Launch year, price, probability of approval, sales forecasts, and discount rates from all seven sponsor reports, side by side, plus newer public figures |
| How old the analyst reports are | `work/research/analyst_staleness.md` | Which later events each report misses, and what each firm has done publicly since |
| Newer analyst actions | `work/research/analyst_public_refresh.md` | Price-target changes, post-Sept 22 comments, management statements, and which CMU databases carry full reports |
| One analyst report in detail | `work/research/analyst_<firm>.md` | Page-cited extracts of each sponsor report (Jefferies, Morgan Stanley, Oppenheimer, RBC, Stifel, Truist, William Blair) |
| Vertex's full portfolio | `work/research/WS-G_vertex_portfolio.md` | Every product and pipeline program, revenue by business line, field forces, deals, and a milestone calendar |
| Laws and rules that limit each option | `work/research/WS-H_policy.md` | What reps and ads may say before approval, rules for sponsored testing and EHR prompts, FDA review timing, and drug-pricing policy |
| The research plan | `work/research/question_tree.md` | The central question broken into sub-questions, with the research stream that owns each one |
| The financial model's design | `work/model/model_spec.md` | How the model counts patients, testing, revenue, costs, and NPV for each of the eight combinations |
| Team observations, fact-checked | `notes/team-insights-and-verification.md` | The team's early claims about Vertex and AMKD, each confirmed or corrected with sources |
| An independent review of the plan | `audit.md` | A review of an earlier prompt version, with a fact-check table of sources |

---

## 4. Where the project stands (as of Sun Sept 27, 2026)

The agent has finished the setup and planning phases and stopped at **Gate A (plan review)**. Its first hypothesis is a contract primary care sales team (1b) plus added unbranded testing ads (2), with spending scaled up in stages after the early-2027 trial result and again at approval. The financial model will test all eight combinations, and the recommendation will follow the numbers. See `work/handoff/gateA.md` for the evidence and the decisions pending.

| Date (2026) | Work | Team review point |
|---|---|---|
| Sun Sept 27 – Mon Sept 28 | Setup, reading, analyst research, plan, first slide titles | **Gate A: plan review** (the agent continues on stated defaults after 6 hours without a reply) |
| Tue Sept 29 – Wed Sept 30 | Seven research streams; assumptions and financial model; independent model check | — |
| Thu Oct 1 | Decision, critique, a 60-minute model walkthrough with all four teammates, revised storyline | **Gate B: strategy lock** (needs the team's explicit approval) |
| Fri Oct 2 | Build the deck | Theme must be chosen by Oct 1 (default: option A) |
| Sat Oct 3 | Checks, simulated judges, one outside reader, fixes | **Gate C: final review** by 3 PM; submit by 9 PM |
| Sun Oct 4 | Buffer; hard deadline 11:59 PM Eastern | — |

---

## 5. What each teammate should do this week

1. **Answer the Gate A decisions** in `work/handoff/gateA.md` (theme, fonts, simulation, who pulls newer analyst reports).
2. **Send Chris your strengths** (for example finance, clinical, sales, or presenting), so each person owns one part of the model and one set of likely judge questions.
3. **Share office-hours notes** from the Sept 22 session, if you attended.
4. **Hold one 15–20 minute conversation** by Sept 30 with a primary care physician, a nephrologist, a pharma sales or marketing professional, or a patient advocate. Guides: `work/handoff/interview_guides.md`. Save notes in `work/research/interviews/<date>_<role>.md`. Only quotes the team collects, with permission, may appear in the deck.
5. **Pull newer analyst reports** if that task is yours: Vertex notes dated after Sept 22, 2026, from CMU databases (Capital IQ, Bloomberg), saved in `materials/analyst-reports/updated/`.

---

## 6. Folder map

```
README.md          this file
materials/         case PDF, announcement, organizer email, seven analyst reports (licensed; see section 7)
  analyst-reports/updated/   newer analyst reports the team pulls
notes/             team reference files
  profile-amkd-disease.md          the disease and the drug
  profile-vertex.md                the company
  profile-market-and-competitors.md  competitors and the market
  acronyms.md                      glossary of every term (four columns)
  vertex-timeline-2026-2028.md     dated events and milestones
  team-insights-and-verification.md  team claims, fact-checked
  writing-standard.md              plain-language rules for all project text
  theme-brief.md                   deck colors and fonts
work/              the agent's working files
  handoff/         gate packages, status, interview guides, AI disclosure, simulation proposal
  research/        analyst extracts, research streams, question tree
  model/           financial model specification (the Excel model arrives in Phase 3)
  deck/            slide titles and storyline (the PowerPoint arrives in Phase 5)
  theme/           theme suggestion deck and its build script
  qa/              language-check and PDF-export scripts
  decision_log.md  every decision and fact correction, dated
prompts/           the agent prompt that runs this work (v4), its changelog, and diffs
_archive/          earlier versions of files; nothing is deleted
audit.md           independent review of an earlier prompt version
state.md, handoff.md   status files for AI agents: project state, latest session summary, next actions
```

---

## 7. Rules everyone follows

- **Case materials stay inside the team.** The case PDF and the analyst reports may be used only for this competition. Keep them out of any public repository, shared drive, or website. Do not paste their text into web searches or public AI tools; search for public facts in your own words. The analyst reports carry a licensing line naming a Vertex employee; never copy it or the report pages into the deck. Each teammate already has the files from Vidhur's Sept 21 email; after cloning, copy them into `materials/` on your own machine. The files in `work/research/analyst_*.md` summarize those reports, so keep them inside the team as well.
- **Plain language.** All project text follows `notes/writing-standard.md`: numbers instead of adjectives, simple words, and no stock phrases such as "leverage" or "robust." The agent checks every file with `work/qa/lint_language.py`.
- **Every number has a source.** Each figure on a slide carries a footnote with the source and its date, or a team assumption ID (for example "A-07") from the assumptions register.
- **Nothing invented.** No made-up quotes, interviews, surveys, or expert opinions.
- **Vertex's existing programs are the baseline.** Vertex already pays for free APOL1 testing and runs the Power Forward and American Kidney Fund campaigns. The deck builds on them and never presents them as new ideas.
- **Nothing gets deleted.** Old versions move to `_archive/` with a line in `_archive/ARCHIVE_LOG.md`.

---

## 8. Using an AI assistant with this repository

You can connect your own AI assistant (Claude, ChatGPT, Copilot, or another) to this repository and ask it questions. A hidden block at the top of this file and of `STARTHERE.md` tells the assistant to read the status files first (`state.md`, `handoff.md`, `work/handoff/status.md`, the latest gate file, and `work/decision_log.md`), to answer from the project files with sources, and to keep the licensed case files private. To see the block, open the raw file.

## 9. Contacts

- **Organizers:** Logan Foster (EVP, Tepper Healthcare Club) and Joshua Soulliere. Their email addresses are in `materials/Case Comp Announcement.pdf`.
- **Agent runs and file questions:** Chris Woodfin.
- **Team lead:** Vidhur Vashisht.
