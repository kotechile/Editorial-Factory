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
meta_title: "Your 60% Fast Lane Is Blind"
meta_title_source: "derived_from_title"
meta_description: "Roughly 60 to 70 percent of Ørsted's firewall changes take a pre-approved fast lane that never reaches the change board."
meta_description_source: "derived_from_lead"
---

<!-- lead -->

Roughly 60 to 70 percent of Ørsted's firewall changes take a pre-approved fast lane that never reaches the change board. The energy firm calls that a win, because a request goes live in about ten minutes instead of a few days [2]. A day later, a paper measured what this lane leaves blind. A system that only allows or stops an action must decide before the facts arrive, its authors write. Real work and the first step of an attack look the same at the moment of the request [1]. Checking the effects instead cut attack success from 47.0 percent to 2.7 percent, and not by clearing types faster [1].

<!-- tension -->

## The big picture:

Ørsted did not build a shortcut around control. It built the lane on Nautobot, an open-source network tool, with custom checks on new data. The network splits into zones, and each zone carries its own safety profile [2]. Requests still arrive through ServiceNow, and peer review still runs on rules made by users. Logs tie every rule back to the request that made it [2].

What changed is who decides. A security team looked at traffic flows, marked some types as lower risk, and sent those to peer review instead of the board.

What strikes me here is that the fast lane is the control itself. Six changes in ten clear on a judgment about their type, made long before the change exists. João Soares, Ørsted's lead IT security consultant, is blunt that the rest is not a choice. Anything outside the cleared types goes to the change board, and "it cannot be optional" [2]. That is a stronger stance than most shops take, even though most volume rests on a type check.

The authors argue about where that choice belongs, not whether to make it. A monitor that only allows or stops work must decide early. The details that separate routine tasks from a break-in show up later in the trace [1]. So they move the choice to the effect that crosses the system line. A tool call, a shell command and a script all land as the same file and network actions [1].

A short policy listing trusted sources settles most of those effects at once, and the rest are held, not refused, while the agent keeps working. A person or a model with limited say then releases or drops each held effect, reading the trace first [1].

The timing matters because the change is changing hands. SolarWinds launched Avior on 14 October with "risk-tiered autonomy so that potentially dangerous actions always require explicit human approval" [3]. The tool also repairs drift by restoring the last good settings. That tier is judged before the action ever runs. It is the cleared band moved one layer down, where a type stands in for evidence that only arrives later.

## By the numbers

- **60 to 70% — Pre-approved share:** the part of Ørsted's firewall requests handled as lower-risk flows with peer review rather than change-board approval, per Soares [2].
- **47.0% to 2.7% — Attack success:** the undefended agent's rate on the AgentDojo test against the boundary monitor's, with usefulness held steady across three tests and three models [1].
- **10 minutes against a few days — Lane speed:** a pre-approved request can go live in about ten minutes, including the ask and a teammate's review. One that needs the board waits days [2].
- **44 minutes — Site cut off:** how long one data centre provider's change to its attack-filter settings cut that site off from the rest of the network, 21:05 to 21:49 on 9 October. Accounts with no tie to it were still hit through a shared pipeline [4].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your 60% Fast Lane Is Blind</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Pre-approved share</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="210" height="18" rx="4" fill="#818cf8"/>
  <text x="460" y="84" fill="#f1f5f9" font-size="13" font-weight="600">70%</text>
  <text x="514" y="84" fill="#64748b" font-size="11">([2])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Attack success</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="141" height="18" rx="4" fill="#38bdf8"/>
  <text x="391" y="132" fill="#f1f5f9" font-size="13" font-weight="600">47%</text>
  <text x="445" y="132" fill="#64748b" font-size="11">([1])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

The paper is a test result and Ørsted is just one operator, so what I am watching next is whether the gap between their setups closes.

- **Whether the error rate gets printed:** SolarWinds describes its tiers and guardrails but gives no rate at which a dangerous action is called correctly [3]. That number is the whole case for tiering, and nobody has published it.
- **Whether the held effects get their own log:** pausing an effect is what keeps speed while a call is pending. It needs a place for those effects to wait [1]. An operator running this takes on a new record to keep. That is the same shift this desk traced in [the safety gate that moved to verified state](/agent-safety-gate-moves-to-verified-state/).
- **How the three logs join up:** Ørsted already ties a rule to its request and its requester [2]. The missing link in an automated pipeline is who caused the change when a model wrote the request. That is what an auditor asks for first.
- **Whether the band widens as agent volume grows:** a cleared type pays off by handling volume cheaply, so the pressure runs one way. The paper's numbers suggest the band should narrow as the drafting tool gets better, not widen.

