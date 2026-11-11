---
title: "Your Agent Says Done: 40 of 66 Without Proof"
vertical: multi_agent_enterprise_fabric
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An agent run's exit is a claim about evidence, not a state the model can report: a model-driven loop declared 40 of 66 held-out task clusters finished without support while a certificate that ties each answer claim to trace evidence declared none, at no cost in supported completions — so the receipt belongs at the boundary and the step cap belongs only at the fuse."
date: 2026-11-11
slug: your-agent-says-done-40-of-66
meta_title: "Your Agent Says Done: 40 of 66 Without Proof"
meta_title_source: "derived_from_title"
meta_description: "A model-driven agent loop called 40 of 66 test tasks finished without evidence behind the answer. The design that demanded a trace receipt called none."
meta_description_source: "derived_from_lead"
---

<!-- lead -->
A model-driven agent loop called 40 of 66 held-out task clusters finished, and in each of those cases the trace behind the answer did not support it [1]. A different design let a run report complete only when a typed receipt tied every required answer claim to evidence inside its trace, and a replay rebuilt each derived value from what the tools returned. It called none of them finished that way [1]. Both designs ran the same frozen study, and supported completions came in at 97 of 132 against 92 of 132, so the proof did not cost finished work [1]. That result changed how I read every "done" a fabric writes into a ledger.

<!-- tldr -->

## At a glance
- **The shift:** the end of an agent run is becoming a check the runtime performs, not a word the model emits.
- **The number:** 40 of 66 task clusters ended without support under a model-driven controller; none under an evidence-checked exit [1].
- **The risk:** the check proves the claims rest on the trace. It does not prove the answer is true.

<!-- tension -->

## Four ways to say done

The paper behind that result lists the exit signals most fabrics lean on. Each one is cheap to produce. A model emits the word done. Its checklist says approved. A heuristic spots a long answer and a pile of prior calls. A critic model judges the answer plausible [1]. None of them says which observation supports which final claim [1]. None says whether the evidence covers the entity and period the request named, or whether a derived number can be rebuilt from what the tools returned [1].

The cost of the weakest substitute is the one I keep circling. A critic core is a model asked whether the run looked finished. Across 48 synthetic tasks in six tool-use families, with eight fault classes injected, it produced 252 of 288 unsafe completions, against none for the receipt [1]. The critic was not careless; it answered a different question, about how the answer read rather than whether the answer was paid for.

## By the numbers

| Exit signal | What it checks | Overhead | Primary failure mode | Best for |
|---|---|---|---|---|
| Model's own "done" | Nothing outside the token stream | Near zero | Declares completion without support | Prototypes only |
| Critic model | Plausibility of the answer | One extra inference | 252 of 288 unsafe completions on faulted tasks [1] | Screening, never gating |
| Budget or step cap | Counters, not content | None at runtime | Stops working runs at the wall | A fuse, not a test |
| Evidence receipt | Trace support per claim, replayed values | Typed schema per task | Cannot certify external truth | Ledger boundaries |

- **97 of 132 — Supported completions:** the receipt's rate against the controller's 92 of 132, so the check did not cost finished work [1].
- **18 of 66 — Recoverable:** trajectories the receipt turned back into a state the run could resume, 17 of which then completed with support [1].

A run that cannot produce the receipt is not a lost run: the receipt design recovered 18 of 66 runs, and 17 of those then completed with support [1]. A failed exit is a state you can inspect, while a retry budget gives you nothing to inspect.

<!-- tactical-insight -->

## What the runtime enforces

The defaults show what a fabric gets when nobody decides. LangGraph's Python build ships a recursion limit of 10,007 super-steps from version 1.1.4, and 10,000 before that [5]. Its JavaScript port ships 25 [6]. That is one graph runtime, two official ports, and a gap of roughly 400 times. Neither number knows whether the task was finished. My read is that the number is a fuse. A fuse is not a specification.

Temporal's durable workflows stop at a harder wall. An execution's event history is capped at 51,200 events or 50 megabytes, with at most 2,000 in-flight activities, child workflows, signals or cancellations per execution [7]. That ceiling is real, and it is also not a completion test — it is where the bill stops growing.

