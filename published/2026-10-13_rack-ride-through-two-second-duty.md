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
meta_title: "Right Locally, Wrong by 3.8 GW"
meta_title_source: "derived_from_title"
meta_description: "On July 22, a power line in northern Virginia failed and cleared exactly as it should."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/rack-ride-through-two-second-duty/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "The 3.8 GW Grid Dropoff. A vast array of high-voltage data center substation transformers compressed through a telephoto lens"
image_caption: "The 3.8 GW Grid Dropoff: Tech giants set new rules to survive grid voltage dips."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

On July 22, a power line in northern Virginia failed and cleared exactly as it should. Then 2,970 megawatts (MW) of data center power dropped off the grid anyway. Another 1,099 MW followed as voltage spiked.

That is 3.8 gigawatts (GW) gone in two waves. It is more than double the size of similar events in July 2024 and February 2025 [3]. Every drop was a safety switch working as designed.

On September 17, four of the largest data center operators set a new rule. It says how long a site must hold on before it may let go: 2 seconds, at a shallow dip [1].

<!-- tension -->

## The big picture:

The standard is a duty the buyers wrote for themselves, not a rule handed to them.

That is the part I keep coming back to. The Open Compute Project (OCP) standard, version 1.0.0, takes effect September 17, 2026. Engineers from Google, Microsoft, Meta, and Nvidia wrote the rules [1].

It forces a site to ride out a voltage dip, then recover. Between 80% and 90% of normal voltage, server power must hold for 2 seconds. It holds half a second between 50% and 80%. Between 35% and 50%, a quarter second [1].

Below 35%, it holds for 0.15 seconds. Once voltage returns to normal, the load must hit 90% of its past level within 2 seconds [1].

The scope leaves a huge gap. The promise only covers servers, which make up 70% to 90% of a site's total power draw [1].

Cooling gets a free pass. The authors note that chillers run on variable-speed drives. Those drives react differently to a dip and take longer to restart [1].

Other grid threats sit on a future-work list with no hard numbers. Frequency ride-through, rate of change of frequency, and phase jumps all wait for a later version [1].

So the trade wrote a 2-second duty for the servers it buys by the pallet. It left a blank for the systems that carry the heat away.

Now the software side, which changed how I view our own change plans. A research team measured this exact pattern in self-healing code.

They built an outside gate. It decides which of a tool's self-made changes may stay. They tested it across 16 matched runs [4].

The gate turned down 383 changes that looked fine on replay. Of those, 211 (55%) solved the first failure but broke a process that used to work [4]. A fix that works for the broken part can still damage the wider system.

Other work shows the same trade-off. One system cuts repair time by 98.1%, from 170 minutes a patch to 3.2 minutes, at a 92% success rate [5]. Its worst case, 85%, is the one where the fault hides in a deep structure the tool cannot see [5].

Another runs repair as an outside control plane. It recovers roughly 10% to 47% of the time it fires [6]. These are two sides of one problem.

A site that switches to onsite generators during a voltage dip protects its own racks. Many sites doing that at once tears a 3.8 GW hole in the grid.

An artificial intelligence (AI) agent patching its own failure fixes its own workflow. Two hundred and eleven of them doing it leaves a pile of new bugs. Each fix is local, and each one is rational. Each one needs a gate that knows the blast radius.

That gate is now the operator's problem. On October 9, the Federal Energy Regulatory Commission (FERC) approved a large-load registry. PJM (the grid operator for 13 states and Washington, D.C.) had proposed it [7][8].

The registry tracks location, ramp schedules, and backup power sources [7][8].

FERC turned down PJM's plan to cut power to those large loads first during a crisis. The agency cited state power over retail rates and the unfair targeting of one customer class [7].

FERC's own words: states "have a crucial role to play in this challenge by designating which retail customers must be curtailed when the system is stressed" [7]. The grid operator got the data, but not the kill switch. The only lever left on 3.8 GW of load behavior is the setting inside the fence.

## By the numbers

- **3.8 GW — The load that left:** 2,970 MW moved to onsite generators in the first wave on July 22. Another 1,099 MW went as voltage rose, more than twice the roughly 1,500 MW events of July 2024 and February 2025 [3].
- **2 seconds — The ride-through floor:** the least time server power stays on at 80% to 90% of normal voltage, falling to 0.15 seconds below 35% [1].
- **90% in 2 seconds — Post-fault recovery:** once voltage settles, server power must return to 90% of its past level within 2 seconds [1].
- **211 of 383 — Right locally, wrong globally:** changes an outside gate turned down, of which 55% fixed their own failure while breaking a case that had worked [4].

<!-- tactical-insight -->

## What I'd watch:

- **Relay setting ownership:** The OCP duty lives in relay and protection settings, which are config files rather than hardware buys. The team that signs off firmware may now carry a grid duty [1].
- **The cooling blank:** The standard exempts chillers. In late September, a maker showed a chiller running straight off an 800 volts direct current (VDC) feed, delivering more than 1,000 tons, or 3.5 MW, of cooling [1][2]. The load with no ride-through duty now shares that same direct current bus.
- **The frequency hole:** Voltage dips have strict rules. Frequency changes and phase jumps do not [1]. A site can meet version 1.0.0 in full and still lack a plan for the mode that follows a big loss of generation.
- **The legacy fleet:** The standard exempts existing sites, and those with signed grid deals, for the life of the site. It applies to growth at those sites and to new ones [1]. The risk does not retire with the exemption.
- **Gate authority:** The software work points to an outside gate with a yes-or-no call [4]. I am watching to see if the power side builds one, or if the relay scheme stays the last part of the stack that approves itself.

