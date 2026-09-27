# Run Status (for a new session to resume)

**Last updated:** Sun Sept 27, 2026, 12:52 PM Eastern.
**Prompt:** `prompts/agent-prompt-v4.md` (run started 11:51 AM Eastern; decision log D-001).
**Phase:** stopped at **Gate A** (`work/handoff/gateA.md`, sent 12:50 PM Eastern). Default applies at 6:50 PM Eastern if the team has not replied: continue with the plan and hypothesis H1, simulation yes, theme A on Oct 1, keep Georgia and Arial, Chris owns the analyst pull.

## Done (Phases 0 and 1)
- Decision log D-001 to D-006 (`work/decision_log.md`): start and placeholders; central question; hypothesis H1 (contracted primary care force plus added unbranded testing ads, staged on the early-2027 interim and approval); fact corrections from the extractions (D-004) and the public refresh (D-005: the 45% diabetic probability is Guggenheim's, and the base probability of success is 65%); design rules from WS-H (D-006).
- Language check `work/qa/lint_language.py` (zero ban hits across 23 files at Gate A); PDF export and page rendering `work/qa/export_pdf.py`.
- Theme suggestions `work/theme/theme_suggestions.pptx` and `.pdf` (build script beside them).
- Research: seven analyst extracts plus `analyst_six_summary.md`, `analyst_staleness.md`, `analyst_consensus.md`, `analyst_public_refresh.md`, `WS-G_vertex_portfolio.md`, `WS-H_policy.md`, `question_tree.md`.
- Drafts: `work/deck/titles_draft_v1.md`, `work/handoff/simulation_proposal.md`, `interview_guides.md`, `ai_disclosure.md`, `work/model/model_spec.md`.
- `notes/vertex-timeline-2026-2028.md` updated: Guggenheim correction, Aug 3 FDA one-year-eGFR agreement, Sept 22–23 analyst figures, Kidney Week Oct 21–25, Q3 results Nov 2, and WS-G registry dates.

## Next (after Gate A)
1. Log the team's Gate A answers (or the 6:50 PM default) in the decision log.
2. Launch WS-A, WS-B, WS-C, WS-D, WS-E, WS-F, WS-I in parallel (specs in the prompt's Phase 2 table; add D-006's design rules and the handoffs from WS-G and WS-H to each subagent prompt). WS-F must confirm the "September 2027" launch remark from the Sept 9 webcast replay and look for inaxaplin's US orphan designation.
3. Start the model build on Sept 29 on draft inputs (`work/model/model_spec.md`), with the audit finished by the end of Sept 30.

## Facts found this session that are not in the prompt
- Case PDF colors: headings #7030A0 (Office default purple); Vertex logo purple #3E125F; Vertex wordmark gray #595A5F; Healthcare Club navy #010F3B and red #F13345.
- pptxgenjs and markitdown are not installed; python-pptx 1.0.2 is. Decks are built with python-pptx and exported through PowerPoint COM.
- Open Sans and Source Serif 4 are not installed (font decision at Gate A).
