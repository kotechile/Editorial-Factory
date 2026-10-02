# Signals: career_velocity_equity_engineering — 2026-10-02
**Window:** 2026-09-02 → 2026-10-02
**Queries run:** 12 (Carta equity/comp reports, Levels.fyi comp data, secondary-market volume & pricing, 409A / down-round, severance / unvested equity, PTEP exercise windows, QSBS / 1202 tax, AI-equity premium, IPO/exit liquidity)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Nasdaq Private Market unveils PAM™ AI investing agent | https://www.nasdaq.com/press-release/nasdaq-private-market-unveils-pamtm-ai-agent-cracking-open-private-markets-everyone | 2026-09-17 | 40M+ Americans qualify as accredited investors but only 4.3% invest in private markets (3x that number express interest); private market peaked >$5T in early 2026; NPM has executed >$80B in secondary volume | Liquidity access productized for investors | 72 |
| 2 | Oracle layoff package cancels unvested equity | https://www.calcalistech.com/ctechnews/article/1kwjft2um | 2026-09-23 | Unvested RSUs/options canceled at termination; 26-week severance cap; 3-mo (or 1-mo) exercise window; ~21k positions cut FY26, $2.8B restructuring | Cliff forfeiture / unvested equity | 82 |
| 3 | JPMorgan: 3 changes to qualified small business stock (QSBS) | https://www.jpmorgan.com/insights/business-planning/qsbs-planning-tax-benefits-qualifications-and-strategy | 2026-09-22 | QSBS holding period 5yr→3yr (partial), gross-assets ceiling $50M→$75M, exclusion cap $10M→$15M per taxpayer/issuer (One Big Beautiful Bill Act) | Equity tax planning / liquidity math | 66 |
| 4 | Levels.fyi comp medians updated (Microsoft/Google) | https://www.levels.fyi/companies/google/salaries/software-engineer | 2026-09-30 | Google median total comp $305k; Microsoft $233k; Meta E5 $478k; AI-specialized SWEs pull 43–56% premium over generalists | Comp baseline — evergreen rolling aggregate | 62 |

**Dropped (< 60 intensity or out-of-window):**
- **EquityZen Q2 2026 "tale of two markets"** — average secondary trade at **38% discount** to last round (vs 8% in Q1); 98.5% of volume in mature 6+yr companies; secondaries projected $250B in 2026. Sharpest data point for the "your startup equity is worth less than the headline" thesis, but published **July 9, 2026** — out of window; do NOT widen past 45 days (`radar_30day.md` §4).
- **Carta "AI shifts in compensation"** (Apr 8, 2026) — median equity grant for AI/ML engineers +59% (Jan 2024→Feb 2026) at $1M–$10M startups, +30% at $25–50M. Out of window; the underlying trend is durable but the anchor is April.
- **NPM "Secondary Scene 2026 Outlook"** (Mar 31, 2026) — tenders $35B in 2025 (vs $45B IPO); ~50% of tender programs Series A–C (up from 30%); 132-day avg between tenders (down from 899 in 2022); 60% oversubscribed. Rich liquidity data, but a March report — out of window.
- **Meta 2026 refreshers −5%** (FT, Feb 2026) — after −10% in 2025. Out of window.
- **Uber layoffs 3,300** (Sept 2, 2026) — fresh but generic mass-layoff; no primary equity-specific figure beyond headcount; weak fit for the equity/offer persona.
- **Cerebras (May 14) / Kraken (S-1 Nov 2025, IPO paused → 2027)** — exit-moment stories all out of window; Kraken secondary pricing slid to ~$9.6B implied (Aug 2026, Forge $29.41/share) but the S-1 is Nov 2025.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=0 heuristic=- window=2026-09-02..2026-10-02 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
