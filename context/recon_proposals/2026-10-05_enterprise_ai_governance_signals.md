# Signals: enterprise_ai_governance — 2026-10-05

**Window:** 2026-09-05 → 2026-10-05
**Queries run:** 12

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Non-human identities (NHIs) become the #1 route into the enterprise | https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities | 2026-09-09 | Compromised NHIs (31%) nearly 2x phishing (17%) as primary entry point; NHI misuse top identity event type (42%); 95% claim visibility vs 36% actually monitor; 91% use AI with internal access vs 56% formal governance | non-human identity lifecycle & governance gap | 90 |
| 2 | OpenClaw Enterprise: an open-source, vendor-neutral agent control plane | https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise | 2026-09-29 | MIT-licensed control plane for persistent agents; multi-tenancy, hard security boundaries, governance + auditability across the agent lifecycle; "Kubernetes for agents"; OpenAI + Red Hat + NVIDIA | shadow AI migration to managed agent gateway / runtime governance | 82 |
| 3 | Regulation arrives faster than enterprise governance readiness | https://cloudsecurityalliance.org/blog/2026/09/16/enterprise-reality-why-organizations-aren-t-as-prepared-for-ai-governance-as-they-think-they-are | 2026-09-16 | 94% operate where AI regulations already apply; only 29% prepared for the EU AI Act and 12% for APAC; 74% say they'd pass an AI compliance audit but only 27% call their program mature | EU AI Act & regulatory compliance replay | 80 |
| 4 | RBAC stops working once agents act autonomously after login | https://cloudsecurityalliance.org/blog/2026/09/08/shadow-ai-does-not-read-your-org-chart-rethinking-identity-governance-for-autonomous-agents | 2026-09-08 | 90% claim visibility into their AI footprint vs 59% admit shadow AI operates outside governance; RBAC governs at login, agents decide continuously afterward; SPIFFE/SPIRE + OAuth 2.0 token exchange + CAEP | attribute-based access control & runtime authorization for agents | 74 |

## Candidate Synthesis Pairs



<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=4 heuristic=0.75-0.95 window=2026-09-05..2026-10-05 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #2 ⨂ #3 | governance_x_runtime | A: shadow AI migration to managed agent gateway / runtime governance | B: EU AI Act & regulatory compliance replay | https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise https://cloudsecurityalliance.org/blog/2026/09/16/enterprise-reality-why-organizations-aren-t-as-prepared-for-ai-governance-as-they-think-they-are | 0.95 | prior_cycle_token_overlap:enterprise |
| 2 | #1 ⨂ #4 | governance_x_runtime | A: non-human identity lifecycle & governance gap | B: attribute-based access control & runtime authorization for agents | https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities https://cloudsecurityalliance.org/blog/2026/09/08/shadow-ai-does-not-read-your-org-chart-rethinking-identity-governance-for-autonomous-agents | 0.78 | - |
| 3 | #1 ⨂ #2 | governance_x_runtime | A: non-human identity lifecycle & governance gap | B: shadow AI migration to managed agent gateway / runtime governance | https://spycloud.com/newsroom/spycloud-2026-identity-threat-report-finds-non-human-identities https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise | 0.77 | prior_cycle_token_overlap:enterprise |
| 4 | #2 ⨂ #4 | governance_x_runtime | A: shadow AI migration to managed agent gateway / runtime governance | B: attribute-based access control & runtime authorization for agents | https://www.redhat.com/en/blog/why-red-hat-building-open-foundation-enterprise-agents-openclaw-enterprise https://cloudsecurityalliance.org/blog/2026/09/08/shadow-ai-does-not-read-your-org-chart-rethinking-identity-governance-for-autonomous-agents | 0.75 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=1.0 intensity=0.81 angle_fit=1.0 contrast=1.0 → 0.95 (governance_x_runtime)
- #2: token_coverage=0.5 intensity=0.82 angle_fit=1.0 contrast=1.0 → 0.78 (governance_x_runtime)
- #3: token_coverage=0.5 intensity=0.86 angle_fit=1.0 contrast=0.9 → 0.77 (governance_x_runtime)
- #4: token_coverage=0.5 intensity=0.78 angle_fit=1.0 contrast=0.92 → 0.75 (governance_x_runtime)
<!-- synthesis-seed:end -->

