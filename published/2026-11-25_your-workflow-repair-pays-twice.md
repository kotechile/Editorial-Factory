---
title: "Why Your Workflow Repair Pays Twice: 12 Calls vs 7"
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
meta_title: "Why Your Workflow Repair Pays Twice: 12 Calls vs 7"
meta_title_source: "derived_from_title"
meta_description: "A workflow repair that pays again for calls which already ran is not bad luck. It is the promised behavior of durable execution — a runtime that saves each…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-workflow-repair-pays-twice/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Workflow Repair Pays Twice On Replay. An industrial reel-to-reel data recorder mid-replay in a dark control room, a sealed fresh tape spool"
image_caption: "Workflow Repair Pays Twice On Replay: Replay re-bills paid calls or serves stale results; identity checks take milliseconds."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A workflow repair that pays again for calls which already ran is not bad luck. It is the promised behavior of durable execution — a runtime that saves each step and, after a crash, re-runs its record instead of calling your providers again. A study published 4 November 2026 measures what that guarantee is worth, and where it fails [1]. When a model fixes a workflow that died partway through, the fix either re-bills the calls that ran fine — on one live job, 12 paid image calls where 7 were needed — or it serves a stale result whose inputs the model had already changed, and calls the run a success. A contract stamped on each call's identity closes both holes. The checks take milliseconds.

<!-- tldr -->
## At a glance

When a model-written agent workflow fails after some calls have been paid for, the repair itself can re-bill that work or serve a replaced artifact. A 4 November 2026 study defines a call-identity contract that stops both, and puts a price on it.

<!-- tension -->
## Replay remembers events, not intent

Durable execution offers a deal smaller than it sounds. The runtime saves what happened, and on resume it serves those saved results rather than calling out again. Amazon Web Services (AWS) documents the terms for its Step Functions service plainly: Standard Workflows are exactly-once, a task never runs twice unless Retry is specified, and the full run history stays retrievable for 90 days [5]. Temporal, the other major durable engine, states the same idea as a size rather than a promise: an execution's event history is capped at 51,200 events or 50 megabytes, with a warning at 10,240 [6]. What neither engine promises is that a saved result still matches what you now mean. That gap opens when the code itself needs fixing, and a study by Chenyang Jiang, Benyang Pan and Puqu Wu names both ways it costs you [1].

The first failure mode arrives through the front door. Five of six image calls in a fanout have been paid for; the sixth fails. The natural repair — show the model the error, let it rewrite the script — re-issues calls one through five, because the rewritten script cannot prove those calls are the same calls. The second mode is quieter. The model edits a paid payload in place, a prompt or a seed, and the replay engine returns the saved result anyway. The run completes with the replaced artifact, and nobody is told. I read the paper's examples twice before accepting that the second mode is the more expensive one: it never raises an error, so the wrong output ships as a success.

The fix is an identity stamped on each call, built from three parts: the callsite, meaning the exact place in the code where the call sits, plus its fanout position and its occurrence count within the run [2]. A rewrite that leaves the call in place keeps its name, so the paid names form a frozen prefix — the code around a frozen call stays writable [2]. Three checks enforce the rule [3]. A static gate rejects, before any container starts, a rewrite that would change a paid call. A runtime digest stops a changed payload at a paid identity. An occurrence ledger flags a payload about to be paid twice. Under the paper's three stated assumptions, a rewrite that passes the gate replays every paid call it makes, spends only on new work, and reports the names it skips [4].

## By the numbers

- **258 paid calls:** What 22 gate-passed repairs replayed across media jobs, with zero duplicate executions [1].
- **7 paid calls:** What a live six-way image fanout cost once the repair replayed its five paid calls, instead of 12 [1].
- **1.19 extra fixes:** The measured repair overhead, at 17.2 seconds per fix [1].

<!-- tactical-insight -->
## What the field does today

