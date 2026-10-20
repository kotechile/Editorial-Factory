---
title: Your Lock's Blind 90% Bet
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "A 2027 door lock is a choice between four different meanings of local — on-device, on-hub, on-your-block and on-the-vendor's-permission — and only one question survives all four: what has to be alive for the bolt to retract."
date: 2026-10-20
slug: your-locks-blind-90-bet
synthesis: true
sources:
  - https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories
  - https://www.aboutamazon.com/news/devices/ring-smart-lock-battery-recharge
image_path: "context/assets/illustrations/your-locks-blind-90-bet/featured.jpg"
image_style: "editorial_macro"
image_model: "flux"
image_alt: "The Smart Lock Network War. Extreme close-up of a brushed-steel smart deadbolt extending from a door edge against a dark"
image_caption: "The Smart Lock Network War: Four definitions of local control for your front door."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Ring's new smart lock keeps working when your home Wi-Fi dies, because it routes around your router. The deadbolt stays online through Amazon Sidewalk, a web of nearby Echo and Ring devices, and Amazon says that web covers more than 90% of people in the U.S. [4][6][7]. Your lock's blind 90% bet is which network has to stay alive.

Six days later, Apple announced a lock with a different plan. The bolt uses Matter (the smart home standard) and Aliro, and Apple claims it works "entirely locally" so core functions survive internet outages [1].

Both companies sell local control. They mean different things by it.

<!-- tension -->

## The big picture:

Matter has been the baseline for gadgets that work together for years. Buy a device with the badge, and it should talk to your hub. Apple just shipped its own hardware that earns the badge honestly [1].

Its hinge is the part no box mentions. You still need a hub you buy and a Wi-Fi network you keep [3].

What strikes me here is that Amazon did not argue about any of it. It went around.

The Ring lock gets its link from a network Amazon already runs. A Sidewalk device reaches a Bridge up to half a mile away. That Bridge sends the traffic to the cloud [4].

Amazon says more than 90% of people in the U.S. live inside that cover [4]. You need no hub on your side. You need no home router in the path.

Local control now covers four setups, and each one fails in its own way. Local on the device means the bolt decides by itself. Local on your hub uses Thread and Matter, with a box holding the keys.

Local on your block means a neighbour's Echo carries the message. Local by the vendor's say-so means a working link that a software change can switch off.

That last one is real. The Home Assistant platform dropped its SolarEdge Local link in October. SolarEdge had turned off the local web interface in inverter software changes starting in 2020 [8].

The fix reads the same inverter over the home network, with no account and no cloud [8]. The wiring never changed. The permission did.

## By the numbers

- **More than 90% — Sidewalk's reach:** Amazon says over 90% of people in the U.S. live in an area with Sidewalk coverage, and a device can reach a Bridge up to a half mile away before the Bridge carries the data to the cloud [4].
- **0.15% — The neighbour's share:** A Sidewalk Bridge gives up no more than 0.15% of average U.S. household internet use, which Ring likens to streaming about 10 minutes of 4K resolution video [5].
- **10 days — Apple's video window:** Camera events sit in the buyer's iCloud+ plan for 10 days, and Apple says there is no separate camera subscription [1].
- **13 November — The hub ships:** HomeView pre-orders opened on 13 October, with availability from 13 November, and the accessories follow from December [2][3].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are not arguing about rules. They are arguing about what stays online.

- **Which parts count as core:** Apple says the lock's core access functions survive with no internet [1]. I want that list, because LG (the electronics maker that builds the cameras) says the family needs an Apple hub and a Wi-Fi connection [3]. One function on the device and one need in the house can both be true.
- **Whether the cover language firms up:** Ring's footnote lets Sidewalk coverage change or stop, and Amazon's own guide says the Bridge hands data to the cloud [4][7]. The signal I am watching for is the first public account of a lock that fails during a local outage.
- **Where the bill lands:** Apple's answer to "no hub" is a hub, and HomeView is one more purchase on top of the lock [2]. Amazon's answer is a network it owns and does not charge for [5]. That explains why the spec sheets look alike but the bills do not.
- **Where the off switch sits:** The SolarEdge case shows a local link dying on a software call, with the community rebuilding on a second local one [8]. The open question for both locks is which of their local paths is written down and which is a favour.

