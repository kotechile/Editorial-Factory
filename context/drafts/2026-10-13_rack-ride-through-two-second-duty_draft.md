---
title: "Right Locally, Wrong by 3.8 GW"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "A data center's own relay and protection settings now decide grid reliability, because the regulator declined the right to switch large loads off and the industry answered by standardizing how long a site must hold on when the grid moves — and the same locally-right, globally-wrong pattern is now measured in autonomous software repair."
date: 2026-10-13
slug: rack-ride-through-two-second-duty
synthesis: true
sources:
  - https://www.opencompute.org/documents/ocp-base-spec-interface-specification-between-hyperscalers-and-utility-grid-for-disturbance-performance-pdf
  - https://arxiv.org/abs/2609.24130
---

<!-- lead -->

On July 22, a power line in northern Virginia failed, and its fault cleared the way it should. Then about 2,970 megawatts (MW) of data center load left the grid anyway. Another 1,099 MW followed as the voltage rose.

That is roughly 3.8 gigawatts (GW) gone in two waves, more than twice the size of the same event in July 2024 and February 2025 [3]. Every one of those transfers was a safety move that worked as designed. On September 17, the four biggest buyers of that power set a number for how long a site must hold on before it may let go: 2 seconds, at a shallow dip [1].

<!-- tension -->

## The big picture:

The standard is a duty the buyers wrote for themselves, not a rule handed to them. That is the part I keep coming back to.

The document is an Open Compute Project (OCP) base standard, version 1.0.0, effective September 17, 2026. Engineers from Google, Microsoft, Meta and Nvidia wrote it [1]. It binds a site to ride out a voltage dip, then recover.

Between 80% and 90% of normal voltage, the computing load must hold for 2 seconds. Between 50% and 80%, it holds for half a second. Between 35% and 50%, a quarter second [1]. Below 35%, it holds for 0.15 seconds. Once the voltage is back in its normal band, the load must return to 90% of its pre-fault level within 2 seconds [1].

The scope is where it gets odd. The promise covers only the computing load, which the authors put at 70% to 90% of a site's total draw [1]. Cooling is left out. The authors say the chillers run through variable frequency drives, whose behaviour in a dip differs from the computing load's, and whose restore times run longer [1].

Frequency ride-through, rate of change of frequency, phase jump and ramp rate sit on a future-work list, with no numbers in version 1.0.0 [1]. Auxiliary load is under 1% and gets no promise at all [1].

So the trade wrote itself a 2-second duty for the gear it buys by the pallet, and left a blank where the gear that carries the heat away goes.

Now the other half, and this is the part that changed how I read our own change process. A team measured the same shape in software. They built an outside gate that decides which of an agent's own changes may persist, then ran it over 16 matched pairs of tests [4].

The gate rejected 383 changes that looked good on replay. Of those, 211 — 55% — fixed the failure that triggered them while breaking a case that had worked before [4]. Their finding is narrow: a change that is right for the thing that broke can be wrong for the system around it, often enough to change the call.

The rest of that work says the same thing from the other side. One framework reports a 98.1% cut in mean time to repair, from 170 minutes a patch to 3.2 minutes, at a 92% success rate [5]. Its worst case, 85%, is the one where the fault hides in a nested structure the repair agent cannot see [5]. A third runs repair as an outside control plane, so the logic never touches the app, and still recovers only 10% to 47% of the time it fires [6].

Put the two halves together and it is one problem. A site that switches to its own generators during a disturbance is right for its own racks. Three dozen sites doing that at once is a 3.8 GW hole in the grid. An agent that patches its own failure is right for its own workflow. Two hundred and eleven of them doing that is a pile of regressions nobody ordered. Each fix is local, and each one is rational. Each one needs a gate that knows the blast radius.

That gate is now the operator's problem, because the regulator handed the choice back. On October 9, the Federal Energy Regulatory Commission (FERC) approved the large-load registry that PJM (the grid operator for 13 states and Washington, D.C.) had proposed. It lists location, ramp schedule, capacity supply, backup generation and fuel sources [7][8].

FERC rejected the operator's plan to cut power to those loads first. The grounds were state authority over retail rates and likely unfair treatment of one class of customer [7]. FERC's own words: states "have a crucial role to play in this challenge by designating which retail customers must be curtailed when the system is stressed" [7]. The grid got the data and not the switch. What is left as a lever on 3.8 GW of behaviour is the setting inside the fence.

## By the numbers

- **3.8 GW — The load that left:** 2,970 MW moved to onsite generation in the first wave on July 22, then another 1,099 MW as voltage rose, more than twice the roughly 1,500 MW events of July 2024 and February 2025 [3].
- **2 seconds — The ride-through floor:** the least time the computing load stays on at 80% to 90% of normal voltage, falling to 0.15 seconds below 35% [1].
- **90% in 2 seconds — Post-fault recovery:** once voltage is back in its normal band, the computing load must return to 90% of its pre-fault level within 2 seconds [1].
- **211 of 383 — Right locally, wrong globally:** changes an outside runtime gate turned down, of which 55% fixed their own failure while degrading a case that had worked [4].

<!-- tactical-insight -->

## What I'd watch:

- **Whether the relay setting has an owner.** The duty in the OCP standard lives in relay and protection settings, which are configuration, not procurement. The team that signs off a firmware push may now carry a grid duty in a config file [1].
- **The cooling blank.** The standard exempts the chillers. In the same fortnight, a maker showed a chiller running straight off an 800 VDC feed at more than 1,000 tons, or 3.5 MW, of cooling [1][2]. The load with no ride-through duty is the load going onto the same DC bus.
- **The frequency hole.** Voltage dips are pinned down. Frequency ride-through, rate of change of frequency and phase jumps are not [1]. A site can meet version 1.0.0 in full and still have no rule for the mode that follows a big loss of generation.
- **The grandfathered fleet.** The rollout plan exempts sites already running, or holding a signed grid-connection deal, for the life of the site, and applies the duty only to growth [1]. The risk does not retire with the exemption.
- **Which gate has the authority.** The software leg points at an outside gate with an explicit yes-or-no call [4]. I would want to know whether the power side has one, or whether the relay scheme is the last part of the stack that still approves itself.

