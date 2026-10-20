---
title: Your 180-day model is already wrong
vertical: nhil_infrastructure_ops
persona: it_ops_leader
one_big_thing: "NERC's new computational-load rules attach the evidence duty to setting changes on a 180-day clock, while dynamic power controllers rewrite those settings all day — so the operator has to make the controller's own action log the model-verification record."
date: 2026-10-20
slug: your-180-day-model-is-already-wrong
synthesis: true
sources:
  - https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-computational-loads-clo-001-1-final-clean.pdf
  - https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
image_path: "context/assets/illustrations/your-180-day-model-is-already-wrong/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "NERC Rules Vs Dynamic Power. Isometric cutaway of a server power distribution bay with glowing dynamic routing pathways."
image_caption: "NERC Rules Vs Dynamic Power: New grid rules mandate fixed models for dynamic loads."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The North American Electric Reliability Corporation (NERC) just cleared its first mandatory grid rules for data centers on a final stakeholder ballot [1][2]. The main rule starts a 180-day clock to prove a site model is correct the moment you change a setting. But smart power tools change these settings all day long, which means a fixed model is wrong the second you file it.

<!-- tension -->

## The big picture:

I have read the new rules and the latest hardware tests all week. They describe the exact same system from two different worlds. NERC treats grid response as a fixed trait that changes through clear events. Modern software treats it as a dial to turn all day.

First, look at the rulebook. The final-ballot package holds three new standards for heavy computing loads, plus edits to two grid-connection rules [2][3]. 

This package hits any site pulling at least 50 megawatts (MW) through gear rated at 100 kilovolts or higher [2]. NERC raised this bar from 20 MW and 60 kilovolts after industry pushback, so it catches fewer sites than the first draft [3]. It applies to existing sites, not just new ones [5].

The rule sets a strict clock. Owners must prove their grid model matches the real hardware within 365 days of going live. After that, any change to hardware, software, firmware or settings that alters grid response starts a fresh 180-day clock [2]. 

Between changes, the next verification is due within ten calendar years of the last transmittal, and planning data is due once every 13 months [2]. The rule assumes a data center sits still.

The hardware tells a different story. Nvidia and Nscale recently tested MaxLPS, a power-control tool, on Kimi K2.5 tasks at a site in Iceland [4]. 

A fixed plan fit 140 chips inside a 264.4-kilowatt (kW) power budget. By turning the smart tool on, the site ran 192 chips inside that exact same limit [4]. 

The software watches real power draw and shifts limits between machines. It raises the limit on one chip when another draws less, holding the site's total power steady [4]. The site's power shape moved because software moved it.

That same week, the Open Compute Project published the Grid Resilience Specification with Google, Meta, Microsoft and Nvidia. This standard requires large sites to stay connected during grid faults, respond on their own, and return to near-full power in under two seconds [6]. Automatic response is the goal, not a bonus.

## By the numbers

- **180 days — Rule clock:** Model proof runs from a hardware, software, or setting change that alters grid response, while the standard data refresh is once every 13 months [2].
- **140 to 192 — Chips per budget:** The same 264.4 kW planned budget held 37.1% more chips, with total output up 49.2% [4].
- **97.0 to 131.8 kW — Mean chip draw:** Total measured power rose from 166.2 to 198.9 kW, shifting the power shape while the planned limit stayed flat [4].
- **17% — Slowest delay cost:** The slowest 1% of first tasks got 17% slower from a 15.7-second start point, while the middle group stayed within 5% [4].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how normal these automatic changes are now. Hewlett Packard Enterprise (HPE) says its customers approved about 10,000 automatic fixes in 90 days on office networks rather than data-center protection settings, clearing 70% to 80% of likely faults without a human [7]. That is roughly 111 automatic actions a day, clashing with a grid filing meant to last 13 months.

