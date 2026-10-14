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
---

<!-- lead -->

Two measurements landed a day apart, and both point at one blind spot in the fabric's per-call check. It sees the call. The lease and the edge go unmeasured — a replay left 13 capability-steps in reach after their last justified use, and a change to the shape of the agent graph alone lifted disclosure to an agent the topology added from 0% to 52.2% [1][2].

Neither result involves a bad actor. Both describe reach that outlives the reason it was granted.

<!-- tension -->

## The big picture:

The part I keep circling: permission and exposure are two different quantities. Only one of them is on the architecture diagram.

The first paper replays 96 cells of agent work. The cells cover 12 tasks in storage, messaging and cloud operations. Three of its policies keep a standing grant, and all three leave the same 13 capability-steps in reach after their last justified step. So the gap between them comes from scope and timing, not from how long a grant lingers after use. A fourth policy holds zero by design. It leases authority to the step and lets it die there [1].

Then the team ran the case, not the table. Twenty-four episodes of a fake mail workflow, with a small open model picking the tools. The planted stale send fired in all nine standing-grant episodes. It fired in none of the three lease episodes. All 24 required action runs still finished [1].

Widening the grant made it worse in a way no per-call audit would show. Full access added 91.33 capability-steps that no task in the replay needed [1].

The second paper takes the other axis. Nothing has to go wrong for a leak to happen. A fact handed to one allowed agent travels on through normal handoffs. Across 485 scenarios, three topologies and seven channels, disclosure to a recipient the topology added went from 0% to 52.2%. Surface leakage stayed flat at 60.6% to 62.8% [2].

That flatness is the bit I keep coming back to. The labels a filter reads did not move. Only the graph moved. The choice of framework on its own drove a 150-fold spread in leakage [2]. The wiring carries the secret, not the wording on it.

The answer enterprises are being sold this month aims somewhere else. A hyperscaler's agent registry page, stamped 2026-10-08 by its own footer, three days before that first measurement, describes a catalog that "maintains the authoritative inventory of agents, MCP (Model Context Protocol) servers, tools, skills, and external endpoints, and generates the identifiers and resource names referenced by discovery clients and security policies" [4]. The request itself goes to a companion identity service that works out who is making the call [4].

An inventory of nodes plus a who-asked check is the right shape for provisioning. I do not read it as the wrong tool. I read it as a tool for a different quantity. Neither a lease nor an edge is a property of a registered node. Neither one is a row in that catalog.

At the boundary, a research control plane shows what a per-action fix looks like when it is done well. It signs off on one exact action, and hands out an allowance that can be spent once. In its own test, 6,560 attempts to claim from 82 allowances produced exactly one win per allowance. A 32-call race produced one committed effect. A retry after a lost reply sent nothing [3].

Then the paper states its own limit. A policy that was too loose on purpose still let through an effect nobody wanted. Distributed holds, crash recovery, exactly-once effects at real targets and links between rival builds all stay untested [3]. That is the shape of the problem. The allowance can be spent once. Whether it should have been spent, on this path, for this recipient, is still outside the check.

A third team names the class. In enterprise agent tests, a check on the single action caught 0.09 of the state-dependent violations. A check on the workflow state caught 0.96 [5].

A fourth splits a pair the fabric tends to treat as one. The right to use a fact as proof is not the right to let it stay. A fact can be needed as evidence while its full meaning was never cleared to persist [6].

## By the numbers

- **13 — Stale steps under standing grants:** Three standing-grant policies in a 96-cell replay all left 13 capability-steps in reach after their last justified use; the step-lease control left zero by design [1].
- **52.2% — Disclosure the topology added:** Across 485 multi-agent scenarios, protected facts reaching an agent the topology added rose from 0% to 52.2%, while surface leakage stayed flat at 60.6% to 62.8% [2].
- **91.33 — Steps a full-access agent never needed:** Widening the same policies to full access added 91.33 capability-steps that no task in the replay needed [1].
- **0.09 vs 0.96 — What an action-level check sees:** A check on the single action caught 0.09 of state-dependent violations in enterprise agents; a check on the workflow state caught 0.96 [5].

<!-- tactical-insight -->

## What I'd watch:

What I'm watching next is whether the lease and the recipient turn into named fields, because both papers park their leftover risk in the space a field would fill.

- **A lease on the contract, not in the policy:** The step-lease control held zero leftover exposure by design, while the standing grants shared the same 13 stale steps [1]. I'd want to know whether a grant's expiry becomes part of the tool contract, the way an idempotency key did, rather than a line in a policy doc that drifts from the code.
- **Filters that read the recipient:** A recipient-aware filter cut leftover disclosure from 96.7% to 29.25% and kept 94.1% of the disclosures that were allowed, against 20.5% for blanket redaction [2]. Those are the numbers to beat. The same paper is candid that 95.5% of what it still leaked came from what its detector never saw. The detector, not the policy, is the bottleneck.
- **One-shot allowances outside a lab:** One win per allowance across 6,560 racing claims is a real result — on three etcd members on one host, with fake identities and a mock target [3]. Production is where the untested list lives.
- **The counter that matters:** The registry counts registered parts [4]. The leak figure moved with the count of hops [2]. Those two numbers can drift apart with nobody editing a single permission.

<!-- nuanced-takeaway -->

## The catch

My read: this pair is a warning about the unit of a control, not proof that inventories are useless. Nobody has measured that a catalog of registered agents fails. The two papers measure what a per-call check cannot see.

The containment result is also narrower than it sounds. One workflow, one small model, 24 episodes. The authors call it "a reproducible containment case, not cross-workflow or cross-model effectiveness" [1]. The topology numbers span four models and two frameworks, but they come from a benchmark, not from a live estate [2].

The fixes cost something the papers do not price. Step-scoped grants mean more grants, more issuance and more refusals. A filter that reads the recipient needs a detector, and its misses become the leftover risk [2].

I could be wrong, but I would treat two questions as ones a fabric review has to answer out loud: how long is this grant live, and who gets this next? The one I'm still curious about: does a lease slow a long workflow down in practice, or does it only move the queue?

<!-- tldr -->

## At a glance

- **The Big Shift:** Two measurements days apart show that in multi-agent systems the exposure sits in how long authority stays usable and which agents the handoffs add — not in whether a single call was allowed. A workflow replay found all three standing-grant policies holding the same 13 stale capability-steps. A change of topology lifted leakage to added recipients from 0% to 52.2%.
- **Why It Matters:** Enterprise fabrics are governed by node inventories and per-request identity. Those catch a bad actor asking for a resource. They do not bound a grant that outlives its task, or a fact that travels one hop too far. Adding an agent adds both.
- **What I'd Watch:** Whether the lease and the recipient become named fields, and whether the numbers hold outside a benchmark.
  - **Step lease:** A grant that ends when its workflow step ends, so authority cannot sit unused in an agent's reach after the task is done.
  - **Recipient-aware filter:** Rewriting a message based on who receives it and why, not on how sensitive its label says it is.
  - **One-shot allowance:** A signed permit for one exact action that can be claimed once and never again, so a retry cannot spend it twice.
- **The Catch:** The containment evidence is one workflow and one small model. The topology figures come from a benchmark. Both fixes add issuance and detection work, and their misses become the new leftover risk. An inventory of nodes is still the right tool for provisioning — it is just not a measure of exposure.

## Sources

[1] "CreepScope: Measuring Post-Use Authorization Exposure in Tool-Using Agents" (Yu, Liu, Zhang, Wang, Qian, Chen, Jiang), measured 2026-10-11 — https://arxiv.org/abs/2610.15988
[2] "When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems" (Ogundoyin, Ikram), measured 2026-10-12 — https://arxiv.org/abs/2610.16039
[3] "KedgeFlow: A Programmable Control Plane for Enterprise AI Agents" (He, Yu), measured 2026-10-10 — https://arxiv.org/abs/2610.14810
[4] Google Cloud, "Agent Registry overview", page footer dated 2026-10-08 — https://docs.cloud.google.com/agent-registry/overview
[5] "LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents" (Cong, He, Li, Wu, Shen, Peng, Li, Song), measured 2026-10-13 — https://arxiv.org/abs/2610.17685
[6] "Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State" (Chen, Zhao, Ma, Yao, Wei), measured 2026-10-12 — https://arxiv.org/abs/2610.16414
