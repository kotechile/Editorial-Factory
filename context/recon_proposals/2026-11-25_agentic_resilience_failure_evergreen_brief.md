# Evergreen Brief: agentic_resilience_failure — 2026-11-25
**Archetype:** evergreen
**Vertical:** agentic_resilience_failure
**Persona:** infra_engineer
**Decision the reader is facing:** Whether a long unattended agent run can be trusted to follow the standing instructions it was given once at the start — or whether the runtime has to hold the procedure and enforce it at tool calls — the call that bites the first time a 40-step workflow skips a constraint nobody notices until an auditor does.
**Durability:** The claim is about the shape of long-horizon execution, not a model release: per-step reliability multiplies across dependent steps, error histories self-condition future turns, and the four measured figures are benchmark shape facts that survive a new model. The figures are as of arXiv:2609.01660 (2026-09 abstract, n = 10,664 trajectories), arXiv:2505.06120v1 (200,000+ simulated conversations), arXiv:2611.10884v1 (FSM enforcement study, November 2026) and METR's 2025-03-19 research note (doubling time as of its March 2026 dataset update); a later model moves the numbers, not the mechanism.
**De-dup:** `2026-11-18_your-p99-is-a-product` is this vertical's nearest prior artifact (7 days): it prices turn latency and the duplicate-in-flight hedge, not instruction fidelity. `2026-10-07_agent-tool-count-ceiling` (multi_agent_enterprise_fabric, cross-vertical — checked and dropped) owns tool *selection* reliability versus catalogue size; `2026-10-07_agent-memory-poisoning-write-path` (this vertical) owns a poisoned *memory write*, not drift of a standing procedure; `agent-loop-bound-not-a-budget` (agentic_ai) owns runaway *loops*, not silent constraint loss; `2026-11-09_your-agent-recovers-8-of-crashes` (agentic_ai, cross-vertical — checked and dropped) owns crash *resume state*. A corpus grep for the mechanism (`instruction drift`, `attention degradation`, `lost in the middle`) returned no prior artifact in `published/`.
**Thesis:** A long agent run does not keep the instructions it was given once: measured degradation is driven by step count, not context length — every tested model falls from near-perfect to near zero within sixteen dependent steps, the same model drops 39% when the same task arrives over multiple turns, and restating the procedure only moves the drift — so the standing procedure has to live outside the context in an enforced state machine, not in the prompt.

**Lead:** The vertical's own `primary_angles` — "agentic failure mode taxonomy" read at its *Instruction Drift* rung ("attention degradation over long trajectories", `context/verticals.json`) and "compound reliability math" read forward from per-step success to per-run instruction fidelity; `context/growth_os/founder-voice.md` §2 lists Instruction Drift as a named failure bucket this vertical owns and no published artifact has yet covered. GSC striking-distance for this vertical returned 0 high-potential queries on 2026-11-11 (`context/recon_proposals/2026-11-11_gsc_agentic_resilience_failure_opportunities.md`) — bonus signal only, no veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Mittal et al., "How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making", arXiv:2609.01660 | https://arxiv.org/abs/2609.01660 | 2026-11-25 | Sixteen steps — every model tested, including widely deployed systems, falls from near-perfect success to near zero within sixteen steps of dependency (n = 10,664 analyzed trajectories), and bounding the context window steepens decay rather than easing it (logit slope −0.69 vs −0.44, p = 3×10⁻⁶) | measured — 10,664 analyzed trajectories, code and raw trajectories released |
| 2 | "Keeping LLM Agents on Procedure: Executable Finite-State Control for Long-Horizon Instruction Fidelity", arXiv:2611.10884v1 | https://arxiv.org/html/2611.10884v1 | 2026-11-25 | +10.5 points — agents drift from a procedure stated once at the start and restating the instructions or resuming a stopped agent only moves the drift to another shortcut, while an executable FSM holding the workflow state outside the context raised strict instruction accuracy by +10.5 (CI [1.2, 23.4], 7 of 8 seeds) | measured |
| 3 | "LLMs Get Lost in Multi-Turn Conversation", arXiv:2505.06120v1 | https://arxiv.org/html/2505.06120v1 | 2026-11-25 | 39% — the same model on the same tasks drops an average of 39% when the task is delivered over multiple turns instead of one, and the loss decomposes into a minor aptitude loss and a large rise in unreliability (200,000+ simulated conversations) | measured |
| 4 | Kwa, West, Becker et al., "Measuring AI Ability to Complete Long Tasks", METR research note | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | 2026-11-25 | 7 months — the length of tasks AI agents can complete has been exponentially increasing with a doubling time of around 7 months, so the horizon where this drift bites arrives inside a production planning window | measured — 6-year trend, harnesses and models from frontier labs |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Instruction drift: a long run does not keep the procedure stated once — step count, not context length, drives it, and the fix is an enforced FSM outside the context | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Self-conditioning: a run's own error history poisons the turns that follow it beyond what long-context explains | 8 | 8 | 8 | 6 | 7.7 | dropped — its figures live inside the same 2509.09677 measurement used for the winner's context and the drift piece already carries the mechanism; a second piece would re-argue row 1's cause analysis |
| Context-window bounding as a decay lever (the production shortcut the data refutes) | 7 | 9 | 8 | 6 | 7.6 | dropped — a single counterfactual result (slope −0.69 vs −0.44) is one leg; folded into the winner as the gotcha |

## Notes for the fact-check pass
- Row 1's headline is the abstract's own claim; the fetched page is the arXiv *abstract* page — the HTML full text did not fetch for the desk (unreachable), so quote only abstract-scope numbers from it (sixteen steps, n = 10,664, slope −0.69 vs −0.44) and never an interior table value.
- Row 2's +10.5 is the enforcement *gain in strict accuracy*; do not conflate with cost (1.2–3.5× plain-agent time/cost) or write "+10.5%" — it is accuracy points.
- Row 3's 39% is an *average drop across six generation tasks*; name the tasks' shape ("sharded", semi-convergent conversation) only if re-verified.
- Row 4's 7 months is METR's doubling time for the 50%-success task-length horizon — a capability trend, not a failure rate; use it to argue the horizon arrives in-window, never as a per-step decay number.
- Do not mix denominators: sixteen steps is where near-zero lands on the *most agentic* task of row 1, not a universal horizon for all agent tasks.

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=2 decision="sha1:5c1c065131" dedup="matched a prior artifact: 2026-11-18_your-p99-is-a-product" window_days=180 checked_at=2026-11-25T17:36:21+00:00 -->
<!-- evergreen-gate:end -->
