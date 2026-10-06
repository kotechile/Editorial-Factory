---
title: "The Cloud Bill Break-Even: When Renting Servers Stops Paying"
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "Leaving the cloud is a choice with clear math: bulk deals only cut cloud server costs by 30% to 50%, while firms that move steady apps to their own gear cut spend by half or more."
date: 2026-10-06
slug: cloud-repatriation-break-even
archetype: evergreen
evergreen: true
meta_title: "The Cloud Bill Break-Even: When Renting Servers Stops Paying"
meta_title_source: "derived_from_title"
meta_description: "37signals cut its cloud bill from $3.2 million to $1.3 million a year by moving seven apps off Amazon and onto its own gear."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/cloud-repatriation-break-even/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "Rows of heavy physical server racks receding into the distance in a massive data center hall."
image_caption: "Moving steady workloads to owned physical servers can cut massive cloud hosting bills by half."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
37signals cut its cloud bill from $3.2 million to $1.3 million a year by moving seven apps off Amazon and onto its own gear [3][5]. That move won back almost $2 million a year. The firm now expects to save $10 million over five years [2][3].

<!-- tension -->

## The big picture:

Cloud prices charge extra for demand you cannot guess. 

When an app runs flat and steady, you still pay for room you never use. Andreessen Horowitz looked at one software firm worth a billion dollars. Its cloud spend reached 81% of the cost of sales, and 75% to 80% is common in the field [1].

Bulk deals do not fix this gap. Long-term deals cut server costs by only 30% to 50%, and Amazon still keeps a profit margin near 30% after them [1].

What strikes me here is the sheer size of the base spend. Flexera's 2026 survey of 753 buyers shows 76% of large firms spend more than $5 million a month on public cloud. Wasted rented space hit 29% [4].

This pressure hurts firms with huge bills and steady loads. It helps the server hosts and bare-metal shops that charge by the physical rack.

One rule forces many of these moves: data fees. Moving data out of a cloud is a metered charge that grows with traffic. Cloudflare prices its own storage with no fee to move data out [6].

## By the numbers

- **$3.2 million to $1.3 million — Yearly cloud bill:** The fall after pulling seven apps off Amazon's cloud is a saving of almost $2 million a year [3][5].
- **81% — Cloud sales cost:** The share of sales cost eaten by public cloud at one billion-dollar software firm [1].
- **29% — Wasted rented space:** The share of rented servers buyers admit goes unused in Flexera's 2026 survey [4].
- **$0.015 per gigabyte-month — Free-transfer storage:** Cloudflare's monthly list price for storage that charges nothing to move data out [6].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">The Cloud Bill Break-Even: When Renting Servers Stops Paying</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">Cloud sales cost</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="243" height="18" rx="4" fill="#818cf8"/>
  <text x="493" y="84" fill="#f1f5f9" font-size="13" font-weight="600">81%</text>
  <text x="547" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Wasted rented space</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="87" height="18" rx="4" fill="#818cf8"/>
  <text x="337" y="132" fill="#f1f5f9" font-size="13" font-weight="600">29%</text>
  <text x="391" y="132" fill="#64748b" font-size="11">([4])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

The teams running these moves skip the debate over whether the cloud is good or bad. I've been watching them sort apps by how wild their traffic swings, hunting for the exact fees that grow with use.

- **The use profile:** A job running flat all day acts differently than a spiky web app. The flat job pays back owned servers, while the spiky one needs rented room.
- **The discount ceiling:** A bulk deal buys only 30% to 50% off the server sticker price [1]. Teams weigh any deeper offer against the hard cost of buying physical racks.
- **The transfer line:** Data fees grow fast as traffic spikes, unlike fixed server costs. Storage with free data transfers lists at $0.015 per gigabyte-month [6]. I would check that exact price against any massive cloud bill.
- **The saving pattern:** 37signals cut its costs by half to two-thirds [2][3]. Dropbox told investors it saved $75 million in the two years before it went public [1].

<!-- nuanced-takeaway -->

## The catch

Moving off the cloud is not free money. Owned gear wears out and needs a strict plan to replace it. 

Someone still has to manage the physical room, cooling, and power limits. 37signals got its massive cut partly because it squeezed new servers into racks and power it already leased [3].

That 29% waste figure is a broad survey average, not a direct read on your own bill [4]. A team dealing with wild demand swings will easily beat physical servers on total cost. Dropbox needed two full years and a large staff to land its $75 million win [1].

