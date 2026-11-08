# Review brief — yard_robotics — 2026-11-08

**Vertical:** yard_robotics
**Persona:** homeowner_pro
**Decision the reader is facing:** whether the $2,799 spent this month on a wire-free robot mower for a fenced one-acre lawn should go to the unit rated for the acre or the unit that covers more ground per charge, and what that choice does to the hours the machine spends working.
**Format:** comparison
**Price as of:** 2026-11-08
**Verdict:** Buy the Segway Navimow X350 at $2,799.00 for a fenced acre — it is the only one of the two rated for a full acre, it runs at 60 dB(A) and it ships its RTK antenna — while the Mammotion LUBA 3 AWD 3000 at the same $2,799.00 wins only on a lot of 0.75 acre or less with a bank past 27 degrees or a canopy that breaks the satellite fix, where its 38.6-degree slope rating and its LiDAR are the point.
**De-dup:** `2026-11-01_one-mower-two-prices-450-apart` compared a Kress KR172 and a LUBA mini 2 in the 0.3-0.5 acre class and priced a dealer promotion; `2026-10-24_your-1-acre-mowers-04-acre-trap` set the rated-versus-usable acreage rule on a Husqvarna with no price comparison. Neither prices these two units, neither is a same-price head-to-head, and neither computes dock-to-dock time per pass. A corpus grep for X350, LUBA 3, X315 and X330 returns no artifact.
**Thesis:** The acreage rating on the badge is a duty-cycle claim, not a capacity claim: at the same $2,799 the mower rated for 1.5 acres covers 0.30 acre per charge while the one rated for 0.75 acre covers 0.42, so the cheaper mower per rated acre is the slower one per hour of cutting, and its own rating is only reachable by running most of a day.

