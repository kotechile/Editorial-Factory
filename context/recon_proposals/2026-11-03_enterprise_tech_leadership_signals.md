# Signals: enterprise_tech_leadership — 2026-11-03
**Window:** 2026-10-04 → 2026-11-03
**Queries run:** 17 (10 date-agnostic web fan-outs across the four configured source classes —
`hacker_news`, `substack_tech_leads`, `cloud_cost_reports`, `x_ai` — each with the §3 date-agnostic
fallback phrasing, 3 primary-page fetches, 2 Algolia/HN checks, 2 publisher-date probes). The HN/Algolia
sweep (six keyword queries against the window, 15-point floor) returned no front-page engineering post on
repatriation, monolith consolidation or AI unit cost; it is a source-class check and is never written as
a signal row — a process row in this table poisons the pairing step, exactly as a code-availability row does.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Dun & Bradstreet AI Momentum survey, Q4 2026 — 10,000 businesses, 32 countries: return rate flat while data readiness is the split | https://www.prnewswire.com/news-releases/dun--bradstreet-survey-of-10-000-businesses-finds-ai-returns-stable-for-most-but-data-ready-companies-pull-ahead-on-roi-302922158.html | 2026-10-28 | "28% report broad or strong returns from AI efforts, unchanged from last quarter"; "Only 8% of businesses report that their enterprise data is fully ready to support AI at scale"; "81% of businesses with enterprise data that is fully ready for AI are obtaining broad or strong ROI, compared with 12% of those whose data is only partially ready"; on strong ROI alone "55% … compared with 2% of those with low or no data readiness"; 57% of partially-ready report "only pockets of ROI" against 16% of fully ready; "9% say most pilots have scaled with clear gains"; 37% "scaling AI pilots into production, up from 34% in Q3"; 65% plan to increase AI spending | AI ROI as a data-foundation variable, not a model variable | 92 |
| 2 | Deloitte "State of AI in the Enterprise" 2026 — 3,500 leaders, 25 countries, fielded May–June 2026: revenue gains rising, unit cost unmeasured | https://www.deloitte.com/us/en/about/press-room/enterprise-ai-enters-an-roi-reckoning.html | 2026-10-29 | "reported revenue gains from AI increasing to 28% (up from 20% reported in Deloitte's January report)"; "81% of companies surveyed reporting faster decision-making and execution"; "only 25% say they are using AI to deeply transform the business"; "While 71% track total AI inference and API spend, only 51% track token volume and 44% track per-unit inference cost"; "Forty percent of enterprises … now allow AI systems to execute decisions or take actions without human approval, at least to a moderate degree"; "23% say accountability remains unclear when an AI system produces a negative outcome"; 60% have redesigned jobs, "only 15% report a significant shift in decision-making authority" | ROI definition and the missing denominator (cost per unit of work) | 90 |
| 3 | Deloitte report landing page — "The bill is visible. The unit cost isn't." | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html | 2026-10-29 | "81% of surveyed leaders say AI has improved speed of decision-making and execution, yet only 25% are deeply transforming the business"; "71% track total AI inference and API spend, but only 44% track per-unit inference cost" | Same release's own framing of the measurement gap | 74 |
| 4 | The Register — VMware customers weigh exit as licensing bills bite (Unisphere Research for Rimini Street, 269 VMware user organizations, fielded Dec 2025–Feb 2026) | https://www.theregister.com/virtualization/2026/10/07/nine-in-10-vmware-customers-eye-the-exit-as-licensing-bills-bite/5301591 | 2026-10-07 | "Nine out of ten respondents … say higher licensing costs were prompting them to consider alternatives"; "54 percent cited the end of perpetual license support"; "Sixty percent … considering a multi-hypervisor strategy"; "Forty-eight percent said they did not currently plan to move any assets to VMware Cloud Foundation"; Gartner: "By 2029, 55 percent of enterprises will initiate proofs of concept for alternative distributed hybrid infrastructure products to replace their VMware-based deployments …, up from 25 percent in 2026" | Platform churn under the private-cloud target (runner-up angle) | 78 |

**Dating note.** Rows 1–3 are releases published inside the window by the organizations that ran the
surveys. Deloitte's fielding window is May–June 2026 and is stated in the piece and in the claim cell;
its *release* is 2026-10-29. D&B's AI Momentum survey is quarterly and the release states the Q3→Q4
comparison, so the figures are current-quarter. Row 4 is a publication dated 2026-10-07 reporting a
survey fielded December 2025–February 2026 — carried as a runner-up leg only, with its fielding window
named, never as a fresh measurement. The HN sweep is likewise an observation-date check with no row of its own.

## Dropped at Stage 1 (with reason)

