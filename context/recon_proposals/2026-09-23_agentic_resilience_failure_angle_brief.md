# Angle Brief: agentic_resilience_failure — 2026-09-23

**Winner:** Checkpoint-and-rollback, the reliability cure everyone is shipping, is itself a security failure surface — five distinct ways a "faithful" rollback restores a state that never validly existed.

**Scores:** N=9 A=9 S=9 → Composite=9.0

**Hook:** A security paper dropped August 29 that walks three real frameworks — Hermes, Cline, and LangGraph — through end-to-end attacks that let a rollback reship malware as "verified," forward email without authorization, and double a payment. Not one attack requires corrupting a checkpoint. "Correct rollback does not imply secure recovery."

**Tension:** Durable execution is 2026's hottest reliability trend — Diagrid Catalyst, Temporal, DBOS, AWS Lambda Durable Functions, Microsoft Durable Task all sell checkpoint/resume as the answer to agent flakiness. Teams are adopting rollback wholesale to fix the compound-reliability problem (0.95^10 ≈ 59.9%). But the paper shows a checkpoint only restores *part* of the state: the framework state, the workspace, or the OS/sandbox — never the outside world. External side effects (a sent payment, a forwarded email, a released artifact) don't roll back with you. So rollback can re-bind a security decision to an artifact it never actually validated.

**Target reader:** infra_engineer

**Single claim to defend:** Rollback/checkpointing in agent systems does not guarantee safe recovery — there are five distinct, exploitable failure modes that let a correctly-restored checkpoint continue an execution whose states and effects never coexisted in any valid history.

**Runner-ups + why rejected:**
- *Agentic Transaction / ACID-Agent (arXiv:2608.13900, 8.5-worthy)* — strong, fresh, and squarely on the transactional angle (90.0 vs Claude Code 75.2, +10.6%), but it is a *positive* "here's a framework that works" result. Lower contrarian edge than the winner, which flips the field's own cure into a liability. Held as a corroborating secondary (its "semantic durability / failed-step isolation" findings reinforce the winner's thesis).
- *Diagrid "Top 5 Mistakes" (Aug 31)* — rich practitioner numbers (Inngest: 74% incident rate, 0% scale confidence) but vendor-authored secondary; the load-bearing primary is the arXiv paper. Kept as "why now" corroboration.
- *Provenance Integrity (arXiv:2608.12761)* — in-window and relevant, but narrower (audit/provenance) and no attack demonstration; folded into the durability discussion.
- All other candidates (memory poisoning June, context contamination July, error-cascade March, Microsoft taxonomy April, fault characterization March) are **out of window** and dropped per the 30-day freshness gate.
