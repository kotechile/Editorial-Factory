# Signals: enterprise_ai_governance — 2026-11-23
**Window:** 2026-10-24 → 2026-11-23
**Queries run:** 7 (web search ×3 angles, HN Algolia ×3, report-date probes ×3)
**Persona:** enterprise_cai (Chief AI/Information-Security Officer buying control planes)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Linux Foundation launches Agent Name Service (ANS) | https://www.linuxfoundation.org/press/linux-foundation-welcomes-agent-name-service-to-bring-verifiable-identity-and-discovery-to-ai-agents | 2026-11-10 | ANS launched as an LF project at KubeCon NA: open standard giving AI agents verifiable identity over existing DNS, 7-document spec (naming, registration/versioning, DNS publication, public log auditing, integrity monitoring, agent-to-agent authentication); 11 orgs contributed or adopted (Cisco, Cloudflare, DigiCert, GoDaddy, Infoblox, Salesforce, OWASP…); AGNTCY Agent Directory Service verifies ANS identities | non-human identity NHI lifecycle management | 88 |
| 2 | Salt Security ships Autonomous Defense for its Agentic Security Platform | https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense | 2026-10-28 | First-party launch post: instead of an alert or a ticket, workflows can revoke agent/MCP tool access, push blocking rules to WAFs and API gateways, update guardrail policies, and close posture gaps. Restates its own 2H 2026 survey (383 practitioners): 49.8% had a confirmed/suspected agent action nobody authorized in 12 months; only 17.5% can automatically stop an agent misbehaving in production | agent blast-radius fencing and kill-switches | 90 |
| 3 | OWASP publishes Securing Agentic Applications V2 | https://genai.owasp.org/resource/securing-agentic-applications-v2/ | 2026-11-10 | Builder & defender's guide v2 released on the resource page dated November 10, 2026: secure architectures, threat mitigation, identity and access controls, runtime protection, supply chain security, assurance testing across single- and multi-agent environments | zero-trust agent security boundaries | 78 |
| 4 | Coral — open-source execution rails where agents write their own tools | https://github.com/withcoral/coral | 2026-11-16 | Released as a public repository under the paper's own name (Show HN, 52 points, Nov 16): "execution rails for agents" — precise permissions per agent plus custom tools the agent authors itself, pitched for sensitive enterprise systems; 5.0k stars / 224 forks; Apache-2.0; TypeScript-program interface replacing the 0.x SQL interface | agent blast-radius fencing and kill-switches | 82 |
| 5 | Zalando open-sources an Agentic Identity Broker (OAuth delegation) | https://github.com/zalando-incubator/agentic-identity-broker | 2026-11-06 | Show HN Nov 6: OAuth delegation for AI agents — agents exchange delegated authorization instead of holding long-lived secrets, addressing the credential-sprawl half of NHI management | non-human identity NHI lifecycle management | 72 |
| 6 | OWASP GenAI Data Security Best Practices v2 — Part 2 | https://genai.owasp.org/resource/genai-data-security-best-practices-v2-part2/ | 2026-11-17 | Resource page dated November 17, 2026: second part of the v2 data-security practices for generative AI — data protection controls for AI pipelines (the leakage leg of agent governance) | cross-domain context poisoning and data leakage | 70 |

**Dating note:** Rows 1–6 are event-dated from the publisher's own page (LF press release dateline 2026-11-10; Salt blog dateline October 28, 2026; OWASP resource pages carry their own dated listings; GitHub rows dated from their HN Show postings). No observation-dated rows.

**Queries run detail:** "<angle>" last-30-days variants ×4; HN Algolia created_at_i>1761273600 for "agent governance", "AI agent identity", "machine identity AI agent"; publisher date probes on salt.security press release (2026-10-13) and OWASP resource listings.

## Dated background
- Salt Security, State of Agentic AI and API Security 2H 2026 (survey of 380+ practitioners + Salt Labs telemetry; 49.8% unauthorized-action incidence, 12.5% full-path traceability, 17.5% auto-containment, 86.4% ≥1 agent, 59.5% >10 agents, 76.8% chained action sequences, 54.3% confirmed/suspected shadow MCP server, 32.9% found one): https://salt.security/press-releases/state-of-agentic-ai-and-api-security-2h-2026 (published 2026-10-13 — 11 days before the window; admissible as corroboration via Salt's in-window 2026-10-28 post, never as a standalone in-window anchor)
- Salt Labs Manus hijack write-up (guardrail detected but could not stop the code from running): https://salt.security/blog/when-a-security-guardrail-detects-the-attack-and-still-cant-stop-it (October 2026 research, restated in the in-window 2026-10-28 post)
- HN discussion of Coral (Show HN, 52 points): https://news.ycombinator.com/item?id=46260787 (2026-11-16)
- CSA/industry NHI governance context (8% of NHIs lack HR ownership linkage after creator departure; unapproved AI tools used by 45% of workforce per 2026 DBIR — used as background framing only): https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=1 heuristic=0.77-0.77 window=2026-10-24..2026-11-23 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #2 ⨂ #6 | governance_x_runtime | A: agent blast-radius fencing and kill-switches | B: cross-domain context poisoning and data leakage | https://salt.security/blog/an-alert-doesnt-stop-an-attack-introducing-autonomous-defense https://genai.owasp.org/resource/genai-data-security-best-practices-v2-part2/ | 0.77 | prior_cycle_token_overlap:security |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.8 angle_fit=1.0 contrast=1.0 → 0.77 (governance_x_runtime)
<!-- synthesis-seed:end -->

