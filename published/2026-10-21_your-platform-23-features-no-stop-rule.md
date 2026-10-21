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
meta_title: "Your Platform: 23 Features, No Stop Rule"
meta_title_source: "derived_from_title"
meta_description: "The most common number of features a platform team now owns is 23, up from four a year earlier. In the same fortnight, 51% of chief information officers…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-platform-23-features-no-stop-rule/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Internal Platform Bloat. A split layout showing an endlessly expanding rack of metal modules next to a single, locked module"
image_caption: "Internal Platform Bloat: Why custom platforms grow endlessly without stop rules."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The most common number of features a platform team now owns is 23, up from four a year earlier [2]. In the same fortnight, 51% of chief information officers (CIOs) told Gartner they expect artificial intelligence (AI) to raise the total cost of ownership of their technology [1]. Your platform holds 23 features, and almost nobody has written the stop rule that says when to stop.

<!-- tension -->

## The big picture:

The part I keep circling is how these two reports cover each other's blind spots. Gartner weighs the bill. Octopus Deploy watches the workbench.

Building got cheaper at the start. It did not get cheaper at the end.

Teams that build platform features from scratch are the most likely to report no clear plan. Of those custom builders, 57.9% named that gap as an obstacle, against 16.7% of the teams that buy an underlying tool [2]. That is about 3.5 times the rate.

A missing plan looks soft until features fill the space. The most common feature count went from 4 to 23 in twelve months [2]. Each new feature is another thing to patch, wire up, and explain at the next audit.

Buying carries a brake that building lacks. A renewal date forces a review [1]. A paid tool that stops earning its place gets cut. An internal platform never comes up for renewal, so it only grows.

That is why the CIO figures read as an expectation rather than a shock. Only 13% of those CIOs say AI has delivered significant value so far, and 51% expect it to raise what their technology costs to own [1].

Just 31% hold a rule to halt a pilot before production, and 17% hold one to kill a low-value project already live [1]. Firms with those rules are 2.3 and 2.6 times more likely to be the ones that deliver [1].

## By the numbers

- **51% — cost expectation:** share of CIOs who expect AI to raise the total cost of ownership of their technology, from a poll of 2,002 CIOs fielded May to July 2026 [1].
- **31% and 17% — stop rules:** share holding a rule for halting a pilot before production, and for killing a low-value project already live; those firms are 2.3 and 2.6 times more likely to be top performers [1].
- **57.9% vs 16.7% — plan gap:** custom builders who cite a lack of clear plan as an obstacle, against tool buyers, in a survey of 379 platform teams [2].
- **4 to 23 — feature sprawl:** the most common number of features a platform team is responsible for, 2025 against 2026 [2].

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your Platform: 23 Features, No Stop Rule</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">cost expectation</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="153" height="18" rx="4" fill="#818cf8"/>
  <text x="403" y="84" fill="#f1f5f9" font-size="13" font-weight="600">51%</text>
  <text x="457" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">stop rules</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="93" height="18" rx="4" fill="#818cf8"/>
  <text x="343" y="132" fill="#f1f5f9" font-size="13" font-weight="600">31%</text>
  <text x="397" y="132" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 3 -->
  <text x="20" y="180" fill="#e2e8f0" font-size="13" font-weight="500">plan gap</text>
  <rect x="240" y="166" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="166" width="173" height="18" rx="4" fill="#818cf8"/>
  <text x="423" y="180" fill="#f1f5f9" font-size="13" font-weight="600">57.9%</text>
  <text x="477" y="180" fill="#64748b" font-size="11">([2])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch:

I have been hunting for teams that keep a retire list, and they are rare. The live question is not whether a team builds, but what still sits beside the build.

