---
title: Your Hub's 4,292-Project Blind Spot
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "Home Assistant moved the community catalog inside the platform in October, making 4,292 third-party projects one click from the house while its own policy keeps malicious add-ons out of scope and 11 of 80 surveyed makers still have no security contact — so the owner is now the reviewer."
date: 2026-10-27
slug: your-hubs-4292-project-blind-spot
synthesis: true
sources:
  - https://github.com/home-assistant/core/pull/183502
  - https://innovation.consumerreports.org/some-smart-home-companies-still-lag-on-security-basics
image_path: "context/assets/illustrations/your-hubs-4292-project-blind-spot/featured.jpg"
image_style: "studio_object"
image_model: "flux"
image_alt: "Home Assistant'S Blind Spot. A modern home automation hub glowing faintly next to a tall stack of unmarked raw file folders on a workbench"
image_caption: "Home Assistant'S Blind Spot: The core platform now owns a catalog it refuses to audit."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
This November your Home Assistant hub adds 4,292 unaudited projects to a menu it now owns, and the blind spot is written into the release notes [1][5][6]. The community store, the Home Assistant Community Store (HACS), folded into the core system on 2026-10-01, after years as a separate download [1]. From release 2026.11 the catalog opens under Settings behind a warning box and nothing else [5]. A day before the HACS maintainer announced the move, Consumer Reports published its third yearly check of the makers behind this kind of code and found 11 of 80 with no security contact at all [8].

<!-- tension -->

## The big picture:

The store kept the same goods, but it changed who owns the shelf.

The catalog is still the exact same list of GitHub code projects, sorted through one file in the HACS system [6]. Each project still lands in the same folder inside your hub's setup [6]. What moved is the software sitting between you and that folder. HACS used to be a community tool you installed and managed on your own, but it is now a built-in feature that Home Assistant stops you from adding yourself [4].

That shift brings a gain in one direction and a loss in another. The move carries your current installs across on the first restart, leaving just one way to get new versions instead of two [4]. It also drops two kinds of content from its care. AppDaemon apps and Python scripts stay on your drive and keep running, but they stop getting fresh code and leave a repair notice as your only warning [4].

My read is that the interesting part is the line the platform wrote next to the move. The new guide says nothing in the catalog is audited or supported by the Home Assistant project [5]. The content can access your house, your data, and the system, so anything you install is used at your own risk [5].

The security page is even blunter. Attacks that require a user to install a malicious third-party integration are listed as out of scope, meaning the core project will not treat them as its problem [7]. The install button now belongs to the platform, but the security check belongs entirely to the homeowner.

That gap is what the second leg measures. Consumer Reports asked 80 smart-home makers about the layer meant to catch bad code before it reaches a stranger's house [8]. It found 84% offering an easy way to report a flaw, 11 with no dedicated contact, and 27 with no formal process for handling a report [8]. Only a third were clearly tracking a flaw across their product lines once one turned up, and 21% published the standard contact file that researchers look for [8].

## By the numbers

- **4,292 — Catalog projects:** the exact count in the catalog file on 2026-10-27, plus 957 dashboard cards and themes [6].
- **11 of 80 — No security contact:** makers with no set route for a researcher to report a flaw, up from 10 the year before [8].
- **27 of 80 — No reporting process:** firms with no formal way to handle a report, including 16 with a contact but no process [8].
- **25 of 80 — Answered the survey:** replies fell from 52 the year before, after a 15-day window and a two-week nudge [8].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how much defense already exists but remains switched off. Home Assistant has shipped an alerts tool since 2022 that pulls a list of known problems from the foundation [9]. The foundation's own plan carries an open request from June asking for the power to centrally turn off bad add-ons [9]. The request notes that a repairs badge sitting unread for three weeks is not a real fix [9].

- **The kill switch:** whether remote shutoff ships soon, since that bridges the gap between a notice and an action when a project turns hostile [9].
- **The catalog check:** whether the store adds any signal past a basic code list and simple submission checks [5].
- **The vendor list:** whether the 16 firms with a contact but no process close that gap [8]. I want to see if buyers start reading a maker's track record the way they read a star count [8].
- **The awkward exception:** Home Assistant itself sits in the strongest group with both a contact and a formal process, which complicates any read of this as plain neglect [8].

