# Review Brief: home_diagnostics_tech — 2026-11-01

**Archetype:** review
**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether $40.58, $149.99 or $169.99 buys the inspection camera that can actually show what is inside a finished wall cavity before the drywall is opened, and which of the three specs — probe diameter, articulation or depth of field — decides that.
**Format:** comparison
**Price as of:** 2026-11-01
**Verdict:** Buy the Teslong TD450S at $149.99 for a wall cavity, because it is the only one of the three that steers 210 degrees and the only one whose maker publishes a working distance at all, 0.79 to 3.94 inches straight ahead. Buy the Klein ET19 at $169.99 only where the hole must stay at a quarter inch, and buy the Klein ET16 at $40.58 only for a straight shot into a hole you have already made.
**De-dup:** `2026-10-31_home_diagnostics_tech_evergreen_brief` scored this exact candidate — the borescope against the wall opening — at 7.1 and dropped it because every borescope vendor listing (Klein, Depstech, Home Depot) was unreachable to the verifier; this run fetched three vendor hosts and the repair-cost host, so the instrument half now has anchors. No prior artifact prices an inspection camera: `2026-10-25_your-50-meter-reads-78-its-metal` prices moisture meters, `2026-10-24_your-250-imager-needs-15-degrees` prices the thermal imager, and a grep of `published/`, `context/drafts/` and `context/recon_proposals/` for borescope, ET19, ET16 and TD450 returns no article that carries a scope price.
**Thesis:** The spec that decides whether a camera can see into a wall is the far end of its depth of field, not its megapixel count or its screen: the only scope here that publishes one focuses to 3.94 inches, which is shorter than a stud bay is wide, and the two scopes that publish no working distance at all are the two that cannot be steered.

**Lead:** The vertical's own beats, `context/verticals.json` `primary_angles` #2 ("the $80 articulating borescope against a $450 drywall repair: seeing inside the wall before opening it"), read at the season when a homeowner is chasing a cold-room draft or a water stain with the heat on and the wall intact. GSC for this vertical returned no review or versus query on 2026-10-31 (`context/recon_proposals/2026-10-31_home_diagnostics_tech_signals.md` records thin impressions as a non-veto). Every price and every spec below was fetched from the page named, 2026-11-01. The $450 repair figure in the angle is not carried: the only fetchable repair price found is a professional's minimum, and the article uses that instead.

| Product | Price | Source | Note |
|---|---|---|---|
| Klein ET16 borescope for Android | $40.58 | https://hausoftools.com/products/klein-tools-et16-borescope-for-android%C2%AE-devices | 0.35 in camera head, 10 ft armored gooseneck, phone is the screen, 640 x 480 |
| Teslong TD450S dual-lens articulating camera | $149.99 | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 0.33 in dual-lens probe, 210 degree articulation, 4.5 in screen, published depth of field |
| Klein ET19 pro borescope | $169.99 | https://hausoftools.com/products/klein-tools-et19-pro-borescope | 0.22 in dual-lens probe, 9.8 ft armored snake, 4.3 in screen, no articulation |

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | Haus of Tools — Klein ET16 product page (price block) | https://hausoftools.com/products/klein-tools-et16-borescope-for-android%C2%AE-devices | 2026-11-01 | $40.58 | retailer list price, USD, in stock |
| 2 | Haus of Tools — Klein ET19 product page (price block) | https://hausoftools.com/products/klein-tools-et19-pro-borescope | 2026-11-01 | $169.99 | retailer list price, USD, in stock |
| 3 | Teslong — TD450S dual lens product page (price block) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | $149.99 | manufacturer direct price, current price, USD |
| 4 | Klein Tools — ET16 specification table | https://www.kleintools.com/catalog/borescopes/borescope-android-devices | 2026-11-01 | 0.35 | manufacturer spec, camera head diameter in inches (0.9 cm); no working distance published anywhere in the table |
| 5 | Klein Tools — ET19 specification table | https://www.kleintools.com/catalog/borescopes/pro-borescope | 2026-11-01 | 0.22 | manufacturer spec, camera head diameter in inches (0.6 cm); no working distance published |
| 6 | Teslong — TD450S technical specs (probe) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 0.33 | manufacturer spec, probe diameter in inches (8.5 mm), dual lens |
| 7 | Teslong — TD450S technical specs (articulation) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 210° | manufacturer spec, articulation angle, two-way lever control |
| 8 | Teslong — TD450S technical specs (near focus, straight view) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 0.79 | manufacturer spec, depth of field straight-viewing starts at 0.79 in |
| 9 | Teslong — TD450S technical specs (far focus, straight view) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 3.94 | manufacturer spec, depth of field straight-viewing ends at 3.94 in |
| 10 | Teslong — TD450S technical specs (far focus, side view) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 2.76 | manufacturer spec, depth of field side-viewing ends at 2.76 in |
| 11 | Teslong — TD450S technical specs (probe length) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 5.08 | manufacturer spec, probe length 5.08 ft (1.55 m) |
| 12 | Teslong — TD450S technical specs (monitor) | https://teslong.com/products/td450s-articulating-8-5mm-dual-lens-inspection-camera | 2026-11-01 | 854x480 | manufacturer spec, 4.5-inch screen resolution; photos captured at 1920x1080 on a 1.0 megapixel sensor |
| 13 | Klein Tools — ET19 specification table (display row) | https://www.kleintools.com/catalog/borescopes/pro-borescope | 2026-11-01 | 480p | manufacturer spec, display and screen resolution rows both read 480p on the same page that describes a 1920 x1080 monitor |
| 14 | Klein Tools — ET19 description (monitor claim) | https://www.kleintools.com/catalog/borescopes/pro-borescope | 2026-11-01 | 1920 x1080 | manufacturer marketing sentence, "4.3-Inch Color LCD monitor (1920 x1080) resolution", contradicted by row 13 on the same page |
| 15 | Klein Tools — ET16 specification table (cable) | https://www.kleintools.com/catalog/borescopes/borescope-android-devices | 2026-11-01 | 10-Foot | manufacturer spec, 10-Foot (3 m) armored gooseneck |
| 16 | Klein Tools — ET19 specification table (cable) | https://www.kleintools.com/catalog/borescopes/pro-borescope | 2026-11-01 | 9.8-Foot | manufacturer spec, 9.8-Foot (3 m) armored snake |
| 17 | Bob Vila — drywall repair cost, quoting Fixr | https://www.bobvila.com/articles/drywall-repair-cost/ | 2026-11-01 | $75 | publisher's cost guide, "at least $75 to repair small holes up to 4 inches in diameter"; $200 to $550 for multiple holes in one room |

