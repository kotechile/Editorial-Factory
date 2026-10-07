# Verified Brief: agentic_resilience_failure — 2026-10-07 (EVERGREEN track)

Archetype: evergreen. Topic = governing the agent **memory write path** rather than the prompt: a
memory poisoning attack lands untrusted content in the store, the agent reads it back later as
trusted context, and a guardrail sitting at the model never sees it. Every external claim below
traces to a source the evergreen gate fetched live and confirmed contains the cited figure
(4/4 gate rows verified on 3 hosts, `<!-- evergreen-gate: -->` marker in
`context/recon_proposals/2026-10-07_agentic_resilience_failure_evergreen_brief.md`). Row 5 is a
context citation verified by hand against the fetched page (not a gate row).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Attack rate (memory store) | The GhostWriter attack reaches **98%** injection and about **60%** activation against state-of-the-art memory agents | VERIFIED | https://arxiv.org/abs/2607.06595 | "GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents." |
| 2 | Root cause | The attack succeeds "due to the lack of security-focused memory governance" | VERIFIED | https://arxiv.org/abs/2607.06595 | "This attack is possible due to the lack of security-focused memory governance." |
| 3 | Mitigation shape | The paper's defense, Agentic Memory Sentry (AM-Sentry), uses two controls — a memory-saving policy and a memory-retrieval screen — and cuts the attack while keeping the agent useful | VERIFIED | https://arxiv.org/abs/2607.06595 | "we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility." |
| 4 | Query-only injection rate | A second attack, MINJA, reaches over **95%** injection success and **70%** attack success, and needs no elevated privileges | VERIFIED | https://arxiv.org/html/2601.05504v2 | "the MINJA (Memory Injection Attack) achieves over 95 % injection success rate and 70 % attack success rate under idealized conditions." / "a practical attack that demonstrates how regular users with no elevated privileges can poison an agent's long-term memory through query-only interactions." |
| 5 | Memory read path | A real coding agent loaded the **first 200 lines** of its memory files straight into the system prompt, so a poisoned write becomes a trusted instruction | VERIFIED | https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code | "In the version of Claude Code we evaluated, we found that first 200 lines of these files are loaded directly into the AI's system prompt (the system prompt includes the foundational instructions that shape how the model thinks and responds.)" |
| 6 | Persistence | The payload persisted "across all projects, sessions, and reboots", and the vendor shipped a fix (v2.1.50) that removes user memories from the system prompt | VERIFIED | https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code | "Its output is injected directly into Claude's context and persists across all projects, sessions, and reboots." / "as of Claude Code v2.1.50, Anthropic has included a mitigation that removes user memories from the system prompt." |
| 7 | Live campaign scale | Microsoft found **over 50** unique memory-poisoning prompts from **31** companies across **14** industries, mapped to a formal threat-catalogue entry (MITRE ATLAS AML.T0080, "Memory Poisoning") | VERIFIED | https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning | "We identified over 50 unique prompts from 31 companies across 14 industries, with freely available tooling making this technique trivially easy to deploy." / "This technique is formally recognized by the MITRE ATLAS knowledge base as 'AML.T0080: Memory Poisoning.'" |
| 8 | Standard (context, not a gate row) | OWASP added Memory & Context Poisoning as ASI06 in its Top 10 for Agentic Applications, published 2025-12-09 | VERIFIED (context) | https://genai.owasp.org/2026/05/13/memory-is-a-feature-it-is-also-an-attack-surface | "As co-lead of OWASP ASI06: Memory & Context Poisoning entry as part of OWASP Top 10 for Agentic Applications, I have spent a lot of time thinking about a simple question: what happens when an AI agent does not just process untrusted input, but carries it forward?" |

## Gate rules applied
- 7/7 gate-relevant external claims VERIFIED against the fetched primary page (rows 1–7); 0 REMOVED,
  0 FLAGGED. Row 8 is a named-standard context citation (the OWASP ASI06 entry), verified by hand.
- Hosts among the gate rows: arxiv.org (rows 1–4, two distinct papers), blogs.cisco.com (rows 5–6,
  one page cited for two figures), microsoft.com (row 7).
- No synthesis: single-signal evergreen topic; the dual-anchor gate does not apply.
- Boundary wording for drafting: the two attack rates are **measured** in a lab (as of the 2026
  papers cited); the Cisco and Microsoft figures are **disclosed research / a live-campaign count**
  (as of April 2026 and February 2026 respectively). Date every figure in-text and never present the
  lab rates as a production base rate.
- Durability guard: name no product version as the load-bearing fact. The mechanism (a memory write
  the agent later reads back as trusted context) is the durable point; the Claude Code version is
  evidence, not the thesis.
- Acronyms the body must expand at first use: MINJA, OWASP. Never invent an expansion; "AM-Sentry"
  is written as "Agentic Memory Sentry", and MITRE ATLAS is described rather than posted bare.

De-dup: nearest prior artifact for this vertical is `retry-is-the-failure-amplifier` (2026-10-07) —
the retry/recovery primitive. This piece is the persistence primitive (memory write), and the
2026-09-23 rollback brief is the checkpoint primitive. Three different failure classes.
