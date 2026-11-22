# Verified Brief: home_diagnostics_tech — 2026-11-22

Review run (`skills/review_comparison.md`), format `comparison`, three pocket thermal imagers.
Claim extraction from `context/recon_proposals/2026-11-22_home_diagnostics_tech_review_brief.md`
(8 evidence rows, all fetched by `scripts/review_gate.py` on 2026-11-22 — gate PASS, 2 hosts,
marker written 2026-11-22T15:05:41+00:00).

**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** which sub-$240 pocket thermal imager to buy this winter to find missing insulation, cold corners and hot breaker lugs on an ordinary house — and whether the $90 step from the cheapest unit buys anything the winter scan can actually see.
**Format:** comparison
**Price as of:** 2026-11-22
**Verdict:** Buy the RISION Magic Pro at $199 as of 2026-11-22 — it is the cheapest unit of the three whose detector natively holds 256×192, and the $40 premium on the Thermal Master P3 Lite buys a macro lens (itself a $50 add-on) and a December shipping batch, not pixels; the $109 Magic stays the right buy only where the reader wants a once-a-season cold-wall check and can accept a 160×120 detector that paints a bay's worth of wall in 120 tiles.
**De-dup:** 2026-11-21_your-109-cameras-missing-verdict (news) covered the $109 Magic as a thesis; 2026-11-07_your-512x384-cameras-10x-illusion (news) covered the upscale arithmetic. Neither is a purchase decision, and no artifact on any track compares units or quotes a cart figure. A corpus grep for `Magic Pro`, `P3 Lite`, `TC001`, `512×384` across published/, context/drafts/ and context/recon_proposals/ returns the two news pieces only.
**Thesis:** every unit in this class prints a super-resolved headline number, so the only count that separates them is the detector underneath: 19,200 native pixels at $109 against 49,152 at $199, a $90 step, and the $40 spread between $199 and $239 separates two cameras that share the same 49,152-pixel detector and nothing else that matters to a wall.

| Product | Price | Source | Note |
|---|---|---|---|
| RISION Magic (AF01) | $109.00 | https://www.rision.com/products/rision-magic-smartphone-thermal-camera.js | 160×120 native, super-resolved to 320×240; variant JSON shows the item available, cart figure in cents; the rendered page shows a sale display of $119.00 against a $139.00 list |
| RISION Magic Pro (AF02) | $199.00 | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera.js | 256×192 native, QuadIR upscales to 512×384; variant JSON shows the item available; rendered page shows $229.00 against $299.00 |
| Thermal Master P3 Lite (P2 Max) | $239.00 | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 256×192 VOx native, X³ IR upscales to 512×384; og meta figure 239.00, variants at 23900 against a compare-at 26900; macro lens is a separate variant at $50.00; ships in batches from early Dec (silver) / mid-Dec (black) |

