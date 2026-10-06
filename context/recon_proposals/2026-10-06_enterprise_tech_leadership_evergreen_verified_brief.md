# Verified Brief: enterprise_tech_leadership — 2026-10-06 (EVERGREEN track)

Archetype: evergreen. Topic = the cloud repatriation break-even. Every claim below traces to a source
that the evergreen gate fetched live and confirmed contains the cited figure
(6/6 rows verified on 6 hosts, `<!-- evergreen-gate: -->` marker in
`context/recon_proposals/2026-10-06_enterprise_tech_leadership_evergreen_brief.md`).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Cost-of-revenue trap | A billion-dollar private software company's public cloud spend reached **81% of cost of revenue**; 75% to 80% was called common among software companies | VERIFIED | https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ | "A billion dollar private software company told us that their public cloud spend amounted to 81% of COR, and that 'cloud spend ranging from 75 to 80% of cost of revenue was common among software companies'." |
| 2 | Discount ceiling | Committed-use discounts cut cloud compute by only **~30-50%**, and AWS still clears a **~30% blended operating margin** net of them | VERIFIED | https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ | "cloud compute typically drops by ~30-50% with committed use. But AWS still operates at a roughly 30% blended operating margin net of these discounts and an aggressive R&D budget" |
| 3 | Prior mover | Dropbox disclosed **$75M** in cumulative savings over the two years prior to its IPO, mostly from repatriating workloads | VERIFIED | https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/ | "In 2017, Dropbox detailed in its S-1 a whopping $75M in cumulative savings over the two years prior to IPO due to their infrastructure optimization overhaul, the majority of which entailed repatriating workloads" |
| 4 | Observed outcome | 37signals expects to save **~$10 million over five years**, a cut in infrastructure costs of **between half and two-thirds** | VERIFIED | https://basecamp.com/cloud-exit | "Leaving the cloud will save us ~$10 million over five years. That's a reduction in our infrastructure costs of between half and two-thirds." |
| 5 | First-party run-rate | 37signals cut its cloud bill from the original **$3.2 million/year** run rate to **$1.3 million**, a saving of almost $2 million per year in 2024 | VERIFIED | https://world.hey.com/dhh/our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd | "For 2024, we've brought the cloud bill down from the original $3.2 million/year run rate to $1.3 million. That's a saving of almost two million dollars per year for our setup!" (dated 17 October 2024) |
| 6 | Independent confirmation | Trade press confirms the run-rate move from **$3.2 million per year to $1.3 million** and a ~$2 million saving | VERIFIED | https://www.datacenterdynamics.com/en/news/37signals-claims-it-saved-almost-2m-last-year-from-cloud-repatriation/ | "reduced its cloud bill from $3.2 million per year to $1.3 million"; "37signals estimates that it saved $2 million on its cloud bill this year after its cloud repatriation project" (19 October 2024) |
| 7 | Survey baseline | **29%** of IaaS/PaaS spend is wasted (after five years of decline), and **76%** of large enterprises spend more than $5 million a month on public cloud | VERIFIED | https://info.flexera.com/CM-REPORT-State-of-the-Cloud | "After five years of decline, wasted cloud spend increased slightly to 29%"; "76% of large enterprises spend more than $5 million each month" (Flexera 2026 State of the Cloud, N=753) |
| 8 | Egress anchor | Cloudflare R2 standard storage lists at **$0.015 / GB-month** with no egress charge at any storage class | VERIFIED | https://developers.cloudflare.com/r2/pricing/ | "Storage $0.015 / GB-month"; "There are no charges for egress bandwidth for any storage class." |

## Gate rules applied
- 8/8 claims VERIFIED against the fetched primary page; 0 REMOVED, 0 FLAGGED.
- Claim 3 (Dropbox $75M) is carried with attribution to the a16z analysis, which cites Dropbox's S-1 —
  the S-1 itself is not fetchable in this environment, so the article attributes the figure to a16z.
- Claim 8 is a published list price (vendor claim), used only as the egress comparison point.
- No synthesis: single-signal evergreen topic; the dual-anchor gate does not apply here.