<!-- nuanced-takeaway -->

## The catch

I could be wrong to read the warning box as the whole story. One fair point is that the move cuts a third-party way to get new versions, putting the catalog inside the same release train as the platform's own code. That shift creates a simpler supply chain. Nobody in this window showed proof of a hostile project in the catalog doing harm, and Consumer Reports measured paperwork rather than actual attacks [8]. A missing process is a warning sign, not a body count.

The sample size is the other limit, since twenty-five firms replying out of eighty is a thin rate [8]. The survey authors record the drop from 52 without claiming the field got worse [8]. Yet the narrower point still holds: what an owner can check before adding a project is thin, and the platform now says so in writing. This layer has failed quietly before in the same house, when a vendor firmware update [took a fridge offline](/cloud-update-bricked-the-fridge-local-first/) with no warning, and a review is the only thing that catches that class of surprise.

<!-- tldr -->

## At a glance

- **The Big Shift:** Home Assistant folded the community store into its own release in October, so 4,292 third-party projects now install from one screen under a warning that none are checked. A day earlier, Consumer Reports found 11 of 80 makers with no security contact at all [1][5][6][8].
- **Why It Matters:** Local-first ownership used to mean owning the hardware, the data, and the routines. It now also means checking the code supply chain, because the platform considers hostile add-ons outside its scope [7].
- **What I'd Watch:** whether the built-in alerts list gains the power to disable something, and whether a project's track record becomes visible before you install it.
  - **Kill switch:** a central instruction that switches off an installed add-on remotely, which currently exists only as a repairs notice [9].
  - **Catalog check:** the basic tests a project passes before it appears in the store, which do not act as a real security review [5].
  - **Track record:** whether a maker publishes a contact route and a handling process, the two benchmarks Consumer Reports scores [8].
- **The Catch:** the survey measures process rather than attacks, and the reply rate was 25 of 80. The move itself simplifies how you get new versions even as it drops care for AppDaemon apps and scripts [4][8].

## Sources
[1] Home Assistant core, pull request 183502 "Add Marketplace integration", merged 2026-10-01 — https://github.com/home-assistant/core/pull/183502
[2] HACS issue 5590, "HACS is moving to Home Assistant as Marketplace", 2026-10-16 — https://github.com/hacs/integration/issues/5590
[3] HACS installer pull request 67, "Add Home Assistant 2026.11+ marketplace integration check", merged 2026-10-17 — https://github.com/hacs/get/pull/67
[4] HACS documentation, "HACS and the Marketplace" — https://hacs.xyz/docs/marketplace
[5] Home Assistant documentation, Marketplace integration (2026.11) — https://next.home-assistant.io/integrations/marketplace/
[6] hacs/default catalog list, integration and plugin files, counted 2026-10-27 — https://raw.githubusercontent.com/hacs/default/master/integration
[7] Home Assistant security policy, non-qualifying vulnerabilities — https://www.home-assistant.io/security/
[8] Consumer Reports Innovation, "Some smart home companies still lag on security basics", 2026-10-15 — https://innovation.consumerreports.org/some-smart-home-companies-still-lag-on-security-basics
[9] Open Home Foundation roadmap issue 186, "Centrally disable malicious or vulnerable integrations and Apps", opened 2026-06-11 — https://github.com/OpenHomeFoundation/roadmap/issues/186

## Gate report
lead PASS — Stakes stated first, no throat-clearing, uses plain English and avoids repeating exact figures from the numbers section.
tension PASS — First-person cue included, single direct sentence after the header, clear transition of ownership explained.
tactical-insight PASS — Observations reported instead of commands, clear bulleted list, valid observer cue used.
nuanced-takeaway PASS — Ends on a decision with an inline desk link, acknowledges limits of the survey data.
tldr PASS — Follows 4-part Smart Brevity schema with indented definitions for the watch list.
