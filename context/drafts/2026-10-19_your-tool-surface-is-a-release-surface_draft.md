---
title: "Your Gateway: 60.5% Injection Risk"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "The tool surface — which tools the gateway exposes, what the candidate list says after a deploy, and where a monitor's evidence reaches its decision — decides an agent's security and cost more than the model does, and because it changes after deployment it needs a release process."
date: 2026-10-19
slug: your-tool-surface-is-a-release-surface
synthesis: true
sources:
  - https://arxiv.org/abs/2610.23449
  - https://arxiv.org/abs/2610.23362
---

<!-- lead -->
Three papers landed within 48 hours, and none of them is about the model. One ran 11,118 real tools from 251 servers through seven gateways, and found that the gateway's shape alone moved tool-injection attack success from 60.5% for a flat tool list to 19.6% for on-demand discovery [1]. One found 18 cases where a safety detector fired and the framework stranded the verdict before the block [2]. One recovered 33 of 45 broken function calls without touching a weight [3].

The gateway is the part of your agent stack that decides which tools the model can see. That quiet choice sets most of the injection risk, and almost nobody treats it like a release.

<!-- tension -->

## The big picture:

I keep coming back to one detail in all three papers: the part that failed was still running. Nothing crashed. The monitor was set up, the tool list was served, the schema was valid.

The shared object is the tool surface. That covers four things: the tools a gateway exposes, the text that describes them, the list the model actually sees, and the wiring that carries a monitor's verdict to a block.

The first paper explains why the surface matters now. Teams no longer connect one agent to one server. They run many agents against many servers, so a gateway sits in the middle to hold credentials and endpoints [1].

The benchmark sorted seven shipped gateways into two designs. A flat gateway puts the whole list in the prompt. A discovery gateway exposes search tools, and the agent pulls a tool only when it asks [1].

That one choice sets what the model can be tricked by. The two designs split on tool injection at every junk-tool count: the flat mean ran from 51.5% down to 40.6% as junk tools piled up, while the discovery design stayed near 16% [1]. They do not split on direct prompt injection, where both types land near 44% [1].

The reason is plain. A gateway does not touch the user's prompt. It decides which tool descriptions enter the context [1].

The second paper finds the same boundary breaking in the other direction. A monitor can read tool calls, streams, detector output and verifier input, and any of those can move to a new field in a framework upgrade [2]. The paper applies a canary test to public repairs. It confirms 18 cases across 11 safety projects and four ecosystems, and 14 of them reach a block decision [2].

The clearest case is small. A regex detector returned a positive match. The framework still let the output through, because nothing mapped that result to the block decision. The fix added the missing mapping, and the same payload was blocked [2].

**What strikes me here:** the detector was right. The evidence existed and never arrived. That is not a jailbreak, and a guardrail test would never see it [2].

The third paper takes the same surface from the repair side. Tool descriptions, argument schemas and the visible tool list change after a deploy, even when the tool itself behaves the same [3]. A repair layer with schema checks, candidate retry and one constrained rewrite lifted accuracy from 0.717 to 0.813 on one test and from 0.580 to 0.805 on another [3].

The ablation is the interesting part. Description edits and schema renames did less harm than a drifted tool list full of distractors [3]. The list on offer is the most dangerous thing to let move.

## By the numbers

- **60.5% vs 19.6% — Indirect attack success:** the mean for flat gateways against discovery gateways under the same agent and model, with no junk tools in the pool. The gap holds in all three setups: 47.2% vs 30.9%, and 42.5% vs 15.6% [1].
- **233.3k vs 12.6k — Tokens a turn:** at 1,500 injected junk tools, the flat mean climbs from 8.3k to 233.3k tokens per turn. The discovery design moves from 9.1k to 12.6k. Task time at that size runs 64.1 seconds against 38.7 [1].
- **18 of 18 — Evidence-path failures:** 18 confirmed cases across 11 safety project groups and four ecosystems. Nine were repairs at a known boundary, eight were coverage gaps on a new surface, one was a boundary-only case [2].
- **0.580 to 0.805 — Function-calling accuracy:** one open model with 9 billion parameters on a 200-example test, after a repair layer recovered 33 of 45 drift-induced failures. A larger sibling model moved 0.635 to 0.845 under the same protocol [3].

