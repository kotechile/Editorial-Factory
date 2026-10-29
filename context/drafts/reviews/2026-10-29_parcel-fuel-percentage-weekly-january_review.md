# Review report — 2026-10-29_parcel-fuel-percentage-weekly-january_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-29_parcel-fuel-percentage-weekly-january_draft.md` · attempt kept: 3 of 3
- figures in the ledger: 19 · citations: 6 · quotes: 7 · sources: 6

## The reviewer's reading

THROUGH-LINE: The United States Postal Service is shifting its parcel pricing power from a negotiated base rate to a weekly fuel percentage, adopting a strategy that United Parcel Service just used to drive revenue up while volume fell.
SHAPE: Lead: Introduces the USPS policy change and the UPS earnings context. ; The big picture: Explains how moving from a flat charge to a weekly floating percentage transfers pricing risk to the shipper. ; By the numbers: Lists the exact figures defining the old bridge, the new USPS metrics, and the UPS earnings. ; What I'd watch: Highlights the operational friction points, specifically contract carve-outs and transition timing. ; The catch: Tempers the panic by noting the surcharge only applies to base postage. ; At a glance: Summarizes the shift, the stakes, and the immediate operational hurdles.
UNEARNED CLAIMS: The draft implies the new weekly percentage will be more expensive than the 8% bridge, but since the initial percentage is unpublished, we cannot claim it is a price hike yet.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1114 | 1039 |
| sentence length mean | 19.4 | 17.5 |
| sentence length spread (sd) | 9.9 | 7.9 |
| rhythm health (0-1) | 0.898 | 0.968 |
| short sentences (<=8 words) | 23.8% | 9.1% |
| filler per 1,000 words | 0.9 | 0.0 |
| hedge per 1,000 words | 4.49 | 3.85 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 1 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 49.6 (FAIL) |
| sections restating the through-line | 2 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 49.6 < floor 50.0 — the long words costing the score, each to be replaced or used once: revenue, january, postage, million, carrier, contract, quarter, service, domestic, pricing, arrives, shipper

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 9.9 -> 7.9 (kept 80% of the draft's variance)

## Advisories

- rhythm flattened: sentence-length sd 9.9 -> 7.9 (kept 80% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 2, "rhythm_sd": [9.9, 6.5], "rhythm_health": [0.898, 0.57], "filler": [0.9, 0.0], "words": 1132, "flesch": 50.7, "score": [false, -1, -1.15]}
{"attempt": 2, "ok": false, "hard": 4, "regressions": 0, "rhythm_sd": [9.9, 9.3], "rhythm_health": [0.898, 0.936], "filler": [0.9, 0.0], "words": 1144, "flesch": 53.3, "score": [false, -4, 0.88]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [9.9, 7.9], "rhythm_health": [0.898, 0.968], "filler": [0.9, 0.0], "words": 1039, "flesch": 49.6, "score": [false, -1, 1.84]}
```
