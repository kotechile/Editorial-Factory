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
meta_title: "Your 60% Drop Isn't the Model"
meta_title_source: "derived_from_title"
meta_description: "Your agent's task score drops 60% when its tools break the way the Model Context Protocol (MCP) ecosystem says they fail, from 8.08 out of 10 to 3.23."
meta_description_source: "derived_from_lead"
---

<!-- lead -->

Your agent's task score drops 60% when its tools break the way the Model Context Protocol (MCP) ecosystem says they fail, from 8.08 out of 10 to 3.23 [1]. A model six times larger keeps no more of its score than a small one. A second study gave six models the same actions in two formats, and the agents changed what they did in 94.3% of 2,004 paired episodes [2]. That drop isn't the model. It is the bill for two choices made once, when a firm picks a fabric: the shape every tool call arrives in, and what sits behind the call when it breaks.

<!-- tension -->

## The big picture

Once a firm settles on one agent fabric, it takes on the results for every agent built on top. I read the two October papers side by side, and together they cover what a buying review tends to skip. One team broke MCP tool calls on purpose and measured what survived. The other held the tools still and changed only how the actions were shown to six models [1][2]. Neither varied the other's factor. Read together, they say where the result of a fabric really comes from.

The first study did not invent its failures. It pulled the mix from 57,240 issue threads across 1,774 open-source MCP servers, which is mostly permanent breakage. It then ran 1,350 test cells over two model sizes, three agent stacks and three fault types [1]. Task score fell from 8.08 to 3.23 out of 10, a drop of 4.85 points. Scale bought nothing: the 120-billion model from the same family held no more of its clean score than the 20-billion one, finishing 91.1% of tasks against 95.6% [1]. The stack moved the outcome much further: 88% to 95% on one, 91% to 95% on the second, 95% to 97% on the third [1].

The second study built one set of actions and showed them two ways, as MCP tools and as command-line interface (CLI) commands, both running through one shared runtime [2], and across six models and three test worlds the runs then diverged in 94.3% of 2,004 paired cases. The split changed which action a model chose, how it failed and how it recovered [2]. When the authors fixed only how an action was carried out, leaving the decision alone, the score rose in all six settings by up to 9.0 points. MCP token use fell by up to 27,100 a task [2]. Same tool, different port.

Public tests cannot settle this with one success rate. One vendor ran 75 identical GitHub jobs. The CLI side finished 25 of 25, MCP 18 of 25, and every miss was a timeout [3]. A separate 50-task study across two business settings found the advantage flipped by task. CLI led where the work demanded wide reading, MCP led on narrow lookups, and the gap shrank for the newest models [4].

Vendors are shipping the plumbing that makes the choice invisible. MuleSoft markets a control plane for agents, MCP servers and interfaces. Its 21 October release adds local agent-network tests over an Agent-to-Agent (A2A) chat link, plus per-model OAuth client credentials [5]. SAP (the German business-software vendor) moved its agent suite to general release, wiring assistants into business workflows on the records' own permissions [6]. Both are sensible controls, and neither meters what the port does to the agent.

## By the numbers

