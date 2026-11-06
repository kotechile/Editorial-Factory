# Evergreen Brief: consumer_asset_repair_replace_tco — 2026-11-06
**Archetype:** evergreen
**Vertical:** consumer_asset_repair_replace_tco
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** A three-year-old phone holds a charge through the morning and reports a battery that is no longer new. Decide whether to buy a replacement battery — and how many more years of use that actually buys — or to put the money toward a new handset, at the moment the battery health number stops looking healthy.

**Durability:** What stays true is the rule, not the price: a lithium battery's service life is published as a cycle count (80% of original capacity at a stated number of full cycles), so any reader can convert their own charging habit into years without trusting a reviewer's vibes. The rated counts are spec-page facts as of 2026-11-06 — 500 full cycles for the iPhone generations through the 14, 1000 from the iPhone 15, 1000 for Mac laptops — and the EU's 800-cycle floor applies to smartphones and slate tablets placed on the EU market from 20 June 2025 onward, a date fixed in the regulation. The prices are dated list prices as of 2026-11-06 (Apple's out-of-warranty battery service as tabulated by iFixit, and iFixit's own kit prices), and the article prints each one with its date and source, so a reader re-running the same division with next year's prices gets a correct answer.

**De-dup:** `2026-10-30_your-ink-plan-bills-20-cents` is this vertical's nearest prior evergreen artifact (consumables priced per printed page, with an overage and a tank break-even), and `2026-10-30_your-screen-gap-999-vs-99` is the same day's news piece, which priced Apple's *insured-versus-cash service ladder* for a screen and a fold. Neither touches a cycle rating: this brief is about the published **service life of the battery part** — 500 cycles on one generation, 1000 on the next, 800 as the EU floor — and the decision that follows from it (swap the part, keep the machine), with no screen, no plan comparison and no consumable-per-page arithmetic. `2026-10-23_why-your-fridge-upgrade-pays-12-50` prices an appliance's *energy* annuity against a repair hour and `2026-10-23_your-cheap-part-a-599-bill` prices a wearable's service ladder, so the vertical has never argued a battery's rated life. Cross-corpus check by hand, as the SOP requires: `grep -ril "charge cycle\|cycle count\|battery health" published/` returns six artifacts, and every one is about something else — a snow-thrower pack, a robotic mower's runtime, an inventory cycle-count method — with no article on a phone or laptop battery's rated cycle life in any vertical.

**Thesis:** The battery is the only part of a phone with a printed expiry, and the number is small — 500 full cycles through the iPhone 14 generation, twice that from the iPhone 15, and 800 as the EU's new minimum — so the third year of a handset is a $47-to-$99 part, not a new machine, and the cycle rating on the spec page is the number that decides which.

**Lead:** The vertical's own beats — `primary_angles[3]`, "battery and screen replacement economics against trade-in credit and refurbished substitution" — read on the battery side, which the vertical has never covered (the 2026-10-30 news run priced screens and the insured ladder; the 2026-10-30 evergreen priced ink). The persona's `wants` ("tinkering tax audits", "anti-subscription creep") make the reader the person who wants the wear part's clock, not a brand's upgrade pitch. Two vendors state the whole decision without either stating it: Apple publishes one cycle rating per device class on its battery page, and iFixit publishes the same rating beside a *duration* ("roughly 18-24 months") and a kit price. `gsc_analyzer.py` carries 0 query opportunities for this vertical today (young site, thin impressions) — bonus signal only, no veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Apple — Batteries: Service and Recycling (iPhone owners) | https://www.apple.com/batteries/service-and-recycling/ | 2026-11-06 | 500 — iPhone 14 models and earlier are designed to retain 80% of their original capacity at 500 complete charge cycles | vendor claim (manufacturer spec) |
| 2 | Apple — Batteries: Service and Recycling (iPhone owners) | https://www.apple.com/batteries/service-and-recycling/ | 2026-11-06 | 1000 — iPhone 15 models are designed to retain 80% of their original capacity at 1000 complete charge cycles | vendor claim (manufacturer spec) |
| 3 | Apple Support — Apple Service and Repair for iPhone (AppleCare battery service) | https://support.apple.com/iphone/repair | 2026-11-06 | 80% — We'll replace the battery for no extra charge if the capacity drops below 80% | vendor claim (plan term) |
| 4 | iFixit — iPhone 12 Battery Replacement guide (introduction) | https://www.ifixit.com/Guide/iPhone+12+Battery+Replacement/140588 | 2026-11-06 | 500 — iPhone batteries are rated to hold 80% of their capacity for up to 500 charge cycles, which lasts roughly 18-24 months for most users | vendor claim (repair vendor, third-party) |
| 5 | iFixit — iPhone 15 Battery Replacement guide (introduction) | https://www.ifixit.com/Guide/iPhone+15+Battery+Replacement/165733 | 2026-11-06 | 1000 — iPhone batteries are rated to hold 80% of their capacity for up to 1000 charge cycles | vendor claim (repair vendor, third-party) |
| 6 | iFixit — iPhone Battery Replacement: Costs and Considerations (cost table) | https://www.ifixit.com/Wiki/iPhone_Battery_Replacement | 2026-11-06 | 46.99 — iFixit's iPhone 12 battery kit costs $46.99, against Apple's $89 out-of-warranty service for the same model | vendor claim (kit price + cited service price) |
| 7 | iFixit — iPhone 15 Battery (product page) | https://www.ifixit.com/products/iphone-15-battery | 2026-11-06 | 49.99 — iPhone 15 Battery Fix Kit price | vendor claim (list price) |
| 8 | European Commission — Smartphones and Tablets (ecodesign product page) | https://energy-efficient-products.ec.europa.eu/product-list/smartphones-and-tablets_en | 2026-11-06 | 800 — batteries must withstand at least 800 charge and discharge cycles while retaining at least 80% of their initial capacity | regulation (applies from 20 June 2025) |

