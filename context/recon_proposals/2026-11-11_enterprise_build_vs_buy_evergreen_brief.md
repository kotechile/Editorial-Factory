# Evergreen Brief: enterprise_build_vs_buy — 2026-11-11

**Archetype:** evergreen
**Vertical:** enterprise_build_vs_buy
**Persona:** eng_leader
**Decision the reader is facing:** Whether to answer an integration that has started hitting its vendor's API rate limit by buying the higher tier — Shopify's ladder runs 2, 4, 20 and 40 requests a second, GitHub's runs 5,000 then 15,000 requests an hour — or by reshaping the requests themselves, and how to size the overshoot before spending on either. It bites the week a nightly sync that used to finish before standup is still running at 9am and someone proposes the enterprise plan as the fix.
**Durability:** Still true in twelve months because the mechanism is a capacity contract, not a price level: a vendor's limit is counted in requests and every request costs the same whether it carries one record or a hundred ("each request counts equally, regardless of how much or how little data is returned", as the Shopify page puts it), so the items-per-request constant — not the plan — sets throughput, and the plan's ladder multiplies the budget by 3× or 20× at most. Every figure is a first-party published policy read as of 2026-11-11 (GitHub REST docs, Stripe rate-limit docs, Shopify REST Admin API limits, GitHub's price list) and the one labour input is the 2025 O*NET wage vintage, so a reader can re-read the same four pages in a year and re-run the same two divisions.
**De-dup:** `2026-10-21_your-ci-bill-232-hours` is this vertical's nearest prior evergreen artifact (`published/2026-10-21_your-ci-bill-232-hours.md`, 21 days): it prices a metered CI minute against a rented server-hour and ends in a utilisation test for compute the team would run itself — no rate limit, no request, no page size and no vendor plan tier appears there. `2026-11-04_your-support-bill-an-engineer-at-190k` prices the support line as a percentage ladder versus a flat fee; this brief prices throughput, not the support contract, and cites none of its pages. `2026-10-28_your-sso-bill-125-a-connection` prices one feature in three billing units (connection, seat, tier gate); the tiers here are plan levels of one API and the unit is a request, not a seat. `2026-10-07_sla-credit-is-not-insurance` prices the credit paid back after an outage — no availability, credit or remedy claim appears here. Today's news piece `2026-11-11_your-44x-ticket-saving-needs-a-busy-box` prices dollars per ticket against dollars per GPU-hour; this brief never touches token or GPU prices. Cross-vertical greps (`grep -ril "rate limit\|429\|per_page\|pagination" published/`) return only passing mentions inside agent-runtime and home-automation articles (`2026-10-15_agent-loop-bound-not-a-budget`, `2026-10-12_agent-timeout-false-alarm-budget`) which bound a loop and a timeout, and none argues the request-budget thesis; the desk's own 2026-09-23 news angle brief priced AI cost-tool maintenance in engineer-years and is a different claim.
**Thesis:** A rate limit is a throughput budget counted in requests, not in data — every request costs the same whether it carries one record or 250 — so the lever that decides whether a nightly job finishes is the page size, and the tier ladder only fixes an integration whose overshoot is inside its multiple: 3× on GitHub (5,000 to 15,000 an hour), 20× on Shopify (2 to 40 requests a second), which means the enterprise plan is the wrong purchase for a job that is fifty times over the limit.

**Lead:** The vertical's own `primary_angles` entry "api ingestion and third-party service redundancy costs and fallback layers" plus `context/growth_os/founder-voice.md` §3 pillar "API Ingestion & Redundancy Overhead" (paying enterprise API tiers rather than staffing an on-call engineer), sharpened against `context/growth_os/customer-truth.md`'s integration anecdotes. The specific material: while re-reading the vendor docs that the desk's earlier integration work cites, three first-party pages published hard request budgets for the same class of integration — GitHub 5,000 an hour, Stripe 100 a second, Shopify 2 a second with a plan ladder to 40 — and the shopify page states the sentence that decides the argument, that each request counts equally regardless of how little data it returns. GSC was checked and returned zero striking-distance queries for this vertical (`context/recon_proposals/2026-11-11_gsc_enterprise_build_vs_buy_opportunities.md`), so it is a bonus signal only and vetoes nothing.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | GitHub Docs — Rate limits for the REST API | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | 2026-11-11 | 5,000 requests per hour — the personal rate limit for a user's token | measured (published API policy) |
| 2 | GitHub Docs — Rate limits for the REST API | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | 2026-11-11 | 15,000 requests per hour — the limit for a GitHub App owned by a GitHub Enterprise Cloud organization | measured (published API policy) |
| 3 | GitHub Docs — Using pagination in the REST API | https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api | 2026-11-11 | 100 — the maximum value of per_page on most endpoints, and a request without it returns 30 | measured (published API policy) |
| 4 | Stripe Docs — Rate limits | https://docs.stripe.com/rate-limits | 2026-11-11 | 100 requests per second — the global live-mode rate limit per Stripe account | measured (published API policy) |
| 5 | Shopify — REST Admin API rate limits | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | 2026-11-11 | 40 requests/app/store — the bucket size, emptied at two requests a second on the standard plan | measured (published API policy) |
| 6 | Shopify — REST Admin API rate limits | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | 2026-11-11 | 2/second — the standard leak rate, against 4, 20 and 40 requests a second on the higher plans | measured (published API policy) |
| 7 | GitHub — Pricing | https://github.com/pricing | 2026-11-11 | $21 USD per user / month — the Enterprise plan price | vendor claim |
| 8 | O*NET OnLine — Software Developers (15-1252.00) | https://www.onetonline.org/link/summary/15-1252.00 | 2026-11-11 | $65.38 hourly — median wage for software developers, 2025 | measured |

## How the figures convert (desk arithmetic, to be recomputed in the final)

- GitHub personal token: 5,000 ÷ 3,600 = **1.39 requests a second**. At `per_page=100` that is **500,000 records an hour**; at the 30-item default it is 150,000.
- GitHub Enterprise Cloud: 15,000 ÷ 3,600 = **4.17 requests a second**, 1,500,000 records an hour at 100 a page — **3× the personal token**, and the docs add that a higher-limit app *reduces the remaining budget* available to lower-limit authentication methods on the same account.
- Stripe: 100 a second is **360,000 an hour** and 8.64 million a day, per account and shared across every integration — 72× GitHub's per-token rate; the sandbox ceiling is 25 a second, a quarter of live, so a load test never sees the production limit.
- Shopify: bucket 40 at a leak rate of 2 a second is **20 seconds of banked burst** (40 ÷ 2), and the plan ladder is 2 → 4 → 20 → 40 requests a second, i.e. **20× from standard to Commerce Components**; the page also caps offset paging, returning a 429 once a `page` offset passes 100,000 records (400 pages at `limit=250`).
- The buy side: $21 a seat × 50 seats = $1,050 a month, **$12,600 a year**, which is **192.7 engineer-hours** at $65.38 — and it buys the 3×, not the throughput. Priced per extra request (10,000 an hour × 24 × 365 = 87.6M a year) the uplift is $0.000144 a request, which is not the point of the purchase and must not be sold as one.

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The rate limit is a request budget sold as a tier ladder: page size buys more than the plan | 9 | 8 | 9 | 9 | 8.8 | **winner** |
| Webhook at-least-once delivery: how long the dedupe table has to be retained | 8 | 9 | 8 | 7 | 8.0 | dropped — the retry window is a spec, not a price; no priced "buy" leg exists for the decision, and two of the three retry windows are on the same host as rows already used |
| Managed cache per GB-month vs a rented instance (Redis-shaped) | 7 | 8 | 7 | 7 | 7.2 | dropped — repeats the metered-versus-rented utilisation test already published at `2026-10-21_your-ci-bill-232-hours` |
| Egress pricing: what leaving a metered store costs per TB | 8 | 7 | 4 | 8 | 6.7 | dropped — the incumbent's rate table renders as `priceOf!` templates the verifier cannot read (`aws.amazon.com/s3/pricing/`, probed 2026-11-11) and the zero-egress side states only "no charges for egress bandwidth", so the article would rest on one host and one qualitative claim |
| Startup cloud credits: what the architecture costs when the subsidy expires | 7 | 5 | 6 | 6 | 6.1 | dropped — program terms change every cycle, so the figure fails the 12-month bar, and the decision is a subsidy cliff rather than a build-versus-buy call |

## Notes for the drafter

- The load-bearing sentence is Shopify's own — *each request counts equally, regardless of how much or how little data is returned* — so quote it verbatim and build the page-size rule on it. It is on row 5's page.
- Do **not** claim the enterprise tier does not raise limits: GitHub's does, 3×. The honest claim is that the multiple is small relative to what a page-size constant buys, and that GitHub's own docs say the higher-limit app draws down the same account's budget.
- Stripe's 100 a second is **per account and global**, and some endpoints carry their own 25-a-second ceiling — so a backfill and a checkout path share the budget. Say that once; do not invent an endpoint figure the article does not cite.
- Never present $12,600 as the price of a rate limit; it is the price of a plan bought for governance and data residency, whose limit rise arrives as a side effect.
- The 100,000 offset ceiling and the 20-second bucket burst ride in prose under rows 5–6 (same page); both were read on that page by eye. No gate row leads on `100,000` or `20` because the matcher would resolve them on a neighbouring figure.

## Gate result

<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=8 fetched=8 sources=6 hosts=5 decision="sha1:cd94251e00" dedup="matched a prior artifact: 2026-10-21_your-ci-bill-232-hours" window_days=180 checked_at=2026-11-11T19:03:51+00:00 -->
<!-- evergreen-gate:end -->
