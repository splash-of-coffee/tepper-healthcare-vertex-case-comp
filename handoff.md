# Handoff — Tepper Vertex Case Comp (AMKD / inaxaplin)
**Date:** 2026-09-27
**Session Focus:** Build, audit, and harden a multi-phase agent prompt that runs the whole qualifying-round workflow for the 2026 Tepper Healthcare Case Competition.

## Situation
Chris's 4-person Tepper MBA team (Vidhur Vashisht lead, Skylar Dennerlein, Mike Homze, Chris) competes in the Vertex-sponsored case: recommend zero/one/both of Option 1 (sales: exactly one of 1a hire / 1b contract / 1c retarget nephrology reps) and Option 2 (direct-to-patient ads for APOL1 testing) to reach AMKD patients in primary care, with investment, headcount, NPV, ROI, payback. The qualifying deck (PDF) is due **Oct 4, 2026 11:59 PM Eastern**, and the team's internal target is Oct 3 at 9 PM. Finalists are announced Oct 8, the final deck is due Oct 20, and the final is in Boston Oct 22–23. **The strategy cannot change after Oct 8.** Deliverable this session was the prompt itself, not the deck. The prompt is ready to run once three placeholders are filled.

## Completed This Session
- `prompts/agent-prompt-v4.md` — current prompt (≈600 lines). Sections: role, mission, writing_standard, inputs, organizer_answers, equity_research_refresh, case_requirements, rubric_map, winning_principles, fact_base_seed, baseline, analytical_traps (15), workflow (Phases 0–7, Gates A/B/C), simulation_addon, subagent_contracts, deck_standard, operating_rules, first_move.
- `audit.md` — Opus subagent audit of v3: 32 findings (6 blockers), ~35-row fact-check table with sources, 13 gaps, fix list. v4 applies all of it, with 3 team modifications: the theme pick is kept but non-blocking; persona subagents are kept with an override line; the simulation is cut to Tier 1 and the staged-vs-committed comparison moves into the main model.
- `_archive/agent-prompt-v1.md`, `v2.md`, `v3.md` — rebuilt from the session record after Claude wrongly deleted them; logged in `_archive/ARCHIVE_LOG.md`. `prompts/CHANGELOG.md` summarizes every version; `prompts/diffs/v1-to-v2.diff`, `v2-to-v3.diff`, `v3-to-v4.diff`.
- `notes/vertex-timeline-2026-2028.md` — dated events May–Sep 27 2026 plus milestones through Dec 2028, each labeled reported / company guidance / analyst expectation / team projection, plus a table of analyst ranges.
- `notes/writing-standard.md` — binding plain-language standard ("AI accent" ban list, 11 rules, slide exemption, lint spec for `work/qa/lint_language.py`).
- `notes/acronyms.md`, `notes/team-insights-and-verification.md`, `notes/theme-brief.md`, `prompts/analytics-scientist-brief.md`.
- `materials/` — case PDF, announcement, organizer email, 7 analyst reports (copies; originals remain in Downloads).
- Chris's global agent rules file (outside this repository) — new "Archive Instead of Delete" rule: move files to `_archive/` in the working project and log them in `_archive/ARCHIVE_LOG.md`, never delete by default.

