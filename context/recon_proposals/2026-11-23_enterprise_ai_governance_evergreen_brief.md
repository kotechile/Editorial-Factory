# Evergreen Brief: enterprise_ai_governance — 2026-11-23
**Archetype:** evergreen
**Vertical:** enterprise_ai_governance
**Persona:** enterprise_cai
**Decision the reader is facing:** Which agent decisions keep a human checkpoint, who sits there, and what that person must be able to do — before the deployer-side high-risk obligations the amended AI Act starts applying on 2 December 2027.
**Durability:** The Article 14 and Article 26 texts are enacted law and have not changed since the Act's 12 July 2024 publication; the application dates are as of the AI Omnibus amendment reflected in the timeline pages verified on 2026-11-23 — Annex III high-risk obligations apply from 2 December 2027 (Article 113 as amended), prohibitions 1–8 have run since February 2025, prohibition 9 starts December 2026. The oversight duty itself is not a phase-in, so the design rule stays true for years.
**De-dup:** `2026-11-09_your-index-is-the-boundary` is this vertical's nearest prior evergreen artifact (retrieval ACL boundaries); this differs — it argued where retrieval is fenced, this argues who the law requires inside the loop and what that person must be able to do. Cross-vertical check: `2026-11-04_your-agent-deletes-ask-nobody` (multi_agent_enterprise_fabric) argued tool-approval *defaults* in the stack; this argues the statutory oversight *duty* and its staffing — no mechanism overlap.
**Thesis:** Human oversight is not a review queue bolted onto an agent after launch — Articles 14 and 26 make it a design property with named abilities (see the output, override it, intervene, stop the system in a safe state) held by named people with competence, training and authority, so the deployment that fails is the one where the checkpoint exists in the workflow but the person holding it cannot legally do any of those four things.

**Lead:** Founder-voice §2 for this vertical ("Immutable Cryptographic Audit Provenance" / oversight as deployer duty) and the untouched Article 14/26 pillar; the `enterprise_cai` persona's `wants` list (EU AI Act compliance); customer-truth anecdote 3 (the bank that could not reconstruct its agent's weekend decisions) — oversight is the other half of that audit failure.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | EU AI Act, Article 14: Human Oversight (euaiact.com transcription) | https://www.euaiact.com/article/14 | 2026-11-23 | 14 — the provider must design the high-risk AI system so that it can be effectively overseen by natural persons during the period in which they are in use, and the overseer must be able to intervene in the operation of the system or interrupt it through a 'stop' button or a similar procedure that allows the system to come to a halt in a safe state (Art. 14(4)(e)) | measured |
| 2 | EU AI Act, Article 26: Obligations of Deployers of High-Risk AI Systems (euaiact.com transcription) | https://www.euaiact.com/article/26 | 2026-11-23 | 26 — a deployer shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support (Art. 26(2)) | measured |
| 3 | EU Artificial Intelligence Act — Article 113: Entry into Force and Application | https://artificialintelligenceact.eu/article/113/ | 2026-11-23 | 113 — as amended, the Chapter III requirements for AI systems classified as high-risk under Article 6(2) and Annex III shall apply from 2 December 2027 (with Article 6(1) and its corresponding obligations from 2 August 2027) | measured |
| 4 | European Commission — A European approach to Artificial Intelligence (digital-strategy.ec.europa.eu) | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-11-23 | 2025 — prohibitions 1-8 of the AI Act became effective in February 2025, while prohibition 9 comes into effect in December 2026 under the AI Omnibus amendment, so the Act's dates move by amendment and a compliance plan needs the amended timeline | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Where the human sits: Article 14/26 oversight as a design property with named abilities | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Oversight staffing cost model (what a 24/7 checkpoint costs per agent) | 8 | 6 | 5 | 8 | 6.8 | dropped — the cost anchors are vendor pricing pages, and the load-bearing utilization figure has no measured primary |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:e87f09d0fc" dedup="matched a prior artifact: 2026-11-09_your-index-is-the-bound" window_days=180 checked_at=2026-11-23T18:07:28+00:00 -->
<!-- evergreen-gate:end -->
