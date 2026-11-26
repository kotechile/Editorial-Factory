# Review report — 2026-11-26_your-sku-cut-leaves-a-1-1b-bill_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-26_your-sku-cut-leaves-a-1-1b-bill_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 14 · citations: 5 · quotes: 5 · sources: 5
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Under Armour's doubled 50% SKU cut is a one-time simplification that pays once, while the $1.1 billion overhang above plan is a recurring decision-speed problem the purge alone cannot fix.

SHAPE: lead — the doubled cut announced against the inventory that grew anyway, and the margin cost already booked; At a glance — one plain paragraph naming subject, audience, finding; tension (chronology) — the three dates in order (quarter end, call, trade write-up), then the mechanism: why fewer SKUs simplify a forecast but not the demand that left the stock there; By the numbers — three one-metric bullets after the mechanism; tactical — what Under Armour is actually doing next (licensing, timed launches, reduced buys, AI hours) and the Cisco fork; catch — the excess as symptom, the fall 2027 timing, the bundled guidance that hides what the cut bought.

NOT YET EARNED: the draft's lead says "sales in North America fell faster than the buys" — the release supports wholesale −6%, DTC −8%, eCommerce −12%, not that comparison as stated; I restate it as channels falling while inventory rose. The draft's "spread over two years" for the halving has no source support; dropped. The 20–30% carrying-cost figure must stay tied to [4] and the inline link. SKU figures and call quotes stay cited to [2], release figures to [1].

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 796 | 788 |
| sentence length mean | 17.3 | 16.5 |
| sentence length spread (sd) | 8.9 | 8.3 |
| rhythm health (0-1) | 0.95 | 0.891 |
| short sentences (<=8 words) | 18.5% | 15.9% |
| filler per 1,000 words | 1.26 | 1.27 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 48.7 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 48.7 < floor 50.0 — the long words costing the score, each to be replaced or used once: inventory, decision, billion, forecast, planning, quarter, november, reduction, cutting, revenue, guidance, planned

## Flow regressions against the draft

- rhythm health fell 0.95 -> 0.891 (mean 17.3 -> 16.5 words, sd 8.9 -> 8.3) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm health fell 0.95 -> 0.891 (mean 17.3 -> 16.5 words, sd 8.9 -> 8.3) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [8.9, 8.3], "rhythm_health": [0.95, 0.891], "filler": [1.26, 1.27], "words": 788, "flesch": 48.7, "score": [false, -1, -0.48], "critic_fails": 0, "critic_advisories": 1}
```
