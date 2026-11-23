# Evergreen run: home_infrastructure_lifecycle_tco — 2026-11-23 — NO PUBLISH

**Verdict: no publish.** Every candidate came from the skill §2 evidence leads (primary_angles,
founder-voice §3, customer-truth anecdotes, the home_lifestyle_intel feed, GSC bonus signal —
0 opportunities, the documented young-site status, never a veto) and every one was refused by
the de-dup rule or failed the Evidence axis. Scores logged to `skills/self_improvement_eval.md`.
No gate was run and no gate marker was written: there is no brief to gate.

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Water-heater replacement timing under the May 6, 2029 UEF 2.30 electric floor (ecfr 10 CFR 430.32(d); ENERGY STAR $550/yr + $5,610 lifetime household-of-4; A.O. Smith 8–12-year service life) | 9 | 9 | 8.5 | 9 | 8.9 | **refused by hand — retread of `published/2026-10-26_you-are-pricing-the-fuel-not-the-tank.md`** (same vertical, same 2.30 floor, same May 6, 2029 build date, same 0.9307−(0.0002×V) formula, even the same 1,000-cubic-feet room constraint); the sibling `home_equity_tco` evergreen run TODAY (2026-11-23 `your-heat-pump-quote-buys-the-floor`) also anchors on 10 CFR 430.32 |
| Solar PV payback after the §25D credit termination (26 U.S.C. §25D(h) — expenditures after December 31, 2025 excluded; Cornell LII, fetched) ⨂ EIA 17.30¢/kWh residential 2025 (fetched) | 8 | 8 | 3.5 | 8 | 5.9 | dropped — the load-bearing installed-cost-per-watt figure has no fetchable primary (`pvwatts.nrel.gov`, `empower.lbl.gov/tracking-the-sun`, `openei.org` all unreachable; SEIA report page carries no $/W; energy.gov carries only a resale-premium figure), so no payback arithmetic can be earned |
| Sinking fund vs HELOC on the $18k roof (customer-truth Anecdote 2; founder-voice 1.5% reserve) | 8 | 6 | 3 | 7 | 6.1 | dropped for the third time — the financing-rate figures have no fetchable primary (`fred.stlouisfed.org` unreachable per the 2026-11-09 run; the 1.5% and 8.5% figures are corpus assertions, not gate rows) |
| Attic air-sealing / insulation R-value by climate zone | 8 | 7 | 4 | 8 | 6.8 | dropped again — the requirements sit in the IECC, not on a fetchable host; `energy.gov/energysaver/*` paths 404 to the verifier (casebook, confirmed 2026-10-13) |
| Smart irrigation rate hedge; battery payback; panel-upgrade 80% rule; replacement windows | — | — | — | — | — | not re-scored — each is a published artifact's own thesis (`2026-10-05_smart-irrigation-payback-water-tier`, `2026-10-12_battery-payback-five-state-gap` + home_equity_tco `2026-10-26_your-battery-payback-0-or-38`, `smart_home_telemetry` `2026-10-13_panel-upgrade-80-percent-test`, this vertical's `2026-10-12_windows-13-percent-best-case`) |

## What the run verified en route (reusable evidence)
- `ecfr.gov/current/title-10/.../section-430.32` fetches (96 KB) and carries both the pre-2029
  electric-storage Medium row `0.9307 − (0.0002 × V r)` and the on/after May 6, 2029 flat
  `2.30` row — verified with `figure_evidence`, both clean.
- `energystar.gov/products/heat_pump_water_heaters` fetches (7.9 KB; 40°–90°F, 1,000 cubic feet)
  and `…/benefits-savings` fetches (3.0 KB; $550/yr, $5,610 lifetime, 13-year lifespan, $1,503
  incremental, payback table by household size) — the two HPWH pages this desk needs are both
  reachable, unlike the guessed `/savings_and_benefits` subpath (unreachable).
- `hotwater.com/info-center/when-to-repair-or-replace.html` fetches (19 KB) and carries "8 to 12
  years" as the manufacturer's suggested service life — but a row cell leading on `8 to 12 years`
  evidences on the reCAPTCHA key's stray `8` in the page header; lead the cell on `12 years`,
  which windows on the operative sentence.
- `law.cornell.edu/uscode/text/26/25D` fetches and carries the termination (§25D(h),
  Pub. L. 119–21 § 70506(a)): "expenditures made after December 31, 2025".
- `eia.gov` energy-explained electricity prices: fetched, residential 17.30¢ (2025).
