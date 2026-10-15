---
title: "68 Loops Your Runtime Never Stopped"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "An agent run needs a bound that lives outside the model and outside the framework's own default: a census of 6,549 agent repositories confirmed 68 runaway loops, every one of them missing a bound, while the defaults meant to catch them are version- and layer-dependent."
date: 2026-10-15
slug: agent-loop-bound-not-a-budget
archetype: evergreen
evergreen: true
meta_title: "68 Loops Your Runtime Never Stopped"
meta_title_source: "derived_from_title"
meta_description: "A scan of 6,549 agent repositories found 68 loops that nothing in the code stopped. A reviewer checked every one by hand and confirmed a 91.9% precision rate."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/agent-loop-bound-not-a-budget/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "Unstoppable Agent Loops. A modular looping track mechanism with an unattached barrier resting on brushed steel."
image_caption: "Unstoppable Agent Loops: Missing runtime bounds cause massive API billing spikes."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A scan of 6,549 agent repositories found 68 loops that nothing in the code stopped. A reviewer checked every one by hand and confirmed a 91.9% precision rate [1]. In 65 of those 68 cases, the recorded damage was a runaway bill for API (application programming interface) calls, and the same 65 ended in a model denial of service [1]. Your runtime carries the same exposure. The missing part is not intelligence, but a ceiling the model cannot move.

<!-- tension -->

## The big picture:

I read the study's method more closely than its summary, because the testing method is the interesting part. 

It turns each program into a typed map of loops, model calls, and state changes. Then it asks one question about every path: can this repeat, and does a real limit cover it [1]?

That last word is the trick. A limit written next to a loop is not the same thing as a limit over it [1].

The authors sort every candidate path into one of two boxes. "Covered" means a verified, framework-default, or config-level bound applies. "Uncovered" means the bound is missing, weak, switched off, ineffective, or jumped over by the path it was meant to stop [1].

The census that came out of that work is small and sharp. All 68 confirmed failures carried a missing strong bound, and in 26 of them, the exit still belonged to the model itself [1].

**The part I keep circling:** the big frameworks ship these controls already. LangChain has `max_iterations`, LangGraph has recursion limits, the OpenAI Agents software development kit (SDK) has a turn limit, and CrewAI has `max_iter` [1].

The paper's own conclusion is that the controls settle nothing on their own. Teams skip them, set them badly, or place them where they do not cover the loop that really repeats [1].

## By the numbers

- **68 loops — Confirmed failures:** hand review confirmed 68 runaway-loop failures across 47 of the 6,549 scanned agent repositories. Reviewers flagged 74 candidates and confirmed 68, at 91.9% precision [1].
- **65 of 68 — Cost exhaustion:** API cost exhaustion was the recorded impact in 65 confirmed failures. Model denial of service hit the same 65, and context-window exhaustion hit 19 [1].
- **26 of 68 — Model-owned exit:** the exit relied on the model's own output in 26 confirmed failures. A tool-controlled retry decided it in 28, and a strong bound was missing in all 68 [1].
- **1000 steps — LangGraph's graph default:** the documented default recursion limit since version 1.0.6. The core library's own reference still documents 25 for its call-recursion setting [2][3].

<!-- tactical-insight -->

## What I'd watch:

I am watching four places the bound leaks in what operators actually report.

- **Inherited defaults:** LangGraph's graph page documents a default recursion limit of 1000 super-steps since version 1.0.6 [2]. The core library's own reference still says a call recursion limit defaults to 25 [3]. Which number a run gets depends on the layer that sets it.
- **Subagents:** an issue in the project's own tracker describes a parent capped at 150 (or 300) whose subagents still ran at the framework default of 25. They died on tasks of 13 or more tool calls [4]. The issue is now closed.
- **Iteration is not time:** CrewAI stops an agent at 20 iterations by default, and leaves `max_execution_time` unset unless you set it [5]. A step cap is not a clock, and neither one is a dollar cap.
- **The bill shows up first:** the recorded impact in the census was cost, not a wrong answer [1]. Two agents arguing in a loop keep producing believable output the whole time.

**What I'm watching next:** whether the static pass that found these loops becomes routine before release, just like a standard code linter.

