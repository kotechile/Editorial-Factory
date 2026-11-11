---
title: "Your Agent Says Done: 40 of 66 Without Proof"
vertical: multi_agent_enterprise_fabric
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An agent run's exit is a claim about evidence, not a state the model can report: a model-driven loop declared 40 of 66 held-out task clusters finished without support while a receipt that ties each answer claim to trace evidence declared none, at no cost in supported completions — so the receipt belongs at the boundary and the step cap belongs only at the fuse."
date: 2026-11-11
slug: your-agent-says-done-40-of-66
meta_title: "Your Agent Says Done: 40 of 66 Without Proof"
meta_title_source: "derived_from_title"
meta_description: "A model-driven agent loop called 40 of 66 held-out task clusters finished, and in each case the trace behind the answer did not support the claim."
meta_description_source: "derived_from_lead"
---

<!-- lead -->
A model-driven agent loop called 40 of 66 held-out task clusters finished, and in each case the trace behind the answer did not support the claim [1]. A different design let a run report complete only when a typed receipt tied every required answer claim to evidence inside its trace, and a replay rebuilt each derived value from what the tools returned. It called none of them finished that way [1]. Both designs ran the same frozen study, and supported completions came in at 97 of 132 against 92 of 132, so the proof did not cost finished work [1].

<!-- tldr -->

## At a glance

- **The shift:** a run ends on a check the runtime performs, not a word the model emits.
- **The number:** 40 of 66 clusters ended unsupported; none under an evidence-checked exit [1].
- **The risk:** the check proves claims rest on the trace, not that the answer is true.

<!-- tension -->

## Four ways to say done

The paper behind that result lists the exit signals most fabrics lean on. Each is cheap to produce, and each answers a different question than "is the work supported":

1. **A done token** — the model emits the word itself.
2. **An approved checklist** — the run's own list of steps comes back ticked.
3. **A length heuristic** — a long answer plus a pile of prior calls reads as effort.
4. **A critic model** — a second model decides the answer looks plausible [1].

None of them says which observation supports which final claim [1]. None says whether the evidence covers the entity and period the request named, or whether a derived number can be rebuilt from what the tools returned [1].

I keep coming back to the critic core, because it is the strongest of the four and still fails in the direction that matters. Across 48 synthetic tasks in six tool-use families, with eight fault classes injected, it produced 252 of 288 unsafe completions, against none for the receipt [1]. The critic was not careless; it answered a different question, about how the answer read rather than whether the answer was paid for.

A run that cannot produce the receipt is not a lost run. The receipt design recovered 18 of 66 runs, and 17 of those then completed with support [1]. A failed exit is a state you can inspect, while a retry budget gives you nothing to inspect.

## By the numbers

- **Unsafe completions:** the critic core shipped 252 of 288; the receipt shipped none [1].
- **Supported completions:** the receipt finished 97 of 132 against the controller's 92 of 132 [1].
- **Recoverable runs:** 18 of 66 came back as resumable state; 17 then completed with support [1].

<!-- tactical-insight -->

## What the runtime enforces

The defaults show what a fabric gets when nobody decides. One runtime, two official ports, and the two numbers are almost 400 times apart:

| Layer | What it counts | Documented value | What it proves |
|---|---|---|---|
| Python graph runtime | super-steps per run | 10,007 from version 1.1.4, 10,000 before that [5] | that the graph moved |
| JavaScript graph runtime | super-steps per run | 25 [6] | the same thing, with a fuse 400 times closer |
| Durable workflow | events in the history | 51,200 events or 50 megabytes, and 2,000 in-flight operations [7] | that the run is over |

I read the table three times before I believed the gap. Neither number knows whether the task was finished. The number is a fuse, and a fuse is not a definition.

A stop computed from content rather than from a counter is not exotic. On a 60-question multi-hop test, a judge-free semantic stopper cut operational tokens by 38% against a fixed iteration cap at parity quality (p = 0.81 [8]). The check compared consecutive drafts, work the runtime did on evidence the runtime could see.

The order of the parts matters: a receipt at the boundary, a fuse at the runtime, and nothing in between that a model gets to assert. The list of outputs the receipt checks is the real definition of the task. A fabric that cannot write that list down cannot check it. It is the same question as [who owns the order of the steps](/your-router-breaks-275-constraints/): that design decides where the model sits inside the path, and the exit decides what the path hands back before it ends.

<!-- nuanced-takeaway -->

