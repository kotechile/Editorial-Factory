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
---

<!-- lead -->
This November your Home Assistant hub adds 4,292 unaudited projects to a menu it now owns, and the blind spot is written into the release notes. The community store that used to be a separate download, the Home Assistant Community Store (HACS), was merged into the platform itself on 2026-10-01 [1]. From release 2026.11, the catalog opens under Settings behind a warning box and nothing else [5]. Twelve days before the migration guide went up, Consumer Reports published its third yearly check of the makers behind that kind of code. It found 11 of 80 with no security contact at all [8].

<!-- tension -->

## The big picture:

The store did not change what it sells. It changed who owns the shelf. The catalog is still the same list of GitHub repos. It is still curated through one file in the HACS project, and each project still lands in the same folder inside the hub's config [6].

What moved is the software between the owner and that folder. HACS was a community project you installed, updated and could remove. From November it is a built-in add-on that Home Assistant blocks you from installing on its own [4].

That is a gain in one direction and a loss in another. The move carries existing installs across on the first restart, keeps their names, and leaves one path for updates instead of two [4]. It also drops two kinds of content from management. AppDaemon apps and Python scripts stay on disk and keep running, but they stop getting updates, and a repair notice is the only signal [4]. The platform's hold on the add-on layer grew in the same release that quietly cut it back.

My read is that the interesting part is not the move but the line the platform wrote next to it. The new docs say it plainly. Nothing in the catalog "is tested, audited, or supported by the Home Assistant project". The content "can access your home, your data, and the system that runs Home Assistant", and anything installed is used "at your own risk" [5].

The security page is blunter. Attacks that "require the user to install a malicious other software, like a third-party integration" are listed as out of scope. The project will not treat them as its problem [7]. The install button now belongs to the platform. The review still belongs to the owner.

That gap is what the second leg measures. Consumer Reports asked 80 smart-home makers about the layer meant to catch bad code before it reaches a stranger's house [8]. It found 84% offering an easy way to report a flaw, 11 with no dedicated contact, and 27 with no formal process for handling a report at all [8]. Only a third were clearly tracking a flaw across their product lines once one turned up, and 21% published the standard contact file that researchers look for [8].

## By the numbers

- **4,292 — Catalog projects:** the exact count in the catalog file on 2026-10-27, plus 957 dashboard cards and themes, all reachable from one admin screen [6].
- **11 of 80 — No security contact:** makers with no set route for a researcher to report a flaw, up from 10 the year before [8].
- **27 of 80 — No reporting process:** firms with no formal way to handle a report, a group that includes 16 with a contact but no process behind it [8].
- **25 of 80 — Answered the survey:** replies fell from 52 the year before, after a 15-day window and a two-week nudge [8].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how much of the gear already exists and is simply not turned on. Home Assistant has shipped an alerts add-on since 2022 that pulls a list of known problems from the foundation and shows it in the repairs panel [9]. The foundation's own roadmap carries an open issue from June. It asks for the power to "centrally disable malicious or vulnerable integrations and Apps", and it is candid that a repairs badge sitting unread for three weeks "is not a response at all" [9].

- **The kill switch:** whether remote disable ships in 2026.11 or later, since that is the gap between a notice and an action when a project turns hostile [9].
- **The catalog check:** whether the store adds any signal past a repo's manifest and the existing submission checks, given that the platform has said it audits nothing [5].
- **The vendor list:** whether the 16 firms with a contact but no process close that gap. And whether buyers start reading a maker's track record the way they read a star count [8].
- **The name that cuts the other way:** Home Assistant itself sits in Consumer Reports' strongest group, with both a contact and a formal process. That is awkward for anyone who wants to read this as plain neglect [8].

<!-- nuanced-takeaway -->

## The catch

I could be wrong to read the warning box as the story. One fair counterweight is that the move deletes a third-party update path. It puts the catalog inside the same release train as the platform's own code, which is a simpler supply chain in the literal sense. Nobody in this window produced evidence of a hostile project in the catalog doing harm, and Consumer Reports measured paperwork and contact routes, not attacks. A missing process is a warning sign, not a body count.

The sample is the other limit. Twenty-five firms replying out of eighty is a thin rate, and the survey's own authors record the drop from 52 without claiming the field got worse [8]. The narrower point still holds. What an owner can check before installing a project is thin, and the platform has now said so in writing.

<!-- tldr -->

## At a glance

- **The Big Shift:** Home Assistant folded the community store into its own release in October. So 4,292 third-party projects now install from one admin screen, under a warning that none of them is audited [1][5][6].
- **Why It Matters:** Local-first ownership used to mean owning the box, the data and the routines. It now also means vetting the code supply chain, because the platform's security page puts hostile add-ons outside the class it will accept as a flaw [7].
- **What I'd Watch:** whether the built-in alerts list gains the power to disable something, and whether a project's track record becomes visible before installation.
  - **Kill switch:** a central instruction that switches off an installed add-on remotely, which today exists only as a repairs notice [9].
  - **Catalog check:** the repo tests a project passes before it appears in the store, which is not an audit [5].
  - **Track record:** whether a maker publishes a contact route and a handling process, the two things Consumer Reports scores [8].
- **The Catch:** the survey measures process rather than attacks, and the reply rate was 25 of 80. The move itself simplifies one update path even as it drops management of AppDaemon apps and scripts [4][8].

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