- **60% — Task score under faults:** score fell from 8.08 to 3.23 out of 10, a paired drop of 4.85 points (range −5.22 to −4.48), against failures drawn from 57,240 incident threads [1].
- **94.3% — Runs that split on matched tools:** with the same actions on the same runtime, MCP and CLI agents went different ways in 2,004 paired runs, changing action choice, failure path and recovery [2].
- **91.1% vs 95.6% — The larger model under faults:** a 120-billion model against a 20-billion one from the same family, with no larger share of its clean score kept (p = 0.96) [1].
- **Up to 9.0 points and 27,100 tokens — Interface repair, best case:** fixing only how an action was carried out moved all six settings and cut MCP token use in all three worlds [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your 60% Drop Isn&#x27;t the Model</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Task score under faults</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="180" height="18" rx="4" fill="#818cf8"/>
  <text x="430" y="84" fill="#f1f5f9" font-size="13" font-weight="600">60%</text>
  <text x="484" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Runs that split on matched tools</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="282" height="18" rx="4" fill="#818cf8"/>
  <text x="532" y="132" fill="#f1f5f9" font-size="13" font-weight="600">94.3%</text>
  <text x="586" y="132" fill="#64748b" font-size="11">([2])</text>
  <!-- Row 3 -->
  <text x="20" y="180" fill="#e2e8f0" font-size="13" font-weight="500">The larger model under faults</text>
  <rect x="240" y="166" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="166" width="273" height="18" rx="4" fill="#818cf8"/>
  <text x="523" y="180" fill="#f1f5f9" font-size="13" font-weight="600">91.1%</text>
  <text x="577" y="180" fill="#64748b" font-size="11">([1])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

- **Whether the fabric interface test exists at all.** The method is cheap to copy: one set of actions, two shapes, one runtime, your own task mix [2]. What I am watching next is whether buyers stop borrowing numbers from other people's mixes; the two public tests disagree on direction [3][4].
- **Fault profiles read from your own vendor.** The most useful step in the fault study is how it picked its failures before testing anything [1]. A fabric tried on clean tools has measured its best day and nothing else.
- **Stack-level error handling as a scored line.** The 88% to 95% against 95% to 97% gap under the same faults is the first published sign that the wrapper decides survival [1], and the interface study found the harness could flip a cost ranking on its own [4]. The same split shows up from [the failure side](/agent-failure-topology-not-model/), where the shape of the run, not the model, decides how a multi-agent failure spreads.
- **Handoff continuity as the next number to ask for.** A study published on 27 October ran 1,039 tasks across six receiving models. It finds that locating the evidence again is not the same as carrying the work forward, and the best receiver changes by track [7]. That is the measure an A2A fabric needs next.

<!-- nuanced-takeaway -->

## The catch

The 60% is a stress result, not a field rate. The faults came from a mix heavy in permanent breakage, were run on 25 single-server tasks and one model family, and the threat model covers everyday breakage rather than an attacker, limited to the tool call itself [1]. The authors call the stack finding a hint rather than a settled fact, with the two tests at p = 0.048 and p = 0.074 [1]. This is also the reviewed paper of the two, accepted as a poster at the Neural Information Processing Systems conference.

The interface study is an unreviewed preprint, and its models sit well below the frontier: four Qwen3 sizes, one DeepSeek Flash tier and one Gemini Flash tier, on three test worlds [2]. That matters, because the vendor test found the interface effect shrinking as models get better [4]. If that trend holds, the shape half of this argument is a cost that fades, while the fault half does not, since the flat line ran from 20-billion to 120-billion inside one family [1]. Where I've landed: the interface test earns its keep on the private, mid-sized models most firms actually run, and the fault test earns it everywhere.

What neither paper shows is a fabric in production: both measure one boundary in a controlled setting, and the vendors selling the control plane make no claim beyond it, selling policy, identity and cost over a list of agents [5][6]. The honest position is that the two things with the largest measured effect are the two the buying decision leaves untested, which argues for a local test rather than another vendor.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> /durable-execution-not-a-transaction/ [same site (aichieve.net); same category; topical overlap: context, model, protocol, tools] Link "Durable Execution Is Not a Transaction" in the section where the article touches context, model, protocol. -->
<!-- internal-link hint: "Stop Piling Memory Onto AI Agents" -> /maskills-multi-agent-skills-optimization/ [same site (aichieve.net); same category; topical overlap: agent's, drop, score] Link "Stop Piling Memory Onto AI Agents" in the section where the article touches agent's, drop, score. -->
<!-- internal-link hint: "Your Agent's Next Step" -> /gate-the-step-not-the-model/ [same site (aichieve.net); same category; topical overlap: agent's, fail] Link "Your Agent's Next Step" in the section where the article touches agent's, fail. -->
## Related reading

- [Durable Execution Is Not a Transaction](/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
- [Stop Piling Memory Onto AI Agents](/maskills-multi-agent-skills-optimization/) — more on Autonomous & Agentic Workflows
- [Your Agent's Next Step](/gate-the-step-not-the-model/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Two October papers split the agent fabric's outcome across two variables nobody compares. One shows a 60% task-score fall under realistic MCP faults, with no gain from a model six times larger [1]. The other reveals 94.3% of paired runs going different ways when only the shape of the tool interface changes [2].
- **Why It Matters:** The interface shape and the stack behind it are set once, at fabric choice, and both carry effects larger than any model shortlist will show, while the control planes now on sale meter policy, identity and cost instead.
- **What I'd Watch:** The next round of fabric choices will rely on borrowed numbers, and those numbers disagree.
  - **Interface test:** run your own task mix through two shapes of the same actions on one runtime, comparing the runs rather than a single success rate.
  - **Fault injection:** read the failure mix from your own vendor's real incidents, measuring what finishes under it, because a clean-tool test cannot see the effect.
  - **Handoff continuity:** check whether a receiving agent carries the work forward, not just whether it can find the evidence again.
- **The Catch:** The 60% comes from a mix heavy in permanent breakage, evaluated on 25 single-server tasks and one model family. The interface study is an unreviewed preprint on mid-sized models, and the stack finding remains a hint rather than a settled fact.

## Sources

[1] Iannillo, Owotogbe, Natella, Avallone, Kudryavtseva, Kumara. "Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance." arXiv:2610.32555, submitted 23 October 2026; accepted as a poster at the Neural Information Processing Systems conference. https://arxiv.org/abs/2610.32555
[2] Shi, Pang, Li. "Matched Capabilities, Different Behaviors: A Controlled Study of MCP and CLI Interfaces for Language Agents." arXiv:2610.34298, submitted 25 October 2026. https://arxiv.org/abs/2610.34298
[3] Madabhushi, Ravi. "MCP is up to 32× more expensive than CLI. Here's why we still use it." Scalekit, 11 March 2026. https://www.scalekit.com/blog/mcp-vs-cli-use
[4] Hou, Dumitru, Arakelyan, Zhang, Wang, Li, Rane. "MCP vs. CLI: Does an AI Agent's Tool Interface Still Matter?" Scale Labs, 8 July 2026. https://labs.scale.com/blog/mcp-vs-cli
[5] MuleSoft. "Agent Fabric Release Notes," entries dated 31 August 2026 and 21 October 2026. https://docs.mulesoft.com/release-notes/agent-fabric/agent-fabric-release-notes
[6] SAP News. "SAP Puts the Autonomous Enterprise to Work," 6 October 2026. https://news.sap.com/2026/10/sap-connect-sap-puts-autonomous-enterprise-to-work
[7] Li, Li, Li, Maeda, Ogawa, Haseyama. "Benchmarking Task Takeover Across Agent Handoffs." arXiv:2610.36523, submitted 27 October 2026. https://arxiv.org/abs/2610.36523