A stop computed from content rather than from a counter is not exotic. On a 60-question multi-hop test, a judge-free semantic stopper cut operational tokens by 38% against a fixed iteration cap at parity quality (p = 0.81 [8]). The check compared consecutive drafts, work the runtime did on evidence the runtime could see.

What I keep circling is the order of the parts: a receipt at the boundary, a fuse at the runtime, and nothing in between that a model gets to assert. The list of outputs the receipt checks is the real definition of the task. A fabric that cannot write that list down cannot check it. It is the same question as [who owns the order of the steps](/your-router-breaks-275-constraints/): that design decides where the model sits inside the path, and this one decides what the path hands back before it ends.

<!-- nuanced-takeaway -->

## Where the receipt stops

The receipt states its own boundary in one line. It certifies support in a recorded trace under declared assumptions, "not external truth, safety, or alignment" [1]. A trace can support a claim the world has since contradicted, so the receipt says the run did its work without saying the work was right. I find that a strength at a ledger boundary, because the other option on offer is how plausible the answer looks, which certifies nothing.

The long-horizon evidence shows the failure the receipt aims at. Across 17 frontier models, 79% of the runs that were never solved ended when the 90-minute budget expired while the agent was still working [3]. Mean reward on those runs sat between 0.10 and 0.35, nowhere near finished [3]. They burned an average of 9.8M tokens over about 239 episodes and 88.9 minutes each [3]. The authors call it a false-finish pattern: agents overestimate completion and under-invest in the last check [3].

The model's own read on whether the task can still succeed is the last signal to lean on. On runs that failed, it still put the odds above 70% even after 60% of the budget was gone, and the alarm fired only in the final 20% [4]. Used as a stop anyway, a trained estimator saves 28% to 64% of tokens on failed runs at 1.6 to 4.2 percentage points of success [4] — a cost control with a measured price in success, and one the same paper reports collapsing when training skipped a supervised warm start [4].

The exit input is also attackable. LoopTrap poisoned the signal that ends the loop and averaged 3.57 times the steps across eight mainstream agents, with a peak of 25 times [2]. Content an agent reads can keep it working, so the fuse has to exist even when the receipt is good, and the receipt has to come from code that reads the trace rather than from a model that reads the chat. The part I would watch next is the receipt's slot list in production fabrics: does it name the answers the business needs, or only the fields the tool schema happened to return?

## Sources
- [1] Jason Liu, "When May an Agent Stop? Evidence-Carrying Termination for Tool-Using LLMs" (arXiv:2608.23623v1, 22 August 2026) — https://arxiv.org/html/2608.23623v1
- [2] Huiyu Xu, Zhibo Wang, Wenhui Zhang et al., "LoopTrap: Termination Poisoning Attacks on LLM Agents" (arXiv:2605.05846v1, 7 May 2026) — https://arxiv.org/html/2605.05846v1
- [3] Tencent HY LLM Frontier et al., "Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading" (arXiv:2607.08964v3, 9 October 2026) — https://arxiv.org/html/2607.08964v3
- [4] Yuxiang Lin, Zihan Wang, Mengyang Liu et al., "BAGEN: Are LLM Agents Budget-Aware?" (arXiv:2606.00198v1, 29 May 2026) — https://arxiv.org/html/2606.00198v1
- [5] LangChain, "Graph API overview" (LangGraph for Python, recursion limit) — https://docs.langchain.com/oss/python/langgraph/graph-api
- [6] LangChain, "Graph API overview" (LangGraph.js, recursion limit) — https://docs.langchain.com/oss/javascript/langgraph/graph-api
- [7] Temporal Technologies, "Workflow Execution limits" — https://docs.temporal.io/workflow-execution/limits
- [8] Sahil Shrivastava, "Semantic Early-Stopping for Iterative LLM Agent Loops: A Judge-Efficient Study of When to Halt" (arXiv:2606.27009v1, 25 June 2026) — https://arxiv.org/html/2606.27009v1
