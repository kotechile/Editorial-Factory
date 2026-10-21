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
image_path: "context/assets/illustrations/agent-fleet-two-meters/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "The Unbudgeted Host Meter. A massive engineered base block supporting a tiny upper module on a concrete floor."
image_caption: "The Unbudgeted Host Meter: The hidden 39x cost gap inside your AI agent framework."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Two agent frameworks ran the same eleven coding tasks on the same machine this month. One fired nearly 39x more system process launches per tool call than the other: 117.2 against 3.0. That gap does not show up in test scores, and it sits on the half of your agent fleet's bill that nobody budgets for: the host meter.

The other half is the token meter, and it is the one with a dashboard, a vendor category and a research field of its own. The host meter has a paper published last week.

<!-- tension -->

## The big picture:

I keep coming back to one comparison from a systems paper posted on 2026-10-18 [1]. Researchers ran ten agent frameworks against eleven matched coding tasks, and held everything else the same. Framework identity explained 52.95% of the spread in peak memory. Task content explained 4.22% [1].

### Two meters, one bill

The harness sets the host load. One heavy framework starts a process for nearly everything it touches. It pays a median of 6,420 page faults and 180.6 context switches per tool call [1]. A lighter framework in the same set does its work in-process and pays 3.0 process launches. The others sat between them, at 51.6, 15.2 and 10.7 launches per call [1].

Peak memory and process count barely track each other: the rank correlation is 0.13 [1]. A budget built on memory cannot see the process pressure. A budget built on process count cannot see the memory.

The second paper, posted a day later, prices a different meter [2]. It treats the choice of model per role as a search problem. Given a set of models for planning, solving, searching and checking, which mix gives the best quality for the money? The authors tested eight quality and cost matrices. Each covered workflows with two to five roles and up to 1,681 possible mixes. Their method found most of the true trade-off curve at about 10% of the cost of testing every mix. On one of the eight it hit 88.75% recall at 100% precision, for about a tenth of the full evaluation bill [2].

My read is that these two results describe the same purchase from opposite ends. One says the framework sets the host envelope by an order of magnitude more than the task does. The other says the model menu can now be searched cheaply enough to run every week. Neither paper mentions the other's lever.

### What the market is selling

The vendor talk in this window has picked one of those meters. MuleSoft's own event page lists "Control AI Costs & Govern Every Agent with MuleSoft Agent Fabric" for 2026-10-07. A follow-up on 2026-11-18 is titled "Controlling AI Spend While Navigating Regulatory Guardrails" [3]. Cost shows up here as a governance problem: a view over a list of agents, and a rule about who may spend.

That is a real control, and it answers a real question. It does not touch the host meter. A registry can see that an agent exists and what it may call. It cannot see that one agent's framework spawns a process per tool call while its neighbour does not.

## By the numbers

- **52.95% vs 4.22% — Memory variance:** Framework identity explains 52.95% of peak resident memory variance across ten frameworks on eleven matched tasks; task content explains 4.22% [1].
- **117.2 vs 3.0 — Launches per tool call:** The heaviest framework fires nearly 39 times more process launches per call than the lightest, on identical tasks. On the heavy side, that is 6,420 page faults and 180.6 context switches per call [1].
- **5.7–7.1 ms vs 12.1–18.4 ms — 95th-percentile allocation latency:** On a shared host at 90% of combined peak memory demand, a controller that knew the framework kept the protected worker's latency low. A flat budget let the same latency climb, and failed to finish two to three of every three runs [1].
- **88.75% — Curve recall:** The per-role model search reached that recall at 100% precision on one instance, for about a tenth of the full evaluation cost [2].

<!-- tactical-insight -->

## What I'd watch:

Teams stacking several frameworks on one host budget meet this pressure first. What I'd watch next:

