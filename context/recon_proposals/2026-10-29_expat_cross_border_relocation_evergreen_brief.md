# Evergreen Brief: expat_cross_border_relocation — 2026-10-29
**Archetype:** evergreen
**Vertical:** expat_cross_border_relocation
**Persona:** cross_border_expat
**Decision the reader is facing:** Which dollar value goes on this year's US return for foreign pay and foreign tax paid — and whether the exclusion's $130,000 cap is already used up before a single rule about the exclusion applies.
**Durability:** The rule set is statutory and does not expire: income is translated at the rate prevailing when it is received, paid or accrued; accrued foreign tax may use the yearly average unless one of three exits applies; tax actually paid — and any refund of it — is translated at the payment-date rate; a currency crossing the inflation floor is forced to the year-end rate. The numbers are dated: IRS yearly averages as of the 2025 tax-year table (page last reviewed 17 September 2026), the ECB reference rate as of 29 October 2026, the Federal Reserve H.10 as of 19 October 2026, and the Form 1116 conversion instructions as of the current published edition. A reader in twelve months still needs the method; only the rates move, and every one of them is printed here with its date.
**De-dup:** `2026-10-22_your-130000-cap-costs-the-credit` is this vertical's nearest prior artifact (seven days ago), and it argued a different decision — whether to trade the exclusion for the credit and what that trade forfeits on the excluded slice. This piece sits upstream of that choice: it prices what the cap is denominated in, how much euro salary the cap actually covers at three published rates, and which of three rates the return applies to income, to accrued tax and to tax paid. A corpus grep for `exchange rate|yearly average|currency conversion` across `published/` and `context/recon_proposals/` returned one hit (`published/2026-10-20_your-24gb-card-is-4gb-short.md`), a hardware article with no relation to the thesis, so no prior artifact in any vertical owns this mechanism.
**Thesis:** The code's thresholds are dollars while a cross-border life is not, so the exchange rate decides how much of the $130,000 cap a euro salary consumes and what the credit for foreign tax is worth — and a single return applies at least three different rates, one to income, one to accrued tax and one to tax paid, with a one-way election that can lock the method for later years.

**Lead:** The vertical's own `primary_angles` — "cross-border net cash flow and fx shock simulator over 5-year horizons" and "the true cost of dual-jurisdiction compliance feie and ftc optimization" — read against `context/growth_os/customer-truth.md` anecdote 2 (the unhedged FX swing that erased a Lisbon arbitrage) and `context/growth_os/founder-voice.md` §3 ("A 12% adverse exchange-rate swing over 24 months can completely wipe out anticipated cost-of-living arbitrage"). The specific material: the IRS's own published yearly-average table carries five years of euro and pound rates on one page, so the arithmetic of what a fixed foreign salary is worth in dollars — and how much of a dollar-denominated cap it consumes — can be built entirely from published official rates rather than estimated.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Internal Revenue Service — Yearly average currency exchange rates | https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates | 2026-10-29 | 0.886 — the 2025 yearly average for the euro zone is 0.886 euro per US dollar, against 0.951 for 2022 and 0.846 for 2021 | measured (official yearly average) |
| 2 | Internal Revenue Service — Yearly average currency exchange rates, United Kingdom row | https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates | 2026-10-29 | 0.759 — the 2025 yearly average for the United Kingdom pound is 0.759 per dollar, against 0.811 for 2022 | measured (official yearly average) |
| 3 | European Central Bank — Euro foreign exchange reference rates | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html | 2026-10-29 | 1.1130 — the ECB reference rate for 29 October 2026 quotes the US dollar at 1.1130 per euro | measured (central-bank reference rate) |
| 4 | Board of Governors of the Federal Reserve System — H.10 Foreign Exchange Rates, release of 26 October 2026 | https://www.federalreserve.gov/releases/h10/current/ | 2026-10-29 | 1.1209 — the H.10 weekly table quotes the euro at 1.1209 US dollars on 19 October 2026 | measured (central-bank release) |
| 5 | Internal Revenue Service — Instructions for Form 1116 (Foreign Tax Credit) | https://www.irs.gov/instructions/i1116 | 2026-10-29 | 30% — a currency is inflationary where cumulative inflation reaches 30% over the 36 calendar months before the tax year ends, which forces the year-end rate in place of the yearly average | measured (statutory definition quoted in the instructions) |

## Arithmetic the article will carry (computed from rows 1–4, reproduced here so the rewrite can be audited against it)

