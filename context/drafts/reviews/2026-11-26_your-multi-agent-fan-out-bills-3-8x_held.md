---
title: "Your Agent Fan-Out Bills 3.8×: 16 Agents, One Price Tag"
vertical: agentic_ai
meta_title: "Your Agent Fan-Out Bills 3.8×: 16 Agents, One Price Tag"
meta_description: "A 16-agent tier went on sale the same week the first equal-cost study priced the fan-out bill at 3.8× a single agent for 1–5 test points. Headcount is the wrong dial."
primary_keyword: "agent fan-out"
secondary_keywords: [parallel subagents, multi-agent orchestration]
kind: news
persona: ai_architect
one_big_thing: "Perplexity put a 16-agent fan-out on sale the same week a study priced parallel subagents at 3.8× the bill for 1–5 test points. Headcount is the wrong dial."
date: 2026-11-26
slug: your-multi-agent-fan-out-bills-3-8x
synthesis: true
sources:
  - https://www.perplexity.ai/hub/blog/introducing-computer-multiagent
  - https://arxiv.org/abs/2611.33893
---

<!-- lead -->
Perplexity now sells a Multiagent tier, and the first equal-cost study of the pattern landed the same week. One lead agent runs a team of up to 16 agents on models from different labs, and the team cross-checks its own work [1]. The study priced the parallel bill at 2.6 to 3.8 times one agent's spend, for 1 to 5 extra points on hidden tests [3]. A single sentence of instruction won most of that margin back. For anyone writing the budget line under an agent platform, the agent-count slider is now a cost dial.

<!-- tldr -->
## At a glance
A 16-agent vendor tier and the first equal-cost study of parallel subagents landed nine days apart. This piece is for architects who price agent runs, and its finding is that the default fan-out overpays for what it returns.

<!-- tension -->
## The fan-out met its price tag
The dates first, in order. On 17 November, Perplexity's launch post described the new effort level, a tier above Ultra for its Computer product, open to Max subscribers on the web [1]. On 24 November, a practitioner essay on Kalzumeus called multiagent coding "as much of a paradigm shift as LLMs coding" [2]. On 25 November, the measurement arrived [3].

The launch itself is a fan-out by design. One lead agent assigns up to 16 workers on Claude Opus 5.5, GPT (OpenAI's model line) 6.1 Sol and Gemini 4 Carbon, with Claude Fable 5.2 planning the split. The agents share findings directly and check each other's work, and the lead merges the results into one deliverable [1]. The announcement carries no cost figure. The study does.

It compared one agent against a main agent that delegates to parallel subagents — child agents spawned to work at the same time. The tasks came from the NL2Repo and ProgramBench benchmarks, which both build a whole code base from a written spec. On randomly drawn tasks, the subagents added 1 to 5 points of hidden-test pass rate, a gap that held across model versions [3]. That margin cost 2.6 to 3.8 times a single agent's spend [3]. At equal cost, the single agent scored the same or better [3].

The mechanism matters more than the average. The gain appeared where a lone agent had stopped checking its own work too early. With OpenAI's GPT (the model line behind ChatGPT) 5.6 Sol, one sentence did most of that work: told to probe the reference program first, the single agent won back most of the subagent gain at a fraction of the cost, reaching 75% on the atlas benchmark [3]. With the newer GPT 6.1 Sol, the gain shrank further, because the lone model checked itself more [3]. The fan-out partly pays for checking that a better-instructed single agent does alone.

## By the numbers
- **Up to 16 agents:** the cap on a lead's team in Perplexity's new effort level [1].
- **3.8× the bill:** the top of the parallel cost range against one agent on randomly drawn tasks [3].
- **82% lower cost:** what a budget-aware router paid to match the strongest multi-agent system [5].

<!-- tactical-insight -->
## Where the bill is being trimmed
I read the reactions this week as a search for the right dial, because nobody close to the pattern argues for dropping it. A coordination benchmark from Bespoke Labs showed the waste plainly. Three agents pushed separate fixes for the same bug at once, and merge conflicts threw away two of the three [4]. The research answer to that duplicated work is a router, not fewer agents. MeterRouter treats each query's budget as a hard cap, and it matched the strongest multi-agent router's accuracy at 82% lower cost [5]. A separate benchmark, CypherMAS, found the flip side: models above 27 billion parameters got worse as the graph grew longer, and working runs spent more model calls than the shortest route needed [6]. Routing, not headcount, is where both papers put the leverage. The failure topology this desk mapped last month is the same duplicated-work bill this week's study prices.

<!-- nuanced-takeaway -->
## The catch
The study's own scope keeps this from being an anti-parallel verdict, and my reading, held loosely, is that the honest summary is a hedge. Gains were larger on hard tasks. The parallel runs also produced more modular code, with more files and shorter functions [3]. And the one-sentence probe fix did not transfer to dsh (DeepSeek's open-source agent harness) or to NL2Repo [3]. So the claim is narrow: on ordinary code work, the default fan-out does not pay for itself, and the recoverable margin sits in the instruction, the fresh context and the routing policy — not in the agent count. Until a vendor prints a cost column beside its agent-count slider, the buyer holds the pencil.

## Sources
- [1] Perplexity, "Introducing Multiagent for the most complex work", 2026-11-17 — https://www.perplexity.ai/hub/blog/introducing-computer-multiagent
- [2] Patrick McKenzie, "Multiagent coding is the future", 2026-11-24 — https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/
- [3] arXiv, "When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction", 2026-11-25 — https://arxiv.org/abs/2611.33893
- [4] Bespoke Labs, "Multi Agent Coordination Bench", 2026-11-18 — https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/
- [5] arXiv, "MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems", 2026-11-25 — https://arxiv.org/abs/2611.34327
- [6] arXiv, "CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems", 2026-11-24 — https://arxiv.org/abs/2611.33242
