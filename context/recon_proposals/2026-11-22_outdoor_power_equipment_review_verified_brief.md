# Verified Brief: outdoor_power_equipment — 2026-11-22

Review run (`skills/review_comparison.md`), format `comparison`, three battery snow machines.
Claim extraction from `context/recon_proposals/2026-11-22_outdoor_power_equipment_review_brief.md`
(18 evidence rows, all fetched by `scripts/review_gate.py` on 2026-11-22 — gate PASS, 5 hosts).

**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** which battery snow machine to buy for a large driveway before the first storm — an $849 single-stage 21-inch Ryobi kit, a $1,599 Toro 60V 24-inch two-stage, or a $2,499.99 Greenworks 80V MAXIMUS 24-inch two-stage — and whether the $1,650 premium to the top of the class buys anything the mid-tier machine does not already do.
**Format:** comparison
**Price as of:** 2026-11-22
**Verdict:** Buy the Toro 24 in. Power Max e24 (model 39925) at $1,599 for most large driveways: its 24-inch cut, 20-inch intake height and three battery ports clear the same 24-inch path as the Greenworks MAXIMUS kit at $900 less, and every battery port is another evening's worth of clearing. Buy the Greenworks 80V MAXIMUS (MSN240TN3) only where a dealer-network service contract and the 4-year battery warranty matter more than the $900; buy the Ryobi 40V HP 21-inch single-stage (RY40HPSN02K2) at $849 only for a driveway shorter than the reach of its 35-foot throw, where its 11.5-inch depth is enough and the two-stage class's $750+ entry premium does not pay.
**De-dup:** `2026-11-08_your-150-snow-shovels-6-inch-trap` is this vertical's last review and prices a corded Snow Joe SJ627E against a Toro Power Shovel — plug-in machines, no battery in either; `2026-11-21_your-899-blowers-9-day-window` is news about an EGO kit discount window, not a machine-to-machine comparison, and it prices the EGO 21-inch single-stage kit, not a two-stage; `2026-11-22_your-snow-cores-1300-apart` is yard_robotics' review of a $4,899 robot snow platform, not a homeowner-pushed machine. A corpus grep for "Power Max e24", "MAXIMUS" and "RY40HPSN" across `published/`, `context/drafts/` and `context/recon_proposals/` returns only this brief; no artifact prices a battery two-stage push-machine comparison.
**Thesis:** In the battery snow class the deciding number is not clearing width — all three machines cut within 3 inches of each other — it is intake height and where the batteries go: the single-stage takes 11.5 inches of snow per pass, the two-stage pair takes 20 and 18 inches, and the $1,650 spread between the cheapest and dearest kits buys almost no width, only depth, mass and battery capacity. The class charges three prices for roughly one 24-inch promise, and the mid-tier machine is priced where the promise is actually delivered.