## Active Decisions
- **Baseline includes Vertex's existing programs** (free APOL1 testing via Labcorp/Natera/Arkana, Power Forward campaign since Nov 2022, AKF campaign, apol1ckd.com) → Option 2 means added spend only. This came from audit F01; Morgan Stanley p.5 confirms free genotyping.
- **150K/100K patient figures are US+Europe**, not US → size options on an estimated US label-eligible subset (non-diabetic, proteinuric, eGFR ≥ trial floor) and its primary care share.
- **AMPLIFIED results dated Sept 22, 2026**; the diabetes cohort's 95% CI (−36.3% to +7.2%) includes no effect, so it is treated as low-probability upside only.
- **Report tags are not scenario anchors**: RBC ("bear") is Outperform with a $543 target; the Stifel file is dated 3/25/26, not 5/25. Scenarios are built from drivers, bounded by analyst figures ($1.4B–$3.3B risk-adjusted 2035; $6.2B Oppenheimer unadjusted peak; PoS 50–70%).
- **Model must split pull-forward vs. net-new diagnoses** (Jefferies KOL: ~75% eventually diagnosed), use yearly cohorts, and report both NPV conditional on approval and risk-adjusted NPV, including a ~2029 full-approval path.
- **Slides:** 12–13 main + 3 appendix confirmed OK by the team; optional 17th AI-disclosure slide built as a separate file. Citations sit on each slide so the appendix can be dropped.
- **Organizer answers (Chris, 2026-09-27):** EHR prompts and legal cascade testing may sit inside an option; an outside reader is allowed; no AI-disclosure guidance.
- **Theme:** Option A (Vertex purple #52247F, Source Serif 4 + Open Sans, Carnegie Red #C41230 on the title slide only) is the default if the team has not picked by Oct 1.
- **Writing:** Chris flagged "AI accent" word choice. The standard is binding for all output, including messages to Chris.

## Current State
- Project root: `tepper-healthcare-vertex-case-comp/`. `work/` subfolders (research, model, deck, qa, handoff, theme, analytics) exist but are empty; the agent has not been run.
- `materials/analyst-reports/updated/` does not exist yet; the prompt tells the agent to create it.
- Tools verified installed: numpy, pandas, scipy, sklearn, statsmodels, matplotlib, openpyxl, python-pptx, PyMuPDF (fitz), pdfplumber, pdftotext, pywin32, Excel, and PowerPoint. Missing: pypdf, shap, LibreOffice, and pdftoppm, so the Read tool cannot render PDF pages; use fitz for text.
- No row for this project in `project_registry.md` yet.

## Next Actions
1. Fill the three `[[FILL]]` placeholders in `prompts/agent-prompt-v4.md`: teammate strengths (line ~12), office-hours notes path (inputs table), start date (workflow). Save as v5 per the versioning rule: new file, archive v4, add a changelog entry and a diff.
2. Assign a teammate to pull post-Sept 22 VRTX analyst reports through CMU library databases into `materials/analyst-reports/updated/`.
3. Start a fresh Opus 5.5 max-effort session in the project root and paste or point it to `prompts/agent-prompt-v4.md` (or v5). It should stop at Gate A with `work/handoff/gateA.md`.
4. Optional: add a PreToolUse hook blocking `rm`/`Remove-Item` to enforce the archive rule. It was offered and Chris has not answered.
5. Optional: resolve the duplicate MiroFish folder (two copies on Chris's machine); archive it, don't delete it.

## Gotchas
- **Never delete prior prompt versions.** Move them to `_archive/`, then update `prompts/CHANGELOG.md` and `prompts/diffs/`. Chris was upset when v1–v3 were deleted.
- The `mba_*` persona agents run a Context Assembly step that reads Chris's memory and course material. v4 requires an override line at the top of every persona subagent prompt.
- Chris's global CLAUDE.md says to `/save` at 65% context; v4 overrides that for the agent run (it updates `work/handoff/status.md` instead).
- Bash heredocs with quotes or backslashes broke twice this session. Write Python edit scripts with the Write tool to the scratchpad and then run them.
- openpyxl writes formulas without calculating them. Recalculate through Excel COM before reading model outputs.
- The Jefferies PDF's printed page numbers are 7 lower than its PDF page numbers; cite PDF pages.
- Analyst reports carry a license line naming a Vertex employee. Never reproduce it or the report pages in the deck.
- Audit facts not independently re-verified by Claude: Power Forward start date, Labcorp eligibility details, BMO 45% PoS, Jefferies page citations. The v4 prompt tells the agent to recheck all post-May-2026 facts.
