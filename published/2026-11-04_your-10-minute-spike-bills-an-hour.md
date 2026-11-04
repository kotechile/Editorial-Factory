---
title: "Your 10-Minute Spike Bills an Hour"
vertical: agentic_resilience_failure
kind: news
persona: infra_engineer
one_big_thing: "A short traffic surge can leave an agent-serving engine slower at the same load it served an hour earlier, because the sessions the surge created keep each other alive through cache eviction and recompute — so recovery has to be judged by the state left behind, and the move that ended it in the published run was retiring the burst's sessions, not adding capacity."
date: 2026-11-04
slug: your-10-minute-spike-bills-an-hour
meta_title: "Your 10-Minute Spike Bills an Hour"
meta_description: "A ten-minute surge left an agent-serving engine at a fifth of its throughput an hour later, at a request rate it had served all morning."
image_alt: "Torn paper strips form a loop on a scratched steel workbench, one yellow strip lifting at the break."
image_caption: "A paper loop of session tokens on a workbench, the break marked by one yellow strip."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
image_path: "context/assets/illustrations/your-10-minute-spike-bills-an-hour/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
---

<!-- lead -->

At 09:55 an on-call engineer watches a 10-minute traffic spike end, and the agent service keeps getting worse. Arrivals are back at the rate the engine had served all morning, yet the wait for the first token has gone from about 0.2 seconds to 60. A group at Nanyang Technological University measured that on a real serving engine, and it bills an hour. A burst at twice the base rate cut the work that actually finishes — what the paper calls goodput — by roughly 88% for the sessions that arrived after it [1]. Processor load, queue length, and memory use all looked fine the whole way in, so nothing on that dashboard warned of it [1].

<!-- tension -->

## The loop that outlives its trigger

An agent session is not one call. It is a chain of turns that share a prompt and wait on tools, and it ends only after its last turn [1]. Every turn resends most of the earlier text. In the traces this paper replays, the median prompt holds 25.6K tokens, and 98.2% of them appeared in the previous call [1]. Engines lean on a prefix cache — a saved copy of earlier work that a returning call reuses instead of reading its whole history again. That cache is what makes long sessions cheap at all [1].

Cheap, and fragile, because the live sessions have a combined size. The paper calls it the working set: the total context of every live session, including the ones parked on a tool [1]. When it reaches about twice the cache capacity, the cache drops old entries before their own sessions come back. A returning turn then rebuilds its prompt from the start, which is work it had already paid for once [1].

A miss here is not a slow read; it is the same reading done twice. That rebuild takes time, the slower turn holds its session open longer, and the longer session adds more context to the pile. I read that loop as the whole finding: the engine's chance of recovering depends on a crowd it is still growing.

The experiment separates the two cases. On the same arrival stream, a surge a third above base recovered inside twenty minutes [1]. A surge of double did not. The wait for the first token reached about a minute, and the share of a returning prompt the cache could serve fell from 0.95 to 0.27 [1]. Sessions arriving in the following hour finished at 17 an hour against 138 [1]. The difference was whether the working set reached the cliff, at roughly twice the cache [1].

The test that shows cause is the one where the authors killed the burst's own sessions. By minute 25 both runs hold about 110 live sessions, 65 of them from the burst, with a first token near 9 seconds [1]. Killing them restored service in two minutes [1]. Left to finish, they stayed active another 25 minutes. Meanwhile the base population climbed to 1.7 times its normal size at minute 50 and 2.4 times at minute 90 [1]. At the same arrival rate the engine either stays healthy or keeps sliding, on its earlier exposure alone [1].

## By the numbers

- **17 an hour against 138 — sessions finished, after the burst:** the same arrivals that completed 138 sessions an hour without a surge completed 17 in the hour after one [1].
- **0.95 to 0.27 — prefix hit rate:** the share of a returning call's prompt the cache could serve, before and after the working set crossed the cliff [1].
- **18 up, 20 down — tasks one deployed change flipped:** one task in six changed outcome beyond the noise floor, which averages to nothing and is what no undo repairs [2].

<!-- tactical-insight -->

## What the operators are already doing

The upstream fix is being built in public, and it measures the same thing. An open issue on the llm-d router proposes adding a session-level admission gate — a check at the door that limits how many sessions run at once. Its author ran both arms on one vLLM pod replaying 338 real coding-agent sessions: the prefix hit rate went from near zero to 0.685 and the first token from 52.7 seconds to 3.0 [4]. That pod was already overloaded rather than freshly surged, and the fix lands on the same lever. The gate trades a little waiting at the door for a lot less redone work inside.

