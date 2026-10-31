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
Bitwarden's next release ships two builds of the same vault, and the version you install from an app store is no longer the free one. A notice posted on 9 October 2026 states the store apps "will be the commercially licensed builds" [1]. Anyone who wants only the GNU General Public License version 3 (GPLv3) build must side-load it. The notice adds that those users "will not have access to any features that they pay for that is commercially licensed" [1]. The commercial license covers specific modules, granting use "for the sole purposes of internal development and internal testing, and only in a non-production environment" [2].

That non-production clause demands attention. The notice is five lines of routine housekeeping. Yet the file it points to targets people who build against the code, not someone running a vault on a spare computer.

<!-- tension -->

## The big picture:

Self-hosting is often sold as a property right. You hold the app, the argument goes, so nobody can change the terms under your feet. I view this license split as a direct test of that self-hosting promise. A price increase shows up on a monthly bill. A build change happens quietly. What changed this month is which app the vendor hands to the stores, and shipping remains a choice the vendor owns.

The calm public messaging sits awkwardly next to the legal text. The company states "no action is needed", adding that the shift brings "no change to self-hosting" [1]. Staff note the update "only affects those who are repackaging and reselling Bitwarden" [1]. The repo agrees on the open half, as the default license across the clients code is GPLv3, and the Bitwarden-licensed code sits in one directory [3]. Nothing there promises the two builds will stay equal.

The same forum thread says it outright, with staff writing that "some future components will be published under the commercial license and will exist only in that build" [1]. New features get judged "on a case-by-case basis" [1].

## By the numbers

- **2 builds per release:** the vendor compiles a GPLv3 copy and a paid copy of the same apps, and until now the stores received the GPLv3 one [1][3].
- **Clause 2.1 limits production:** the Bitwarden License permits use of its Commercial Modules "for the sole purposes of internal development and internal testing, and only in a non-production environment" [2].
- **60 days for a license refresh:** a business running its own server gets 60 days from its renewal date to update the license file before the server shuts down [4].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this change are not fighting over the text. Instead, they are auditing what sits in each build. A separate audit posted on 11 October claims the two web files shipped side by side in late September [5]. It found the paid bundle carrying files and routes the open one lacks. That is the audit's claim, not a finding from this desk, and anyone can test it by unpacking the two archives. It points the same way as the vendor's own statement about features living in one build only.

What I am watching next is how community forks handle the missing parts.

- **Which build sits on each device:** the store app and the side-loaded app are different files from a single repo, and the notice keeps GPLv3 terms only on the side-loaded version [1].
- **What a mirror project can promise:** asked if the change reached Vaultwarden users, a maintainer replied that the paid features "are not Bitwarden Licensed as far as i know" [6]. The thread closed four days later on whether the apps still talk to each other, not on the license question [6].
- **The renewal date:** for a company running its own server, the license file is a calendar item with a 60-day tail [4].

The open question is what happens to a server when its owner side-loads the free app, upgrades it, and finds a key feature missing. Nobody in the thread provides an answer, and the license does not cover commercial parts in daily use.

<!-- nuanced-takeaway -->

## The catch

My reading is that the admin work matters more than the license text. Bitwarden has not made its code closed, it has not named a price, and it says self-hosting remains untouched. The loudest reaction in the thread claims a free password manager is being taken away, but that is not what the files say [1][3]. The GPLv3 build keeps shipping, and a fork stays legal.

The honest limit is that the split may never matter. If the paid build keeps everything the free one has, the dividing line remains invisible and the notice becomes routine admin after all. The cost nobody has priced is the user's own time. Switching a vault means signing in again on every phone, browser, and desktop. It requires re-teaching a household where the passwords now live. That work is the tinkering tax this beat usually prices in hours and watts. This month, it turned up as an audit instead.

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
