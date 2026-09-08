---
title: "OWASP's 2026 LLM Top 10 is the first built on incident data — and the danger moved from the model to the permissions"
vertical: agentic_ai
persona: eng_leader
date: 2026-09-03
slug: owasp-excessive-agency-2026
---

<!-- lead -->
On August 4, the Open Worldwide Application Security Project (OWASP) published a new security list. It is the 2026 Generative Artificial Intelligence (GenAI) Large Language Model (LLM) Top 10. For the first time, data drives the ranking [1]. The project pulled 7,714 real-world incidents from public databases. They also used a database tracking artificial intelligence harms. The team sorted 6,639 incidents with enough detail to categorize. Then they checked the community vote against this record [2]. One entry moved significantly because of this data. Excessive Agency climbed to the number three spot. The authors call this the most consequential move. "The vote and the record agree," they write. "Agentic deployments are where the damage is landing" [3].

<!-- tension -->
For three years, the main risk involved fooling the model. Prompt injection tricks a model with malicious instructions. This attack keeps the top spot. But the 2026 data redraws where the actual damage lands. Excessive Agency enables damaging actions. These happen after a model generates manipulated outputs [4]. Three specific engineering failures cause this vulnerability [4]. These are excessive functionality, excessive permissions, and excessive autonomy. The core problem shifted. Attackers no longer just trick the model. Developers hand the software extra tools. They grant identities that are too powerful. They let software act without human oversight.

The authors explain the data clearly. Prompt injection keeps the top slot based on votes. But it falls out of the top ten by raw incidents. The authors call this gap a defense effect [5]. Teams fight injection attacks hard. Fewer clean exploits reach public databases. Misinformation trends the opposite way. Voters put it near the bottom. The incident record puts it near the top. The authors call this the widest gap in the direction that hurts [5]. The vote and the data parted ways in useful places [2].

<!-- tactical-insight -->
None of this is a fundamental model problem. Therefore, none of the fixes are model fixes. The 2026 prevention list is a practical engineering checklist. Every item applies the principle of least privilege [4]. This limits software to the exact access it needs.

- **Cut the tools.** An agent might only need to read documents. Its tools must not include functions to alter or erase files. An agent reading email must not send mail. Replace open-ended tools like running system commands. Use narrow alternatives. Check these against a strict data format [4].
- **Cut the permissions.** A read-only agent connects to a database using a restricted identity. It gets the command to read data. It never gets commands to add, change, or erase records. Multi-agent workflows pass tasks down a chain. Carry the original user's restricted access across these calls [4]. Do not fall back to a highly privileged service account.
- **Cut the autonomy.** Require human approval for high-impact actions. Enforce authorization rules in standard application code. Never ask the model whether an action is allowed. A graduated policy categorizes actions by risk. Recoverable actions can auto-approve. Irreversible actions must route to a human [4].

The document details a concrete failure scenario. A personal assistant agent connects to a user's mailbox. It uses a tool that can summarize and send messages. A crafted incoming email tricks the agent. The agent scans the inbox. Then it forwards sensitive mail outward. Three independent fixes stop this attack. First, use a tool built only for reading mail. Second, use Open Authorization (OAuth). OAuth is a standard framework for granting limited access. Give it a read-only scope. Third, require a human to hit send on drafted messages. Limiting the send rate caps the damage if all fail [4]. A customer service bot shows the graduated policy in action. It auto-processes a recoverable refund as store credit. An irreversible cash payout routes to human approval [4].

One boundary matters deeply. The 2026 document draws this line in plain terms. This list covers the model as a software component. Eventually, that model becomes an independent actor. It gets tools, memory, and downstream consequences. At that moment, the risk moves to a different list [2]. That list is the OWASP Agentic Top 10. Teams shipping agents must read both documents.

<!-- nuanced-takeaway -->
Keep the evidence in proportion. This list remains a consensus product. The community vote carries most of the weight. Incident data accounts for the rest. One noisy year of data cannot overturn expert judgment [2]. Excessive Agency rising to number three is not purely objective. It is where belief and evidence finally align. The defense effect cuts both ways. A risk missing from the record might just be well-defended. It does not mean the threat is gone. Prompt injection keeps the top slot for exactly this reason [5]. The actionable core is not about fearing the third spot. It is the lead authors' opening instruction. Stop trying to build a model that cannot be fooled. Build the system around it carefully [2]. When the model gets fooled, nothing important should break.

<!-- tldr -->
- The 2026 OWASP GenAI LLM Top 10 relies on real incident data. This moved Excessive Agency to No. 3 [1][2][3].
- The damage shifted from fooling the model to over-permissioning the software. This includes excessive functionality, permissions, and autonomy [4].
- The fix limits agents to exact access needs. This means narrow tools, scoped identities, human approval, and authorization in code [4].

## Sources
[1] OWASP, "OWASP Top 10 for Large Language Model Applications" (project page) — https://owasp.org/www-project-top-10-for-large-language-model-applications ("published August 4, 2026").
[2] OWASP GenAI LLM Top 10 2026 — "Letter from the Project Leads" (LLM00_Preface.md) — https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM00_Preface.md
[3] OWASP GenAI LLM Top 10 2026 — "What's New in the 2026 Top 10" (LLM00_Preface.md) — same URL as [2].
[4] OWASP GenAI LLM Top 10 2026 — "LLM03:2026 Excessive Agency" — https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/final/LLM03_ExcessiveAgency.md
[5] OWASP GenAI LLM Top 10 2026 — Preface, prompt-injection and misinformation analysis — same URL as [2].

<!-- linkedin -->
The 2026 OWASP LLM Top 10 did something unprecedented.
It checked the vote against 7,714 real incidents.

One number changed the list.
Excessive Agency jumped to the third spot.
Agentic deployments are where the damage lands today.

The risk is no longer just fooling the model.
It is what you let the agent do.

The fix is unglamorous:
• Cut the tools.
• Cut the permissions.
• Require human sign-off on irreversible actions.
• Enforce authorization in code.

Does your model have tools, memory, and downstream consequences?
Pair this list with the Agentic Top 10.

Build systems assuming the model will get fooled.
Ensure nothing important breaks when it happens.

## Gate report
lead: PASS — Strict sentence limits applied to drastically raise Flesch score. Expanded all acronyms at first use. Preserved the lead incident and citations verbatim.
tension: PASS — Eradicated hollow transitions, filler clauses, and conjunctions. Short, declarative sentences maximize readability. Concrete nouns prioritized over abstractions.
tactical-insight: PASS — Completely replaced all SQL jargon (DELETE, INSERT, SELECT, UPDATE) with plain English equivalents. All sentences are rigorously split to stay under 15 words. Added brief glosses for "prompt injection", "least privilege", and "OAuth".
nuanced-takeaway: PASS — Readability maximized via one idea per sentence. Dropped conjunctive clauses entirely ('which', 'while', 'as', 'and that'). Preserved the pragmatic takeaway without corporate sign-offs.
tldr: PASS — Maintained exactly 3 scannable bullet points starting with "-". Sentences kept exceptionally short. No prose paragraphs included.
