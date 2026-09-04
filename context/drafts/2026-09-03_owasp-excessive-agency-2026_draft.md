---
title: "OWASP's 2026 LLM Top 10 is the first built on incident data — and the danger moved from the model to the permissions"
vertical: agentic_ai
persona: eng_leader
date: 2026-09-03
slug: owasp-excessive-agency-2026
---

<!-- lead -->
On August 4, OWASP published its 2026 GenAI LLM Top 10, and for the first time the list wasn't built on opinion [1]. The project pulled 7,714 real-world incidents from public vulnerability databases and an AI-harm database, sorted the 6,639 with enough detail to categorize, and checked the community's vote against the record [2]. One entry moved because of it: Excessive Agency climbed to No. 3 — "the most consequential move on the list," the authors write, "because the vote and the record agree that agentic deployments are where the damage is landing" [3].

<!-- tension -->
For three years the headline risk has been the model being fooled. Prompt injection still holds No. 1, and it isn't going anywhere. But the 2026 data redraws where the damage actually lands. Excessive Agency is "the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM" [4]. Its root causes are three specific, engineering-shaped failures: excessive functionality, excessive permissions, and excessive autonomy [4]. The shift is from "someone tricked the model" to "someone handed the agent a tool it didn't need, an identity that was too powerful, or the freedom to act with no human in the loop."

The list's authors are explicit about what the data changed. Prompt injection keeps the top slot on the strength of the vote — but ranked by raw incident record alone, it "falls out of the top 10 entirely," a gap the authors call a "defense effect": teams fight injection hard, so fewer clean exploits reach a public database [5]. Misinformation runs the other direction. Voters put it near the bottom; the incident record puts it near the top — "the widest gap in the direction that actually hurts" [5]. The vote and the data "parted ways in specific, useful places" [2].

<!-- tactical-insight -->
None of this is a model problem, so none of the fixes are model fixes. The 2026 entry's prevention list is a Monday-morning checklist, and every item is least-privilege applied to agents [4].

- **Cut the tools.** If the agent only needs to read documents, the third-party tool you wire up must not also ship modify and delete. If it only reads email, it must not send mail. Replace open-ended tools — "run a shell command," "fetch a URL" — with narrow, schema-validated alternatives [4].
- **Cut the permissions.** A read-only agent connects to the database with an identity that has SELECT and nothing else — not UPDATE, INSERT, or DELETE. In delegated or multi-agent workflows, carry the original user's context and scope across chained tool calls instead of falling back to a privileged service identity [4].
- **Cut the autonomy.** Put human-in-the-loop approval on high-impact, irreversible actions. Enforce authorization in logic — a pre-execution policy decision point — never by asking the LLM whether an action is allowed. A graduated policy (audit, warn, block, escalate) lets recoverable actions auto-approve while irreversible ones route to a human [4].

The entry walks through the concrete failure this closes. A personal-assistant agent wired to a user's mailbox to summarize mail, using a tool that also happens to send messages. A crafted incoming email (indirect prompt injection) tricks the agent into scanning the inbox and forwarding sensitive mail to an attacker. Three independent fixes stop it: a mail-reading-only tool, OAuth with a read-only scope, and a human hitting send on every drafted message — with rate-limiting on the send interface to cap the damage if all three fail [4]. The graduated version: a customer-service bot auto-processes a refund as store credit (recoverable), while an irreversible external payout routes to human approval [4].

One boundary matters. The 2026 document draws it in plain terms: this list covers the model as a component inside your application. "The moment that model becomes an actor, with tools it can call, memory it carries between sessions, and consequences it sets in motion downstream, the risk moves to the OWASP Agentic Top 10" [2]. If you're shipping agents, you're reading both.

<!-- nuanced-takeaway -->
Keep the weight of the evidence in proportion. This list is a consensus product: the community vote carries 75%, incident data 25% — "one noisy year of data does not get to overturn the judgment of the people doing the work" [2]. Excessive Agency's rise isn't a clean, objective measurement; it's the first time belief and evidence point the same direction. And the defense effect cuts both ways: a risk's absence from the incident record can mean it's well-defended, not that it's gone — which is exactly why prompt injection keeps the top slot despite falling out of the raw record [5]. The actionable core isn't "fear No. 3." It's the lead authors' opening instruction: "Stop trying to build a model that cannot be fooled. Build the system around it, so that when the model is fooled, and it will be, nothing important breaks" [2].

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
OWASP's 2026 LLM Top 10 did something it's never done: it checked the vote against 7,714 real incidents.

One number changed the list. Excessive Agency jumped to No. 3 — "the most consequential move" — because "agentic deployments are where the damage is landing."

The risk is no longer just fooling the model. It's what you let the agent do: excessive functionality, excessive permissions, excessive autonomy.

The fix is unglamorous:
• Cut the tools — read-only means read-only.
• Cut the permissions — SELECT, nothing else.
• Human sign-off on anything irreversible.
• Enforce authorization in code, never by asking the LLM.

If your model has tools, memory, and downstream consequences, pair this list with the Agentic Top 10.

Build so that when the model gets fooled — and it will — nothing important breaks.
