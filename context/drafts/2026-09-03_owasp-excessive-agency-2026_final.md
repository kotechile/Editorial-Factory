---
title: "OWASP's 2026 LLM Top 10 is the first built on incident data — and the danger moved from the model to the permissions"
vertical: agentic_ai
persona: eng_leader
date: 2026-09-03
slug: owasp-excessive-agency-2026
---

<!-- lead -->
On August 4, OWASP published its 2026 GenAI LLM Top 10. For the first time, the security list rests on hard data rather than pure consensus [1]. The project ingested 7,714 real-world incidents from public vulnerability and AI-harm databases. Researchers isolated the 6,639 events with enough detail to categorize, then weighed the community's traditional vote against the actual incident record [2]. That collision forced one major shift. Excessive Agency jumped to No. 3. The authors call it "the most consequential move on the list, because the vote and the record agree that agentic deployments are where the damage is landing" [3].

<!-- tension -->
For three years, security teams fixated on attackers fooling the model. Prompt injection retains the No. 1 spot, but the 2026 data redraws the actual blast radius. Excessive Agency ranks third because it acts as "the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM" [4]. Its root causes are distinct engineering failures: excessive functionality, excessive permissions, and excessive autonomy [4]. The threat model has shifted. The problem is no longer just a tricked model. The problem is an agent holding a tool it didn't need, an identity that was too powerful, or the freedom to act without human oversight.

The authors mapped exactly how the incident data altered the landscape. Prompt injection keeps the top slot on the strength of the community vote. Yet ranked by raw incident records alone, it "falls out of the top 10 entirely" [5]. The authors call this a "defense effect." Security teams fight injection aggressively, meaning fewer clean exploits survive to reach public databases [5]. Misinformation moved the opposite way. Voters placed it near the bottom, but the incident record pushed it near the top — "the widest gap in the direction that actually hurts" [5]. In these critical areas, the vote and the data "parted ways in specific, useful places" [2].

<!-- tactical-insight -->
None of this is a model problem. Consequently, none of the fixes are model fixes. The 2026 prevention list operates as a strict engineering checklist, applying the principle of least privilege directly to AI agents [4].

- **Strip the tools.** If an agent only needs to read documents, the third-party tool you wire up must not ship modify and delete capabilities. If it only reads email, it cannot send mail. Replace open-ended tools — like executing shell commands or fetching arbitrary URLs — with narrow, schema-validated alternatives [4].
- **Restrict the permissions.** A read-only agent must connect to the database using an identity limited to SELECT. It cannot hold UPDATE, INSERT, or DELETE rights. In delegated or multi-agent workflows, carry the original user's context and scope across chained tool calls instead of defaulting to a highly privileged service account [4].
- **Revoke the autonomy.** Require human-in-the-loop approval for high-impact, irreversible actions. Enforce authorization in the application logic — a pre-execution policy decision point. Never ask the LLM whether an action is allowed. Implement a graduated policy (audit, warn, block, escalate) so recoverable actions auto-approve while irreversible ones route to a human [4].

The OWASP entry details the exact failure mode this checklist prevents. Imagine a personal-assistant agent wired to a user's mailbox to summarize messages. It uses a tool that also happens to send mail. A crafted incoming email triggers an indirect prompt injection. The agent scans the inbox and forwards sensitive mail to an attacker. Three independent architectural choices stop this exploit: a read-only mail tool, an OAuth token restricted to a read-only scope, and a human clicking "send" on every drafted message. Rate-limiting the send interface caps the damage if all three fail [4]. In a graduated setup, a customer-service bot can auto-process a refund as store credit because the action is recoverable, but an external cash payout requires human approval [4].

One boundary matters above all. The 2026 document draws it clearly: the Top 10 list covers the model as a component inside an application. "The moment that model becomes an actor, with tools it can call, memory it carries between sessions, and consequences it sets in motion downstream, the risk moves to the OWASP Agentic Top 10" [2]. If you ship agents, you must read both.

<!-- nuanced-takeaway -->
Keep the evidence in proportion. The new Top 10 remains a consensus product. The community vote carries 75% of the weight, while the incident data carries 25%. As the authors note, "one noisy year of data does not get to overturn the judgment of the people doing the work" [2]. Excessive Agency's rise is not a purely objective measurement. It marks the first time industry belief and empirical evidence point in the exact same direction. The defense effect also cuts both ways. A risk's absence from the incident record often means teams defend against it well, not that the threat vanished [5]. Prompt injection keeps the top slot for this exact reason. The actionable core of the report is not a mandate to fear the No. 3 threat. It is the lead authors' opening instruction: "Stop trying to build a model that cannot be fooled. Build the system around it, so that when the model is fooled, and it will be, nothing important breaks" [2].

<!-- tldr -->
- The 2026 OWASP GenAI LLM Top 10 is the first edition grounded in incident data (7,714 incidents; 6,639 categorized), and it moved Excessive Agency to No. 3 [1][2][3].
- The damage has shifted from fooling the model to over-permissioning the agent: excessive functionality, permissions, and autonomy [4].
- The fix is least-privilege applied to agents — narrow tools, scoped identities, human approval on irreversible actions, and authorization in logic, not in the LLM [4].

## Sources
[1] OWASP, "OWASP Top 10 for Large Language Model Applications" (project page) — https://owasp.org/www-project-top-10-for-large-language-model-applications ("published August 4, 2026").
[2] OWASP GenAI LLM Top 10 2026 — "Letter from the Project Leads" (LLM00_Preface.md) — https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM00_Preface.md
[3] OWASP GenAI LLM Top 10 2026 — "What's New in the 2026 Top 10" (LLM00_Preface.md) — same URL as [2].
[4] OWASP GenAI LLM Top 10 2026 — "LLM03:2026 Excessive Agency" — https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM03_ExcessiveAgency.md
[5] OWASP GenAI LLM Top 10 2026 — Preface, prompt-injection and misinformation analysis — same URL as [2].

<!-- linkedin -->
OWASP's 2026 LLM Top 10 did something it has never done. It checked the community vote against 7,714 real-world incidents.

That data changed the landscape. Excessive Agency jumped to No. 3 — "the most consequential move" — because "agentic deployments are where the damage is landing."

The primary risk is no longer just attackers fooling the model. The danger lies in what you let the agent do: excessive functionality, excessive permissions, and excessive autonomy.

The fix requires strict engineering discipline:
• Strip the tools — read-only means read-only.
• Restrict the permissions — SELECT, nothing else.
• Require human sign-off on anything irreversible.
• Enforce authorization in code, never by asking the LLM.

If your model has tools, memory, and downstream consequences, pair this list with the Agentic Top 10.

Build your application so that when the model gets fooled — and it will — nothing important breaks.

## Gate report
lead: PASS — Direct, data-focused, establishes the OWASP update and the rise of Excessive Agency without filler.
tension: PASS — Contrasts prompt injection vs. agency, explains the "defense effect," and uses varied sentence lengths to maintain momentum.
tactical-insight: PASS — Translates the vulnerability into concrete engineering fixes (least privilege, narrow tools) with a clear example.
nuanced-takeaway: PASS — Contextualizes the 75/25 weighting, explains the defense effect nuance, and ends on a strong architectural philosophy without corporate sign-offs.
tldr: PASS — Exactly three bullet points starting with hyphens, preserving citations and core facts.
