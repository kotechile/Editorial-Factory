# Evergreen Brief: personal_microeconomics_tinkering_tax — 2026-11-21
**Archetype:** evergreen
**Vertical:** personal_microeconomics_tinkering_tax
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** Whether to spend a weekend scripting an automation for a small recurring task (file cleanup, backup nudge, dashboard refresh) instead of doing it by hand or paying a managed tool — a decision that arrives the moment the task annoys a third time and the editor is already open.
**Durability:** The break-even equation is arithmetic on the reader's own minutes, not a market fact: it stays correct for years as long as the inputs are dated. O*NET's $47.66 hourly median wage is the 2025 figure, "as of" the May-2025 O*NET update pulled 2026-11-21; the 48.0% maintenance share is the 1978 Lientz-Swanson survey as quoted on the fetched page; Zapier Professional is $19.99/month as of 2026-11-21 (vendor list price, dated in the article).
**De-dup:** `2026-10-10_self-hosting-break-even-one-hour-a-year` is this vertical's nearest prior artifact: it divides a managed subscription fee by the O*NET wage to price self-hosting *labour*, and it prices an always-on service, not a one-off script. This brief prices the *build-versus-repeat equation of hobbyist automation itself* — the threshold minutes-per-week at which a script out-earns its own maintenance, and the upkeep-hour count at which a managed tool wins. Also checked and distinct: `2026-10-07_automation-payback-splits-by-sku-geometry` (warehouse robot capex, a different vertical's fleet math), `2026-10-31_your-standby-bill-hides-62-watts` (electricity audit; it shares the O*NET wage anchor but divides an audit's first-year saving, not a script's build time), and today's news artifact `2026-11-21_your-ram-kit-costs-22-filament-spool` (component price ratios). Cross-vertical grep for "zapier", "script", "automate" and "break-even" returns no published artifact arguing this mechanism.
**Thesis:** A hobbyist script has to out-earn its own maintenance before it earns anything: at a 30-minutes-a-quarter upkeep habit, a 2-minute weekly task never breaks even — the threshold is roughly 4 minutes a week over a 5-year life — and once DIY upkeep passes about 5 hours a year, the managed tool's $19.99/month is cheaper in hours.

**Lead:** Founder-voice pillar §3 "The Hobbyist Automation ROI Equation" (context/growth_os/founder-voice.md:238) plus the persona's stated want "hobbyist automation roi calculator setup time vs manual execution" (context/personas.json systems_tinkerer_pro.wants). No GSC anchor used; the vertical's demand signal is thin on this surface.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | O*NET OnLine, 15-1244.00 Network and Computer Systems Administrators | https://www.onetonline.org/link/summary/15-1244.00 | 2026-11-21 | 47.66 — $47.66 hourly median wage (2025), the loaded rate the script's DIY hours bill against | measured |
| 2 | EltexSoft, "Software maintenance cost per year", quoting the 1978 Lientz & Swanson survey of 69 data processing organizations | https://eltexsoft.com/blog/software-maintenance-cost | 2026-11-21 | 48.0% — 48.0% of annual staff hours went to maintaining and enhancing existing systems, so upkeep, not building, dominates a script's life | measured |
| 3 | Zapier pricing page | https://zapier.com/pricing | 2026-11-21 | 19.99 — Zapier Professional starts from $19.99/month, the managed alternative priced in hours at the O*NET wage | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The hobbyist automation break-even equation (script vs manual vs managed) | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Quarterly zero-based subscription audit framework (the 4-sessions-in-30-days rule) | 8 | 8 | 5 | 7 | 7.2 | dropped — the audit-benchmark anchors are vendor telemetry, not fetchable primary measurement |
| True unit economics of 3D printing (nozzle wear, support waste, electricity) | 7 | 8 | 6 | 8 | 7.3 | dropped — today's news artifact `2026-11-21_your-ram-kit-costs-22-filament-spool` already owns the filament-price mechanism this week |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=3 fetched=3 sources=3 hosts=3 decision="sha1:95aa16e68a" dedup="matched a prior artifact: 2026-10-10_self-hosting-break-even" window_days=180 checked_at=2026-11-21T17:34:36+00:00 -->
<!-- evergreen-gate:end -->
