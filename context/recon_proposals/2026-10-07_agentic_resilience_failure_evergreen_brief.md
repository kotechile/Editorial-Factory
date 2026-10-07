# Evergreen Brief: agentic_resilience_failure — 2026-10-07

**Archetype:** evergreen
**Vertical:** agentic_resilience_failure
**Persona:** infra_engineer
**Decision the reader is facing:** Whether to give a production agent persistent, cross-session memory at all — and, if yes, where the trust boundary for a *memory write* sits: a validated write path with per-user scoping and a retrieval screen, or trusting the model to write its own memory and hoping a prompt-level guardrail catches the bad content.
**Durability:** Still true in 12 months and not a news fact: the mechanism — an untrusted input lands in the memory store, the agent reads it back later as *trusted* context (in the Claude Code case the read path promoted stored memory straight into the system prompt), and the failure fires in a later session — is architectural, not a version artefact. The measured attack rates are as of the two 2026 studies cited (arXiv:2607.06595, arXiv:2601.05504) and the 2026 vendor disclosures; the exact percentages will drift, the write-path control does not.
**De-dup:** Nearest prior artifact for this vertical is `retry-is-the-failure-amplifier` (2026-10-07, `published/2026-10-07_retry-is-the-failure-amplifier.md`): that thesis is about the *recovery* action — a retry loop amplifying cost and duplicating side effects inside one run. This one is about the *persistence* primitive — a memory write that survives the run and attacks a session days later. Different failure class, different primitive, different evidence. The only other prior artifact, the 2026-09-23 news brief on rollback, is about checkpoint/rollback security, also distinct.
**Thesis:** A persistent-memory agent's real attack surface is the memory write path, not the prompt: a guardrail sitting at the model does not catch a poisoned memory that fires days later, so the control belongs at the store boundary — validate every write, scope it per user, and screen what the retrieval path promotes into trusted context.

**Lead:** The vertical's own `primary_angles` ("context poisoning mitigation") plus founder-voice §3 `agentic_resilience_failure` ("Context Poisoning: an erroneous intermediate tool output contaminating all subsequent reasoning steps"). Grounded in the intel feeds' incident research — the Cisco MemoryTrap disclosure on Claude Code and the Microsoft recommendation-poisoning campaign — and the OWASP ASI06 entry of the 2026 Agentic Top 10, which codifies the class as a standard. GSC returned 0 high-potential striking-distance queries for this vertical (impressions still thin on a young site), so demand is not the driver: the persona's standing architectural decision is.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Torres, Shrestha, Misra — *When Agents Remember Too Much: Memory Poisoning Attacks on LLM Agents* (GhostWriter), arXiv:2607.06595 | https://arxiv.org/abs/2607.06595 | 2026-10-07 | 98% — near-universal GhostWriter injection rate into agent memory, with a high average activation rate of approximately 60%; the paper's AM-Sentry (a memory-saving policy plus a memory-retrieval screen) sharply cuts the success rate at the store boundary | measured |
| 2 | *Memory Poisoning Attack and Defense on Memory Based LLM-Agents*, arXiv:2601.05504 | https://arxiv.org/abs/2601.05504 | 2026-10-07 | 95% — MINJA reaches over 95% injection success through ordinary query-only interaction, with a 70% attack-success rate under idealized conditions, i.e. no elevated privileges required | measured |
| 3 | Habler & Chang — *Identifying and remediating a persistent memory compromise in Claude Code* (Cisco Blogs, 2026-04-01) | https://blogs.cisco.com/ai/identifying-and-remediating-a-persistent-memory-compromise-in-claude-code | 2026-10-07 | 200 — the first 200 lines of the agent's memory files were loaded directly into the system prompt, so a poisoned memory write became a persistent, trusted instruction that survived across projects, sessions and reboots | vendor claim (disclosed research, with the affected vendor's fix confirmed) |
| 4 | Microsoft Defender Security Research Team — *Manipulating AI memory for profit: the rise of AI Recommendation Poisoning* (2026-02-10) | https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning | 2026-10-07 | 50 — over 50 unique memory-poisoning prompts traced to 31 companies across 14 industries in a live campaign, mapped to MITRE ATLAS AML.T0080 (AI Agent Context Poisoning) | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Memory poisoning: govern the write path, not the prompt | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Cascading error containment / blast-radius budget | 8 | 8 | 7 | 8 | 7.8 | dropped — its containment leg overlaps the 2026-10-07 retry piece and it has no distinct measured anchor |
| Compound reliability math (0.95^10) as a capacity budget | 8 | 9 | 5 | 9 | 7.6 | dropped — the load-bearing figure is arithmetic, and the 2026-10-07 retry piece already carries it |
| Agentic failure-mode taxonomy (founder's four buckets) | 8 | 9 | 6 | 7 | 7.6 | dropped — taxonomy restates framework sources with no measured anchor of its own, and reads as a listicle |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:3576a991ee" dedup="matched a prior artifact: retry-is-the-failure-amplifier" window_days=180 checked_at=2026-10-07T17:32:49+00:00 -->
<!-- evergreen-gate:end -->