<!-- nuanced-takeaway -->

## The catch

The big number here is from July, and I would date it every time it is quoted. The July 22 event sits outside this month's window; the in-window news is the standard that answers it.

Another outlet put the same event at 3.9 GW, which is the same reading rounded differently, so I have used one figure and one source rather than stacking them [3].

The standard is also weaker than a rule. It grandfathers the sites already built, treats compliance there as best-effort and optional, and pushes the biggest engineering questions to a later version [1]. Nothing in it shows a hyperscaler running to these numbers yet.

The software leg carries its own limits. It comes from single teams on small sets: 16 matched runs over three test suites, not a live fleet [4][5][6]. The three frameworks also disagree about how often repair works at all: 92% success in one, 10% to 47% recovery in another [5][6]. I could be wrong, but the 55% figure describes a gate turning down proposals, which is not the same as counting how often a shipped agent breaks something quietly.

FERC's ruling is narrower than it reads too. The agency turned down one design for cutting power, and said the operator may refile if it explains why data centers would be shed before other large users [8]. It did not rule that large loads can never be cut. It said the states get to pick who goes first [7]. PJM's last auction cleared with a shortfall of 6,831 MW, so the pressure behind the plan has not gone anywhere [9].

What I take from it is smaller than "the grid is failing" and bigger than a compliance note. The behaviour that holds a grid together is more and more a setting inside the buildings it feeds, and the people who own those buildings never asked for that job.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A routine power-line fault in northern Virginia on July 22 cleared normally, and roughly 3.8 GW of data center load transferred to onsite generation anyway — the largest such transfer that grid operator has seen, and more than double the same event in 2024 and 2025. On September 17, the data center trade answered with a standard that sets how long a site must hold on through a voltage dip: 2 seconds at a shallow sag, 0.15 seconds in a deep one.
- **Why It Matters:** The duty to keep the grid steady has moved from the power contract into the relay and protection settings inside the fence. FERC approved the grid operator's registry of large loads on October 9 but turned down its plan to cut their power first, so the data is available and the switch is not. What keeps a site from dropping a gigawatt is now configuration the operator owns.
- **What I'd Watch:** whether the power side gets the outside gate the software side is being handed, and what the exempt load does.
  - **Ride-through window:** the least time a computing load must stay on at a given voltage, which turns a safety switch-off into a timed call.
  - **Post-fault recovery:** the duty to return to 90% of pre-fault load within 2 seconds once voltage is normal, which caps how far a site can lean on its own generators.
  - **Admission gate:** an outside check on which self-made fixes may persist, because a change that repairs one failure can degrade another case.
- **The Catch:** The standard is optional, grandfathers the sites already built, and leaves frequency ride-through, phase jumps and cooling out of version 1.0.0. The 3.8 GW event is dated July 22 and sits outside this month's window. The software proof is single-team preprint work, and FERC's ruling blocks one way of cutting power, not the idea.

## Sources

[1] Open Compute Project, "Data Center Facility Project: Interface Specification Between Hyperscalers and Utility Grid for Disturbance Performance, Version 1.0.0" (OCP Base Specification, effective 17 September 2026) — https://www.opencompute.org/documents/ocp-base-spec-interface-specification-between-hyperscalers-and-utility-grid-for-disturbance-performance-pdf
[2] Trane Technologies, "Trane Technologies Demonstrates Industry-First 800-Volt Direct Current Chiller for Next-Generation AI Data Centers" (30 September 2026) — https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2026/Trane-Technologies-Demonstrates-Industry-First-800-Volt-Direct-Current-Chiller-for-Next-Generation-AI-Data-Centers/default.aspx
[3] Data Center Knowledge, "3.8 GW Load Drop Prompts Potential PJM Data Center Rules" (6 October 2026) — https://www.datacenterknowledge.com/regulations/3-8-gw-load-drop-prompts-potential-pjm-rules
[4] arXiv:2609.24130, "Self-Healing Harness for Runtime Oversight of Agent Self-Modification" (21 September 2026) — https://arxiv.org/abs/2609.24130
[5] arXiv:2610.06971, "AegisFlow: A Multi-Agent Agentic AI Framework for Autonomous Remediation and Self-Healing in Fragile Data Ecosystems" (3 October 2026) — https://arxiv.org/abs/2610.06971
[6] arXiv:2609.34701, "ResonAct: Streaming Metrics for Runtime Diagnosis and Self-Healing in Multi-Agent Systems" (28 September 2026) — https://arxiv.org/abs/2609.34701
[7] Utility Dive, "FERC rejects most of PJM's large load interconnection plan" (12 October 2026) — https://www.utilitydive.com/news/ferc-pjm-large-load-interconnection-iras-byonc/832716
[8] Reuters, "US panel approves PJM's registry of data centers, rejects plan to curtail power to them" (12 October 2026) — https://www.reuters.com/business/energy/us-panel-approves-pjms-registry-data-centers-rejects-plan-curtail-power-them-2026-10-12
[9] mgrid.org, "FERC Rejects PJM's Curtail-First Plan for New Large Loads, and Keeps Only the 50 MW Definition and a Registry" (10 October 2026) — https://mgrid.org/2026/10/10/ferc-rejects-pjms-curtail-first-plan-for-new-large-loads-and-keeps-only-the-50-mw-definition-and-a-registry
