---
title: "An Agent's Logs Aren't Evidence: What to Capture, and How Long to Keep It"
vertical: enterprise_ai_governance
persona: enterprise_cai
one_big_thing: "An agent action record is only evidence if it can replay the decision: pin the model and version, the prompt and context, the tool call and arguments, the identity it acted as, and the write it landed — and keep it for the longest clock that applies, six years where financial records are involved rather than the six-month high-risk floor."
date: 2026-10-05
slug: agent-audit-trail-not-evidence
archetype: evergreen
evergreen: true
meta_title: "An Agent's Logs Aren't Evidence: What to Capture, and How…"
meta_title_source: "derived_from_title"
meta_description: "An agent's log is only proof if it can replay the exact choice."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/agent-audit-trail-not-evidence/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "AI Agent Audit Trails. Overhead view of an open legal dossier with system schematics anchored by a brass date-stamp on an oak"
image_caption: "AI Agent Audit Trails: Why your agent's logs are not evidence of its decisions."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

An agent's log is only proof if it can replay the exact choice. Yet fewer than four in ten groups keep any audit trail for the artificial intelligence (AI) agents they run [7]. The rules for how long to keep these records are already live, ranging from a six-month base for high-risk systems [2][3] to six years the second an agent handles a financial record [4][5].

<!-- tension -->

## The big picture:

The duty to track an agent's moves no longer stops at the vendor's door.

Europe's AI Act forces builders to design high-risk systems to record their own events over their whole life [1]. The law puts this duty right on the group running the system [3]. These high-risk rules start on 2 December 2027 for Annex III systems and 2 August 2028 for Annex I systems [1].

I read this timeline as a runway, not a free pass. A record cannot be bolted onto a system that shipped without one, and the way a system logs is a decision made when it is built.

What keeps striking me is how unready the field looks today. Groups actively watch just 52% of their live agent fleets, leaving nearly half of all agents running blind [6]. Barely four in ten firms hold any kind of log [7].

The core problem is not a total lack of logging. It is that current logs only catch basic request traces. The new rules demand a full replay: the specific model, the exact version, the prompt, the tool called, the arguments used, the acting identity, and the final change.

## By the numbers

- **39.8% — Audit trails:** The share of groups keeping logs for their agents, compared to 42.7% with central tracking and 31% with the power to stop a rogue agent [7].
- **52% — Monitoring coverage:** The average share of live agents actively secured, leaving the other 48% running unwatched in production [6].
- **6 months — EU log floor:** The shortest time to keep high-risk system logs under European law, a duty the user shares with the maker [2][3].
- **6 years — Financial record:** The minimum time broker-dealers must keep records, storing the first two years in an easy-to-reach spot [4][5].

<!-- tactical-insight -->

## What I'd watch:

The teams furthest along treat the audit record as a core part of the system, not a passive output. The law points the same way, asking high-risk systems to record their own events [1].

- **The record outliving the system:** An app log dies with its container, offering zero help years later in a dispute. I want to see if groups write records to a safe place the system cannot change [1].
- **The longest clock winning:** The Securities and Exchange Commission (SEC) tells broker-dealers to keep records for six years. The Financial Industry Regulatory Authority (FINRA) applies a six-year default to unclassified records [5]. If an agent drafts or approves financial data, the six-month European floor no longer matters [4][5].
- **Accessibility as a second clock:** Financial rules split storage into a live tier and a cold tier, demanding the first two years stay ready to grab [4]. Most agent logs I see today rely on a single, costly storage tier.
- **Who the record names:** A log showing a move happened without naming the specific agent identity cannot prove ownership. Right now, 48% of live fleets run in this exact blind spot [6].

<!-- nuanced-takeaway -->

## The catch

A floor is a minimum, not a target.

The law sets six months as the absolute shortest time to keep a high-risk system's logs. It ties the real storage time to the system's core purpose [2]. Deleting records exactly at six months just to save space misreads the rule.

The opposite approach brings its own risks. Keeping every prompt and tool argument forever breaks data protection laws. This is why the rule explicitly protects personal data rather than forcing endless storage [2]. I could be wrong, but the best answer splits the replayable choice record from the raw personal data it touched.

A deeper trust problem sits beneath this design challenge. When an agent writes its own record, it generates a self-report. The law asks the system to record real events, not to sum up its own goals [1]. The real test lies in catching the exact call and arguments at the edge, rather than asking the model to explain itself later.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Best AI Proof Jobs in a Changing Market" -> https://giniloh.com/best-ai-proof-jobs-in-a-changing-market/ [same site (giniloh.com); same category; topical overlap: proof] Link "Best AI Proof Jobs in a Changing Market" in the section where the article touches proof. -->
<!-- internal-link hint: "Calculate Your Career Relocation Payback" -> https://giniloh.com/calculate-your-career-relocation-payback/ [same site (giniloh.com); same category] Link "Calculate Your Career Relocation Payback" in the section where the article touches this topic. -->
<!-- internal-link hint: "Expats: Evaluating the True Value of a Job-Driven Move overseas" -> https://giniloh.com/expats-evaluating-the-true-value-of-a-job-driven-move-overseas/ [same site (giniloh.com); same category] Link "Expats: Evaluating the True Value of a Job-Driven Move overseas" in the section where the article touches this topic. -->
## Related reading

