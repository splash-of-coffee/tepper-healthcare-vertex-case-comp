# Simulation Add-on Proposal (Tier 1 Monte Carlo) — Decision Needed at Gate A

Written Sept 27, 2026. The team decides yes or no. The role brief for the subagent that would run it is `prompts/analytics-scientist-brief.md`.

**What it does.** A Monte Carlo simulation reruns the financial model 10,000 times. Each run draws a different value for every uncertain input from its low-to-high range in the assumptions register. All eight combinations are scored on the same 10,000 draws, so the comparison between combinations is fair. The output reports how often each combination has an NPV above zero, how often each one ranks first, and each one's range of outcomes (the 10th, 50th, and 90th percentile NPV).

**What it adds to the deck.** It adds at most one chart on the sensitivity slide and two method lines in the model appendix. A typical sentence would read: "The recommended combination has a positive NPV in [N]% of 10,000 simulated futures and ranks first in [M]%."

**What it costs.** It takes about one working day of agent time on Oct 1. It runs on Chris's machine with installed Python packages, so it costs no money and sends no data anywhere.

**Conditions.**
- It starts only after the Excel model passes its cell-by-cell audit. If the audit is not finished by the end of Sept 30, the add-on is skipped for the qualifying round.
- The Python copy of the model must match the Excel NPV for every combination within 1% before any result is used.
- A second subagent (mba_optimizer) reviews the statistics before the results reach the strategy lock (Gate B).
- The register's low and high values are treated as the 10th and 90th percentiles, not as hard limits, so the simulation does not understate the chance of a loss.

**Risks.**
- The simulation may show the recommendation ranking first less often than the base case suggests. The team would then have to report that result or change the recommendation before the lock.
- Every teammate must be able to explain the chart in the final round. The explanation takes two sentences: the model was rerun 10,000 times with inputs drawn from their ranges, and the chart counts how often each plan comes out ahead.
- Simulation results come from the team's own assumptions. The deck describes them as a test of those assumptions, not as evidence.

**Deferred to the final round, if the team wants them.** The regulatory scenario tree, the machine-learning rules, and the MiroFish stakeholder simulation (Tiers 2–4 in the brief). The staged-versus-committed comparison is already in the main model.

**Decision for the team.** Reply "simulation yes" or "simulation no." With no reply within 6 hours of the Gate A package, the default is **yes, subject to the audit cutoff above**, because the add-on costs no money and is dropped automatically if the model runs late.
