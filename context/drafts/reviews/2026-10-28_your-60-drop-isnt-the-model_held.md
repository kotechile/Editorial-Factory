---
title: "Your 60% Drop Isn't the Model"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "In an agent fabric the two things that decide the outcome are the shape of the tool interface and the stack that wraps it, both picked before any model test: a fault study shows a 60% task-score collapse with no gain from a model six times larger, and a controlled interface study shows 94.3% of paired runs going different ways on the same tools."
date: 2026-10-28
slug: your-60-drop-isnt-the-model
synthesis: true
sources:
  - https://arxiv.org/abs/2610.34298
  - https://arxiv.org/abs/2610.32555
---

<!-- lead -->

Your agent's task score fell 60% when its tools broke the way the Model Context Protocol (MCP) ecosystem says they fail. A model six times larger kept no more of its score than the small one [1]. That collapse is not a model failure, but the bill for two choices finalized when a firm selects a fabric. The outcome depends on the shape every tool call takes, and the stack sitting behind that call when it snaps.

<!-- tension -->

## The big picture

Two papers landed six days apart, and they measure the exact variables a standard procurement review skips. One broke MCP tool calls on purpose and checked what survived [1]. The other held the tools steady and altered only how they appeared to the models [2]. Neither team tested the other's axis. I read these two papers side by side and see a sharp warning about where an agent fabric gets its reliability.

The first study did not invent its failures, reading the mix from 57,240 issue threads across 1,774 open-source MCP servers and finding mostly permanent breakage [1]. It then ran 1,350 test cells over two model sizes, three agent stacks and three fault types. Task score fell from 8.08 to 3.23 out of 10, a drop of 4.85 points. The 120-billion model from the same family held no more of its clean score than the 20-billion one, with 91.1% of tasks finished against 95.6% [1]. The stack moved the result more than the model did, landing at 95% to 97% on one, 88% to 95% on another and 91% to 95% on the third [1].

The second study built one set of actions and two ways to show them: MCP tools and Command-Line Interface (CLI) commands, both run through the same runtime [2]. Across six models and three task worlds, the two runs went different ways in 94.3% of 2,004 paired cases. The split showed up in which action a model chose, how it failed and how it recovered [2]. When the authors fixed only how an action was carried out, leaving the decision alone, the score rose in all six settings by up to 9.0 points. MCP token use fell by up to 27,100 a task [2].

Public tests cannot settle this debate with a single success rate. One vendor ran 75 identical GitHub jobs: the CLI side finished 25 of 25, the MCP side 18 of 25, and every miss was a connection timeout [3]. A separate 50-task study across two business-like worlds found the edge flip by task. CLI pulled ahead where the work meant wide reading, MCP won on a narrow lookup, and the gap dropped for the newest models [4]. Its cost finding proves the point: the same interface was cheaper on one harness and dearer on another [4].

Vendors are shipping the parts that make this choice invisible. MuleSoft calls Agent Fabric a control plane for agents, MCP servers and interfaces. Its 21 October release adds local agent-network tests over an Agent-to-Agent (A2A) chat link plus per-model Open Authorization (OAuth) client credentials [5]. Systems, Applications, and Products (SAP) moved its agent suite to general release, acting inside workflows on the records' own permissions [6]. Both are sensible products that meter policy and identity, yet neither measures what the port does to the agent.

## By the numbers

- **60% — Task score under faults:** score fell from 8.08 to 3.23 out of 10, a paired drop of 4.85 points (range −5.22 to −4.48), against failures drawn from 57,240 incident threads [1].
- **94.3% — Runs that split on matched tools:** with the same actions on the same runtime, MCP and CLI agents went different ways in 2,004 paired runs, changing action choice, failure path and recovery [2].
- **91.1% vs 95.6% — The larger model under faults:** a 120-billion model against a 20-billion one from the same family, with no larger share of its clean score kept (p = 0.96) [1].
- **Up to 9.0 points and 27,100 tokens — Interface repair, best case:** fixing only how an action was carried out moved all six settings and cut MCP token use in all three worlds [2].

<!-- tactical-insight -->

## What I'd watch:

