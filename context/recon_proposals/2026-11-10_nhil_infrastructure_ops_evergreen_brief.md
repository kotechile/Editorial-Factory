# Evergreen Brief: nhil_infrastructure_ops — 2026-11-10
**Archetype:** evergreen
**Vertical:** nhil_infrastructure_ops
**Persona:** it_ops_leader
**Decision the reader is facing:** Whether a sealed (no-egress) enclave's certificates can be issued and renewed by machines inside the boundary before the public lifetime ladder drops to 100 days in March 2027 and 47 days in March 2029 — i.e. whether to fund an internal issuing authority plus automated trust-bundle delivery this budget year, or keep the renewal runbook that assumes a 398-day certificate and a person to file the ticket.
**Durability:** The dates are regulatory, not market: the CA/Browser Forum Baseline Requirements themselves carry the ladder — 398 days before 2026-03-15, 200 days from 2026-03-15, 100 days from 2027-03-15, 47 days from 2029-03-15 — with the validation-data reuse period falling from 398 to 200 to 100 to 10 days on the same rungs, all as of the BR edition published in the Forum's server-certificate repository on 2026-11-10. Let's Encrypt's own operational plan (90 days cut in half to 45 days by 2028, authorization reuse 30 days to 7 hours) is as of its 2 December 2025 post, and the vendor summary of the ballot schedule (398 / 200 / 100 / 47 days, SII reuse down from 825 days) is as of its 2025 post. What a reader re-reads each cycle is the rung that has just landed; what does not expire is the arithmetic — renewal rate equals certificate count times 365 divided by the lifetime ceiling — because no future ballot lengthens a certificate.
**De-dup:** `2026-11-03_your-backup-66-mw-permit-trap` is this vertical's nearest prior evergreen artifact (behind-the-meter plant regulation), and `2026-11-03_nhil_infrastructure_ops_evergreen_brief` the brief behind it. That piece converts federal emissions thresholds into megawatts to size an on-site plant; this one converts a certificate-lifetime ladder into a renewals-per-day requirement to size an internal issuing authority. No shared source, no shared mechanism. `2026-10-06_rack-power-density-ceiling-build-before-you-buy` (the building shell), `2026-10-13_remediator-recovers-46-percent` (how much authority a closed-loop remediator gets), `2026-10-20_enclave-overhead-62-percent-not-4` (what a confidential enclave costs in throughput) and `2026-10-27_your-gpu-break-even-is-37-percent-busy` (own vs rent capacity) are the other four; none mentions a certificate, a CA or a renewal. Cross-vertical check run this run (`grep -ril "certificate expir\|cert renew\|acme\|public ca\|47-day\|certificate lifetime" published/`): the only hits are `2026-10-10_self-hosting-break-even-one-hour-a-year` and `2026-10-10_home-assistant-cloud-rename-hardware-rent`, where "a certificate expires with no warning" appears as one item in a list of server-owner failure modes; no published article in the corpus argues certificate lifetimes or offline issuance.
**Thesis:** A 47-day certificate is not a TLS-housekeeping chore, it is an air-gap throughput requirement: the Baseline Requirements take the public ceiling to 200 days now, 100 days in March 2027 and 47 days in March 2029, and an enclave that cannot reach a public authority or a revocation service has to issue and distribute its own certificates, so a 500-certificate estate moves from about 1.3 renewals a day to about 10.6 — a rate that only unattended issuance inside the boundary survives, and the agent runtime is the workload that fails first because nobody in that loop files a ticket.

