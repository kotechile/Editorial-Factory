# Signals: home_diagnostics_tech — 2026-11-07
**Window:** 2026-10-08 → 2026-11-07
**Queries run:** 13 web fan-outs across the vertical's six `primary_angles` and its configured sources, 1 Home & Lifestyle Intelligence MCP pull (`--recent 30 --vertical home_diagnostics_tech --format signals`, 10 items, every one mortgage / data-centre / clean-energy policy noise with zero rows on this beat — recorded as absent, not as a veto), and 6 primary-page reads (Thermal Master's product page and its October blog post, the Picothermal build write-up, Hackaday's coverage of it, FLIR's store grid, FLIR's own E5 Pro page). 9 in-window rows kept; GSC carried 0 candidates (`2026-10-24_gsc_home_diagnostics_tech_opportunities.md`, bonus signal only).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Thermal Master P3 Lite sells a "512 × 384" resolution that is an upscale of a 256 × 192 detector | https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android | 2026-10-20 | "$239.00" sale / "$269.00" regular; bullet reads "512 × 384 Razor-Sharp X³ IR resolution powered by a 256 × 192 VOx detector", and the overview states "it upscales native 256x192 thermal resolution to 512x384" | The headline pixel count on the box is produced by software, not sampled by the detector | 78 |
| 2 | The vendor's own home-inspection guide tells buyers to choose on that upscaled number | https://thermalmaster.com/blogs/blog/a-thermal-camera-worth-buying-for-home-inspection-in-2026 | 2026-10-20 | "Its 512 × 384 X³IR resolution and ≤40 mK thermal sensitivity help reveal subtle temperature differences"; P3 Lite black ships from 2026-10-26 | A buying criterion that cannot be checked on the native array | 70 |
| 3 | Picothermal: a builder revives a 160 × 120 FLIR Lepton 3.5 camera and makes it speak WebUSB to a browser instead of an app | https://www.cezarchirila.com/blog/2026/10/picothermal/ | 2026-10-15 | Lepton 3.5 "160x120" against the MLX90640's "24x32"; "being tied to an app meant that I would need to maintain it if I didn't want the device to become obsolete" | The data path, not the detector, decides how long the instrument stays useful | 76 |
| 4 | Hackaday frames the same build as an escape from app abandonware | https://hackaday.com/2026/10/15/a-thermal-camera-that-uses-webusb | 2026-10-15 | "today's app is tomorrow's non-functional abandonware"; hardware is "a FLIR sensor talking to an RP2040"; the firmware was written with an AI agent in 2026, not by hand | A camera whose only vendor dependency is a browser standard | 68 |
| 5 | FLIR's own store prices the same 160 × 120 tier at $1,399 | https://www.flir.com/store | 2026-11-07 | FLIR E5 Pro 160 × 120 $1,399; C8 320 × 240 $999; One Pro 160 × 120 $429 (sale $349); One 80 × 60 $249; Edge Pro 160 × 120 $529; TG268 160 × 120 $599; MR77 moisture meter $929 | What the brand tier charges for pixels a $239 camera claims four times over | 72 |
| 6 | FLIR's E5 Pro page states the pixel count honestly and sells the surrounding services | https://www.flir.com/products/e5-pro/ | 2026-11-07 | "160 × 120 thermal resolution (19,200 pixels)"; $1,399.00; bundled "12-month Flir Ignite Pro subscription", MSX, 3.5-inch 640 × 480 touchscreen | The premium is reporting, warranty, training and cloud — not resolution | 70 |
| 7 | FLIR markets its newest handheld line on the software layer, not the detector | https://www.flir.com/browse/portable-inspection-solutions/handheld-thermal-cameras/ixx-series/ | 2026-11-07 | Store banner: "NEW iXX-Series: Revolutionizing Thermal Inspections with App-Driven Intelligence" | The industry is moving value into the app while the hobbyist moves it out | 62 |
| 8 | Blower-door and infrared are still sold together as the audit pair, and the imager is the optional half | https://www.homeinspector.org/reporter-articles/when-to-consider-thermal-imaging | 2026-08-31 | ASHI Reporter argues thermal imaging "should remain optional" in a standard inspection because mandating it "would increase costs, expand liability" | Out of window — carried as dated background, not an anchor | 0 |
| 9 | The EPA's 2026 Technology Transitions revisions keep the A2L transition running into commercial refrigeration | https://hvac-blog.acca.org/preparing-for-the-next-phase-of-a2l-adoption-in-hvacr | 2026-10-19 | Commercial-refrigeration contractors will need "refrigerant leak detection, circulation or ventilation fans"; service tools "should be rated for use with flammable refrigerants" | Instrument requirements follow the refrigerant, not the homeowner's wish | 64 |

## Dated background
- The Picothermal firmware and web page are public: https://github.com/icamaster/picothermal and the WebUSB landing page https://www.cezarchirila.com/webusb/picothermal.html — carried as background only; a code-availability row pairs against every other row and would poison the seed step.
- ASHI Reporter, "When to Consider Thermal Imaging", 2026-08-31 — https://www.homeinspector.org/reporter-articles/when-to-consider-thermal-imaging (outside the 30-day window; used only to show that the professional standard still treats infrared as an add-on).
- EPA stationary refrigeration programme page (Section 608 technician certification) — https://www.epa.gov/section608/section-608-technician-certification (standing record, no in-window action).
- Thermal Master P3 Lite model naming: the product page states "P3 Lite is the product name, while P2 Max is its model designation" — https://thermalmaster.com/products/p3-lite-thermal-camera-for-iphone-and-android (packaging may still read P2 Max; recorded so the drafter does not treat the two names as two products).

**Dating note:** rows 1–4 are event-dated (a product page and a build write-up published inside the window; row 1's date is the vendor blog post of 2026-10-20 that introduced the camera's marketing claims, since the product page itself carries no visible date). Rows 5–7 are standing retail and product pages read on 2026-11-07 — the observation date is in the Date column and the prices are labelled as of that reading, never as a price change event. Row 9 is a corporate-partner post dated 2026-10-19. Row 8 is outside the window and is background only.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=9 candidates=0 heuristic=- window=2026-10-08..2026-11-07 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

