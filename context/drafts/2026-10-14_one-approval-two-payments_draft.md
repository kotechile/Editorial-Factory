---
title: "One Approval, Two Payments: The 24-Hour Trap"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A checkpoint records progress, never effect identity: a parked approval answered by several processes fires the gated effect once per answer, and the payment layer's own key can be pruned after 24 hours — so a step that moves money needs a consume-once claim in a store outside the run."
date: 2026-10-14
slug: one-approval-two-payments
archetype: evergreen
evergreen: true
---

<!-- lead -->
Two workers answering one parked approval can fire the payment twice. In a controlled test across five agent frameworks, resuming the same paused interrupt from several processes fired the gated action once per caller. Every caller got through in 36 of 40 test cells, and the rate never dropped below 0.933 [1]. No two of the five behaved the same way, and none published a checkable rule for what a resume means [1].

<!-- tension -->

## The big picture:

The layer that stores checkpoints makes one promise. A run can stop for a human answer, then carry on.

It says nothing about work that already happened. Three frameworks give three clashing answers to that question. One says a restored run skips finished work. A second tells users to make everything before a wait safe to run again. A third keeps finished step results so it does not repeat them [1]. All three describe the same resume button.

Measured behavior then parts ways with the docs. One framework re-ran recorded work after a hard process kill. It was exactly-once across pauses and at-least-once across crashes, on one interface. Another re-ran finished steps that had already changed something, against its own written claim. A third could not resume at all after a crash mid-step [1].

A second study looked from the recovery side. A faithful rollback is not the same as a safe one. A restored checkpoint can resume a run whose state, assumptions and outside effects never existed together at any single moment [2].

My read is that the resume layer is being trusted for something it never claimed. A checkpoint marks progress. It is not a receipt for a payment.

**Why it matters:** An effect that fires twice is money, a duplicate ticket, or a second email to a customer. The resume layer will not stop it, because that layer never tracked the effect.

## By the numbers

- **36 of 40 cells — Concurrent resume duplicates:** One paused approval, resumed by several processes, fired the gated effect once per caller. The rate hit 1.0 in 36 of 40 cells and never fell below 0.933, on both durable backends [1].
- **67.2% and 67.7% — Faults found on resume:** Missing internal state and unbounded replay were the most common failures across five systems that save and restore agent runs, on two test suites. Unrecorded outside effects showed up in just 2.3% [2].
- **51,200 events — Journal ceiling:** One workflow's event history is capped at 51,200 events or 50 megabytes, with a warning after 10,240 events or 10 megabytes. Unfinished operations are capped at 2,000 per type [3].
- **24 hours — Payment key life:** A key that stops a repeat charge can be pruned once it is at least 24 hours old. A request that reuses a pruned key is treated as brand new [5].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that the fix for the double charge is small and boring, and it sits outside the framework. The same team shipped a gate that marks the answer as used, in a store both workers can see, before any step runs. It served one caller and refused the rest, where the stock saver duplicated {2:10} against the gate's {1:10} [1].

- **Who consumes the approval:** The claim lives in shared storage, so the second answer is refused before any step runs. That is the whole difference between the two measured results [1].
- **How long the pause may ride:** The payment layer has its own clock. A key can be gone after 24 hours. A run parked overnight, or over a weekend, can retire its own protection and turn a retry into a second charge [5]. The engines bound the other end: 2,000 unfinished operations of each type per run, a 256 KiB (a quarter of a megabyte) cap on what one step may carry, and a 25,000-event history that fails a run outright [3][4].
- **What the tests measure:** The harness makes no model calls and uses no timing windows. The duplication is a property of the storage interface itself, not of a slow network or a clever prompt [1].

I keep coming back to how much of this is a naming problem. A step that is safe to repeat is a different animal from a step that moves money. The resume layer treats both the same way.

<!-- nuanced-takeaway -->

## The catch

The limits of the evidence matter here, and the authors state most of them. Their checkers are process counters and a file on disk, not a live payment system. The tests cover one workflow shape per framework. They do not measure how often the failure happens in production [1].

The frameworks can change. The paper says outright that single bugs may be patched upstream, and two already were. So it rests its case on the contract and on pinned versions, not on any one bug's lifespan [1].

The second study shows why this hides so well. Unrecorded outside effects appeared in only 2.3% of the runs it checked. Most test tasks work on local files, databases or pretend systems. Few of them make a lasting change through an outside service [2]. So a green test suite can say nothing about the one step that moves money.