My read: treating any single price as a strict law is a mistake. What holds across the sources is narrower. Renting steady servers carries a built-in fee that bulk deals never fully erase.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Calculate Your Career Relocation Payback" -> https://giniloh.com/calculate-your-career-relocation-payback/ [same site (giniloh.com); same category; topical overlap: moving] Link "Calculate Your Career Relocation Payback" in the section where the article touches moving. -->
<!-- internal-link hint: "Expats: Evaluating the True Value of a Job-Driven Move overseas" -> https://giniloh.com/expats-evaluating-the-true-value-of-a-job-driven-move-overseas/ [same site (giniloh.com); same category; topical overlap: moving] Link "Expats: Evaluating the True Value of a Job-Driven Move overseas" in the section where the article touches moving. -->
<!-- internal-link hint: "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" -> https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/ [same site (giniloh.com); topical overlap: cloud, renting] Link "NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…" in the section where the article touches cloud, renting. -->
## Related reading

- [Calculate Your Career Relocation Payback](https://giniloh.com/calculate-your-career-relocation-payback/) — more on Mental Models & Strategy
- [Expats: Evaluating the True Value of a Job-Driven Move overseas](https://giniloh.com/expats-evaluating-the-true-value-of-a-job-driven-move-overseas/) — more on Mental Models & Strategy
- [NVIDIA RTX PRO: Groundbreaking Performance, But Does the Math…](https://giniloh.com/nvidia-rtx-pro-groundbreaking-performance-but-does-the-math-check/) — more on Major Purchases & Assets
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** 37signals cut its cloud bill from $3.2 million to $1.3 million a year by moving seven apps onto its own gear [3][5], projecting roughly $10 million in savings over five years [2].
- **Why It Matters:** Bulk deals only cut server costs by 30% to 50% [1], leaving firms paying a massive fee for unused room on steady apps.
- **What I'd Watch:** How tech teams sort apps by traffic swings to find the exact break-even point.
  - **Use profile:** Whether an app runs flat enough to pay back physical servers within a standard planning cycle.
  - **The discount ceiling:** The 30% to 50% limit on server deals [1], which sets the exact price floor physical ownership must beat.
  - **The transfer meter:** Data fees that grow fast with traffic, compared to free-transfer storage priced at $0.015 per gigabyte-month [6].
- **The Catch:** Owned servers wear out and demand strict power planning, and the best savings rely on fitting new machines into existing rack space [3]. The 29% waste metric [4] is an industry average, not a sure thing.

## Sources
[1] Andreessen Horowitz, "The Cost of Cloud, a Trillion Dollar Paradox" — https://a16z.com/the-cost-of-cloud-a-trillion-dollar-paradox/
[2] 37signals, "Cloud Exit" — https://basecamp.com/cloud-exit
[3] David Heinemeier Hansson, "Our cloud-exit savings will now top ten million over five years" (17 October 2024) — https://world.hey.com/dhh/our-cloud-exit-savings-will-now-top-ten-million-over-five-years-c7d9b5bd
[4] Flexera, "2026 State of the Cloud Report" — https://info.flexera.com/CM-REPORT-State-of-the-Cloud
[5] Data Center Dynamics, "37signals claims it saved almost $2m last year from cloud repatriation" (19 October 2024) — https://www.datacenterdynamics.com/en/news/37signals-claims-it-saved-almost-2m-last-year-from-cloud-repatriation/
[6] Cloudflare, "R2 pricing" — https://developers.cloudflare.com/r2/pricing/

<!-- linkedin -->
I keep coming back to one number from 37signals leaving the cloud: $3.2 million a year down to $1.3 million.

That is almost $2 million a year back, simply by moving seven apps onto gear the firm already owned. It now expects around $10 million in savings over five years.

My read: the interesting part is not that the cloud costs a lot. It is that the vendor discount does not fix the built-in fee. Bulk deals cut server prices by only about 30% to 50%, and Amazon still clears a profit margin near 30% after them.

Andreessen Horowitz tells the exact same story from the other side. They found one billion-dollar software firm where cloud spend reached 81% of its cost of sales. Flexera's 2026 survey puts 29% of rented space squarely in the wasted column.

The detail that stuck with me is the data transfer line. Transfer fees grow fast with traffic, while owned gear does not. Storage with free data transfers lists at $0.015 per gigabyte-month.

What I take from it: this is a pure usage question, not a religious cloud-versus-server debate. The massive savings seem to require a strict hardware cycle and an existing physical data center.

I'm curious how other tech leaders run the break-even math: push for deeper bulk discounts, or pull the heavy apps back to bare metal?

## Gate report
lead
PASS — Delivers the core $1.9M savings takeaway immediately in the first sentence with no preamble, using simple vocabulary.
tension
PASS — Replaces dense jargon with plain English to improve Flesch score, uses a clear first-person cue, and keeps paragraphs under 3 sentences.
tactical-insight
PASS — Observes operator behavior without issuing commands, uses clear bullets with simple wording, and includes a first-person cue.
nuanced-takeaway
PASS — Acknowledges the hard limits of hardware ownership directly, uses a first-person cue, and avoids cliche sign-offs or complex corporate speak.
tldr
PASS — Strictly follows the 4-part Smart Brevity schema, separating the executive summary cleanly from the main text with highly readable plain-English bullets.
