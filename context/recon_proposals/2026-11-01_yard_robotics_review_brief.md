# Review brief — yard_robotics — 2026-11-01

**Vertical:** yard_robotics
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to take the Kress KR172 at the $1,249.99 its own model page shows, the $1,699.99 its dealer promotion asks through 31 December 2026, or the Mammotion LUBA mini 2 AWD 1500 at $1,799.00, for a 0.3 to 0.5 acre lot bought in the off-season window.
**Format:** comparison
**Price as of:** 2026-11-01
**Verdict:** Buy the Kress KR172 at $1,249.99 if a dealer will put that number on paper — at that price it is the cheapest rated acre here at $2,499.98 an acre, and the Mammotion LUBA mini 2 AWD 1500 at $1,799.00 wins only on a lot under heavy canopy or steeper than 40%, where its onboard LiDAR and its 80% slope claim are the point.
**De-dup:** `2026-10-24_your-1-acre-mowers-04-acre-trap` is the sizing rule (a rating is a best case, so judge cost per usable acre) and prices no purchase; `2026-10-25_snow-robot-stops-at-6000-ft2-it-docks` reviewed a robotic snow blower, not a mower. A corpus grep across `published/`, `context/drafts/` and `context/recon_proposals/` for KR172, KR161 or LUBA mini 2 returns no review, and no artifact prices a mower in a November promotion window.
**Thesis:** The off-season sale is the moment this decision actually gets made, and the numbers that settle it are not the ones on the banner: the half-acre Kress costs $199 more than its own quarter-acre sibling, the same model costs $450 more through the dealer promotion than on Kress's own model page, and the LiDAR machine costs $549 more for 0.13 acre less rated lawn.

**Lead:** the vertical's beats, `context/verticals.json` `primary_angles` #1 ("wire-free navigation on a real lot: LiDAR vs RTK vs vision where tree cover blocks the sky") and #2 (the breakeven against a landscaping contract), read at the moment the money moves: the first week of November, with Kress running a dealer promotion that states it is valid through 31 December 2026 and Mammotion sitting on a $200 discount off a $1,999 regular price. GSC was checked as the bonus signal only (`context/recon_proposals/2026-10-24_gsc_yard_robotics_opportunities.md` carries 0 candidates; thin impressions on a young site never veto a topic). The persona is `homeowner_pro` in `context/personas.json` — payback math and gotchas — so the brief prices the acre, not the badge.

| Product | Price | Source | Note |
|---|---|---|---|
| Kress KR172 ½-acre RTKⁿ | $1,249.99 | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | $2,499.99 regular; 0.5 acre recommended, 0.7 acre maximum at a 72-hour cadence; "Find a dealer", no cart |
| Kress KR161 ¼-acre RTKⁿ | $1,050.99 | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BC-acre-robotic-lawn-mower-kr161 | $2,099.99 regular; 0.25 acre maximum; same page pattern |
| Mammotion LUBA mini 2 AWD 1500 | $1,799.00 | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | $1,999.00 regular; 0.37 acre; 360° LiDAR plus dual-camera vision; online cart |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Kress — KR172 model page (price block) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | $1,249.99 | vendor sale price shown on the model page, against $2,499.99 regular |
| 2 | Kress — KR172 model page (price block) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | $2,499.99 | vendor regular price on the same page |
| 3 | Kress — KR172 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | 0.5 acre | vendor: "Recommend area (cutting every 48h) 0.5 acre"; the same table prints "Maximum area (cutting every 72h) 0.7 acre" |
| 4 | Kress — KR172 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | 59 db | vendor: "Sound level perceived 59 db" |
| 5 | Kress — KR172 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | 40% | vendor: "Maximum slope 40%" |
| 6 | Kress — KR172 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | 26.48 lbs | vendor weight, with the charging base and RTK antenna listed in the box contents |
| 7 | Kress — KR172 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | 2026-11-01 | 7 7/8 in | vendor cutting width, systematic navigation, 4 Ah battery at 20 V |
| 8 | Kress — KR161 model page (price block) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BC-acre-robotic-lawn-mower-kr161 | 2026-11-01 | $1,050.99 | vendor sale price, against $2,099.99 regular |
| 9 | Kress — KR161 model page (technical specifications) | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BC-acre-robotic-lawn-mower-kr161 | 2026-11-01 | 0.25 acre | vendor: "Maximum lawn size 0.25 acre" — no second cadence figure is printed for this model |
| 10 | Kress — dealer promotion page (KR172 row) | https://www.kress.com/en-us/robotic-mowers | 2026-11-01 | $1,699 | vendor: "Kress RTKⁿ ½-acre robotic lawn mower KR172 $3,199.98 Only $1,699.99"; page terms "Offer valid through December 31, 2026, or while supplies last. At participating Kress dealer only." |
| 11 | Kress — dealer promotion page (KR172 anchor price) | https://www.kress.com/en-us/robotic-mowers | 2026-11-01 | $3,199 | the "regular" price the same page strikes through, $700 above the $2,499.99 on the model page |
| 12 | Kress — dealer promotion page (offer terms) | https://www.kress.com/en-us/robotic-mowers | 2026-11-01 | $699.99 | "a free RTK mapping cart worth $699.99", part of the same offer |
| 13 | Mammotion — LUBA mini 2 AWD product page (price block) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | $1,799.00 | vendor sale price, online cart |
| 14 | Mammotion — LUBA mini 2 AWD product page (price block) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | $1,999.00 | vendor regular price |
| 15 | Mammotion — LUBA mini 2 AWD product page (coverage) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | 0.37 acre | vendor: "Ideal for small to medium lawns up to 0.37 acre" |
| 16 | Mammotion — LUBA mini 2 AWD product page (battery FAQ) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | 0.12 acre | vendor: "6.1Ah … delivering up to 0.12 acre of mowing coverage per charge" |
| 17 | Mammotion — LUBA mini 2 AWD product page (slope) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | 80% | vendor: "Handles slopes up to 80%" |
| 18 | Mammotion — LUBA mini 2 AWD product page (noise) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | 65 dB | vendor: "<65 dB Noise Level" — a ceiling, not a measured figure |
| 19 | Mammotion — LUBA mini 2 AWD product page (battery) | https://us.mammotion.com/products/luba-mini-2-awd-robot-lawn-mower | 2026-11-01 | 6.1 Ah | vendor battery capacity; IPX6 stated on the same block |
| 20 | TurfCloud Store — authorized Kress dealer listing | https://store.turfcloud.com/products/kr172-kress-rtk%E2%81%BF-acre-robotic-lawn-mower | 2026-11-01 | $1,249.99 | dealer listing at the same $1,249.99 against $2,499.99 regular; the listing showed the unit out of stock |
| 21 | SmartYard Northwest — authorized Kress dealer, model table | https://smartyardnw.com/kress-robotic-mowers-review | 2026-11-01 | $1,699.99 | a second authorized dealer's price for the KR172, matching the promotion rather than the model page |
| 22 | PCMag — best robot lawn mowers (tested picks) | https://www.pcmag.com/picks/the-best-robot-lawn-mowers | 2026-11-01 | $1,099 | the cheap end of the tested field: a 0.3-acre LiDAR unit at $1,099, the floor this comparison sits above |

