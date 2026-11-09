# Review report — 2026-11-09_your-condensers-repair-bill-2090-vs-700_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-09_your-condensers-repair-bill-2090-vs-700_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 8 · citations: 7 · quotes: 0 · sources: 7
- reader-side critic: 0 holding defect(s), 4 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The refrigerant class inside the condenser now decides the repair: R-410A's 2,090 global warming potential sits above the 700 cap for new residential equipment, and the statute cuts the national allowance to 30 percent in 2029.
SHAPE: At a glance: delivers the three urgent facts; The big picture: sets the timeline and the supply ladder once; By the numbers: isolates the replacement fluids and the later allowance floor; What I'd watch: reads the bid through gas, build date, and the 2029 step; The catch: explains what the law does not restrict and what the sources do not price.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 907 | 894 |
| sentence length mean | 18.2 | 19.8 |
| sentence length spread (sd) | 8.2 | 6.6 |
| rhythm health (0-1) | 0.984 | 0.69 |
| short sentences (<=8 words) | 8.7% | 0.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 4.41 | 4.47 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.3 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 8.2 -> 6.6 (kept 80% of the draft's variance)
- rhythm health fell 0.984 -> 0.69 (mean 18.2 -> 19.8 words, sd 8.2 -> 6.6) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm flattened: sentence-length sd 8.2 -> 6.6 (kept 80% of the draft's variance)
- rhythm health fell 0.984 -> 0.69 (mean 18.2 -> 19.8 words, sd 8.2 -> 6.6) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 1, "rhythm_sd": [8.2, 7.4], "rhythm_health": [0.984, 0.932], "filler": [0.0, 0.0], "words": 743, "flesch": 48.2, "score": [false, -5, -0.99], "critic_fails": 2, "critic_advisories": 1}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [8.2, 6.6], "rhythm_health": [0.984, 0.69], "filler": [0.0, 0.0], "words": 894, "flesch": 54.3, "score": [true, 0, -2.39], "critic_fails": 0, "critic_advisories": 4}
{"attempt": 3, "ok": false, "hard": 4, "regressions": 3, "rhythm_sd": [8.2, 5.8], "rhythm_health": [0.984, 0.495], "filler": [0.0, 0.0], "words": 776, "flesch": 54.9, "score": [false, -4, -4.76], "critic_fails": 2, "critic_advisories": 1}
```
