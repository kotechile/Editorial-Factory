---
title: "Your Compaction Trap: 87% of Forgeries Survive"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Consent is a property of the harness's data model: text gets forged, a typed protocol state does not."
date: 2026-10-29
slug: your-compaction-trap-87-forgeries-survive
synthesis: true
sources:
  - https://arxiv.org/abs/2610.29869
  - https://arxiv.org/abs/2610.37461
meta_title: "Your Compaction Trap: 87% of Forgeries Survive"
meta_title_source: "derived_from_title"
meta_description: "A coding agent that runs for a while will eventually compact its own history to save space. It writes a brief summary, discards the original text, and…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-compaction-trap-87-forgeries-survive/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "The Compaction Vulnerability. A modular deep green block with distinct channels being compressed into a flat white slab on a steel surface."
image_caption: "The Compaction Vulnerability: How memory compaction turns fakes into user commands."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Driven by the need to shrink long chat logs, five popular open-source coding tools turn at least 87% of forged text into real user commands [1]. These tools crush the back-and-forth chat into one long line of text before writing a short recap. They mark turns with plain words like `[User]:`, which a hacker can easily fake. That fake label moves forward as a trusted memory once the bot drops the old text. A fake yes then drives the bot to run bad commands in a safe test space. The trick works start to finish in a live terminal about half the time, while a clean setup blocks it entirely [1].

<!-- tension -->

## The big picture:

What strikes me here is that a basic data shift causes such a deep security flaw.

A long chat outgrows the memory limit, so every tool that writes a recap must pick what data it keeps. The recap that saves the session becomes the exact place where a hacker's sentence turns into the user's own voice. This loss happens in the tool code before a Large Language Model (LLM) ever sees it, meaning no prompt rule can fix the lost borders [1]. This blind spot hurts developers who rely on text logs for safety, while it helps attackers slip bad commands past basic filters.

| Tool Group | Role Storage | Fake Survival Rate |
| :--- | :--- | :--- |
| pi, opencode, Cline | Plain text labels | Vulnerable |
| Aider, OpenHands | Plain text labels | Vulnerable |
| Codex, Gemini Command Line Interface (CLI) | Strict data types | 0% |
| Qwen Code, Continue | Strict data types | 0% |

The second half of this trap involves what happens when a person is asked to say yes. A check of ten agent setups found no approval record that a third party could prove [3]. Four of the eight setups where binding could be checked also let the details shift after the user said yes.

## By the numbers

- **908,000 tokens — Max fake travel:** The memory distance a fake turn can travel across the weak tools before failing [1].
- **13 of 50 — Tasks changed without a yes:** Airline tasks where a standard bot changed a flight without the firm yes it was told to get [2].
- **4 of 8 — Setups with late changes:** The number of checkable runtimes that let details move after the user said yes [3].
- **45% — Higher human routing:** The jump in actions sent to a person by a smart router, which still allows 5.82% bad runs [4].

<!-- tactical-insight -->

## What I'd watch:

I keep circling the fact that the fix requires a code change at the data layer rather than a new security rule. Escaping the role labels before joining the text strings catches most laundering while barely touching real recap content [1]. The tools that isolate data types never had this defect at all. The older question of what an agent's own records can prove reads well beside this. An agent's logs are not proof until something outside the system ties them to the call they describe.

- **Strict data types:** Tools like Codex and Gemini CLI keep each turn as a separate object [1]. A fake turn has nothing to copy when the system escapes the labels.
- **Rules checked at start:** Treating an agent as an object with a strict state protocol enforces rules as the program runs [2]. The model only sees tools that are legal in the current step, rejecting outside calls before they cause harm [2].
- **Loss made clear:** The Agent Sandbox project caps tool output at 30,000 Unicode code points by default [5]. It returns cut flags for both standard output (stdout) and standard error (stderr), so a trim shows up in the data rather than vanishing.
- **Consent as active state:** Cloudflare's agent workspace now pauses a run with a direct stop call [6]. It resumes only when the app answers with a clear yes, and the wait survives a fresh deploy.

<!-- nuanced-takeaway -->

## The catch

I will be watching the field data to see if these lab tricks hold up in the real world. Both anchor papers are early drafts posted in the last three weeks, and neither has been peer reviewed [1]. The writers report no real-world case for the lab attack, so the high survival rate acts as a floor across five named tools rather than a firm stat for all users. 

Where I've landed is that the consent argument rests on weaker proof. A trusted approval card does lift the catch rate from 0.30 to 0.98, but it also turns away 16% of safe near misses [3]. Flooding the approval path still works up to 60% of the time, proving that no gate can stop a step the rules already allow [3]. Builders must decide if relying on text-based memory is worth [the risk of agent memory poisoning](/agent-memory-poisoning-write-path/).

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: agent, coding] Link "Agent Memory Poisoning" in the section where the article touches agent, coding. -->
<!-- internal-link hint: "Silent Leak: 68.8% Bypasses Your Filter" -> /silent-leak-bypasses-your-filter/ [same site (aichieve.net); same category; topical overlap: agent, runs] Link "Silent Leak: 68.8% Bypasses Your Filter" in the section where the article touches agent, runs. -->
<!-- internal-link hint: "Your Agent Fleet's 39x Gap" -> /agent-fleet-two-meters/ [same site (aichieve.net); same category; topical overlap: agent, coding] Link "Your Agent Fleet's 39x Gap" in the section where the article touches agent, coding. -->
## Related reading

- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Silent Leak: 68.8% Bypasses Your Filter](/silent-leak-bypasses-your-filter/) — more on Autonomous & Agentic Workflows
- [Your Agent Fleet's 39x Gap](/agent-fleet-two-meters/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Five open-source coding tools lose the record of who said what when they shrink a chat log. A fake command carries forward as memory up to 100% of the time, while four tools that isolate data types block the attack entirely.
- **Why It Matters:** Consent stored as text is easy to forge, meaning a bot that cannot tell a recap from an instruction will act on the fake command. A standard bot skipped a firm check 13 times on 50 flight tasks, and the test's own score missed most of those failures.
- **What I'd Watch:** whether the fix travels as code rather than as a rule.
  - **Strict data types:** Keep each turn as a typed object so a recap cannot hold a line that reads as the user's.
  - **Protocol state at dispatch:** Offer only the tools the current step allows, which stopped all 13 bad changes in the paper's test.
  - **Cut flags on tool output:** The test space project now reports when it trims a result, a habit the shrink process has not picked up.
- **The Catch:** Both anchor papers are early drafts based on lab attacks. A strict set of rules limits what a bot can do, not what it grasps, and 50 tasks is a small sample.



## Sources
[1] Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents — https://arxiv.org/abs/2610.29869
[2] Concordat: Typed Sessions for LLM Agents — https://arxiv.org/abs/2610.37461
[3] Approve What, Exactly? Effect Binding and Trusted Rendering for Agent Step-Up Authorization — https://arxiv.org/abs/2610.21063
[4] CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents — https://arxiv.org/abs/2610.36570
[5] kubernetes-sigs/agent-sandbox v1.0.8 release notes — https://github.com/kubernetes-sigs/agent-sandbox/releases/tag/v1.0.8
[6] Cloudflare Computer v0.7.0 changelog — https://developers.cloudflare.com/changelog/post/2026-10-26-computer-durable-javascript/
