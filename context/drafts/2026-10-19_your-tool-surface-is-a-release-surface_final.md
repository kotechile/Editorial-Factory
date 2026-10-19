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
image_path: "context/assets/illustrations/your-tool-surface-is-a-release-surface/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "The Gateway Injection Risk. A modular mechanical inspection gate interlocking with a solid processing module on a brushed"
image_caption: "The Gateway Injection Risk: How tool surfaces drive most agent injection risks."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Three new research papers landed within 48 hours, and none of them focus on the model. One ran 11,118 real tools from 251 servers through seven gateways. It found the gateway's design alone dropped tool-injection attack success from 60.5% to 19.6% [1]. Another found 18 cases where a safety detector fired and the verdict never reached the block [2]. A third recovered 33 of 45 broken function calls without touching a model weight [3].

The gateway is the part of your agent stack that decides which tools the model can see. That quiet choice sets most of your injection risk, yet almost nobody treats it like a software release.

<!-- tension -->

## The big picture:

I keep coming back to one detail across all three papers: the part that failed was still running. 

Nothing crashed. The monitor was set up, the tool list was served, and the data schema was valid.

The shared point of failure is the tool surface. It covers four things: the tools on offer, the text that describes them, the list the model sees, and the wiring from a monitor's verdict to a block.

The first paper explains why this surface matters now. Teams no longer connect one agent to one server. They run many agents against many servers, placing a gateway in the middle to hold credentials and endpoints [1].

The benchmark sorted seven shipped gateways into two designs. A flat gateway puts the entire tool list directly in the prompt. A discovery gateway exposes search tools, so the agent pulls a tool only when it asks [1].

That single choice dictates what tricks the model. The two designs split on tool injection at every junk-tool count. The flat mean ran from 51.5% down to 40.6% as junk tools piled up, while the discovery design stayed near 16% [1]. They do not split on direct prompt injection, where both types land near 44% [1].

The reason is plain. A gateway does not touch the user's prompt. It decides which tool descriptions enter the context window [1].

The second paper finds the same boundary breaking in the other direction. A monitor can read tool calls, streams, detector output, and verifier input. Any of those can move to a new field during a framework upgrade [2]. 

The paper applies a canary test to public repairs. It sends a known payload and checks whether the system catches it. The test found 18 cases across 11 safety projects and four ecosystems. Of those, 14 reach a block decision [2].

The clearest case is small. A regular expression (regex) text pattern detector returned a positive match. The framework still let the output through because nothing mapped that result to the actual block decision. The fix added the missing mapping, and the system blocked the same payload [2].

**What strikes me here:** the detector was right. The evidence existed but never arrived. That is not a jailbreak, and a guardrail test would never see it [2].

The third paper addresses the same surface from the repair side. Tool descriptions, schemas and the tool list change after a deploy, even when the tool behaves the same [3]. A repair layer uses schema checks, candidate retries and one constrained rewrite. It lifted accuracy from 0.717 to 0.813 on one test, and from 0.580 to 0.805 on another [3].

Testing the parts one by one revealed the most interesting detail. Description edits and schema renames did less harm than a drifted list full of junk tools [3]. The list on offer is the most dangerous thing to let move.

## By the numbers

- **60.5% vs 19.6% — Indirect attack success:** mean rate for flat gateways compared to discovery gateways running the same agent and model, with zero junk tools in the pool [1].
- **233.3k vs 12.6k — Tokens a turn:** token usage at 1,500 injected junk tools, where the flat mean climbs to 233.3k while the discovery design reaches only 12.6k [1].
- **18 — Evidence-path failures:** cases found across 11 safety project groups and four ecosystems. Nine were repairs at a known boundary, eight were gaps on a new surface, and one was a boundary-only case [2].
- **0.580 to 0.805 — Function-calling accuracy:** one open model with 9 billion parameters, on a 200-example test. A repair layer recovered 33 of 45 drift-induced failures [3].

<!-- tactical-insight -->

## What I'd watch:

I'd want to know which shape a team runs before I believed any claim about its agent's safety. 

