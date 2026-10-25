# Review Brief: home_diagnostics_tech — 2026-10-25
**Archetype:** review
**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to spend $34.98 on a pin meter, $49.97 on a pinless meter, or $109.99 on a two-in-one, when the surface that needs checking is finished drywall and neither cheap meter reports a drywall moisture percentage you can threshold.
**Format:** comparison
**Price as of:** 2026-10-25
**Verdict:** Buy the Klein ET150 at $34.98 if the material you are checking is wood or framing — it is the only one of the three whose number is a calibrated percentage in wood, to plus or minus 2%. Buy the Klein ET140 at $49.97 instead if the wall is already painted and you need to sweep without leaving pin holes; buying both costs $84.95, still $25.04 less than the $109.99 Triplett MS150 that carries the same two sensors in one body.
**De-dup:** `2026-10-24_your-250-imager-needs-15-degrees` (home_diagnostics_tech, published) covers the thermal imager's limits and carries no meter price or model; `2026-10-24_home_diagnostics_tech_evergreen_verified_brief` cites moisture only as one of three surface-cooling causes. This vertical's 2026-10-24 evergreen run scored the same pin-versus-pinless candidate at 8.0 and **dropped it** because no second host carried a pinless-accuracy figure; this run clears that floor with manufacturer tables and a building scientist's field write-up, so the subject is now admissible rather than new. A grep of `published/`, `context/drafts/` and `context/recon_proposals/` for "moisture meter", ET140, ET150 and MS150 returns no prior artifact that prices a meter.
**Thesis:** What a homeowner buys with these three meters is a depth and a calibrated scale, not a moisture percentage: the pinless unit reads a relative index to 3/4 inch through whatever sits behind the drywall, the pin unit reads a real percentage only in wood, and the two-in-one charges $25.04 more than buying both cheap meters without adding a drywall-calibrated scale — the scale that a 78-versus-0.3 percent disagreement in a builder's wall shows is the difference between a number you can act on and a number that merely looks alarming.

**Lead:** The vertical's own beats, `context/verticals.json` `primary_angles` #4 ("pin versus pinless moisture meters: the dry-to-the-touch lie on drywall, subfloor and framing"), read at the hour the decision is made: heating season opens, the first cold snap drives interior moisture into cold cavities, and the reader is standing in front of a finished wall that feels dry. GSC for this vertical returned 0 candidates on 2026-10-24 (`context/recon_proposals/2026-10-24_gsc_home_diagnostics_tech_opportunities.md`) — thin impressions on a young site, a non-veto. Prices and specs below are all fetched from the pages named, 2026-10-25.

| Product | Price | Source | Note |
|---|---|---|---|
| Klein ET140 pinless moisture meter | $49.97 | https://hausoftools.com/products/klein-tools-et140-pinless-moisture-meter | pinless, 3/4-inch (1.9 cm) sensing depth, nine LED bars, no holes |
| Klein ET150 pin moisture meter | $34.98 | https://hausoftools.com/products/klein-tools-et150-pin-moisture-meter | 8 mm replaceable pins, 3/8-inch (1 cm) depth, wood to plus or minus 2% |
| Triplett MS150 pin and pinless moisture meter | $109.99 | https://www.triplett.com/products/ms150-pin-pinless-moisture-meter-with-audible-indicator | both sensors in one body, pinless 6 to 99.9% relative, pin 1.5 to 33% building materials |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Haus of Tools — Klein ET140 product page (price block) | https://hausoftools.com/products/klein-tools-et140-pinless-moisture-meter | 2026-10-25 | $49.97 | retailer list price, in stock, free shipping |
| 2 | Haus of Tools — Klein ET150 product page (price block) | https://hausoftools.com/products/klein-tools-et150-pin-moisture-meter | 2026-10-25 | $34.98 | retailer list price, new arrival |
| 3 | Triplett — MS150 product page (price block) | https://www.triplett.com/products/ms150-pin-pinless-moisture-meter-with-audible-indicator | 2026-10-25 | $109.99 | manufacturer direct price |
| 4 | Klein Tools — ET140 specification table | https://www.kleintools.com/catalog/environmental-testers/pinless-moisture-meter | 2026-10-25 | 0.75 | manufacturer spec, sensing depth in inches (1.9 cm); accuracy on the same table is +/-4%, sensor pad 1.25 x 2 inches |
| 5 | Klein Tools — ET150 specification table | https://www.kleintools.com/catalog/environmental-testers/pin-moisture-meter | 2026-10-25 | 0.38 | manufacturer spec, sensing depth in inches (1 cm); accuracy on the same table is wood plus or minus 2%, drywall and masonry stated as relative readings |
| 6 | Klein Tools — ET150 specification table (range row) | https://www.kleintools.com/catalog/environmental-testers/pin-moisture-meter | 2026-10-25 | 0% to 100% Relative Humidity | manufacturer spec, the drywall and building-material scales — a relative scale, not a moisture content |
| 7 | GreenBuildingAdvisor — "Pinless Moisture Meters", Peter Yost | https://www.greenbuildingadvisor.com/article/pinless-moisture-meters | 2026-10-25 | 78% | one homeowner's pinless meter read this on drywall at an outside corner; Yost attributes it to the metal cornerbead behind the joint compound |
| 8 | GreenBuildingAdvisor — same article (pin reading, same spot) | https://www.greenbuildingadvisor.com/article/pinless-moisture-meters | 2026-10-25 | 0.3% | Delmhorst pin-type meter on the same wall; Yost states 0.3% by weight is about equilibrium at 50% relative humidity and 70°F |
| 9 | GreenBuildingAdvisor — same article (acceptability thresholds) | https://www.greenbuildingadvisor.com/article/pinless-moisture-meters | 2026-10-25 | 0.5% | Delmhorst manual thresholds as Yost reports them: up to about 0.5% acceptable, 0.5% to 1% cautionary, over 1% unacceptable |
| 10 | Tramex — "What is an acceptable moisture level for drywall?" | https://tramexmeters.com/learn/acceptable-moisture-readings-in-drywall-tramex-meters | 2026-10-25 | 8.5% MC | manufacturer statement that a drywall-calibrated pin scale runs 0.0 to 8.5% MC in alignment with ASTM C1789, and that a comparative pinless scale is 0-100 |
| 11 | Tramex — same page (dual depth) | https://tramexmeters.com/learn/acceptable-moisture-readings-in-drywall-tramex-meters | 2026-10-25 | 9mm | manufacturer spec, a shallow depth scale (regular depth 30 mm) that reduces the influence of the substrate behind the drywall |
| 12 | General Tools — MMD4E specification table | https://generaltools.com/products/pin-type-lcd-moisture-meter | 2026-10-25 | 1.5 to 33% | manufacturer spec, a pin meter claiming a building-material percentage range (wood 5 to 50% WME), i.e. the calibration claim differs meter to meter |