- **The next rule:** NERC is moving a fault-response request through its committees now. This follow-on rule will define the exact grid behavior the smart controllers are tuning for [3].
- **Owner or operator:** A recent rule change split the group that owns a site from the one running it. Many firms will learn which one they are when they sign up, and the 180-day proof duty sits with the owner [3][5].
- **Joining the logs:** My read is that operators who get ahead here will turn the controller's action history into their rule-following record. Tying each automatic change to the specific grid model dial it moved is the only true proof [4].
- **Buyer demands:** A survey by Cisco and Omdia shows nearly 70% of network leaders want clear proof for Artificial Intelligence (AI) actions [8]. More than half already run automatic tools today, so the demand for clean logs is coming from buyers first.
- **Tail delays:** The 17% slowdown at the bottom end of Nvidia's test is the exact metric that sparks client complaints weeks after a system starts up [4].

<!-- nuanced-takeaway -->

## The catch

I could be wrong about how regulators will read these logs, and the unknowns matter. NERC has not firmly stated that an automatic power cap counts as a setting change [2]. The rule's words are broad, and a site with protection relays in front of the controller might argue the controller is not the gear being modeled. 

The Nvidia test is also a single vendor's run on one site [4]. None of this is a hard law yet. The rules still need a board vote, and the filing has to reach the Federal Energy Regulatory Commission (FERC) by December 31 [2][5].

The part I keep circling is that a model checked against a snapshot of a self-tuning site is not a lie. It is just what the paperwork was built to take. The harder question is what a grid planner does with a model that was right in March, for a site that has been retuning itself ever since.

<!-- tldr -->

## At a glance

- **The Big Shift:** NERC's first mandatory grid rules for data centers cleared their final ballot. The rules start a 180-day clock to prove a grid model is correct when a setting changes, just as smart controllers start shifting those settings all day [1][2][4].
- **Why It Matters:** The rules assume a data center sits still, but new power tools change a site's electrical behavior constantly. This leaves grid planners relying on old paperwork to manage power stability.
- **What I'd Watch:** How operators turn their automatic action logs into the evidence a planner will accept.
  - **Fault-response rules:** A pending NERC rule defining exactly how a site must act during a grid event [3].
  - **Group sign-ups:** New rules separating site owners from operators, placing the strict 180-day burden on the owner [3].
  - **Controller history:** Logs that tie automatic power limits to specific grid model changes to prove the site follows the rules [4].
- **The Catch:** NERC has not said if automatic power tools trigger the 180-day clock, the hardware tests show a single vendor, and the rules still need federal approval [2][4][5].

## Sources

[1] NERC, "NERC's Computational Loads Standards Pass Final Ballot, Advance to Board Adoption," October 15, 2026 — https://www.nerc.com/newsroom/nercs-computational-loads-standards-pass-final-ballot-advance-to-board-adoption
[2] NERC, "CLO-001-1 — Computational Load Interconnection, Studies, & Modeling Data," Final Draft, October 2026 (final ballot October 9–14, 2026) — https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-computational-loads-clo-001-1-final-clean.pdf
[3] NERC, "Large Loads Action Plan Q3 2026 Update" — https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf
[4] Nvidia Technical Blog, "How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency," September 27, 2026 — https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
[5] NERC, "Frequently Asked Questions: Computational Loads — Registry Criteria and Project 2026-02 Standards," October 2026 — https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-faq---october-2026.pdf
[6] Nvidia Blog, "OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide," October 12, 2026 — https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories
[7] Fierce Network, "HPE's self-driving network fixes 70–80% of issues on its own: Rahim," October 12, 2026 — https://www.fierce-network.com/cloud/hpes-self-driving-network-fixes-70-80-issues-its-own-rahim
[8] Cisco Blogs, "NetOps Is Already Deploying Agentic Autonomy — Trust Will Decide How Far It Goes," September 23, 2026 — https://blogs.cisco.com/news/netops-is-already-deploying-autonomy-trust-will-decide-how-far-it-goes

## Gate report

lead
PASS — Defines NERC fully on first use and immediately states the core conflict using plain, short sentences.

tension
PASS — Uses simple words and short paragraphs to clearly contrast the static rulebook with the dynamic hardware reality without jargon.

tactical-insight
PASS — Translates technical moves into plain-English observations, defines all acronyms like HPE and AI, and uses no prescriptive commands.

nuanced-takeaway
PASS — Directly addresses the limitations and regulatory unknowns (defining FERC) in plain language with a strong first-person reflection.

tldr
PASS — Follows the strict 4-part Smart Brevity structure with highly scannable, jargon-free summaries.
