# Review report — 2026-10-29_half-your-tokens-5-of-bill_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-29_half-your-tokens-5-of-bill_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 24 · citations: 5 · quotes: 2 · sources: 5

## The reviewer's reading

THROUGH-LINE: The standard six-month test for AI success relies on token costs, but as cheaper open-weight models handle more volume, this metric will detach from actual business value, allowing teams to pass the test via routing tricks rather than real process change.
SHAPE: Lead: introduces the disconnect between token volume and the strict return deadlines ; The big picture: contrasts the massive, settled AI spend with the lack of clear budgets, ownership, and visibility on the return side ; By the numbers: isolates the core statistics showing the gap between volume, cost, and expected payback ; What I'd watch: highlights the tactical danger of optimizing for routing over real savings, and identifies what metrics buyers should track instead ; The catch: caveats the data as a forecast and separate surveys, noting that better metrics alone cannot fix organizational lag ; At a glance: summarizes the shift, its implications, and the specific indicators to monitor.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1138 | 1101 |
| sentence length mean | 16.2 | 15.3 |
| sentence length spread (sd) | 7.3 | 5.7 |
| rhythm health (0-1) | 0.837 | 0.49 |
| short sentences (<=8 words) | 12.2% | 14.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.88 | 0.91 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 1 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.5 (PASS) |
| sections restating the through-line | 2 | 2 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 7.3 -> 5.7 (kept 78% of the draft's variance)
- rhythm health fell 0.837 -> 0.49 (mean 16.2 -> 15.3 words, sd 7.3 -> 5.7) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm flattened: sentence-length sd 7.3 -> 5.7 (kept 78% of the draft's variance)
- rhythm health fell 0.837 -> 0.49 (mean 16.2 -> 15.3 words, sd 7.3 -> 5.7) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [7.3, 5.7], "rhythm_health": [0.837, 0.49], "filler": [0.0, 0.0], "words": 1101, "flesch": 52.5, "score": [true, 0, -3.19]}
{"attempt": 2, "ok": false, "hard": 6, "regressions": 1, "rhythm_sd": [7.3, 6.4], "rhythm_health": [0.837, 0.693], "filler": [0.0, 0.0], "words": 1000, "flesch": 47.2, "score": [false, -6, -0.62]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [7.3, 6.5], "rhythm_health": [0.837, 0.77], "filler": [0.0, 0.0], "words": 1139, "flesch": 53.0, "score": [false, -1, -0.01]}
```
