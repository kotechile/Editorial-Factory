---
title: "An Agent's Logs Aren't Evidence: What to Capture, and How Long to Keep It"
vertical: enterprise_ai_governance
persona: enterprise_cai
one_big_thing: "An agent action record is only evidence if it can replay the decision: pin the model and version, the prompt and context, the tool call and arguments, the identity it acted as, and the write it landed — and keep it for the longest clock that applies, six years where financial records are involved rather than the six-month high-risk floor."
date: 2026-10-05
slug: agent-audit-trail-not-evidence
archetype: evergreen
evergreen: true
---

<!-- lead -->

Only 39.8% of organisations keep a log or an audit trail for the artificial intelligence (AI) agents they run, and the record most of them keep cannot answer the one question it will be asked: why did the agent do that [7]. The rules on how long that record has to live are already written, and they disagree with each other — at least six months for the logs of a high-risk system [2][3], and six years once an agent's output becomes a financial record [4][5].

<!-- tension -->

## The big picture:

The duty to keep an agent's record no longer stops at the vendor's door. Europe's AI Act requires a high-risk system to be built so it can record its own events from the day it runs, over the lifetime of the system rather than around an incident [1].

The same law puts the retention duty on the organisation running the system, not only on the company that made it [3]. The article text as published notes those high-risk duties begin 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems [1]. I read that as a runway, not a reprieve, because a record schema is a build-time decision. You cannot retro-fit provenance onto a system that shipped without it.

What keeps striking me is how thin the field state is next to that runway. Mean monitoring coverage across deployed agent fleets is 52%, which leaves 48% of production agents running with no security or governance monitoring at all, and only 9.5% of organisations secure more than 81% of theirs [6]. Fewer than four in ten hold a log or audit trail of any kind [7].

The gap is not that nobody logs. It is that what gets logged is a request trace — a call went out at 03:14 — while the rules describe a replay: which model, at which version, given which prompt and context, calling which tool with which arguments, acting as which identity, writing which change.

## By the numbers

- **39.8% — Audit trails:** the share of organisations holding logging or audit trails for their agents, against 42.7% with central monitoring and just 31% able to stop a misbehaving agent immediately [7].
- **52% — Monitoring coverage:** the mean share of deployed agents actively monitored and secured, so the other 48% run unmonitored in production [6].
- **six months — EU log floor:** the minimum retention for logs a high-risk system generates, and the deployer carries that duty as well as the provider [2][3].
- **6 years — Financial record:** broker-dealer records are preserved at least 6 years, with the first two years in an easily accessible place [4][5].

<!-- tactical-insight -->

## What I'd watch:

The teams furthest along treat the record as part of the system, not an output of it. The statute points the same way when it asks a high-risk system to be able to record its own events over its lifetime [1].

- **The record outliving the system:** an application log dies with the container that wrote it, which is no help three years into a dispute. What I want to see is whether the record is written somewhere the system itself cannot rewrite [1].
- **The longest clock winning:** the Securities and Exchange Commission (SEC) rule for broker-dealer records runs to six years, and anything with no separately specified period still runs to six under the Financial Industry Regulatory Authority (FINRA) rule [5]. Where an agent drafts, approves or books anything financial, the six-month European floor is not the number that matters [4][5].
- **Accessibility as a second clock:** the financial-records rule splits retention into a live tier and a cold tier, with the first two years kept where they can actually be produced on request [4]. Most agent logs I have seen have exactly one tier — the expensive one.
- **Who the record names:** a record that says an action happened but not which agent identity performed it cannot be attributed to a system or an owner, which is the state 48% of production fleets are in [6].

<!-- nuanced-takeaway -->

## The catch

A floor is a floor, not a target. Six months is the least a high-risk system's logs may be kept, and the same article ties retention to the purpose the system was built for [2]. Deleting at six months and one day because the number looks tidy is a misreading.

The opposite failure is just as real. Keeping every prompt and every tool argument forever collides with data-protection law, which is why the retention clause carves out the protection of personal data rather than setting an open-ended duty [2]. I could be wrong, but the workable answer looks like a schema that separates the replayable decision record from the payload it was made on.

There is also a trust problem underneath the design problem. A record the agent writes about itself is a self-report. The statute asks the system to record events, not to summarise its own intentions [1] — which is why the interesting engineering sits in capturing the call and its arguments at the boundary, not in asking the model to explain itself afterwards.

<!-- tldr -->

## At a glance

- **The Big Shift:** Regulators now require a record of what an autonomous AI agent did, over the system's lifetime, and they put part of that retention duty on the organisation running the agent rather than only on the vendor [1][3]. Only 39.8% of organisations hold a log or audit trail for their agents today [7].
- **Why It Matters:** The record is what turns an agent's action into something a regulator, an auditor or an insurer can accept. With mean monitoring coverage at 52% and 48% of production agents unmonitored, most enterprises are one incident away from being unable to reconstruct what happened [6].
- **What I'd Watch:** whether agent records start being designed for replay instead of written as a by-product of runtime.
  - **Replayable record:** a captured set of facts — model and version, prompt and context, tool call and arguments, acting identity, resulting write — that lets someone rebuild the decision later [1].
  - **Retention floor:** the shortest period the law lets you delete, set at six months for high-risk system logs [2][3].
  - **Accessible tier:** the part of a financial record kept where it can be produced quickly, currently the first two years of a six-year duty [4].
- **The Catch:** the six-month figure is a minimum, not a plan, and the longest applicable clock usually wins — six years where financial records are involved [4][5]. Keeping everything forever runs into data-protection limits instead, so the schema has to separate the decision record from the personal data it touched [2].

## Sources

[1] EU Artificial Intelligence Act — Article 12 (Record-Keeping) (https://artificialintelligenceact.eu/article/12/)
[2] EU Artificial Intelligence Act — Article 19 (Automatically Generated Logs) (https://artificialintelligenceact.eu/article/19/)
[3] EU Artificial Intelligence Act — Article 26 (Obligations of Deployers of High-Risk AI Systems) (https://artificialintelligenceact.eu/article/26/)
[4] U.S. Securities and Exchange Commission — Rule 17a-4, 17 CFR 240.17a-4 (eCFR current text) (https://www.ecfr.gov/current/title-17/chapter-II/part-240/subject-group-ECFR7a4d0e4bdb3ba50/section-240.17a-4)
[5] Financial Industry Regulatory Authority (FINRA) — Rule 4511 (General Requirements) (https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511)
[6] Gravitee — State of AI Agent Security 2026 (https://www.gravitee.io/state-of-ai-agent-security)
[7] Guild + Morning Consult — The AI Agent Management Gap, fielded 4–9 August 2026 (https://www.guild.ai/blog/news/ai-agent-management-gap)

<!-- linkedin -->

I keep coming back to one number: only 39.8% of organisations keep a log or audit trail for the AI agents they run. The rest have agents acting on their systems with no record of what they did.

The retention rules are already written, and they do not agree with each other. A high-risk system's logs under Europe's AI Act must be kept at least six months, and the duty sits on the organisation running the system, not just the vendor. Broker-dealer records run to six years, with the first two years kept somewhere they can actually be produced on request.

My read: the gap is not that nobody logs. It is that what gets logged is a request trace, while the rules describe a replay — which model and version, which prompt and context, which tool call with which arguments, acting as which identity, writing which change. Fewer than four in ten hold an audit trail at all, and mean monitoring coverage across production fleets sits at 52%.

I could be wrong, but the six-month figure gets read as a target when it is a floor, and the longest clock usually wins. What I'm watching next: whether teams separate the replayable decision record from the personal data it touched, instead of keeping everything forever and calling it compliance.