- **Whether the fabric's interface test exists at all.** The method is cheap to copy, requiring one set of actions, two shapes, one runtime and your own task mix [2]. What it rules out is borrowing a number from someone else's mix, since the two public tests disagree on direction [3][4]. What I am watching is whether enterprise teams start building these internal benchmarks before signing contracts.
- **Fault profiles read from your own vendor.** The most useful step in the fault study is how it picked its failures before it tested anything [1]. A fabric tried out on clean tools has measured its good day and nothing else.
- **Stack-level error handling as a scored line.** The 88% to 95% against 95% to 97% gap under the same faults is the first published sign that the wrapper decides survival [1]. The interface study found the harness could flip a cost ranking on its own [4].
- **Handoff continuity as the next number to ask for.** A study out on 27 October ran 1,039 tasks across six receiving models [7]. It finds that finding the evidence again is not the same as carrying the work forward, with the best receiver changing by track [7]. That is the measure an A2A fabric needs next.

<!-- nuanced-takeaway -->

## The catch

The 60% is a stress result, not a field rate. The faults came from a mix heavy in permanent breakage, testing 25 single-server tasks and one model family [1]. The authors call the stack finding a hint rather than a settled fact, with the two tests at p = 0.048 and p = 0.074 [1]. This is also the reviewed paper of the two, accepted as a poster at the Neural Information Processing Systems conference.

The interface study is a preprint, and its models sit well below the frontier. It tested four Qwen3 sizes, one DeepSeek Flash tier and one Gemini Flash tier on three simulated task worlds [2]. That matters because the commercial test found the interface effect shrinking as models get better [4]. If that holds, the shape half of this argument is a cost that fades, while the fault half does not. The flat line ran from 20-billion to 120-billion inside one family [1]. My reading is that the interface test earns its keep on the private, mid-sized models most firms run, while the fault test applies everywhere.

What neither paper shows is a fabric in production. Both measure one boundary in a controlled setting, and the vendors selling the control plane make no claim beyond it, selling policy, identity and cost over a list of agents [5][6]. The honest read is that the two things with the largest measured effect are the two the buying decision leaves untested.

<!-- tldr -->

## At a glance

- **The Big Shift:** Two October papers split the agent fabric's outcome across two things nobody compares. One shows a 60% task-score fall under realistic MCP faults, with no gain from a model six times larger [1]. The other shows 94.3% of paired runs going different ways when only the shape of the tool interface changes [2].
- **Why It Matters:** The interface shape and the stack behind it are set once, at fabric choice. Both carry effects larger than any model shortlist will show, while the control planes now on sale meter policy, identity and cost instead.
- **What I'd Watch:** The next round of fabric choices will be argued with borrowed numbers, and those numbers disagree.
  - **Interface test:** run your own task mix through two shapes of the same actions on one runtime, then compare the runs and not a single success rate.
  - **Fault injection:** read the failure mix from your own vendor's real incidents, because a clean-tool test cannot see the effect.
  - **Handoff continuity:** check whether a receiving agent carries the work forward, not just whether it can find the evidence again.
- **The Catch:** The 60% comes from a mix heavy in permanent breakage, on 25 single-server tasks and one model family. The interface study is an unreviewed preprint on mid-sized models, and the stack finding is a hint rather than a settled fact.

## Sources

[1] Iannillo, Owotogbe, Natella, Avallone, Kudryavtseva, Kumara. "Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance." arXiv:2610.32555, submitted 23 October 2026; accepted as a poster at the Neural Information Processing Systems conference. https://arxiv.org/abs/2610.32555
[2] Shi, Pang, Li. "Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents." arXiv:2610.34298, submitted 25 October 2026. https://arxiv.org/abs/2610.34298
[3] Madabhushi, Ravi. "MCP is up to 32× more expensive than CLI. Here's why we still use it." Scalekit, 11 March 2026. https://www.scalekit.com/blog/mcp-vs-cli-use
[4] Hou, Dumitru, Arakelyan, Zhang, Wang, Li, Rane. "MCP vs. CLI: Does an AI Agent's Tool Interface Still Matter?" Scale Labs, 8 July 2026. https://labs.scale.com/blog/mcp-vs-cli
[5] MuleSoft. "Agent Fabric Release Notes," entries dated 31 August 2026 and 21 October 2026. https://docs.mulesoft.com/release-notes/agent-fabric/agent-fabric-release-notes
[6] SAP News. "SAP Puts the Autonomous Enterprise to Work," 6 October 2026. https://news.sap.com/2026/10/sap-connect-sap-puts-autonomous-enterprise-to-work
[7] Li, Li, Li, Maeda, Ogawa, Haseyama. "Benchmarking Task Takeover Across Agent Handoffs." arXiv:2610.36523, submitted 27 October 2026. https://arxiv.org/abs/2610.36523
