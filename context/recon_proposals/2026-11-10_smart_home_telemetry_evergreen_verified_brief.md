# Verified Brief: smart_home_telemetry — 2026-11-10

**Gate:** `evergreen_gate.py` PASS — 6 rows, 6 fetched, 3 sources, 3 hosts (eia.gov, energy.gov, greenbuttonalliance.org), marker written 2026-11-10T19:06:22+00:00 to `context/recon_proposals/2026-11-10_smart_home_telemetry_evergreen_brief.md`.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Count of advanced meters | About 119 million advanced electricity meters in 2022, ≈72% of total electric meters | VERIFIED | https://www.eia.gov/tools/faqs/faq.php?id=108&t=3 | "In 2022, U.S. electric utilities had about 119 million advanced ( smart ) metering infrastructure (AMI) installations, equal to about 72% of total electric meters installations." |
| 2 | Residential share of the installed base | About 88% of advanced-meter installations are residential; about 73% of residential meters are advanced | VERIFIED | https://www.eia.gov/tools/faqs/faq.php?id=108&t=3 | "Residential customers accounted for about 88% of total AMI installations, and about 73% of total residential electric meters were AMI meters." |
| 3 | Resolution floor and delivery cadence | An advanced meter records at a minimum of hourly intervals and provides the data to the utility and the customer at least once a day | VERIFIED (prose row — no numeric token, so it cannot carry a gate row) | https://www.eia.gov/tools/faqs/faq.php?id=108&t=3 | "AMI includes meters that measure and record electricity usage at a minimum of hourly intervals and that provide the data to both the utility and the utility customer at least once a day." |
| 4 | Dating of the counts | The EIA FAQ's own currency line | VERIFIED | https://www.eia.gov/tools/faqs/faq.php?id=108&t=3 | "Last updated: October 20, 2023." |
| 5 | Program coverage promised | Over 60 million homes and businesses covered by signatory commitments | VERIFIED | https://www.energy.gov/oe/green-button | "In total, these commitments ensure that over 60 million homes and businesses will be able to securely access their own energy information in a standard format." |
| 6 | Program participation | Over 50 utilities and electricity suppliers signed on; program launched January 2012 | VERIFIED | https://www.energy.gov/oe/green-button | "The Green Button initiative was officially launched in January 2012. To date, a total over 50 utilities and electricity suppliers have signed on to the initiative." |
| 7 | Live access count | Over 40 million homes and firms can access and share their own data today | VERIFIED | https://www.greenbuttonalliance.org/ | "Today, over 40 million residential and commercial customers have the ability to digitally access and securely share their Green Button energy data with authorized apps and services through utility-provided Green Button Connect My Data implementations." |

## Gate rulings

- **60 million vs 40 million is not a contradiction and must not be merged.** The Department of Energy figure is what signatories *committed* to cover; the Green Button Alliance figure is live Connect My Data access. The article prints both with their owners (row 5 and row 7) and says the gap measures how much of the promise got built.
- **The hourly floor is prose, not a row.** Row 3's sentence carries no numeric token, so `figure_evidence` cannot match it; it is quoted above, it lives on the page rows 1–4 already verify, and the draft cites [1] for it. No separate gate row was invented to carry it.
- **No price is cited anywhere in this piece.** No retail host answered the verifier this round (Emporia and Shelly unreachable; `sparkfun.com` serves a CT sensor, not a whole-home kit), so the decision is settled on information rather than on a payback, and the draft says so.
- **No 15-minute interval is claimed.** The EIA floor is hourly; finer intervals exist at some utilities but no page fetched today states one, so the unit is the hour and every derived count follows from it.
- **Derived arithmetic (recompute in the final, never copy):** 365 × 24 = 8,760 rows a year; 365 × 24 × 60 × 60 = 31,536,000 at one sample a second, which is 3,600× the hourly series; 119 million ÷ 0.72 ≈ 165 million total meters, stated as derived only and never printed as a published count.

## Removed

- A "your utility must give you the data" claim — REMOVED. The EIA definition describes what an advanced meter does; it does not oblige a utility to serve the file. The draft says "a program that covers 40 million accounts is not every meter in the country".
- A dollar payback for the clamp kit — REMOVED. No fetched source prices one.
- A 15-minute or real-time interval claim — REMOVED. Not on any fetched page.
