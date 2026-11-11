---
title: "Your Rate Limit's Hidden 100x"
vertical: enterprise_build_vs_buy
kind: evergreen
archetype: evergreen
evergreen: true
persona: eng_leader
one_big_thing: "A vendor's rate limit is a budget counted in requests, so the page size decides whether a nightly sync finishes long before the plan ladder does."
date: 2026-11-11
slug: your-rate-limit-1-39-a-second
---

<!-- lead -->
Every vendor's rate limit is a budget counted in requests, and GitHub's is 5,000 an hour for a personal token [1]. Because a call returning one record costs exactly what a call returning 100 costs, the scale is the only free lever in the equation. That rule explains a pattern plenty of teams meet at 3am: a nightly sync that used to finish before standup is still running, and the throughput problem is a page-size problem in disguise. The clock is the record count divided by the rate, divided again by the items each request carries. Vendors sell the other half of that division as a plan ladder, and the ladder is real — just small beside the hidden multiplier in your own application programming interface (API) call [2].

<!-- tldr -->

## At a glance

- **The shift:** Rate limits are sold as a plan ladder, from two requests a second to forty.
- **The number:** 500,000 records an hour, at 100 items a page [2].
- **The risk:** The budget is shared per account, so a backfill can starve the interactive path [3].

<!-- tension -->

## The bucket, not the price

Every limit here is a bucket with a hole in it. Shopify's is the plainest: an app gets 40 requests per store, and the bucket drains at two a second [4]. A burst is therefore a loan against the next twenty seconds, not extra capacity. Push past it and the reply is a 429, the web's "too many requests" status, with a retry hint in seconds [4]. GitHub counts per token instead, and the counter is shared, so an app granted the higher limit draws from the same budget as the token it acts for [1].

I read Shopify's bucket table twice before the arithmetic set in. The top rung is forty requests a second, twenty times the standard plan's two [4]. GitHub's enterprise tier is 15,000 an hour, three times a personal token's 5,000 [1]. The price arrives as a per-seat plan at $21 a user a month, so fifty seats is $12,600 a year [5]. Against the 2025 median wage of $65.38, that is about 193 hours of a software developer [6]. It is a governance purchase with a throughput side effect, and reading it the other way round is how teams pay the bill and still wait.

Five thousand requests an hour works out to 1.39 a second [1]. On its own that number is nothing. Multiplied by the 100 items a GitHub page can carry, it is 500,000 records an hour [2]. No rung on any of these ladders sells that multiplication.

Stripe makes the sharing visible on its own page: 100 requests a second for the whole account, with 25 a second on most individual endpoints underneath that ceiling [3]. A month-end reconciliation and a checkout path do not get separate allowances. The budget is per account rather than per workload, and no plan upgrade changes that.

## By the numbers

- **100 items a page:** the ceiling GitHub allows on most endpoints, where one example request returns 30 [2].
- **40 requests per store:** Shopify's bucket, refilling at two a second so a burst lasts twenty seconds [4].
- **15,000 an hour:** the app limit GitHub grants an enterprise organisation, against 5,000 for a personal token [1].

<!-- tactical-insight -->

## Measure the overshoot first

The teams that get this right do one calculation before they ask for a contract. They turn the job into requests, divide by the published rate, and compare the answer with the ladder's multiple. Twice over the limit is a tier decision, because a threefold raise settles it. Fifty times over is a design decision, because no rung on any of these ladders reaches fifty.

What I am watching is where the batching lives. Shopify's page says each request counts equally however little data it returns, which makes page size the cheapest capacity a team owns [4]. GitHub caps that lever at 100 items a request [2]. Shopify's own example pages already move 250 [4].

The second lever is easy to miss: Shopify stops answering once a page offset passes 100,000 records, so a backfill written with page numbers dies at the boundary [4]. The third is patience. Shopify tells apps to average two requests a second rather than spend the bucket at once [4]. Stripe's own guidance is to retry with exponential backoff and jitter instead of firing again immediately [3].

None of this is a rewrite. It is the same unit problem that made [one sign-on feature cost three different prices](/your-sso-bill-125-a-connection/), except the units here are requests and records rather than seats and connections.

<!-- nuanced-takeaway -->

## The catch

The page-size lever stops at the endpoint's own ceiling, and some work never batches. A webhook — a call the vendor makes to your server when something changes — arrives one event at a time. A single-record write is a single request however clever the client is. For those paths the ladder is the honest purchase, and so is a queue that survives a 429 and tries again later.

My reading, held loosely: the two purchases answer different questions. The tier raises a ceiling you are already close to. The page size changes how much of that ceiling you use. A team that cannot say which problem it has will buy the plan, keep the late nights, and blame the vendor.

## Sources

- [1] GitHub Docs, "Rate limits for the REST API" — https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- [2] GitHub Docs, "Using pagination in the REST API" — https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api
- [3] Stripe Docs, "Rate limits" — https://docs.stripe.com/rate-limits
- [4] Shopify, "REST Admin API rate limits" — https://shopify.dev/docs/api/admin-rest/usage/rate-limits
- [5] GitHub, "Pricing" — https://github.com/pricing
- [6] U.S. Department of Labor, O*NET OnLine, "Software Developers (15-1252.00)" — https://www.onetonline.org/link/summary/15-1252.00
