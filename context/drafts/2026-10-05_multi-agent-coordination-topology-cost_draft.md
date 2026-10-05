---
title: "Multi-Agent Coordination: Pick the Topology That Pays"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Coordination topology is a cost-and-verifiability decision, not a capability flex: parallel fan-out buys breadth at roughly 15× the tokens, a deliberative ensemble buys factual reliability, and sequential handoffs keep the bill flat."
date: 2026-10-05
slug: multi-agent-coordination-topology-cost
archetype: evergreen
evergreen: true
meta_title: "Multi-Agent Coordination: Pick the Topology That Pays"
meta_description: "Anthropic's agent swarm beat a single model by 90.2% and used about 15 times the tokens. The coordination mode, not the model, is the real budget line."
---

<!-- lead -->
Anthropic's multi-agent research system beat a single Claude Opus 4 agent by 90.2% on an internal research eval, and it used about 15 times the tokens to get there [1]. That one trade — more capability for a much bigger bill — is why coordination topology is now an architecture decision rather than a fashion.

The three modes teams actually ship are parallel fan-out, sequential handoff, and a deliberative ensemble. Wiring the wrong one is how an agent program quietly runs out of budget.

<!-- tension -->

## The big picture:

For two years, "multi-agent" meant a chat room of models talking to each other. The evidence now says the wiring — how the agents pass state, not how clever each model is — decides both the result and the cost.

What changed is that agent stacks grew up into distributed systems: an orchestrator, scoped subagents, and shared state. So the question moved from whether agents can collaborate to which topology earns its bill.

My read: the modes are not interchangeable, and the cheapest one is the most underused.

## By the numbers

- **90.2% — Fan-out upside:** Anthropic's system, with an Opus 4 lead and Sonnet 4 subagents, outperformed a single Opus 4 agent on its internal research eval [1].
- **~15× — Token multiplier:** Those multi-agent runs used about 15 times the tokens of a single chat, and an agent alone about 4 times a chat [1].
- **14 — Design failure modes:** A 150-trace study sorted multi-agent breakdowns into 14 modes across 3 categories: system design, inter-agent misalignment, and task verification [2].
- **65.1% — Ensemble score:** A layered ensemble of open models hit 65.1% on AlpacaEval 2.0, ahead of GPT-4 Omni at 57.5% [3].

<!-- tactical-insight -->

## What I'd watch:

I've been watching how the teams closest to this wire their runtimes, and four choices keep coming up.

- **Fan-out for breadth, not for everything:** Anthropic's orchestrator spawns subagents to chase independent directions at once. The 90.2% gain arrived with the 15× bill, so it pays only where the task's value is high [1]. The part I keep circling is how often that condition fails quietly.
- **Sequential handoff for pipelines:** A coordinated multi-agent conversation framework reached the top of the GAIA benchmark by about 8 points, with each agent working on the step before it [4]. It is the mode that ships while the debate about swarms continues.
- **A deliberative ensemble when output must be checkable:** Layered aggregation pushed AlpacaEval 2.0 to 65.1%, ahead of a single GPT-4 Omni at 57.5% [3]. Extra passes over the same question buy factual reliability, at the cost of latency.
- **The failure budget, not the model:** MAST's 150-trace analysis found the dominant failures are system design and misalignment, not a weak model [2]. I'd want to know which coordination choice removes a whole category rather than patching one symptom.

<!-- nuanced-takeaway -->

## The catch

The evidence is young. Anthropic's 90.2% is one internal eval, and the multipliers are its own measurement [1]. MAST's 14 modes come from 150 traces [2], and the ensemble result is a 2024 benchmark [3].

I could be wrong that topology dominates. A weak model in a clean topology still fails, and a strong model in a flat loop still works. The risk I'd watch is fan-out landing on tasks whose value never justified the 15× bill.

<!-- tldr -->

## At a glance

- **The Big Shift:** Multi-agent work is now a topology decision. Parallel fan-out, sequential handoff, and deliberative ensembles each buy something different, at a different price.
- **Why It Matters:** The coordination mode, not the model, is the real budget line. A fan-out that adds 90.2% capability while spending 15 times the tokens is a win on a high-value task and a quiet loss on a low-value one.
- **What I'd Watch:** I'm watching how teams match the mode to the work, and where the failure bill lands.
  - **Fan-out:** An orchestrator spawns subagents that chase independent directions at once, buying breadth and paying the biggest token multiplier.
  - **Sequential handoff:** Each agent works on the step before it, which keeps cost flat and ships today.
  - **Deliberative ensemble:** Several passes answer the same question and combine, buying factual reliability at the cost of latency.
- **The Catch:** The evidence is thin and mostly self-reported — one internal eval, a 150-trace study, and a 2024 benchmark. Topology helps, but it does not rescue a bad model or a low-value task.

## Sources

[1] Anthropic Engineering, "How we built our multi-agent research system" (2025). https://www.anthropic.com/engineering/multi-agent-research-system
[2] Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657 (v1 2025-03-17). https://arxiv.org/abs/2503.13657
[3] Wang et al., "Mixture-of-Agents Enhances Large Language Model Capabilities," arXiv:2406.04692 (2024-06-07). https://arxiv.org/abs/2406.04692
[4] Microsoft Research, "AutoGen: Enabling next-gen LLM applications via multi-agent conversation framework." https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/

<!-- linkedin -->
I've been reading the multi-agent papers all week, and one number from Anthropic stopped me: its research agents beat a single top model by 90.2% — and spent about 15 times the tokens doing it.

That trade is the whole story. Multi-agent work is a topology decision now, and there are three modes worth comparing.

Fan-out gives you breadth and the biggest token bill. A sequential handoff keeps cost flat — the AutoGen conversation framework reached the top of GAIA by about 8 points that way. A deliberative ensemble buys factual reliability; a layered one hit 65.1% on AlpacaEval 2.0, ahead of GPT-4 Omni.

My read: the mode, not the model, is the real budget line. And the failures agree — a 150-trace study found the dominant breakdowns are system design and misalignment, not a weak model.

What I'm watching next: how often fan-out lands on tasks whose value never justified the 15× bill. The catch is that the evidence is thin — one internal eval, one failure study, and a 2024 benchmark.

Curious which mode people are actually shipping in production.
