# Verified Brief: enterprise_build_vs_buy — 2026-11-11 (evergreen)

Archetype: evergreen. Topic: a vendor's rate limit is a request budget sold as a tier ladder, and the page size is the lever the ladder cannot sell. Every row below was read on the page itself (not from a search excerpt). All six are first-party documents; the two that are a vendor's own price list are labelled as vendor claims.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | GitHub — personal budget | A personal token gets 5,000 REST requests an hour | VERIFIED | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | "All of these requests count towards your personal rate limit of 5,000 requests per hour." |
| 2 | GitHub — enterprise budget | An app owned by a GitHub Enterprise Cloud organization gets 15,000 an hour, and a higher-limit app draws down the same budget | VERIFIED | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | "Requests made on your behalf by a GitHub App that is owned by a GitHub Enterprise Cloud organization have a higher rate limit of 15,000 requests per hour."; "However, requests made by a higher-limit app reduce the remaining budget available for lower-limit authentication methods." |
| 3 | GitHub — secondary limit | No more than 100 concurrent requests are allowed | VERIFIED (prose only — no gate row) | https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api | "No more than 100 concurrent requests are allowed." |
| 4 | GitHub — page size | The maximum `per_page` is 100 on most endpoints, and the documented example request returns 30 | VERIFIED | https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api | "For most endpoints, the maximum value of per_page is 100."; "GET /repos/octocat/Spoon-Knife/issues will only return 30 issues from the octocat/Spoon-Knife repository" |
| 5 | Stripe — global budget | The global live-mode limit is 100 requests a second per account, 25 in sandbox, and 25 a second on most individual endpoints | VERIFIED | https://docs.stripe.com/rate-limits | "Global API rate limit Live mode : 100 requests per second Sandbox : 25 requests per second"; "Individual API endpoints (unless otherwise noted) 25 requests per second" |
| 6 | Stripe — retry guidance | Stripe tells callers to retry with exponential backoff and jitter | VERIFIED | https://docs.stripe.com/rate-limits | "reduce simultaneous requests and retry with exponential backoff and jitter" |
| 7 | Shopify — plan ladder | The plan ladder is 2, 4, 20 and 40 requests a second | VERIFIED | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | "Standard limit : 2 requests/second Advanced Shopify limit : 4 requests/second Shopify Plus limit : 20 requests/second Shopify for enterprise (Commerce Components) : 40 requests/ second" |
| 8 | Shopify — bucket | The bucket holds 40 requests and refills at two a second; a burst is 20 seconds of banked capacity | VERIFIED | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | "Bucket size : 40 requests/app/store Leak rate : 2/second"; "you can build your app to average two requests per second" |
| 9 | Shopify — the load-bearing sentence | Each request costs the same however little data it returns | VERIFIED | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | "Each request counts equally, regardless of how much or how little data is returned." |
| 10 | Shopify — offset ceiling | A page offset past 100,000 records returns a 429 | VERIFIED | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | "When the value of the page parameter results in an offset of over 100,000 of the requested resource, a 429 Too Many Requests error is returned." |
| 11 | Shopify — example page size | The page's own example uses `limit=250` | VERIFIED | https://shopify.dev/docs/api/admin-rest/usage/rate-limits | "a request to GET /admin/collects.json?limit=250&page=401 would generate an offset of 100,250 (250 x 401 = 100,250)" |
| 12 | GitHub — price (vendor claim) | GitHub Enterprise lists at $21 a user a month | VERIFIED (vendor claim) | https://github.com/pricing | "$ 21 USD per user / month" |
| 13 | O*NET — wage | Software developers' median wage is $65.38 an hour, 2025 vintage | VERIFIED | https://www.onetonline.org/link/summary/15-1252.00 | "Median wages (2025) $65.38 hourly, $135,980 annual" |

## Derived arithmetic (desk, recomputed 2026-11-11 — no gate reads these)

- 5,000 ÷ 3,600 = **1.389** requests a second; 15,000 ÷ 3,600 = **4.167**.
- 5,000 requests × 100 items = **500,000 records an hour**; at 30 items a page it is 150,000.
- 15,000 ÷ 5,000 = **3×**; 40 ÷ 2 = **20×**; 40 requests ÷ 2 a second = **20 seconds** of burst.
- 100,000 ÷ 250 = **400 pages** before Shopify's offset ceiling bites.
- $21 × 50 seats × 12 = **$12,600 a year**; 12,600 ÷ 65.38 = **192.7 engineer-hours**.
- 100 ÷ 1.389 = **72×** — Stripe's global ceiling against GitHub's per-token one.

## Binding rulings for the drafter

1. **Never say a tier does not raise the limit.** GitHub's does, threefold; Shopify's does, twentyfold. The defensible claim is that the multiple is small against what a page-size constant buys, and that GitHub's own docs say the higher-limit app draws from the same account's budget.
2. **$12,600 is not the price of a rate limit.** It is the price of a 50-seat Enterprise plan bought for governance and data residency, whose limit rise arrives as a side effect. Write it that way or leave it out.
3. **Stripe's 100 a second is per account and global.** Some endpoints carry their own 25-a-second ceiling. A month-end reconciliation and a checkout path share one budget; do not claim separate allowances exist.
4. **Shopify's numbers are plan-specific.** 2 a second is the standard plan's leak rate; Plus and Commerce Components multiply both the rate and the bucket. Never present 2 a second as Shopify's limit without naming the plan.
5. **The 30-item figure is the documented example's output, not a stated default** — the page says the example request "will only return 30 issues". Write it as the example, as the draft does.
6. **The concurrency limit (100 concurrent) rides in prose only** — a row led on `100` cannot be evidenced, because the matcher resolves it on the `per_page` sentence earlier in the same page.
7. **The article's own link** goes to `https://aichieve.net/your-sso-bill-125-a-connection/` (probed 200 on 2026-11-11), this vertical's prior evergreen on unit pricing. It is the only body link.
