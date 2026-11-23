# Run detail: home_equity_tco evergreen — 2026-11-23 your-heat-pump-quote-buys-the-floor

Topic: the federal minimum-efficiency floor (7.5 HSPF2 / 14.3 SEER2, 10 CFR 430.32) as the
worst machine you can legally buy, with duct leakage (15–20% of space-conditioning energy,
InterNACHI) eating the upgrade premium; the $2,000 25C credit window through Dec 31, 2032.
Angle 3 (heat pump COP/tariff) — the COP half was previously dropped (2026-10-26, no fetchable
COP page); this run anchors on the statutory floor instead.

Evidence: 5 rows, 4 hosts (ecfr.gov, energystar.gov, eia.gov ×2, nachi.org), all figures
verified with figure_evidence before the gate; gate PASS 18:38 UTC, marker written.
De-dup: nearest prior evergreen 2026-11-09_your-pmi-ends-at-78-not-todays-value; cross-vertical
heat-pump artifacts (2026-11-02_your-heat-pump-cuts-everyone-13, 2026-11-23_your-fuel-decided-your-winter-bill)
checked and dropped — different mechanisms.

Pipeline: draft pre-tuned (critic PASS, accessibility PASS); headline final
"Your Heat Pump's 20% Silent Leak" scored 100 STRONG (lead_ok False = 2 allowed absents).
Review HELD once: reviewer cut the internal link claiming cross-vertical, and left the
held title at 58 WEAK. Hand repair (per casebook: a hold with hard=0 is a flow regression):
re-added the same-site link (/your-fuel-decided-your-winter-bill/), restored the 100-score
title, fixed the bullet lead-in, promoted to _final. Gate 8/8 PASS.

Publish: CMS post 473, media 472, Supabase e20a8a37, 3 generated internal links + 1 earned
inline; front built and verified live (hero, -1024x576 derivative, og:image, all 4 link
targets resolve). run_pipeline finish fails on pre-existing defects owned by other verticals
(3 voice problems in agentic_ai drafts, 4 illustration_overlay test failures).
