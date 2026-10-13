---
title: "Your AI Incident Clock: 4 Hours, Not 15 Days"
vertical: enterprise_ai_governance
persona: enterprise_cai
one_big_thing: "Europe's AI Act serious-incident report is a provider's filing and, under Regulation (EU) 2026/1744, does not apply until 2 December 2027 — so the incident clock an enterprise actually has to meet is the shortest one already running in its own rulebooks: 72 hours for a personal-data breach, 24 hours for an early warning, and four hours from classification for a major technology incident."
date: 2026-10-12
slug: ai-incident-clock-4-hours-not-15-days
archetype: evergreen
evergreen: true
meta_title: "Your AI Incident Clock: 4 Hours, Not 15 Days"
meta_description: "The AI Act's 15-day serious-incident report is the vendor's filing and starts in December 2027. The clocks an enterprise has to meet are 72, 24 and 4 hours."
---

<!-- lead -->

Four hours is how long a financial firm has to tell its supervisor that a technology incident is major, once it has classified it that way [9]. Fifteen days is the number most European incident playbooks for artificial intelligence (AI) were built around — the deadline in the AI Act's serious-incident article [1]. Those two numbers are not the same kind of thing. The 15-day report belongs to the company that put the high-risk system on the market, and as the law now reads it does not apply until 2 December 2027 [2][3].

<!-- tension -->

## The big picture:

The duty to report a serious AI incident sits on whoever placed the high-risk system on the European market. The text is blunt about it: providers report to the market surveillance authority of the member state where the incident happened, immediately after establishing a causal link or believing one is likely, and "in any event, not later than 15 days after the provider or, where applicable, the deployer, becomes aware of the serious incident" [1]. Two shorter deadlines sit inside the same article — two days where the incident is a widespread infringement or a serious and irreversible disruption of critical infrastructure, and 10 days where a person has died [1].

What counts as serious is wider than most people assume. It runs from death and serious harm to health, through a serious and irreversible disruption of critical infrastructure, to the infringement of European Union law meant to protect fundamental rights, and on to serious harm to property or the environment [4]. That third limb is the one that makes an agent leaking personal data, or denying someone a service, a candidate for the report at all.

What strikes me is who is not the filer. The enterprise running the system has a different duty in the same chapter: where it identifies a serious incident, it informs the provider first, then the importer, and suspends use of the system [2]. No filing deadline is attached to that sentence.

Then the schedule moved. Regulation (EU) 2026/1744 rewrote Article 113 of the Act, and the amended text applies the high-risk sections — the ones the reporting duty lives in — from 2 December 2027 for systems classified high-risk under Annex III, and from 2 August 2028 for systems inside regulated products under Annex I [3]. The deployer's own article carries those same dates [2]. So the enterprise that spent this year preparing for an obligation dated August 2026 is now waiting until December 2027 — for a duty it was never the filer of.

The clocks that are running sit in other rulebooks, and every one of them is shorter. A personal-data breach goes to the supervisory authority without undue delay and, where feasible, within 72 hours of the controller learning of it [7]. A significant incident under the European Union's network and information security rules draws an early warning within 24 hours, an incident notification within 72, and a final report within a month [8]. For a financial entity, a major technology incident under the Digital Operational Resilience Act (DORA) goes to the supervisor within four hours of being classified as major, and no later than 24 hours from discovery [9].

## By the numbers

- **15 days — The provider's AI Act report:** the deadline for a serious incident, counted from awareness, with two days for critical-infrastructure disruption and 10 days after a death [1].
- **2 December 2027 — When it starts:** the amended application date for the high-risk rules, including the incident report, with 2 August 2028 for systems inside regulated products [3].
- **24 hours — Early warning:** the first of three filings for a significant incident, then an incident notification at 72 hours and a final report within a month [8].
- **four hours — From classification:** how long a financial entity has after calling an incident major, with a 24-hour outer bound running from discovery [9].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this have stopped treating notification as paperwork and started treating the classification decision as the deadline. What I'd watch next:

