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
image_path: "context/assets/illustrations/multi-agent-coordination-topology-cost/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "The Cost Of Agent Topology. A modular brushed-aluminum pneumatic manifold valve block fanning out into multiple channels on a"
image_caption: "The Cost Of Agent Topology: How agent wiring choices dictate your token budget."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Anthropic's new multi-agent research system beat a single Claude Opus 4 agent by 90.2% on a private test, but it burned about 15 times the tokens to do it [1]. That massive token bill shows that how you wire agents together is a choice about money, not just a tech trick. Teams use three main setups: spreading tasks out widely, passing work down a line step-by-step, or asking a group to vote on the best answer. Picking the wrong setup is a fast way to drain a budget without noticing.

<!-- tension -->

## The big picture:

For two years, a multi-agent setup just meant a chat room where artificial intelligence (AI) models talked to each other. Now, these setups run as real software systems. 

They use a main controller to hand out work, smaller agents to do specific jobs, and a shared memory to track progress. How these agents pass their work along decides both the final answer and the final bill. My read: these three setups do very different jobs, and builders often skip the cheapest option.

## By the numbers

- **90.2% — Fan-out upside:** Anthropic's setup, using an Opus 4 lead and Sonnet 4 subagents, beat a single Opus 4 agent on a private research test [1].
- **~15× — Token multiplier:** The team's multi-agent runs used about 15 times the tokens of a single chat [1].
- **14 — Design failure modes:** A study of 150 traces sorted multi-agent crashes into 14 types across system design, bad agent alignment, and task checking [2].
- **65.1% — Ensemble score:** A layered voting group of open models hit 65.1% on the AlpacaEval 2.0 test, beating a single Generative Pre-trained Transformer (GPT)-4 Omni model at 57.5% [3].

<!-- tactical-insight -->

## What I'd watch:

I have been watching how teams wire their systems, and four choices keep coming up.

- **Fan-out for wide searches:** Anthropic's main controller creates smaller agents to chase different ideas at the same time. The 90.2% gain arrived with a 15× token bill [1]. This wide net only makes sense when the task is worth the high cost. The part I keep circling is how often teams pay this massive bill for simple tasks that do not need it.
- **Sequential handoffs for pipelines:** A step-by-step chat framework reached the top of the General AI Assistant (GAIA) test by about 8 points [4]. Each agent simply works on the step right before it. This keeps the token bill flat and predictable. It is the setup that works best right now while people still argue about massive agent swarms.
- **A deliberative ensemble for checking facts:** Grouping models in layers pushed the AlpacaEval 2.0 score to 65.1% [3]. Multiple passes over the same question buy a more truthful answer. The trade-off is that it takes much longer to get a reply, which slows down the whole system.
- **The failure budget:** A study of 150 agent runs found that most crashes come from bad system design and poor alignment, not a weak model [2]. I would want to know which wiring choice removes a whole class of errors, rather than just patching one symptom.

<!-- nuanced-takeaway -->

## The catch

The proof for all of this is still very new and mostly self-reported. Anthropic's 90.2% jump is just one private test, and the cost multipliers are their own numbers [1]. 

The 14 crash types come from a small set of 150 runs [2]. The group voting win relies on a 2024 benchmark [3]. I could be wrong that the wiring matters most. A bad model in a clean setup still fails, and a great model in a messy loop still works. The risk I would watch is teams using expensive, wide-net setups on tasks that never justify the massive token bill.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> https://giniloh.com/planner-as-router-fold-the-model-choice-into-the-plan/ [same site (giniloh.com); same category; topical overlap: agent, system] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches agent, system. -->
<!-- internal-link hint: "MCP Skills Extension" -> https://giniloh.com/mcp-skills-extension/ [same site (giniloh.com); same category; topical overlap: agent] Link "MCP Skills Extension" in the section where the article touches agent. -->
<!-- internal-link hint: "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" -> https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/ [same site (giniloh.com); topical overlap: pays, single] Link "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" in the section where the article touches pays, single. -->
## Related reading

- [Planner-as-Router: Fold the Model Choice Into the Plan](https://giniloh.com/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows:
- [MCP Skills Extension](https://giniloh.com/mcp-skills-extension/) — more on Autonomous & Agentic Workflows:
- [NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…](https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Multi-agent work is now a wiring choice. Spreading tasks out, passing tasks down a line, and group voting each buy something different at a different price.
- **Why It Matters:** The wiring choice, not the model, drives the real cost. A setup that adds 90.2% more skill while spending 15 times the tokens is great for a high-value task, but a quiet loss for a cheap one.
- **What I'd Watch:** I am watching how teams match the setup to the work, and where the errors happen.
  - **Fan-out:** A main controller makes smaller agents chase different paths at once, buying a wider search but charging the highest token fee.
  - **Sequential handoff:** Each agent works linearly on the step right before it, which keeps costs flat and ships easily today.
  - **Deliberative ensemble:** Multiple passes look at the same prompt to buy a more truthful answer, though it slows down the reply.
- **The Catch:** The data is thin and mostly self-reported. Good wiring helps, but it does not fix a bad model or make a cheap task worth a massive bill.

## Sources

[1] Anthropic Engineering, "How we built our multi-agent research system" (2025). https://www.anthropic.com/engineering/multi-agent-research-system
[2] Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657 (v1 2025-03-17). https://arxiv.org/abs/2503.13657
[3] Wang et al., "Mixture-of-Agents Enhances Large Language Model Capabilities," arXiv:2406.04692 (2024-06-07). https://arxiv.org/abs/2406.04692
[4] Microsoft Research, "AutoGen: Enabling next-gen LLM applications via multi-agent conversation framework." https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/

<!-- linkedin -->
I have been reading the latest multi-agent papers all week, and one number from Anthropic stopped me. Its new research agents beat a single top model by 90.2%, but they spent about 15 times the tokens to do it.

That trade is the whole story. Multi-agent work is a wiring choice now, and there are three setups worth comparing.

Spreading tasks out widely gives you a broad search and the biggest token bill. Passing tasks down a line keeps costs flat. The step-by-step AutoGen framework reached the top of the General AI Assistant (GAIA) test by about 8 points that way. A group voting setup buys better facts. A layered group hit 65.1% on AlpacaEval 2.0, ahead of a single Generative Pre-trained Transformer (GPT)-4 Omni model.

My read: the setup, not the model, is the real budget line. The failures back this up. A study of 150 runs found the main crashes come from bad system design, not a weak model.

What I am watching next: how often teams use expensive, wide-net setups on tasks that never justified the massive token bill. The catch is that the proof is still thin—one private test, one failure study, and a 2024 benchmark.

Curious which setup people are actually shipping in production?

## Gate report
lead: PASS — Direct, punchy opening sentence delivering the core news and token tradeoff immediately in plain English.
tension: PASS — Clear structural shift explained in simple words, with a distinct first-person observer cue.
tactical-insight: PASS — Translates complex topologies into clear, observable use cases with a strong first-person framing and zero commands.
nuanced-takeaway: PASS — Highlights the limitations of the data using clear, direct language and an observer cue.
tldr: PASS — Strictly follows the 4-part Smart Brevity schema with correctly formatted nested bullets.
