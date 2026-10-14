---
title: "One Approval, Two Payments: The 24-Hour Trap"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A checkpoint records progress, never effect identity: a parked approval answered by several processes fires the gated effect once per answer, and the payment layer's own key can be pruned after 24 hours — so a step that moves money needs a consume-once claim in a store outside the run."
date: 2026-10-14
slug: one-approval-two-payments
archetype: evergreen
evergreen: true
meta_title: "One Approval, Two Payments: The 24-Hour Trap"
meta_title_source: "derived_from_title"
meta_description: "One paused approval answered by two workers can fire two payments."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/one-approval-two-payments/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "The Double Payment Trap. Isometric cutaway of a hardware routing bay where one input splits into two output lanes bypassing a"
image_caption: "The Double Payment Trap: How resuming paused approvals fires duplicate payments."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
One paused approval answered by two workers can fire two payments. In a test across five agent frameworks, resuming the same pause from several processes fired the action once per caller [1]. Every caller got through in 36 of 40 cells, and the rate never fell below 0.933 [1]. The second window is the payment key itself, which can be dropped once it is 24 hours old [5]. No two of the five frameworks behaved the same way, and none published a checkable rule for what a resume means for work already done [1].

<!-- tension -->

## The big picture:

The layer that stores checkpoints makes one promise. A run can stop for a human answer, then carry on.

It says nothing about work already done. Three frameworks give three clashing answers to that gap [1]. One says a restored run skips finished work. A second tells users to make all work before a wait safe to run again.

A third keeps finished step results so it does not repeat them [1]. All three describe the same resume button — and that is the trap.

What the tests show differs from the docs. One framework re-ran recorded work after a hard kill [1]. It ran exactly once across pauses and at least once across crashes, on one interface. Another re-ran finished steps that had already changed outside systems, against its own written claim. A third could not resume at all after a crash mid-step [1].

A second study looked from the recovery side. A faithful rollback is not always a safe one. A restored checkpoint can resume a run whose state and outside effects never existed together at any one moment [2].

My read: teams trust the resume layer for a job it never claimed. A checkpoint marks progress. It is not a receipt for a payment.

**Why it matters:** An effect that fires twice means a duplicate charge, a second ticket, or a repeated email. The resume layer will not stop it, because that layer never tracked the effect.

## By the numbers

- **36 of 40 cells — Concurrent resume duplicates:** One paused approval, resumed by several processes, fired the gated effect once per caller. The rate hit 1.0 in 36 of 40 cells and never fell below 0.933 on both storage backends [1].
- **67.7% — Uncontrolled replay:** Missing state and uncontrolled replay were the most common faults in five systems that save and restore runs. Unrecorded outside effects showed up in just 2.3% of checks [2].
- **51,200 events — Journal ceiling:** One engine caps a run's event history at 51,200 events or 50 megabytes, with a warning at 10,240 events. Unfinished operations are capped at 2,000 per type [3].
- **24 hours — Payment key life:** A key that stops a repeat charge can be removed once it is at least 24 hours old. A request that reuses a pruned key looks new to the processor [5].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that the fix for the double charge sits outside the framework. The same team shipped a gate that marks the answer as used in a shared store before any step runs [1]. It served one caller and refused the rest, where the stock saver let both through [1].

- **Who consumes the approval:** The claim lives in shared storage, so the second answer is refused before any step runs. This is the whole difference between the two measured results [1].
- **How long the pause rides:** The payment layer has its own clock, and a key can disappear after 24 hours [5]. A run parked over a weekend can lose its cover and turn a retry into a second charge [5]. Engines enforce their own limits: 2,000 unfinished operations per type, a 256 KiB cap on what one step may carry, and a 25,000-event history limit [3][4].
- **What the tests measure:** The test harness makes no model calls and uses no timing windows. The repeat is a flaw in the storage interface itself, not a slow network or a clever prompt [1].

I keep coming back to the wording. A step that is safe to repeat is a different animal from a step that moves money. The resume layer treats both the same way.

<!-- nuanced-takeaway -->

## The catch

The limits of the evidence matter here, and the authors state them clearly. Their checkers use process counters and a file on disk, not a live payment system [1]. The tests cover one workflow shape per framework. They do not measure how often this happens in production [1].

The frameworks also change fast. The paper notes that single bugs may be patched upstream, and two already were [1]. So the findings rest on the contract and on pinned versions, not on one bug's life [1].

The second study shows why this flaw hides so well. Unrecorded outside effects appeared in only 2.3% of the runs it checked [2]. Most test tasks work on local files, databases or pretend systems.

Few make a lasting change through an outside service [2]. A green test suite says nothing about the one step that moves real money.

