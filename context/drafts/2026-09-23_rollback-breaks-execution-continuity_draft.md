---
title: "Rollback Is Not a Safety Net"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "A faithfully-restored checkpoint can resume an execution whose states and effects never coexisted in any valid history — checkpoint-and-rollback does not guarantee safe recovery."
date: 2026-09-23
slug: rollback-breaks-execution-continuity
---

<!-- lead -->
An agent is told to strip malware from a repository before release. It removes the payload, scans the cleaned code, and records a passing result. Then the release fails on some missing metadata, the operator hits rollback — and the tool restores the *pre-cleanup* files while the "verified" scan result survives in the agent's state. The malicious repo ships under a scan that was run on the version without the malware [1]. That is the first attack in "Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback" (arXiv:2608.29381, August 29, 2026), and it took no corrupted checkpoint to pull off — just a correct rollback.

<!-- tension -->
**Why it matters:** Checkpoint-and-rollback is the reliability cure the agent ecosystem is racing to ship. Durable-execution vendors now sell it as a product category, and frameworks like CRAB and DeltaBox optimize it specifically for agents [1]. The premise is sound on its face: long agent runs accumulate state and external effects that are expensive to rebuild after a crash, so you snapshot and resume. The problem is that a checkpoint only restores *some* of the state — the framework state, the workspace, or the OS/sandbox — and never the outside world. A sent payment, a forwarded email, a released artifact do not roll back with you.

**The big picture:** The paper's central finding is that "correct rollback does not imply secure recovery." A faithfully-restored checkpoint can resume an execution whose states, assumptions, and external effects never coexisted in any valid history [1]. That is the exact failure shape the compound-reliability crowd already knows: chain ten steps at 95% each and you land at roughly 59.9% end-to-end (0.95¹⁰). Checkpointing was supposed to fix that. It closes some gaps and opens five new ones.

**By the numbers:**
- **5 failure modes:** incomplete internal state coverage, inconsistent checkpoint state, external state mismatch, unbound nondeterministic replay, unrecorded external effects [1].
- **3 real attacks:** on Hermes, Cline, and LangGraph — enabling malware-verification bypass, unauthorized mail forwarding, and double payment [1].
- **1,735 executions:** across 347 benchmark traces from TerminalBench and AgentBench, over five representative checkpoint/rollback systems [1].
- **98.7% / 99.9% / 99.5%:** the paper's detection pipeline precision, recall, and accuracy for spotting these recovery failures [1].

<!-- tactical-insight -->
**The playbook:** Treat rollback as a partial restore with a known recovery boundary, not a time machine. Four moves cover most of the gap.

- **Map the recovery boundary before you trust it.** Ask what a checkpoint restores — framework state, workspace files, or a full sandbox — and what it doesn't. LangGraph snapshots graph state; Cline and Hermes snapshot workspace files; E2B snapshots the whole sandbox. Each leaves a different set of dependencies outside the boundary [1].
- **Make external side effects idempotent and recorded.** Double payment happens when a payment is an "unrecorded external effect" that a resumed run repeats. Idempotency keys and an append-only effect log mean replay can't double-charge [1][3].
- **Bind every validation to the exact artifact it checked.** The Hermes attack works because the "verified" label floats free of the files it was computed on. Pin the result to a hash of the workspace state it approved, so a rollback that changes the files invalidates the verification [1].
- **Kill nondeterminism in replay.** Pin seeds, model versions, and tool versions; log the nondeterministic inputs (timestamps, RNG, external responses) so a restored checkpoint re-executes the same way instead of drifting [1].

**The corroborating data:** a transaction-style harness (ACID-Agent) scores 90.0 against 75.2 for 3-majority Claude Code while spending ~60% of the tokens ($0.13 vs $0.21) — and removing its failed-step isolation drops the score 11.7%, because a failed step's contaminated state leaks into the next one [2]. Isolation and durability are doing real work, not ceremony.

<!-- nuanced-takeaway -->
**The catch:** Rollback is not the enemy — it is necessary, and this is not an argument to delete it. The failure is the assumption that a faithful restore equals a safe resume. Two honest caveats. First, this is a security paper: its three attacks are adversarial, but the underlying failure modes fire without an attacker too — a crash-and-resume that re-runs a payment is the same "unrecorded external effect" with no adversary in the loop. Second, covering the dependency set costs real engineering: you need effect logs, content hashing, and deterministic replay wired into a runtime that most teams bolt on after the fact. Until the recovery boundary is treated as an explicit design surface, rollback will keep restoring a state that never validly existed.

<!-- tldr -->
- **The Big Shift:** Checkpoint-and-rollback — the durability fix the whole agent industry is adopting — turns out to have its own failure surface. A new study shows five ways a *correct* rollback restores a state whose files, decisions, and outside effects never coexisted, and demonstrates three working attacks on Hermes, Cline, and LangGraph.
- **Why It Matters:** If rollback silently re-binds a "verified" result to an artifact it never checked, agents can ship malware as clean, forward email without authorization, or charge twice. The cost lands on anyone running autonomous agents against payments, mail, or releases.
- **The Winning Moves:**
  - **Map the recovery boundary:** know whether a checkpoint restores framework state, workspace files, or a full sandbox — and what stays outside it.
  - **Idempotent effects:** use idempotency keys and an append-only effect log so a resumed run can't re-charge a payment.
  - **Bind validation to the artifact:** hash the exact workspace a scan approved, so changing the files voids the result.
  - **Deterministic replay:** pin seeds and model/tool versions and log nondeterministic inputs.
- **The Catch:** The attacks are adversarial, but the failure modes also fire from a plain crash-and-resume, and the fixes (effect logs, content hashing, deterministic replay) are real engineering that most teams retrofit only after an incident.

## Sources
[1] "Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback" — arXiv:2608.29381 — https://arxiv.org/abs/2608.29381
[2] "Agentic Transaction: Towards ACID-Compliant Agent Systems" — arXiv:2608.13900 — https://arxiv.org/abs/2608.13900
[3] Diagrid, "Top 5 Mistakes Shipping AI Agents to Production in 2026" (Aug 31, 2026) — https://www.diagrid.io/infrastructure/top-5-mistakes-shipping-agents-production-2026

<!-- linkedin -->
Your agent checkpoint/rollback feature has a security hole no one is talking about. A paper out of arXiv (Aug 29) shows "correct rollback does not imply secure recovery": a faithfully-restored checkpoint can resume an execution whose files, decisions, and outside effects never coexisted. Three working attacks on Hermes, Cline, and LangGraph — malware shipped as "verified," unauthorized mail forwarding, and a double payment — none requiring a corrupted checkpoint. The fix isn't less rollback; it's treating the recovery boundary as a design surface: map what's inside vs. outside the snapshot, make external effects idempotent, bind validation to the exact artifact it checked, and pin nondeterminism. A transaction-style harness (ACID-Agent) hits 90.0 vs 75.2 for 3-majority Claude Code at ~60% of the tokens — and dropping its failed-step isolation costs 11.7%. Durable execution is necessary. It is not sufficient.
