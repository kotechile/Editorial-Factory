# Review report — 2026-11-07_your-mowers-recall-has-an-importer_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-07_your-mowers-recall-has-an-importer_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 14 · citations: 6 · quotes: 0 · sources: 6
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The importer, not the brand on the machine, determines whether a defective outdoor tool gets repaired or abandoned, and this quarter both Stanley Black & Decker and Husqvarna moved production away from their own badges.
SHAPE: Lead opens with the two recall outcomes and the importer gap; At a glance fixes the shift, number and risk; The big picture lays out the chronology and the importer mechanism; By the numbers holds three figures not used in the prose; What I'd watch follows the margin table and the parts channel; The catch separates importer reachability from build quality.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 963 | 975 |
| sentence length mean | 20.9 | 18.6 |
| sentence length spread (sd) | 10.3 | 9.3 |
| rhythm health (0-1) | 0.697 | 0.855 |
| short sentences (<=8 words) | 9.5% | 14.6% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 1.03 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 50.8 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): DR

## Flow regressions against the draft

- hedge density rose: 0.0 -> 1.03 per 1,000 words

## Advisories

- figure not in the draft or the brief: 22 — confirm it is the source's own
- hedge density rose: 0.0 -> 1.03 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 0, "rhythm_sd": [10.3, 9.2], "rhythm_health": [0.697, 0.994], "filler": [0.0, 0.0], "words": 983, "flesch": 54.4, "score": [false, -4, 2.38], "critic_fails": 2, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.3, 9.3], "rhythm_health": [0.697, 0.855], "filler": [0.0, 0.0], "words": 975, "flesch": 50.8, "score": [false, -1, 0.65], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 3, "regressions": 1, "rhythm_sd": [10.3, 8.7], "rhythm_health": [0.697, 0.937], "filler": [0.0, 0.0], "words": 785, "flesch": 52.4, "score": [false, -3, 1.92], "critic_fails": 2, "critic_advisories": 0}
```