The savings are the small half of this study. What I keep returning to is the crash window, because it is where the contract earns its keep. The system writes an attempt record before it sends a call out. The process can die in that gap. When it does, the run fails closed: it raises an error, produces no silent duplicate, and waits for an operator to decide. If the operator declares the attempt abandoned, at most k effects repeat per crash [8]. The window is bounded, not closed — and the bound is a human decision.

The nearest thing in production today is Temporal's patching path. An author marks calls with patched() and deprecate_patch(), old code keeps answering existing executions, and new code takes over from there [7]. Temporal planned to remove the older worker-versioning method from its server in March 2026 [7]. AWS puts the burden on the caller for Express Workflows, which may run more than once, and its documentation steers users toward actions that are safe to repeat [5]. Both are habits an author maintains by hand. Both sit one careless rewrite away from the failure modes above. The contract makes the property mechanical instead. One boundary is already settled elsewhere: what the failure message itself may name — [what the error text can promise a repair](/your-error-text-breaks-the-repair/) — decides whether the agent can attempt a recovery at all, while this contract decides what that attempt may replay.

<!-- nuanced-takeaway -->
## The catch

The evidence is one study, not a census. Its repairs ran on media workflows and a twelve-task support set, on a platform whose broker approves every call. Twenty-two repairs and one live fanout establish the direction, not a fleet-wide saving. The guarantee also holds only under the paper's three stated assumptions [4], so any team porting the idea should re-derive them for its own runtime rather than trusting the numbers to travel. And identity has a floor that no design removes: no identity can both survive a call being moved and avoid wrong reuse, so moving a paid call to a new place in the code stops the run before any spend [2]. The move is caught, but it waits for a human. My reading, held loosely, is that the trade is the honest one. The price of never paying twice is that some repairs need a person to say yes.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "MCP Skills Extension" -> /mcp-skills-extension/ [same site (aichieve.net); same category; topical overlap: workflow] Link "MCP Skills Extension" in the section where the article touches workflow. -->
<!-- internal-link hint: "Your Error Text Breaks the Repair" -> /your-error-text-breaks-the-repair/ [same site (aichieve.net); same category; topical overlap: repair] Link "Your Error Text Breaks the Repair" in the section where the article touches repair. -->
<!-- internal-link hint: "Your Planner Is Not Your Model" -> /your-planner-is-not-your-model/ [same site (aichieve.net); same category; topical overlap: workflow] Link "Your Planner Is Not Your Model" in the section where the article touches workflow. -->
## Related reading

- [MCP Skills Extension](/mcp-skills-extension/) — more on Autonomous & Agentic Workflows
- [Your Error Text Breaks the Repair](/your-error-text-breaks-the-repair/) — more on Autonomous & Agentic Workflows
- [Your Planner Is Not Your Model](/your-planner-is-not-your-model/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources

- [1] Chenyang Jiang, Benyang Pan, Puqu Wu, "Call-Level Revision Contracts for LLM-Authored Workflows", arXiv:2611.06967v1, 4 Nov 2026 — https://arxiv.org/html/2611.06967v1
- [2] Same study, identity definition and frozen prefix — https://arxiv.org/html/2611.06967v1
- [3] Same study, static gate, runtime digest and occurrence ledger — https://arxiv.org/html/2611.06967v1
- [4] Same study, the replay guarantee under three assumptions — https://arxiv.org/html/2611.06967v1
- [5] AWS, "Choosing workflow type in Step Functions", retrieved 2026-11-25 — https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html
- [6] Temporal Technologies, "Workflow Execution limits", retrieved 2026-11-25 — https://docs.temporal.io/workflow-execution/limits
- [7] Temporal Technologies, "Versioning" (Python SDK), retrieved 2026-11-25 — https://docs.temporal.io/develop/python/versioning
- [8] Jiang, Pan, Wu, crash-window protocol, arXiv:2611.06967v1 — https://arxiv.org/html/2611.06967v1
