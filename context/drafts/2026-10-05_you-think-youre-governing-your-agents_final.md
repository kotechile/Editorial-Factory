---
title: "You Think You're Governing Your AI Agents. The Data Says You're Not."
vertical: enterprise_ai_governance
persona: enterprise_cai
one_big_thing: "Non-human identities are now the #1 route into the enterprise, and the open agent control plane (OpenClaw Enterprise) is the runtime enforcement layer the policy-only model never was."
date: 2026-10-05
slug: you-think-youre-governing-your-agents
synthesis: true
sources:
  - https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities
  - https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise
---

<!-- lead -->

Stolen machine identities just became the top way hackers break into companies. Just weeks after this data dropped, tech leaders shared free code to help fix the massive blind spot.

<!-- tension -->

## The big picture:

The gap between what bosses believe and what is true keeps growing. 

A SpyCloud poll of 750 security chiefs shows that stolen non-human identities (NHIs) are now the main way attackers get in [1]. These include service accounts, application programming interface (API) keys, and artificial intelligence (AI) agents. I have been watching this shift, and the blind spot shocks me. Most firms (95%) say they see their machine identities. Yet only 36% actually track them [1].

Rule-making lags behind tech use. About 91% of companies run AI agents with deep access, but just 56% have strict rules for them [1]. My read: firms still treat safety as a paper document, while the live systems ignore it.

## By the numbers

- **31% vs 17% — NHI entry point:** stolen machine identities are nearly twice as likely as phishing to let hackers in [1].
- **95% vs 36% — Tracking gap:** firms that think they track machine identities versus those that really do [1].
- **91% vs 56% — Rule lag:** firms running AI agents with deep access versus those with strict rules for them [1].
- **3 — Open control backers:** OpenAI, Red Hat, and a top chipmaker are building OpenClaw Enterprise as free software for always-on agents [2].

<!-- tactical-insight -->

## What I'd watch:

The builders closest to this problem are voting with code. Red Hat calls OpenClaw Enterprise a major shift for agents. They frame it as a tool to run agents across teams [2]. Kevin Lin leads this work at OpenAI. He notes that companies want the same safety from agents that they expect from normal software [2].

What I'd watch next:

- **The live replacement:** engineers are moving rules into the active systems with scoped access and instant cut-offs. I want to see if this live layer closes the 95-to-36 tracking gap [1][2].
- **The RBAC shift:** role-based access control (RBAC) checks human logins, but agents keep acting long after that. I am curious how many firms will wire new tokens together to manage this live access [4].
- **The rule hammer:** 94% of groups work where AI laws apply, but only 29% are ready for the European Union (EU) AI Act [3]. I expect this new software to become the exact proof that auditors demand.

<!-- nuanced-takeaway -->

## The catch

I could be wrong that this software fixes the debate. Free code is still early tech. Open software does not mean safe systems. Better tools fail to fix the blame gap if nobody owns the identities. A control plane only keeps a company safe if a human turns it on and runs it. That 95-to-36 tracking gap is a belief problem. Belief rarely changes just because the tools get better.

<!-- tldr -->

## At a glance

- **The Big Shift:** Non-human identities (NHIs) are now the main way hackers breach firms, showing a huge gap in tracking. Meanwhile, tech giants just launched OpenClaw Enterprise to move agent rules from static paper to live systems.
- **Why It Matters:** Enterprise AI rules are moving out of paper documents and into the live tech stack. With 94% of firms facing AI laws and only 29% ready for the European Union (EU) AI Act, active checks are now a must.
- **What I'd Watch:** whether these live systems actually force firms to track their agents.
  - **Control plane:** the software layer that actively limits what an agent can do in real time.
  - **Non-human identity (NHI):** the keys or accounts that let software act inside a system.
  - **RBAC (role-based access control):** an older model that grants access based on a human's job at login, which fails when agents act on their own.
- **The Catch:** open tools do not fix broken trust. System upgrades cannot solve the safety gap if no one actively owns and tracks the machine identities.

## Sources

[1] SpyCloud — 2026 Identity Threat Report (https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities)
[2] Red Hat — "Why Red Hat is building an open foundation for enterprise agents with OpenClaw Enterprise" (https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise)
[3] Cloud Security Alliance — "Enterprise Reality: Why Organizations Aren't as Prepared for AI Governance as They Think They Are" (https://cloudsecurityalliance.org/blog/2026/09/16/enterprise-reality-why-organizations-aren-t-as-prepared-for-ai-governance-as-they-think-they-are)
[4] Cloud Security Alliance — "Shadow AI Does Not Read Your Org Chart: Rethinking Identity Governance for Autonomous Agents" (https://cloudsecurityalliance.org/blog/2026/09/08/shadow-ai-does-not-read-your-org-chart-rethinking-identity-governance-for-autonomous-agents)

<!-- linkedin -->

I keep coming back to one number this week: 95% of firms say they see their machine identities, but only 36% actually track them. SpyCloud's latest report finds non-human identities (NHIs) — the application programming interface (API) keys, service accounts, and artificial intelligence (AI) agents nobody turns off — are now the top way hackers get in. They nearly double phishing. My read: we measure safety by whether a policy exists, but the live systems stopped obeying it a while ago. Just weeks later, tech giants shared free code to fix this. OpenClaw Enterprise launched with backing from Red Hat, OpenAI, and top chip leaders, applying a fresh playbook to agents. I could be wrong, but it looks like the fix for a belief problem is finally being built as real systems rather than paper documents. What I'm watching next: whether a live control plane actually closes that 95-to-36 gap, or just gives us a cleaner screen for the same unowned identities.

## Gate report

lead: PASS — Delivers the core news (stolen machine identities as the top entry point and the release of free control plane code) immediately in sentence 1 without preamble.
tension: PASS — Features the mandatory H2, short framing paragraphs, a first-person cue ("I have been watching this shift"), and properly formatted 'By the numbers' bullets with exact citations.
tactical-insight: PASS — Uses 'What I'd watch:' H2, includes first-person cues ("I want to see"), and formats 3 actionable observations as bolded bullets without commanding the reader.
nuanced-takeaway: PASS — Opens with 'The catch' H2, includes a first-person cue ("I could be wrong"), and clearly articulates the limitation of open-source tooling solving a human belief problem.
tldr: PASS — Follows the exact 4-part Smart Brevity schema under 'At a glance', including indented sub-bullets defining technical terms in plain English. Flesch reading ease improved via simplified vocabulary and shorter sentences, and all acronyms (including all-caps brand tokens) are handled correctly.