Most diagrams do not show a gateway at all.

- **The shape in production:** a flat list and a discovery layer are different systems with the same name. The flat design led by 2.1 points in task success with a clean pool, then trailed by 2.3 points at 1,500 junk tools [1]. Whoever owns the gateway owns that crossover.
- **The evidence path:** a canary test puts a known payload on one changed surface. It records if the monitor saw it, and what the system decided. That test confirmed all 18 cases by running against a repair, not against the model [2].
- **Tool-list churn:** adding tools to a live agent reads as a release event. Junk tools carried most of the measured harm [3]. The papers did not study change control, but that link is mine.
- **The cost crossover:** a flat gateway is cheaper on latency with a small pool, taking 20.8 seconds against 30.1. It gets dearer as the pool grows, with a break-even between 500 and 1,000 tools [1].
- **Who signs off:** gateway, model, and runtime interact enough that they should be picked as one system [1]. In most org charts, those three sit in different teams.

**What I'm watching next:** whether the canary test shows up in framework release notes or stays a research method.

<!-- nuanced-takeaway -->

## The catch

The best safety numbers in the gateway study need a second look. 

One discovery gateway posted the lowest indirect attack success in the set. The authors flag why: the agent failed most of the benign tasks too. It failed the injected goal because it is a broken agent, not a safe one [1].

The repair numbers come from one open model family on three synthetic drift types, not from a frontier model in production [3]. They show the layer is cheap and works on the cases the authors built, but they do not prove it covers every real drift.

The evidence-path corpus is 18 cases from one author, with fixed revisions, negative controls, and a frozen audit [2]. It shows the failure class is real and repeatable, not how often it happens.

My read is that the safest claim here is also the cheapest to accept. The surface decides outcomes, and the surface is setup. Setup drifts, and drift is not a model problem.

The part I could be wrong about is scale. Three papers in two days is a signal, but it is not a trend yet.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** three papers published within 48 hours measured the link between an agent and its tools, finding the damage there rather than in the model. Gateway shape moved indirect attack success between 60.5% and 19.6%, and a monitor's verdict died before the block in 18 confirmed cases.
- **Why It Matters:** the tool surface sets both the attack path and the bill. At 1,500 junk tools, the flat design cost 233.3k tokens a turn against 12.6k, and a drifted tool list did more harm than any schema edit.
- **What I'd Watch:** whether teams start treating the tool surface as a release item with a pinned shape and a test on the evidence path, and what that test finds.
  - **Flat vs discovery:** a flat gateway lists every tool in the prompt. A discovery gateway offers search tools and fetches on demand. It is slower to start and far cheaper once the list grows.
  - **Canary contract:** a known payload placed on one changed surface. It records if the monitor saw it, and what the system decided. It tests the wiring, not the detector.
  - **Tool-list drift:** the set of visible tools changing after a deploy. In the measured test, it did more harm than description or schema edits.
- **The Catch:** the repair evidence comes from one open model family on synthetic drift, and the 18 cases are one author's confirmed corpus, not a count of frequency. The lowest attack numbers in the gateway study came with an agent that could not finish the task.

## Sources
[1] Zheng, Chen, Li & Li — "GatewayBench: Unified Capability and Security Evaluation Platform for MCP Gateways," arXiv:2610.23449v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23449
[2] Liao — "Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries," arXiv:2610.23362v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23362
[3] Chattopadhyay, Halder & Roy — "Robust Function Calling for LLM Agents Under Interface Drift," arXiv:2610.23342v1 [cs.AI] (2026-10-16) — https://arxiv.org/abs/2610.23342

## Gate report
PASS — lead delivers three concrete results in the first paragraph, with zero throat-clearing.
PASS — tension structures the narrative with H2s, translates "ablation" and "regex", and formats the numbers correctly.
PASS — tactical-insight frames observations clearly under "What I'd watch:" without commanding the reader.
PASS — nuanced-takeaway accurately addresses the limitations of the studies and includes a first-person perspective.
PASS — tldr follows the 4-part Smart Brevity schema with indented sub-bullets under What I'd Watch.
