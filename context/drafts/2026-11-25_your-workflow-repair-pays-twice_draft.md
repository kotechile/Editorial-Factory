---
title: "Why Your Workflow Repair Pays Twice: 12 vs 7"
vertical: multi_agent_enterprise_fabric
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
primary_keyword: "workflow repair"
secondary_keywords: ["durable execution", "replay", "idempotency", "agent workflow"]
one_big_thing: "A durable engine's replay keeps the old record, not your new intent: the natural repair of a failed agent workflow re-pays calls that already ran, or silently serves a replaced artifact — a call-identity contract closes both for milliseconds of checking."
date: 2026-11-25
slug: your-workflow-repair-pays-twice
---

<!-- lead -->

A repair that pays again for calls which already ran is not bad luck. It is what the replay layer of a durable execution engine guarantees — a runtime that saves each step and re-runs its recorded history after a crash. A study published 4 November 2026 measures both failure modes [1]. When a model fixes a workflow that died partway through, the fix either re-pays calls that succeeded — on one live job, 12 paid image calls instead of 7 — or serves an old result whose inputs the model had changed. A contract that checks each call's identity closes both holes, and the checks take milliseconds.

<!-- tldr -->
## At a glance

Teams that run model-written workflows on durable runtimes face a repair call the engine will not make. A fix may re-bill work that already ran, or serve a replaced artifact and call the run a success. A new study defines the contract that closes both, and the checks cost milliseconds.

<!-- tension -->
## Replay remembers events, not intent

Durable execution is a pattern. The runtime saves its state after each task, and on resume it serves the saved results instead of calling the provider again. Amazon Web Services (AWS) documents the bargain plainly. Standard Workflows are exactly-once: a task never runs twice unless Retry is specified, and the full run history stays retrievable for 90 days [5]. Temporal states the same idea as a size, not a promise: the event history is capped at 51,200 events or 50 megabytes, with a warning at 10,240 [6].

Both failure modes appear when the code itself needs fixing, and a study by Chenyang Jiang, Benyang Pan and Puqu Wu names them [1]. In the first, five of six image calls are paid for and the sixth fails. The natural fix is to show the model the error and let it rewrite the script. The rewritten script then re-issues calls one through five, because it cannot prove those calls are the same ones. In the second mode, the model edits a paid payload in place — a prompt, a seed. The replay engine returns the recorded result. The run then succeeds with the replaced artifact, and nobody notices.

The paper's fix is an identity stamped on each call, built from three parts: the callsite — the exact place in the code where the call sits — its fanout position, and its count within the run [2]. A rewrite that leaves the call in place keeps the identity, so paid identities form a frozen prefix: the frozen unit is the call itself, and the code around it stays writable [2]. Three checks enforce the rule [3]. A static gate rejects a rewrite that would change a paid call before any container starts. A runtime digest stops a changed payload at a paid identity. And an occurrence ledger flags a payload that is about to be paid twice. Under its stated assumptions, a candidate that passes the gate replays every paid call it invokes, runs only new work, and reports the identities it skips [4].

## By the numbers

- **258 committed calls:** What 22 gate-passed repairs replayed across media workflows, with zero duplicate executions [1].
- **7 paid calls:** What a live six-way image job cost once the repair replayed the five calls that had already committed [1].
- **1.19 extra rewrite attempts:** The measured repair overhead, at 17.2 seconds per rewrite [1].

<!-- tactical-insight -->
## What to watch

The overhead is not the argument. The savings are the small half of this study. What I find sharper is the crash window. The system writes an attempt record before it sends a call out. The process may die in that gap. The run then fails closed: it raises an error, produces no silent duplicate, and waits for an operator to decide. If the operator declares the attempt abandoned, at most k effects repeat per crash [8]. The window is bounded, not closed, and the bound is a human decision.

The same idea, half-built, is what I see closest to the field. Temporal's supported path for changing a running workflow is a patch: the author marks calls with patched() and deprecate_patch(), old code keeps answering them, and new code replaces them [7]. Temporal planned to drop the older worker-versioning method from its server in March 2026 [7]. AWS puts the burden on the caller for Express Workflows, which may run more than once. Its documentation steers users toward actions that are safe to repeat [5]. Hand-built patching and caller-side safe-to-repeat calls both sit one rewrite away from the two failure modes. The contract makes the property mechanical instead. The failure reply that starts the repair loop has its own rule — [what the error text may name](/your-error-text-breaks-the-repair/) decides whether the agent can even attempt a recovery — while the contract decides what that attempt may replay.

<!-- nuanced-takeaway -->
## The catch

The evidence is one study, not a census. Its repairs run on media workflows and a twelve-task support set. The platform itself has a broker that approves every call. Twenty-two repairs and one live fanout establish the direction, not a fleet-wide saving. The guarantee also holds only under the paper's three stated assumptions. Identity has a floor. No identity can both survive moving a call and avoid wrong reuse, so moving a call to a new place in the code stops the run before any spend [5]. The move is caught, but it waits for a human — which is the honest price of never paying twice.

## Sources

- [1] Chenyang Jiang, Benyang Pan, Puqu Wu, "Call-Level Revision Contracts for LLM-Authored Workflows", arXiv:2611.06967v1, 4 Nov 2026 — https://arxiv.org/html/2611.06967v1
- [2] Same study, identity definition and frozen prefix — https://arxiv.org/html/2611.06967v1
- [3] Same study, static gate, runtime digest and occurrence ledger — https://arxiv.org/html/2611.06967v1
- [4] Same study, the replay guarantee under three assumptions — https://arxiv.org/html/2611.06967v1
- [5] AWS, "Choosing workflow type in Step Functions", retrieved 2026-11-25 — https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html
- [6] Temporal Technologies, "Workflow Execution limits", retrieved 2026-11-25 — https://docs.temporal.io/workflow-execution/limits
- [7] Temporal Technologies, "Versioning" (Python SDK), retrieved 2026-11-25 — https://docs.temporal.io/develop/python/versioning
- [8] Jiang, Pan, Wu, crash-window protocol, arXiv:2611.06967v1 — https://arxiv.org/html/2611.06967v1