## What the article must carry

- **Depth of field is the axis, stated in inches the reader can measure.** The TD450S publishes 0.79 to 3.94 inches straight ahead and 0.4 to 2.76 inches on the side lens (rows 8, 9, 10). A stud bay between two 2x4s on 16-inch centres is about 14.5 inches across and about 3.5 inches deep, so the far focus lands inside the cavity but well short of the far stud. Klein's ET16 and ET19 tables publish no working distance at all (rows 4, 5) — a negative fact established by reading both tables, and the article says so plainly instead of guessing at a number.
- **Hole size is the second axis, and the arithmetic is checkable.** Heads are 0.22 in (5.5 mm), 0.33 in (8.5 mm) and 0.35 in (9 mm) (rows 5, 6, 4). A 1/4-inch bit is 6.35 mm, which clears the ET19's head and not the other two; a 3/8-inch bit is 9.53 mm, which clears all three. Then the repair-cost row (17) makes the honest counterpoint: a professional charges at least $75 to patch small holes up to 4 inches, so the difference between a 1/4-inch and a 3/8-inch hole is not a different repair bill — both are small holes — and the diameter argument matters because of where the hole is allowed to be, not what it costs to close.
- **Steerability is the third axis.** 210 degrees of two-way articulation on a lever (row 7) against a fixed forward view on a 10-foot bendable gooseneck (row 15) and a fixed dual lens on a 9.8-foot snake (row 16). A side lens turns the view 90 degrees; articulation aims it. State the difference in those words, and say that neither cheap scope moves its head.
- **The trap: resolution language that contradicts itself.** The ET19 page describes a 1920 x1080 monitor in its marketing sentence and prints 480p for the same display in its own spec table (rows 13, 14) — the same page, two answers. The TD450S prints 854x480 for a 4.5-inch screen while capturing 1920x1080 photos on a 1.0 megapixel sensor (row 12). The consequence: the pixel number on the box measures the sensor, not what the eye gets, and no camera in this set resolves better than the screen it shows.
- **The screen question, priced.** The ET16 has no screen at all — the phone is the display and the camera is powered from the phone's port (row 1 page description). That is the entire $109.41 gap to the TD450S and the $129.41 gap to the ET19, and it is the difference between holding a probe in one hand and a phone in the other.
- **Prices carry dates.** Every price in the table and in the prose is dated 2026-11-01 and attributed to the retailer or the maker's own store.
- **Labelling discipline.** Manufacturer-claimed specs (rows 4-16), retailer list prices (rows 1, 2), a manufacturer's own store price (row 3) and a publisher quoting a cost dataset (row 17) are different evidence classes; name the class in the sentence that carries the number. No independent measured test of these three cameras is cited, and the article must not imply one.
- **Mandatory honesty paragraph, near the verdict:** built from three manufacturer spec tables and three retail price pages, plus one published repair-cost guide; the cameras were not handled for this article and no wall was opened for it.
- **No Review or AggregateRating schema.** `Product` + `Offer` with price and `priceValidUntil`, or a plain `ItemList` — this desk cannot rate hardware it did not hold.
- **Verdict block links:** the live calculator https://wellroost.com/calculators/true-cost-of-ownership/ and the vertical hub https://wellroost.com/categories/home-diagnostics-tools/. Both answered HTTP 200 on 2026-11-01; there is no diagnostics-specific calculator on the front, so do not invent one.
- **Length and shape:** comparison, 900-1,200 words, three axes that change the buy (depth of field, hole diameter, steerability), a trap section on resolution language, a verdict-by-situation table, then the honesty paragraph. One earned inline internal link to a live wellroost page; no figure repeated across more than two sections (`context/article_shape.json`).
- **What the article must NOT say.** No first-person testing voice — nothing in the text may claim the desk tried, measured, held or worked with any of the three cameras. No claim that a camera finds a leak or diagnoses a wall — it shows a surface, and the reader still has to interpret it.

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=17 products=3 fetched=17 hosts=4 price_as_of=2026-11-01 checked_at=2026-11-01T15:12:27+00:00 -->
<!-- review-gate:end -->
