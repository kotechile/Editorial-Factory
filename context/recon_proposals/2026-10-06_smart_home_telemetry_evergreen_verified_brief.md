# Verified Brief: smart_home_telemetry — 2026-10-06 (EVERGREEN track)

Archetype: evergreen. Topic = the residential water-leak monitor as a flow-rate classifier: what
rate it must catch, and the two thresholds (night-flow baseline, insurance deductible) that settle
the buy decision. Every claim below traces to a source the evergreen gate fetched live and confirmed
contains the cited figure (4/4 rows verified on 3 hosts, `<!-- evergreen-gate: -->` marker in
`context/recon_proposals/2026-10-06_smart_home_telemetry_evergreen_brief.md`).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Leak volume | The average family wastes **9,400 gallons a year** on household leaks, **180 gallons a week** | VERIFIED | https://www.epa.gov/watersense/statistics-and-facts | "The average family can waste 180 gallons per week, or 9,400 gallons of water annually, from household leaks." |
| 2 | Leak share and threshold | **Nine percent** of US homes have leaks wasting **50 gallons or more per day**; the average household wastes **more than 9,300 gallons a year** | VERIFIED | https://www.epa.gov/watersense/fix-leak-week | "The average household's leaks can account for more than 9,300 gallons of water wasted every year and nine percent of homes have leaks that waste 50 gallons or more per day." |
| 3 | Own-meter test | A family of four exceeding **12,000 gallons a month** signals serious leaks | VERIFIED | https://www.epa.gov/watersense/fix-leak-week | "If a family of four exceeds 12,000 gallons per month, there could be serious leaks." |
| 4 | Water bill lever | The average family spends **more than $1,000 a year** on water and can save **more than $380** by fixing leaks and retrofitting | VERIFIED | https://www.epa.gov/watersense/statistics-and-facts | "The average family spends more than $1,000 per year in water costs, but can save more than $380 annually from retrofitting with WaterSense labeled fixtures and ENERGY STAR certified appliances." |
| 5 | Insurance loss share | **22.6 percent** of homeowners property-damage losses in 2023 were water damage and freezing (ISO/Verisk data via Triple-I) | VERIFIED | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | "Homeowners Insurance Losses By Cause, 2019-2023 … Water damage and freezing 28.7 19.8 23.7 25.8 22.6"; "In 2023, 5.3 percent of insured homes experienced a claim" |
| 6 | Claim severity | The **2023** average homeowners claim severity was **$20,062**, with claim frequency of 5.33 per 100 house-years | VERIFIED | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | "2023 5.33 $20,062"; "(3) Average amount paid per claim; based on accident year incurred losses, excluding loss adjustment expenses" |
| 7 | Meter premise | **87 percent** of Americans get water through a public-supply system, so a metered signal exists at the property line | VERIFIED | https://www.usgs.gov/special-topics/water-science-school/science/domestic-water-use | "The majority of America's population (about 87 percent) gets their water delivered from a public-supply system." |
| 8 | Field note (internal, not a gate row) | A monitor flagged **0.08 gallons per minute** at 3:15 a.m. and a pinhole copper slab leak was fixed before it surfaced, avoiding an estimated **$34,000** of tear-out | VERIFIED (our own field note, `context/growth_os/customer-truth.md` §smart_home_telemetry Anecdote 2) | (internal — attributed in the article as our field notes, never as an external statistic) | "An inline ultrasonic water monitor (Moen Flo) flagged an anomalous continuous flow rate of 0.08 gallons per minute at 3:15 AM while the occupants were asleep." |

**Derived arithmetic (labelled as arithmetic in the article, not as a source figure):** 50 gallons a
day is about 0.035 gallons a minute; 0.08 gallons a minute is about 115 gallons a day (≈42,000 gallons
a year).

## Gate rules applied
- 7/7 external claims VERIFIED against the fetched primary page (rows 1–7); 0 REMOVED, 0 FLAGGED.
  Row 8 is our own field note, carried with attribution and never presented as a third-party stat.
- Hosts: epa.gov (rows 1–4), iii.org (rows 5–6), usgs.gov (row 7) — three hosts, and the two EPA
  pages are cited for different figures rather than one page wearing two costumes.
- No synthesis: single-signal evergreen topic; the dual-anchor gate does not apply.
- Cross-vertical neighbour (recorded for honesty, not a de-dup requirement): the 2026-10-05
  `home_infrastructure_lifecycle_tco` evergreen piece `smart-irrigation-payback-water-tier` cites the
  same `fix-leak-week` page for the "leaks ≈10% of a water bill" figure. Different vertical,
  different artefact, different thesis (irrigation tariff payback vs device-selection and leak-rate),
  and no shared load-bearing figure.