**Lead:** The vertical's own beat *data residency and air-gapped agent runtime* (`primary_angles`, the one angle in this vertical with no artifact yet), the persona's want of "sovereign SLM deployment" (`context/personas.json` → `it_ops_leader`), and `context/growth_os/customer-truth.md` anecdote 3 (a defense contractor's air-gapped telemetry estate running local 8B models, where "routing telemetry through external cloud APIs was legally forbidden"). The specific material is the certificate-lifetime ladder in the CA/Browser Forum Baseline Requirements, which converts an air gap from a network diagram into a standing renewal-rate obligation.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | CA/Browser Forum, "Baseline Requirements for the Issuance and Management of Publicly-Trusted TLS Server Certificates" § 6.3.2 (servercert repository) | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | 2026-11-10 | 397 days — Subscriber Certificates issued before 2026-03-15 SHOULD NOT have a Validity Period greater than 397 days and MUST NOT have a Validity Period greater than 398 days | measured — normative standard text |
| 2 | CA/Browser Forum, BR § 6.3.2, 2029 rung | https://raw.githubusercontent.com/cabforum/servercert/main/docs/BR.md | 2026-11-10 | 46 days — Subscriber Certificates issued on or after 2029-03-15 SHOULD NOT have a Validity Period greater than 46 days and MUST NOT have a Validity Period greater than 47 days | measured — normative standard text |
| 3 | Let's Encrypt, "Decreasing Certificate Lifetimes to 45 Days" (2 December 2025) | https://letsencrypt.org/2025/12/02/from-90-to-45 | 2026-11-10 | 90 days — Let's Encrypt currently issues certificates valid for 90 days, which will be cut in half to 45 days by 2028 | vendor claim — the issuing authority's own plan |
| 4 | Let's Encrypt, authorization reuse plan | https://letsencrypt.org/2025/12/02/from-90-to-45 | 2026-11-10 | 7 hours — the authorization reuse period is currently 30 days, which will be reduced to 7 hours by 2028 | vendor claim — the issuing authority's own plan |
| 5 | DigiCert, "TLS certificate lifetimes will officially reduce to 47 days" | https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days | 2026-11-10 | 398 days — until March 15, 2026 the maximum lifetime for a TLS certificate is 398 days, then 200 days, then 100 days, then 47 days | vendor claim — CA summary of the ballot schedule |
| 6 | DigiCert, SII reuse under the same ballot | https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days | 2026-11-10 | 825 — validations of Subject Identity Information can only be reused for 398 days as of March 15, 2026, down from 825 | vendor claim — CA summary of the ballot |

## Notes on the evidence set (read before drafting)

- **Rows 1 and 2 are the normative record; rows 5 and 6 are the industry summary of the same ballot.** The
  article must attribute the ladder to the Baseline Requirements (rows 1–2) and use the CA blog only as the
  readable restatement, or it cites a vendor for a standard it can cite directly.
- **Matcher traps avoided, recorded for the audit.** On the BR file a cell leading on "200 days" evidences on
  the *domain-validation reuse* line rather than the validity line, "100 days" evidences on the amendment-history
  table, and "10 days" evidences on a 2014 amendment row — so those three rungs are written in prose under rows
  1 and 2 and only the two self-evidencing cells (397 days, 46 days) carry rows. On the Let's Encrypt post a
  cell leading on "45 days" evidences on the page title, so the 45-day rung rides in prose and the row leads on
  the 90-day sentence it is measured from.
- **The scope caveat is part of the thesis, not a footnote.** The Baseline Requirements bind publicly-trusted
  certificates; a private authority sets its own lifetimes. The article says so plainly, and the argument for
  adopting the discipline inside the enclave is the one the sources support: the public certificates an enclave
  still presents outward are already on the ladder, and a revocation channel (CRL/OCSP) is exactly what an air
  gap removes — which is why the industry moved to short lifetimes instead of revocation at all.
- **Arithmetic the article performs visibly** (no source states it, so it is labelled as the desk's own): at
  500 subordinate certificates, renewals per year = 500 × 365 ÷ lifetime; 398 days → 459 a year (1.3 a day),
  200 → 913 (2.5), 100 → 1,825 (5.0), 47 → 3,883 (10.6). Round to whole renewals in the body and state the
  certificate count as the reader's input.
- **No measured third-party study exists** of how many enclaves fail this way; the piece makes no such claim.

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The 47-day certificate clock inside a sealed enclave: renewal rate as an air-gap throughput requirement | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Air-gapped time: NTP holdover and clock drift inside the boundary | 7 | 9 | 5 | 6 | 6.9 | dropped — no fetchable primary states a drift or holdover figure; every time-server spec is a PDF the verifier cannot read |
| Model-refresh payload across the data diode: what an offline estate must mirror each release | 7 | 7 | 5 | 7 | 6.6 | dropped — no dated primary publishes the artifact sizes; the only figures are vendor catalogue pages that move monthly |
| BGP route-leak guardrails before an agent may touch routing (RFC 9234 OTC, max-prefix) | 8 | 9 | 6 | 8 | 7.7 | dropped — the RFCs fetch cleanly but carry no figure a row can lead on, and the 2026-10-13 remediator piece already owns the autonomy-budget argument for this vertical |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=6 fetched=6 sources=3 hosts=3 decision="sha1:d9152b588c" dedup="matched a prior artifact: 2026-11-03_your-backup-66-mw-permi" window_days=180 checked_at=2026-11-10T18:04:27+00:00 -->
<!-- evergreen-gate:end -->
