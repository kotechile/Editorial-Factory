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
---

<!-- lead -->
On October 15, the first mandatory reliability rules for data centers cleared their final ballot. The one that matters to an operator starts a clock at a change: within 180 calendar days of a hardware, software, firmware or setting change that alters how the site responds to the grid, its owner has to prove the model still describes the equipment [1][2]. That same week, Nvidia published a test in which 192 chips ran inside a power budget sized for 140. A control loop kept moving the power limits to make room [4]. If your site runs that second thing, your 180-day model is already wrong when it is filed. Neither document says so out loud.

<!-- tension -->

## The big picture:

I have been reading both documents all week, and they describe one object from opposite ends. NERC (the North American Electric Reliability Corp.) treats grid response as a property that changes through events someone can date. Nvidia's controller treats it as a dial that gets tuned all day.

The rulebook first. The package is three new standards on computational load (CLO-001-1, CLO-002-1 and CLO-003-1), plus edits to two interconnection standards [2][3]. It covers any site with at least 50 megawatts (MW) of connected load fed through gear at 100 kilovolts or higher [2]. NERC raised that bar from 20 MW and 60 kilovolts after comments, so fewer sites are caught than the first draft proposed [3]. Existing sites are caught too, not just new ones [5].

Then the clock. Proof that the model matches the installed hardware is due within 365 days of the site going live. After that, each change that alters grid response opens a fresh 180-day window. Between changes, the gap can run to ten calendar years [2]. Planning data is due at least once every 13 months [2]. A planner's technical objection gets an answer inside 90 days [2].

One clause is the hinge. Between changes, a written note saying nothing has changed is enough [2]. The rule assumes a site that sits still.

