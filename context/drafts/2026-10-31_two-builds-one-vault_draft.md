---
title: 2 Builds, 1 Vault: The License Trap
vertical: personal_microeconomics_tinkering_tax
kind: news
persona: systems_tinkerer_pro
one_big_thing: "The free self-hosted build is now a shipping decision the vendor owns, so the cost of a licence split lands as an audit of every device you enrolled rather than as a price you can see coming."
date: 2026-10-31
slug: two-builds-one-vault
---

<!-- lead -->
Bitwarden's next release ships 2 builds of the same vault, and the one you install from an app store is no longer the free one. A notice posted on 9 October says the store apps "will be the commercially licensed builds" [1]. Anyone who wants only the GPLv3 build must side-load it, the notice adds, and those users "will not have access to any features that they pay for that is commercially licensed" [1]. The licence on the store builds covers what it calls Commercial Modules. It grants use of them "for the sole purposes of internal development and internal testing, and only in a non-production environment" [2].

That clause is the one I read twice. The notice is five lines of housekeeping, but the file it points at is written for people who build against the code, not for someone running a vault on a spare mini PC.

<!-- tension -->

## The big picture:

Self-hosting gets sold to this reader as a property right. You hold the app, the argument goes, so nobody can reprice it under you. A licence split tests that claim harder than a price rise does. A price rise shows up on a bill; a build line does not. What changed this month is which app the vendor hands to the stores, and shipping is a choice the vendor owns.

What I keep circling is how the calm and the clause sit side by side. The company says "no action is needed", and staff add that the change means "no change to self-hosting" and "only affects those who are repackaging and reselling Bitwarden" [1]. The repo file agrees on the open half. The default licence across the clients code is GPLv3, and the Bitwarden-licensed code sits in one folder [3]. Nothing there promises the 2 builds stay equal. 

The same thread says it outright. "Some future components will be published under the commercial license and will exist only in that build," staff write, and new ones get judged "on a case-by-case basis" [1].

## By the numbers

- **2 — builds per release:** It builds a GPLv3 copy and a paid copy of the same apps, and until now the stores got the GPLv3 one [1][3].
- **Clause 2.1 — non-production only:** the Bitwarden License lets you use its Commercial Modules "for the sole purposes of internal development and internal testing, and only in a non-production environment" [2].
- **60 days — licence-file refresh:** a company running its own server has 60 days from renewal to refresh its licence file before the server shuts it off [4].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are not fighting over the text. They want to see what sits in each build. The best attempt so far is a separate audit posted on 11 October. It claims the two web files shipped side by side in late September, with the paid one carrying files and routes the open one lacks [5]. That is the audit's claim, not this desk's finding, and anyone can test it by unpacking two zips. It points the same way as the vendor's own line about features that will live in one build only.

- **Which build sits on each device:** the store app and the side-loaded app are different files from one repo, and the notice keeps GPLv3 terms only on the side-loaded one [1].
- **What a mirror project can promise:** asked if the change reached Vaultwarden users, a maintainer replied that the paid features "are not Bitwarden Licensed as far as i know" and asked where the claim came from [6]. The thread closed 4 days later on whether the apps still talk to each other, not on licensing [6].
- **The renewal date:** for a company running its own server, the licence file is a calendar item with a 60-day tail [4].

The thing I'd want answered is what happens to a server whose owner side-loads the free app, upgrades it, and then finds a feature they use lives only in the build they avoid. Nobody in the thread says, and the licence does not cover commercial parts in daily use.

<!-- nuanced-takeaway -->

## The catch

Where I've landed is that this is a smaller story than the reaction, and a more useful one. Bitwarden has not gone closed, has not named a price, and says self-hosting is untouched. The loudest read of the thread, that a free password manager is being taken away, is not what the files say [1][3]. The GPLv3 build keeps shipping, and a fork stays legal.

The honest limit is that the split may never matter. If the paid build keeps everything the free one has, then the line is invisible and the notice is routine admin after all. The cost nobody has priced is the user's own. Switching a vault means signing in again on every phone, browser and desktop, and re-teaching a household where the passwords now live. That work is the tinkering tax this beat usually prices in [hours and watts](/self-hosting-break-even-one-hour-a-year/). This month it turned up as an audit instead.

<!-- tldr -->

## At a glance

**The shift:** Bitwarden's store builds became the commercial ones, so the free path means side-loading the app.
**The number:** 2 builds per release, and clause 2.1 licenses the commercial parts for non-production use only.
**The risk:** future parts may live in one build, so the free path is a vendor choice, not a promise.

## Sources

[1] Bitwarden community forum, "Published version update in app stores", posted 2026-10-09 — https://community.bitwarden.com/t/published-version-update-in-app-stores/102750
[2] Bitwarden License v1.0, §2.1, in `bitwarden/server` — https://github.com/bitwarden/server/blob/main/LICENSE_BITWARDEN.txt
[3] `bitwarden/clients` LICENSE.txt — https://github.com/bitwarden/clients/blob/main/LICENSE.txt
[4] Bitwarden Help, "License Organizations or Premium" — https://bitwarden.com/help/licensing-on-premise
[5] SoloSoft, "Bitwarden's Dual License Move", 2026-10-11 — https://www.solosoft.dev/post/bitwarden-dual-license-audit
[6] Vaultwarden discussion #7856, "Bitwarden Client License Change", opened 2026-10-15 — https://github.com/dani-garcia/vaultwarden/discussions/7856