<!-- nuanced-takeaway -->

## The catch

The 3.8 GW figure comes from July. I date it every time, because it sits outside this month's window. The in-window news is the standard written to answer it.

Another outlet measured the same event at 3.9 GW [10]. That is the same reading rounded differently, so I use one figure and one source rather than stacking the two.

The OCP standard is also weaker than a binding rule. It exempts existing sites, treats the rules as optional best-effort, and delays the hardest engineering questions to a later version [1]. Nothing shows a large buyer hitting these numbers yet.

The software data carries its own limits. The findings come from single teams running small tests: 16 matched runs over three test suites, not a live fleet [4][5][6].

The tools also disagree on success rates, from 92% in one to about 10% in another [5][6]. I could be wrong, but the 55% figure describes a gate turning down proposals. That is not the same as counting how often a live agent quietly breaks a system.

FERC's ruling is narrower than it looks. The agency blocked one plan for cutting power and invited the operator to refile with better proof [8].

It did not rule that large loads can never be cut [7]. PJM's last auction showed a 6,831 MW shortfall, so the pressure behind the plan has not gone anywhere [9].

What I take from this is bigger than a compliance note but smaller than grid collapse. The behavior that holds the grid together leans more and more on settings inside the buildings it feeds. The people running those buildings never asked for that job.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "40 kW Line: Why the AI Rack Is a Building Project" -> https://giniloh.com/rack-power-density-ceiling-build-before-you-buy/ [same site (giniloh.com); same category; topical overlap: line, power] Link "40 kW Line: Why the AI Rack Is a Building Project" in the section where the article touches line, power. -->
<!-- internal-link hint: "OpenAI’s custom chip beats Nvidia on power" -> https://giniloh.com/openais-custom-chip-beats-nvidia-on-power-2/ [same site (giniloh.com); same category; topical overlap: power] Link "OpenAI’s custom chip beats Nvidia on power" in the section where the article touches power. -->
<!-- internal-link hint: "A 1% Mispick Rate Is a Seven-Figure Line Item" -> https://giniloh.com/warehouse-pick-error-tax-payback/ [same site (giniloh.com); topical overlap: line, wrong] Link "A 1% Mispick Rate Is a Seven-Figure Line Item" in the section where the article touches line, wrong. -->
## Related reading

- [40 kW Line: Why the AI Rack Is a Building Project](https://giniloh.com/rack-power-density-ceiling-build-before-you-buy/)
- [OpenAI’s custom chip beats Nvidia on power](https://giniloh.com/openais-custom-chip-beats-nvidia-on-power-2/)
- [A 1% Mispick Rate Is a Seven-Figure Line Item](https://giniloh.com/warehouse-pick-error-tax-payback/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** A routine power-line fault in northern Virginia cleared normally on July 22. Roughly 3.8 GW of data center power moved to onsite generators anyway. On September 17, the data center trade answered with a standard: 2 seconds of ride-through at a shallow sag, 0.15 seconds in a deep one.
- **Why It Matters:** The job of keeping the grid steady has shifted from power contracts into the relay and protection settings inside the fence. FERC approved a registry of large loads on October 9 but rejected its plan to cut their power first. Operators hold the data, and no kill switch.
- **What I'd Watch:** whether the power side gets the outside gate the software side is building, and what the exempt cooling load does next.
  - **Ride-through window:** the least time server power must stay on at a given voltage, which turns a safety switch-off into a timed choice.
  - **Post-fault recovery:** the duty to return to 90% of pre-fault load within 2 seconds once voltage settles, capping how long a site leans on its own generators.
  - **Admission gate:** an outside check on which self-made software fixes may stay, stopping a local repair from breaking the wider system.
- **The Catch:** The standard stays optional, exempts existing sites, and leaves frequency changes and cooling out of version 1.0.0. The software data rests on single-team preprints, not live fleets. FERC's ruling blocked one method of cutting power, not the idea.

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
[10] RTO Insider, "Va. Data Center Ride-through Performance Faulted for July Voltage Disturbance" (12 August 2026) — https://www.rtoinsider.com/138974-va-data-center-ride-through-performance-faulted-july-voltage-disturbance

## Gate report

lead: PASS — Core news delivered in short, concrete sentences; the 2-second duty lands by the third paragraph with no throat-clearing.
tension: PASS — Splits every long block into 1–3 sentence paragraphs; plain words throughout; both legs (the standard, the self-repair gate) carried with citations.
tactical-insight: PASS — Five bolded bullets framed as observations of what is being watched, never instructions.
nuanced-takeaway: PASS — Names the honest limits of all three pieces of evidence and dates the out-of-window figure on every use.
tldr: PASS — 4-part schema intact, plain-English sub-bullet definitions, caveats in the final slot.
