# Signals: home_diagnostics_tech — 2026-11-21
**Window:** 2026-10-22 → 2026-11-21
**Queries run:** 9 (MCP home_lifestyle_intel returned 10 off-vertical rows — mortgage/offshore-wind/FAA, none diagnostics; source configs fanned out instead: HN Algolia, PR Newswire, vendor first-party, syndicated inspector guidance)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | RISION Black Friday cuts sub-$300 thermal imagers to record lows | https://www.prnewswire.com/news-releases/rision-offers-up-to-45-off-thermal-cameras-for-black-friday-and-cyber-monday-302945429.html | 2026-11-19 | RISION's "biggest sale of the year": Magic 24-g USB-C camera $109 (45% off $199 MSRP, −20°C to 600°C); Magic Pro 256×192 native → 512×384 QuadIR $199 (33% off $299); Torix standalone 2.8-inch $149 (32% off $219); sale Nov 19–30 on Amazon and RISION.com, pitched to "homeowners looking to spot signs of heat loss this winter" | Black Friday just made the $100–$200 thermal imager a mass-market tool | 88 |
| 2 | First 3D omnidirectional thermal invisibility cloak built and tested | https://www.sciencedaily.com/releases/2026/10/261025073051.htm | 2026-10-26 | UIUC (Zhang, Li, Wang) + DTU (Sigmund) built a 3D-printed aluminum-lattice/cast-rubber cloak that guides heat around an object so an infrared camera sees the surrounding temperature pattern "much as it would if no object were present"; works from "virtually any direction"; published in Nature Communications 17, DOI 10.1038/s41467-026-73167-0; Zhang: "it's about hiding and protecting information that is carried by heat" | What an IR camera sees can now be actively engineered to lie — the surface reading is negotiable | 90 |
| 3 | Syndicated inspector guidance: IR scans miss problems even when done right | https://shopping.yahoo.com/home-garden/home-improvement/articles/home-inspections-miss-costly-heat-123500302.html | 2026-11-16 | NHBC Foundation: thermal images are "maps of surface temperature"; indoor/outdoor temps must be far apart for a scan to be useful; documented case: a homeowner sealed attic leaks, but infrared images suggested little changed; a buyer's inspector was questioned over a missed cracked furnace; a two-minute paper test checks windows for drafts without any camera | Even the pro scan is a pattern-map, not a diagnosis — and buyers are disputing what it missed | 80 |
| 4 | HIKMICRO first-party home blog concedes the instrument's own limit | https://www.hikmicrotech.com/en/explore/home-blog/Places-Your-Home-Might-Be-Losing-Heat | 2026-11-21 | Vendor selling home thermal cameras states: "a thermal image shows temperature patterns, not a confirmed diagnosis. An unusual cold area may suggest where to investigate, but further checks may be needed"; cites SEAI: homes can lose up to 30% of heat through the roof; cold spot alone doesn't prove missing insulation (design, airflow, moisture, heating conditions all move surface temps) | The vendor itself disclaims the sale pitch the deal copy makes | 70 |

**Dating note:** Rows 1–3 are event/publication-dated from the publisher's own date field (PR Newswire Nov 19, 2026 09:00 ET; ScienceDaily October 26, 2026; Yahoo datePublished 2026-11-16T12:35:00Z). Row 4 is a standing first-party design page with no publication date — dated by observation (2026-11-21), winter-anchored ("this winter", "your heating is on"). Dated by observation, not by event.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=0 heuristic=- window=2026-10-22..2026-11-21 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background (URLs admissible to --check-briefs, not anchor-eligible)
- https://www.bbc.com/news/articles/cy9j10wj78wo — BBC "Could a thermal camera reveal your hidden heat loss?" (published 2024-11-29, out of window; corroboration only: thermal imagery misleads via calibration, palette, handling; "retrofit anxiety"; ~£160 camera; Octopus Energy ~500 loaner cameras, ~3,800 loans last winter; Citizens Advice ~$410/yr UK heat loss, up to $1,115 worst homes)
- https://www.cezarchirila.com/blog/2026/10/picothermal/ — Picothermal DIY thermal camera, RP2040 + Flir Lepton 3.5 (160×120 radiometric, WebUSB, firmware written by Claude agents) (blog 2026-10-12, 4 days before window; shows the DIY/open-hardware floor)
- https://www.flir.com/discover/home-outdoor/control-energy-bills-thermal-imaging-camera — FLIR first-party pitch of the same claims row 4 now disclaims
- https://www.greenbuildingadvisor.com/article/the-fundamentals-of-thermal-imaging — GBA rater fundamentals (undated evergreen; ΔT requirement, 2009 $1,200 60×60 camera anecdote)
- https://www.remodelista.com/posts/current-obsessions-preparations/ — MCP row, off-vertical, dropped
