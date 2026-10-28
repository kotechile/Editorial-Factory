# Review report — 2026-10-28_your-sso-bill-125-a-connection_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-28_your-sso-bill-125-a-connection_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 15 · citations: 5 · quotes: 1 · sources: 5

## The reviewer's reading

THROUGH-LINE: The cost of single sign-on depends entirely on the unit a vendor chooses to bill—per connection, per seat, or flat plan—meaning a software seat uplift can quickly outpace a dedicated identity connection.
SHAPE: Lead: introduces the three pricing units for the same sign-on feature ; The big picture: explains the architectural shift from custom code to commodity feature and establishes the friction of hidden costs ; By the numbers: quantifies the thresholds where one unit overtakes another using exact vendor pricing ; What I'd watch: examines how teams separate these costs and tracks vendor pricing maneuvers ; The catch: contextualizes the tier uplift as a ceiling rather than a pure feature price and challenges vendor comparison math ; At a glance: summarizes the units, the impact on headcount, and the implications for buyers.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1130 | 900 |
| sentence length mean | 19.2 | 17.7 |
| sentence length spread (sd) | 7.4 | 7.5 |
| rhythm health (0-1) | 0.895 | 0.967 |
| short sentences (<=8 words) | 9.4% | 8.6% |
| filler per 1,000 words | 0.88 | 0.0 |
| hedge per 1,000 words | 0.0 | 1.11 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.4 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "My reading, held loosely: the tier uplift operates as a ceiling, not a pure price for sign-on. Slack's Business+ also carries native data loss prevent…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- hedge density rose: 0.0 -> 1.11 per 1,000 words

## Advisories

- hedge density rose: 0.0 -> 1.11 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 0, "rhythm_sd": [7.4, 7.3], "rhythm_health": [0.895, 0.896], "filler": [0.88, 0.89], "words": 1129, "flesch": 57.0, "score": [false, -4, -0.0]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [7.4, 7.5], "rhythm_health": [0.895, 0.967], "filler": [0.88, 0.0], "words": 900, "flesch": 54.4, "score": [false, -1, 0.79]}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [7.4, 7.5], "rhythm_health": [0.895, 0.842], "filler": [0.88, 0.82], "words": 1216, "flesch": 47.1, "score": [false, -2, -0.36]}
```
