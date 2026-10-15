---
title: "68 Loops Your Runtime Never Stopped"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "An agent run needs a bound that lives outside the model and outside the framework's own default: a census of 6,549 agent repositories confirmed 68 runaway loops, every one of them missing a bound, while the defaults meant to catch them are version- and layer-dependent."
date: 2026-10-15
slug: agent-loop-bound-not-a-budget
archetype: evergreen
evergreen: true
---

<!-- lead -->
A scan of 6,549 agent repositories turned up 68 loops that nothing in the code stopped on their own, and a reviewer checked every one by hand: 47 projects, 91.9% precision [1]. The recorded damage in 65 of the 68 was a runaway API (application programming interface) bill, and the same 65 ended in model denial of service [1]. Your runtime holds the same risk, because the missing part is not intelligence. It is a ceiling the model cannot move.

<!-- tension -->

## The big picture:

I read the study's method more closely than its summary, because the method is the interesting part. It turns each program into a typed model of loops, model calls and state changes. Then it asks one question about every path: can this repeat, and does a real limit cover it [1]?

That last word is the trick. A limit written next to a loop is not the same thing as a limit over it [1].

The authors sort every candidate path into one of two boxes. Covered means a verified, framework-default or config-level bound applies. Uncovered means the bound is missing, weak, switched off, ineffective, or jumped over by the path it was meant to stop [1].

The census that fell out of that work is small and sharp. All 68 confirmed failures carried a missing strong bound. In 26 of them, the exit still belonged to the model itself [1].

**The part I keep circling:** the big frameworks ship these controls already. LangChain has max_iterations, LangGraph has recursion limits, the OpenAI Agents SDK (software development kit) has a turn limit, CrewAI has max_iter [1].

The paper's own conclusion is that the controls settle nothing by themselves. Teams omit them, set them badly, or place them where they do not cover the loop that really repeats [1].

## By the numbers

- **68 loops — Confirmed failures:** hand review confirmed 68 unbounded-loop failures across 47 of the 6,549 scanned agent repositories, out of 74 candidates flagged, at 91.9% precision [1].
- **65 of 68 — Cost exhaustion:** API cost exhaustion was the recorded impact in 65 confirmed failures, with model denial of service in the same 65 and context-window exhaustion in 19 [1].
- **26 of 68 — Model-owned exit:** the exit relied on the model's own output in 26 confirmed failures, and on a tool-controlled retry in 28, while a strong bound was missing in all 68 [1].
- **1000 steps — LangGraph's graph default:** the documented default recursion limit since version 1.0.6, while the core library's own reference still documents 25 for its call-recursion setting [2][3].

<!-- tactical-insight -->

## What I'd watch:

Four places the bound leaks in what people are actually reporting.

- **Inherited defaults:** LangGraph's graph page documents a default recursion limit of 1000 super-steps since version 1.0.6 [2]. The core library's own reference still says a call recursion limit defaults to 25 [3]. Which number a run gets depends on the layer that sets it.
- **Subagents:** an issue in the project's own tracker describes a parent capped at 150 (or 300) whose subagents still ran at the framework default of 25. They died on tasks of 13 or more tool calls [4]. The issue has since been closed.
- **Iteration is not time:** CrewAI stops an agent at 20 iterations by default, and leaves max_execution_time unset unless you set it [5]. A step cap is not a clock, and neither one is a dollar cap.
- **The bill shows up first:** the recorded impact in the census was cost, not a wrong answer [1]. Two agents arguing in a loop keep producing believable output the whole time.

**What I'm watching next:** whether the static pass that found these loops becomes routine before release, the way a linter did.

<!-- nuanced-takeaway -->

## The catch

The census counts confirmed failures in real code. It is a sorting key for frameworks, not a verdict on them, and the paper does not claim a default caused any of these loops [1]. A tracker item is a snapshot too. The one behind the subagent number is closed, so a later release may handle it in a different way [4].

I could be wrong, but I read the 1000-step graph default as the more dangerous of the two numbers, because it is the one a team receives without asking. A thousand steps of tool calls is a bill with a plan attached [2].

The other edge of the trade shows up in the desk's own field case. An unconstrained two-agent critique loop burned $4,200 in credits in 45 minutes before rate limits stopped it [6]. The fix in that note was a recursion budget of five steps, plus a cost ceiling for each session [6].

Five steps would cut off plenty of honest long runs. That is the trade every bound forces: pick the failure you prefer, a bill or a cut-off task.

<!-- tldr -->

## At a glance

- **The Big Shift:** A static scan of 6,549 agent repositories confirmed 68 runaway loops across 47 projects, and every one of them was missing a limit that really governed the repeating path.
- **Why It Matters:** The recorded impact in 65 of the 68 was API cost exhaustion, and the defaults a team inherits sit at different layers and versions — a graph default of 1000 steps, a core reference of 25, an iteration cap of 20, and subagents that do not take their parent's limit.
- **What I'd Watch:** whether teams start checking bound coverage before a release, and which layer they pin it to.
  - **Where the bound lives:** a limit the model's own output can hold open is not a bound; 26 of the 68 confirmed failures still had a model-owned exit.
  - **What it covers:** a limit written beside a loop is not a limit over the loop, so static checks now sort bounds into covered and uncovered.
  - **Which default you inherit:** graph defaults, core-library defaults and subagent paths disagree, so the number you get depends on the layer that sets it.
- **The Catch:** the census is a snapshot, not a verdict on any framework, and a tight bound trades a runaway bill for cut-off honest work.

## Sources
[1] Hou, Wang, Zhao & Wang — "When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents," arXiv:2607.01641v1 [cs.SE] (2026-07-02) — https://arxiv.org/html/2607.01641v1
[2] LangChain documentation — LangGraph Graph API, "Recursion limit" (default 1000 steps since version 1.0.6) — https://docs.langchain.com/oss/python/langgraph/graph-api
[3] LangChain Reference — langchain_core RunnableConfig.recursion_limit ("If not provided, defaults to 25") — https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig/recursion_limit
[4] langchain-ai/deepagents — Issue #1698, "SubAgentMiddleware does not propagate recursion_limit to subagent graphs" (closed) — https://github.com/langchain-ai/deepagents/issues/1698
[5] CrewAI documentation — Agents (max_iter default 20; max_execution_time optional) — https://docs.crewai.com/concepts/agents
[6] Editorial-factory field notes, agentic_ai Anecdote 1 (internal, anonymised) — context/growth_os/customer-truth.md
