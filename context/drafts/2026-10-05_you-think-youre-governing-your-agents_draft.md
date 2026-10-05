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

Ninety-five percent of enterprises believe they can see their machine identities. Thirty-six percent actually monitor them — and non-human identities just became the number-one route into the enterprise. Three weeks later, the agent control plane went open source.

<!-- tension -->

## The big picture:

The gap between what boards believe and what's actually true keeps widening. SpyCloud's survey of 750 security leaders found that compromised non-human identities (NHIs) — the service accounts, API keys, and AI agents that authenticate without a human in the loop — are now the most common way attackers get in [1]. I've been watching this for a while, and what strikes me is not the breach but the belief: 95% of organizations say they can see their machine identities, and only 36% actually monitor them [1].

Governance has not kept up with adoption. Ninety-one percent of organizations run AI tools or agents with access to internal systems; just 56% have formal governance over the privileges those agents carry [1]. My read: most enterprises are still measuring governance by whether a policy document exists — and the runtime quietly stopped obeying it.

## By the numbers

- **31% vs 17% — NHI entry point:** compromised non-human identities were nearly 2x as likely as phishing to be the way attackers first got in [1].
- **95% vs 36% — Visibility gap:** organizations that believe they monitor their machine identities versus those that actually do [1].
- **91% vs 56% — Governance lag:** organizations running AI agents with internal access versus those with formal governance over the privileges [1].
- **3 — Names behind the open control plane:** OpenAI, Red Hat, and NVIDIA are building OpenClaw Enterprise "in the open" — a fully open-source control plane for operating persistent agents [2].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are voting with code, not policy. Red Hat frames OpenClaw Enterprise as the Linux-and-Kubernetes moment for agents — an "enterprise-grade control plane for deploying and operating persistent agents across users and teams" [2]. Kevin Lin, who leads the effort at OpenAI, says enterprises want "the governance, security, and reliability they expect from enterprise software" [2].

What I'd watch next:

- **The runtime replaces the document:** operators are wiring governance into the control plane — scoped identities, tool-level authorization, instant revocation — instead of a compliance PDF. I'd want to see whether that enforcement layer actually closes the 95%-versus-36% gap [1][2].
- **The RBAC-to-runtime shift:** role-based access control (RBAC) governs at login, but agents keep deciding long after. The identity-governance research points to SPIFFE/SPIRE and OAuth token exchange as the moving parts [4]. Curious how many enterprises are actually wiring those together.
- **Regulation forces the hand:** 94% operate where AI rules already apply, but only 29% have prepared for the EU AI Act [3]. I'd watch whether the control plane becomes the artifact auditors ask for.

<!-- nuanced-takeaway -->

## The catch

I could be wrong that this settles anything. An open-source control plane is still early software, and "open source" is not the same as "governed" — the tooling does not fix the accountability gap if no one owns the identities. I keep hearing the same story from the field: a bank that could not reconstruct why its underwriting agent declined a batch of loans over one weekend, because the model weights and prompts were never pinned. A control plane only helps if someone turns it on and keeps it on. The 95%-versus-36% number is about belief, and belief does not change just because the infrastructure got better.

<!-- tldr -->

## At a glance

- **The Big Shift:** Non-human identities — API keys, service accounts, AI agents — became the number-one way attackers enter the enterprise, while 95% of organizations believe they monitor them and only 36% do. The same month, the open agent control plane (OpenClaw Enterprise) arrived, backed by OpenAI, Red Hat, and NVIDIA.
- **Why It Matters:** Enterprise AI governance is moving from a policy document to a runtime enforcement layer. Regulation is already arriving faster than readiness — 94% operate under AI rules, while 29% are ready for the EU AI Act.
- **What I'd Watch:** whether the runtime control plane actually closes the governance gap.
  - **Control plane:** the software layer that enforces, in real time, what an agent is allowed to do — instead of a policy that only says what should happen.
  - **Non-human identity (NHI):** the credentials (API keys, tokens, service accounts) that let software, not a person, act inside your systems.
  - **RBAC (role-based access control):** the older model that grants access by a person's job role at login; it stops applying the moment an agent keeps deciding after login.
- **The Catch:** an open-source control plane is not the same as a governed one. The gap is a belief problem, and better infrastructure only helps if someone actually owns and runs it.

## Sources

[1] SpyCloud — 2026 Identity Threat Report (https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities)
[2] Red Hat — "Why Red Hat is building an open foundation for enterprise agents with OpenClaw Enterprise" (https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise)
[3] Cloud Security Alliance — "Enterprise Reality: Why Organizations Aren't as Prepared for AI Governance as They Think They Are" (https://cloudsecurityalliance.org/blog/2026/09/16/enterprise-reality-why-organizations-aren-t-as-prepared-for-ai-governance-as-they-think-they-are)
[4] Cloud Security Alliance — "Shadow AI Does Not Read Your Org Chart: Rethinking Identity Governance for Autonomous Agents" (https://cloudsecurityalliance.org/blog/2026/09/08/shadow-ai-does-not-read-your-org-chart-rethinking-identity-governance-for-autonomous-agents)

<!-- linkedin -->

I keep coming back to one number this week: 95% of enterprises say they can see their machine identities, but only 36% actually monitor them. SpyCloud's latest report finds non-human identities — the API keys, service accounts, and agents nobody offboards — are now the #1 way attackers get in, nearly 2x phishing. My read: we've been measuring governance by whether a policy exists, and the runtime stopped obeying it a while ago. Then, three weeks later, the control plane went open source: OpenClaw Enterprise, with Red Hat, NVIDIA, and OpenAI. The Linux-and-Kubernetes playbook, applied to agents. I could be wrong, but it looks like the fix for a belief problem is finally being built as infrastructure rather than documents. What I'm watching next: whether a runtime control plane actually closes that 95-to-36 gap, or just gives us a cleaner dashboard over the same unowned identities.