Basin, the scheduler the paper builds, is that idea in four parts. It gives each session a fixed priority, reserves against an admission budget sized to that session's expected peak context, lends cache from idle decode memory, and sheds excess demand [1]. On four H200 deployments it beat Continuum by 1.20 to 1.70 times and HiCache alone by 2.35 to 3.59 times. Switched on after an engine was already stuck, it reached 301.1 sessions an hour where Continuum reached 167.8 [1].

The closest production timeline is duller and worse. Zendesk's AI Agents incident ran from 18:00 on 16 October to 08:56 on 21 October in coordinated universal time. Its engineers paused the rebuild of old messages "after it caused delays in another part of the service" [5]. What held it open was not the trigger but the repair work, the same shape as the loop above. I keep circling that sentence, because a repair job that slows the service is competing for the thing it is trying to restore.

The unit to cap is the session, not the call. [Your Queue Caps the Wrong Unit](/your-192-sessions-stall-the-model-not-the-tools/) did that arithmetic two days ago: at 192 sessions at once the model stalls while the tools barely slow. This piece is the other half of that ledger. Capacity tells you where the cliff is; it does not tell you whether the engine on the far side of it can climb back.

<!-- nuanced-takeaway -->

## The catch

The scope is one deployment. Every hardware experiment here runs one model, Qwen3.6-35B-A3B, on SGLang across H100 and H200 boxes, and the map that flags 17 of 36 deployments comes from a simulation [1]. The direction travels; the coefficients do not. None of that is a reason to distrust the findings, only a reason to reproduce them on your own traces before trusting a threshold.

The second measurement has its own limits. The study tested prompt edits only, on two test suites rather than in production. It ends with the finding that matters to anyone holding an undo button: restoring a stored copy returned behaviour to normal at 0.000, while an undo rebuilt from scratch left it clearly different at −0.16 [2]. The admitted changes altered one task in six beyond noise, 18 up and 20 down, so the average read as nothing while the reach was real [2].

The carry is not only a serving problem. A second study this week found memory systems revising a contradicted fact while the beliefs and plans derived from it stayed accepted. A method that tracks what depends on what gained 6.9 points of impact score over a baseline one level deep, and 26.0 at three or more [3]. That is the same sentence in a different room: the correction is not the recovery.

The part I keep returning to is that both describe the same mistake from different ends, and neither one lets you skip measuring your own population.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "68 Loops Your Runtime Never Stopped" -> /agent-loop-bound-not-a-budget/ [same site (aichieve.net); same category; topical overlap: agent] Link "68 Loops Your Runtime Never Stopped" in the section where the article touches agent. -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: agent] Link "Agent Memory Poisoning" in the section where the article touches agent. -->
<!-- internal-link hint: "Agent Timeouts: Pick 0.1%, Not a Round Number" -> /agent-timeout-false-alarm-budget/ [same site (aichieve.net); same category; topical overlap: agent] Link "Agent Timeouts: Pick 0.1%, Not a Round Number" in the section where the article touches agent. -->
## Related reading

- [68 Loops Your Runtime Never Stopped](/agent-loop-bound-not-a-budget/) — more on Autonomous & Agentic Workflows
- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Agent Timeouts: Pick 0.1%, Not a Round Number](/agent-timeout-false-alarm-budget/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The shift:** A brief surge can leave agent serving degraded at a load the engine handled before.
- **The number:** Sessions finishing in the hour after a 10-minute burst fell to 17 an hour from 138.
- **The risk:** More cache moves the cliff outward; it does not stop a finite surge from crossing it.

## Sources

[1] C. Lu, B. Zhou, Y. Lin and D. Ustiugov, "When Cache Pressure Becomes a Trap: Metastability in Agent Serving," Nanyang Technological University and Harvard University, arXiv:2611.02543, submitted 2026-11-02 — https://arxiv.org/abs/2611.02543

[2] "Recoverability and Verifier Strength: Two Measured Preconditions for Unattended Agent Self-Improvement," arXiv:2610.27465, submitted 2026-10-20 — https://arxiv.org/abs/2610.27465

[3] "A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory," arXiv:2611.02912, submitted 2026-11-02 — https://arxiv.org/abs/2611.02912

[4] llm-d project, "[Agentic] Session level admission control: add a ThunderAgent plugin," llm-d-router issue 2964, opened 2026-09-22 — https://github.com/llm-d/llm-d-router/issues/2964

[5] Zendesk, "Service Incident — October 18, 2026 — AI Agents | Multiple Pods — Agent and customer messages not showing in AI Agents conversations," resolution posted 2026-10-21 — https://support.zendesk.com/hc/en-us/articles/11421427980826-Service-Incident-October-18-2026-AI-Agents-Multiple-Pods-Agent-and-customer-messages-not-showing-in-AI-Agents-conversations
