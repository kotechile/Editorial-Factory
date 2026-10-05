# Verified Brief: agentic_ai — 2026-10-05

Synthesis (dual-anchor). Every claim below was read verbatim from the cited primary source on 2026-10-05.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A (EffectMatch) | An approved action can succeed yet leave a persistent effect the application never approved | VERIFIED | https://arxiv.org/abs/2609.31301 | "An approved database update may succeed yet leave an unapproved notification because execution can produce persistent effects beyond the requested change." |
| 2 | A (EffectMatch) | EffectMatch preserved all clean executions and blocked all tested incorrect commits on 206 public business tasks | VERIFIED | https://arxiv.org/abs/2609.31301 | "In comparative evaluation on 206 public business tasks, EffectMatch preserved all clean executions and prevented all tested incorrect commits." |
| 3 | A (EffectMatch) | All 39 task–fault combinations (each run 3×) rejected the mismatch | VERIFIED | https://arxiv.org/abs/2609.31301 | "EffectMatch preserved all clean executions and rejected the mismatches in all 39 task–fault combinations, each repeated three times." |
| 4 | A (EffectMatch) | 80 task-topology cases preserved truthful handoffs and blocked invalid continuation | VERIFIED | https://arxiv.org/abs/2609.31301 | "80 task-topology cases preserved truthful handoffs and blocked invalid continuation" |
| 5 | B (YouRA) | Research-agent manuscripts diverge from executed experiments because state is not persistent/verifiable | VERIFIED | https://arxiv.org/abs/2610.01097 | "manuscript claims often diverge from executed experiments. This gap is structural: research state, failure histories, and claim-evidence alignment are not maintained as persistent, verifiable state across long-horizon pipelines." |
| 6 | B (YouRA) | YouRA beats MLR-Agent and AI Scientist V2 on MLR-Bench's 10-task subset across all three matched backbones | VERIFIED | https://arxiv.org/abs/2610.01097 | "YouRA improves over both MLR-Agent and AI Scientist V2 on scalar Overall across all three matched backbones." |
| 7 | B (YouRA) | Removing either core-state component drops YouRA below the full system | VERIFIED | https://arxiv.org/abs/2610.01097 | "Removing either core-state component drops YouRA below the full system." |
| 8 | B (YouRA) | YouRA's three components: VSA, Independent Controller, Stateful Reflection | VERIFIED | https://arxiv.org/abs/2610.01097 | "a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller … ; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset" |

**Gate result:** 8/8 VERIFIED, 0 FLAGGED, 0 REMOVED. Both legs carry ≥ 2 VERIFIED primary claims (A: 4, B: 4). Dual-anchor gate passes — synthesis is not under-sourced.
