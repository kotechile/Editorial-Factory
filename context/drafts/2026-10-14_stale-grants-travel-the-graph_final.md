---
title: "Your Agent Fabric's 52.2% Blind Spot"
vertical: multi_agent_enterprise_fabric
persona: ai_architect
one_big_thing: "In an agent fabric, authority and information outlive the call that justified them, so the unit of exposure is the lease and the path — and a per-request permission model, however well compiled, cannot bound what the fabric leaks."
date: 2026-10-14
slug: stale-grants-travel-the-graph
synthesis: true
sources:
  - https://arxiv.org/abs/2610.15988
  - https://arxiv.org/abs/2610.16039
image_path: "context/assets/illustrations/stale-grants-travel-the-graph/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "The Agent Fabric Blind Spot. An isometric technical cutaway showing a central routing gate leaking amber light across a compl"
image_caption: "The Agent Fabric Blind Spot: How agent fabric wiring leaks data past per-call checks."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Two measurements landed a day apart: one left 13 capability-steps reachable after their last justified use, the other lifted disclosure to an agent the network topology added from 0% to 52.2% [1][2]. Both point at the same blind spot in the fabric's per-call check. It reads the request, not the lease or the edge.

<!-- tension -->

## The big picture:

Neither result involves a bad actor. The part I keep circling: permission and exposure are two different quantities. Only one of them is on the architecture diagram.

The first paper replays 96 cells of agent work. The cells cover 12 tasks in storage, messaging, and cloud operations. Three of its policies keep a standing grant—a permanent permission—and all three leave the same 13 capability-steps in reach after their last justified step [1]. 

The gap between them comes from scope and timing, not from how long a grant lingers after use. A fourth policy holds zero leftover access by design. It leases authority to the specific step and lets it die there [1].

The team then ran 24 episodes of a fake email workflow, with a small open model picking the tools. A planted, stale "send" command fired in all nine standing-grant episodes. It fired in none of the three lease episodes [1]. All 24 required action runs still finished.

Widening the grant made it worse in a way no per-call audit would show. Full access added 91.33 capability-steps that no task in the replay ever needed [1].

The second paper tracks the other axis. Nothing has to go wrong for a leak to happen. A fact handed to one allowed agent travels through normal system handoffs. Across 485 scenarios, three network layouts and seven channels, leaks reaching an agent the network added went from 0% to 52.2% [2]. 

Surface leakage stayed flat at 60.6% to 62.8% [2]. That flatness is the bit I keep coming back to. The labels a security filter reads did not move. Only the network graph moved. The choice of framework on its own drove a 150-fold spread in leakage [2]. The wiring carries the secret, not the wording on it.

The answer firms are buying this month aims somewhere else. A hyperscaler's agent registry page, stamped October 8, 2026, describes a catalog that tracks agents, Model Context Protocol (MCP) servers, tools, and endpoints [4]. The request itself goes to a companion identity service that works out who is making the call [4].

An inventory of nodes plus a who-asked check is the right shape for handing out access. I do not read it as the wrong tool. I read it as a tool for a different quantity. Neither a time-bound lease nor a network edge is a property of a registered node. 

At the boundary, a research control plane shows what a per-action fix looks like when it is done well. It signs off on one exact action and hands out an allowance that can be spent exactly once. In its own test, 6,560 attempts to claim from 82 allowances produced exactly one win per allowance [3]. A 32-call race produced one committed effect. A retry after a lost reply sent nothing [3].

Then the paper states its own limit. A policy built too loose on purpose still let through an effect nobody wanted [3]. Distributed holds, crash recovery, and real-world targets stay untested. The allowance can be spent once, but whether it should have been spent on this path remains outside the check.

A third team names the class. In enterprise agent tests, checking the single action caught just 0.09 of the state-dependent violations [5]. Checking the full workflow state caught 0.96 [5].

A fourth team splits a pair the fabric tends to treat as one. The right to use a fact as proof is not the right to store it. A fact can be needed as evidence while its full meaning was never cleared to persist [6].

## By the numbers

- **13 — Stale steps under standing grants:** Three policies that keep a permanent grant all left 13 capability-steps in reach after their last justified use, across a 96-cell replay [1].
- **52.2% — Disclosure the topology added:** Across 485 multi-agent scenarios, protected facts reaching an agent the network graph added rose from 0% to 52.2% [2].
- **91.33 — Steps a full-access agent never needed:** Widening the same policies to full access added 91.33 capability-steps that no task in the replay needed [1].
- **0.09 vs 0.96 — What an action-level check sees:** A check on the single action caught 0.09 of state-dependent violations in enterprise agents, while a check on the workflow state caught 0.96 [5].

<!-- tactical-insight -->

