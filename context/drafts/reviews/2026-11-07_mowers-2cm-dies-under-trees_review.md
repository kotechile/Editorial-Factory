# Review report — 2026-11-07_mowers-2cm-dies-under-trees_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-07_mowers-2cm-dies-under-trees_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 8 · citations: 9 · quotes: 2 · sources: 9
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A wire-free mower's centimetre accuracy is correction data delivered over a path that a specific lot either already has or must be built for, so the sky and signal above the grass decide the purchase before the machine does.
SHAPE: Lead: state the two correction paths and the decision they force; At a glance: fix the shift, the canopy failure figure, and the operational risk; The Correction Ladder: explain RTK correction, tabulate the three options, and show coverage as the real gate; By the numbers: hold the price, sample size, and favourable-forest fix rate the prose does not restate; What the Sellers Already Concede: report what manufacturer pages print about signal loss and coverage queues; The catch: place the 2.03 m canopy result on the spectrum from conifer forest to a three-maple yard.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 892 | 818 |
| sentence length mean | 20.1 | 16.2 |
| sentence length spread (sd) | 8.6 | 4.9 |
| rhythm health (0-1) | 0.736 | 0.372 |
| short sentences (<=8 words) | 2.7% | 2.4% |
| filler per 1,000 words | 1.12 | 0.0 |
| hedge per 1,000 words | 1.12 | 1.22 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 51.2 (PASS) |
| sections restating the through-line | 1 | 3 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 8.6 -> 4.9 (kept 57% of the draft's variance)
- rhythm health fell 0.736 -> 0.372 (mean 20.1 -> 16.2 words, sd 8.6 -> 4.9) — vary sentence length and break any run-on past 40 words
- the through-line is restated in 3 sections (lead, tension, nuanced-takeaway) — develop it, do not repeat it

## Advisories

- rhythm flattened: sentence-length sd 8.6 -> 4.9 (kept 57% of the draft's variance)
- rhythm health fell 0.736 -> 0.372 (mean 20.1 -> 16.2 words, sd 8.6 -> 4.9) — vary sentence length and break any run-on past 40 words
- the through-line is restated in 3 sections (lead, tension, nuanced-takeaway) — develop it, do not repeat it

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.6, 6.6], "rhythm_health": [0.736, 0.723], "filler": [1.12, 0.0], "words": 804, "flesch": 50.8, "score": [false, -1, 0.94], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 3, "rhythm_sd": [8.6, 4.9], "rhythm_health": [0.736, 0.372], "filler": [1.12, 0.0], "words": 818, "flesch": 51.2, "score": [true, 0, -2.85], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.6, 6.6], "rhythm_health": [0.736, 0.756], "filler": [1.12, 0.0], "words": 830, "flesch": 52.8, "score": [false, -1, 1.23], "critic_fails": 1, "critic_advisories": 0}
```