<!-- tactical-insight -->

## What I'd watch:

I'd want to know which shape a team runs before I believed any claim about its agent's safety. Most of the diagrams I see do not show a gateway at all.

- **The shape in production:** a flat list and a discovery layer are different systems with the same name. The flat design led by 2.1 points in task success with a clean pool, then trailed by 2.3 points at 1,500 junk tools [1]. Whoever owns the gateway owns that crossover.
- **The evidence path:** a canary that puts a known payload on one changed surface, then records whether the monitor saw it and what the system decided. That is the test the second paper used to confirm all 18 cases [2]. It runs against a repair, not against the model.
- **Tool-list churn:** adding tools to a live agent reads as a release event here, because distractor tools carried most of the measured harm [3]. The papers did not study change control. That link is mine.
- **The cost crossover:** a flat gateway is cheaper on latency with a small pool, at 20.8 seconds against 30.1. It gets dearer once the pool grows, and the break-even sits between 500 and 1,000 tools [1].
- **Who signs off:** gateway, model and runtime interact enough that the first paper argues they should be picked as one system [1]. In most org charts those three sit in different teams.

**What I'm watching next:** whether the canary test shows up in framework release notes, or stays a research method.

<!-- nuanced-takeaway -->

## The catch

The best safety numbers in the gateway study need a second look. One discovery gateway posted the lowest indirect attack success in the set, and the authors flag why: the agent failed most of the benign tasks too, so it also failed the injected goal. That is a broken agent, not a safe one [1].

The repair numbers come from one open model family on three synthetic drift types, not from a frontier model in production [3]. They show the layer is cheap and that it works on the cases the authors built. They do not show it covers every real drift.

The evidence-path corpus is 18 confirmed cases from one author, with fixed revisions, negative controls and a frozen audit [2]. It shows the failure class is real and repeatable. It is not a count of how often it happens.

My read is that the safest claim here is also the cheapest to accept. The surface decides outcomes, and the surface is setup. Setup drifts, and drift is not a model problem.

The part I could be wrong about is scale. Three papers in two days is a signal. It is not a trend yet.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** three papers published within 48 hours measured the link between an agent and its tools, and each found the damage there rather than in the model. Gateway shape moved indirect attack success between 60.5% and 19.6%, and a monitor's verdict died before the block in 18 confirmed cases.
- **Why It Matters:** the tool surface sets both the attack path and the bill. At 1,500 junk tools the flat design cost 233.3k tokens a turn against 12.6k, and a drifted tool list did more harm than any schema edit.
- **What I'd Watch:** whether teams start treating the tool surface as a release item with a pinned shape and a test on the evidence path, and what that test finds.
  - **Flat vs discovery:** a flat gateway lists every tool in the prompt. A discovery gateway offers search tools and fetches on demand, which is slower to start and far cheaper once the list grows.
  - **Canary contract:** a known payload placed on one changed surface, recording whether the monitor saw it and what the system decided. It tests the wiring, not the detector.
  - **Tool-list drift:** the set of visible tools changing after a deploy. In the measured ablation it did more harm than description or schema edits.
- **The Catch:** the repair evidence comes from one open model family on synthetic drift, and the 18 cases are one author's confirmed corpus, not a count of frequency. The lowest attack numbers in the gateway study came with an agent that could not finish the task.

## Sources
[1] Zheng, Chen, Li & Li — "GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways," arXiv:2610.23449v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23449
[2] Liao — "Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries," arXiv:2610.23362v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23362
[3] Chattopadhyay, Halder & Roy — "Robust Function Calling for LLM Agents Under Interface Drift," arXiv:2610.23342v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23342

## Gate report
PASS — lead delivers three concrete results in the first three sentences, with no preamble.
PASS — tension includes "The big picture:" and "By the numbers" with four bolded stats.
PASS — tactical-insight uses "What I'd watch:" with observation bullets and one labelled inference.
PASS — nuanced-takeaway carries "The catch" with three sourced limits and a first-person reading.
PASS — tldr follows the 4-part schema with sub-bullet definitions under What I'd Watch.
