# Signals: expat_cross_border_relocation — 2026-10-01

**Window:** 2026-09-01 → 2026-10-01 (30 days)
**Vertical:** Advanced Expat, Cross-Border & Multi-Jurisdictional Relocation
**Target persona:** cross_border_expat
**Queries run:** 16 (IRS international bulletins / FEIE 2027 / 2026-32 inflation adjustments, OECD remote-work PE, PwC & Deloitte global-mobility surveys, UK non-dom→FIG / TRF, Portugal NHR→IFICI, Spain Beckham Law / digital-nomad tax, digital-nomad visa changes, expat healthcare / iPMI, remote-work tax-nexus enforcement, Numbeo cost-of-living)

**Verdict:** Weak cycle (second run) — the window advanced only ~7 days since the 2026-09-24 first run, and the single acute watch-item (the official IRS Rev. Proc. 2026-xx carrying the FEIE 2027 figure) has **not** landed yet. Every load-bearing figure still anchors outside the 30-day window; the one fresh in-window item is a secondary *projection* of un-released official figures, not a primary spike.

## Candidate table

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | 2027 federal tax-bracket projections on a broken CPI series — 2025 government shutdown deleted Oct 2025 CPI | https://www.wolterskluwer.com/en/expert-insights/projected-2027-federal-tax-brackets | 2026-09-18 | Wolters Kluwer CCH projects 2027 standard deduction $33,200 (joint) / $16,600 (single) / $24,950 HoH; BLS never published Oct 2025 CPI because of the 2025 shutdown, so 2027 inflation adjustments use an 11-month average (Sept 2025–Aug 2026) instead of the statutory 12-month average; "not clear how the IRS intends to handle this missing month"; official 2027 figures (incl. FEIE) due late Oct/early Nov | FEIE/FTC dual-jurisdiction planning / inflation-adjustment uncertainty | 68 |

## Corroborating / sub-floor (not standalone candidates)

- **Thomson Reuters Checkpoint "Key 2027 figures calculated… now available"** (Sept 2026) — same 11-month-CPI mechanism; projects 2027 standard deduction $33,200 joint / $16,600 single / $24,900 HoH; explicitly "These 2027 inflation-adjusted tax numbers are Thomson Reuters estimates. The IRS will publish official figures later this year." Links "transfer tax and foreign items" (the FEIE bucket) behind a checkpoint.riag.com paywall. **Same axis as #1 (secondary projection of un-released figures) — no standalone candidacy, no crisp FEIE number in the free text.**
- **IRS Rev. Proc. 2026-24 (IRB 2026-25)** — the *first official* 2027 inflation-adjusted figure released: HSA limits $4,500 self-only / $9,000 family. Fresh and primary, but HSA-specific and tangential to this vertical's FEIE/FTC/healthcare angles → below the Intensity-60 floor for this vertical. Its significance is as a signal that the IRS is *starting* to release 2027 amounts piecemeal, with the main Rev. Proc. (FEIE, brackets, standard deduction) still pending.

## Dropped (out-of-window anchors or secondary explainers — do NOT widen past 45 days, `radar_30day.md` §4)

- **IRS Rev. Proc. 2025-32 (FEIE 2026 = $132,900)** — Oct 2025. Out of window. (The 2027 figure is what this vertical is waiting on.)
- **OECD Model Tax Convention 2025 Update — remote-work PE 50% safe-harbor** — Nov 18, 2025. Out of window. KPMG GMS Flash Alert 2026-176 (US/Argentina apply the guidance) is July 14, 2026 — also out of window.
- **UK non-dom → FIG regime + Temporary Repatriation Facility 12%** — regime effective Apr 6, 2025; TRF 12% (2025/26–2026/27) steps to 15% (2027/28). No fresh discrete in-window event; Blick Rothenberg "Autumn Budget 2026" tag is a topic bucket, not a confirmed new announcement.
- **PwC Belgium Annual Mobility Report 2026** — May 4, 2026. Out of window.
- **Deloitte global mobility survey "Travel and remote work"** — May 11, 2026. Out of window.
- **Henley Private Wealth Migration Report 2026** — Feb 2026. Out of window.
- **Portugal NHR → IFICI (NHR 2.0)** — original NHR closed Apr 1, 2025; Skybound Wealth "Portugal After NHR (2026)" is Sept 11, 2026 but a secondary wealth-management explainer with no new primary figure.
- **Spain Beckham Law / digital-nomad tax** — Klevvera "Taxes for Digital Nomads in Spain 2026: The Real Cost" is Aug 28, 2026 (4 days pre-window); otherwise evergreen explainer content, no new regulation.
- **Digital-nomad visa roundups** (Bulgaria/Slovenia/Moldova new 2026) — evergreen aggregator roundups, no single in-window primary event.
- **Expat healthcare / iPMI** — no fresh survey wave; iPMI Global event/marketing content, not a re-fielded survey.

## Anchor-driven cadence note

This vertical's configured sources are all periodic anchors (`irs_international_bulletins` → annual Rev. Proc., October; `oecd_tax_reports` → annual Model update, Nov; `pwc_global_mobility` → annual survey, Jan; `numbeo_cost_of_living` → mid-year / year-end; `international_living` / `nomad_capitalist_audits` → evergreen/opinion). A weekly re-run whose window advanced ~7 days will legitimately find no fresh primary spike — the correct outcome is "no publish", not a widened window.

## Watch-items for next cycle (Q4 2026)

- **IRS Rev. Proc. 2026-xx (~late Oct / early Nov 2026):** the official FEIE 2027 inflation figure — the single most likely fresh ≥8 primary (annual anchor, directly load-bearing for the FEIE/FTC angle and the cross_border_expat persona). The 2025-shutdown missing-CPI wrinkle makes *this* year's figure unusually consequential: watch whether the IRS publishes on an 11-month vs 12-month CPI average.
- **Numbeo year-end Cost of Living Index (~Dec 2026).**
- **PwC / KPMG / Deloitte global-mobility surveys (Jan 2027).**
- **Fresh Expat Health Barometer wave** — the "93% insured yet 53% delayed/forgone care" gap is this vertical's most shareable thesis; re-run the moment a new wave lands in-window.
- **UK Autumn Budget 2026 / FIG follow-ups** — TRF rate step to 15% in 2027/28 is a concrete in-window trigger if announced fresh.

## Candidate Synthesis Pairs



<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=1 candidates=0 heuristic=- window=2026-09-01..2026-10-01 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

