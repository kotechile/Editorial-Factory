---
title: "The Grid Bill for AI Data Centers Died by Three Votes"
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "The cost and the calendar for the grid power that AI racks need are now set by state regulators and grid-operator checks, not by utilities and no longer by federal law — so power strategy is regulatory strategy."
date: 2026-10-06
slug: data-center-grid-bill-died-by-three-votes
---

<!-- lead -->
On Sept. 16 the U.S. House voted 417-3 to make big data centers pay the full cost of the grid upgrades their racks require [1][3]. Two weeks later the Senate killed the same bill, 57-43 — three votes short of the 60 it needed [3].

<!-- tension -->

## The big picture:

The Ratepayer Protection Act (H.R. 9340) asked for little. It would have told every state to *consider* a rule that makes a large power user pay for the poles and wires its site forces the utility to build — even if the user later walks away [2]. A "large-load customer" meant a data center that draws 100 megawatts (MW) or more at one site [2].

What stays with me is the vote count. A bill that won the House 417-3 could not pass a test vote in the Senate [3]. The reason: the bill only told states to think about it. Senate Democrats called it a "toothless messaging bill" and voted it down, saying it would not shield homes from rising bills [3]. Analysts said it would only "reinforce" a shift already underway, as states write their own large-load rules [4].

The body that decides whether a rack gets power, though, is not Congress. It is a state utility board and, more and more, a grid operator's audit queue.

## By the numbers

- **417-3 — House vote:** the bill passed the House on Sept. 16 [1][3].
- **57-43 — Senate vote:** it failed a test vote on Sept. 30; it needed 60 votes to move on, and only four Democrats voted yes [3].
- **100 MW — the cutoff:** a "large-load customer" meant a data center that draws at least 100 MW at one site or campus [2].
- **194 gigawatts (GW) — Texas load held up:** on Sept. 3 the grid operator ERCOT gave 204 projects (66.4 GW) base-load status and 158 projects (127.9 GW) studied-load status, and cut 302.2 GW more [6].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are not lobbying. They are reading a calendar. In Texas, the Electric Reliability Council of Texas (ERCOT) has paused the switch-on of new large-load data centers of 75 MW or more until it finishes a check of every project in its queue [6].

- **The audit gate:** ERCOT graded its whole queue on Sept. 3, then opened a check of every large load, with reports due to the Public Utility Commission of Texas by Dec. 10 [6]. A tentative yes is not a connection.
- **The switch-on freeze:** ERCOT will not let a new large data center draw grid power until the check and a community review finish [6]. Galaxy Digital, which got tentative status for about 4.2 GW across five Texas sites, told investors the check "expects to take several months" [7].
- **The state rulebooks:** California signed seven data-center bills on Sept. 21, so sites must "pay their fair share" of grid-update costs [5]. The federal bill would have asked states to consider what states are now doing anyway [4].
- **The behind-the-meter option:** when the connection date is the constraint, the pull to stop waiting on it grows. ERCOT's "studied" load — projects that still face a scarce-capacity allocation — is the part most exposed to a slip [6].

I'd want to know how many operators now price a behind-the-meter option into the plan, rather than treating it as a backup.

<!-- nuanced-takeaway -->

## The catch

I could be wrong to call a failed vote the story. The bill's weakness was inside it: it told states to *consider* a standard, not adopt one. That is why critics could call it a message rather than a law, and why analysts expect little to change [3][4]. Its defeat may cost no megawatt at all.

The harder catch cuts the other way. The audit and the state rules are less about slowing data centers than about deciding who pays and who may build. ERCOT held about 194 GW of load, against 302.2 GW it cut outright — a sign that most of the queue was never going to be built [6]. A grid operator's yes is rationing, and the rationing now runs through a state board, not a federal law. That reading is mine, not any document's.

<!-- tldr -->

## At a glance

