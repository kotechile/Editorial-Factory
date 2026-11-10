# Review report — 2026-11-10_your-pager-caps-at-2-incidents_final.md

- verdict: **ACCEPTED**
- draft: `2026-11-10_your-pager-caps-at-2-incidents_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 20 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: An on-call rotation is a fixed-cost machine with published limits — eight engineers for a single-site 24/7 rotation, two incidents per 12-hour shift — and the page budget, not the cloud bill, is the real ceiling on how many services a team can own.
SHAPE: Lead: states the two-incident ceiling and why it matters; At a glance: three-line summary box; The rotation comes before the architecture: derives the eight-engineer floor from Google's published rules and prices it; By the numbers: three figures that price the capacity; Where operators start on Monday: the tactical order — cut pages, resize rotation, change shifts last; The catch: the caveats — Google's numbers, the wage anchor, what survives the cautions.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1145 | 1142 |
| sentence length mean | 13.8 | 13.9 |
| sentence length spread (sd) | 5.4 | 5.5 |
| rhythm health (0-1) | 0.367 | 0.399 |
| short sentences (<=8 words) | 21.9% | 21.9% |
| filler per 1,000 words | 0.87 | 0.88 |
| hedge per 1,000 words | 0.87 | 0.88 |
| abstraction per 1,000 words | 0.87 | 0.88 |
| repeated 5-grams | 1 | 1 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 56.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 7.7% | 7.7% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.4, 5.3], "rhythm_health": [0.367, 0.352], "filler": [0.87, 0.88], "words": 1134, "flesch": 56.7, "score": [false, -1, -0.92], "critic_fails": 5, "critic_advisories": 2}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [5.4, 5.5], "rhythm_health": [0.367, 0.399], "filler": [0.87, 0.88], "words": 1142, "flesch": 56.5, "score": [true, 0, -0.54], "critic_fails": 0, "critic_advisories": 2}
```
