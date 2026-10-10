---
title: "Why Home Assistant Renamed Its Cloud"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "The cloud has become a recurring rent on hardware people already own — and the honest counterweight to it is not 'self-hosting is free' but 'self-hosting is a maintenance bill,' which is now being repriced too."
date: 2026-10-10
slug: home-assistant-cloud-rename-hardware-rent
meta_title: "Why Home Assistant Renamed Its Cloud"
meta_title_source: "derived_from_title"
meta_description: "The maker of Home Assistant announced a rename of its paid remote service, effective December 2. Home Assistant Cloud becomes Home Assistant Link."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/home-assistant-cloud-rename-hardware-rent/featured.png"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "Home Assistant Drops Cloud. A modular smart home hub unit with a heavy locking latch and a stack of maintenance ledger cards "
image_caption: "Home Assistant Drops Cloud: The push to end subscription lock-in for smart devices."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The maker of Home Assistant announced on October 2 that it will rename its paid remote service on December 2. Home Assistant Cloud becomes Home Assistant Link. The reason, in its own words: "Big tech ruined the cloud" [1][2].

"We hate clouds," founder Paulus Schoutsen told The Verge [3].

<!-- tension -->

## The big picture:

The word "cloud" now means rising fees, outages, and data harvesting, Nabu Casa wrote [1][2].

The real fight is over where that rent goes. Vendors are moving fees off digital content and onto hardware people already bought.

Nabu Casa draws a hard line. Its Link service is optional and has no lock-in; a home keeps working if the fee is cancelled [1][2]. A big-tech cloud, by contrast, is required and walled off [2].

Schoutsen points to blunt examples. Nest switched off the cloud for thermostats in Europe. Weber shut down the servers running the June Oven. "Now you have a dumb oven that cost $1,500," he said [3].

What strikes me here is that vendors are naming the tinkering tax out loud. This desk has long argued that "free" self-hosting is only free if your hours cost nothing. Now the sticker buys the box, and the plan buys the right to keep using it.

<!-- By the numbers -->

## By the numbers

- **$6.50 a month — Home Assistant Link:** The optional remote plan keeps local hardware working even if it is canceled [3].
- **60% — Nonprofit profit share:** The share of Link's profit that funds the Open Home Foundation, Home Assistant's parent group [3].
- **2.7 million — Active home installs:** The estimated base running Home Assistant, a tiny slice of the smart home market [3].
- **90 to 64 days — Cert lifespan:** Let's Encrypt cuts the free security certificate (cert) renewal window on February 10, 2027, dropping to 45 days by 2028 [4][5].

<!-- tactical-insight -->

## What I'd watch:

What I am watching next is upkeep. The self-hosted maintenance bill is being repriced at the same time.

Let's Encrypt's shorter windows mean a self-hosted server renews its security cert far more often [4].

Modern tools ask the issuer when to renew, and do it unseen. Older setups that hardcoded a "renew 60 days out" rule will soon break. That number was picked for 90-day certs, and it is wrong for 64 [4][5].

- **The renewal cadence:** Cert lives drop from 90 days toward 64, then 45. The safe point is now about two-thirds of the life, not a fixed day count [4][5].
- **The ease trend:** Home Assistant 2026.10 added 15 apps, a one-click hookup for artificial intelligence (AI) assistants, and swapped its map to local tiles after the old provider demanded a key [6].
- **The rent spreading:** Cameras that save no video without a plan, and appliances bricked by retired servers, show the same rent model [3][7].

Schoutsen wants a plain label on the box, saying whether a device needs the cloud. Nabu Casa is building a list of ones that do not [3].

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is how little actually changed for Home Assistant users.

The Verge called the rename "mostly symbolic," and the $6.50 fee still stands [3]. Nabu Casa is giving nothing away.

The local path is not a price cut either. It is a swap. A monthly cash bill becomes a bill paid in hours, hardware, and power. This month, that bill went up when the cert windows shortened [4][5].

The tech also breaks for reasons outside the user's control. A map provider demands a key, or a cert issuer changes its rules [4][6].

