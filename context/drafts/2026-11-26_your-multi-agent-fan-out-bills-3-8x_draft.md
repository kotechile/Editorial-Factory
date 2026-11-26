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
Perplexity now sells a Multiagent tier. One lead agent runs a team of up to 16 agents on models from different labs, and the team cross-checks its own work [1]. That same week, the first equal-cost study priced the fan-out bill at 3.8× one agent's spend. The gain it measured was 1 to 5 points on hidden tests [3]. The fan-out bills several times more and buys a margin a single sentence mostly recovers. For anyone writing the budget line under an agent platform, a quality setting just became a price tag.

<!-- tldr -->
## At a glance
Two facts landed nine days apart: a vendor tier that scales agents to sixteen, and an equal-cost experiment measuring what the parallel pattern returns. This piece is for AI architects and platform engineers who price agent runs, and its finding is that the default fan-out overpays.

<!-- tension -->
## The fan-out met its price tag
On 17 November, Perplexity's launch post described the new effort level. One lead agent assigns up to 16 workers on Claude Opus 5.5, GPT (OpenAI's model line) 6.1 Sol and Gemini 4 Carbon. The agents share findings directly and check each other's work [1]. On 24 November, a practitioner essay on Kalzumeus called multiagent coding "as much of a paradigm shift as LLMs coding" [2]. On 25 November, the measurement arrived [3].

The study then compared one agent against a main agent that delegates to subagents — child agents spawned to work in parallel. The tasks came from the NL2Repo and ProgramBench benchmarks. Both build a whole code base from a written spec. Parallel subagents added just 1 to 5 points of hidden-test pass rate, a gap that held across model versions [3]. That margin cost 2.6 to 3.8 times a single agent's spend [3]. At equal cost, the single agent scored the same or better [3].

The mechanism matters more than the average. The gain showed up where a lone agent had stopped checking its own work too early. With OpenAI's GPT (the model line behind ChatGPT) 5.6 Sol, one sentence did most of that work. Told to probe the reference program first, the single agent won back most of the subagent gain at a fraction of the cost [3]. With the newer GPT 6.1 Sol, the gain shrank further as the lone model checked itself more [3]. A fan-out, in other words, partly pays for checking a better-instructed lone agent does alone.

## By the numbers
- **Up to 16 agents:** the cap on a lead's team in Perplexity's new effort level [1].
- **3.8× the bill:** the top of the parallel cost range against one agent on ordinary tasks [3].
- **82% lower cost:** what a budget-aware router paid to match the strongest multi-agent system [5].

<!-- tactical-insight -->
## Where the bill is being trimmed
I find this week's reactions telling, because neither side argues for dropping the pattern. A coordination benchmark circulated on Hacker News showed the failure plainly. Three agents pushed separate fixes for the same bug at once, and merge conflicts threw away two of the three [4]. The research answer to that waste is a router, not fewer ideas. MeterRouter treats each query's budget as a hard cap. It matched the strongest multi-agent router's accuracy at 82% lower cost [5]. A separate benchmark found the flip side of that problem. Models above 27 billion parameters got worse as the graph grew longer, and working runs spent more model calls than the shortest route needed [6]. Architects who run these shapes will see their own incident notes there. The [multi-agent failure topology](/agent-failure-topology-not-model/) problem this desk mapped last month is the same duplicated-work bill this week's study prices.

<!-- nuanced-takeaway -->
## The catch
The study's own scope keeps this from being an anti-parallel verdict. Gains were larger on hard tasks. The parallel runs produced more modular code, with more files and shorter functions [3]. And the one-sentence probe fix did not transfer to DeepSeek's open harness or to NL2Repo [3]. What the evidence supports is narrower than either the marketing or my own fear. On ordinary code work, the parallel bill does not pay for itself by default. The margin you can win back sits in the instruction, the fresh context and the routing policy, not in the agent count. Until a vendor prints a cost column beside its agent-count slider, the buyer holds the pencil.

## Sources
- [1] Perplexity, "Introducing Multiagent for the most complex work", 2026-11-17 — https://www.perplexity.ai/hub/blog/introducing-computer-multiagent
- [2] Patrick McKenzie, "Multiagent coding is the future", 2026-11-24 — https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/
- [3] arXiv, "When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction", 2026-11-25 — https://arxiv.org/abs/2611.33893
- [4] Bespoke Labs, "Multi Agent Coordination Bench", 2026-11-18 — https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/
- [5] arXiv, "MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems", 2026-11-25 — https://arxiv.org/abs/2611.34327
- [6] arXiv, "CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems", 2026-11-24 — https://arxiv.org/abs/2611.33242
