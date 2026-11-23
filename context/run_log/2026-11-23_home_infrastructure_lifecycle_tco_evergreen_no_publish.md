# Run detail: home_infrastructure_lifecycle_tco — evergreen — 2026-11-23 — NO PUBLISH

Verdict: no publish. No brief written, no gate run, no marker, no draft, no spend beyond probes.

Candidates (full scoring in context/recon_proposals/2026-11-23_home_infrastructure_lifecycle_tco_evergreen_no_publish.md):

1. **Water-heater replacement timing under the May 6, 2029 UEF 2.30 electric floor — 8.9, refused by hand.** Evidence fully verified (ecfr 10 CFR 430.32(d) both rows clean; ENERGY STAR $550/yr household-of-4, $5,610 lifetime, $1,503 incremental, 13-year lifespan; A.O. Smith 8–12-year service life; 3 hosts) but the mechanism is the published thesis of `2026-10-26_you-are-pricing-the-fuel-not-the-tank.md` in this same vertical — same 2.30 floor, same May 6, 2029 build-date rule, same 0.9307−(0.0002×V) formula, same 1,000-cubic-feet room constraint — and today's `home_equity_tco` evergreen winner anchors on the same statute page.
2. **Solar PV payback after the §25D termination — 5.9, dropped on evidence.** §25D(h) (expenditures after December 31, 2025) verified on Cornell LII; EIA 17.30¢/kWh verified; the installed-cost-per-watt leg has no fetchable primary (pvwatts.nrel.gov, empower.lbl.gov, openei.org unreachable; SEIA page carries no $/W), so no payback arithmetic can be earned.
3. **Sinking fund vs HELOC — 6.1**, dropped for the third time (no fetchable financing-rate primary).
4. **Attic insulation — 6.8**, dropped again (IECC unreachable; energysaver paths 404).
5. **Irrigation / battery payback / panel 80% / windows** — published retreads, not re-scored.

Lessons recorded via learn.py: pitfall (grep the corpus for subject tokens before probing hosts) + 3 host rows (energystar HPWH pages, hotwater.com with the `12 years` matcher trap, Cornell §25D).