The part I keep circling is a field note that predates both papers. A four-agent buying pipeline sent orders straight into the system that holds the company's records, with no coordinator. It created $410,000 in phantom stock that had to be reversed by hand [6]. The run recovered. The orders did not.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Retry Is the Bug: An Agent’s Costliest Failure Mode" -> https://giniloh.com/retry-is-the-failure-amplifier/ [same site (giniloh.com); same category; topical overlap: payments] Link "Retry Is the Bug: An Agent’s Costliest Failure Mode" in the section where the article touches payments. -->
<!-- internal-link hint: "270 Attacks: Your Green Tests Are Blind" -> https://giniloh.com/one-skill-too-many-green-test/ [same site (giniloh.com); same category] Link "270 Attacks: Your Green Tests Are Blind" in the section where the article touches this topic. -->
<!-- internal-link hint: "Agent Memory Poisoning" -> https://giniloh.com/agent-memory-poisoning-write-path/ [same site (giniloh.com); same category] Link "Agent Memory Poisoning" in the section where the article touches this topic. -->
## Related reading

- [Retry Is the Bug: An Agent’s Costliest Failure Mode](https://giniloh.com/retry-is-the-failure-amplifier/) — more on Autonomous & Agentic Workflows
- [270 Attacks: Your Green Tests Are Blind](https://giniloh.com/one-skill-too-many-green-test/) — more on Autonomous & Agentic Workflows
- [Agent Memory Poisoning](https://giniloh.com/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent frameworks save checkpoints and resume runs, but they never agreed on what a resume does to past work. Tests show finished effects firing more than once.
- **Why It Matters:** A duplicate payment, ticket, or email carries a real cost. The layer teams trust to stop repeats was never built to track outside effects.
- **What I'd Watch:** Whether teams move the "already used" mark out of the workflow and into shared storage, and how they size the pause. Three things decide it:
  - **Consume-once claim:** A shared record that one answer to a pause has been used, checked before any step runs, so a second caller is refused.
  - **Pause against key life:** The payment layer's own key can expire after 24 hours, leaving a long pause uncovered during a retry.
  - **Engine ceilings:** Limits on unfinished tasks, payload size, and history length decide how long and how large one parked run may be.
- **The Catch:** The evidence comes from lab tests on one workflow shape per framework, not from live production, and the tools underneath change fast.

## Sources
[1] Sajjad Khan, "Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers" (arXiv:2608.03836v1, 2026-08-04) — five frameworks at pinned releases: consume-once fails under concurrent delivery (the gated effect fires once per consumer, saturation 1.0 in 36 of 40 cells, never below 0.933; two racers on separate hosts duplicate in 10/10 repetitions); the opt-in gate claims consumption in the shared store and serves one racer ({1:10} against the stock saver's {2:10}); LangGraph 1.2.9 re-executes durably recorded work after a real SIGKILL, CrewAI 1.15.2 re-executes completed effect-bearing methods, pydantic-graph 1.x cannot resume after a mid-node crash; no two probed frameworks share a conformance profile; the authors state individual violations may be patched upstream (https://arxiv.org/html/2608.03836v1)
[2] Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang and Yinqian Zhang, "Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback" (arXiv:2608.29381v1, 2026-08-29) — the most prevalent failures are incomplete internal state coverage (67.2%) and unbound nondeterministic replay (67.7%), with unrecorded external effects at 2.3%; five representative agent checkpoint/rollback systems across AgentBench and TerminalBench; three end-to-end attacks, including a duplicate payment under one approval (https://arxiv.org/html/2608.29381v1)
[3] Temporal Technologies, "Workflow Execution limits" (documentation) — the Workflow Execution's event history is limited to 51,200 events or 50 MB, warns after 10,240 events or 10 MB, and incomplete Activities, Child Workflows, Signals or Cancellation requests are capped by default at 2,000 per type (https://docs.temporal.io/workflow-execution/limits)
[4] Amazon Web Services, "Step Functions service quotas" (AWS Step Functions Developer Guide) — maximum input or output size for a task, state or execution is 256 KiB; a standard execution's history is capped at 25,000 events and the execution fails at that quota; maximum execution time is 1 year (https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html)
[5] Stripe, "Idempotent requests" (API reference) — for API v1, keys can be removed once they are at least 24 hours old, and "We generate a new request if a key is reused after the original is pruned" (https://docs.stripe.com/api/idempotent_requests)
[6] Field notes — context/growth_os/customer-truth.md §`multi_agent_enterprise_fabric` Anecdote 1: a four-agent procurement pipeline committed purchase requisitions into SAP S/4HANA with no distributed saga coordinator, causing $410,000 in phantom inventory allocations before manual reversal

## Gate report
- lead: PASS — Plainly states the double-payment risk and the measured rate in short sentences, with no preamble.
- tension: PASS — Names what a checkpoint does and does not track, contrasts three documented answers with the measured behaviour, and keeps paragraphs short.
- tactical-insight: PASS — Reports what the researchers shipped and what the engines bound, as observations rather than instructions, with an observer cue.
- nuanced-takeaway: PASS — States the harness limits, the patching risk and the 2.3% outside-effect rate honestly, and closes on the desk's own field note.
- tldr: PASS — Four-part structure with a plain definition for each item the writer is watching.