| Product | Price | Source | Note |
|---|---|---|---|
| Segway Navimow X350 | $2,799.00 | https://navimow.com/products/segway-navimow-x350 | 1.5 acre recommended area; 200 min full-charge mowing time; 80 min charge; 60 dB(A); 50% (27°) slope; cart open |
| Mammotion LUBA 3 AWD 3000 | $2,799.00 | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 0.75 acre; 215 min runtime; 0.42 acre per charge; 80% (38.6°) slope; cart open |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Navimow — X350 product page (model price list) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | $2,799 | vendor: "Navimow X330 $2,299.00 Navimow X350 $2,799.00"; cart open, "Add to cart" |
| 2 | Navimow — X350 product page (spec table, recommended area) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 1.5 acres | vendor: "Recommended Mowing Area … 1.5 acres", the X350 column of the X3 comparison table |
| 3 | Navimow — X350 product page (spec table, full-charge mowing time) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 200 min | vendor: "Full Charge Mowing Time 160 min 200 min 240 min" across the X3 series |
| 4 | Navimow — X350 product page (spec table, charging time) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 80 min | vendor: "Charging Time 65 min 80 min 100 min" across the X3 series |
| 5 | Navimow — X350 product page (notes, laboratory coverage) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 0.3 acres | vendor: "80 minutes of charging provides up to 200 minutes of operating time for coverage of up to 0.3 acres"; lab test, not field |
| 6 | Navimow — X350 product page (spec table, slope) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 27° | vendor: "Maximum Slope Ability 50% (27°)"; boundary limit 25% (14°) on the same row |
| 7 | Navimow — X350 product page (spec table, weight) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 43.7 lbs | vendor weight for the 1.5-acre column |
| 8 | Navimow — X350 product page (spec table, noise) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 60 dB(A) | vendor: "Noise Level 60 dB(A)", footnoted as standard mode |
| 9 | Navimow — X350 product page (X3 accessories) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | $399.99 | vendor: "Navimow Battery 10Ah for X350 / H220 $399.99" — the replacement pack |
| 10 | Navimow — X350 product page (X3 accessories) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | $59.99 | vendor: "Anti-clogging Cutting Disk for X3 Series $59.99" |
| 11 | Navimow — X350 product page (notes, mapping area) | https://navimow.com/products/segway-navimow-x350 | 2026-11-08 | 1.2× | vendor: "Supports map storage up to 1.2× the recommended mowing area (e.g. up to 1.2 acres for a 1-acre model)" |
| 12 | Mammotion — LUBA 3 AWD product page (price block) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | $2,799 | vendor: "LUBA 3 AWD 3000 | 0.75 acre / Standard Version … $2,799.00", "Add to Cart" present; the 1500 and 5000 variants read "Out of Stock" |
| 13 | Mammotion — LUBA 3 AWD product page (model rating) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 0.75 acre | vendor: "LUBA 3 AWD 3000 | 0.75 acre" |
| 14 | Mammotion — LUBA 3 AWD product page (battery section) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 215 minutes | vendor: "21.6V 15Ah lithium battery, delivering up to 215 minutes of runtime per charge" |
| 15 | Mammotion — LUBA 3 AWD product page (battery section) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 0.42 acre | vendor: "covering up to 1700㎡ (0.42 acre) with stable performance" |
| 16 | Mammotion — LUBA 3 AWD product page (drive section) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 38.6° | vendor: "All-Wheel Drive for 80% (38.6°) Slopes" |
| 17 | Mammotion — LUBA 3 AWD product page (design section) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 41 lbs | vendor: "41 lbs Lightweight Design"; the same section states 19 kg |
| 18 | Mammotion — LUBA 3 AWD product page (battery capacity) | https://us.mammotion.com/products/luba-3-awd-robot-lawn-mower | 2026-11-08 | 1700 | vendor metric coverage figure behind the 0.42-acre claim |
| 19 | Kress — robotic lawn mower listing (KR173 row) | https://www.kress.com/en-us/robotic-lawn-mowers | 2026-11-08 | $1,499.99 | vendor: "KR173 Kress RTKⁿ ¾-acre robotic lawn mower with OAS … $2,999.99 $1,499.99" |
| 20 | Kress — dealer promotion page (KR173 row) | https://www.kress.com/en-us/robotic-mowers | 2026-11-08 | $1,999 | vendor: "Only $1,999.99" for the KR173, against "$3,699.98" struck through; terms "Offer valid through December 31, 2026 … At participating Kress dealer only" |
| 21 | Kress — robotic lawn mower listing (KR173 anchor) | https://www.kress.com/en-us/robotic-lawn-mowers | 2026-11-08 | $2,999.99 | the regular price the listing strikes through, $700 under the promotion page's anchor for the same model |
| 22 | HomeGuide — 2026 lawn mowing cost guide (price by yard size) | https://www.homeguide.com/costs/lawn-mowing-cost/ | 2026-11-08 | $60 | publisher's table: 1 acre, weekly, "$60 – $100" per visit |
| 23 | HomeGuide — 2026 lawn mowing cost guide (price by yard size) | https://www.homeguide.com/costs/lawn-mowing-cost/ | 2026-11-08 | $100 | the top of the same weekly 1-acre band |
| 24 | HomeGuide — 2026 lawn mowing cost guide (annual packages) | https://www.homeguide.com/costs/lawn-mowing-cost/ | 2026-11-08 | 25 to 35 | publisher: annual packages "typically include 25 to 35 visits per season" |
| 25 | The Gadgeteer — X350 review (measured cycle) | https://the-gadgeteer.com/2025/06/05/segway-navimow-x350-robotic-lawn-mower-review-are-we-living-in-the-future | 2026-11-08 | 200 minutes | reviewer: "Mowing time between full charges is 200 minutes (covering appx 1.5 acres)" — the reviewer reads the rating as per-charge coverage; Navimow's own note (row 5) puts the same 200 minutes at 0.3 acre |

## What the article must carry

- **State the pick in the first two sentences, then the one case where the other unit wins.** No throat-clearing, no
  "in today's market". The reader's lot size decides between them, so say which size goes where.
- **The duty-cycle finding, with the arithmetic shown.** Both machines list at $2,799.00 on 2026-11-08. Navimow's own
  laboratory note puts 200 minutes of cutting at 0.3 acre, against a 1.5-acre recommended area: 1.5 ÷ 0.3 = **5 charge
  cycles** for one pass of the rated lawn, and at 200 minutes cutting plus 80 minutes charging that is 5 × 280 = **1,400
  minutes, about 23 hours**, of dock-to-dock time. Mammotion's page puts 215 minutes at 0.42 acre against a 0.75-acre
  rating: 0.75 ÷ 0.42 = **1.8 cycles**. Per hour of cutting, 0.3 acre in 3.33 hours is about **3,920 square feet an
  hour**; 0.42 acre in 3.58 hours is about **5,105**. Show the division, not just the totals, and label every figure as
  the maker's own claim.