<!-- nuanced-takeaway -->

## The catch

The census counts confirmed failures in real code. It is a sorting key for frameworks, not a verdict on them, and the paper does not claim a default caused any of these loops [1]. 

A tracker item is a snapshot too. The one behind the subagent number is closed, so a later release may handle it in a different way [4].

My read: I see the 1000-step graph default as the more dangerous of the two numbers, because it is the one a team receives without asking. A thousand steps of tool calls is a bill with a plan attached [2].

The other edge of the trade shows up in the desk's own field case. An unconstrained two-agent critique loop burned $4,200 in credits in 45 minutes before rate limits stopped it [6]. 

The fix in that note was a recursion budget of five steps, plus a cost ceiling for each session [6].

Five steps would cut off plenty of honest long runs. That is the trade every bound forces: pick the failure you prefer, a bill or a cut-off task.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Autonomous & Agentic Workflows" -> /categories/autonomous-agentic-workflows/ [same site (giniloh.com); same category; the article's own category hub (Autonomous & Agentic Workflows:)] Link "Autonomous & Agentic Workflows" in the section where the article touches this topic. -->
<!-- internal-link hint: "One Approval, Two Payments" -> /one-approval-two-payments/ [same site (giniloh.com); same category] Link "One Approval, Two Payments" in the section where the article touches this topic. -->
## Related reading

- [Autonomous & Agentic Workflows](/categories/autonomous-agentic-workflows/) — more on Artificial Intelligence & Future of Work
- [One Approval, Two Payments](/one-approval-two-payments/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A static scan of 6,549 agent repositories confirmed 68 runaway loops across 47 projects. Every one of them was missing a limit that really governed the repeating path.
- **Why It Matters:** The recorded impact in 65 of the 68 was API cost exhaustion. The defaults a team inherits also sit at different layers and versions: a graph default of 1000 steps, a core reference of 25, an iteration cap of 20, and subagents that do not take their parent's limit.
- **What I'd Watch:** whether teams start checking bound coverage before a release, and which layer they pin it to.
  - **Where the bound lives:** a limit the model's own output can hold open is not a bound; 26 of the 68 confirmed failures still had a model-owned exit.
  - **What it covers:** a limit written beside a loop is not a limit over the loop, so static checks now sort bounds into covered and uncovered.
  - **Which default you inherit:** graph defaults, core-library defaults, and subagent paths disagree, so the number you get depends on the layer that sets it.
- **The Catch:** the census is a snapshot, not a verdict on any framework, and a tight bound trades a runaway bill for cut-off honest work.

## Sources
[1] Hou, Wang, Zhao & Wang — "When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents," arXiv:2607.01641v1 [cs.SE] (2026-07-02) — https://arxiv.org/html/2607.01641v1
[2] LangChain documentation — LangGraph Graph API, "Recursion limit" (default 1000 steps since version 1.0.6) — https://docs.langchain.com/oss/python/langgraph/graph-api
[3] LangChain Reference — langchain_core RunnableConfig.recursion_limit ("If not provided, defaults to 25") — https://reference.langchain.com/python/langchain-core/runnables/config/RunnableConfig/recursion_limit
[4] langchain-ai/deepagents — Issue #1698, "SubAgentMiddleware does not propagate recursion_limit to subagent graphs" (closed) — https://github.com/langchain-ai/deepagents/issues/1698
[5] CrewAI documentation — Agents (max_iter default 20; max_execution_time optional) — https://docs.crewai.com/concepts/agents
[6] Editorial-factory field notes, agentic_ai Anecdote 1 (internal, anonymised) — context/growth_os/customer-truth.md

## Gate report
PASS — lead delivers the core 68 loops stat immediately in sentence 1, with zero preamble.
PASS — tension includes 'The big picture:' and 'By the numbers' with 4 bolded stats properly formatted.
PASS — tactical-insight uses 'What I'd watch:' with clear, bolded observation bullets and no commands.
PASS — nuanced-takeaway offers 'The catch' and highlights honest tradeoffs with first-person observation.
PASS — tldr follows the 4-part Smart Brevity format perfectly with sub-bullets under What I'd Watch.
