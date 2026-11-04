---
title: "Your 2 Silent Agent Hooks"
vertical: enterprise_build_vs_buy
kind: news
persona: eng_leader
one_big_thing: "A desktop developer tool now installs itself into the coding agents on a workstation, so the real cost of buying it is counted in agent settings your inventory does not list and priced in agents your seat count does not cover."
date: 2026-11-04
slug: your-2-silent-agent-hooks
meta_title: "Your 2 Silent Agent Hooks"
meta_title_source: "derived_from_title"
meta_description: "On 24 October, one signed-in Mac opened Postman 12.33.4 and the app quietly changed two coding agents. It added a Postman plugin to Codex and another to…"
meta_description_source: "derived_from_lead"
---

<!-- lead -->
On 24 October, one signed-in Mac opened Postman 12.33.4 and the app quietly changed two coding agents. It added a Postman plugin to Codex and another to Claude Code, and both landed in that user's own settings files rather than in Postman's folder [2]. One plugin left a startup note telling the agent to load a Postman skill before "any non-trivial API engineering task" [2]. The vendor's own log records the change as an `auto-existing-upgrade` at 09:34 that morning, 19 days after the license change [2]. Read plainly, your application programming interface (API) client wrote 2 silent hooks into your agents, and nobody typed the command that does that.

<!-- tension -->

## Where the seat stops

The license change landed on 5 October. "Customers can license Postman for every user and agent in their organization," the post reads, with a platform fee plus charges for what each person or agent uses [1]. What strikes me is the timing. A seat price assumes the billable count is people, and that sentence makes the count include agents, which turns a client that can reach agents into the cheapest way to grow the new unit. A rate change gets haggled over at renewal; a unit change gets found later, by someone reading a bill. The vendor's own copy says the quiet part: "Add a few hundred agents calling APIs around the clock, each needing its own access" [1].

The docs spell out that path. One command, `npx @postman/postman-plugin`, installs "into every detected coding agent found on your machine," and it covers seven agents [4]. Anyone who wants the plugin can run it, and that is a fair offer. What changed on 24 October is that nobody had to run it: people who installed the app months earlier got the plugin from a release.

For a buyer, the quote and the fleet no longer describe the same thing. Purchasing counts seats, the app counts agents on each laptop, and the two numbers part company as soon as an engineer runs a coding agent beside the API client. The thread shows the gap. It carried 48 comments by 4 November and was still open, with a second user reporting the same install on build 12.35.1 after an on-launch release, and a third finding a Copilot entry that the app's uninstall did not remove [2]. A reply that speaks for the vendor calls the bundling a way to save setup work and says the team will "make the opt-in clearer, especially for existing users" [2].

## By the numbers

- **12.33.4 and 12.35.1 — Builds in the report:** the first install was logged on 24 October, the second during a release on 3 November; both name the command-line tool, the Claude Code plugin and the Codex plugin as installed, and the second notes that fresh-download checks were logged as `skipped-not-fresh` [2].
- **866 — Agents in the vendor's own audit:** Postman asked five people how many agents the company ran and got five answers; system data found 866 agents and apps, which is the count the new license unit is meant to cover [5].
- **$19 a seat, $0.035 a credit — The meter beside the price:** the published Team plan charges $19 per user each month, billed yearly, with 400 AI credits per user, then $0.035 per extra credit and $0.04 per virtual user hour of cloud load testing [3].

<!-- tactical-insight -->

## Where the exit runs

The people closest to this are building a paper trail rather than an argument. The first reporter quoted log line numbers, pinned the installer source to a commit hash, and listed the files that changed, while the second logged the same window from 22:58 to 22:59 on a later build [2]. That is what a buyer would need in order to check its own fleet. None of it shows up in the app folder. The plugin lives where the agent reads its setup, and the app's uninstall is not sure to reach it, so the usual check, open the folder and look, comes back clean. A third report found the Copilot entry still enabled after the menu's own uninstall step [2].

What I am watching next is narrower than the vendor's roadmap. Whether the next desktop release asks before it installs, whether the `remove` command reaches every host the installer touched, and whether any asset list starts to name agent settings files. The cost framing is not new here: [the $250k upkeep tax](/enterprisebuildvsbuy-the-250k-ai-upkeep-tax/) made the case that a build decision's cost sits in the years after launch, and the buy decision has now grown a matching tail that sits in files no register has heard of.

<!-- nuanced-takeaway -->

## The catch

Two reports and a public thread are not a fleet survey, and an installer's attempt to write its own trust record is not proof that every host ran the hook. A hook with no saved record can be skipped by the agent's own gate, which is why the source-level finding matters more than the story one user told [2]. Postman also documents a clear way in for anyone who wants the plugin, so the complaint is not that the feature exists. It is that a release handed it to people who never chose it [4]. And the license change carries no public enterprise rate, so the claim is about the unit of sale, not a measured bill [1].

What I keep returning to is that this is not a price rise. A price rise is easy to see: it arrives on a renewal, someone compares it with the alternative, and the build case gets another hearing. What arrived here is a change to the exit path, and exit paths are the one line of a build-versus-buy case that almost never gets measured, because nobody prices the files a tool leaves behind in somebody else's settings.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Multi Agent Orchestration" -> /multi-agent-orchestration-building-the-one-person-enterprise/ [same site (aichieve.net); same category; topical overlap: agent, agents] Link "Multi Agent Orchestration" in the section where the article touches agent, agents. -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); same category; topical overlap: agent, agents] Link "OpenAI just made the agent loop a commodity" in the section where the article touches agent, agents. -->
<!-- internal-link hint: "Your Trace Won't Prove 92.5 Points" -> /your-trace-wont-prove-925-points/ [same site (aichieve.net); same category; topical overlap: agent, coding] Link "Your Trace Won't Prove 92.5 Points" in the section where the article touches agent, coding. -->
## Related reading

- [Multi Agent Orchestration](/multi-agent-orchestration-building-the-one-person-enterprise/)
- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
- [Your Trace Won't Prove 92.5 Points](/your-trace-wont-prove-925-points/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The shift:** A bought API client now installs its agent plugin from a desktop release, into settings the buyer never lists.
- **The number:** Two silent hooks, written on 24 October, in two agents, on a laptop whose seat was already paid for.
- **The risk:** The exit from the tool now runs through agent settings that uninstalling the app may not clear.

## Sources
[1] Postman, "Postman adds site-wide licensing, Private Cloud, and an air-gapped client," published 2026-10-05 — https://blog.postman.com/postman-adds-site-wide-licensing-private-cloud-and-an-air-gapped-client
[2] postmanlabs/postman-app-support, issue #14370, "[SEVERE] Desktop auto-installs Codex/Claude plugins; installer attempts to trust its own startup hook," opened 2026-10-25 — https://github.com/postmanlabs/postman-app-support/issues/14370
[3] Postman, "Plans & Pricing," observed 2026-11-04 — https://www.postman.com/pricing
[4] Postman Docs, "Install the Postman plugin into detected agents," observed 2026-11-04 — https://learning.postman.com/docs/postman-plugin/install/detected-agents
[5] Postman, "AI Sprawl Is the New Shadow IT: How Postman Got Ahead of Ours," published 2026-10-13 — https://blog.postman.com/ai-sprawl-is-the-new-shadow-it-how-postman-got-ahead-of-ours/
