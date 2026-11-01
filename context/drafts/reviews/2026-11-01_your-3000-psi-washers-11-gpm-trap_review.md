# Review report — 2026-11-01_your-3000-psi-washers-11-gpm-trap_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-01_your-3000-psi-washers-11-gpm-trap_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 31 · citations: 7 · quotes: 0 · sources: 7

## The reviewer's reading

THROUGH-LINE: Greenworks markets its highest-PSI pressure washer using a peak flow rate that only applies at a low-pressure rinse setting, meaning the cheaper, lower-PSI models actually move more water during heavy cleaning.
SHAPE: Lead: introduces the misleading specification and the models ; The big picture: explains how pressure and flow trade off and how competitors approach the claim ; By the numbers: breaks down the cost per unit of work ; What I'd watch: analyzes the pricing inversion and older model listings ; The catch: reveals the accessory mismatch and missing mid-curve data ; At a glance: summarizes the shift, the key number, and the risk.
UNEARNED CLAIMS: The draft states outright that 100 PSI is a "rinse" setting without citing the manufacturer calling it that; it is a deduction based on DeWalt's parallel soap nozzle footnote.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1292 | 1069 |
| sentence length mean | 24.3 | 20.6 |
| sentence length spread (sd) | 8.4 | 7.0 |
| rhythm health (0-1) | 0.553 | 0.728 |
| short sentences (<=8 words) | 4.7% | 7.5% |
| filler per 1,000 words | 1.55 | 0.0 |
| hedge per 1,000 words | 0.77 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 6 | 6 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 57.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 8.4 -> 7.0 (kept 83% of the draft's variance)

## Advisories

- rhythm flattened: sentence-length sd 8.4 -> 7.0 (kept 83% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 2, "rhythm_sd": [8.4, 5.0], "rhythm_health": [0.553, 0.362], "filler": [1.55, 0.0], "words": 746, "flesch": 61.6, "score": [false, -1, 0.48]}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [8.4, 7.0], "rhythm_health": [0.553, 0.728], "filler": [1.55, 0.0], "words": 1069, "flesch": 57.9, "score": [true, 0, 1.01]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.4, 8.3], "rhythm_health": [0.553, 0.986], "filler": [1.55, 0.0], "words": 985, "flesch": 53.5, "score": [false, -1, 2.68]}
```
