# Evergreen Brief: yard_robotics — 2026-10-24
**Archetype:** evergreen
**Vertical:** yard_robotics
**Persona:** homeowner_pro
**Decision the reader is facing:** How much acreage rating to buy — whether the model a dealer quotes actually covers the lot once the vendor's own ±20% band, its irregular-lawn figure and its boundary-slope limit are applied, decided at order time before a single wire or reference station goes in.
**Durability:** Every figure here is either a published spec-table definition (the two area columns, the two slope columns, the on-charge and charging times) or a manufacturer list price, as of 24 October 2026 product pages; the definitions are what a buyer can still check on the same pages in twelve months, and the price ladder is dated in the article rather than presented as current. No seasonal, promotional or fuel-price figure is load-bearing: this is a sizing and derating rule, not a deal watch.
**De-dup:** No prior yard_robotics artifact exists in any of the three corpora (published/, context/drafts/, context/recon_proposals/), and a corpus grep for mower / robotic-mower / slope-spec tokens across published/ returned no hits; the nearest neighbour checked and dropped is `2026-10-05_smart-irrigation-payback-water-tier.md` (home_infrastructure_lifecycle_tco), which prices a utility tier rather than a machine's stated capacity, and `2026-10-12_cheapest-fuel-priciest-pipe.md`, which argues a fuel/pipe cost trade and shares no mechanism with a spec-sheet derating.
**Thesis:** A robotic mower's acreage is a best-case, tolerance-banded number — the same machine publishes half that area for irregular mowing, a slope limit at the boundary that is a third of the interior one, and a small-tier price per rated acre up to five times the large tier's — so the buyer should price the rating the lot will actually get, not the rating on the box.

**Lead:** The vertical's own beats: `primary_angles` #5 (the installation audit — slope grade, multi-zone lawns and return-to-base failures) and #1 (wire-free navigation where terrain and tree cover decide the machine), read against the persona's `wants` in `context/personas.json` ("payback math, gotchas, code/incentive reality") — a serious homeowner standing in front of three quotable models with no way to tell what each one's acreage figure means.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Husqvarna — Automower 420 iQ product page (specification table) | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | 2026-10-24 | Area capacity - irregular 0.5 acre against area capacity - systematic 1 acre, under a Lawn Size (±20%) 1 acre headline | vendor claim |
| 2 | Husqvarna — Automower 420 iQ product page (specification table) | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | 2026-10-24 | Maximum slope performance at boundary 15 % against a maximum slope performance inside installation of 45 % | vendor claim |
| 3 | Husqvarna — Automower 420 iQ product page (specification table) | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | 2026-10-24 | 84 min typical mow time on one charge against 54 min typical charging time | vendor claim |
| 4 | Husqvarna — Automower 435 iQ AWD product page (specification table) | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-435-iq-awd/ | 2026-10-24 | 1.3 acre Lawn Size (±20%) against area capacity - irregular 0.9 acre, with a maximum slope performance at boundary of 50 % | vendor claim |
| 5 | Husqvarna — Automower 420 iQ product page (price block) | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | 2026-10-24 | $3,299.99 for the 1-acre-rated Automower 420 iQ | vendor claim |
| 6 | Segway — Navimow robot mower range page (sizing guide) | https://navimow.segway.com/ | 2026-10-24 | 265 m² mowing area per charge on the i208 LiDAR, recommended for 800 ㎡ - 2000 ㎡ lawn size | vendor claim |
| 7 | Kress — robotic mowers range page (list-price ladder) | https://www.kress.com/en-us/robotic-mowers | 2026-10-24 | $ 4,199 .98 for the 1¼-acre KR174, against $ 2,799 .98 for the ¼-acre KR161 | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Rated acreage is a best-case number: ±20% band, irregular-mowing capacity at half, boundary slope at a third, and a price-per-acre ladder that inverts | 9 | 8 | 7 | 9 | 8.3 | **winner** |
| Robot mower against a $150–250/month mowing contract: the breakeven month on a quarter to one acre | 9 | 6 | 4 | 8 | 6.7 | dropped — no fetchable primary anchor for the contract price (lead-gen cost pages block the verifier, and a derived wage-only price would be my arithmetic wearing a citation) |
| Per-acre-year consumables: blades, batteries and the year-four battery replacement | 8 | 8 | 5 | 8 | 7.0 | dropped — blade-set interval verifies (500-1000 mowing hours) but no vendor page reached by the verifier carries a replacement battery price or a cycle count |
| Modular base unit versus dedicated mower plus dedicated snow blower: single-point-of-failure math | 8 | 7 | 6 | 7 | 7.0 | dropped — Yarbo's storefront prices verify but the module reliability data that the thesis needs does not exist on any fetchable page |
| Wire-free navigation: LiDAR versus RTK versus vision under tree cover | 8 | 7 | 5 | 6 | 6.6 | dropped — the vendors publish slope and area but not canopy performance, so the comparison would rest on marketing adjectives |

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=4 hosts=3 decision="sha1:7c57b671d7" dedup="matched a prior artifact: 2026-10-05_smart-irrigation-paybac" window_days=180 checked_at=2026-10-24T18:34:40+00:00 -->
<!-- evergreen-gate:end -->
