# Verified Brief: yard_robotics — 2026-11-07 (evergreen)

Topic: the correction-data path behind a wire-free robot mower's accuracy claim.
Sources fetched live 2026-11-07 through `scripts/citation_hub_dossier.fetch_source`; the gate PASSed
7/7 rows on four hosts (`context/recon_proposals/2026-11-07_yard_robotics_evergreen_brief.md`).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Install requirement | A reference station needs a clear 135-degree sky cone and a power outlet | VERIFIED | https://www.husqvarna.com/us/discover/epos | "Reference station must have clear 135-degree view of sky in all upper directions." / "The reference station requires an open sky view (135-degree cone) and access to a power outlet." |
| 2 | Install requirement | The station mounts at least 2 metres (6.5 feet) high | VERIFIED | https://www.husqvarna.com/uk/support/install-virtual-boundaries-with-husqvarna-epos-two-installation-options-ka-70323 | "The reference station must be installed at least 2 metres (6.5 feet) high , with a clear view of the sky in all directions and preferably near a power outlet." |
| 3 | Accuracy ladder | Cloud corrections are rated 1–6 cm and require cellular coverage on site | VERIFIED | https://www.husqvarna.com/id/learn-and-discover/husqvarna-epos | "EPOS via Husqvarna Cloud / Correction data over 4G Cloud / No need for physical installations / Requires cellular coverage on the site / Accuracy typically 1–6 cm" |
| 4 | Accuracy ladder | A single RS 4G station covers up to 25 km and is rated 1–2 cm within 10 km; RS5 uses radio up to 500 m | VERIFIED | https://www.husqvarna.com/id/learn-and-discover/husqvarna-epos | "EPOS RS 4G reference station … One single station needed (range up to 25 km) … Accuracy typically 1–2 cm (within 10 km range)" / "EPOS RS5 reference station … Correction data over short distance radio (range up to 500 m) … Accuracy typically 1–2 cm" |
| 5 | Measured degradation | Survey-grade RTK across 84 points under conifer canopy: horizontal RMSE 2.03 m, MAE 1.63 m, and no fixed solutions were achieved | VERIFIED (FLAGGED — scope) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11479190 | "In terms of the overall horizontal accuracy, an RMSE of 2.03 m and MAE of 1.63 m are found." / "In this study, no Fixed solutions were achieved, with almost all epochs recorded as DGPS solutions (97% of 2670 solutions—30 per point)." / "In total, 84 test points were determined, randomly distributed under the canopy" |
| 6 | Fix threshold and rate | A fixed solution needs at least five satellites held stably, and the fix rate in favourable forest conditions runs about 93% | VERIFIED (secondary technical explainer) | https://www.lefixea.com/article/rtk112 | "Generally, RTK has difficulty obtaining a fixed solution (Fix) unless at least five satellites are being stably received; if the count drops to four or fewer, there is a risk that a position cannot …" / "The fix rate … can remain relatively high (about 93%) in comparatively favorable forest conditions, but drops significantly in more obstructed environments." |
| 7 | Replacement cost | A US dealer lists the EPOS reference station at $899.99, marked down to $799.99 | VERIFIED | https://smartyardnw.com/product/husqvarna-epos-reference-station-2-4 | "$ 899.99 Original price was: $899.99. $ 799.99 Current price is: $799.99." |
| 8 | Vendor concession (prose only) | Kress lists dead reckoning for weak satellite signal in the KR172's key features | VERIFIED | https://www.kress.com/en-us/kress-rtk%E2%81%BF-%C2%BD-acre-robotic-lawn-mower-kr172 | "Centimeter-level accuracy without station antenna in your property … Dead reckoning for mowing even undershade (weak satellite signal)" |
| 9 | Competitor model (prose only) | Network RTK is included at no extra cost, cellular data is free, and coverage is checked by postcode | VERIFIED | https://navimow.segway.com/ | "Network RTK access is included at no extra cost, required cellular data are provided free of charge." / "Check Network RTK Coverage — Enter your postcode to verify if Network RTK is available in your area." |

## Gate rulings for the drafter

- **Row 5 is FLAGGED for scope, not for accuracy.** The trial is a conifer forest, not a lawn with three
  maples, and its own method accepted any position the receiver could log (a high PDOP threshold of 8,
  no signal-to-noise filter), so 2.03 m describes the floor under closed canopy rather than what a
  suburban lot will see. The article must say both: the number, and that it is a forest trial.
- **"No fixed solution" is the load-bearing phrase, not the metre figure.** Under closed canopy the
  receiver never resolved the carrier-phase ambiguity, which is the state in which an RTK mower has no
  centimetre position at all. State it once, in the paper's own terms.
- **Rows 8 and 9 carry no gate row and must not be quoted as measured.** They are a manufacturer's own
  feature list and a competitor's own sales page; label them as such.
- **Do not add a price for any mower.** The only money figure authorised is the dealer price of the
  reference station (row 7), and it is dated to the 7 November 2026 read.
- **Do not generalise the cloud-coverage list.** Husqvarna's own text reads "USA (limited availability by
  region)"; the article says that and nothing wider.
- Terms to gloss on first use: RTK ("real-time kinematic"), correction data, a fixed solution, dead
  reckoning, and the EPOS product name (the maker's own expansion is "Exact Positioning Operating System").
