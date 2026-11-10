# Verified Brief: nhil_infrastructure_ops — 2026-11-10

Fact-check pass over `context/recon_proposals/2026-11-10_nhil_infrastructure_ops_evergreen_brief.md`
(every green row below was re-read from the fetched page, not from the brief's paraphrase).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Certificate-lifetime ladder (standard) | A subscriber certificate issued before 2026-03-15 may not exceed 398 days; the ceiling is 200 days from 2026-03-15, 100 days from 2027-03-15 and 47 days from 2029-03-15 | VERIFIED | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | "Subscriber Certificates issued before 2026-03-15 SHOULD NOT have a Validity Period greater than 397 days and MUST NOT have a Validity Period greater than 398 days … issued on or after 2029-03-15 SHOULD NOT have a Validity Period greater than 46 days and MUST NOT have a Validity Period greater than 47 days" |
| 2 | Validation-data reuse (standard) | The reuse period for domain-validation data falls 398 → 200 → 100 → 10 days on the same rungs | VERIFIED | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | table: "2026-03-15 \| 398 days \| 2026-03-15 \| 2027-03-15 \| 200 days \| 2027-03-15 \| 2029-03-15 \| 100 days \| 2029-03-15 \| 10 days" |
| 3 | Unit definition (standard) | A day is 86,400 seconds for the purpose of these calculations | VERIFIED | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | "a difference of 86,400 seconds shall be equal to one day, ignoring leap-seconds" |
| 4 | Issuer's own plan | Let's Encrypt issues 90-day certificates today and plans 45 days by 2028 | VERIFIED | https://letsencrypt.org/2025/12/02/from-90-to-45 | "We currently issue certificates valid for 90 days, which will be cut in half to 45 days by 2028" |
| 5 | Issuer's own plan | Authorization reuse falls from 30 days to 7 hours by 2028 | VERIFIED | https://letsencrypt.org/2025/12/02/from-90-to-45 | "It is currently 30 days, which will be reduced to 7 hours by 2028" |
| 6 | Industry summary of the ballot | The ladder as a CA summarises it: 398 → 200 (15 March 2026) → 100 (15 March 2027) → 47 (15 March 2029) | VERIFIED | https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days | "From today until March 15, 2026, the maximum lifetime for a TLS certificate is 398 days. As of March 15, 2026 … 200 days. As of March 15, 2027 … 100 days. As of March 15, 2029 … 47 days" |
| 7 | Industry summary of the ballot | Subject identity information reuse drops from 825 days to 398 days as of 15 March 2026 | VERIFIED | https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days | "As of March 15, 2026, validations of Subject Identity Information (SII) can only be reused for 398 days, down from 825" |
| 8 | Revocation reliability | The ballot's rationale is that revocation via revocation lists and online status checks is unreliable in practice | FLAGGED — supported by the CA's summary, not by the standard text itself | https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days | "the revocation system using CRLs and OCSP is unreliable. Indeed, browsers often ignore these features" — attribute to the summary, never to the Baseline Requirements |
| 9 | Scope | The Baseline Requirements bind publicly-trusted certificates; a private authority's lifetimes are its own policy | VERIFIED by inspection of the standard's scope (§1.1 / §6.3.2 apply to "Publicly-Trusted Certificates") | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | "These Requirements … for the Issuance and Management of Publicly-Trusted TLS Server Certificates" |
| 10 | Desk arithmetic (not a source claim) | 500 certificates × 365 ÷ 47 days = 3,883 renewals a year, 7.8 per certificate, 10.6 a day; at 398 days the same estate is 1.3 a day; at 100 days it is 1,825 a year | DERIVED — label as the desk's own arithmetic in the body | — | computed from row 1; the 500-certificate count is the reader's own input and must be written as an assumption |

**Drafter's constraints.**
- The 825-day figure and the 10-day validation rung stay in the prose or out; they must not appear in a
  `By the numbers` bullet as a second metric beside a renewal count.
- Do not write that the Baseline Requirements require a private authority to move to 47 days. They do not.
- Do not claim any measured population of enclaves fails this way; no such measurement exists in the set.
