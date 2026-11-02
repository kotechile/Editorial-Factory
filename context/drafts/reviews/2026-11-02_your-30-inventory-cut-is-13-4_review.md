# Review report — 2026-11-02_your-30-inventory-cut-is-13-4_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-02_your-30-inventory-cut-is-13-4_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 19 · citations: 5 · quotes: 2 · sources: 5

## The reviewer's reading

THROUGH-LINE: Doubling order frequency halves the review interval, not the supplier’s lead time, so the safety-stock cut shrinks from 29.3% toward zero as lead time grows, while the saving that does scale is cycle stock and it pays only if one extra purchase order costs less than $13.87.
SHAPE: The big picture: establish the square-root exposure window and why the 30% claim depends on zero lead time; By the numbers: fix the ceiling, the real cuts by lead time, and the cycle-stock and break-even arithmetic; What I'd watch: trace the supplier clock and the per-order cost to show where the decision lives; The catch: show lead-time variance and the model's unit trap, then state the narrower honest position; At a glance: distill shift, number, risk.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1057 | 949 |
| sentence length mean | 20.7 | 23.6 |
| sentence length spread (sd) | 9.2 | 7.0 |
| rhythm health (0-1) | 0.71 | 0.534 |
| short sentences (<=8 words) | 11.6% | 0.0% |
| filler per 1,000 words | 0.95 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 50.9 (PASS) |
| sections restating the through-line | 1 | 2 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 9.2 -> 7.0 (kept 76% of the draft's variance)
- rhythm health fell 0.71 -> 0.534 (mean 20.7 -> 23.6 words, sd 9.2 -> 7.0) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm flattened: sentence-length sd 9.2 -> 7.0 (kept 76% of the draft's variance)
- rhythm health fell 0.71 -> 0.534 (mean 20.7 -> 23.6 words, sd 9.2 -> 7.0) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [9.2, 7.0], "rhythm_health": [0.71, 0.534], "filler": [0.95, 0.0], "words": 949, "flesch": 50.9, "score": [true, 0, -0.46]}
{"attempt": 2, "ok": false, "hard": 4, "regressions": 0, "rhythm_sd": [9.2, 8.2], "rhythm_health": [0.71, 0.857], "filler": [0.95, 0.0], "words": 1020, "flesch": 57.1, "score": [false, -4, 2.13]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [9.2, 9.0], "rhythm_health": [0.71, 0.864], "filler": [0.95, 0.0], "words": 1034, "flesch": 56.4, "score": [false, -1, 2.18]}
```