The part I keep circling is the desk's own field note, which predates both papers. A four-agent purchasing pipeline sent orders straight into an enterprise system that holds the company's records, with no coordinator. Then $410,000 in phantom stock had to be reversed by hand [6]. The run recovered. The orders did not.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent frameworks save checkpoints and resume runs, but they never agreed on what a resume does to work that already happened. The measurements show finished effects firing again.
- **Why It Matters:** A duplicate payment, ticket or email is a real cost, and the layer teams trust to stop it was never built to track effects at all.
- **What I'd Watch:** Whether teams move the "already used" mark out of the workflow and into shared storage, and how they size the pause. Three things decide it:
  - **Consume-once claim:** A shared record that one answer to a pause has been used, checked before any step runs, so a second caller is refused.
  - **Pause against key life:** The payment layer's own key can be gone after 24 hours, so a long human pause can leave a retry unprotected.
  - **Engine ceilings:** Limits on unfinished operations, payload size and history length decide how long and how large one parked run may be.
- **The Catch:** The evidence comes from lab harnesses on one workflow shape per framework, not from production rates, and the frameworks keep changing under the contract.

## Sources
[1] Sajjad Khan, "Resume Means Resume: A Machine-Checked Conformance Contract for Checkpoint, Interrupt, and Resume Semantics in Workflow Persistence Layers" (arXiv:2608.03836v1, 2026-08-04) — five frameworks at pinned releases: consume-once fails under concurrent delivery (the gated effect fires once per consumer, saturation 1.0 in 36 of 40 cells, never below 0.933; two racers on separate hosts duplicate in 10/10 repetitions); the opt-in gate claims consumption in the shared store and serves one racer ({1:10} against the stock saver's {2:10}); LangGraph 1.2.9 re-executes durably recorded work after a real SIGKILL, CrewAI 1.15.2 re-executes completed effect-bearing methods, pydantic-graph 1.x cannot resume after a mid-node crash; no two probed frameworks share a conformance profile; the authors state individual violations may be patched upstream (https://arxiv.org/html/2608.03836v1)
[2] Guanlong Wu, Dahui Li, Ke Jiang, Jianyu Niu, Cong Wang and Yinqian Zhang, "Safe to Resume? Breaking Execution Continuity of Agent Execution via Rollback" (arXiv:2608.29381v1, 2026-08-29) — the most prevalent failures are incomplete internal state coverage (67.2%) and unbound nondeterministic replay (67.7%), with unrecorded external effects at 2.3%; five representative agent checkpoint/rollback systems across AgentBench and TerminalBench; three end-to-end attacks, including a duplicate payment under one approval (https://arxiv.org/html/2608.29381v1)
[3] Temporal Technologies, "Workflow Execution limits" (documentation) — the Workflow Execution's event history is limited to 51,200 events or 50 MB, warns after 10,240 events or 10 MB, and incomplete Activities, Child Workflows, Signals or Cancellation requests are capped by default at 2,000 per type (https://docs.temporal.io/workflow-execution/limits)
[4] Amazon Web Services, "Step Functions service quotas" (AWS Step Functions Developer Guide) — maximum input or output size for a task, state or execution is 256 KiB; a standard execution's history is capped at 25,000 events and the execution fails at that quota; maximum execution time is 1 year (https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html)
[5] Stripe, "Idempotent requests" (API reference) — for API v1, keys can be removed once they are at least 24 hours old, and "We generate a new request if a key is reused after the original is pruned" (https://docs.stripe.com/api/idempotent_requests)
[6] Field notes — context/growth_os/customer-truth.md §`multi_agent_enterprise_fabric` Anecdote 1: a four-agent procurement pipeline committed purchase requisitions into SAP S/4HANA with no distributed saga coordinator, causing $410,000 in phantom inventory allocations before manual reversal

## Gate report
- lead: PASS — Delivers the duplicate-payment finding and its measured rate in the first two sentences, with no preamble.
- tension: PASS — Names what a checkpoint does and does not track, contrasts the documented answers with the measured behaviour, and keeps paragraphs short.
- tactical-insight: PASS — Reports what the researchers shipped and what the engines bound, as observations rather than instructions, with an observer cue.
- nuanced-takeaway: PASS — States the harness limits, the patching risk and the 2.3% outside-effect rate honestly, and closes on the desk's own field note.
- tldr: PASS — Four-part structure with a plain definition for each item the writer is watching.
