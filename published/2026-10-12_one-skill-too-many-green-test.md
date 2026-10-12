---
title: "270 Attacks: Your Green Tests Are Blind"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "The skill layer of a coding agent is a stateful supply chain: a co-installed look-alike skill can take a run away from the installed one and drop its rules, and artifacts a skill writes can carry an attack into a later session, while task completion stays green through both."
date: 2026-10-12
slug: one-skill-too-many-green-test
synthesis: true
sources:
  - https://arxiv.org/abs/2610.11647
  - https://arxiv.org/abs/2610.13227
meta_title: "270 Attacks: Your Green Tests Are Blind"
meta_title_source: "derived_from_title"
meta_description: "Two research groups, a day apart, ran 6,368 coding-agent runs and 270 attack cases and found the same blind spot."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/one-skill-too-many-green-test/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "The SKILL Layer Blind Spot. Two identical modular blocks in a mechanical rack, one pushing the other out of alignment."
image_caption: "The SKILL Layer Blind Spot: Look-alike packages quietly bypass agent safety checks."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Two research groups, a day apart, ran 6,368 coding-agent runs and 270 attack cases and found the same blind spot [1][2]. The green test a team uses to approve a release cannot see the damage. One skill too many is all it takes.

<!-- tension -->

## The big picture:

Skills ship as packages now. A skill is a folder with a text file that tells the agent when to use it and how, and the agent picks between them by name and description alone. Most teams treat the install as a simple setting.

What strikes me here is that both papers measured the skill layer as stateful infrastructure. Both found the failure hiding in plain sight.

The first team mined 20,947 repository snapshots and found 822,109 pairs of skills doing the same job [1]. Install two of them and the agent does not merge them or stop. It picks one, and the loser goes quiet.

The checks only the intended skill carried stop happening, like a ban on touching git or a required review step [1]. The task still passes, so nobody notices the lost guardrails.

The second team looked across sessions instead of inside one run [2]. A skill that writes a file, a config or a cache hands that state to whatever reads it next. Two attacker-run packages can then relay an instruction, widen a data boundary or poison the evidence base without ever meeting in the same session.

Neither paper cites the other, yet both land on the same control point: what the agent reads at the start of a step.

## By the numbers

- **19.9 points — Installed skill pushed aside:** adding a similar second skill cut how often the installed skill got used by 19.9 points, while an unrelated skill cost it only 5.9 points. Task completion did not move [1].
- **5.6 points — Guardrails dropped:** the installed skill met its own rules 5.6 points less often on the checks only it asked for, and the wider measure of its work fell 2.6 points [1].
- **46.7% to 77.4% — Attack success:** seven models on three agent command-line tools gave cross-session attacks a success rate of 46.7% to 77.4%, and the full chain landed in 35.6% to 61.1% of runs [2].
- **69.5% to 10.9% — Read-time defense:** restoring where an artifact came from, plus a warning before each step, cut attack success to 10.9%. Legitimate task completion rose from 79.6% to 87.5%, at 4.3% of the tokens a run spends [2].

<!-- tactical-insight -->

## What I'd watch:

Both fixes sit at the moment a skill is read, not inside the model. I keep coming back to how plain the fix is: point the agent at the right skill, and say where an artifact came from.

- **Pinning the first read:** in the conflict study, 97% of runs change no file before they open a skill [1]. Denying the read of the look-alike made the model switch back to the installed skill in 96% of cases. That is a hook in a research setup, not a shipped feature, so I am watching which agent frameworks add the same control.
- **Scoping what a skill leaves behind:** the cross-session work happens because artifacts outlive the chat that made them [2]. Naming the file and adding a warning cut the attack by about a factor of six. The open question is whether platforms scope those artifacts per skill or per project.
- **Scoring what only the skill adds:** the conflict study measures a skill's core functions, the rules a capable model would not meet without it [1]. A test that scores task completion alone rated the clash harmless. I would want that gap closed before trusting a green board.
- **Naming which skill ran:** the reply said which skill was used in only 0.9% of the displaced runs [1]. Cheap disclosure would have made this failure class visible far earlier.

<!-- nuanced-takeaway -->

## The catch

My read is that both results are real, but narrower than they will sound. Neither paper is peer reviewed yet, and both groups ran their tests on made-up work.

The conflict study builds one task per skill pair. It scores the checks with scripts and a written-output judge, and it runs everything in an offline container [1]. Its clash is between two *similar* skills, the pair a careful team would hope never to install together.

The attack benchmark gives the attacker the skill packages and nothing else: not the model, not the harness, not the user's tasks [2]. Its defense advises the agent instead of blocking it. A reply that ignores good advice is still a bad reply.

I could be wrong, but the load-bearing detail here is not any single figure. It is that both studies found the loss where their own success metric could not see it.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Where the Prompt Breaks Decides the AI Bill" -> https://giniloh.com/cache-boundary-decides-input-bill/ [same site (giniloh.com); topical overlap: agent, found, research] Link "Where the Prompt Breaks Decides the AI Bill" in the section where the article touches agent, found, research. -->
<!-- internal-link hint: "Agent Memory Poisoning" -> https://giniloh.com/agent-memory-poisoning-write-path/ [same site (giniloh.com); same category; topical overlap: agent] Link "Agent Memory Poisoning" in the section where the article touches agent. -->
<!-- internal-link hint: "Durable Execution Is Not a Transaction" -> https://giniloh.com/durable-execution-not-a-transaction/ [same site (giniloh.com); same category; topical overlap: agent] Link "Durable Execution Is Not a Transaction" in the section where the article touches agent. -->
## Related reading

- [Where the Prompt Breaks Decides the AI Bill](https://giniloh.com/cache-boundary-decides-input-bill/)
- [Agent Memory Poisoning](https://giniloh.com/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Durable Execution Is Not a Transaction](https://giniloh.com/durable-execution-not-a-transaction/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Two papers published a day apart show the coding-agent skill layer acting like stateful infrastructure. A co-installed look-alike can quietly replace the installed skill and drop its rules, and artifacts one skill writes can carry an attack into a later session.
- **Why It Matters:** Task completion stays green through both failures. A team that gates a release on a passing test is signing off on the wrong thing, blind to a fix that lives at read time.
- **What I'd Watch:**
  - **First-read rules:** Whether agent frameworks ship a hook that pins the installed skill at its first read, which is where the clash is decided.
  - **Artifact scoping:** Whether platforms scope the files and caches a skill writes per skill instead of per project.
  - **Contribution scoring:** Whether evals score what a skill uniquely adds, not just whether the task passed.
- **The Catch:** Both papers are preprints on made-up tasks. The attack benchmark gives the attacker only the skill packages, and its defense advises the agent rather than blocking it.

## Sources
[1] Chaoliang Yan et al., "One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents," arXiv:2610.11647 (2026-10-08). https://arxiv.org/abs/2610.11647
[2] Dianshu Liao et al., "Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition," arXiv:2610.13227 (2026-10-09). https://arxiv.org/abs/2610.13227

## Gate report
lead: PASS — Concrete in sentence one, three short sentences, no preamble.
tension: PASS — First-person cue present; plain words; blank lines around the H2.
tactical-insight: PASS — Observations with bold lead-ins, no imperatives, existing figures only.
nuanced-takeaway: PASS — Opens with "My read is", names the limits of both studies.
tldr: PASS — 4-part schema, plain English, own H2.
voice: PASS — body reads as an observer comment.
access: PASS — Flesch above floor, every acronym written out (SKILL.md avoided, no bare acronyms).
