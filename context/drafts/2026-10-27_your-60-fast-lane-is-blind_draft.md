---
title: "Your 60% Fast Lane Is Blind"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "The pre-approved change band is the safety case, not the exemption from it: roughly 60 to 70% of changes already skip the change board, and once an agent drafts or runs them the only control that holds is a fixed policy at the execution boundary that holds back the unclear effects for a decision, because a request category is judged before the evidence that separates routine work from an attack exists."
date: 2026-10-27
slug: your-60-fast-lane-is-blind
synthesis: true
sources:
  - https://arxiv.org/abs/2610.18457
  - https://www.networkworld.com/article/4229048/orsted-builds-compliance-into-automation-speeds-firewall-changes.html
---

<!-- lead -->

Roughly 60 to 70 percent of Ørsted's firewall changes take a pre-approved fast lane that never reaches the change board. The company calls that a win, because a request goes live in about ten minutes instead of a few days [2]. A day later, a paper measured what that lane leaves blind. A monitor that can only allow or refuse an action must decide before the evidence arrives, its authors write. Real work and the first step of an attack look alike at the moment of the act [1]. Their design cut attack success on one test from 47.0 percent to 2.7 percent, and it did not do that by approving categories faster.

<!-- tension -->

## The big picture:

Ørsted did not build a shortcut around control. It built the lane on Nautobot, an open-source network automation platform, with custom checks on the data going in and a network split into zones that each carry their own security profile [2]. Requests still arrive through ServiceNow, peer review still runs on rules created by customers, and logs tie every firewall rule back to the request that made it and to the team behind it [2]. What changed is who decides. A security team looked at traffic flows in advance, marked some types as lower risk, and sent those to peer review instead of the change board.

What strikes me here is that the band is not an escape from control. It is the control. Six changes in ten are cleared by a judgement about a type, made in a workshop, before the change exists. João Soares, Ørsted's lead IT security consultant, is blunt that the rest is not negotiable: anything outside the pre-approved types goes to the change board, and "it cannot be optional" [2]. That is a stronger position than most shops hold, and most of the volume still rests on a type.

The paper argues about where that judgement sits, not whether to make one. A monitor that only allows or refuses must decide before the evidence builds up, because what separates routine work from a break-in lives later in the trace [1]. So the authors move the call to the effect that crosses the boundary: a tool call, a shell command and a script all cross as the same file and network actions [1]. A short policy listing which sources are trusted settles most of those effects on the spot, and the rest are held, not refused, while the agent keeps working. A person or a model with limited authority then releases or refuses each held effect, looking at the trace [1].

The timing matters because the change itself is being handed over. SolarWinds launched Avior on 14 October with "risk-tiered autonomy so that potentially dangerous actions always require explicit human approval" [3]. The tool runs actions through a fixed framework and repairs drift by restoring the last good settings [3]. That tier is judged before the action runs. It is the pre-approved band one layer down: a type, settled in advance, standing in for evidence that comes later.

## By the numbers

- **60 to 70% — Pre-approved share:** the part of Ørsted's firewall requests handled as lower-risk flows with peer review rather than change-board approval, per Soares [2].
- **47.0% to 2.7% — Attack success:** the undefended agent's rate on the AgentDojo test against the boundary monitor's, with normal usefulness held at the undefended level across three tests and three models [1].
- **10 minutes against a few days — Lane speed:** a pre-approved request can go live in about ten minutes, including the ask and a teammate's review, while one that needs the board waits days [2].
- **44 minutes — Site cut off:** how long one data centre provider's change to its denial-of-service protection kept that site offline, 21:05 to 21:49 on 9 October. Accounts with no tie to it were still hit through a shared pipeline [4].

<!-- tactical-insight -->

## What I'd watch:

The paper is a test result and Ørsted is one operator, so what I'm watching next is whether the gap between them closes.

- **Whether the error rate gets printed:** SolarWinds describes its tiers and its guardrails but gives no rate at which a dangerous action is called correctly [3]. That number is the whole case for tiering, and nobody has published it.
- **Whether the held effects get their own log:** holding an effect is what keeps speed while a call is pending, and it needs a place for effects to wait [1]. An operator who runs this inherits a new record to keep, not just a faster lane.
- **How the three logs join up:** Ørsted already ties a rule to its request and its requester [2]. The join missing from an agent-run pipeline is who caused the change when a model wrote the request, and that is what an auditor asks for first.
- **Whether the band widens as agent volume grows:** a pre-approved type pays off by covering volume cheaply, so the pressure runs one way. The paper's numbers suggest the band should narrow as the drafter gets better, not widen.

<!-- nuanced-takeaway -->

## The catch

Where I've landed is that the paper is evidence about a design, not about a network. Its 47.0 percent base is an undefended agent on a test, not a rate seen in anyone's data centre, and Ørsted's 60 to 70 percent is one firm's process as told to a reporter, with no method published [1][2]. A monitor at the boundary also costs real work: something has to hold an effect, something has to release it, and the policy that settles most effects needs an owner to keep it current.

There is a second limit that matters more to me. A trusted-source policy is still a list, and a list is still written by someone guessing what a type means. The gain over a change board is that the guess gets checked against the effect rather than the request, which is a real difference and not a small one. It is not a guarantee, and the board's refusal to be optional is what keeps the rest honest while the pipeline speeds up.

<!-- tldr -->

## At a glance

- **The Big Shift:** Ørsted pushes roughly 60 to 70 percent of its firewall changes through a pre-approved lane that skips the change board. In the same window a paper measured why a lane cleared by request type is the wrong place for the call: attack success only falls from 47.0 percent to 2.7 percent when the check sits at the effect crossing into production.
- **Why It Matters:** agents are being handed the change queue itself, with risk-tiered autonomy and repair jobs that restore settings on their own [3]. If the band is approved by type, the type becomes the thing an attacker aims at, and most of your change volume gets cleared before anyone sees the evidence.
- **What I'd Watch:** whether the vendors selling tiered autonomy publish an error rate, and whether operators who copy the paper's hold-and-decide pattern treat the waiting effects as a new record to keep.
  - **Holding an effect:** pausing one action while the agent keeps working, then releasing or refusing it on the trace, instead of blocking the action outright.
  - **Trusted-source policy:** a short list of which sources may cause which effects, settled at the boundary rather than left to a model's judgement.
  - **The join:** the link between a change, the request that allowed it and the person or model behind it, which is what an auditor asks for first.
- **The Catch:** the 47.0 to 2.7 percent result comes from a test on three agent models, not a live network, and Ørsted's band is one operator's own numbers. Checking at the boundary also needs a place to hold effects and someone to keep the policy current, which is work a change board never had to fund.

## Sources

[1] *Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents*, arXiv:2610.18457v1, submitted 2026-10-13 — https://arxiv.org/abs/2610.18457
[2] Denise Dubie, "Ørsted builds compliance into automation, speeds firewall changes", Network World, 2026-10-12 — https://www.networkworld.com/article/4229048/orsted-builds-compliance-into-automation-speeds-firewall-changes.html
[3] "SolarWinds Unveils Avior, Bringing Deterministic, Agentic AI to Enterprise IT", SolarWinds press release, 2026-10-14 — https://www.solarwinds.com/company/newsroom/press-releases/solarwinds-unveils-avior-bringing-deterministic-agentic-ai-to-enterprise-it
[4] "Incident report for October 9 and 10, 2026", Inngest, 2026-10-15 — https://www.inngest.com/blog/2026-10-15-incident-report-for-october-9-and-10-2026
