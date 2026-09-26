# Signals: expat_cross_border_relocation — 2026-09-24

**Window:** 2026-08-25 → 2026-09-24 (30 days)
**Vertical:** Advanced Expat, Cross-Border & Multi-Jurisdictional Relocation
**Target persona:** cross_border_expat
**Queries run:** 18 (IRS/OECD/PwC tax, FEIE/FTC, remote-work PE nexus, digital-nomad visas, expat healthcare, cost-of-living, tax residency/split-year, residence-based taxation, UK non-dom→FIG, Numbeo mid-year)

**Verdict:** Weak cycle — every candidate's load-bearing figure is anchored OUTSIDE the 30-day window (anchor-driven vertical; configured sources publish annually/quarterly).

## Candidate table

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity | In-window? |
|---|--------|-----------|------|--------------|-------|-----------|-----------|
| 1 | 2026 Expat Health Barometer ("insured but not protected" gap) | april-international.com / expatcommunication.com | survey fielded Apr 28–May 19, 2026; **results Jun 3** | 93% have health cover, yet 53% delayed/forgone care; 51% cite insufficient reimbursement, 48% high cost; 6,400+ expats / 80+ countries | healthcare economics | 74 | **NO** (anchor ~3 mo old) |
| 2 | Cigna 2026 International Health Study (Evernorth Vitality Index 68.9) | cignaglobal.com | Mar 25 / Apr 1, 2026 | 11,000 respondents, 1,900 globally mobile across 13 markets; vitality advantage vs loneliness/stress | healthcare/mobility | 62 | NO (Mar–Apr) |
| 3 | OECD Model Tax Convention 2025 Update — remote-work PE 50% safe-harbor + commercial-reason test | oecd.org | Nov 19, 2025 | 50% working-time threshold below which remote work generally doesn't trigger PE | remote-work tax nexus | 68 | NO (Nov 2025) |
| 4 | Residence-Based Taxation for Americans Abroad Act (LaHood / Sen. Young) | taxfairnessabroad.org; greenbacktaxservices.com | freshest dev Jun 17, 2026 | bill awaits reintroduction + JCT score; ACA comments to Senate Finance Jun 17 | FEIE/FTC / dual-jurisdiction | 58 | NO (Jun; process story) |
| 5 | UK non-dom abolished → FIG regime (4-yr) + Temporary Repatriation Facility 12% | gov.uk; alto-accounting.com | regime effective Apr 6, 2025; TRF 12% 2025/26–2026/27 | 12% reduced rate for pre-Apr-2025 FIG remittances; no credit for US tax paid (double-tax mismatch for US expats) | dual-jurisdiction compliance | 57 | NO (Apr 2025) |
| 6 | Henley Private Wealth Migration Report 2026 (142k→165k) | henleyglobal.com; drumelia.com | Feb 2026 | 165,000 millionaires projected to relocate 2026; UK net outflow 16,500 | wealth migration | 55 | NO (Feb 2026) |
| 7 | Numbeo 2026 Mid-Year Cost of Living Index | numbeo.com | ~Jul 2026 (continuous) | US 69.7 / UK 68.2 / Portugal 48.7 (country index); no discrete news event | cost-of-living | 52 | NO (borderline; live index, not a spike) |
| 8 | FEIE 2026 = $132,900 (Rev. Proc. 2025-32) | irs.gov | Oct 2025 | FEIE $130,000→$132,900; housing $39,870; SS wage base $184,500 | FEIE/FTC optimization | 50 | NO (Oct 2025) |
| 9 | Digital nomad visa expansions (Bulgaria new, Slovenia new 2026, Philippines upcoming) | freelancermap.com; relocateme.substack.com | rolling 2026 | evergreen roundup; no single in-window primary event | relocation / visas | 48 | NO (roundup) |
| 10 | Beancount "183-Day Rule Won't Save You" (FEIE ≠ SE-tax exemption) | beancount.io | Sep 14, 2026 | FEIE excludes income tax only, NOT the 15.3% self-employment tax | FEIE/FTC | 45 | YES (but blog, secondary — no primary anchor) |

## Anchor-driven cadence note
This vertical's configured sources are all periodic anchors:
- `irs_international_bulletins` → annual Rev. Proc. (October); next FEIE figure (2027) expected ~Oct 2026.
- `oecd_tax_reports` → annual Model Convention update (Nov 2025 was the last; next likely late 2026).
- `pwc_global_mobility` → annual survey (Jan 2026 last).
- `numbeo_cost_of_living` → live/continuous index; "mid-year" (~Jul) and "year-end" (~Dec) releases.
- `international_living` / `nomad_capitalist_audits` → evergreen/opinion, no discrete news spikes.

The only genuinely in-window items (Sep 14 Beancount, Sep 22 Numbeo Instagram) are secondary/aggregator content with no primary-source news anchor — below the Intensity-60 floor and non-defensible for a zero-hallucination piece.

## Watch-items for next cycle (Q4 2026)
- **IRS Rev. Proc. 2026-xx (~Oct 2026):** FEIE 2027 inflation adjustment — the single most likely fresh ≥8 primary (annual anchor; directly load-bearing for the FEIE/FTC angle and cross_border_expat persona).
- **OECD/G20 tax:** any fresh Model Convention commentary or PE-rule clarification.
- **PwC/KPMG global-mobility surveys** (annual, ~Jan).
- **Numbeo year-end Cost of Living Index (~Dec 2026).**
- **UK Budget / FIG regime** follow-ups (TRF rate steps to 15% in 2027/28 — a concrete in-window trigger if announced fresh).
