# Evergreen Brief: expat_cross_border_relocation — 2026-10-08
**Archetype:** evergreen
**Vertical:** expat_cross_border_relocation
**Persona:** cross_border_expat
**Decision the reader is facing:** How to time the move — and the first return trip — so the US exclusion clock and the host country's residency clock stop disagreeing, and the relocation ("split") year is not taxed twice.
**Durability:** The load-bearing mechanics are statutory, not annual: the US Physical Presence Test's 330 full days in any 12 consecutive months (IRC §911(d)(1)(B)), the 16% base housing amount tied to the exclusion cap, and the UK's 183-day automatic residency test are as of the 2025–26 tax year and do not expire; only the annually indexed dollar cap changes, and this piece deliberately does not lead on that figure.
**De-dup:** Nearest prior artifact for this vertical is 2026-10-08_expat_cross_border_relocation_angle_brief (a news-cycle brief whose load-bearing signal was the annual FEIE-2027 figure and the Dutch 30%→27% ruling; it returned no publish). This differs — it is a durable two-clock timing piece and leads on no year-specific dollar amount.
**Thesis:** The expensive expat-tax mistake is not FEIE versus FTC; it is that the US qualification clock (330 foreign days in a rolling 12-month window) and the host country's residency clock (e.g. the UK's 183 UK days in a tax year) count different days — so the relocation year lands in the seam between them and can be taxed on both sides.

**Lead:** Persona `cross_border_expat` wants (context/personas.json): "FEIE vs FTC optimization … bilateral tax treaties"; vertical `primary_angles` #1 "the true cost of dual-jurisdiction compliance feie and ftc optimization"; `context/growth_os/founder-voice.md` §3 expat angle #1 ("split-year tax residency triggers"); `context/growth_os/customer-truth.md` expat anecdote #1 (the $42k split-year double-tax on a US→UK move where the two residency start dates were never synchronized).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | IRS, Publication 54 (Tax Guide for U.S. Citizens and Resident Aliens Abroad) | https://www.irs.gov/publications/p54 | 2026-10-08 | 330 full days — the Physical Presence Test requires presence in a foreign country for 330 full days during a period of 12 consecutive months | measured |
| 2 | 26 U.S.C. §911 (Cornell Legal Information Institute) | https://www.law.cornell.edu/uscode/text/26/911 | 2026-10-08 | 330 full days — the statute's own test: present in a foreign country "during at least 330 full days" in any period of 12 consecutive months | measured |
| 3 | HM Revenue & Customs / GOV.UK, "Tax on foreign income: residence" | https://www.gov.uk/tax-foreign-income/residence | 2026-10-08 | 183 days — the UK automatic UK test treats you as resident if you spend 183 or more days in the UK in the tax year (plus the split-year treatment conditions) | measured |
| 4 | IRS, "Foreign Housing Exclusion or Deduction" | https://www.irs.gov/individuals/international-taxpayers/foreign-housing-exclusion-or-deduction | 2026-10-08 | 16% — the base housing amount is 16% of the maximum exclusion, divided by 365 (366 in a leap year) and prorated by qualifying days | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The two-clock seam: the US 330-day FEIE window versus the host country's 183-day residency tax year | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| FEIE versus the Foreign Tax Credit: which to elect, given you cannot claim both on the same income | 8 | 9 | 7 | 8 | 8.0 | held — the load-bearing "no double benefit" rule has no fetchable distinctive numeric anchor this run (the statute carries only a section number, not a figure) |
| IPMI versus local state care: the out-of-pocket healthcare math for a new arrival | 8 | 8 | 5 | 7 | 7.1 | dropped — no fetchable primary carrying a distinctive figure this run (oecd.org is unreachable to the verifier) |

## Notes on the evidence
- Hosts are deliberately spread: `irs.gov`, `law.cornell.edu` and `gov.uk` — the two IRS pages are distinct documents (the publication vs the housing help page), not one page wearing a costume.
- The article must state the US `330`-day rule and the host `183`-day rule as the two clocks, and the `16%` housing base as the reason the exclusion is not the whole story; it must NOT lead on the annually indexed dollar cap (that is a news fact, and it is what the news brief for this vertical already watches).
- Field anecdote to anchor the tension: customer-truth.md §expat anecdote #1 — a US executive who moved to the UK in September, never synchronized the two residency start dates, and hit a $42,000 cash-flow deficit from IRS Form 1116 credit carryover timing against HMRC self-assessment deadlines.

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=3 decision="sha1:8c6862fb93" dedup="matched a prior artifact: 2026-10-08_expat_cross_border_relo" window_days=180 checked_at=2026-10-08T19:34:05+00:00 -->
<!-- evergreen-gate:end -->
