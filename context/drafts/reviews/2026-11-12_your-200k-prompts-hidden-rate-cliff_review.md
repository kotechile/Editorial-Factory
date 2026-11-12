# Review report — 2026-11-12_your-200k-prompts-hidden-rate-cliff_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-12_your-200k-prompts-hidden-rate-cliff_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 28 · citations: 3 · quotes: 1 · sources: 3
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A context window is a capability claim, but the pricing line inside it is the real budget decision — crossing it reprices the whole request, so the 95th-percentile prompt length, not the average, sets what a production AI workflow costs.
SHAPE: Lead: states the core mechanism and the number that matters ; Tension: walks the three vendors' price schedules and does the arithmetic once ; Numbers: isolates the three figures the prose should not restate ; Tactical: what the people closest to the story do with the p95 measurement and what the schedules reveal about levers ; Catch: the caveats that survive — dated benchmark, output asymmetry, and the narrow set of workloads that actually hit the cliff.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 932 | 925 |
| sentence length mean | 16.7 | 16.7 |
| sentence length spread (sd) | 6.3 | 6.3 |
| rhythm health (0-1) | 0.672 | 0.671 |
| short sentences (<=8 words) | 9.6% | 9.6% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 2.15 | 2.16 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 58.3 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [6.3, 6.3], "rhythm_health": [0.672, 0.671], "filler": [0.0, 0.0], "words": 925, "flesch": 58.3, "score": [true, 0, -0.01], "critic_fails": 0, "critic_advisories": 0}
```