- **Where the timer actually starts.** DORA's four hours run from classification, and the outer 24-hour bound runs from discovery, so the decision itself sits inside the clock [9]. I have sat in reviews where reconstructing what an agent did took a week; none of these three regimes waits a week.
- **Whether the enterprise has quietly become the provider.** A deployer stops being only a deployer if it puts its own name or trademark on the system, makes a substantial modification, or changes the intended purpose: it is then treated as a provider and takes on the provider's obligations, which is where the serious-incident report lives [5]. The part I keep circling is that the branding call is usually a product decision, and the filing duty is usually a compliance one.
- **The one AI Act clock already in force.** Providers of general-purpose models with systemic risk have had to track, document and report serious incidents to the AI Office without undue delay since 2 August 2025 [6]. That one belongs to the model vendor, so for an enterprise it is a supplier-contract question rather than a filing.
- **What the vendor's notice promises.** If the 15-day report is the vendor's, the enterprise's own 72-hour clock starts when it knows enough to classify. Whether the contract promises notice within hours or within days decides whether that deadline gets met or gets explained [7].

<!-- nuanced-takeaway -->

## The catch

No single number applies to every reader, and I would distrust anyone naming one without asking which regime you sit in. Four hours binds financial entities and the technology providers inside that perimeter [9]; 24 hours binds organisations in the scope of the network and information security rules [8]; 72 hours applies once personal data is involved [7]. Where none of those reaches an incident, the enterprise owes no notification at all — which is a different answer from "the AI Act covers it".

There is a second limit. A notice tells a regulator what happened; it does not stop the agent. Whatever evidence a firm produces inside four hours is what it captured before the incident, and a record that cannot replay the decision is not much use to a supervisor reading it later [1][4]. I could be wrong, but the sequencing looks unavoidable: the clock is short, the classification starts it, and the classification is only as fast as the record underneath it.

The date change cuts both ways. The December 2027 runway is real for a deployer's own duties, and it defers nothing for anyone who takes the provider role — including the enterprise that brands, modifies or repurposes a system [5].

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Europe's AI Act serious-incident report is the provider's filing, and Regulation (EU) 2026/1744 moved the high-risk rules that contain it to 2 December 2027 (2 August 2028 for systems inside regulated products). The incident clocks already running on an enterprise are shorter: 72 hours for a personal-data breach [7], 24 hours for an early warning [8], four hours from classification under DORA [9].
- **Why It Matters:** An incident playbook built on "15 days" has rehearsed a filing the enterprise may not owe, and the deadlines that do bind it begin with a classification decision rather than a notification. A provider role taken quietly — through branding or modification — pulls the AI Act report and its timeline back onto the enterprise [5].
- **What I'd Watch:** whether the classification decision moves inside the timer, and whether the provider role has been taken without anyone registering it.
  - **Serious incident:** an AI system's incident or malfunctioning that leads to death or serious harm to health, a serious and irreversible disruption of critical infrastructure, an infringement of European Union law protecting fundamental rights, or serious harm to property or the environment [4].
  - **Early warning:** the first of three filings for a significant incident, due within 24 hours of becoming aware [8].
  - **Major ICT-related incident:** the DORA category that starts the four-hour initial-notification clock once a financial entity classifies it that way [9].
- **The Catch:** the shortest applicable clock wins, and it turns on the regime rather than the technology — four hours, 24 hours or 72 hours. Where none of them applies, the enterprise files nothing, which is not the same as being covered.

## Sources

[1] EU Artificial Intelligence Act — Article 73, Reporting of Serious Incidents (https://artificialintelligenceact.eu/article/73/)
[2] EU Artificial Intelligence Act — Article 26, Obligations of Deployers of High-Risk AI Systems (https://artificialintelligenceact.eu/article/26/)
[3] EU Artificial Intelligence Act — Digital Omnibus on AI (Regulation (EU) 2026/1744), amended Article 113 (https://artificialintelligenceact.eu/ai-act-explorer/digital-omnibus)
[4] EU Artificial Intelligence Act — Article 3, definition of "serious incident" (https://artificialintelligenceact.eu/article/3/)
[5] EU Artificial Intelligence Act — Article 25, Responsibilities Along the AI Value Chain (https://artificialintelligenceact.eu/article/25/)
[6] EU Artificial Intelligence Act — Article 55, Obligations of Providers of General-Purpose AI Models with Systemic Risk (https://artificialintelligenceact.eu/article/55/)
[7] General Data Protection Regulation — Article 33, Notification of a personal data breach to the supervisory authority (https://gdpr-info.eu/art-33-gdpr/)
[8] NIS2 Directive (EU) 2022/2555 — Article 23, Reporting obligations (https://www.nis-2-directive.com/NIS_2_Directive_Article_23.html)
[9] FMA Austria — DORA: ICT-related incidents, initial notification within four hours of classification (Delegated Regulation (EU) 2025/301) (https://www.fma.gv.at/en/cross-sectoral-topics/dora/dora-ict-related-incidents)
