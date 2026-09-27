# Prompt Changelog

This file records every version of the agent prompt, what changed, and why. The current version lives in `prompts\`. Earlier versions move to the project's `_archive\` folder, logged in `_archive\ARCHIVE_LOG.md`. **Never delete a previous version.** Each new version gets a new file (`agent-prompt-vN.md`) and an entry here. The `diffs\` folder holds line-by-line differences between consecutive versions.

To compare any two versions yourself, run from the project root:
`git diff --no-index _archive/agent-prompt-v3.md prompts/agent-prompt-v4.md`

| Version | Date | Trigger | Main changes |
|---|---|---|---|
| v1 | 2026-09-27 | First draft, from the case PDF and research on winning case competitions | Engagement-lead role; case rules; a map of the scoring criteria; 12 principles for winning; a fact base from the case plus post-case news (AMPLIFIED, povetacicept decision date, MZE829); a list of common mistakes; an eight-phase workflow with four hard stops; research workstreams A–F; financial model specification; judge simulation. Materials were read from `Downloads`. |
| v2 | 2026-09-27 | Chris's answers: team roster, folder move, 12–13 + 2–3 slide target, AI disclosure, theme, portfolio and market analysis | Paths moved to the project folder. Four-person roster. Citations placed on each slide. AI disclosure drafted regardless of rules. Theme Checkpoint added (three themes, title and body slide each). Workstream G (Vertex portfolio breakdown) and workstream H (market environment and peers) added. Acronym dictionary and team notes added as inputs. |
| v3 | 2026-09-27 | Chris's feedback on AI-accent wording; request for a simulation idea | Writing standard (`notes\writing-standard.md`) made binding for all output, with a language-check script. The whole prompt rewritten in plain language. Optional simulation add-on (Monte Carlo, scenario tree, simple machine learning, MiroFish) proposed at Gate A and run by an analytics scientist subagent (`prompts\analytics-scientist-brief.md`). Plain-language reader added to the checks. |
| v4 | 2026-09-27 | Independent audit (`audit.md`, 32 findings), Chris's answers from the organizers, the analyst-report question | Baseline now includes Vertex's existing free APOL1 testing, Power Forward, and the AKF campaign. Fact corrections: AMPLIFIED dated Sept 22; US-plus-Europe population figures; diabetes result not significant; raised guidance; the Crinetics acquisition; the Journavx force; the Stifel date; report tags that do not match their contents. Model: patients found earlier vs. found only because of the spend, yearly cohorts, referral and biopsy steps, risk-adjusted NPV, full-approval path, staged spending, payer-mix net price, response curves, driver-based scenarios. Workflow: three gates plus a non-blocking theme pick, 6-hour defaults, a teammate model walkthrough, an outside reader, a cap of two simulated-judge rounds. Organizer answers added (12–13 + 3 slides, EHR prompts and cascade testing inside an option, outside review allowed, optional 17th AI-disclosure slide). New refresh of outdated analyst reports. Workstream H trimmed; workstream I (primary care launch examples) added. Persona override line, context override, tool list. Simulation cut to Monte Carlo for the qualifying round. |

## Restoration note (2026-09-27)

Claude deleted v1, v2, and v3 without being asked while writing each new version. Chris caught it after v4. The three files were rebuilt the same day from the session record: v1 from its original text, v2 from its final text as last read, and v3 from its original text plus its two later wording edits. Their contents match the versions as they stood before deletion. The file timestamps show the restoration time, not the original writing time. All three were then moved to `_archive\`.

## Supporting files that change with the prompt

These files were edited in place rather than versioned. Their changes are listed here.

| File | Changes |
|---|---|
| `notes\writing-standard.md` | Created with v3. At v4: examples that favored one option replaced with neutral placeholders; slide exemption added; the lint script now skips table cells and chart labels. |
| `prompts\analytics-scientist-brief.md` | Created with v3. At v4: qualifying round limited to Tier 1 (Monte Carlo); low and high values treated as 10th and 90th percentiles; Tiers 2–4 moved to the final round; Excel recalculation note added. |
| `notes\team-insights-and-verification.md` | Created with v2. At v4: population figures corrected to US plus Europe; guidance raised; Incivek sequence corrected; Crinetics, Journavx force, and organizer answers added. |
| `notes\acronyms.md` | Created with v2. At v4: AMPLIFIED date and population geography corrected; about 20 terms added (Crinetics, Palsonify, Power Forward, 340B, cascade testing, and others). |
| `notes\theme-brief.md` | Created with v2. At v4: theme pick made non-blocking, with Option A as the default after Oct 1. |
| `notes\vertex-timeline-2026-2028.md` | Created with v4. |

**Path cleanup, 2026-09-27.** Before the repository was published to GitHub, local machine paths in v1–v4, the diffs, the analytics brief, the audit, state.md, and handoff.md were replaced with paths relative to the repository root (`tepper-healthcare-vertex-case-comp/`), or with a plain description for files that live outside the repository (Chris's Obsidian notes, Downloads folder, global agent rules, and MiroFish project). No other text changed.
