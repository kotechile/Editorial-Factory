---
title: "Your Agent's 84,000-Write Mistake"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "A long-running agent commits facts it read minutes ago, so the useful question is not whether the record moved but whether the change voids the decision — and the cheap fix is to record the premises the decision used and recheck exactly those at commit."
date: 2026-10-21
slug: agent-writes-stale-basis
archetype: evergreen
evergreen: true
---

<!-- lead -->
Your agent reads a record, reasons for a minute, then writes. Anything that changed in between is invisible to that write. Both obvious defences make the same mistake: blocking every change threw away 84,000 good writes, while letting them through released 126,000 invalid effects [2][3].

A refund agent shows the shape of it. It reads an order, decides the customer is owed 80 pounds, and parks the payment for approval. Before the approval clears, another worker pays the same claim, or the delegated limit falls from 100 to 50. The reasoning was sound when it ran. It is wrong when it commits [1].

There is a third option, and it is the one worth copying. A runtime that rechecks only what the decision rested on cleared the same tests while checking 0.6 conditions per change instead of 6.0 [4].

<!-- tension -->

## The big picture:

I keep circling one line in that study. A version number answers whether the record moved. It does not answer whether the change mattered [1].

A customer's display name can change and leave the refund fully justified. The limit can fall to 50 and void it. A database reports the first fact. It has no view on the second.

The research is naming the failure now. One paper lists four ways shared state goes wrong across agents: a stale read that outlives the moment it was taken, a tool that no longer exists, a chain of knock-on effects, and effects that reorder on the way out [6]. Another looked at one benchmark and found 67.1% of its failures came from agents colliding over shared state [9].

The clock makes it worse. An action often travels through a bus before it reaches the core system, and that bus is patient. Amazon EventBridge retries a failed delivery for 24 hours and up to 185 times by default [10]. A queued message sits in Amazon SQS (Simple Queue Service) for 4 days by default, and up to 14 days [11]. A write computed on Monday can land on Thursday.

## By the numbers

- **84,000 — Good writes thrown away:** blocking every stale write let no bad effect through, yet it also discarded all 84,000 safe changes in the run and matched the exact outcome in just 20% of the ten test cells [3].
- **0.6 vs 6.0 — Checks per change:** rechecking only the decision's own premises cost 0.6 checks per resumed change against 6.0 for a full rescan. At 4,093 recorded reads the check took 9.3 microseconds against 2,595.9 [4].
- **67.1% — Failures from shared state:** one benchmark divides that into 37.2% of agents submitting too early and 29.9% of agents failing to agree, both read as missing coordination [9].
- **2.3x and 8% — The price of prevention:** pessimistic locking cost 1.6 to 2.3 times the baseline, and snapshot isolation added about 8% more tokens on one workload, which the authors call far below the penalty teams assume [7].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this problem are moving the check to the moment of commit and shrinking what it covers. Four things I would look for in a design review:

- **A premise record beside the action.** The runtime writes down what the decision rested on: the order is delivered, the defect is confirmed, no refund has been paid, the limit is 100. Those notes live with the pending action, not with the run [1].
- **A check at commit, not at read.** The conditional write compares the stored versions against those notes at the moment the effect fires, so a slow approval queue cannot let a stale decision through [1].
- **Granularity finer than the row.** The runtime works at field and condition level, which is why it can accept a name change and refuse a limit change on the same record [1].
- **One execution per hot entity, with the ceiling known.** Pinning an order, vendor or employee object to a single durable execution buys ordering. It also parks every waiting approval inside one run, and Temporal caps incomplete signals at 2,000 per execution by default against a history limit of 51,200 events [12].

The cost of prevention is smaller than teams expect. Locking ran 1.6 to 2.3 times the baseline. Snapshot isolation added about 8% more tokens on one workload [7]. Both are numbers a team can budget, not arguments against correctness.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is that this is a design study, not a field report. Its long tests run no language model, and the authors say the results show controlled feasibility rather than production behaviour [5]. The conditions are not pulled out automatically either. Someone still has to teach the fabric which fields matter to which decision.

The 60.0% needs the same care. The study built five changes per scenario and made 60% of them void the decision, on purpose [2]. It proves the failure is real. It does not estimate how often your fabric meets it.

Two of the three clocks are vendor defaults, and defaults move [10][11]. A shorter retention window or a longer retry horizon changes the sums in a review.

What holds either way is narrower than an isolation level. A version number says something moved. It does not say whether it mattered, and the check that survives is the one that asks the second question.

<!-- tldr -->

## At a glance

- **The Big Shift:** An agent reads a record, reasons for seconds or minutes, then writes. Anything that changed in that gap is invisible to the write. Both obvious defences fail: let it land and stale decisions commit, block on any change and safe ones die too.
- **Why It Matters:** The measured options differ by more than style. The unchecked write released 126,000 invalid effects. The block-everything policy discarded all 84,000 safe changes [2][3]. Fabrics that touch payments, requisitions or employee records pay for both mistakes in money.
- **What I'd Watch:** I am watching whether a commit-time recheck becomes a fabric primitive instead of a patch each team writes again.
  - **The premise record:** a written list of the reads and conditions a decision used, kept with the pending action so a later check has something to compare.
  - **The conditional commit:** a compare-and-set on those recorded versions, fired at the effect itself rather than at the read.
  - **The per-entity ceiling:** the 2,000 pending-signal default that limits how long a pinned entity's queue can grow while it waits.
- **The Catch:** The study's long tests run no model, the conditions are not extracted automatically, and the failure share comes from a change set built to fail. Prevention is cheap but not free: about 8% more tokens for snapshot isolation, 1.6 to 2.3 times the baseline for locking [7].

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
