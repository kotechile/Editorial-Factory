---
title: "Your Agent's 84,000-Write Mistake"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A long-running agent commits facts it read minutes ago, so the useful question is not whether the record moved but whether the change voids the decision — and the cheap fix is to record the premises the decision used and recheck exactly those at commit."
date: 2026-10-21
slug: agent-writes-stale-basis
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/agent-writes-stale-basis/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Fixing Stale Agent Writes. A modular mechanical inspection gate checking aligned verification pins on a brushed steel"
image_caption: "Fixing Stale Agent Writes: Rechecking decision premises stops invalid agent writes."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your agent reads a record, thinks for a minute, then writes. The write is the mistake. It ignores everything that changed in that minute. Both obvious fixes fail: blocking every change threw away 84,000 safe changes, and letting them land released 126,000 invalid effects [2][3].

A refund agent shows the trap. It reads an order, decides the buyer is owed 80 pounds, and parks the payment for approval. Before that approval clears, a human pays the same claim, or the agent's spending limit drops from 100 to 50. The logic was sound when it ran, but it is wrong when it commits [1].

A third option works better. A system that rechecks only the facts the decision relied on passed the same tests. It checked 0.6 conditions per change instead of 6.0 [4].

<!-- tension -->

## The big picture:

My read on the research is simple: a version number tells you a record moved, but it cannot tell you if the change actually matters [1].

A buyer's display name can change and leave the refund perfectly valid. The spending limit can drop to 50 and void the whole action. A database sees the first fact, but it has no way to judge the second.

Researchers are finally mapping how shared state breaks across agents. One paper names four traps in shared state. They are stale generation (a read that outlives the moment it was taken), a phantom tool (one that no longer exists), a causal cascade, and tool-effect reordering [6]. Another study ran a benchmark and found 67.1% of that benchmark's failures came from agents colliding over shared state [9].

The first paper also reproduces one of these failures in a live app. It traces a silent overwrite to an open issue in ByteDance's deer-flow and shows the fix [8].

The clock makes these crashes worse. An action often sits in a message bus before it reaches the core system. Amazon EventBridge retries a failed delivery for 24 hours and up to 185 times [10]. A message sits in Amazon Simple Queue Service (SQS) for four days by default [11]. A write computed on Monday can easily land on Thursday.

## By the numbers

- **84,000 — Safe changes lost:** Blocking every stale write stopped bad effects. It also threw out all 84,000 safe changes in the run. It matched the exact outcome in just 20% of the ten test cells [3].
- **0.6 vs 6.0 — Checks per change:** Rechecking only the decision's own premises cost 0.6 checks per resumed change. A full rescan cost 6.0 [4].
- **67.1% — Shared state failures:** One benchmark found 37.2% of agents submitted too early, and 29.9% failed to agree. Both read as missing coordination [9].
- **8% — Token overhead:** Snapshot isolation added about 8% more tokens on one workload. The authors call that far short of the penalty teams assume [7].

<!-- tactical-insight -->

## What I'd watch:

The design the study lands on moves the check to commit time. It also shrinks what that check covers. What I would look for in a review:

- **A premise record beside the action:** The system writes down the facts the decision used. The order is delivered, the defect is real, the limit is 100. Those notes live with the pending action [1].
- **A check at commit:** The system compares the stored versions against those notes right when the effect fires. A slow approval queue cannot let a stale decision through [1].
- **Granularity below the row:** The system checks field-level conditions. This lets it accept a name change but reject a limit change on the exact same record [1].
- **One run per hot entity:** Pinning an order or vendor to one durable execution forces events into a strict line. Temporal caps these waiting signals at 2,000 per execution by default [12].

The cost of stopping these errors is smaller than teams think. Locking ran 1.6 to 2.3 times the baseline, and snapshot isolation about 8% more tokens [7]. Neither price is the order-of-magnitude penalty teams assume.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that this is a controlled design study, not a messy field report. Its long tests run no language model at all. The authors say the results show controlled feasibility, not proof it holds in production [5].

The system does not pull these conditions out on its own, either. A person still has to teach the fabric which fields matter to which decision.

The 60.0% needs the same grain of salt. The study built five changes per scenario, and made 60% of them void the decision on purpose [2]. It proves the failure is real. It does not say how often your own systems will hit it.

What holds either way is narrower than a database lock. A version number says something moved. It does not say whether the move mattered. The check that survives asks the second question.

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent reads a record, thinks for a minute, then writes. Anything that changed in that gap is invisible to the write. Obvious database locks either let bad writes land or kill safe ones.
- **Why It Matters:** The wrong fix costs money. An unchecked write released 126,000 invalid effects. A total block threw out 84,000 safe changes [2][3]. Systems that touch payments or employee records pay for both mistakes.
- **What I'd Watch:** I am watching whether a commit-time recheck becomes a standard building block, not a patch each team rewrites.
  - **The premise record:** A written list of the exact facts and conditions a decision used, kept with the pending action.
  - **The conditional commit:** A check against those recorded versions that fires at the exact moment the effect lands.
  - **The per-entity ceiling:** The 2,000 pending-signal default, which caps how long a pinned entity's queue can wait.
- **The Catch:** The study's tests run no language model. The conditions are not extracted automatically, and the failure share comes from a change set built to fail on purpose.

## Sources

[1] Yongjian Lyu and Yang Ren (Huawei), "From Version Conflicts to Decision Conflicts: Selective Revalidation for Long-Running AI Agents", arXiv:2609.08015v1, 7 Sep 2026. https://arxiv.org/html/2609.08015v1
[2] Same study, the unchecked-release policy and its controlled change set. https://arxiv.org/html/2609.08015v1
[3] Same study, the block-on-any-change policy and durable-cell results. https://arxiv.org/html/2609.08015v1
[4] Same study, the cost of rechecking only the decision's premises. https://arxiv.org/html/2609.08015v1
[5] Same study, stated scope and the no-model test cells. https://arxiv.org/html/2609.08015v1
[6] Sajjad Khan, "Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems", arXiv:2606.17182v1, 15 Jun 2026. https://arxiv.org/html/2606.17182v1
[7] Same paper, measured prevention costs. https://arxiv.org/html/2606.17182v1
[8] Same paper, the deer-flow lost-update reproduction. https://arxiv.org/html/2606.17182v1
[9] Xin Yang, Letian Li and colleagues, "Position: Multi-Agent Systems Should Prioritize Concurrency Control", arXiv:2608.18092v1, 6 Jun 2026. https://arxiv.org/html/2608.18092v1
[10] Amazon Web Services, "Retry policy", EventBridge User Guide, as of 2026-10-21. https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html
[11] Amazon Web Services, "Amazon SQS message quotas", SQS Developer Guide, as of 2026-10-21. https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html
[12] Temporal Technologies, "Workflow Execution limits", as of 2026-10-21. https://docs.temporal.io/workflow-execution/limits

## Gate report
PASS — Lead is direct, punchy, and delivers the core 84,000-write problem immediately without throat-clearing.
PASS — Tension frames the structural issue with shared state clearly, incorporating a first-person cue ("My read on the research...") and expanding SQS on first use.
PASS — Tactical insight reports the study's design in bulleted observations rather than playbook commands.
PASS — Nuanced takeaway flags the study's own limits (no model in the long tests, no automatic extraction) without corporate sign-offs.
PASS — TLDR strictly adheres to the 4-part Smart Brevity format with indented sub-bullets and clear, plain-English summaries.
