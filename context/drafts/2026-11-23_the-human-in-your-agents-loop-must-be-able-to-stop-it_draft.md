---
title: "The Human in Your Agent's Loop Must Be Able to Stop It"
vertical: enterprise_ai_governance
kind: evergreen
archetype: evergreen
evergreen: true
persona: enterprise_cai
one_big_thing: "The EU AI Act makes human oversight a design property, not a meeting: Article 14 names five abilities the overseer must hold — understand the limits, resist automation bias, read the output, override it, stop the system — and Article 26 says those people need competence, training and authority, so a checkpoint whose operator cannot legally do all five is a checkbox, not a control."
date: 2026-11-23
slug: the-human-in-your-agents-loop-must-be-able-to-stop-it
meta_title: "The Human in Your Agent's Loop Must Be Able to Stop It"
meta_description: "Article 14 of the EU AI Act names five abilities a human overseer must hold and Article 26 says they need competence, training and authority — audit your checkpoint against the list."
---

<!-- lead -->

The European Union's AI Act does not let a deployer park a person beside an autonomous agent and call that oversight. Article 14 requires that the system itself "can be effectively overseen by natural persons during the period in which they are in use" [1], and it lists, in law, what the person must be able to do — including interrupting the system "through a 'stop' button or a similar procedure that allows the system to come to a halt in a safe state" [1]. Article 26 then says the deployer must "assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support" [2]. For AI systems classified as high-risk under Annex III, those Chapter III requirements apply from 2 December 2027 as of the amended timeline [3]. A checkpoint nobody can legally exercise is a headcount on a rota, not a control.

<!-- tldr -->

## At a glance

- **The list:** Article 14(4) sets five abilities the overseer must hold — understand the system's limits, resist automation bias, interpret the output, override it, and stop the system safely [1].
- **The staffing:** Article 26(2) makes the deployer assign oversight to people with competence, training, authority and support [2].
- **The clock:** 2 December 2027 for Annex III high-risk systems, per the amended Article 113 [3].

<!-- tension -->

## The big picture: five abilities, spelled out

Article 14(4) is unusually concrete for a statute. The overseer must be able, "as appropriate and proportionate" [1]:

- to properly understand the system's capacities and limitations and monitor its operation, including detecting anomalies and unexpected performance;
- to remain aware of "the possible tendency of automatically relying or over-relying on the output" — automation bias, named in the text [1];
- to correctly interpret the output, using the interpretation tools provided;
- to decide not to use the system, or to disregard, override or reverse its output; and
- to intervene or interrupt the system through a stop button that brings it to a halt in a safe state [1].

That last clause is the one most agent deployments fail first. An agent that writes to a system of record through a queue, or that runs inside a framework without a transaction boundary, has no safe-state halt: pulling the person off the keyboard leaves writes in flight. My read of the five abilities is that they read like a role description for a job most companies have not defined — the stop-button clause is a dead giveaway, because you cannot assign it to someone whose only tool is the same chat window the agent uses.

Article 14(1) puts the burden on the provider's design: the system must be built, "including with appropriate human-machine interface tools", so it can be effectively overseen [1]. Article 26(2) puts the burden on the deployer: assign oversight to people with the necessary competence, training and authority — and support [2]. Two parties, two duties, one control surface. The enterprise that buys a high-risk system and wires it into a workflow owns the second half even when the vendor ships a perfect interface.

One clause goes further than a staffing plan. For high-risk biometric identification systems in point 1(a) of Annex III, Article 14(5) says no action may be taken on the system's identification "unless that identification has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority" [1]. Two signatures, in law, for one class of decision.

## By the numbers

- **5 abilities:** the closed list in Article 14(4) — understand limits, resist automation bias, interpret output, override, stop [1].
- **2 natural persons:** the verification floor Article 14(5) sets for biometric identification results in point 1(a) of Annex III (waivable for law enforcement, migration, border control or asylum where disproportionate) [1].
- **2 December 2027:** the application date, as amended, for the Chapter III requirements on AI systems classified as high-risk under Article 6(2) and Annex III [3].

<!-- tactical-insight -->

## What to audit before the clock runs

The amendments that produced 2 December 2027 are a warning on their own: prohibitions 1 through 8 of the Act took effect in February 2025, while prohibition 9, added through the AI Omnibus, only comes into effect in December 2026 [4]. The dates move, so pin the timeline you plan against to the amended Article 113 text, not to a summary written before the amendment [3][4].

Then run each production agent against the five abilities as a checklist. For every agent you would classify as high-risk, name the person who holds oversight and ask four questions. Can they see the system's limits and its anomalies — is there any display of what the model can and cannot do, and of where its confidence runs out? Can they interpret the output with real interpretation tools, or only re-read prose? Can they override or reverse the output after it has landed — in the system of record, not in the chat transcript? And can they stop the agent such that it halts in a safe state, mid-flight, without corrupting the queue behind it? Any "no" is a finding, and the fix is an engineering change — an interface, a transaction boundary, a kill path — not another slide in the governance deck.

Article 26(2)'s staffing clause turns the same checklist into a rota problem. Competence, training and authority are separable, and the gap is usually authority: the analyst who watches an agent underwrite loans at 3 a.m. but cannot push a reversal button holds competence without authority, and under Article 26 that assignment is the deployer's legal responsibility [2]. The audit line is the person's name and, beside it, the mechanism for each ability — because oversight that exists only in the workflow chart does not satisfy a clause written about "human-machine interface tools" [1].

This pairs with the record-keeping half of the same chapter: an audit trail is only evidence if it captures what a named overseer did with these abilities, which is the argument this desk made about agent logs and replay — see [an agent's logs aren't evidence](/agent-audit-trail-not-evidence/) for the capture list that survives a regulator.

<!-- nuanced-takeaway -->

## The catch

Every obligation here is conditional on the system being high-risk, and classification is its own decision. The Chapter III requirements reach systems that fall under Article 6(2) and Annex III; if your agent is not in an Annex III use case, Article 14 does not bind you directly [3]. The honest reading is not that the list then stops mattering, but that it stops being law and becomes due diligence: the five abilities describe how a competent human catches a machine's error, whether or not a regulator is asking.

The list is also aspirational in one respect the text concedes: "as appropriate and proportionate" [1]. That phrase is doing real work, and it is where most of the argument with a market-surveillance authority would happen. A proportionate oversight arrangement for an agent triaging support tickets is not the same as for an agent underwriting loans, and the statute leaves that calibration to the deployer's risk assessment.

What survives both cautions is the shape. The Act defines oversight as abilities, held by named people, exercised through interfaces the provider had to build [1][2]. Abilities can be tested. A person standing next to an agent with no override, no interpretation tools and no stop button tests the whole arrangement to failure — the test just runs after the incident instead of before it.

## Sources

- [1] EU AI Act (Regulation (EU) 2024/1689), Article 14: Human Oversight — https://www.euaiact.com/article/14
- [2] EU AI Act (Regulation (EU) 2024/1689), Article 26: Obligations of Deployers of High-Risk AI Systems — https://www.euaiact.com/article/26
- [3] EU Artificial Intelligence Act — Article 113: Entry into Force and Application — https://artificialintelligenceact.eu/article/113/
- [4] European Commission, "A European approach to Artificial Intelligence" — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