## What the article must carry

- **The two-price fact, stated plainly.** Kress's own model page shows $1,249.99 against $2,499.99; its own
  promotion page shows $1,699.99 against $3,199.98. Same model, same day, two anchors and two sale prices,
  $450 apart, and the higher one is the one the banner leads with. Say which page prints which, and date both.
- **Do not call the low price transactable.** The model page's call to action is "Find a dealer" — there is no
  cart on it. One authorized dealer listed the same model at the same $1,249.99 and showed none in stock;
  a second dealer listed $1,699.99. The honest sentence is that the number you can buy at depends on the
  dealer, so the quote is the thing to get in writing before the 31 December close.
- **Cost per rated acre, computed from printed endpoints, never estimated.** KR161 $1,050.99 ÷ 0.25 =
  $4,203.96 an acre. KR172 $1,249.99 ÷ 0.5 = $2,499.98 an acre. KR172 at the dealer figure $1,699.99 ÷ 0.5 =
  $3,399.98 an acre. Mammotion $1,799.00 ÷ 0.37 = $4,862.16 an acre. The $199.00 step from the quarter-acre
  Kress to the half-acre one buys 0.25 acre more rating.
- **The two acreage figures are not the same quantity, and the article must say so.** Kress prints area by
  cadence — 0.5 acre if it cuts every 48 hours, 0.7 acre at 72 — while Mammotion prints area per charge —
  0.12 acre on a 6.1 Ah pack for a 0.37 acre rating, which is 3.1 charges for one full pass of its own rated
  area. Neither number is a field measurement; they cannot be subtracted from each other.
- **Navigation is the axis that changes the buy, and both sides admit the dependency in their own words.**
  Kress markets "No antennas. No beacons. No boundary wires." and, in the same feature list, "Dead reckoning
  for mowing even undershade (weak satellite signal)"; the box still contains an RTK antenna, and the brand
  tells buyers to "Verify the coverage at your local dealer" for its network. Mammotion markets "No Wire, No
  Antenna: 360° LiDAR + Dual Camera AI Vision". Report what each depends on; do not claim a measured
  performance difference under canopy, because no source here measures one.
- **Slope and noise as published claims, labelled.** Kress 40% maximum slope and 59 db perceived; Mammotion
  80% and a "<65 dB" ceiling. A ceiling is not a measurement and "perceived" is not a sound-lab number.
- **The trap is the anchor, not the discount.** The promotion's "regular" figure is $700 above the model
  page's regular figure for the same machine, which makes "Save $1,499.99" a headline about an anchor rather
  than about the price. The offer also carries "while supplies last", a dealer-only channel, and a
  December 31, 2026 end date — none of which the banner leads with.
- **Mandatory honesty paragraph:** built from manufacturer spec and price pages, two authorized dealers'
  listings, and one independent review roundup's tested field; the units were not handled here, no unit was
  installed, and no cutting or navigation performance was measured by this desk.
- **No Review or AggregateRating schema.** `Product` + `Offer` with price and `priceValidUntil`, or a plain
  `ItemList`.
- **Verdict-block links:** the vertical hub https://wellroost.com/categories/yard-robotics/ and the ownership
  calculator https://wellroost.com/calculators/true-cost-of-ownership/ — both probed HTTP 200 on 2026-11-01.
  There is no yard-robotics-specific calculator on the front; do not invent one.

## Gate result

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=22 products=3 fetched=22 hosts=5 price_as_of=2026-11-01 checked_at=2026-11-01T14:06:30+00:00 -->
<!-- review-gate:end -->