## Where the receipt stops

The receipt states its own boundary in one line. It certifies support in a recorded trace under declared assumptions, "not external truth, safety, or alignment" [1]. A trace can support a claim the world has since contradicted, so the receipt says the run did its work without saying the work was right. My reading is that this is a strength at a ledger boundary, because the other option on offer is how plausible the answer looks, which certifies nothing.

The long-horizon evidence shows the failure the receipt aims at. Across 17 frontier models, 79% of the runs that were never solved ended when the 90-minute budget expired while the agent was still working [3]. Mean reward on those runs sat between 0.10 and 0.35, nowhere near finished. They burned an average of 9.8M tokens over about 239 episodes and 88.9 minutes each, and the authors call it a false-finish pattern: agents think they are done sooner than they are, and spend too little on the last check [3].

The model's own read on whether the task can still succeed is the last signal to lean on. On runs that failed, it still put the odds above 70% even after 60% of the budget was gone, and the alarm fired only in the final 20% [4]. Used as a stop anyway, a trained estimator saves 28% to 64% of tokens on failed runs at a cost of 1.6 to 4.2 percentage points of success. The same paper reports the estimator collapses when training skipped a supervised warm start [4].

The exit input is also attackable. LoopTrap poisoned the signal that ends the loop and averaged 3.57 times the steps across eight mainstream agents, with a peak of 25 times [2]. Content an agent reads can keep it working, so the fuse has to exist even when the receipt is good, and the receipt has to come from code that reads the trace rather than from a model that reads the chat. What I am watching next is the receipt's slot list in production fabrics: does it name the answers the business needs, or only the fields the tool schema happened to return?

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Undo Is 14.6x Cheaper" -> /your-undo-is-14-6x-cheaper/ [same site (aichieve.net); same category; topical overlap: agent, finished, task] Link "Your Undo Is 14.6x Cheaper" in the section where the article touches agent, finished, task. -->
<!-- internal-link hint: "Your Task Protocol Costs 643 Lines" -> /your-task-protocol-costs-643-lines/ [same site (aichieve.net); same category; topical overlap: agent, task] Link "Your Task Protocol Costs 643 Lines" in the section where the article touches agent, task. -->
<!-- internal-link hint: "Your Trace Fails as an Alarm" -> /your-trace-fails-as-an-alarm/ [same site (aichieve.net); same category; topical overlap: proof, trace] Link "Your Trace Fails as an Alarm" in the section where the article touches proof, trace. -->
## Related reading

- [Your Undo Is 14.6x Cheaper](/your-undo-is-14-6x-cheaper/) — more on Autonomous & Agentic Workflows
- [Your Task Protocol Costs 643 Lines](/your-task-protocol-costs-643-lines/) — more on Autonomous & Agentic Workflows
- [Your Trace Fails as an Alarm](/your-trace-fails-as-an-alarm/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources
- [1] Jason Liu, "When May an Agent Stop? Evidence-Carrying Termination for Tool-Using LLMs" (arXiv:2608.23623v1, 22 August 2026) — https://arxiv.org/html/2608.23623v1
- [2] Huiyu Xu, Zhibo Wang, Wenhui Zhang et al., "LoopTrap: Termination Poisoning Attacks on LLM Agents" (arXiv:2605.05846v1, 7 May 2026) — https://arxiv.org/html/2605.05846v1
- [3] Tencent HY LLM Frontier et al., "Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading" (arXiv:2607.08964v3, 9 October 2026) — https://arxiv.org/html/2607.08964v3
- [4] Yuxiang Lin, Zihan Wang, Mengyang Liu et al., "BAGEN: Are LLM Agents Budget-Aware?" (arXiv:2606.00198v1, 29 May 2026) — https://arxiv.org/html/2606.00198v1
- [5] LangChain, "Graph API overview" (LangGraph for Python, recursion limit) — https://docs.langchain.com/oss/python/langgraph/graph-api
- [6] LangChain, "Graph API overview" (LangGraph.js, recursion limit) — https://docs.langchain.com/oss/javascript/langgraph/graph-api
- [7] Temporal Technologies, "Workflow Execution limits" — https://docs.temporal.io/workflow-execution/limits
- [8] Sahil Shrivastava, "Semantic Early-Stopping for Iterative LLM Agent Loops: A Judge-Efficient Study of When to Halt" (arXiv:2606.27009v1, 25 June 2026) — https://arxiv.org/html/2606.27009v1