- **Retire lists beat roadmaps:** a roadmap records what gets added. A retire list records what gets switched off, and when.
- **Renewal pressure as a feature:** a bought tool arrives with a date on it, and that date forces an argument about value. The teams I watch import that pressure into internal tools, with a set review and a named owner.
- **Kill rules at intake:** Gartner's 17% is the production-side form of the same instrument [1]. An intake form that asks what would make a team stop is a small change with a large effect on the tail.
- **Mandatory use as the other lever:** teams required to use a platform hit most of their goals at 62.2%, against roughly 27.5% where use was optional [3].
- **Feature count as a cost line:** the Octopus report finds no link between owning more features and hitting more goals [2]. That gap is where the next budget talk starts.

<!-- nuanced-takeaway -->

## The catch

Three limits matter here, and the first is the source's own interest. Octopus Deploy sells deployment tooling, and its headline call — build less, buy more — favours its own product [2]. My read is that the build-method split and the plan gap still carry weight, because both are reported as data rather than as advice. The framing is not neutral, though.

Second, the link is not a cause. The report notes that building may be less a result of a missing plan than a substitute for one: engineers build things to work out what the problem is [2]. A written plan might not have stopped any of those builds.

Third, buying does not lift the load. Technical complexity is the obstacle most cited by the teams that buy tools — 54.2%, against 26.3% of scratch builders [2]. The work moves from writing code to wiring and tending someone else's.

The sample is modest as well: 379 teams over four months, with optional questions, so the smaller cuts are hints rather than a census [2].

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Multi Agent Orchestration" -> /multi-agent-orchestration-building-the-one-person-enterprise/ [same site (aichieve.net); same category; topical overlap: team] Link "Multi Agent Orchestration" in the section where the article touches team. -->
<!-- internal-link hint: "Where the Prompt Breaks Decides the AI Bill" -> /cache-boundary-decides-input-bill/ [same site (aichieve.net); same category; topical overlap: team] Link "Where the Prompt Breaks Decides the AI Bill" in the section where the article touches team. -->
<!-- internal-link hint: "Your 100-Case Eval" -> /100-case-eval-925-coverage/ [same site (aichieve.net); same category; topical overlap: number] Link "Your 100-Case Eval" in the section where the article touches number. -->
## Related reading

- [Multi Agent Orchestration](/multi-agent-orchestration-building-the-one-person-enterprise/)
- [Where the Prompt Breaks Decides the AI Bill](/cache-boundary-decides-input-bill/)
- [Your 100-Case Eval](/100-case-eval-925-coverage/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Two new surveys, one of 2,002 CIOs and one of 379 platform teams, describe the same build-versus-buy call from opposite ends. The most common feature count on a platform team rose from 4 to 23 in a year, while most CIOs now expect AI to raise what their technology costs to own.
- **Why It Matters:** AI cut the cost of starting a build and left the cost of owning one alone. A platform with no stop rule has no renewal date, so its features, its patch load, and its upkeep only grow.
- **What I'd watch:** Whether platform teams start to carry the tool that bought tools carry by default — a date on which the thing gets reviewed.
  - **Retire list:** a standing list of features set to be switched off, the one artifact that makes a feature count fall.
  - **Kill rule:** the written test under which a pilot does not ship, which 31% of CIOs hold today.
  - **Mandatory use:** a platform people are told to use reached its goals at 62.2%, against 27.5% where use was optional.
- **The Catch:** The build-method finding comes from a vendor of deployment tooling whose call favours buying, the plan gap is a link rather than a cause, and the buyers' own top obstacle is technical complexity — buying moves the work rather than ending it.

## Sources

[1] Gartner, "Gartner Survey Finds Only 13% of CIOs Say Their Enterprise Has Realized Significant or Transformational Value from AI" (2026-10-19) — https://www.gartner.com/en/newsroom/press-releases/2026-10-19-gartner-survey-finds-only-13-percent-of-cios-say-their-enterprise-has-realized-significant-or-transformational-value-from-ai
[2] Octopus Deploy, "The Future of Platform Engineering report" (2026-10-01) — https://i.octopus.com/whitepapers/2026-future-of-platform-engineering.pdf
[3] Octopus Deploy, "The Future of Platform Engineering report" announcement (2026-10-01) — https://octopus.com/blog/future-of-platform-engineering
