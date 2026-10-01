# Signals: home_ops_execution — 2026-10-01
**Window:** 2026-09-01 → 2026-10-01
**Queries run:** 12 (home_lifestyle_intel `--recent 30` + 11 web-fallback sweeps: icc_safe_codes, ashrae_standards, contractor_talk, journal_light_construction, reddit_home, plus contractor-licensing / lien / retainage / permit / HVAC-refrigerant / water-heater angles)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | EPA AIM Act R-410A install-deadline rollback finalized; "no action assurance" lapsed Sept 1 | https://www.federalregister.gov/documents/2026/05/26/2026-10387/phasedown-of-hydrofluorocarbons-reconsideration-of-certain-regulatory-requirements-promulgated-under | 2026-09-01 | EPA final rule (effective 2026-07-27) lets contractors install R-410A split systems manufactured before Jan 1, 2025; EPA "no action assurance" (Dec 22, 2025) lasted "until September 1, 2026, or until this rule is finalized, whichever comes sooner" | HVAC refrigerant transition / PM runbooks | 65 |
| 2 | DOE commercial gas water heater condensing mandate — effective Oct 6, 2026; 1-year enforcement delay | https://www.phccweb.org/news/u-s-department-of-energy-efficiency-standards-for-commercial-water-heaters-effective-in-less-than-six-months | 2026-10-06 | All commercial gas water heaters must be condensing (storage TE 80%→95%, instantaneous 80%→96%; residential-duty commercial >75k BTU/hr UEF 0.9297); DOE enforcement policy (Apr 24) suspends civil penalties Oct 6 2026–Oct 5 2027 | annual PM vendor contracts / appliance lifecycle | 60 |
| 3 | ICC 2027 IBC/IFC/IWUIC published Sept 2026 (off-site construction + 500-yr floodplain) | https://builder.media/2026/09/icc-finalizes-2027-building-codes | 2026-09-30 | 2027 I-Codes publish in stages — IBC/IFC/IWUIC Sept 2026, IRC Feb 2027; ICC/MBI 1200/1205/1210 off-site standards; flood-resistant design extends to 500-year floodplain | permitting / code changes | 68 |

**Dropped (< 60 intensity or out-of-window):**
- **California Civil Code § 8811 / § 8850** — 5% retainage cap + payment-dispute resolution for private construction, effective **Jan 1, 2026** (the single most on-vertical development for the "SOW + retainage escrow" angle, but ~9 months old, out of window; do NOT widen past 45 days to smuggle it in — `radar_30day.md` §4).
- **Ohio HB 614** — first statewide Home Improvement Contractor Registration (OCILB), effective Jan 1, 2026. Out of window.
- **Florida § 489.1295 "Prohibition Against Nonpayment"** — contractor licensing risk on payment disputes, effective July 1, 2026. Out of window.
- **Louisiana Act 757** — contractor license insurance requirements, effective Aug 1, 2026 (one day pre-window). Out of window.
- **CSLB statewide sting "142 legal actions"** — surfaced by search but the source article is dated **Aug 4, 2022** (El Dorado DA) — stale, not a fresh signal.
- **California SB 779 / Georgia SB 553 / Florida HB 803 / Washington 2SHB 1534** — the July 1, 2026 contractor/permitting law wave already swept and dropped in the 09-24 first run; retreads, out of window.
- **home_lifestyle_intel MCP**: 10 items across 4 categories — **zero** map to contractor/permitting/lien/HVAC-diagnostic angles (same as 09-24; this vertical must lean on web fallbacks).

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=3 candidates=0 heuristic=- window=2026-09-01..2026-10-01 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
