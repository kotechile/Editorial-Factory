# Review report — 2026-11-09_your-index-is-the-boundary_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-09_your-index-is-the-boundary_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 7 · citations: 4 · quotes: 1 · sources: 4
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A retrieval index is a second copy of the corpus, so the real access boundary is the number and partitioning of indexes plus the identity allowed to query each one; any filter that runs after retrieval is decoration.
SHAPE: At a glance: state the shift, the proof figure, and the operational risk ; The big picture: establish the retrieval order, the inversion evidence, and the poisoning evidence that make the index a boundary ; By the numbers: pin the three figures not already explained ; What I'd watch: report the vendor isolation tiers and the classification-attribute decision ; The catch: hold the cost of isolation and the identity limit together, then close on the pre-retrieval check.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 832 | 692 |
| sentence length mean | 18.6 | 16.9 |
| sentence length spread (sd) | 6.9 | 6.8 |
| rhythm health (0-1) | 0.824 | 0.791 |
| short sentences (<=8 words) | 5.1% | 5.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 4.81 | 5.78 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 51.4 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- hedge density rose: 4.81 -> 5.78 per 1,000 words

## Advisories

- hedge density rose: 4.81 -> 5.78 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 3, "regressions": 1, "rhythm_sd": [6.9, 7.4], "rhythm_health": [0.824, 0.968], "filler": [0.0, 0.0], "words": 736, "flesch": 51.8, "score": [false, -3, 0.78], "critic_fails": 2, "critic_advisories": 0}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [6.9, 6.8], "rhythm_health": [0.824, 0.791], "filler": [0.0, 0.0], "words": 692, "flesch": 51.4, "score": [true, 0, -0.85], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [6.9, 6.6], "rhythm_health": [0.824, 0.725], "filler": [0.0, 0.0], "words": 826, "flesch": 48.8, "score": [false, -2, 2.09], "critic_fails": 1, "critic_advisories": 0}
```