<!-- nuanced-takeaway -->

## The catch

Where I've landed is that the paper offers facts about a design, not a live network. Its 47.0 percent base is an undefended agent on a test. Ørsted's 60 to 70 percent is one firm's process as told to a reporter, with no method published [1][2]. Checking at the boundary also costs real work. Something has to hold an effect and something has to release it, and the policy that settles most effects needs an owner.

A trusted-source policy is still a list written by someone guessing what a type means. The real gain over a change board is that the guess gets checked against the effect rather than the request. It is not a sure thing, and the board's refusal to be optional is what keeps the rest honest while the pipeline speeds up.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "70% of Agent Failures" -> /agent-failures-tests-stayed-green/ [same site (aichieve.net); same category; topical overlap: roughly] Link "70% of Agent Failures" in the section where the article touches roughly. -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> /agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (aichieve.net); same category; topical overlap: percent] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches percent. -->
<!-- internal-link hint: "Multi Agent Orchestration" -> /multi-agent-orchestration-building-the-one-person-enterprise/ [same site (aichieve.net); same category; topical overlap: changes] Link "Multi Agent Orchestration" in the section where the article touches changes. -->
## Related reading

- [70% of Agent Failures](/agent-failures-tests-stayed-green/)
- [Agentic AI Adoption Soars, But Profits Stall in 2026](/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
- [Multi Agent Orchestration](/multi-agent-orchestration-building-the-one-person-enterprise/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Ørsted pushes roughly 60 to 70 percent of its firewall changes through a pre-approved lane that skips the change board. In the same window, a paper measured why a lane cleared by request type is the wrong place for the call. Attack success only falls from 47.0 percent to 2.7 percent when the check sits at the effect crossing into production.
- **Why It Matters:** agents are taking over the change queue itself, with risk-tiered rules and repair jobs that restore settings on their own [3]. If the band is approved by type, the type becomes the target, and most of your change volume gets cleared before anyone sees the facts.
- **What I'd Watch:** whether the vendors selling tiered setups print an error rate, and whether operators who copy the hold-and-decide pattern treat the waiting effects as a new record.
  - **Holding an effect:** pausing one action while the agent keeps working, then releasing or stopping it based on the trace.
  - **Trusted-source policy:** a short list of which sources may cause which effects, settled at the boundary rather than left to a model.
  - **The join:** the link between a change, the request that allowed it, and the person or model behind it.
- **The Catch:** the 47.0 to 2.7 percent result comes from a test on three agent models, not a live network. Checking at the boundary also needs a place to hold effects and someone to keep the policy current.

## Sources

[1] *Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents*, arXiv:2610.18457v1, submitted 2026-10-13 — https://arxiv.org/abs/2610.18457
[2] Denise Dubie, "Ørsted builds compliance into automation, speeds firewall changes", Network World, 2026-10-12 — https://www.networkworld.com/article/4229048/orsted-builds-compliance-into-automation-speeds-firewall-changes.html
[3] "SolarWinds Unveils Avior, Bringing Deterministic, Agentic AI to Enterprise IT", SolarWinds press release, 2026-10-14 — https://www.solarwinds.com/company/newsroom/press-releases/solarwinds-unveils-avior-bringing-deterministic-agentic-ai-to-enterprise-it
[4] "Incident report for October 9 and 10, 2026", Inngest, 2026-10-15 — https://www.inngest.com/blog/2026-10-15-incident-report-for-october-9-and-10-2026

## Gate report

- lead: PASS — opens on the operator's own coverage figure and the paper's finding in sentence three; one figure in the first sentence, no preamble.
- tension: PASS — states the shift and who it hits, carries a plain `By the numbers` block sourced from both anchors, and keeps a first-person cue.
- tactical-insight: PASS — four reported observations with bold lead-ins, no instruction to the reader, one live internal link.
- nuanced-takeaway: PASS — the two honest limits (benchmark result, one operator's numbers) and the cost of boundary checks, closed on a labelled reading.
- tldr: PASS — four-part card carrying both legs and the collision.