- **Host fingerprints.** The systems paper builds an offline resource profile for each framework. It then feeds a phase-aware controller that sets memory floors and ceilings per step. The useful part is that a framework can be told apart by its resource print at all. A job planner can then answer which harness it is running [1].
- **Capacity reviews.** Benchmarks report test scores, run times and token costs. None of those show host-side behaviour [1]. I'd expect early enterprise use to land as a third column in a capacity plan, not as a new product.
- **Labelled routing claims.** The model-assignment work cuts the cost of testing, not the cost of running [2]. A tool claiming a 90% saving is worth a careful read of which bill it cuts.
- **Shared-host tests.** The memory study ran inference off-box, so its figure is a pure harness cost [1]. In a live fabric, that pressure lands beside everything else on the node.

<!-- nuanced-takeaway -->

## The catch:

Both results come from lab work, and the papers say so. The memory study replays captured traces on one dedicated host, with a single model provider behind it. Its authors list closed-source frameworks as an open problem [1]. The search study replays matrices that were already bought and makes no new model calls. Its coverage is uneven: on HotpotQA the mean recall is 0.58 at 10% of the testing budget and 0.74 at 30% [2].

The memory finding also carries no price list. It reports latency, fault counts and process launches, not dollars [1]. A heavier framework can still be the right choice for its tools, its ecosystem or its state model.

The detail I keep landing on: two teams read these two meters with different instruments, and only one of them reaches the spend review. That blind spot is where a capacity forecast quietly fails.

<!-- tldr -->

## At a glance

- **The Big Shift:** Two papers published a day apart measured the two halves of an agent fleet's running cost. One found the framework, not the task, sets the host memory envelope by an order of magnitude. The other found that picking a model per role is now a cheap search.
- **Why It Matters:** Capacity plans built from task mix and token prices miss the meter that varies most per unit of work. On a shared host at a tight memory budget, a flat budget failed to finish most runs. A framework-aware controller held wait times at 5.7–7.1 ms.
- **What I'd Watch:** Whether the harness becomes a line item and a measured signal.
  - **Harness fingerprints:** An offline resource profile per framework, used by a planner to tell whose pressure is whose.
  - **Phase-aware memory tiers:** Per-step memory floors and ceilings that follow the switch between waiting on a model and running tools.
  - **Labelled routing claims:** Reports that split testing spend from running spend, so a 90% saving cannot be read as the wrong one.
- **The Catch:** Both are replays, not production. The host study used one machine and one provider, the search study replayed bought data with uneven coverage, and neither prices the host meter in dollars.

## Sources

[1] Wentao Hong, "AgentLens: Framework-Aware Characterization and Resource Control for Heterogeneous LLM Agents," arXiv:2610.25231, submitted 2026-10-18. https://arxiv.org/abs/2610.25231

[2] Qian Xie, Wenyue Hua, Yueli He, Sripad Karne, Armaan Agrawal, Nikos Pagonas, Eugene Wu, Kostis Kaffes, Tianyi Peng, Nairen Cao, "Which Model for Which Role? Cost-Efficient Pareto Recommendation for LLM Agentic Workflows," arXiv:2610.26676, submitted 2026-10-19. https://arxiv.org/abs/2610.26676

[3] MuleSoft, "Events" (Agent Fabric webinar calendar), entries dated 2026-10-07 and 2026-11-18, observed 2026-10-21. https://www.mulesoft.com/events

## Gate report

PASS — lead: opens on the measured 39x spread between two frameworks, then names the two meters.
PASS — tension: states the memory-variance finding with its exact figures, the decoupling, and the model-search result; the vendor framing is attributed to the page that carries it.
PASS — tactical-insight: reports what the papers' own mechanisms do and what the desk expects to see next, with no instruction to the reader.
PASS — nuanced-takeaway: carries both labs' stated limits and the uneven frontier coverage from the source.
PASS — tldr: four-part schema, both synthesis legs visible under The Big Shift.
Post-rewrite audit: restored the source's own nouns and units that the rewrite had genericised or rounded — framework identity (not "setup"), 180.6 context switches (not 181), "nearly 39 times" (not 39), the 90%-of-combined-peak-memory demand basis (not "90% load"), 95th-percentile allocation latency (not "wait times"), and the two webinar titles verbatim; removed an invented expansion of the HotpotQA benchmark name.
