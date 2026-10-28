---
title: "Your SSO Bill: $125 a Connection, $7.75 a Seat"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "One sign-on feature is sold in three units — a per-connection price with no cap on users, a per-seat tier uplift, and a flat plan fee — so the unit printed on the quote sets the bill, and Slack's seat uplift alone passes a whole identity connection once a team clears sixteen seats on that one tool."
date: 2026-10-28
slug: your-sso-bill-125-a-connection
archetype: evergreen
evergreen: true
---

<!-- lead -->
Your single sign-on (SSO) bill now arrives in three units for one feature, because vendors price the same identity handshake three distinct ways. The unit printed on the quote sets the final number, regardless of the provider. WorkOS charges $125 a month for each connection and says the count of end users does not change the bill [1]. Slack takes a second route, lifting the whole seat into a higher tier. A seat costs $7.75 a month more on annual billing, $15 against $7.25, once Security Assertion Markup Language (SAML) shows up in its plan table [2]. Okta, Google and Azure all speak this standard. Sentry takes a third shape, folding the same feature into a flat $80-a-month plan that costs the same at one engineer or forty [4].

<!-- tension -->

## The big picture:

Sign-on used to be custom code a platform team wrote once and kept alive for years. It is now a line item on three kinds of price cards, because the large identity providers settled on a handful of standards and every vendor can resell the handshake. Each card measures a completely different thing. A connection counts the links to customer login systems, a seat counts the people on your team, and a plan gate counts the software tiers.

These three units do not swap cleanly for one another, which makes the market read as confusing rather than competitive. A per-link price buys the handshake for an application you run, allowing one link per customer login system [1]. A per-seat suite buys staff sign-in capabilities for your own firm. A tier gate is what a software vendor charges inside its own product for the same handshake. It is the shape most leaders meet first, because it arrives on a renewal sheet rather than in a new buying file [2].

I look at these three models and see a market that settled on a technical standard but never agreed on a commercial unit. An internal container deployer, built to dodge a licence fee, burned 1,200 hours of senior platform time over two years with sign-on among the additions, and was scrapped anyway ([Your Cluster's Hidden Clock](/your-cluster-hidden-clock/)). That engineering team bought none of the three shapes. It paid in hours, the fourth unit, and the only one with no price tag printed on it.

## By the numbers

- **$7.75 a seat — the tier uplift:** Slack prices its Business+ seat at $15 against $7.25 on the Pro tier, meaning a two-hundred-seat team pays $18,600 a year more to put sign-on inside a tool it already uses, while one WorkOS connection with no user cap is $1,500 [1][2].
- **16 seats — where the gate passes the connection:** If you divide the connection price by the seat uplift, the per-seat gate costs more than a whole identity connection once a team clears sixteen seats on that single tool [1][2].
- **23 engineer-hours — the build line:** One month of the connection price equals 1.91 hours of developer time at the median wage, meaning a connection costs about 23 engineer-hours a year, and a home-built sign-on layer that eats more than that per connection loses on labor before it ever loses on uptime [1][5].
- **$54 a month — the flat-plan gate:** The Sentry business plan is $80 against the team plan's $26, so sign-on there costs $648 a year at any headcount [4].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this problem are separating two distinct counts, because the figure that decides a quote is people for one shape and login links for another. That split rarely shows up on a standard purchase order, so the billing details demand careful attention.

- **The seat count, not the tool count:** A tier gate bills per person, so its total cost climbs every month the headcount does, while a connection price stays flat when the engineering team doubles [1][2]. A four-hundred-person firm on one gated tool already pays more for sign-on than a smaller rival pays for a whole identity layer.
- **The flat plan that hides the gate:** Where sign-on rides on a plan a team would buy anyway for monitoring or issue tracking, the extra cash is real but nobody books it to identity, so the cost never reaches the build-or-buy discussion [4].
- **The blank quote:** Linear lists sign-on only in its Enterprise tier, prices Enterprise as "Custom", and demands annual billing, so the one tier with the feature is the one tier a buyer cannot model from the public page [3].
- **What a connection does not buy:** Creating and removing accounts, plus streaming the audit log, are separate line items on the same WorkOS pricing ladder [1]. A team that buys the handshake still owns the account administration work around it.

What I am watching next is whether the blank quote becomes the industry standard for identity features. If the tier that carries sign-on keeps sliding toward a hidden sales conversation, the only open comparison left will sit between dedicated identity vendors, and buyers will lose the ability to test a software gate against anything.

<!-- nuanced-takeaway -->

## The catch

My reading is that the tier uplift operates as a price ceiling rather than a direct bill for identity. Slack's Business+ tier also carries native data loss prevention, mobile device management and user provisioning, so a team that needs those features has already bought the tier [2]. Where sign-on is the only reason to upgrade, the financial gap is the exact number worth arguing at renewal.

The vendor's own comparison line deserves the same level of doubt. WorkOS prints "vs $100 to build it yourself" next to its connection price, with no period, no scope and no basis [1]. Read as a monthly rate, it makes every internal build look cheap; read as a one-off charge, it makes every build look free. Neither reading is supported on the page.

The prices here are list figures read on 2026-10-28, and the short promotion on Slack's cards is left out, so the lasting claim is the architectural shape rather than the current rate. A per-seat gate rises with headcount, a per-connection price does not, and WorkOS's own ladder cuts the connection unit only as the total connection count grows [1]. The specific rate will expire over time; which side of the crossing a team sits on will not.

<!-- tldr -->

## At a glance

- **The Big Shift:** One sign-on feature is now sold three ways — per connection, per seat as a tier upgrade, and as a flat plan fee — meaning the same technical handshake lands as very different bills.
- **Why It Matters:** The unit on the quote decides whether the cost tracks headcount, tracks how many customer login systems a team serves, or never moves, and most renewals never name which one is being charged.
- **What I'd Watch:** I am watching which billing unit spreads as vendors adjust their tiers.
  - **Connection pricing:** A fee per login link with no charge per user, which suits large teams.
  - **Tier gating:** Sign-on sold only in the next plan up, priced per seat, climbing with total headcount.
  - **Flat plan fees:** Sign-on folded into one monthly plan, hidden in a budget line nobody calls identity.
- **The Catch:** A tier upgrade usually bundles more than sign-on, so the pricing gap is a ceiling on what the feature costs, and only published shapes can be computed while custom tiers remain opaque.

## Sources

[1] WorkOS, "Pricing" (Enterprise SSO, Directory Sync and Audit Logs; connection bands and the end-user pricing FAQ) — retrieved 2026-10-28. https://workos.com/pricing

[2] Slack, "Pricing" (Pro, Business+ and Enterprise+ plan table; SAML single sign-on and SCIM user management) — retrieved 2026-10-28. https://slack.com/pricing

[3] Linear, "Pricing" (Business and Enterprise tiers; SAML and SCIM) — retrieved 2026-10-28. https://linear.app/pricing

[4] Sentry, "Pricing" (team, business and enterprise plans; SAML + SCIM support) — retrieved 2026-10-28. https://sentry.io/pricing/

[5] O*NET OnLine, "15-1252.00 — Software Developers" (median wages, 2025) — retrieved 2026-10-28. https://onetonline.org/link/summary/15-1252.00
