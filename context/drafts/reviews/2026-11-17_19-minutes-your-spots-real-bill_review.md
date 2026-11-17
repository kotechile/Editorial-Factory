# Review report — 2026-11-17_19-minutes-your-spots-real-bill_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-17_19-minutes-your-spots-real-bill_draft.md` · attempt kept: 3 of 3
- figures in the ledger: 13 · citations: 5 · quotes: 0 · sources: 5
- reader-side critic: 0 holding defect(s), 4 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The spot discount is not the economics; the checkpoint interval is, because a 30-second reclaim notice forces a save cadence that the discount must pay for in lost compute.
SHAPE: Lead: state the thesis as a concrete bill arriving 19 minutes into the run ; At a glance: fix the three numbers the reader needs before the argument ; The big picture: establish the formula and the two measured failure rates that feed it ; By the numbers: the arithmetic that turns failure rate and write time into the interval ; What I'd watch: the operational stance the vendors and Meta assume, and the write-time threshold that breaks it ; The catch: where the formula bends, and what the reader must measure for themselves.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 874 | 872 |
| sentence length mean | 18.1 | 17.0 |
| sentence length spread (sd) | 9.7 | 8.1 |
| rhythm health (0-1) | 0.876 | 0.925 |
| short sentences (<=8 words) | 11.6% | 15.2% |
| filler per 1,000 words | 1.14 | 1.15 |
| hedge per 1,000 words | 0.0 | 1.15 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 58.8 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 9.7 -> 8.1 (kept 84% of the draft's variance)
- hedge density rose: 0.0 -> 1.15 per 1,000 words

## Advisories

- rhythm flattened: sentence-length sd 9.7 -> 8.1 (kept 84% of the draft's variance)
- hedge density rose: 0.0 -> 1.15 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [9.7, 9.8], "rhythm_health": [0.876, 0.759], "filler": [1.14, 1.14], "words": 874, "flesch": 58.3, "score": [true, 0, -0.94], "critic_fails": 0, "critic_advisories": 3}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [9.7, 8.4], "rhythm_health": [0.876, 0.824], "filler": [1.14, 1.17], "words": 854, "flesch": 60.6, "score": [true, 0, -0.45], "critic_fails": 0, "critic_advisories": 3}
{"attempt": 3, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [9.7, 8.1], "rhythm_health": [0.876, 0.925], "filler": [1.14, 1.15], "words": 872, "flesch": 58.8, "score": [true, 0, -0.31], "critic_fails": 0, "critic_advisories": 4}
```
