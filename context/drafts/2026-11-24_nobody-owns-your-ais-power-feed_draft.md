---
title: Nobody Owns Your AI's Power Feed
vertical: nhil_infrastructure_ops
kind: news
persona: it_ops_leader
one_big_thing: "AI infrastructure is moving onto improvised local power while enterprises hand network management to agents. Your next edge site may run on a scavenged jet engine that a permit challenge can silence."
date: 2026-11-24
slug: nobody-owns-your-ais-power-feed
synthesis: true
sources:
  - https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide
  - https://www.prnewswire.com/news-releases/new-research-reveals-network-readiness-gap-in-enterprise-edge-ai-302944747.html
---

<!-- lead -->
Eight retired jet engines now power xAI's Mississippi data center, because the utility grid cannot deliver power to new sites fast enough [1]. Sixteen days later, a survey of 319 IT staff found that 72% of firms adapting their networks plan to hand control to agentic AI tools [2]. Those two facts are one story, and the seam between them is where the risk sits. The work and the control are moving onto local systems, and nobody owns the power feed underneath them.

<!-- tldr -->
## At a glance
AI compute is leaving the grid and the cloud, moving onto on-site generators and edge servers, while those same sites are being set up for agentic management. This piece is for IT operations leaders, and the finding is that the readiness gap is measurable and unowned.

<!-- tension -->
## Power and control leave together
The power side landed first. On 3 November, reporting showed xAI running eight turbine cores scavenged from old airliners at a Mississippi site [1]. Each repurposed engine produces up to 50 megawatts, roughly the load of 15,000 homes [1]. The state's permits allow a 25% higher limit on volatile organic compounds than normal [1].

The Southern Environmental Law Center has already challenged that approval. The group also alleges the projected emissions were undercounted, and formaldehyde sits among the chemicals in dispute [3]. My read of the sequence is plain. The grid cannot light up new AI sites fast enough, so the power gets makeshift from whatever burns.

The control side landed sixteen days after that. Enterprise Management Associates released the survey on 19 November. It covers 319 IT staff in edge inference strategy, paid for by Scale Computing [2]. Only 40% of the people polled are fully sure their networks can support their edge AI plans [2].

Some 64% of firms split their AI work between edge sites and the cloud [2]. Just 18% avoid that split by running everything where the data lives [2]. The same report shows 72% of those firms planning to adopt agentic tools [2]. The tools would steer networks the teams themselves do not fully trust.

One honest caveat belongs here: a vendor paid for the research and its fielding window is not disclosed. The release date is the date to use.

## By the numbers
- **8 converted jet engines:** the turbines now running as xAI's Mississippi power plant [1].
- **50 megawatts per engine:** what one repurposed jet turbine produces, about 15,000 homes of load [1].
- **64% hybrid placement:** enterprises splitting AI inference between edge sites and the cloud [2].

<!-- tactical-insight -->
## Where improvised supply meets delegated control
Put the two legs together and the seam shows. The edge sites now getting AI work are, on the survey's own numbers, sites whose networks only 40% of their teams fully trust [2]. The engines that could feed them face a live legal challenge [1]. What gives me pause is the layer in between. The power contract, the network setup and the agent policy live in three separate documents. Each has a different owner.

The people closest to the story are already circling that gap. Scale Computing's own pitch is to join compute, networking and security into one system [2]. Its research found the split-up management that gap creates. In telecom, Nokia announced an agentic platform with Nvidia [4]. It runs on the operator's own site, so its own data, models and policies stay inside their walls. That is still a launch announcement rather than a shipping product, but the demand it answers is real.

Researchers also released a closed-loop demo on 4 November [5]. LLM agents steer when base stations wake and sleep in it. That is the kind of control edge sites are being set up to hand over.

A Canonical outage on 11 November took launchpad and its software download services down for about seven hours [6]. Canonical blamed a fault in one of its own data centers, and people spent half a day fixing it. What I am watching next is whether any on-site engine contract now ships with an agent veto clause. Or the first report of an agent acting against a power cut becomes that clause.

<!-- nuanced-takeaway -->
## The catch
A vendor paid for this survey and has product to sell against the gap it finds. So the 72% figure deserves doubt, not dismissal [2]. The direction behind it is backed up by the separate scramble for power on the other leg [1]. And makeshift power is not automatically wrong.

A turbine running under a contested permit is still running, with humans watching. The other option is a site that never lights up at all. Where I have landed is that the risk is not the engine and not the agent. The risk is the unowned seam. Nobody has written the runbook that says which authority can cut which feed.

That is the same gap security teams already found in agent boundaries. There, [the kill switch misses half the agents in practice](/kill-switch-misses-half-your-agents/) [7]. The question I would put to any vendor selling both halves of this story, power and agents is simple. Who holds the physical veto, and does that answer survive contact with the power contract?



## Sources
- [1] Tom's Hardware, "Elon Musk's xAI installs eight converted jet engines to power Mississippi data center", 2026-11-03 — https://www.tomshardware.com/tech-industry/data-centers/elon-musks-xai-installs-eight-converted-jet-engines-to-power-mississippi-data-center-permits-allow-25-percent-higher-limit-for-pollutants-concerns-raised-over-carbon-monoxide
- [2] PR Newswire / Scale Computing, "New Research Reveals Network Readiness Gap in Enterprise Edge AI", 2026-11-19 — https://www.prnewswire.com/news-releases/new-research-reveals-network-readiness-gap-in-enterprise-edge-ai-302944747.html
- [3] The New York Times, "Old, Polluting Jet Engines Are Being Scavenged to Power Data Centers", 2026-11-03 — https://www.nytimes.com/2026/11/03/climate/jet-engines-ai-data-center-generators-boneyard.html
- [4] Nokia newsroom, "Nokia advances AI-RAN toward commercial deployment… sovereign agentic AI platform", 2026-10-21 — https://www.nokia.com/newsroom/nokia-advances-ai-ran-toward-commercial-deployment-and-physical-ai-launches-sovereign-agentic-ai-platform-for-telco-autonomy-with-nvidia
- [5] arXiv, "Agentic Wireless Optimization: Workflow Automation, Algorithm Design, and Multi-Timescale Network Operations", 2026-11-04 — https://arxiv.org/abs/2611.05887v1
- [6] Ubuntu Discourse, "Service interruption affecting Canonical websites", 2026-11-11 — https://discourse.ubuntu.com/t/service-interruption-affecting-canonical-websites/91653
- [7] giniloh.com / aichieve.net desk, "Kill Switch Misses Half Your Agents: 12 Vendors Agree" — https://aichieve.net/kill-switch-misses-half-your-agents/
