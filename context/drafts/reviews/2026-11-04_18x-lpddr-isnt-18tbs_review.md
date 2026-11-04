# Review report — 2026-11-04_18x-lpddr-isnt-18tbs_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-04_18x-lpddr-isnt-18tbs_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 12 · citations: 4 · quotes: 0 · sources: 4

## The reviewer's reading

THROUGH-LINE: Microsoft's Maia 300 and Qualcomm's high bandwidth compute attack the same memory-bound inference bottleneck in opposite directions, but their headline numbers measure different things against different bases, leaving tokens per watt on a named workload as the missing buyer's measure.
SHAPE: Lead: sets the two headline numbers as unlike quantities and why; The big picture: shows the shared bottleneck, the three design paths, and the unit split; By the numbers: grounds the rack and efficiency claims not stated in prose; What I'd watch: reads the field from the buyer side and names the outside test to track; The catch: explains that the ratio is not easy marketing but still not comparable; At a glance: holds the shortest version without new claims.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1023 | 908 |
| sentence length mean | 18.0 | 19.0 |
| sentence length spread (sd) | 8.5 | 7.4 |
| rhythm health (0-1) | 0.997 | 0.901 |
| short sentences (<=8 words) | 14.9% | 2.4% |
| filler per 1,000 words | 0.98 | 0.0 |
| hedge per 1,000 words | 1.96 | 1.1 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.7 (PASS) |
| sections restating the through-line | 2 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The tidy story is that these figures are marketing and a buyer should ignore them. My own caution is that a ratio is not automatically weaker than a r…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- rhythm health fell 0.997 -> 0.901 (mean 18.0 -> 19.0 words, sd 8.5 -> 7.4) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.997 -> 0.901 (mean 18.0 -> 19.0 words, sd 8.5 -> 7.4) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 0, "rhythm_sd": [8.5, 8.0], "rhythm_health": [0.997, 0.992], "filler": [0.98, 0.0], "words": 982, "flesch": 48.0, "score": [false, -5, 1.5]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.5, 7.4], "rhythm_health": [0.997, 0.901], "filler": [0.98, 0.0], "words": 908, "flesch": 53.7, "score": [false, -1, 0.73]}
```