| # | Source | URL | Retrieved | Figure | Measured | Class |
|---|---|---|---|---|---|---|
| 1 | RISION — Magic cart record | https://www.rision.com/products/rision-magic-smartphone-thermal-camera.js | 2026-11-22 | 10900 | Shopify variant JSON figure in cents = $109.00, single variant, available true | maker cart record |
| 2 | RISION — Magic page, native detector | https://www.rision.com/products/rision-magic-smartphone-thermal-camera | 2026-11-22 | 160×120 | page states a native 160×120 resolution super-resolved to 320×240, ≤40mK NETD, 25Hz | manufacturer-claimed |
| 3 | RISION — Magic page, measurement range | https://www.rision.com/products/rision-magic-smartphone-thermal-camera | 2026-11-22 | (-20°C to 600°C) | printed with the Fahrenheit pair -4℉ to 1112℉; accuracy ±2°C (or ±2% of the reading) | manufacturer-claimed |
| 4 | RISION — Magic Pro cart record | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera.js | 2026-11-22 | 19900 | Shopify variant JSON figure in cents = $199.00, single variant, available true | maker cart record |
| 5 | RISION — Magic Pro page, native sensor | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera | 2026-11-22 | 256×192 | "Native 256×192 sensor. QuadIR™ algorithm upscales resolution to 512×384" | manufacturer-claimed |
| 6 | Thermal Master — P3 Lite price | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | $239.00 | og meta product figure, variants at 23900 cents against compare-at 26900 | maker cart record |
| 7 | Thermal Master — P3 Lite detector | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | 256×192 @12μm | VOx detector row in the specification block | manufacturer-claimed |
| 8 | Thermal Master — P3 Lite range | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | -20°C~600°C | measurement range row, printed with -4°F~1112°F; accuracy ±2°C / ±2% | manufacturer-claimed |
| 9 | Thermal Master — P3 Lite macro variant | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-11-22 | $50.00 | macro lens sold as a separate variant at 5000 cents; kit variants ("Black + Macro Lens") at 28900 cents | maker cart record |
| 10 | RISION — Magic Pro owner review | https://www.rision.com/products/rision-magic-pro-smartphone-thermal-camera | 2026-11-22 | Find the cold spots on your house. So simple to use, download app, plug it in, see the images. | verified buyer review, 3 reviews on the page; owner report, not a measurement | owner report |
| 11 | RISION press release (PR Newswire, 2026-11-19) | https://www.prnewswire.com/news-releases/rision-offers-up-to-45-off-thermal-cameras-for-black-friday-and-cyber-monday-302945429.html | 2026-11-22 | Magic 24-g USB-C camera $109 (45% off $199 MSRP) | vendor announcement of the November 19–30 sale window on Amazon and RISION.com; matches the live cart record | vendor announcement |

## Verification rulings

- **Cart record beats rendered banner.** RISION's rendered pages print a sale display of $119.00 (Magic) and $229.00 (Magic Pro), but the variant record a buyer reaches — the cart — holds 10900 and 19900 cents, both `available: true`, and matches RISION's own November 19 press release ($109 Magic, 45% off, through November 30). The article leads with the cart figure as of 2026-11-22 and states the rendered banner may revert after November 30. FLAGGED as a discrepancy, carried as stated.
- **Topdon refused on stock, not taste.** topdon.us TC001 ($289.00) and TC001 Mini ($139.00) both carry the server-rendered sold-out badge ("badge price__badge-sold-out … Sold out", three renders each) on 2026-11-22; §2's admissibility rule (purchasable today at a listed figure) excludes them. The article names them as the unavailable Android-workhorse option, without figures.
- **Every headline resolution is an upscale.** 320×240 (Magic), 512×384 (Magic Pro QuadIR), X³ IR 512×384 (P3 Lite) are all software super-resolution over smaller native detectors (160×120, 256×192, 256×192). This is the 2026-11-07 news thesis; this article states it in one line and does not re-argue it.
- **No measured figures exist from any hand.** All three makers print NETD ≤40mK and ±2°C accuracy as claims. No independent measured review of these three units was found fetchable on 2026-11-22 (the GBA HIKMICRO Pocket 2 review is a different unit at a different class). The article labels every number manufacturer-claimed and derives nothing but arithmetic from printed endpoints.
- **Macro lens is an add-on, not included.** The P3 Lite's macro lens is a separate $50.00 variant; the $239.00 base does not carry it. Claim removed in earlier draft-stage framing ("P3 Lite adds a macro lens") and corrected to "sold as a $50 add-on."
- **Shipping window is a real constraint.** P3 Lite silver ships from early December, black from mid-December (maker's own shipping notice); a buyer who wants to scan this week buys RISION, and the article says so.

## Derived arithmetic (computed from printed endpoints, never estimated)

160×120 = 19,200 native pixels; 256×192 = 49,152; $109 ÷ 19,200 = $5.68 per native pixel; $199 ÷ 49,152 = $4.05; $239 ÷ 49,152 = $4.86; $199 − $109 = $90; $239 − $199 = $40; $239 + $50 = $289 (P3 Lite with macro lens).
