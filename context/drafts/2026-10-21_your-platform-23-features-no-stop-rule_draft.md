---
title: "Your Platform: 23 Features, No Stop Rule"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "AI did not settle build versus buy; it moved the risk from the subscription line onto a feature list nobody agreed to stop growing, and the teams that build most are the least likely to have written the rule that ends it."
date: 2026-10-21
slug: your-platform-23-features-no-stop-rule
synthesis: true
sources:
  - https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
  - https://i.octopus.com/whitepapers/2026-future-of-platform-engineering.pdf
---

<!-- lead -->
Two surveys landed this fortnight, and the number I keep returning to is 23. That is the most common count of features a platform team now owns, up from 4 a year earlier [2]. In the same two weeks, a Gartner poll of 2,002 chief information officers (CIOs) found that 51% expect artificial intelligence (AI) to raise the total cost of ownership of their technology [1]. Your platform holds 23 features, and almost nobody has written the stop rule that would keep it there.

<!-- tension -->

## The big picture:

I read the two findings together because each one covers the other's blind spot. Gartner weighs the bill. Octopus Deploy watches the workbench. Neither one says what the pair implies.

Building got cheaper at the front. It did not get cheaper at the back. In the Octopus survey, the teams that build their platform features from scratch are also the teams most likely to say they lack a clear plan. Of those builders, 57.9% named that gap, against 16.7% of the teams that buy an underlying tool [2]. That is about 3.5 times the rate.

A gap in plan looks soft until you see what fills it. Features fill it. The most common feature count went from 4 to 23 in twelve months [2]. Each new feature is another thing to patch, wire up, and explain at the next audit.

Buying carries a brake that building lacks. A renewal date forces a review [1]. A paid tool that stops earning its place gets cut. An internal platform has no renewal date, so it only ever grows.

That is why the CIO number reads as an expectation, not a shock. If the build side has no stopping point, the cost keeps arriving. Just 31% of CIOs hold a rule for halting a pilot before production, and 17% hold one for killing a low-value project already live [1]. Firms with those rules are 2.3 and 2.6 times more likely to be the ones that deliver [1].

## By the numbers

- **51% — cost expectation:** share of CIOs who expect AI to raise the total cost of ownership of their technology, from a poll of 2,002 CIOs fielded May to July 2026 [1].
- **31% and 17% — stop rules:** share holding a rule for halting a pilot before production, and for killing a low-value project already live; those firms are 2.3 and 2.6 times more likely to be top performers [1].
- **57.9% vs 16.7% — plan gap:** scratch builders who cite a lack of clear plan as an obstacle, against tool buyers, in a survey of 379 platform teams [2].
- **4 to 23 — feature sprawl:** the most common number of features a platform team is responsible for, 2025 against 2026 [2].

<!-- tactical-insight -->

## What I'd watch:

The live question is not whether a platform team builds, but what still sits beside the build. I have been hunting for teams that keep a retire list, and they are rare.

- **Retire lists beat roadmaps:** a roadmap records what gets added. A retire list records what gets switched off, and when. A modal count of 23 features says most teams keep only the first.
- **Renewal pressure as a feature:** a bought tool arrives with a date on it, and that date forces an argument about value. The teams I watch import that pressure into internal tools, with a set review and a named owner.
- **Kill rules at intake:** Gartner's 17% is the production-side form of the same instrument [1]. An intake form that asks what would make a team stop is a small change with a large effect on the tail.
- **Feature count as a cost line:** the Octopus report finds no link between owning more features and hitting more goals [2]. That gap is where the next budget talk starts.

<!-- nuanced-takeaway -->

## The catch

Three limits matter here, and the first is the source's own interest. Octopus Deploy sells deployment tooling, and its headline call — build less, buy more — favours its own product [2]. My read is that the build-method split and the plan gap still carry weight, because both are reported as data rather than as advice. The framing is not neutral, though.

Second, the link is not a cause. The report notes that building may be less a result of a missing plan than a substitute for one: engineers build things to work out what the problem is [2]. A written plan might not have stopped any of those builds.

Third, buying does not lift the load. Technical complexity is the obstacle most cited by the teams that buy tools — 54.2%, against 26.3% of scratch builders [2]. The work moves from writing code to wiring and tending someone else's. The sample is modest, too: 379 teams over four months, with optional questions, so the smaller cuts are hints rather than a census [2].

<!-- tldr -->

## At a glance

- **The Big Shift:** Two new surveys, one of 2,002 CIOs and one of 379 platform teams, describe the same build-versus-buy call from opposite ends. Most CIOs now expect AI to raise what their technology costs to own, while the teams that build from scratch are the ones most likely to say they have no clear plan.
- **Why It Matters:** AI cut the cost of starting a build and left the cost of owning one alone. A platform with no stop rule has no renewal date, so its features, its patch load, and its upkeep only grow.
- **What I'd watch:** Whether platform teams start to carry the tool that bought tools carry by default — a date on which the thing gets reviewed.
  - **Retire list:** a standing list of features set to be switched off, the one artifact that makes a feature count fall.
  - **Kill rule:** the written test under which a pilot does not ship, which 31% of CIOs hold today.
  - **Feature count as a cost line:** the finding that owning more features does not track with hitting more goals.
- **The Catch:** The build-method finding comes from a vendor of deployment tooling whose call favours buying, the plan gap is a link rather than a cause, and the buyers' own top obstacle is technical complexity — buying moves the work rather than ending it.

## Sources

[1] Gartner, "Gartner Survey Finds Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI" (2026-10-19) — https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
[2] Octopus Deploy, "The Future of Platform Engineering report" (2026-10-01) — https://i.octopus.com/whitepapers/2026-future-of-platform-engineering.pdf
[3] Octopus Deploy, "The Future of Platform Engineering report" announcement (2026-10-01) — https://octopus.com/blog/future-of-platform-engineering
