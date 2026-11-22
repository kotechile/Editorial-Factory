# Review brief — home_diagnostics_tech — 2026-11-22

## Review brief

**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** which sub-$240 pocket thermal imager to buy this winter to find missing insulation, cold corners and hot breaker lugs on an ordinary house — and whether the $90 step from the cheapest unit buys anything the winter scan can actually see.
**Format:** comparison
**Price as of:** 2026-11-22
**Verdict:** Buy the RISION Magic Pro at $199 as of 2026-11-22 — it is the cheapest unit of the three whose detector natively holds 256×192, and the $40 premium on the Thermal Master P3 Lite buys a macro lens (itself a $50 add-on) and a December shipping batch, not pixels; the $109 Magic stays the right buy only where the reader wants a once-a-season cold-wall check and can accept a 160×120 detector that paints a bay's worth of wall in 120 tiles.
**De-dup:** 2026-11-21_your-109-cameras-missing-verdict (news) covered the $109 Magic as a thesis — that a surface pattern is a clue, not a diagnosis; 2026-11-07_your-512x384-cameras-10x-illusion (news) covered the upscale arithmetic. Neither settles a purchase; no prior artifact on any track compares units or quotes a cart figure, and a corpus grep for `Magic Pro`, `P3 Lite`, `TC001`, `512×384` across published/, context/drafts/ and context/recon_proposals/ returns the two news pieces only. This piece must not re-argue either thesis — it spends its words on the buying decision.
**Thesis:** every unit in this class prints a super-resolved headline number, so the only count that separates them is the detector underneath: 19,200 native pixels at $109 against 49,152 at $199, a $90 step, and the $40 spread between $199 and $239 separates two cameras that share the same 49,152-pixel detector and nothing else that matters to a wall.

## Price table

| Product | Price | Source | Note |
|---|---|---|---|
| RISION Magic (AF01) | $109.00 | https://www.rision.com/products/rision-magic-smartphone-thermal-camera.js | 160×120 native, super-resolved to 320×240; variant JSON shows the item available, cart figure in cents; the rendered page shows a sale display of $119.00 against a $139.00 list |
| RISION Magic Pro (AF02) | $199.00 | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera.js | 256×192 native, QuadIR upscales to 512×384; variant JSON shows the item available; rendered page shows $229.00 against $299.00 |
| Thermal Master P3 Lite (P2 Max) | $239.00 | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 256×192 VOx native, X³ IR upscales to 512×384; page carries og meta figure 239.00, variants at 23900 against a compare-at 26900; macro lens is a separate variant at $50.00; ships in batches from early Dec (silver) / mid-Dec (black) |

## Evidence rows

| # | Source | URL | Retrieved | Figure | Measured |
|---|---|---|---|---|---|
| 1 | RISION | https://www.rision.com/products/rision-magic-smartphone-thermal-camera.js | 2026-11-22 | 10900 | Shopify variant JSON figure in cents = $109.00, single variant, available true |
| 2 | RISION | https://www.rision.com/products/rision-magic-smartphone-thermal-camera | 2026-11-22 | 160×120 | native detector, page states super resolution 320×240 and ≤40mK NETD |
| 3 | RISION | https://www.rision.com/products/rision-magic-smartphone-thermal-camera | 2026-11-22 | (-20°C to 600°C) | measurement range printed with the Fahrenheit pair -4℉ to 1112℉ |
| 4 | RISION | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera.js | 2026-11-22 | 19900 | Shopify variant JSON figure in cents = $199.00, single variant, available true |
| 5 | RISION | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera | 2026-11-22 | 256×192 | native sensor; page states the QuadIR algorithm upscales the image to 512×384 |
| 6 | Thermal Master | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | $239.00 | og meta product figure, variants at 23900 cents against compare-at 26900 |
| 7 | Thermal Master | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | 256×192 @12μm | VOx detector row in the specification block |
| 8 | Thermal Master | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | -20°C~600°C | measurement range row, printed with -4°F~1112°F |

## Honesty ruling

The article is built from the three makers' own specification pages and cart records plus owner reviews printed on those pages; nothing was run, held or measured by the desk, and no first-person language may imply a unit was tried. Manufacturer-claimed figures, derived arithmetic and owner reports are labelled as separate evidence classes. Figures carry dates in the table and in prose. No rating structure is emitted for any unit. Two display-versus-cart discrepancies are stated, not hidden: RISION's rendered pages show $119.00 / $229.00 sale displays while the cart record a buyer reaches charges $109.00 / $199.00, matching RISION's own November 19 press release (Magic $109, 45% off, through November 30); the article leads with the cart record as of 2026-11-22 and says the displayed sale banner may revert after November 30. The P3 Lite's batch-shipping window and its separately sold macro lens are both stated.

## Derived arithmetic (inputs printed above, computed in-session)

160×120 = 19,200 native pixels; 256×192 = 49,152; $109 ÷ 19,200 = $5.68 per native pixel; $199 ÷ 49,152 = $4.05; $239 ÷ 49,152 = $4.86; $199 − $109 = $90; $239 − $199 = $40; $239 + $50 = $289 (P3 Lite with macro lens).

## Notes for the draft

- Three axes that change the buy: native detector pixels (19,200 vs 49,152 at one $90 step); the $40/$50 pair that separates two 49,152-pixel cameras on kit and shipping, not sensing; platform and timing (P3 Lite includes a USB-C-to-Lightning adapter for pre-2018 iPhones but ships from December batches; the RISION pair is in stock now and needs a Type-C iPhone).
- The trap: every headline resolution on all three pages is an upscale — 320×240, 512×384, X³ IR 512×384 — so a reader comparing headline numbers sees a 4× leap that no detector made. The comparison matrix must carry the native row.
- The cart-record point is the article's sharpest finding: the November 30 deadline is a real cliff on the two RISION units, and the rendered page understates what the cart charges today.
- Owner-report evidence class: the Magic Pro page carries 3 verified reviews (one owner: "Find the cold spots on your house. So simple to use, download app, plug it in, see the images."); the P3 Lite page's December shipping notice is the honest counterweight.
- Verdict block must link the vertical's calculator (/calculators/true-cost-of-ownership/) and the category hub (/categories/home-diagnostics-tools/).
- Comparison matrix header: | Unit | Cart | Claimed | Native | Fails at | — Claimed column shows the super-resolved headline, Native the detector, Fails at the named situation.

## Gate result

<!-- review-gate:start -->
<!-- review-gate: helper=review_gate.py format=comparison rows=8 products=3 fetched=8 hosts=2 price_as_of=2026-11-22 checked_at=2026-11-22T15:08:03+00:00 -->
<!-- review-gate:end -->