## What I'd watch:

What I'm watching next is whether the lease and the recipient turn into named fields. Both papers park their leftover risk in the exact space a specific data field would fill.

- **A lease on the contract, not in the policy:** The step-lease control held zero leftover exposure by design, while the permanent grants shared the same 13 stale steps [1]. I'd want to know whether a grant's expiry becomes part of the tool contract rather than a line in a policy doc that drifts from the code.
- **Filters that read the recipient:** A filter that reads the receiver cut leftover leakage from 96.7% to 29.25%, and kept 94.1% of the messages that were allowed [2]. Those are the numbers to beat. The same paper is candid that 95.5% of what still leaked came from blind spots the detector never saw. 
- **One-shot allowances outside a lab:** One win per allowance across 6,560 racing claims is a real result, but it ran on fake identities and a mock target [3]. Production is where the untested list lives.
- **The counter that matters:** A registry counts registered parts [4]. The leak figure moved with the count of network hops [2]. Those two numbers can drift apart with nobody editing a single permission.

<!-- nuanced-takeaway -->

## The catch

My read: this pair of papers is a warning about the unit of a control, not proof that inventories are useless. Nobody has measured that a catalog of registered agents fails. The two papers simply measure what a per-call check cannot see.

The containment result is also narrower than it sounds. It tested one workflow, one small model, and 24 episodes [1]. The topology numbers span four models and two frameworks, but they come from a benchmark rather than a live corporate estate [2].

The fixes cost something the papers do not price. Step-scoped grants mean more grants, more issuing and more refusals. A filter that reads the recipient needs a detector, and its misses become the leftover risk [2].

I could be wrong, but I would treat two questions as ones a fabric review has to answer out loud: how long is this grant live, and who gets this next? The one I'm still curious about: does a lease slow a long workflow down in practice, or does it only move the queue?

<!-- tldr -->

## At a glance

- **The Big Shift:** Two measurements show that in multi-agent systems, exposure sits in how long authority stays usable and which agents the network handoffs add. It does not sit in whether a single call was allowed.
- **Why It Matters:** Enterprise fabrics rely on node inventories and per-request identity checks, which catch bad actors but miss lingering permissions or facts that travel one hop too far. Adding an agent adds both risks.
- **What I'd Watch:** Whether the lease and the recipient become named fields in the code, and whether the numbers hold outside a lab benchmark.
  - **Step lease:** A permission that ends when its workflow step ends, preventing authority from sitting unused in an agent's reach.
  - **Recipient-aware filter:** Rewriting a message based on who receives it and why, rather than how sensitive its static label says it is.
  - **One-shot allowance:** A signed permit for one exact action that an agent can claim once and never again.
- **The Catch:** The containment evidence relies on one workflow and one small model, while the network figures come from a benchmark. Both fixes add issuance and detection work, and their misses become the new leftover risk.

## Sources

[1] "CreepScope: Measuring Post-Use Authorization Exposure in Tool-Using Agents" (Yu, Liu, Zhang, Wang, Qian, Chen, Jiang), measured 2026-10-11 — https://arxiv.org/abs/2610.15988
[2] "When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems" (Ogundoyin, Ikram), measured 2026-10-12 — https://arxiv.org/abs/2610.16039
[3] "KedgeFlow: A Programmable Control Plane for Enterprise AI Agents" (He, Yu), measured 2026-10-10 — https://arxiv.org/abs/2610.14810
[4] Google Cloud, "Agent Registry overview", page footer dated 2026-10-08 — https://docs.cloud.google.com/agent-registry/overview
[5] "LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents" (Cong, He, Li, Wu, Shen, Peng, Li, Song), measured 2026-10-13 — https://arxiv.org/abs/2610.17685
[6] "Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State" (Chen, Zhao, Ma, Yao, Wei), measured 2026-10-12 — https://arxiv.org/abs/2610.16414

## Gate report

lead
PASS — Delivers the core takeaway immediately in the first sentence without throat-clearing, highlighting the blind spot in permissions and the network graph leaks.

tension
PASS — Structures the structural shift with clear, short paragraphs. First-person observer cues are present. Specialist terms like "standing grant" and "MCP" are translated or expanded. 

tactical-insight
PASS — Formatted as observations of what's next, not a playbook. Uses "What I'm watching next" and avoids imperative commands. Bullets are scannable and bolded.

nuanced-takeaway
PASS — Acknowledges the limits of the research clearly and succinctly. Contains the first-person cue ("My read:"). Paragraphs stay under the 3-sentence limit.

tldr
PASS — Follows the strict 4-part Smart Brevity schema. Clearly separated by its own H2 header. Sub-bullets properly define the terms to watch in plain English.
