# Verified Brief: resilient_home_assets (evergreen) — 2026-10-09
**Archetype:** evergreen
**Slug:** backup-battery-sizing-critical-loads
**Angle Type:** Single-signal (durable). The news-track freshness gate does not run here (`skills/evergreen_topics.md`).
**Decision:** How many kWh of stationary storage and which circuits on the backed-up subpanel for a multi-day outage.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Consumption baseline | U.S. residential electricity use averaged 10,791 kWh a year — about 899 kWh a month — as of the 2022 reporting year (EIA's latest complete figure) | VERIFIED | https://www.eia.gov/tools/faqs/faq.php?id=97&t=3 | "In 2022, the average annual amount of electricity sold to (purchased by) a U.S. residential electric-utility customer was 10,791 kilowatthours (kWh), an average of about 899 kWh per month." — U.S. EIA |
| 2 | Price line | The U.S. average residential retail electricity price was 18.31 cents per kWh in July 2026, up 4.9% from July 2025 | VERIFIED | https://www.eia.gov/electricity/monthly/update/end-use.php | "Residential 18.31 [cents/kWh] ... Change from July 2025 4.9%" — U.S. EIA, Electricity Monthly Update, End-Use (July 2026) |
| 3 | Load envelope | A full freezer holds its temperature for about 48 hours and a refrigerator for about 4 hours; food is unsafe after 2 hours above 40°F | VERIFIED | https://www.ready.gov/power-outages | "The refrigerator will keep food cold for about four hours. A full freezer will keep the temperature for about 48 hours." … "Throw away any food that has been exposed to temperatures 40 degrees or higher for two hours or more" — FEMA / Ready.gov |
| 4 | Generation baseline | NREL assumes an average residential solar system size of 7.15 kW (range 3–11 kW) | VERIFIED | https://www.energy.gov/eere/solar/homeowners-guide-going-solar | "For its analyses, NREL uses an average system size of 7.15 kilowatts direct-current with a 3-11 kilowatt range." — U.S. Department of Energy / NREL |

## Gate rules check
- Evergreen floor (`scripts/evergreen_gate.py`): 4 verified rows on 3 distinct hosts (eia.gov, ready.gov, energy.gov) — PASS, marker written.
- REMOVED: 0. FLAGGED: 0.

**Drafter notes:**
- The whole-house figure (row 1) is the *wrong* sizing unit; the critical-loads figure (row 3) is the right one. Make that contrast the spine of the piece; do not present the annual kWh as the answer.
- Attribute the price (row 2) as "July 2026" — it is re-indexed monthly; keep the "as of" intact.
- Row 4 is the generation baseline (solar), not a battery figure — use it only to make the point that buyers borrow the wrong number from the solar quote.
- Do NOT carry any customer-case dollar figure (e.g. a specific bank kWh or storm duration) that is not in rows 1–4 or the source list. No secondary-derived sums.
