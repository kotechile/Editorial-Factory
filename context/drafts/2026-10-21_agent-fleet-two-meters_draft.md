---
title: Your Agent Fleet's 39x Gap: One Meter Nobody Budgets
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "An agent fabric's running cost is set as much by the harness as by the model it calls in each role, and only the model meter is instrumented, tooled and sold."
date: 2026-10-21
slug: agent-fleet-two-meters
synthesis: true
sources:
  - https://arxiv.org/abs/2610.25231
  - https://arxiv.org/abs/2610.26676
---

<!-- lead -->
Two agent frameworks ran the same eleven coding tasks on the same machine this month. One of them fired 117.2 process launches for every tool call. The other fired 3.0. That is a nearly 39x gap in kernel work on identical jobs. A team watching test scores would call it a tie. A team paying for the hosts would call it a different fleet. Your agent fleet bills on two meters. The token meter counts what the models cost. The host meter counts what the harness costs to run. Only the host meter stays off the dashboard, and nobody budgets for it.

<!-- tension -->

## The big picture:

I keep coming back to one comparison from a systems paper posted on 2026-10-18. The researchers ran ten agent frameworks against eleven matched coding tasks. Everything else was held constant. Then they asked what explained the spread in peak memory across those runs. Framework identity explained 52.95% of the variance. Task content explained 4.22% [1].

### Two meters, one bill

That is a strange result for anyone who sizes nodes from a task mix. The work did not set the memory profile. The way the harness is built did. MetaGPT starts a process for nearly everything it touches. It pays a median of 6,420 page faults and 180.6 context switches per tool call. CAMEL (a lighter multi-agent framework in the same set) does its work in-process and pays 3.0 launches. The other frameworks sat in between, at 51.6, 15.2 and 10.7 launches per call [1].

The spread does not fold into one metric either. Peak memory and process count move together only weakly, with a rank correlation of 0.13. A budget built on memory cannot see the process pressure. A budget built on process count cannot see the memory [1].

The second paper, posted a day later, prices a different meter. It treats model choice per role as a search problem. Given a set of models for planning, solving, searching and checking, which mix gives the best quality for the money? The authors tested eight quality and cost matrices. Each covered workflows with two to five roles and up to 1,681 possible mixes. Their method finds most of the true trade-off curve at about 10% of the cost of testing every mix [2]. On one of the eight, it hit 88.75% recall at 100% precision for about a tenth of the full evaluation bill [2].

My read is that these two results describe the same purchase from opposite ends. One says the harness sets the host envelope by an order of magnitude more than the task does. The other says the model menu can now be searched cheaply enough to run every week. Neither paper mentions the other's lever.

### What the market is selling

The vendor talk in this window has picked one of those meters. MuleSoft's own event page lists "Control AI Costs & Govern Every Agent with MuleSoft Agent Fabric" for 2026-10-07. A follow-up on 2026-11-18 is titled "Controlling AI Spend While Navigating Regulatory Guardrails" [3]. Cost shows up as a governance problem here: a view over a list of agents, and a rule about who may spend.

That is a real control, and it answers a real question. It does not touch the host meter. A registry can see that an agent exists and what it may call. It cannot see that the agent's harness spawns a process per tool call while the one next to it does not.

## By the numbers

- **52.95% vs 4.22% — Memory variance:** Framework identity explains 52.95% of peak resident memory variance across ten frameworks on eleven matched tasks; task content explains 4.22% [1].
- **117.2 vs 3.0 — Launches per tool call:** MetaGPT against CAMEL on identical tasks, a nearly 39x gap in kernel work, with 6,420 page faults and 180.6 context switches per call on the heavy side [1].
- **5.7–7.1 ms vs 12.1–18.4 ms — Slow-tail allocation latency:** On a shared host at 90% of combined peak demand, a harness-aware controller held the protected worker's 95th-percentile latency where a flat budget let it climb, and the flat budget failed to finish two to three of every three runs [1].
- **88.75% — Curve recall:** The per-role model search reached that recall at 100% precision on one instance, at about a tenth of the full evaluation cost [2].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this are the ones putting several frameworks on one host budget. What they do next shows up in a few places.

- **Harness fingerprints.** The systems paper builds an offline profile for each framework. It then feeds a phase-aware controller that sets memory floors and ceilings per step. The interesting part is not the controller. It is that a framework can be told apart by its resource print at all. That turns "which harness is this job running" into a question a scheduler can answer [1].
- **Capacity reviews that ask for a second line.** The paper's own point is that benchmarks report test scores, run time and token cost. None of those show host-side behaviour. I'd expect the first serious adoption to land as a third column in a capacity plan, not as a new product [1].
- **Routing tools that name their bill.** The model-assignment work cuts the cost of testing, not the cost of running. Those are different numbers. A tool that reports a 90% saving without saying which one is worth a careful read of the label [2].
- **Co-location as the real test.** Inference ran off-box in the memory study, so its figure is a pure harness cost. In a live fabric that pressure lands beside everything else on the node. That is the case the co-location replay models [1].

<!-- nuanced-takeaway -->

## The catch:

Both results are lab instruments, and the papers say so. The memory work replays traces captured on one dedicated host, with a single model provider behind it. Its authors list closed-source frameworks and automatic fingerprinting as open problems [1]. The search work replays matrices that were already bought and makes no new model calls. Its coverage is uneven: on HotpotQA the mean recall is 0.58 at 10% of the evaluation budget and 0.74 at 30% [2].

Nor does the memory finding come with a price list. It reports latency, fault counts and process launches, not dollars. Nothing in it says a heavier harness is the wrong choice. Teams pick a framework for its tools, its ecosystem and the shape of its state model. A resource print is one input among several.

What I take from the pair is narrower and more useful. The two meters are read by different people with different tools. Only one of them shows up in the spend review. That gap is where an architect's forecast quietly goes wrong.

<!-- tldr -->

## At a glance

- **The Big Shift:** Two papers published a day apart measured the two halves of an agent fleet's running cost. One found the framework, not the task, sets the host memory envelope by an order of magnitude. The other found that picking a model per role is now a cheap search.
- **Why It Matters:** Capacity plans built from task mix and token prices miss the meter that varies most per unit of work. On a shared host at a tight memory ceiling, a flat budget failed to finish most runs, while a harness-aware one held latency at 5.7–7.1 ms.
- **What I'd Watch:** Whether the harness becomes a line item and an instrumented signal.
  - **Harness fingerprints:** An offline resource profile per framework, used by a scheduler to tell whose pressure is whose.
  - **Phase-aware memory tiers:** Per-step memory floors and ceilings that follow the switch between waiting on a model and running tools.
  - **Labelled routing claims:** Reports that split testing spend from running spend, so a 90% saving cannot be read as the wrong one.
- **The Catch:** Both are replays, not production. The host study used one machine and one provider, the search study replayed bought data with uneven coverage, and neither prices the host meter in dollars.

## Sources

[1] Wentao Hong, "AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents," arXiv:2610.25231, submitted 2026-10-18. https://arxiv.org/abs/2610.25231

[2] Qian Xie, Wenyue Hua, Yueli He, Sripad Karne, Armaan Agrawal, Nikos Pagonas, Eugene Wu, Kostis Kaffes, Tianyi Peng, Nairen Cao, "Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows," arXiv:2610.26676, submitted 2026-10-19. https://arxiv.org/abs/2610.26676

[3] MuleSoft, "Events" (Agent Fabric webinar calendar), entries dated 2026-10-07 and 2026-11-18, observed 2026-10-21. https://www.mulesoft.com/events