<!-- nuanced-takeaway -->

## The catch

The honest version is that Amazon's lock drops a need that Apple's stack keeps. Apple's lock promises something Amazon's cannot. It keeps a core function that never leaves the door.

Both claims are narrow. Both are true as written.

Ring's Sidewalk route still ends at a cloud, just later in the path. The network is Amazon's, with the coverage footnote written for the places it does not reach [4][7]. Apple's route ends at your hub, which is a computer the buyer has to buy, power, and patch [3].

Neither is an island. My read, held loosely, is that "works locally" has become the least useful line on a smart home box. It names a shape, not a promise.

The question that survives all four meanings is duller and better. What has to be alive for the bolt to retract?

<!-- tldr -->

## At a glance

- **The Big Shift:** In the same week, Ring shipped a smart lock that stays online through Amazon Sidewalk instead of home Wi-Fi, and Apple shipped a lock it says works entirely locally over Matter, Thread, and Aliro. Two answers to the same failure, six days apart [1][6].
- **Why It Matters:** Neither answer removes a need. It moves the need. Apple's family calls for a hub and Wi-Fi, by its own partner's words, and Amazon's calls for Sidewalk cover that its own footnote can interrupt [3][7]. For a 2027 lock purchase, "local" no longer says which network has to survive a bad night.
- **What I'd Watch:** Which parts of each promise hold in an outage, and how each vendor writes them down.
  - **Core functions:** The short list of things a lock can still do with no internet, which Apple says it keeps and nobody has published yet.
  - **Cover terms:** Whether the "subject to change or interruption" line survives Sidewalk's first public failure.
  - **The vendor's off switch:** The SolarEdge Local removal, where a software change retired one local link and the fix was a second local one.
- **The Catch:** Apple's local path runs through hardware the buyer owns and has to keep running. Amazon's runs through a network it operates. Both are real, but neither is freedom.

## Sources

[1] Apple, "Introducing Apple Home Collection, a new lineup of smart home accessories," 2026-10-13 — https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories

[2] Apple, "Meet Apple HomeView, a new way to enjoy entertainment, stay connected, and manage the home," 2026-10-13 — https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home

[3] LG Global Newsroom, "LG Electronics Announces New Smart Home Accessories, Designed in Collaboration With Apple for the Apple Home Collection," 2026-10-13 — https://www.lg.com/global/newsroom/news/corporate/lg-electronics-announces-new-smart-home-accessories-designed-in-collaboration-with-apple

[4] Amazon, the About Amazon explainer on Amazon Sidewalk — https://www.aboutamazon.com/news/devices/everything-you-need-to-know-about-amazon-sidewalk

[5] Ring, "Amazon Sidewalk" product page — https://ring.com/amazon-sidewalk

[6] Amazon, "Ring ends smart lock anxiety with a lock you can recharge by hand," About Amazon, 2026-10-07 — https://www.aboutamazon.com/news/devices/ring-smart-lock-battery-recharge

[7] Ring, "Ring Announces Smart Lock, Expands 4K Camera Lineup, and Introduces New Pan-Tilt 2K Indoor Camera," The Ring Blog, 2026-10-09 — https://blog.ring.com/products-innovation/ring-announces-smart-lock-expands-4k-camera-lineup-and-introduces-new-pan-tilt-2k-indoor-camera

[8] Home Assistant, "2026.10: You are here," 2026-10-07 — https://www.home-assistant.io/blog/2026/10/07/release-202610

## Gate report
lead: PASS — Direct opening under 28 words, zero filler, split into short paragraphs of 1-3 sentences.
tension: PASS — Clear signposting, paragraphs strictly 1-3 sentences, uses first-person observer cue, highly readable plain English.
tactical-insight: PASS — Bulleted list, no imperative commands, the co-developer's name is spelled out on first use.
nuanced-takeaway: PASS — Honest trade-off presented, uses "My read" cue, strictly short paragraphs.
tldr: PASS — Strict 4-part Smart Brevity structure with indented sub-bullets and plain language.
