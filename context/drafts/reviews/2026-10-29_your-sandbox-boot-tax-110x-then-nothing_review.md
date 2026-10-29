# Review report — 2026-10-29_your-sandbox-boot-tax-110x-then-nothing_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-29_your-sandbox-boot-tax-110x-then-nothing_draft.md` · attempt kept: 3 of 4
- figures in the ledger: 15 · citations: 5 · quotes: 0 · sources: 5

## The reviewer's reading

THROUGH-LINE: The sandbox boot cost is a fixed tax paid once per agent trajectory, meaning substrate choice is an arithmetic problem where the same delay ruins a short run but vanishes into the noise of a long one.
SHAPE: Lead: Introduces the sandbox boot tax and the arithmetic reality of fixed costs divided by trajectory length. ; The big picture: Explains the architectural trade-off between keeping sandboxes warm and starting them on demand, showing how both fail to solve the underlying math. ; By the numbers: Lays out the specific metrics of the boot tax, from the 110x spread to the 125ms floor. ; What I'd watch: Outlines the practical steps for evaluating the cost, focusing on run length, billing models, and hiding the boot behind inference. ; The catch: Contextualizes the 110x claim as a vendor-authored preprint and emphasizes that no source provides a universal break-even point. ; At a glance: Summarizes the shift, the impact, the metrics to watch, and the limitations of the data.
UNEARNED: The draft claims "agent runtimes now build a fresh box for most tool-using jobs," but the brief only supports the *evaluation* of this boundary (SpecBox frames it as a trade-off), not a definitive industry-wide shift to fresh boxes for *most* jobs. I have reframed this to reflect the architectural choice rather than an asserted market standard.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1108 | 1037 |
| sentence length mean | 17.8 | 16.3 |
| sentence length spread (sd) | 10.2 | 7.5 |
| rhythm health (0-1) | 0.832 | 0.88 |
| short sentences (<=8 words) | 15.6% | 19.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 64.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 10.2 -> 7.5 (kept 74% of the draft's variance)

## Advisories

- rhythm flattened: sentence-length sd 10.2 -> 7.5 (kept 74% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 3, "rhythm_sd": [10.2, 5.6], "rhythm_health": [0.832, 0.432], "filler": [0.0, 0.0], "words": 895, "flesch": 50.7, "score": [false, -1, -3.87]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.2, 10.3], "rhythm_health": [0.832, 0.702], "filler": [0.0, 0.0], "words": 704, "flesch": 45.4, "score": [false, -1, -1.04]}
{"attempt": 3, "ok": true, "hard": 0, "regressions": 1, "rhythm_sd": [10.2, 7.5], "rhythm_health": [0.832, 0.88], "filler": [0.0, 0.0], "words": 1037, "flesch": 64.9, "score": [true, 0, 0.38]}
{"attempt": 4, "ok": false, "hard": 2, "regressions": 2, "rhythm_sd": [10.2, 11.6], "rhythm_health": [0.832, 0.566], "filler": [0.0, 0.0], "words": 842, "flesch": 45.4, "score": [false, -2, -2.84]}
```