## Arithmetic the brief fixes for the drafter (recompute from the rows, never round-trip through the draft)

- At one full cycle a day, a 500-cycle rating is **500 days = 1.37 years**; a 1000-cycle rating is **2.74 years**; the EU's 800-cycle floor is **2.19 years**.
- At one full cycle every other day, the same ratings run **2.74 / 5.48 / 4.38 years**.
- iFixit's own gloss on the 500-cycle rating is **18 to 24 months**, i.e. **1.5 to 2.0 years** — the same order as the daily-cycle arithmetic and the vendor's own words, so the article uses the vendor's range and shows the division beside it.
- Kit cost per rated cycle: **$46.99 ÷ 500 = $0.094** (iPhone 12 kit) and **$49.99 ÷ 1000 = $0.050** (iPhone 15 kit). Apple's service per rated cycle: **$89 ÷ 500 = $0.178** (iPhone 12) and **$99 ÷ 1000 = $0.099** (iPhone 15, Apple's figure via iFixit's table).
- Cost of buying one more rated life: **$46.99 to $99** against a handset price the brief deliberately does not print (no primary handset price survived the verifier on the shop pages), so the comparison is stated as a share: the part is **5.3 percent of a $900 handset** and **9.4 percent of a $500 one**, computed only if the draft names a handset price from a cited page — otherwise it stays in per-cycle and per-year terms.
- Annualised: **$46.99 over 2.0 years = $23.50 a year**; **$49.99 over 2.74 years = $18.25 a year**; **$89 over 1.37 years = $64.96 a year** (the expensive path: paying Apple's 500-cycle-model service at the daily-cycle rate).
- The gap between the two published ratings is **2x** (500 to 1000), and the EU floor sits at **1.6x** the old one and **80 percent** of the new one.

## Rulings the drafter must respect

1. **Never say the battery was "designed to fail".** The ratings are published service-life specs, and the article's claim is narrower and checkable: the part's rated life is *stated*, and it is shorter than the phone's software life on the older generation.
2. **The 500-to-1000 jump is a change in the published rating, not a proven change in chemistry.** Apple's page states both numbers and explains neither; iFixit's guides repeat both. Write "the rating doubled between generations", never "the battery got twice as durable".
3. **iFixit's "18-24 months" is a repair vendor's gloss, not a measurement** — attribute it to iFixit and keep Apple's cycle count as the primary number.
4. **Apple's service prices come from iFixit's table, not from Apple's own page**, because Apple's service-cost module loads client-side and the verifier reads "Pricing failed to load" instead of a figure. Attribute those prices to iFixit's table and say so.
5. **No handset price is printed unless a cited page carries one.** The Apple shop pages do not expose a price token to the verifier, so the article compares in per-cycle and per-year terms instead of inventing a ₹/$/€ sticker.
6. **The EU row is a comparator, not a claim about the reader's device.** It applies to products placed on the EU market from 20 June 2025; say that, and do not imply a US-sold phone meets or misses it.

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The battery's rated cycle life: 500 vs 1000, the EU's 800 floor, and the $47 swap | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Extended-warranty math versus self-insuring an appliance failure | 9 | 7 | 5 | 8 | 7.3 | dropped — still no fetchable primary plan price for an appliance plan, and the 2026-10-30 news piece already priced an insured ladder against a cash one |
| Espresso-machine cost per shot against descaling and gasket cycles | 8 | 8 | 5 | 8 | 7.2 | dropped — descaling and gasket prices live on retailer and repair-shop pages the verifier refuses (confirmed again this run) |
| Right-to-repair parts-availability duty (how many years a maker must stock a part) | 8 | 9 | 7 | 6 | 7.6 | dropped — the only fetchable statement of the duty is the EU's 7-year rule, which binds the EU market and says nothing about the reader's device; the US state statutes remain unfetchable |
| Trade-in credit versus a refurbished substitution | 8 | 7 | 4 | 7 | 6.5 | dropped — trade-in and refurbished prices render client-side; no verified figure survived probing |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=8 fetched=8 sources=7 hosts=4 decision="sha1:b03a5d8a4d" dedup="matched a prior artifact: 2026-10-30_your-ink-plan-bills-20-" window_days=180 checked_at=2026-11-06T19:34:47+00:00 -->
<!-- evergreen-gate:end -->