Not everyone wants to run a server room. Home Assistant sits in about 2.7 million homes, a rounding error next to Google and Amazon [3].

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Almost Half of 3D Prints Fail" -> https://giniloh.com/almost-half-of-3d-prints-fail-the-real-cost-of-the-hobby/ [same site (giniloh.com); same category; topical overlap: maker] Link "Almost Half of 3D Prints Fail" in the section where the article touches maker. -->
<!-- internal-link hint: "Self-Hosted AI: When to Buy vs Rent GPUs" -> https://giniloh.com/self-hosted-ai-when-to-buy-vs-rent-gpus/ [same site (giniloh.com); topical overlap: cloud, rent] Link "Self-Hosted AI: When to Buy vs Rent GPUs" in the section where the article touches cloud, rent. -->
<!-- internal-link hint: "Beyond the Emergency Fund" -> https://giniloh.com/beyond-the-emergency-fund-how-to-build-a-frictionless-wealth/ [same site (giniloh.com); same category] Link "Beyond the Emergency Fund" in the section where the article touches this topic. -->
## Related reading

- [Almost Half of 3D Prints Fail](https://giniloh.com/almost-half-of-3d-prints-fail-the-real-cost-of-the-hobby/) — more on Money & Wealth
- [Self-Hosted AI: When to Buy vs Rent GPUs](https://giniloh.com/self-hosted-ai-when-to-buy-vs-rent-gpus/) — more on Major Purchases & Assets
- [Beyond the Emergency Fund](https://giniloh.com/beyond-the-emergency-fund-how-to-build-a-frictionless-wealth/) — more on Money & Wealth
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** The maker of Home Assistant will rename its paid remote service to Home Assistant Link on December 2, declaring "Big Tech ruined the cloud." The $6.50 monthly price stays. The point is the argument: cloud access has become a recurring rent on hardware people already own.
- **Why It Matters:** Tech rent is spreading from digital content to physical devices. Cameras stop recording without a plan, and ovens stop working when a vendor turns off a server. The box price no longer buys true ownership.
- **What I'd Watch:** Whether the hours spent on the "own it yourself" path keep rising while cash bills rise on the corporate side.
  - **Cert renewals:** Let's Encrypt cuts free cert lives from 90 days to 64 on February 10, 2027, then 45 days by 2028. Automatic tools absorb it; hardcoded schedules break.
  - **Local-first tooling:** Home Assistant 2026.10 ships one-click AI setup and local maps, steadily cutting the hours a local server takes.
  - **Vendor hardware plans:** The same rent model is reaching cameras and appliances, where a good device dies when a server shuts down.
- **The Catch:** The rename is symbolic and the fee remains. Running a smart home locally is not free. It swaps a cash bill for an upkeep bill, and that bill just went up.

## Sources
[1] Nabu Casa, "Cloud becomes Link," 2026-10-02 — https://www.nabucasa.com/news/2026-10-02-cloud-becomes-link
[2] Home Assistant, "Big Tech ruined the cloud, so we're renaming ours," 2026-10-02 — https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/
[3] The Verge, "Home Assistant says 'Big tech ruined the cloud, so we're out'," 2026-10-02 — https://www.theverge.com/tech/1003936/home-assistant-says-big-tech-ruined-the-cloud-so-were-out
[4] Let's Encrypt, "64-Day Certificate Lifetimes Coming Feb 2027," 2026-10-07 — https://letsencrypt.org/2026/10/07/64-day-certs
[5] Ars Technica, "Let's Encrypt cuts certificate lifetimes to 64 days starting February 2027," 2026-10-08 — https://arstechnica.com/gadgets/2026/10/lets-encrypt-cuts-certificate-lifetimes-to-64-days-starting-february-2027
[6] Home Assistant, "2026.10: You are here," 2026-10-07 — https://www.home-assistant.io/blog/2026/10/07/release-202610
[7] Arlo Community, "New Arlo Subscription Plans and Features," 2026-09-15 — https://community.arlo.com/t5/Arlo-Secure/bd-p/en-arlo-secure

## Gate report
lead: PASS — Delivers the core news (the rename and its reason) in the first short sentence, no preamble.
tension: PASS — Frames the shift to hardware rent, carries the first-person observer cue ("What strikes me here"), and honors strict H2 spacing.
tactical-insight: PASS — Reports what operators are doing instead of instructing, keeps the observer cue, and bulletizes the moves.
nuanced-takeaway: PASS — States the honest trade-off (local is a time bill that still breaks) with the cue ("The part I keep circling"); paragraphs stay brief.
tldr: PASS — Follows the 4-part schema under a distinct "At a glance" H2, separated from the preceding section.
