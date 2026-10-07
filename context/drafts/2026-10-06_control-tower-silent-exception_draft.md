---
title: "Will Your Control Tower Auto-Resolve the Theft It Can't See?"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "The cargo-theft exception that costs the most — a load handed to a fake carrier at pickup — is the one a control tower is least able to flag, so agent autonomy should be tiered by loss severity, not by how often an exception fires."
date: 2026-10-06
slug: control-tower-silent-exception
synthesis: true
sources:
  - https://www.tive.com/press-release/tive-research-45-of-companies-using-active-monitoring-recover-more-than-half-of-stolen-cargo-1-5x-the-rate-of-those-relying-on-passive-monitoring
  - https://www.scmr.com/article/agentic-ai-supply-chain-exception-management
---

<!-- lead -->
A load stolen by a fake carrier never shows up as a late load. That is the trap hiding inside two pieces of research published a day apart in late September. Tive asked 442 supply chain leaders how they protect freight. Teams watching goods in transit recover more than half of a stolen load 45% of the time. Teams working from after-the-fact reports manage 30% [1]. The same survey found that 55% of the leaders who could name how their latest theft began blamed a false identity at the pickup dock [1]. A day later, Supply Chain Management Review set out the case for letting software agents clear routine exceptions on their own [2]. Put those three facts side by side and a control tower is watching the wrong end of the problem.

<!-- tension -->

## The big picture:

A control tower earns its keep by noticing when the plan bends. A trailer sits too long, a route drifts off its lane, a temperature climbs past its limit — the system catches the bend and raises a flag. That logic assumes the freight left under a real carrier and something went wrong on the road.

The loss that is growing does the opposite. The load checks out at pickup and simply never arrives. Tive's chief executive, Krenar Komoni, put the shift plainly: "Cargo theft is becoming harder to catch at the point of pickup. A load can leave looking legitimate, and the first signs of a theft may come while the shipment is already on the move" [1]. An exception desk is built to catch motion. This exception is a missing phone call.

I keep circling the same asymmetry: the monitoring with the best recovery numbers is pointed at the moment after the loss is already gone.

## By the numbers

- **45% vs 30% — Recovery gap:** Teams using active in-transit monitoring recover more than half of a stolen load 45% of the time, against 30% for teams relying on passive monitoring [1].
- **53% vs 29% — Route-deviation edge:** Route-deviation alerts show the strongest recovery margin of anything measured, nearly 1.8 times the rate of teams without them [1].
- **55% — Fraud at pickup:** Of the leaders who could identify how their most recent theft began, 55% cited identity-based fraud — fake identities, fictitious pickups, and synthetic ones [1].
- **84% — Ready to delegate:** 84% would trust software to run at least one cargo-security job without approval, and only 16% want a person to review every alert [1].

<!-- tactical-insight -->

## What I'd watch:

- Operators are starting to treat carrier identity as a live signal rather than a check at onboarding. The patterns under discussion are behavioral: a first-time lane, a pickup that starts outside the carrier's usual area, a driver or tractor that does not match the record, a seal and an arrival time that disagree.
- The recovery data points at route deviation as the single strongest lever, and I'd want to know whether that same alerting can be aimed at the pickup event rather than only at the highway [1].
- Delegation is arriving faster than oversight. Most respondents would hand software some cargo-security authority, yet the review's own rule for it keys on volume, clear rules and limited downside, with consequential calls going to a person [2].
- What strikes me is where that leaves the expensive case. A system that auto-closes a clean-looking pickup — marking it delivered and clearing the flag — can erase the last trace of a load that was never going to arrive.

<!-- nuanced-takeaway -->

## The catch

The honest counter is that in-transit monitoring is not wasted here. A fraudster still has to move the trailer, and route deviation remains the strongest recovery signal anyone has measured [1]. The delegation push is reasonable too: a queue of thousands of routine exceptions a day is a real cost, and a person approving each one is not a serious control.

What strikes me is the mismatch, not the direction. The tiering rule now being written sorts authority by how often an exception fires and how clean its rule is. Identity fraud at pickup fails both tests — it is neither high-volume nor rule-clear; it is one plausible-looking event that breaks late — while carrying the largest loss. I could be wrong, but that looks like a design that automates the cheap cases and leaves the expensive one dark.

<!-- tldr -->

## At a glance

- **The Big Shift:** Two studies published a day apart in late September 2026 point at the same thing. In-transit monitoring is what recovers stolen freight, and identity fraud at pickup is what starts most thefts. A control tower built to catch motion anomalies sees neither half cleanly.
- **Why It Matters:** The losses that are growing are the ones a dashboard struggles to flag. An exception desk staffed and tuned for high-volume events will keep auto-clearing the cheap cases while the exception that empties a trailer stays quiet.
- **What I'd Watch:** Whether the recovery signal from in-transit alerts transfers to the pickup event, and how much authority operators hand an agent over an exception that looks routine.
  - **Route deviation:** A live alert when a trailer drifts off its planned lane. Tive's data shows the strongest recovery margin of any tool measured.
  - **Identity as a runtime signal:** Judging a carrier during the pickup — a first-time lane, an origin outside its usual area, a driver-tractor mismatch — instead of trusting an onboarding check.
  - **Autonomy tiering:** The proposal to let agents clear high-volume, rule-clear exceptions and escalate consequential ones. The open question is where a fraud pickup lands.
- **The Catch:** Monitoring still helps, because a stolen trailer has to move. But an agent that auto-closes a clean-looking pickup can clear the last trace of a load that never arrives, so the authority limits and the audit trail have to be settled before the speed is.

<!-- internal-links -->

## Sources
[1] Tive, "Cargo Theft Prevention in the Age of AI" — survey of 442 supply chain, transportation, operations, security and executive leaders across North America, Europe and Latin America; published 2026-09-29 — https://www.tive.com/press-release/tive-research-45-of-companies-using-active-monitoring-recover-more-than-half-of-stolen-cargo-1-5x-the-rate-of-those-relying-on-passive-monitoring
[2] Souraj Roy and Samriddha Basu, "From forecast to action: How agentic AI is rewiring supply chain exception management," Supply Chain Management Review, 2026-09-30 — https://www.scmr.com/article/agentic-ai-supply-chain-exception-management

<!-- linkedin -->
I keep coming back to one pair of numbers from the last week of September. On Sept. 29, Tive published a survey of 442 supply chain leaders showing that teams watching freight in transit recover more than half of a stolen load 45% of the time, against 30% for teams working from after-the-fact reports. In the same survey, 55% of the leaders who could name how their latest theft began pointed at a false identity at the pickup dock. A day later, Supply Chain Management Review argued that software agents should clear routine exceptions on their own.

My read: those two things do not sit well together. A control tower is tuned to notice motion that goes wrong — a trailer sitting too long, a route that drifts. A load taken by a fake carrier does neither. It checks out at pickup and never arrives.

The part I keep circling: the delegation rule being written keys on how often an exception fires and how clean its rule is. The fraud pickup fails both — it looks routine right up until it isn't — so the case that costs the most is the one most likely to stay with a person, or worse, get closed automatically.

I'm curious how others are reading it: is carrier identity something you now check during the pickup, or still a box ticked at onboarding?