## What the article must carry

- **The pair beats the combo, in arithmetic the reader can check.** $49.97 + $34.98 = $84.95. The MS150 is $109.99, which is $25.04 more (29.5% more) for the same two sensor types in one housing. State both the total and the gap; do not round to "about $25".
- **Depth is the axis that changes the buy.** 0.75 inch (ET140) against 0.38 inch (ET150): an inch-scale number that decides whether the reading is the wall's face or the cavity behind it. 0.75 / 0.38 = 1.97, so the pinless sensor reaches roughly twice as deep — which is the feature on a bare stud wall and the defect on a wall with cornerbead, steel studs, foil facing or tile backer behind it.
- **What the spec sheets actually say, in three different languages.** ET140: "Calibrated for Drywall, Masonry, Hardwood, Softwood Only", accuracy +/-4%, range 0 to 100% (row 4). ET150: accuracy "Wood: ± 2%, Drywall & Masonry: Relative Readings" and a drywall range written as "0% to 100% Relative Humidity" (rows 5, 6) — a relative scale wearing a percentage sign. MS150: pinless "6 to 99.9%" labelled relative, pin mode 1.5 to 33% building materials (row 3 page description).
- **The 78-versus-0.3 disagreement is the article's spine.** One meter, on one drywall corner, read 78% while a calibrated pin meter read 0.3% on the same spot (rows 7, 8). The cause was metal less than half an inch behind the joint compound. The consequence: a relative index and a moisture content are different quantities, and only the second has published thresholds (row 9: 0.5% acceptable, 0.5-1% cautionary, over 1% unacceptable).
- **The genuinely calibrated option is a different price class.** A drywall-calibrated pin scale reading 0.0 to 8.5% MC (row 10) is what makes a threshold meaningful, and the meters carrying it are not the three in this table — say that plainly instead of implying the cheap meters can be trusted to a number. Also write the shallow-depth point from row 11: dual-depth pinless designs exist precisely because a single deep pinless read is contaminated by the substrate.
- **Say what a baseline buys for free.** The cheap substitute for calibration is a comparative reading against a known-dry patch of the same material, taken several times along the same wall, near the base, doorjambs, and plumbing penetrations — Yost's guidance (row 7-9 article). This is the article's actionable method and it costs nothing.
- **Labelling discipline.** Manufacturer-claimed figures (rows 4, 5, 6, 10, 11, 12), one building scientist's documented field observation (rows 7, 8, 9), and retailer prices (rows 1, 2, 3) are three evidence classes; name the class in the sentence that carries the number. The dB-style error to avoid here is quoting a manufacturer accuracy as if an independent party measured it.
- **Mandatory honesty paragraph, near the verdict:** this review is built from four manufacturers' spec sheets, one building scientist's field write-up and three retailer price pages; the meters were not handled and no wall was read for it.
- **No Review or AggregateRating schema.** `Product` + `Offer` with price and `priceValidUntil`, or a plain `ItemList` — this desk cannot rate hardware it never held.
- **Verdict block links:** the vertical hub https://wellroost.com/categories/home-diagnostics-tools/ and the live calculator https://wellroost.com/calculators/true-cost-of-ownership/ (both returned HTTP 200 on 2026-10-25). There is no diagnostics-specific calculator on the front — do not invent one.
- **Length and shape:** comparison format, 900-1,200 words, three axes that change the buy (depth versus what is behind the wall; calibrated percentage versus relative index; one body versus two), a trap section, a verdict-by-situation table, then the honesty paragraph. No figure repeated across more than two sections (`context/article_shape.json`).

## Gate result

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=12 products=3 fetched=12 hosts=6 price_as_of=2026-10-25 checked_at=2026-10-25T15:11:15+00:00 -->
<!-- review-gate:end -->
