# Review report — 2026-10-31_two-builds-one-vault_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-31_two-builds-one-vault_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 2 · citations: 6 · quotes: 9 · sources: 6

## The reviewer's reading

THROUGH-LINE: Bitwarden's decision to ship commercially licensed builds to app stores does not end free self-hosting, but it shifts the burden of maintaining an open-source setup from a simple download to an ongoing device-by-device audit.
SHAPE:
Lead: Introduces the shift of store builds to the commercial license and the restrictive clause on those modules.
The big picture: Explores the tension between the vendor's calm reassurances and the reality that future features may only live in the commercial build.
By the numbers: Lays out the hard data on the build split, the specific license limits, and the server refresh window.
What I'd watch: Examines how the community is responding tactically by mapping the gaps between builds rather than arguing over the text.
The catch: Concludes that while the software remains open, the real cost is the administrative tinkering tax of side-loading and managing devices.
UNEARNED CLAIMS: The draft implies a high likelihood of missing features for free users right now, but the evidence only supports that future components *may* exist case-by-case; the draft also leans hard on the "tinkering tax" without fully connecting it to the specific administrative act of side-loading across multiple platforms.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 889 | 881 |
| sentence length mean | 17 | 15.4 |
| sentence length spread (sd) | 7.6 | 6.2 |
| rhythm health (0-1) | 0.929 | 0.586 |
| short sentences (<=8 words) | 10.8% | 9.8% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 2.25 | 2.27 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.1 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "My reading is that the admin work matters more than the license text. Bitwarden has not made its code closed, it has not named a price, and it says se…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words
- accessibility gate: undefined acronym(s): GNU

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 7.6 -> 6.2 (kept 82% of the draft's variance)
- rhythm health fell 0.929 -> 0.586 (mean 17 -> 15.4 words, sd 7.6 -> 6.2) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm flattened: sentence-length sd 7.6 -> 6.2 (kept 82% of the draft's variance)
- rhythm health fell 0.929 -> 0.586 (mean 17 -> 15.4 words, sd 7.6 -> 6.2) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 1, "rhythm_sd": [7.6, 7.2], "rhythm_health": [0.929, 0.866], "filler": [0.0, 0.0], "words": 889, "flesch": 51.6, "score": [false, -5, -0.5]}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 2, "rhythm_sd": [7.6, 6.2], "rhythm_health": [0.929, 0.586], "filler": [0.0, 0.0], "words": 881, "flesch": 53.1, "score": [false, -2, -2.76]}
{"attempt": 3, "ok": false, "hard": 3, "regressions": 1, "rhythm_sd": [7.6, 7.0], "rhythm_health": [0.929, 0.823], "filler": [0.0, 0.0], "words": 904, "flesch": 48.3, "score": [false, -3, -0.82]}
```