- **The Big Shift:** The House passed a bill to make large data centers pay the full cost of the grid upgrades they trigger, 417-3, and the Senate killed it two weeks later on a test vote, 57-43.
- **Why It Matters:** The questions that set a data center's real timeline — who pays for the wires and who is allowed to connect — are being answered by state utility boards and by grid-operator checks, not by federal law, so an infrastructure team's power plan is now a regulatory-timing plan.
- **What I'd Watch:**
  - **The audit gate:** Texas grid operator ERCOT put every large load on tentative status, then opened a check, so a tentative yes is not yet a connection.
  - **The switch-on freeze:** New large data centers of 75 MW or more cannot get approval to draw power until the check and a community review finish.
  - **The state rulebooks:** States such as California are writing their own large-load cost rules, and those dockets — not the federal bill — now set the terms.
- **The Catch:** The federal bill only asked states to "consider" a standard, so its defeat may change little; and grid operators are rationing connections anyway, with most of the queued load already cut.

## Sources

[1] U.S. Congress, "H.R.9340 — Ratepayer Protection Act," 119th Congress, bill record. https://www.congress.gov/bill/119th-congress/house-bill/9340
[2] U.S. Congress, "H.R.9340 — Ratepayer Protection Act," full text. https://www.congress.gov/bill/119th-congress/house-bill/9340/text
[3] R. Cowan & N. Groom, Reuters, "US Senate Blocks Bill to Address Data Center Costs" (2026-09-30). https://www.usnews.com/news/politics/articles/2026-09-30/us-senate-set-to-block-bill-to-address-data-center-costs
[4] Utility Dive, "House passes ratepayer protection bill to limit data center cost shifts" (2026-09-17). https://www.utilitydive.com/news/house-passes-ratepayer-protection-bill-data-centers/830658
[5] Office of Governor Gavin Newsom, "Governor Newsom signs most comprehensive data center laws in the nation, providing communities more control on water, electricity, and land use" (2026-09-21). https://www.gov.ca.gov/2026/09/21/governor-newsom-signs-most-comprehensive-data-center-laws-in-the-nation-providing-communities-more-control-on-water-electricity-and-land-use
[6] ERCOT, "Item 14: Batch Zero Update," Board of Directors Meeting, Sept. 14–15, 2026. https://www.ercot.com/files/docs/2026/09/11/14-Batch-Zero-Update.pdf
[7] Galaxy Digital, "Galaxy Provides Update on ERCOT Batch Zero Large Load Classifications" (2026-09-08). https://investor.galaxy.com/news-releases/news-release-details/galaxy-provides-update-ercot-batch-zero-large-load

<!-- linkedin -->
I've been following the data-center power fight all month, and one vote number stopped me. On Sept. 16 the House passed the Ratepayer Protection Act 417-3 — a bill to make big data centers pay the full cost of the grid upgrades they trigger. On Sept. 30 the Senate killed it, 57-43. Three votes short of the 60 it needed.

My read: the headline is the failure, but the substance is that the bill only asked states to "consider" a standard. So its defeat may change almost nothing — because the states are moving without it, and because the thing that actually gates a data center is not a law. It is an interconnection queue.

The bit I keep circling: in Texas, ERCOT put its whole large-load queue on tentative "Batch Zero" status on Sept. 3 — 204 projects (66.4 GW) as base load, 158 (127.9 GW) as studied load — then paused the switch-on of new large loads of 75 MW or more until it finishes a check. Galaxy's ~4.2 GW of tentative approvals are exactly that: tentative.

What I'm watching next is whether more operators start pricing a behind-the-meter option into the plan instead of treating it as a backup. Curious how others are reading the queue: a real gate, or a date that slips?

## Gate report
lead: PASS — opens with the House vote and the Senate result in the first two sentences; no preamble.
tension: PASS — context signpost under 'The big picture:' plus a 'By the numbers' section; first-person cue ("What stays with me") present.
tactical-insight: PASS — observation-shaped bullets under 'What I'd watch:', first-person cue present, no instructions to the reader.
nuanced-takeaway: PASS — honest limitation with a first-person cue under 'The catch'.
tldr: PASS — four-part schema under 'At a glance' with sub-bullet definitions.
