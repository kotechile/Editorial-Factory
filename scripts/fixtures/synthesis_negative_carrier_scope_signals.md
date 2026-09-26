# Signals: supply_chain — fixture (negative: "carrier" must not fire the insurance pattern)

**Window:** 2026-08-18 → 2026-09-17
**Provenance:** rows copied verbatim from `context/recon_proposals/2026-09-17_supply_chain_signals.md`.
Regression guard: rows 1 and 5 share an ocean `carrier` and a claims `mitigation` across two
different domains, which the pre-rewrite engine paired into "The Uninsurable Suburb" for a
logistics vertical. Expected result now: zero validated pairs. Do not edit the URLs.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Samsung Electronics America files FMC complaint against CMA CGM S.A. (Docket No. 26-12), seeking ≥$186M in reparations over alleged unlawful demurrage/detention/rail-storage charges | https://www.federalregister.gov/documents/2026/09/04/2026-18122/ | 2026-09-04 (served 09-01) | $186M total; $148M improper D&D/rail charges + $8.1M mitigation + $30M prejudgment interest; 121,000+ charges paid | Detention/demurrage dispute as cost-recovery weapon under OSRA-22 | 88 |
| 5 | C.H. Robinson September freight update: ocean vulnerable to typhoon congestion/blank sailings; LTL excess capacity fading | https://www.chrobinson.com/en-us/resources/insights-and-advisories/north-america-freight-insights/sep-2026-freight-market-update | 2026-09 (monthly) | LTL carrier-fit now material; no conventional peak | Capacity tightening | 60 |