- **Broadcom, "As AI Workloads Grow, 83% of Enterprises Look to Private Cloud Repatriation"**
  (https://www.broadcom.com/company/news/articles/cloud/as-ai-workloads-grow-83-of-enterprises-look-to-private-cloud-repatriation,
  2026-10-08). The October article reports the *Private Cloud Outlook 2026* report, which Broadcom's
  own investor release dates **June 2026**, fielded **11 February – 13 March 2026** (1,800 senior IT
  decision-makers; Radius Tech). A PR-dated-in-window wrapper around a June report is not an in-window
  signal — kept in `## Dated background`.
- **Gartner, "Over $3.5 Trillion of AI Infrastructure Spending Could Be Exposed to Impairment by the
  End of 2030"** (2026-10-14). In window and primary, but this desk anchored its 80%-of-neoclouds
  figure on 2026-10-20 in `your-gpu-landlord-80-wont-survive`; spent, not reused.
- **Gartner IT spending forecast 15% / $7.35 trillion (2026-10-21) and the 44%-of-CEOs release
  (2026-10-20)** — this vertical's own 2026-10-27 winner (`your-15-percent-raise-is-a-price-hike`).
  Retread.
- **Cloudera "The Great AI Re-Architecture"** (released 2026-08-11, fielded 5–22 June 2026; 66% moved
  AI workloads back to private cloud) — reused in the 2026-11-01 ZDNET analysis, but the release and
  its fielding both sit outside the window.
- **Gartner, "70% of enterprises will abandon agentic AI built by vendor forward-deployed engineering
  by 2028"** (2026-09-29) — five days before the window opened.
- **Retool 2026 Build vs Buy report, Flexera State of the Cloud 2026 (18 March), FinOps State of
  FinOps 2026 (19 February)** — all fielded and released outside the window.
- **Twilio Segment "Goodbye Microservices" (2018)** resurfacing as a 2026 HN thread — stale document,
  not a 30-day development.
- **Broadcom VDDK removal (2026-08-25)**, **Tesco/Proxmox replacement (June 2026)**, **Gartner DHI
  Magic Quadrant (7 September 2026)** — real but outside the window; the Register row
  above carries them as its own reporting.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=0 heuristic=- window=2026-10-04..2026-11-03 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background

- Broadcom / VMware, *Private Cloud Outlook 2026: The AI Tipping Point* — report published June 2026,
  fielded 2026-02-11 → 2026-03-13, 1,800 senior IT decision-makers, 8 countries, Radius Tech partner.
  83% considering or already repatriated (69% in 2025); 50% already repatriated some workloads (35%
  in 2025); 51% cite security and compliance; 39% cost predictability; 39% performance; 43% are moving
  AI training/LLM/inference workloads; 47% business-critical.
  https://www.vmware.com/docs/private-cloud-outlook-2026
  https://investors.broadcom.com/news-releases/news-release-details/broadcoms-private-cloud-outlook-2026-reveals-ai-tipping-point
  https://www.broadcom.com/company/news/articles/cloud/as-ai-workloads-grow-83-of-enterprises-look-to-private-cloud-repatriation
- Gartner, "Over $3.5 Trillion of AI Infrastructure Spending Could Be Exposed to Impairment by the End
  of 2030" (2026-10-14) — https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030
- Gartner, "Worldwide IT Spending to Grow 15% in 2027, Totaling $7.35 Trillion" (2026-10-21) —
  https://www.gartner.com/en/newsroom/press-releases/2026-10-21-gartner-forecasts-worldwide-it-spending-to-grow-15-percent-in-2027-totaling-7-point-35-trillion
- Gartner, "44% of CEOs Struggle to Demonstrate AI Financial Returns" (2026-10-20) —
  https://www.gartner.com/en/newsroom/press-releases/2026-10-20-gartner-says-44-percent-of-ceos-struggle-to-demonstrate-ai-financial-returns-as-technology-becomes-central-to-growth
- Cloudera, *The Great AI Re-Architecture* (2026-08-11; fielded 2026-06-05 → 2026-06-22; 1,500
  enterprise architects) — https://www.cloudera.com/about/news-and-blogs/press-releases/2026-08-11-ninety-five-percent-of-enterprises-have-delayed-ai-projects-as-infrastructure-limitations-spark-the-great-ai-re-architecture.html
- ZDNET analysis of repatriation economics, carried 2026-11-01 (no new primary data) —
  https://www.zdnet.com/tech/cloud-repatriation-enterprise-cost-optimization
- Gartner DHI Magic Quadrant, published 2026-09-07 (Julia Palmer et al.) — the 25% → 55% forecast the
  Register quotes.
- Broadcom VDDK public download removal, 2026-08-25 (reported impact on migration tooling) —
  https://www.theregister.com/virtualization/2026/10/07/nine-in-10-vmware-customers-eye-the-exit-as-licensing-bills-bite/5301591