| Product | Price | Source | Note |
|---|---|---|---|
| Toro 24 in. Power Max e24 60V (39925, 10.0Ah kit) | $1,599 | https://www.toro.com/en/product/39925 | 24-inch cut, 20-inch intake, up to 20 car spaces on one charge; the maker lists $1,599.00 and routes to retailers |
| Greenworks 80V MAXIMUS 24" two-stage kit (MSN240TN3, 2×4.0Ah) | $2,499.99 | https://www.greenworkstools.com/products/80v-24-cordless-battery-two-stage-snow-blower-kit-msn240tn3 | 24-inch cut, 18-inch depth, 176.4 lbs, open cart on the maker's own store |
| Ryobi 40V HP 21" single-stage kit (RY40HPSN02K2, 2×8Ah) | $849 | https://www.ryobitools.com/products/46396054982 | 21-inch width, 11.5-inch depth, auger-propelled single-stage — the class floor, not a two-stage |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Toro — 39925 product page, price block | https://www.toro.com/en/product/39925 | 2026-11-22 | $1,599.00 | the maker's listed price, printed as "$1,599.00 USD" beside "Model: 39925"; page is flagged "Retailer Sale Item" and routes to retailers |
| 2 | Toro — 39925, key features | https://www.toro.com/en/product/39925 | 2026-11-22 | clear up to 20 car spaces | "can easily clear up to 20 car spaces on one charge" — vendor-rated |
| 3 | Toro — 39925, key features: intake | https://www.toro.com/en/product/39925 | 2026-11-22 | 20-inch intake height | "With our 24-inch clearing width and 20-inch intake height" |
| 4 | Toro — 39925, key features: ports | https://www.toro.com/en/product/39925 | 2026-11-22 | add another 4 to 20 car spaces | "with a second and third battery slot, you can add another 4 to 20 car spaces" — three ports total |
| 5 | Greenworks — MSN240TN3 product page, price | https://www.greenworkstools.com/products/80v-24-cordless-battery-two-stage-snow-blower-kit-msn240tn3 | 2026-11-22 | 2,499.99 | list price token in the page's price markup; the cart is open ("Get it by: Wed, Nov 25th") |
| 6 | Greenworks — MSN240TN3, specs: cut | https://www.greenworkstools.com/products/80v-24-cordless-battery-two-stage-snow-blower-kit-msn240tn3 | 2026-11-22 | Cleaning width: 24” / Cleaning depth: 18” | vendor spec table |
| 7 | Greenworks — MSN240TN3, specs: throw | https://www.greenworkstools.com/products/80v-24-cordless-battery-two-stage-snow-blower-kit-msn240tn3 | 2026-11-22 | discharges up to 50 ft. | "Chute rotates 200 degrees and discharges up to 50 ft. in distance" — vendor-rated |
| 8 | Greenworks — MSN240TN3, specs: weight and warranty | https://www.greenworkstools.com/products/80v-24-cordless-battery-two-stage-snow-blower-kit-msn240tn3 | 2026-11-22 | Product Weight 176.4lbs | same page carries "Product Warranty 5-year" and "Battery Warranty 4-year" |
| 9 | Greenworks — 80V 5.0Ah replacement pack | https://www.greenworkstools.com/products/80v-gen-2-2-5-ah-lithium-ion-battery | 2026-11-22 | 329.99 | spare-pack price on the maker's own store, open cart |
| 10 | Ryobi — RY40HPSN02K2 product page, price | https://www.ryobitools.com/products/46396054982 | 2026-11-22 | $849.00 | list price of the kit variant "(2) 8Ah Battery/Charger"; Add to Cart is live |
| 11 | Ryobi — RY40HPSN02K2, specs: cut | https://www.ryobitools.com/products/46396054982 | 2026-11-22 | 21” WIDTH & 11.5” DEPTH | vendor spec block |
| 12 | Ryobi — RY40HPSN02K2, specs: throw | https://www.ryobitools.com/products/46396054982 | 2026-11-22 | Clearing Distance Up to 35' | vendor-rated spec table |
| 13 | Ryobi — RY40HPSN02K2, specs: coverage and weight | https://www.ryobitools.com/products/46396054982 | 2026-11-22 | Clears up to 25 Car Spaces Using Included (2) 40V 8Ah Batteries | same page: "Weight 59.4 lbs.", 5-year tool / 3-year battery warranty |
| 14 | Pro Tool Reviews — EGO 56V 2-stage review (class reference) | https://www.protoolreviews.com/ego-2-stage-snowblower | 2026-11-22 | Price: $799.99 bare, $1299.99 kit | publisher-recorded EGO SNT2405 pricing — the independent two-stage benchmark the class prices itself against; EGO's own kit was not fetchable at a live price on 2026-11-22, so it is cited as the reference point, not a fourth buy |
| 15 | Pro Tool Reviews — EGO 56V 2-stage, measured runtime | https://www.protoolreviews.com/ego-2-stage-snowblower | 2026-11-22 | The same 6 driveways with powdery snow and low auger speed only used 20-30% of the battery! | measured by the publisher — the class's real-world runtime anchor |
| 16 | Family Handyman — EGO snow blower review | https://www.familyhandyman.com/article/ego-snow-blower-review | 2026-11-22 | 24-car driveway with 8 inches of snow | publisher-reported vendor claim; note the same maker claim is phrased "18-car" on EGO's own page — the class's coverage claims are not measured on a shared yardstick |
| 17 | Pro Tool Reviews — best Greenworks snow blowers | https://www.protoolreviews.com/best-greenworks-snow-blower-reviews | 2026-11-22 | It can clear 18-inch snowfalls and fling snow up to 50-feet using its 200-degree articulating discharge chute. | publisher-verified spec for the Greenworks 80V 24" two-stage |
| 18 | Pro Tool Reviews — best Greenworks snow blowers, price | https://www.protoolreviews.com/best-greenworks-snow-blower-reviews | 2026-11-22 | This one is $2499.99 with two 5.0Ah batteries and a charger. | publisher-recorded kit price, matching the live vendor price on the 4.0Ah kit |

## Derived arithmetic (computed from printed endpoints, never estimated)

- **Dollars per inch of clearing width.** $849 ÷ 21 = **$40.43**; $1,599 ÷ 24 = **$66.63**; $2,499.99 ÷ 24 = **$104.17**. The width ladder *rises* with price — the price is not buying width.
- **Dollars per inch of intake depth.** $849 ÷ 11.5 = **$73.83**; $1,599 ÷ 20 = **$79.95**; $2,499.99 ÷ 18 = **$138.89**. Depth is also nearly flat from Ryobi to Toro, then doubles at the top — the MAXIMUS premium buys mass and warranty, not depth per dollar.
- **The pass-count cliff.** A 10-inch storm: the Ryobi takes one pass per 11.5 inches and a second sweep for the remainder; the Toro and Greenworks intakes take it in one. In a 16-inch storm the single-stage needs two full passes, the two-stage pair still one.
- **Throw geometry.** 35 ft (Ryobi) vs 50 ft (both two-stages, vendor-rated): the single-stage can only clear what it can throw within its own width — a 21-inch path at 35 feet of arc is a cone that ends near the driveway edge on a wide lot.
- **Battery amortization.** A spare 80V 5.0Ah pack is **$329.99** — 13.2% of the MAXIMUS kit's price. At the class's $799.99 bare / $1,299.99 kit split (Pro Tool Reviews), a two-pack difference is a whole single-stage battery kit.

