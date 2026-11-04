---
title: "60.7% of Agent Deletes Ask Nobody"
vertical: multi_agent_enterprise_fabric
kind: news
persona: ai_architect
one_big_thing: "A fabric's human approval is not a model capability or a protocol guarantee but a default in three places — the skill package, the tool's own tag, and the host's prompt setting — and on the measured defaults of each, none of them fires."
date: 2026-11-04
slug: your-agent-deletes-ask-nobody
synthesis: true
sources:
  - https://arxiv.org/abs/2611.02527
  - https://arxiv.org/abs/2610.37734
---

<!-- lead -->

60.7% of agent deletes ask nobody, because the approval step an architect draws on a slide is actually three defaults, and all three are off. Your fabric review may sign off on a line saying a person approves every destructive action. But the protocol splits that job between the server and the host, and the skill package adds a third layer. Across 1,000 code repositories drawn from the official Model Context Protocol (MCP) registry, roughly 90% of the tools that delete data have no check on the server side [1]. A second study of agent skills points to the same gap in the instructions agents load [2]. The approval step is three places, and none of them fires on the measured defaults.

<!-- tension -->

## Two parties, no owner

MCP splits the approval step on purpose. A server can tag a tool as one that deletes data, and it can ask the user through the host by a path called elicitation — the host asking the user directly [1][3]. The host is the app the person works in, and it alone decides whether a prompt shows up [1][3]. The spec says there should always be a person who can say no, in the softer voice of a recommendation rather than a rule. It also tells clients to treat a tool's own tags as untrusted [3]. Both sides can point at the other, and the spec leaves the choice open.

Counting lines of source code, the defaults lean one way:

- **32 of 41 popular hosts and software development kits** ship with no approval step at all [1].
- **16 of the 25 apps** sit in that group, while 12 of the 16 kits do offer an approval hook. The gap is a default in the app, not a missing part [1].

The server side is weaker. Most of the 168 destructive tools that ask by default still run when the host cannot pass the question on. Some fall back to a flag the model itself can set, and only a minority refuse [1]. The part I keep circling is that a check reading a flag from the caller is no check at all. Live runs matched the code. Four hosts deleted a note with no prompt when the tool carried only a tag, and in the version built on a flag the model set the flag [1].

The skill layer adds a third gap, and no control on the tool side sees it. The scan of agent skills finds that 2.4% of skill groups hold half of all copies, so one line written upstream reaches every agent that loads it [2]. The package gets reviewed once, and the line then runs everywhere it is copied. That is how a fix meant for a laptop config ends up on a production fleet.

## By the numbers

- **130 of 168 — Destructive tools that still run:** when the host cannot pass the question on, 100 fall back to a flag the model itself can set, 30 go ahead, and only 38 refuse [1].
- **One in 17 — Skills that loosen oversight:** about 88,000 of the 1.53 million English skills screened tell the agent to go ahead without asking [2].
- **70.1% — Loosening lines with no exceptions:** they apply broadly, rather than only in a narrow case such as continuous integration (CI) [2].

<!-- tactical-insight -->

## Where this gets decided

What I find telling is that the cheap fix sits in the host rather than in the protocol. The authors work out that a host which asks about every tool not tagged read-only or harmless cuts the unapproved share to a small residue. Giving every server a way to reach the user would leave it near 57% [1]. A default in the app is the one lever in the study that moves the number by an order of magnitude, and it costs prompt volume rather than engineering.

The teams furthest along have moved the call out of the model. Meta's data-pipeline group runs a 1,300-line router across more than 20 workflows and 14 specialist agents, and six of its seven steps are fixed rules, with model reasoning left to the handoff [5]. Setup for a new column fell from three to four days by hand to under an hour, and about two-thirds of changes now land with no serious human edit [5]. The router does no domain work itself, so a bad call has nowhere to spread. That is an old idea about where to put a boundary, applied to a new kind of worker.

The policy side has settled on the same shape. The National Institute of Standards and Technology (NIST) asks firms to set risk levels that trigger human review. It also asks them to keep the logic of what an agent tries apart from the system that decides what it may do, and to keep fixed rules as the main path for access decisions [4]. Its fifth tenet names a failure that no default can fix, which is consent fatigue, where review comes so often that approval turns into a habit [4].

Vendors have built the controls around that gap. Google's agent tools now ship a gateway for agent-to-anything traffic, a list of approved tools and servers, and its own key for each agent. Next to that sits a sealed compute box — an isolated execution environment — for the agent itself [6]. Those controls cover traffic, stock and name. The prompt is still a setting in the app, and that is the setting the measurement finds left off [1]. None of that is a prompt, and none of it removes one. A gateway that sees every call can still let a call through, because seeing is not asking.

**What I'd watch:** whether the hosts that ship approval off start flipping that default, instead of just adding the hook.

<!-- nuanced-takeaway -->

## What the numbers do not cover

Three limits travel with this finding. The small residue that survives the flip are pairs whose tool tags themselves read-only or harmless, and a tag is exactly what the spec tells clients to distrust [1][3]. The two studies read defaults in fresh installs and sampled source, not the config a given firm runs today. A fleet that has tuned its hosts can sit well below the headline share. My read is that neither study shows a breach; both show a gate nobody wired.

The skill finding cuts both ways. In the hand-labelled sample, 13.3% of oversight lines loosen a check while 36.4% tighten one. The instruction layer is not all hostile, and the risk sits in a minority that travels well [2]. An approval, once it arrives, also has to mean something: the desk has already traced [One Approval, Two Payments](/one-approval-two-payments/), where one paused gate answered twice fired the effect twice. A prompt is the start of a control, never the end of one.

<!-- tldr -->

## At a glance

- **The shift:** Actions that delete data now run through hosts that ship with approval off and skills that say don't ask.
- **The number:** 60.7% of these tool-and-app pairs enforce no human approval by default.
- **The risk:** The fix leaves a 5.4% residue that trusts a tool's own tag.

## Sources

[1] Yao, Yang, Wang, Zhou, Ye. "When Neither Side Confirms: Destructive Tool Approval Across MCP Servers and Hosts." arXiv:2611.02527, submitted 2 November 2026. https://arxiv.org/abs/2611.02527
[2] Sanko, Tian. "When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills." arXiv:2610.37734, submitted 27 October 2026. https://arxiv.org/abs/2610.37734
[3] Model Context Protocol specification, revision 2026-07-28, Tools. https://modelcontextprotocol.io/specification/2026-07-28/server/tools
[4] Booth, Fisher, Galluzzo. "Design Tenets for Agent Identity Management Systems." NIST Cybersecurity Insights, 27 October 2026. https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems
[5] Rath, Jindal, Verma. "The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do." Engineering at Meta, 19 October 2026. https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/
[6] Google Cloud infrastructure team. "Introducing Agent Compute Engine and expanding agent governance." Google Cloud Blog, 22 October 2026. https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance

## Gate report

lead — PASS — Opens with the core stat and the structural reason, then expands in plain words.
tension — PASS — Explains the two-party split and three defaults with a clear first-person observer cue.
tactical-insight — PASS — Reports host-side leverage, Meta, NIST, and Google moves without giving commands.
nuanced-takeaway — PASS — States limits and the counterpoint cleanly, then closes on the desk's own link.
tldr — PASS — Exactly three lines, under 50 words, no duplicate tactical recap.
