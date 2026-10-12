---
title: "One Skill Too Many: The Green Test Is Blind"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "The skill layer of a coding agent is a stateful supply chain: a co-installed look-alike skill can take a run away from the installed one and drop its rules, and artifacts a skill writes can carry an attack into a later session, while task completion stays green through both."
date: 2026-10-12
slug: one-skill-too-many-green-test
synthesis: true
sources:
  - https://arxiv.org/abs/2610.11647
  - https://arxiv.org/abs/2610.13227
---

<!-- lead -->
Across 6,368 controlled coding-agent runs and 270 adversarial skills cases, two research groups published a day apart found the same blind spot [1][2]. The green test a team gates a release on cannot see the damage. One skill too many is all it takes.

<!-- tension -->

## The big picture:

Skills ship as packages now. A skill is a folder with a SKILL.md file that tells the agent when to use it and how, and the agent picks between them by name and description alone. Most teams treat the install as configuration.

What strikes me here is that both papers measured the skill layer as stateful infrastructure. Both found the failure sitting in plain sight.

The first team mined 20,947 repository snapshots and found 822,109 pairs of skills that do the same job [1]. Install two of them and the agent does not merge them or refuse. It picks one, and the loser goes quiet.

The checks only the installed skill carried stop happening, like a ban on touching git or a required review step [1]. The task still passes, so nobody notices.

The second team looked across sessions instead of inside one [2]. A skill that writes a file, a config or a cache hands state to whatever reads it next. Two attacker-run packages can then relay an instruction, widen a data boundary or poison the evidence base, and they never have to meet in one session.

Neither paper cites the other. Both land on the same control point anyway: what the agent reads at the start of a step.

## By the numbers

- **19.9 points — Installed skill pushed aside:** adding a similar second skill cut how often the installed skill got used by 19.9 points. An unrelated skill cost it only 5.9 points, and task completion did not move [1].
- **5.6 points — Guardrails dropped:** the installed skill's own requirements were met 5.6 points less often on the checks only it asked for, while the wider measure of its behaviour fell 2.6 points [1].
- **46.7% to 77.4% — Attack success:** seven models on three agent command-line tools gave cross-session attacks a success rate of 46.7% to 77.4%, and the full chain landed in 35.6% to 61.1% of runs [2].
- **69.5% to 10.9% — Read-time defense:** restoring where an artifact came from, plus a warning before each step, cut attack success to 10.9%. Legitimate task completion rose from 79.6% to 87.5%, at 4.3% of the tokens a run spends [2].

<!-- tactical-insight -->

## What I'd watch:

Both fixes sit at the moment a skill is read, not in the model. I keep coming back to how plain the intervention is: point the agent at the right skill, and say where an artifact came from.

- **Pinning the first read:** in the conflict study, 97% of runs change no file before they open a skill [1]. Denying the read of the look-alike made the model switch back to the installed skill in 96% of cases. That is a hook in a research setup, not a shipped feature, so I am watching which harnesses add the equivalent.
- **Scoping what a skill leaves behind:** the cross-session work happens because artifacts outlive the conversation that made them [2]. Attribution and an advisory cut the attack by about a factor of six. The open question is whether platforms scope those artifacts per skill or per project.
- **Scoring what only the skill adds:** the conflict study measures a skill's core functions, the requirements a capable model would not meet without it [1]. A test that scores task completion rated the clash harmless. I would want that gap closed before trusting a green board.
- **Naming which skill ran:** the reply said which skill was used in only 0.9% of the displaced runs [1]. Cheap disclosure would have made this failure class visible far earlier.

<!-- nuanced-takeaway -->

## The catch

My read is that both results are real and narrower than they will sound. Neither paper is peer reviewed yet, and both ran on constructed work.

The conflict study builds one task per skill pair. It scores the checks with scripts and a written-output judge, and it runs everything in an offline container [1]. Its clash is between two *similar* skills, the pair a careful team would hope never to install.

The attack benchmark gives the attacker the skill packages and nothing else: not the model, not the harness, not the user's tasks [2]. Its defense advises the agent instead of blocking it. A reply that ignores good advice is still a bad reply.

I could be wrong, but the load-bearing number here is not any single figure. It is that both studies put the loss where their own success metric could not see it.

<!-- internal-links -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Two papers published a day apart show the skill layer acting like stateful infrastructure. A co-installed look-alike can quietly replace the installed skill and drop its rules, and artifacts one skill writes can carry an attack into a later session.
- **Why It Matters:** Task completion stays green through both failures, so a team that gates a release on passing tests is signing off on the wrong thing. The fixes act at read time, not on the model.
- **What I'd Watch:**
  - **First-read rules:** Whether agent harnesses ship a hook that pins the installed skill at its first read, the point where the conflict is decided.
  - **Artifact scoping:** Whether platforms scope the files and caches a skill writes per skill instead of per project.
  - **Contribution scoring:** Whether evaluations score what a skill uniquely adds, not just whether the task passed.
- **The Catch:** Both papers are preprints on constructed tasks. The attack benchmark gives the attacker only the skill packages, and its defense advises the agent rather than blocking it.

## Sources
[1] Chaoliang Yan et al., "One Skill Too Many: How Co-Installed Skills Conflict in Coding Agents," arXiv:2610.11647 (2026-10-08). https://arxiv.org/abs/2610.11647
[2] Dianshu Liao et al., "Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition," arXiv:2610.13227 (2026-10-09). https://arxiv.org/abs/2610.13227