| Item | Figure | Basis |
|---|---|---|
| €100,000 at the 2025 average (0.886) | $112,867 | 100,000 ÷ 0.886 |
| €100,000 at the 2022 average (0.951) | $105,152 | 100,000 ÷ 0.951 |
| €100,000 at the 2021 average (0.846) | $118,203 | 100,000 ÷ 0.846 |
| Swing, 2022 average → 2025 average, same euros | +$7,714, +7.34% | 112,867 ÷ 105,152 − 1 |
| €100,000 at the ECB rate of 29 October 2026 (1.1130) | $111,300 | 100,000 × 1.1130 |
| Gap between the 2025 average and that spot rate | −$1,567, −1.39% | 111,300 vs 112,867 |
| £100,000 at the 2025 average (0.759) vs 2022 (0.811) | $131,752 vs $123,305 | +6.85% |
| €115,000 at the 2025 average against the $130,000 cap | $129,797 — $203 of headroom | 115,000 ÷ 0.886 |
| €115,000 at the 2021 average against the same cap | $135,934 — $5,934 over the cap | 115,000 ÷ 0.846 |
| The $130,000 cap expressed in euros | €115,180 at the 2025 average; €109,980 at the 2021 average | 130,000 × 0.886; 130,000 × 0.846 |
| €10,000 of accrued foreign tax, 2025 average vs the 29 October spot | $11,287 vs $11,130 — $157 apart | 10,000 ÷ 0.886; 10,000 × 1.1130 |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The dollar-denominated cap against a euro salary, and the three rates one return applies | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Totalization: who pays social security on a three-year posting, and what the certificate of coverage settles | 8 | 8 | 4 | 7 | 6.8 | dropped — `irs.gov/individuals/international-taxpayers/totalization-agreements` fetches but carries no figure a row can lead on, and `ssa.gov` answers the verifier as unreachable, so the numeric floor cannot be met |
| Medicare and private cover once you live abroad | 9 | 8 | 3 | 7 | 7.0 | dropped — `medicare.gov/coverage/travel-outside-the-u-s` and `cms.gov/medicare/coverage/outside-united-states` are both unreachable to the verifier, and the CMS fact sheet is a PDF (`unsupported`) |
| Your US state keeps taxing you after you leave on paper | 9 | 9 | 4 | 7 | 7.5 | dropped — `california.public.law` and `ftb.ca.gov` answered unreachable on this run's probes, so a state-statute row could not be fetched; re-probe before revisiting |

## Notes for the fact-check pass
- The general revenue rule is quoted verbatim from `irs.gov/individuals/international-taxpayers/foreign-currency-and-currency-exchange-rates` ("Use the exchange rate prevailing when you receive, pay, or accrue the item. If there is more than one exchange rate, use the one that most properly reflects your income.") — that page carries no figure, so it is a prose citation and a `## Sources` line, never a gate row.
- The three exits from the yearly average, the payment-date election and the refund rule are quoted from `irs.gov/instructions/i1116`; only the 30%/36-month inflation floor has a figure distinctive enough to lead a gate row (a cell led on "2 years" evidenced on the page's navigation block, so the two-year and prior-year exits ride in prose under row 5's citation).
- `irs.gov/publications/p54` states that the dollar is the functional currency and points at the yearly-average table, but it prints no rule sentence on the average itself; do not attribute the method rule to Pub 54.
- The IRS yearly-average table is *foreign currency units per US dollar*, so a conversion divides by the rate. Every dollar figure above divides; the reciprocal (dollars per euro) is stated only where it is computed and named as computed.
- The $130,000 exclusion cap itself is cited from `irs.gov/instructions/i2555` in `## Sources` (already verified for `2026-10-22_your-130000-cap-costs-the-credit`); it is not restated as a gate row here because a comma-grouped cell tokenises to `130`/`000`.
- Probed and unusable on this beat this run: `medicare.gov`, `cms.gov`, `ssa.gov`, `california.public.law`, `ftb.ca.gov`, `gov.uk/guidance/social-security-abroad-ni38`, `irs.gov/instructions/i114` (all unreachable); `government.nl` and `gov.uk/national-insurance-if-you-go-abroad` fetch but carry no figure bearing on this decision.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=4 hosts=3 decision="sha1:aa06d0f5e7" dedup="matched a prior artifact: 2026-10-22_your-130000-cap-costs-t" window_days=180 checked_at=2026-10-29T19:34:53+00:00 -->
<!-- evergreen-gate:end -->
