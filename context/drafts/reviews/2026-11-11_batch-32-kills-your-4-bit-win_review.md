# Review report — 2026-11-11_batch-32-kills-your-4-bit-win_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-11_batch-32-kills-your-4-bit-win_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 38 · citations: 7 · quotes: 0 · sources: 7
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A quantization recipe's speedup is the share of your step time that is memory-bound, so 4-bit weights pay at batch 1 and fade as batches grow, while FP8 overtakes exactly where the matmul becomes compute-bound.
SHAPE: Lead: state the paradox in one concrete measurement ; At a glance: the shift, the number, the risk ; The big picture: explain why bytes moved, not arithmetic, is the saving ; By the numbers: the ceiling, the footprint, the quality bill ; What I'd watch: the scheduler's role and the missing FP8 measurement ; The catch: the accuracy record cannot settle the choice, and one shipped card is the counterweight.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1039 | 1046 |
| sentence length mean | 20.3 | 20.5 |
| sentence length spread (sd) | 8.0 | 8.1 |
| rhythm health (0-1) | 0.649 | 0.641 |
| short sentences (<=8 words) | 2.2% | 2.2% |
| filler per 1,000 words | 2.89 | 2.87 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 57.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.0, 8.2], "rhythm_health": [0.649, 0.577], "filler": [2.89, 3.1], "words": 968, "flesch": 57.7, "score": [false, -1, -0.79], "critic_fails": 0, "critic_advisories": 2}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [8.0, 8.1], "rhythm_health": [0.649, 0.641], "filler": [2.89, 2.87], "words": 1046, "flesch": 57.5, "score": [true, 0, -0.04], "critic_fails": 0, "critic_advisories": 1}
```
