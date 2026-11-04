# Evergreen Brief: agentic_resilience_failure — 2026-11-04
**Archetype:** evergreen
**Vertical:** agentic_resilience_failure
**Persona:** infra_engineer
**Decision the reader is facing:** Whether to recover a failed multi-step agent run by replaying the task from its first step or by unwinding the steps it already committed — and, before the failure, how to classify each tool call so that an unwind is even possible.
**Durability:** The claim is about the action space, not a product: a step's class (idempotent, reversible, compensable, irreversible) sets what recovery can cost, and that does not change with a framework release. The measured figures are as of the arXiv v1 postings of 25 April 2026 (n = 1,008 runs) and 16 June 2026 (45 workflows), the Temporal documented history cap as of the docs retrieved 2026-11-04, and the PostgreSQL 18 documentation as of 2026-11-04; none of the three is a price or a rate, so a reader in 12 months is checking editions, not freshness.
**De-dup:** `2026-10-28_your-90-restart-monitor-proves-nothing` is this vertical's nearest prior artifact — it prices a restart as a purchase and reads 103 live restart decisions, but it never asks what the undo of an already-committed step costs or how a step is classified; this brief takes the undo path itself. `2026-10-07_retry-is-the-failure-amplifier` and `2026-10-14_gate-the-step-not-the-model` own retry bounding and step-boundary reliability, not compensation. Checked and dropped cross-vertical: `2026-10-14_one-approval-two-payments` (multi_agent_enterprise_fabric) already owns the 24-hour idempotency-key pruning window as its thesis, so that mechanism is excluded from this piece entirely.
**Thesis:** A failed agent step is not recovered by a rollback but by an unwind whose price is set by the class of every action already committed, and the measured gap is large enough to design for — unwinding to the earliest conflict held full-restart quality at 0.78 wasted acts per run against 11.41 for replaying the task, and staging effects before commit intercepted 45 of 45 risk-bearing effects where per-call defenses left 31 of 45 untouched.

**Lead:** The vertical's own `primary_angles` include "transactional undo redo rollbacks", the one beat in that list neither the news runs nor the prior evergreens have taken (`context/verticals.json`); `context/growth_os/founder-voice.md` §3 for this vertical states the position ("autonomous agents must support transactional rollbacks … so that an API drop at Step 9 doesn't invalidate Steps 1–8"), and `context/growth_os/customer-truth.md` Anecdote 2 supplies the field shape (a nine-step reconciliation agent that restarted after a Step 8 timeout and double-booked $18,000 of disbursements). The specific material is the 2026 literature that finally measures the choice rather than asserting it: a reversibility taxonomy with a benchmarked rollback rule, and a transactional runtime with pre-commit interception numbers. GSC striking-distance for this vertical returned 0 high-potential queries on 2026-11-04 (thin impressions, bonus signal only) — recorded, not used as a veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Zhai, Li, Wang — "Revisable by Design: A Theory of Streaming LLM Agent Execution" (arXiv:2604.23283v1, Table 1) | https://arxiv.org/html/2604.23283v1 | 2026-11-04 | 14.6× — the Revision Absorber matched full-restart quality (3.07 vs 3.17, quality CI crossing zero) while wasting 0.78 acts per run against 11.41, 14.6× fewer discarded steps on a DeepSeek-V3 grid of n = 1,008 runs, 144 balanced runs per method | measured |
| 2 | "Cordon: Semantic Transactions for Tool-Using LLM Agents" (arXiv:2606.17573v1, §6.2) | https://arxiv.org/html/2606.17573v1 | 2026-11-04 | 31/45 — per-call defense boundaries leave 31/45 risk-bearing effects policy-violating or post-hoc-only, while the transactional runtime intercepts 45/45 before commit | measured |
| 3 | Cordon evaluation, §6.3 system performance (same paper) | https://arxiv.org/html/2606.17573v1 | 2026-11-04 | 4.17ms — median rollback latency, with 15/15 resume checks passing, at 22.2–23.4% of the measured path in transaction control | measured |
| 4 | Temporal documentation — Workflow Execution Limits | https://docs.temporal.io/workflow-execution/limits | 2026-11-04 | 51,200 — the workflow execution's event history is limited to 51,200 events or 50 MB and warns after 10,240 events or 10 MB, so an undo log for a long-running agent has a hard ceiling | documented limit (vendor) |
| 5 | PostgreSQL 18 documentation — PREPARE TRANSACTION | https://www.postgresql.org/docs/current/sql-prepare-transaction.html | 2026-11-04 | 200 bytes — a prepared transaction's identifier must be less than 200 bytes long, and once prepared the transaction's state is fully stored on disk and can be committed or rolled back from any session | documented behaviour (vendor) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The undo is the design: classify every step as idempotent / reversible / compensable / irreversible before choosing restart, compensation or human, and price the unwind with the measured 14.6× waste gap | 9 | 9 | 9 | 8 | 8.8 | **winner** |
| Idempotency keys are pruned at 24 hours, so a replay a day later is a new charge | 8 | 7 | 7 | 9 | 7.7 | dropped — re-argument: `2026-10-14_one-approval-two-payments` (multi_agent_enterprise_fabric) already owns this exact thesis and the 24-hour window |
| Two-phase commit exists in Postgres but ships disabled (`max_prepared_transactions` defaults to zero) | 7 | 9 | 7 | 6 | 7.4 | dropped — narrow and unmeasured on its own; kept as a supporting row instead (row 5 carries the identifier cap, the default-zero fact is stated in prose) |
| A workflow's event history caps at 51,200 events, so a long saga must checkpoint through Continue-As-New | 6 | 8 | 8 | 7 | 7.2 | dropped as a standalone — one vendor limit, no measured consequence; becomes row 4 inside the winner |
| Rolling back an LLM agent wastes an order of magnitude fewer steps than restarting | 8 | 8 | 9 | 6 | 7.9 | merged into the winner — it is the winner's strongest single figure, not a separate decision |

## Notes
- Row 1's evidence window opens on the sample (`n = 1,008`) and carries the 0.78 / 11.41 comparison inside the same excerpt; the 14.6× ratio is the paper's own arithmetic on those two waste figures, and it is restated in the paper's prose ("saving 14.6× on waste"). The quality difference between the two methods is not significant (CI [−0.27, +0.05]), which is the article's own caveat: unwinding does not buy better output, it buys the same output for less discarded work.
- Row 3's 22.2–23.4% transaction-control share is the honest cost side of the argument and belongs in the piece: pre-commit staging is not free, it moves cost from wasted steps into a control path.
- Row 5's gloss separates two pages: the 200-byte identifier cap is on the PREPARE TRANSACTION page cited; the default of `max_prepared_transactions` to zero is on the runtime-config page and is cited in the article's Sources, not led as a row because that page carries no figure this matcher can hold.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=4 hosts=3 decision="sha1:72e19ec5d9" dedup="matched a prior artifact: 2026-10-28_your-90-restart-monitor" window_days=180 checked_at=2026-11-04T17:33:22+00:00 -->
<!-- evergreen-gate:end -->