The other half of the story. Nvidia and Nscale ran MaxLPS (Nvidia's power-allocation controller) on Kimi K2.5 workloads at a campus in Keflavík, Iceland [4]. A static plan ran 140 chips inside a 264.4 kW budget. With the controller on, 192 chips ran inside that same budget [4]. Output rose from 1.08 million to 1.62 million tokens a second, and output per provisioned watt rose from 4.10 to 6.12 [4].

How it did that is the point. The software watches real draw and shifts power between machines. It lifts the limit on one chip when another draws less, while holding the site's total [4]. Mean chip draw rose from 97.0 to 131.8 kW. Total measured power rose from 166.2 to 198.9 kW [4]. The load shape moved because software moved it.

In the same week, the industry wrote down what it wants from a site during a grid event. The Open Compute Project (OCP) grid resilience spec, from Google, Meta, Microsoft and Nvidia, has large sites stay connected, respond on their own, and return to near-full load in under two seconds [6]. Automatic response is the goal, not a bonus.

## By the numbers

- **180 days — Clock starts at a change:** Model proof runs from a hardware, software, firmware or setting change that alters grid response, not from a date, and the standing data refresh is once every 13 months [2].
- **140 to 192 — Chips in one budget:** The same 264.4 kW provisioned budget held 37.1% more chips, with total output up 49.2% and output per provisioned watt from 4.10 to 6.12 tokens a second per watt [4].
- **97.0 to 131.8 kW — Mean chip draw:** Total measured power rose from 166.2 to 198.9 kW, and use of the budget from 62.9% to 75.2%, so the load shape moved while the provisioned number did not [4].
- **17% — Tail latency cost:** The slowest 1% of first tokens got 17% slower from a 15.7-second baseline, while the median and the 75th percentile stayed within 5% [4].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how little of this is hypothetical. Unattended change is already routine in volume. Hewlett Packard Enterprise (HPE) says its customers approved about 10,000 automatic fixes in 90 days, on office networks rather than data-center protection settings. It also says the network clears 70% to 80% of likely faults with no operator on the ticket [7]. That works out to about 111 approved actions a day, set against a filing every 13 months.

- **The next rule is already moving:** NERC's working group signed off the disturbance-performance request on October 13, with the technical committee on October 20 and the Standards Committee on October 21. That rule will define the behaviour the controller is tuning for [3].
- **Owner or operator:** A rule change on October 8 split the entity that owns and maintains a site from the one that runs it. Many firms will learn which one they are at registration, and the 180-day duty sits with the owner [3][5].
- **Joining two logs:** My read is that the operators who get ahead here can show a controller history keyed to the model's dials. Which policy moved which limit, when it moved, and what it did to the load shape. Nvidia's own roll-out method already treats each step that way — the boundary first, then a baseline, then policies added slowly, capacity added with tests at every stage, and production limits fixed last [4].
- **Buyers want the trail:** In a Cisco and Omdia survey of 1,000 network leaders, nearly seven in ten want a clear reason for each AI-driven action. More than half say they run agent systems that act in production today [8]. The audit trail is arriving from the buying side first.
- **Tail latency is the tell:** The 17% shift at the slow end is the kind of number that never shows up in a commissioning file and always shows up in a customer complaint six weeks later [4].

<!-- nuanced-takeaway -->

## The catch

I could be wrong about the join, and the caveats are real. NERC has not said a power cap counts as a setting change. The rule's wording is broad and vague, and a site with relays in front of the controller may argue the controller is not the thing being modeled [2]. The test is one workload at one campus, run by the vendor, and Nvidia says the numbers fit that test setup [4]. The rules are not in force yet: the board votes this quarter, then the filing goes to the Federal Energy Regulatory Commission (FERC), with December 31 as the deadline set in a July order [2][5].

The part I keep circling is that the gap cuts both ways. A model checked against a snapshot of a site that re-tunes itself is not a lie anyone told. It is what the paperwork was built to accept. The harder question is what a transmission planner does with a model that was right in March, for a site that has been retuning ever since.

<!-- tldr -->

## At a glance

- **The Big Shift:** NERC's first mandatory reliability rules for data centers passed their final ballot on October 15. They carry a 180-day model-proof clock that starts when a setting change alters grid response, and in the same week Nvidia showed 192 chips running inside a budget sized for 140 through constant power re-allocation [1][2][4].
- **Why It Matters:** The proof duty lands on discrete changes, while the deployed control loop changes the site's electrical behaviour all day. The filing then describes a site that no longer exists, and that filing is what a planner uses to judge the next disturbance.
- **What I'd Watch:** Whether operators start treating the controller's action log as the compliance record, and how the next rule defines the behaviour being tuned. The pieces to watch:
  - **Disturbance-performance request:** The follow-on rule for how a site must behave during a grid event, now moving through NERC's committees [3].
  - **Owner and operator registration:** The two entity types approved on October 8 decide which firm carries the 180-day duty [3].
  - **Controller change history:** A log that ties each policy or limit change to the model dials it moved, which turns a control loop into evidence [4].
- **The Catch:** NERC has not ruled that a power controller is a setting change, the test is a single vendor run with a 17% tail-latency cost, and the rules still need a board vote and a FERC filing before anything is enforceable [2][4][5].

## Sources

[1] NERC, "NERC's Computational Loads Standards Pass Final Ballot, Advance to Board Adoption," October 15, 2026 — https://www.nerc.com/newsroom/nercs-computational-loads-standards-pass-final-ballot-advance-to-board-adoption
[2] NERC, "CLO-001-1 — Computational Load Interconnection, Studies, & Modeling Data," Final Draft, October 2026 (final ballot October 9–14, 2026) — https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-computational-loads-clo-001-1-final-clean.pdf
[3] NERC, "Large Loads Action Plan Q3 2026 Update" — https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf
[4] Nvidia Technical Blog, "How NVIDIA DSX MaxLPS Maximizes AI Factory Throughput and Efficiency," September 27, 2026 — https://developer.nvidia.com/blog/how-nvidia-dsx-maxlps-maximizes-ai-factory-throughput-and-efficiency
[5] NERC, "Frequently Asked Questions: Computational Loads — Registry Criteria and Project 2026-02 Standards," October 2026 — https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-faq---october-2026.pdf
[6] Nvidia Blog, "OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide," October 12, 2026 — https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories
[7] Fierce Network, "HPE's self-driving network fixes 70–80% of issues on its own: Rahim," October 12, 2026 — https://www.fierce-network.com/cloud/hpes-self-driving-network-fixes-70-80-issues-its-own-rahim
[8] Cisco Blogs, "NetOps Is Already Deploying Agentic Autonomy — Trust Will Decide How Far It Goes," September 23, 2026 — https://blogs.cisco.com/news/netops-is-already-deploying-autonomy-trust-will-decide-how-far-it-goes
