# Verified Brief: supplier_risk_reshoring_decision — 2026-11-07 (evergreen)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Peso spot | The Mexico peso rate was 18.5922 currency units per U.S. dollar on 30 October 2026 | VERIFIED | https://www.federalreserve.gov/releases/h10/current/ | "Release Date: November 2, 2026 Foreign Exchange Rates -- H.10 Weekly (Rates in currency units per U.S. dollar except as noted by an asterisk) COUNTRY CURRENCY Oct. 26 Oct. 27 Oct. 28 Oct. 29 Oct. 30 … MEXICO PESO 18.5922 18.6381 18.6730 18.7911 18.7942" |
| 2 | Dollar leg | The effective federal funds rate was 3.88 percent on 5 November 2026 | VERIFIED | https://www.federalreserve.gov/releases/h15/ | "Instruments 2026 Oct 30 2026 Nov 2 2026 Nov 3 2026 Nov 4 2026 Nov 5 Federal funds (effective) 1 2 3 3.88 3.88 3.88 3.88 3.88" |
| 3 | Peso leg | Banco de México's key rate is 6.25 percent, cut by 0.25 percentage points from 6.50 percent (November 2026) | VERIFIED (secondary aggregator — the central bank's own pages are unreachable to the verifier; see FLAG below) | https://countryeconomy.com/key-rates/mexico | "Mexico INTEREST RATES Interest rates fall in Mexico Mexico has lowered its interest rates by 0.25 percentage points, from 6.5% to an annual rate of 6.25%." |
| 4 | Duty conversion | Customs converts a foreign-currency invoice at a certified quarterly rate that governs every export date in the quarter, replaced by the certified daily rate only when the two differ by 5 percent or more; the section was last amended at T.D. 81-117 in 1981 | VERIFIED | https://www.ecfr.gov/current/title-19/section-159.34 | "The certified quarterly rate established under paragraph (a) of this section shall be used for Customs purposes for any date of exportation within the quarter, except in the following cases: … ( 2 ) Certified daily rate. If the certified daily rate for the date of exportation varies by 5 percent or more from the certified quarterly rate, notice of such variation and the rate or rates certified for such day shall be published in the Customs Bulletin, and such certified daily rate shall be used for Customs purposes in connection with merchandise exported on such day. [T.D. 73-175, 38 FR 17482 , July 2, 1973, as amended by T.D. 81-117, 46 FR 24944 , May 4, 1981]" |
| 5 | Derived (arithmetic, not a source claim) | A twelve-month forward at covered interest parity prices the peso at 19.0164 per dollar, a 2.2815 percent premium over spot; on a $10,000,000 peso bill converted at spot the same purchase costs $223,059 less | VERIFIED as arithmetic, recomputed in the run from claims 1–3 above (10,000,000 × (1 − 18.5922/19.0164) = 223,058.82) | (derived) | n/a — every percentage in the article is recomputed from the two cited cells, never copied from a draft |

## FLAG — the peso policy rate rides on a secondary citation

Banco de México's own site is unreachable to the verifier on every path tried: the home page returns a 1,368-character
navigation shell, `tipcamb/main.do` returns 607 characters with no rates, `monetary-policy/index.html` and the monetary-policy
announcement index both answer `unreachable`, and `tipcamb/tipCamMIAction.do` fetches 1,588 characters with no numeric rate.
The 6.25 percent / 6.50 percent pair is therefore cited through a data aggregator that reproduces the central bank's
decision, and the row is labelled as such. Two consequences for the draft and the audit: the article must attribute the rate
to Banco de México rather than to the aggregator, and the run log records that the primary was unreachable rather than
absent. The figure is independently consistent with the forward arithmetic it feeds.

## Notes for the drafter

- The 5 percent band and the 1981 amendment are in one sentence on the regulation page; the "5 percent" cell cannot lead a
  gate row because the first `5 percent` on the page belongs to § (a)(1), the proclaimed-rate exception. The rule therefore
  rides in prose under citation [4] and the table row leads on `1981`.
- `19 CFR 159.35` (the daily rate is the New York Fed's certified buying rate, and a New York bank holiday rolls it back to
  the last business day) is prose-and-Sources only: no numeric token.
- The 42-day and 4-day cycle lengths are this desk's own field anecdote (`context/growth_os/customer-truth.md` Anecdote 1),
  not a measured transit benchmark; use them for exposure-days arithmetic and label them as our own field work.
- Recompute in the final: 2.2815 percent, 19.0164, the $2,625 and $250 per-cycle figures on a $1,000,000 purchase, and
  $223,059 on $10,000,000. Do not restate the peso-side premium as a dollar saving without the same base.