## What the article must carry

- **Width is the decoy spec.** All three cut 21–24 inches. Rows 3, 6, 11: the real axis is intake depth — 11.5 in vs 20 in vs 18 in — because depth sets how many passes a single storm takes, and passes are the winter's actual labor.
- **The three prices are one promise.** $849 → $1,599 → $2,499.99 for paths within 3 inches of each other (rows 3, 6, 11). The arithmetic section shows width per dollar *rises*; say plainly what the premium buys instead: self-propel, ports, mass, warranty and throw.
- **Battery ports are the runtime ladder.** Row 4: the Toro has three ports and the maker prices each at "another 4 to 20 car spaces". Ryobi runs two 8Ah packs. The Greenworks kit carries two 4.0Ah with a third port. Runtime is expandable, not fixed — say the kits' claimed coverage (rows 2, 13) is a vendor rating under the packs in the box.
- **Coverage claims are not measured on a shared yardstick.** Rows 2, 13 use car spaces; the Greenworks publisher row (17) uses 3,000 sq ft and 18-inch snowfalls; the EGO reference is phrased 18-car on the maker's page and 24-car in Family Handyman's retelling (row 16). The article must refuse a single-coverage ranking and compare pass counts instead.
- **The trap is the spare pack.** Row 9: $329.99 — one-eighth of the MAXIMUS kit — for one more evening. A two-stage kit without a third pack is a half-machine in February; price the pack into the platform decision.
- **Label the honest ceiling of the evidence.** Row 14–16: Pro Tool Reviews measured the EGO sibling of this class, not the machines in the table. Every capacity figure for the three products here is vendor-rated. Say so once, clearly.
- **Verdict by situation**, not a single ranking: a drive with two-car plow windrows and >16-inch events (Toro); a buyer who wants the longest warranty and will pay for it (Greenworks); a short drive, lighter storms, and budget as the deciding constraint (Ryobi — with the intake-height consequence stated, not softened).
- **Mandatory honesty paragraph:** this review is built from three manufacturer product pages, one maker's spare-pack store page and two independent publishers (Pro Tool Reviews, Family Handyman); the desk did not run, push or measure any of the machines, and every capacity figure is a vendor rating except where a publisher is named. No Review or AggregateRating schema — `Product` + `Offer` with the price and `priceValidUntil`, or a plain `ItemList`.
- **Verdict block links:** the vertical hub https://wellroost.com/categories/outdoor-power-equipment/ and the live ownership calculator https://wellroost.com/calculators/true-cost-of-ownership/ (both probed HTTP 200 on 2026-11-08; re-probe before the push). There is no snow-specific calculator on either front; do not invent one.
- **One earned inline internal link** in the body, site-relative, from the live corpus; justified targets: `/your-899-blowers-9-day-window/` (the EGO buy-window news already on the front) or the vertical hub.

## Drafter rulings (labels the article must keep)

1. Prices are the makers' and retailers' printed prices on 2026-11-22. Toro lists $1,599.00 and routes the buyer to retailers (its own page is flagged "Retailer Sale Item"), so say a dealer may price it differently; Greenworks and Ryobi sell direct at the prices in the table.
2. The Ryobi machine is a single-stage auger-propelled unit and must never be described as a two-stage. Its role in the piece is the class floor the two-stage premium is measured against.
3. Pounds per minute, throw distance, car spaces and square-foot coverage are vendor claims under vendor conditions — label each on use. The only measured runtime in the table belongs to Pro Tool Reviews, and it is for the EGO sibling, not the three machines compared.
4. The EGO SNT2405 has no verified live price today and no fourth product is admitted. It appears only as the publisher-recorded class reference, priced as of the publisher's review, never as a current buy.
5. The article must not imply use: no first-person claim that a machine was run, measured, tried or owned, and no claim of time spent with one. It says what the pages publish, what the publishers measured, and that nothing was handled.
6. Do not rank the three machines on any single "power" number. The makers publish under different yardsticks (car spaces, square feet, inches), which is why the article compares intake depth and pass counts instead.
7. The 13.2% spare-pack share is the article's arithmetic on the printed $329.99 and $2,499.99, attributed as arithmetic. The two-stage sibling prices ($799.99 bare / $1,299.99 kit) are Pro Tool Reviews' published figures, labeled as such.

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=18 products=3 fetched=18 hosts=5 price_as_of=2026-11-22 checked_at=2026-11-22T14:46:24+00:00 -->
<!-- review-gate:end -->