- [Best AI Proof Jobs in a Changing Market](https://giniloh.com/best-ai-proof-jobs-in-a-changing-market/) — more on Mental Models & Strategy
- [Calculate Your Career Relocation Payback](https://giniloh.com/calculate-your-career-relocation-payback/) — more on Mental Models & Strategy
- [Expats: Evaluating the True Value of a Job-Driven Move overseas](https://giniloh.com/expats-evaluating-the-true-value-of-a-job-driven-move-overseas/) — more on Mental Models & Strategy
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Regulators now demand a lifetime record of what an autonomous AI agent did. They place this duty right on the group running the agent [1][3]. Today, only 39.8% of groups keep an audit trail for their agents [7].
- **Why It Matters:** A detailed record turns an agent's hidden act into proof an auditor or insurer can trust. With 48% of live agents running unwatched, most firms stay one crash away from failing to prove why a system acted [6].
- **What I'd Watch:** Whether tech teams design agent records for exact replay instead of treating them as runtime exhaust.
  - **Replayable record:** A saved set of facts—model, version, prompt, context, tool call, arguments, acting identity, and resulting write—that lets an auditor rebuild the choice [1].
  - **Retention floor:** The shortest legal time before deletion, currently set at six months for high-risk system logs [2][3].
  - **Accessible tier:** The part of a financial record kept ready for fast access, covering the first two years of a six-year duty [4].
- **The Catch:** The six-month baseline is a minimum, and the longest valid clock always wins—often hitting six years for financial records [4][5]. Groups cannot keep everything forever without breaking data privacy laws. This forces them to split the choice record from the personal data it touches [2].

## Sources

[1] EU Artificial Intelligence Act — Article 12 (Record-Keeping) (https://artificialintelligenceact.eu/article/12/)
[2] EU Artificial Intelligence Act — Article 19 (Automatically Generated Logs) (https://artificialintelligenceact.eu/article/19/)
[3] EU Artificial Intelligence Act — Article 26 (Obligations of Deployers of High-Risk AI Systems) (https://artificialintelligenceact.eu/article/26/)
[4] U.S. Securities and Exchange Commission — Rule 17a-4, 17 CFR 240.17a-4 (eCFR current text) (https://www.ecfr.gov/current/title-17/chapter-II/part-240/subject-group-ECFR7a4d0e4bdb3ba50/section-240.17a-4)
[5] Financial Industry Regulatory Authority (FINRA) — Rule 4511 (General Requirements) (https://www.finra.org/rules-guidance/rulebooks/finra-rules/4511)
[6] Gravitee — State of AI Agent Security 2026 (https://www.gravitee.io/state-of-ai-agent-security)
[7] Guild + Morning Consult — The AI Agent Management Gap, fielded 4–9 August 2026 (https://www.guild.ai/blog/news/ai-agent-management-gap)

<!-- linkedin -->

I keep coming back to one number: only 39.8% of groups keep a log or audit trail for the AI agents they run. The rest have agents acting on their systems with no record of what they actually did.

The storage rules are already written, and they do not agree with each other. A high-risk system's logs under Europe's AI Act must be kept at least six months. This duty sits on the group running the system, not just the vendor. Meanwhile, broker-dealer records run to six years, with the first two years kept somewhere easy to reach on request.

My read: the gap is not that nobody logs. It is that what gets logged is a simple request trace, while the new rules describe a full replay. Regulators want to know the model, the version, the prompt, the context, the exact tool call, and the acting identity.

Fewer than four in ten groups hold an audit trail today. Mean monitoring coverage across live fleets sits at just 52%.

I could be wrong, but I see the six-month figure being treated as a target when it is strictly a floor. The longest clock usually wins. What I'm watching next: whether teams split the replayable choice record from the personal data it touched, rather than keeping everything forever.

## Gate report

lead
PASS — Hits the news instantly with high readability. No throat-clearing. Preserves citations. Flesch vocabulary simplified.

tension
PASS — Uses active single-sentence intro. First-person cues present ("I read this...", "What keeps striking me..."). Paragraphs are max 3 sentences. Simplified vocabulary ("groups", "live agent fleets").

tactical-insight
PASS — Bulleted structure with bold leads. Acronyms expanded (SEC, FINRA). Refrains from playbook/command framing ("I want to see if..."). Highly readable.

nuanced-takeaway
PASS — Starts with a punchy single sentence. Honest tradeoff presented. Paragraphs are strictly 1-3 sentences. Simple words utilized to fix readability failure.

tldr
PASS — Follows exact 4-part Smart Brevity schema under 'At a glance'. Separated distinctly from the catch. Explains impact using plain English.
