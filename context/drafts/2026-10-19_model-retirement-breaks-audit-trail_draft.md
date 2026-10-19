---
title: "2-Week Notice Breaks Your Audit Trail"
vertical: enterprise_ai_governance
persona: enterprise_cai
one_big_thing: "A retired model version breaks an audit trail that pins it, and notice runs from 2 weeks to 12 months, so pin policy and re-validation capacity are one decision."
date: 2026-10-19
slug: model-retirement-breaks-audit-trail
archetype: evergreen
evergreen: true
---

<!-- lead -->
The shortest retirement notice on the market is 2 weeks, and it breaks your audit trail. The model version your record names has an expiry date, and the vendor picks it. At OpenAI a preview model can be pulled in 2 weeks [1]. At Anthropic the floor is 60 days [2]. On Google Cloud a model is listed as good for 12 months [3]. On Amazon Bedrock one notice window is 45 days [4]. That gap is the problem. The evidence you built for a regulator has a shelf life you did not set.

<!-- tension -->

## The big picture:

Pinning a version is how a governed agent becomes reviewable. The record names the model, the prompts and the tool calls. A reviewer can re-run the decision months later. That works while the version still exists.

My read is that the retirement notice is the weak link. Most teams treat it as a buying event. It is an evidence event, and the published numbers barely overlap.

OpenAI sets floors by tier. Generally available (GA) models get 6 months. Specialized variants get 3 months. Preview models may be retired in 2 weeks [1].

Anthropic promises 60 days for public models. It also says that partner platforms set their own dates. The same model can carry two schedules, based on where you bought it [2].

Google Cloud lists models as available for 12 months after release. Each entry carries its own retirement date. A date may move later, but not earlier [3].

Bedrock uses three states. Its Legacy period is the notice window before a model reaches end of life (EOL). That window comes in two lengths: 6 months and 45 days [4].

The pattern is plain. Firms get a fixed number of days to re-test an agent. A vendor sets that number, and the buyer did not negotiate it.

## By the numbers

- **2 weeks — Shortest published notice:** OpenAI says preview models "may be retired with much shorter notice, such as 2 weeks". That sits under 6 months for generally available models and 3 months for specialized variants [1]. An agent pinned to a preview tier holds the shortest clock on the market.

- **60 days — Anthropic floor:** Anthropic tells customers with active deployments at least 60 days before a public model retires. It also warns that Amazon Bedrock and Google Cloud set their own dates, so the state and the deadline can differ by platform [2].

- **12 months — Google Cloud floor:** Google lists models as available for at least 12 months after release. It prints a retirement date for each one. Timelines may stretch, but they will not be pulled forward past the printed date [3].

- **15 days — Bedrock inactivity rule:** A model in its Legacy window cannot be taken up by new customers. Existing customers may lose access after 15 days of idle use, before the printed EOL date [4]. The two Legacy windows run 6 months and 45 days.

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this issue are not arguing about notice lengths. They are moving the proof away from the model itself.

- **Hash the version, not the label:** A record that says "model X, version 2026-09" is worth little on its own. The founder view at this desk is that the flight recorder holds model weights and version, temperature, prompt hashes and tool arguments. That is what makes a replay a replay, not a re-roll. A retirement kills the served endpoint. Your hash is what a reviewer can still check [1].

- **Price the clock as a control:** A team pinned to a 12-month model has a slower review cycle than a team on a 45-day Legacy clock [3][4]. The number that matters is not the longest notice on offer. It is the shortest one across every channel an agent runs on, and a cloud reseller may not match the developer's own schedule [2].

- **Watch the model list, not the inbox:** OpenAI posts a per-model shutdown date through its models endpoint [1]. A governance team can read a retirement from a feed instead of waiting for an email.

- **Treat a swap as a re-test:** Anthropic tells teams to test the replacement on the task before the old model goes. A retired model rejects requests outright [2]. For an agent under review, that test is the same work as the first sign-off: same prompts, same expected output, same limit.

<!-- nuanced-takeaway -->

## The catch

None of these numbers is a promise. OpenAI's floors apply unless safety or compliance needs a faster cut [1]. Google commits that a retirement date will not move earlier than the one printed, and says nothing about a safety exception either way [3]. Bedrock says its dates are its own, and may differ from what the developer publishes. One model can hold several end dates at once [4].

My read is that pinning buys proof and costs freshness. A pinned agent misses the vendor's safety patches and quality fixes. Each pin is also a future migration you booked for yourself.

The other path carries a quieter cost. Always-on-latest keeps the agent current, and it destroys the trail. The version that made last quarter's decision is gone when someone asks about it.

There is a channel trap too. Buying the same model through a second platform can change both the clock and the state. A register that records the model maker, but not the platform that served it, has logged a fact that binds nobody [2][4].

<!-- tldr -->

## At a glance

- **The Big Shift:** Vendors now retire model versions on published schedules. Notice runs from 2 weeks to 12 months, based on the vendor and the tier. A firm that pins a version for audit replay is holding an asset with a vendor-set expiry date [1][2][3][4].

- **Why It Matters:** A record that names a version stops being replayable once that version is gone. The risk is not the cost of the move. It is finding out at audit time that the decision you defend cannot be rebuilt.

- **What I'd Watch:** I am watching how teams split the pin call from the move call, and whether the notice clock enters the control register at all.
  - **Version hashing:** Keep a fingerprint of each model version an agent ran, so the record outlives the endpoint.
  - **Channel-aware registers:** Log the platform that served the model, since that platform owns the date.
  - **Re-test budget:** Hold test capacity sized to the shortest notice in the estate, not the longest.

- **The Fine Print:** Notice floors are vendor claims with safety carve-outs, not service guarantees. Pinning also freezes an agent on an older model, so the control that saves the trail is the one that delays every fix.

## Sources

[1] OpenAI, "Deprecations" — model deprecation notice periods and the per-model shutdown date. https://platform.openai.com/docs/deprecations
[2] Anthropic, "Model deprecations" — 60-day notice floor, lifecycle states, partner-platform schedules. https://docs.claude.com/en/docs/about-claude/model-deprecations
[3] Google Cloud, "Model versions" (Vertex AI) — availability of at least 12 months after release, per-model retirement dates, no earlier dates. https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions
[4] Amazon Web Services, "Model lifecycle" (Amazon Bedrock) — Active, Legacy and end-of-life states, 6-month and 45-day Legacy periods, 15-day inactivity rule. https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html
