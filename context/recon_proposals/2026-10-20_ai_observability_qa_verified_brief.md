# Verified Brief: ai_observability_qa — 2026-10-20

**Verification method:** both anchors were fetched through the arXiv API with `id_list` (which returns each paper's own `<summary>`, the primary abstract text, with its exact `<published>` stamp); the vendor and benchmark legs were fetched as pages. No claim below rests on a secondary writeup.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A — Claim Laundering | Across four decision models and three domains, the agent's action record outweighs the environment when the two conflict | VERIFIED | https://arxiv.org/abs/2610.25947 | "In all 12 configurations of four decision models and three domains, records have a larger average effect on commitment decisions than observations" |
| 2 | A — Claim Laundering | After a step that claims success but did not take effect, the agent keeps committing in a majority to all of the tested cases | VERIFIED | https://arxiv.org/abs/2610.25947 | "after claimed-but-failed steps, the models still stop, advance, or purchase in 53-100% of cases" |
| 3 | A — Claim Laundering | The failure is represented inside the model even when the decision ignores it | VERIFIED | https://arxiv.org/abs/2610.25947 | "linear probes on intermediate hidden states distinguish successful from failed steps on held-out apps, tasks, and goals (AUROC 0.77-1.00), and activation patching reveals increasing influence from records in later layers" |
| 4 | A — Claim Laundering | A veto at an intermediate layer recovers success at a few percent of serving latency, under injected silent failures | VERIFIED | https://arxiv.org/abs/2610.25947 | "EVIGATE, an intermediate-layer veto that requires no additional forward pass and adds 0.04-2.0% serving latency. Under injected silent failures, EVIGATE improves task success by 18.7 points in live ALFWorld agents, 5.0 in WebShop, and 5.1 in a phone simulator" |
| 5 | A — Claim Laundering | Gates calibrated offline do not transfer to live trajectories | VERIFIED | https://arxiv.org/abs/2610.25947 | "Its effectiveness depends on representative calibration states: gates calibrated on offline counterfactual states do not transfer reliably to live agent trajectories." |
| 6 | B — Harness state | Whether a lost fact can be re-observed changes success far more than whether it can be re-fetched | VERIFIED | https://arxiv.org/abs/2610.26632 | "truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fact cannot be re-observed: the two penalties differ by 92.5 percentage points (90% CI [89.5, 95.5])" |
| 7 | B — Harness state | The contrast replicated on a second provider's model, pre-registered | VERIFIED | https://arxiv.org/abs/2610.26632 | "A pre-registered replication on one model from a second provider showed the same contrast." |
| 8 | B — Harness state | Summarising old turns plus a note-taking invitation recovers most of a harness gap on ARC-AGI-3; the note-taking half alone recovers less, native replay the rest | VERIFIED | https://arxiv.org/abs/2610.26632 | "Summarizing old turns instead of dropping them, while keeping the Standard harness's invitation to take notes, recovers 86% of a 63-point gap without replaying the model's reasoning. The same harness without the invitation recovers 43%, and adding the provider's native replay of the model's reasoning recovers the remaining 57%." |
| 9 | B — Harness state | These harness shares are single-run point estimates | VERIFIED | https://arxiv.org/abs/2610.26632 | "These are point estimates from one counted run per configuration and game, and the replay share depends on a single run." |
| 10 | Corroboration — trace-level success | Successful multi-agent traces routinely contain local execution errors that were absorbed | VERIFIED | https://arxiv.org/abs/2610.25852 | "Across 1,828 traces from nine MAS-benchmark configurations, IFs occur in 54.3% of successful and 75.2% of failed traces." |
| 11 | Corroboration — evidence validity | A stored judgement can outlive the evidence that supported it, under changes that do not alter system behaviour | VERIFIED | https://arxiv.org/abs/2610.21177 | "a recorded judgment does not guarantee that its supporting evidence remains valid" and "Controlled interventions on 48 evidence views expose 36 binding faults missed by hash-only checks without changing agent behavior." |
| 12 | Friction — what the market prices | A vendor claims frontier-level trace error detection at a small fraction of the cost, on its own benchmark of 523 traces | VERIFIED (vendor's own benchmark, labelled) | https://laminar.sh/blog/flow-1 | "On our benchmark, it matches GPT-6-sol in detection quality while being 23x cheaper." Table: flow-1 "Detection F1 .835" against "GPT-6-sol (high) .816"; "888" traces per $1 for flow-1 against "38" for GPT-6-sol; "our benchmark of 523 difficult agent traces" |
| 13 | Friction — deterministic graders | On a guardrail benchmark, typed decision models land mid-table against both classifiers and LLM judges | VERIFIED | https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails | Table 1, prompt injection: "Jev — Jev-style — 86.35% — 4th — 348.1" median latency; "Qwen3.6-35B — LLM-as-a-judge — 89.31% — 1st — 312.5"; "deberta-v3-base-prompt-injection-v2 — Pre-trained classifier — 89.01% — 2nd — 54.1" |

**Gate rulings for the drafter (each is a hard constraint):**
1. **Write 92.5 as percentage points of success, never as a percentage.** The vertical's own 2026-10-13 evergreen (`100-case-eval-925-coverage`) already carries "92.5%" as a coverage figure; a second 92.5% in the same vertical would read as the same statistic.
2. **Never state an absolute success rate for the harness probe.** The paper reports a *difference* of 92.5 percentage points between two penalties, not two measured rates. No "success fell from X% to Y%" — that arithmetic does not exist in the source.
3. **The ARC-AGI-3 shares carry the one-run caveat in the same sentence or the next one.** 86%, 43% and 57% are shares of a 63-point gap from "one counted run per configuration and game".
4. **EVIGATE's gains are task-success points under injected silent failures**, in three named environments (ALFWorld, WebShop, a phone simulator). Not production, not "18.7% more reliable".
5. **MASIF's 54.3% is traces from nine benchmark configurations**, not production traces; say so.
6. **AgentEval's 36 faults come from controlled interventions on 48 evidence views**, not from production incidents.
7. **Laminar is a vendor's own benchmark on 523 traces.** Label it as the vendor's benchmark. Do not claim it beats Claude Opus 5, whose .890 sits above flow-1's .835 in the same table.
8. **Red Hat's latencies include network round-trips** (US servers, test machine in the UK), and its authors say the zero-shot policies may not be optimal for decision models. Carry both caveats if latency is quoted.
9. **Do not claim agents are trained on their logs, or that the record is deliberately falsified.** The mechanism is a silent failure plus a record that reports success — not deception.

**Supporting primary URLs (for `## Sources`; all present in the signals file):**
- https://arxiv.org/abs/2610.25947 — anchor 1
- https://arxiv.org/abs/2610.26632 — anchor 2
- https://arxiv.org/abs/2610.25852 — implicit-failure rate
- https://arxiv.org/abs/2610.21177 — evidence-validity figures
- https://laminar.sh/blog/flow-1 — vendor trace-reader benchmark
- https://developers.redhat.com/articles/2026/10/02/benchmarking-ai-decision-models-against-traditional-guardrails — decision-model vs judge benchmark

**Gate result:** 13 claims checked, **13 VERIFIED**, 0 FLAGGED, 0 REMOVED. Dual-anchor gate **PASS** — anchor A carries 5 VERIFIED claims, anchor B carries 4.