- **Price per rated acre, computed not estimated.** $2,799.00 ÷ 1.5 = **$1,866.00** an acre for the X350;
  $2,799.00 ÷ 0.75 = **$3,732.00** for the LUBA 3 AWD 3000. Say plainly that the cheaper number per acre belongs to the
  slower machine, and why the two ratings are not the same quantity.
- **The reviewer misreading is the best evidence for how the badge misleads.** The Gadgeteer's review reads the 200
  minutes as covering "appx 1.5 acres"; Navimow's own note puts those same 200 minutes at 0.3 acre. Put both sentences
  in the piece, attribute each, and let the reader see that a rating is a daily duty cycle rather than a tank of range.
  Do not accuse the reviewer — the two documents simply disagree about what the number measures.
- **Three axes that change the buy, each with its numbers then its consequence:** (1) coverage per charge and time per
  pass, above; (2) slope, 50% (27°) for the X350 against 80% (38.6°) for the LUBA, with Navimow's own boundary limit of
  25% (14°) noted — a lot with a bank past 27 degrees is a LUBA lot; (3) navigation, where the X350 ships an RTK antenna
  and Navimow markets network RTK coverage as something to check for your address, while Mammotion's LUBA 3 pairs 360°
  LiDAR with iNavi NetRTK over a built-in 4G module that is free for three years.
- **The trap: neither is antenna-free at this acreage, and the cheap number is a subscription later.** Mammotion's page
  offers "Click Here to Renew the Subscriptions of MAMMOTION 4G Service" and prints no renewal price, so the recurring
  cost is unquantified — write that as a stated gap, never as a number. Navimow's own spec table lists 4G (3 Years Free)
  on the X3 line; the X350 also carries the antenna in the box, which is a mast and a cable run in the yard.
- **Ownership cost, priced only where a price exists.** Navimow prints a replacement 10Ah pack at $399.99 and an
  anti-clogging cutting disk at $59.99 for the X3 series; Mammotion's page prints no battery or blade price for the LUBA 3
  and no 4G renewal price, so the honest line is that its consumable schedule is unpublished rather than cheap.
- **The contract benchmark, from the publisher's own table, not a guess.** One acre weekly runs $60 to $100 a visit;
  twenty-six weekly visits (the desk's own season length, stated as an assumption) is $1,560 to $2,600 a season. So
  $2,799 is about **1.1 to 1.8 seasons** of the contract it replaces. Say that the first-year case is not a saving and
  that the trade is the hours, not the money.
- **The Kress caveat, one paragraph, because a 0.75-acre reader should see it.** Kress's own mower listing sells the
  ¾-acre KR173 with obstacle avoidance at $1,499.99 against $2,999.99 regular on 2026-11-08, while its dealer promotion
  page lists the same model at $1,999.99 against $3,699.98 — two of the maker's own pages, $500 apart, dealer channel
  only, offer stated to run through 31 December 2026 while supplies last. Report both numbers, and say the quote is the
  price.
- **Honesty paragraph, mandatory and specific:** the comparison is built from the two makers' own product and price
  pages, one publisher's cost table and two independent reviews; the desk did not handle, install or measure either
  machine, and every runtime, coverage and slope figure in the piece is the maker's claim or a division of one.
- **No Review or AggregateRating schema.** `Product` + `Offer` with price and `priceValidUntil`, or a plain `ItemList` —
  nothing here was rated by this desk.
- **Verdict-block links:** the vertical hub https://wellroost.com/categories/yard-robotics/ and the ownership calculator
  https://wellroost.com/calculators/true-cost-of-ownership/ — both probed HTTP 200 on 2026-11-08. There is no
  yard-robotics-specific calculator on the front; do not invent one.

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=25 products=2 fetched=25 hosts=5 price_as_of=2026-11-08 checked_at=2026-11-08T14:06:15+00:00 -->
<!-- review-gate:end -->
