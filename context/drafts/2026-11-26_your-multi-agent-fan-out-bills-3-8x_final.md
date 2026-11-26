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
image_path: "context/assets/illustrations/your-multi-agent-fan-out-bills-3-8x/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "Parallel Agents Bill 3.8X For Five Points. Glass prism splitting one beam of light into sixteen parallel copper rays across a steel bench"
image_caption: "Parallel Agents Bill 3.8X For Five Points: Perplexity sells agent count as a tier while one instruction line buys the gain back."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A vendor now sells agent count as a tier, because buyers treat team size as a quality dial. Perplexity's new Multiagent effort level puts one lead agent over up to 16 workers on models from rival labs, and the team checks its own work [1]. The same week, the first equal-cost study priced that pattern at 2.6 to 3.8× one agent's spend. The gain was 1 to 5 points on hidden tests [3]. The fan-out bills several times more, and one instruction sentence mostly buys the gain back. If you write the budget line under an agent platform, a quality setting just became a price tag.

<!-- tldr -->

## At a glance

Two things landed nine days apart: a vendor tier that scales agent teams to sixteen, and an equal-cost study measuring what the parallel pattern actually returns. This piece is for AI architects and platform engineers who price agent runs, and its finding is that the default fan-out overpays.

<!-- tension -->

## The fan-out met its price tag

On 17 November, Perplexity's launch post described the new effort level: one lead agent assigns up to 16 workers across Claude Opus 5.5, OpenAI's Generative Pre-trained Transformer (GPT) model GPT-6.1 Sol and Gemini 4 Carbon, and the agents share findings and check each other's work [1]. On 24 November, a practitioner essay on Kalzumeus argued, as conviction rather than measurement, that multiagent coding is "as much of a paradigm shift as LLMs coding" [2]. On 25 November, the measurement arrived [3].

The study compared one agent against a main agent that hands work to subagents — child agents started to run in parallel. The tasks came from the NL2Repo and ProgramBench benchmarks. Both build a whole code base from a written spec. Parallel subagents added just 1 to 5 points of hidden-test pass rate, a gap that held across model versions [3]. That margin cost 2.6 to 3.8 times a single agent's spend, and at equal cost the single agent scored the same or better [3].

What strikes me is the mechanism, not the average. The gain showed up where a lone agent had stopped checking its own work too early. With OpenAI's GPT-5.6 Sol, one sentence did most of that work. Told to probe the reference program first, the single agent won back most of the subagent gain at a fraction of the cost [3]. With the newer GPT-6.1 Sol, the gain shrank further as the lone model checked itself more [3]. A fan-out, in other words, partly pays for checking that a better-instructed lone agent does alone.

## By the numbers

- **Up to 16 agents:** the cap on a lead's team in Perplexity's new effort level [1].
- **3.8× the bill:** the top of the parallel cost range against one agent on ordinary tasks [3].
- **82% lower cost:** what a budget-aware router paid to match the strongest multi-agent system [5].

<!-- tactical-insight -->

## Where the bill is being trimmed

I've been watching this week's reactions, and neither side argues for dropping the pattern. A coordination benchmark circulated on Hacker News showed the failure plainly: three agents pushed separate fixes for the same bug at once, and merge conflicts threw away two of the three [4]. The research answer to that waste is a router, not fewer ideas. MeterRouter treats each query's budget as a hard cap, and it matched the strongest multi-agent router's accuracy at 82% lower cost [5]. A separate benchmark found the flip side. Models above 27 billion parameters got worse as the graph grew longer. Working runs spent more model calls than the shortest route needed [6].

**What I'd watch:** architects who run these shapes will recognize their own incident notes. The duplicated-work bill this study prices is the same one [multi-agent failure topology](/agent-failure-topology-not-model/) problem this desk mapped last month.

<!-- nuanced-takeaway -->

## The catch

My read is that the study's own scope keeps this from being an anti-parallel verdict. Gains were larger on hard tasks. The parallel runs also produced more modular code — more files, shorter functions [3]. The one-sentence probe fix also did not transfer to DeepSeek's open-source agent harness (dsh) or to NL2Repo [3]. So the evidence supports something narrower than either the marketing or the alarm this bill first provokes: on ordinary code work, the parallel bill does not pay for itself by default. The margin you can win back sits in the instruction, the fresh context and the routing policy, not in the agent count. Until a vendor prints a cost column beside its agent-count slider, the choice sits with the buyer.

## Sources

- [1] Perplexity, "Introducing Multiagent for the most complex work", 2026-11-17 — https://www.perplexity.ai/hub/blog/introducing-computer-multiagent
- [2] Patrick McKenzie, "Multiagent coding is the future", 2026-11-24 — https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/
- [3] arXiv, "When Are Parallel Subagents Effective for Coding? An Empirical Study on Repository Construction", 2026-11-25 — https://arxiv.org/abs/2611.33893
- [4] Bespoke Labs, "Multi Agent Coordination Bench", 2026-11-18 — https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/
- [5] arXiv, "MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems", 2026-11-25 — https://arxiv.org/abs/2611.34327
- [6] arXiv, "CypherMAS: Benchmarking Routing Reliability in LLM-Based Multi-Agent Systems", 2026-11-24 — https://arxiv.org/abs/2611.33242

