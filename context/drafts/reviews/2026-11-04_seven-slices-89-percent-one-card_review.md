# Review report — 2026-11-04_seven-slices-89-percent-one-card_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-04_seven-slices-89-percent-one-card_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 28 · citations: 4 · quotes: 2 · sources: 4

## The reviewer's reading

THROUGH-LINE: A Multi-Instance GPU slice is metered by memory eighths, not compute sevenths, so seven tenants get roughly 89% of one card's memory speed and 85% of its cores, and sizing must start from the resource a workload saturates.
SHAPE: The big picture: state the asymmetry and the aggregate; By the numbers: hold the figures the prose does not restate; What I'd watch: report how operators test one axis at a time and the isolation trade, plus the open copy-lane question; The catch: bound the claim with the core-bound LLM case, the single-machine copy link, and NVIDIA's rounding; At a glance: summarize the shift, the floor, and the risk.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 803 | 771 |
| sentence length mean | 18.3 | 18.5 |
| sentence length spread (sd) | 11.6 | 10.9 |
| rhythm health (0-1) | 0.716 | 0.827 |
| short sentences (<=8 words) | 24.3% | 22.9% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 3.74 | 3.89 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.9 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): GB, NVIDIA
- accessibility gate: unglossed specialist term(s): KV cache — explain each in plain words at first use (em-dash clause or parenthesis)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 0, "rhythm_sd": [11.6, 9.9], "rhythm_health": [0.716, 0.702], "filler": [0.0, 0.0], "words": 787, "flesch": 49.1, "score": [false, -4, 0.61]}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 0, "rhythm_sd": [11.6, 10.9], "rhythm_health": [0.716, 0.827], "filler": [0.0, 0.0], "words": 771, "flesch": 54.9, "score": [false, -2, 0.8]}
```
