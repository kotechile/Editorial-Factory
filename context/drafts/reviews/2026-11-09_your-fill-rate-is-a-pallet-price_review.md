# Review report — 2026-11-09_your-fill-rate-is-a-pallet-price_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-09_your-fill-rate-is-a-pallet-price_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 23 · citations: 3 · quotes: 2 · sources: 3
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A shipper's order-fill promise is now priced by the spread between scarce committed warehouse space and uneven short-term space, not by the size of the safety stock it sets.
SHAPE: At a glance: states the shift, proof and risk; The big picture: sets the release timeline and explains the split between committed and short-term space; By the numbers: gives fresh figures that sharpen the mechanism; What I'd watch: reports local ratings and narrowing buyer leverage; The catch: limits the comparison and names the publisher's stake.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 835 | 808 |
| sentence length mean | 15.0 | 22.5 |
| sentence length spread (sd) | 7.5 | 8.0 |
| rhythm health (0-1) | 0.703 | 0.571 |
| short sentences (<=8 words) | 14.3% | 0.0% |
| filler per 1,000 words | 1.2 | 0.0 |
| hedge per 1,000 words | 1.2 | 1.24 |
| abstraction per 1,000 words | 2.4 | 2.48 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 46.9 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 46.9 < floor 50.0 — the long words costing the score, each to be replaced or used once: warehouse, quarter, september, logistics, short-term, october, capacity, national, markets, cheapest, complete, committed

## Flow regressions against the draft

- rhythm health fell 0.703 -> 0.571 (mean 15.0 -> 22.5 words, sd 7.5 -> 8.0) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.703 -> 0.571 (mean 15.0 -> 22.5 words, sd 7.5 -> 8.0) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 0, "rhythm_sd": [7.5, 7.1], "rhythm_health": [0.703, 0.764], "filler": [1.2, 1.23], "words": 810, "flesch": 54.4, "score": [false, -2, 0.44], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [7.5, 8.0], "rhythm_health": [0.703, 0.571], "filler": [1.2, 0.0], "words": 808, "flesch": 46.9, "score": [false, -1, 0.12], "critic_fails": 0, "critic_advisories": 2}
{"attempt": 3, "ok": false, "hard": 4, "regressions": 1, "rhythm_sd": [7.5, 6.9], "rhythm_health": [0.703, 0.801], "filler": [1.2, 2.61], "words": 765, "flesch": 50.9, "score": [false, -4, -0.99], "critic_fails": 1, "critic_advisories": 2}
```
