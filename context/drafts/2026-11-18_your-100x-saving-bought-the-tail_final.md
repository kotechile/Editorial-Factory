---
title: Your 100x Saving: A Hidden Cap
vertical: enterprise_build_vs_buy
kind: news
persona: eng_leader
one_big_thing: "A metered unit is a bound, not a price — so the self-hosted saving is the buyer taking back the variance, and it is only collectible by writing the caps the vendor used to write."
date: 2026-11-18
slug: your-100x-saving-bought-the-tail
synthesis: true
sources:
  - https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345
  - https://bruceroettgers.eu/blog/protomaps/
image_path: "context/assets/illustrations/your-100x-saving-bought-the-tail/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "A printed price list on a control-room desk, one row highlighted in yellow beside a steel straightedge."
image_caption: "Self-hosting only pays once you write the caps your vendor used to absorb."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Mapbox's price list says a single map load carries unlimited requests for map tiles [1]. That is a fixed price for work nobody counted, and a self-hoster stops paying it: a 139-gigabyte world map now sits in storage for about $5 a month — the 100x headline — because the person who built it then wrote the limits Mapbox had been writing for him [2]. Revolut made the same trade with models, and its published 30 cents per million tokens is what the bill looks like once it stops moving [3]. The saving is real. The hidden part is what the invoice no longer shows: the caps your vendor had been holding for you, and the tail they absorbed.

<!-- tldr -->
## At a glance
- **The shift:** Vendors meter a unit that holds unbounded work, so the seller carries your heavy traffic.
- **The number:** $5.00 a thousand map loads, against $0.05 to serve them yourself.
- **The risk:** A self-hosted bill stays cheap only if you write the caps.

<!-- tension -->
## What the margin was buying

Revolut's engineers started on Gemini in early 2025, moved to Claude Code in early 2026, and ran both under strict budget limits [3]. The operator's reason was simple: some engineers were spending "$1,000 a month, $10,000 a month" with little return [3]. By November the default was a model the bank runs itself, Z.ai's open-weight General Language Model (GLM-5.3), on 56 Nvidia B200 graphics processing units (GPUs) shared by roughly 2,000 engineers [3]. The published figure is 30 cents per million input and output tokens, about a tenth of what Codex or Claude Code cost, quoted for the earlier GLM-5.1 deployment [3].

The ratio is not the interesting part. What had to be fixed to make it hold is.

The weights alone need 380 gigabytes (GB) of graphics memory, and each user's conversation needs another 6 to 26 GB [3]. So the context window is capped at 256,000 tokens, although the model can serve a million. "Long context is a scam," the operator said [3]. That cap is a product decision, and it is what the 100x was bought with.

A token price equals the work. Every retry and every extra page of context lands on the buyer, which is why the tool shipped with dollar limits. A map load does not equal the work: one load can pull one tile or five thousand, and Mapbox charges the same either way [1]. Its margin was never only the dataset. It was the spread between a light visitor and a heavy one.

Cancel that spread and you inherit it. The map's builder had to allow only named referrers, switch on caching for large objects, throttle any single request to 10 kB/s after 10 megabytes (MB), and set a monthly bandwidth ceiling [2]. Four settings, no code, all of it work Mapbox used to do without being asked. I read the builder's configuration notes twice because none of the four settings is a price: the cap is the product.

Where that lands on a GPU fleet is a question this page has already priced. [Self-hosted AI: when to buy versus rent GPUs](/self-hosted-ai-when-to-buy-vs-rent-gpus/) is the break-even on hardware; this is the break-even on the traffic.

## Who carries the tail

| The unit you buy | What one unit contains | Who carries a heavy client | The cap that follows |
|---|---|---|---|
| A map load | Unlimited tile requests inside one load | The vendor | None for the buyer |
| A million tokens | Exactly the tokens spent, retries included | The buyer | A context ceiling |
| A self-hosted tile file | Every byte a visitor pulls | The buyer | A bandwidth ceiling and a throttle |
| A self-hosted model | Every token, plus each resident conversation | The buyer | A context ceiling and a latency floor |

## By the numbers
- **$0.05:** The builder's own estimate of serving a thousand map loads [2].
- **$5.00:** Mapbox's entry rate for a thousand loads once a site passes 50,000 free ones [1].
- **200 tokens a second:** Revolut's default floor, against about 800 for after-hours sign-ins [3].

<!-- tactical-insight -->
## Where this bites first

The latency target is the tell. Revolut aims for a first token in under three seconds, at a context of 256,000 tokens [3]. The operator's own line is that past five seconds, "my Slack inbox starts to blow up" [3]. Somebody now has to hold that level on hardware the bank owns, and the queue shows up only when the box is busy.

Two signals answer the open question next. Throughput per engineer is one: 2,000 people on 56 cards is about 36 each, and the jump to roughly 800 tokens a second after 5 p.m. suggests the fleet is sized for sessions rather than seats [3]. The other is the daily build behind the map file, which the project publishes on its own schedule [2].

What I find hard to square is how little of this reaches the case for building. The savings are arithmetic on a price list. The caps are a job description, and only one of the two tends to get written down.

<!-- nuanced-takeaway -->
## The catch

The two bills do not cover the same things. Mapbox's unit buys unlimited tile requests and a dataset somebody else keeps current, and a self-hosted map still starts from a daily build [2]. At low volume the build loses outright: $5 of storage plus a $1 monthly minimum is money a free tier does not charge.

The headline multiple also rests on five megabytes a view. Take a month of 100,000 loads, half of them free under Mapbox's tiers. The bill comes to $250 [1]. The same traffic costs about $5 to deliver at the builder's own rate [2].

The multiple is real and it is not the point. My reading is that the build wins on volume and loses on variance. Steady, heavy traffic pays for the caps; a spiky month hands you the spike. That is the line worth writing beside the savings: not the discount, but who holds the caps when the month goes wrong.

## Sources
- [1] Mapbox, "Mapbox pricing" (price list, observed 2026-11-18) — https://www.mapbox.com/pricing
- [2] Bruce Röttgers, "Protomaps: Self-hosting map tiles has gotten cheap and easy", 2026-11-15 — https://bruceroettgers.eu/blog/protomaps/
- [3] The Register, "British fintech Revolut slashes AI coding costs 10x by cutting out Claude and going self-hosted", 2026-11-03 — https://www.theregister.com/ai-and-ml/2026/11/03/british-fintech-revolut-slashes-ai-coding-costs-10x-by-cutting-out-claude-and-going-self-hosted/5307345

<!-- internal-links -->
