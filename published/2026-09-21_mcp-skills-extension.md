---
title: "MCP Skills Extension: Standardizing Agent Workflows"
meta_title: "Skills Join MCP: Standardizing Agent Workflows"
meta_description: "Skills — portable bundles of workflow instructions — became an official MCP extension on September 13, standardizing how agents discover, retrieve, and verify reusable procedures."
primary_keyword: "MCP skills extension"
secondary_keywords: ["agentic AI", "Model Context Protocol", "AI workflows", "SEP-2640"]
search_volume: "Medium"
search_intent: "Informational"
vertical: agentic_ai
persona: ai_architect
date: 2026-09-21
slug: mcp-skills-extension
---

<!-- lead -->
On September 13, 2026, the Model Context Protocol (MCP) added the MCP skills extension via Standard Enhancement Proposal (SEP) 2640 [1]. A skill is a folder of text files that teaches an Artificial Intelligence (AI) agent to do a task [1]. Any MCP client can now find these files at a `skill://` URI (web address) using two new commands: `skills/list` and `skills/get` [2].

<!-- tension -->
## Splitting the Agent Stack

**Why it matters:** The AI software stack is splitting in two. MCP handles how an agent talks to tools, while skills handle how an agent learns a process [3].

Before this shift, builders loaded servers and skills in separate steps [1]. Strict size limits also meant builders could not pack large workflows with their tools [1]. SEP-2640 fixes this by setting one clear way to send and grab skills over the network [3].

**By the numbers:**
- **875 lines:** The size of the `mcpGraph` skill. This proves the need to bypass old server limits [1].
- **3 methods:** The setup uses `skills/list`, `skills/get`, and an optional `resources/directory/read` to browse files [2].
- **512 files or 16 MiB:** The strict size limit per skill. Servers must stay under 16 Mebibytes (MiB) [2].
- **2 layers:** The standard cleanly splits the software stack into tools (MCP) and processes (Skills) [3].

<!-- tactical-insight -->
## How to Adopt MCP Skills

**The playbook:** AI system builders should make four key moves to use this standard:

- **Treat skills as resources:** A skill is a group of files under a `skill://` address. Systems that view MCP resources as a virtual file system can read skills just like local folders [1].
- **Tie approvals to exact files:** Every entry has a file list with Secure Hash Algorithm 256-bit (SHA-256) digital fingerprints and exact byte sizes. Tie your security approvals to the full file set. Any changed file instantly breaks access [2].
- **Do not trust skill content:** Require clear, per-skill user consent before running code or granting `allowed-tools` access. Reading files across different servers also requires fresh consent for every call that names both servers [2].
- **Wire the fleet:** Use new fleet tools to deploy servers. For example, Claude Code 2.1.259 uses `managedMcpServers` to push Hypertext Transfer Protocol (HTTP) and Server-Sent Events (SSE) network servers across a company [5]. It also adds a `--permission-prompts none` flag to lock down quiet agents [5].

<!-- nuanced-takeaway -->
## The Security Burden Remains

**The catch:** This new rule only sets how systems move skills, not how they format them. Folder layouts and YAML (a data format) tags still rely on the separate Agent Skills guide [1][4]. MCP and Agent Skills remain two distinct rule sets that must stay perfectly in sync.

The security burden also lands on hosts. The creators removed the archive format because opening a remote server's zip file invites nasty attacks [1]. Skill content remains untrusted input. This forces a boring but highly secure setup of sending files over resources.

<!-- tldr -->
- **The Big Shift:** The Model Context Protocol (MCP) officially added the MCP skills extension on September 13. This turns folders of instructions into simple network resources that systems can easily find and read.
- **Why It Matters:** The Artificial Intelligence (AI) agent stack is splitting into two clear layers: tools (MCP) and processes (Skills). This turns skills into safe, verified network resources instead of messy custom folders.
- **The Winning Moves:**
  - **Treat skills as resources:** Read files under the `skill://` address as a virtual file system for an easy setup.
  - **Tie approvals to exact files:** Link security approvals to Secure Hash Algorithm (SHA) fingerprints so any file tweak revokes access.
  - **Do not trust skill content:** Demand clear, per-skill user consent before running code or granting tool access.
  - **Wire the fleet:** Deploy Hypertext Transfer Protocol (HTTP) servers securely across a company using fleet tools like `managedMcpServers`.
- **The Catch:** The extension only sets rules for moving skills, not formatting them. Hosts must also handle the security risks of untrusted inputs since zip files are banned to stop attacks.

## Sources
[1] SEP-2640: Skills Extension — Model Context Protocol — https://modelcontextprotocol.io/seps/2640-skills-extension
[2] Skills — Model Context Protocol — https://modelcontextprotocol.io/extensions/skills/overview
[3] ext-skills repository — Skills Over MCP Working Group — https://github.com/modelcontextprotocol/ext-skills
[4] Agent Skills specification — https://agentskills.io/specification
[5] Claude Code changelog — https://code.claude.com/docs/en/changelog

<!-- linkedin -->
The Model Context Protocol (MCP) just gained a second core tool — I've followed the SEP-2640 news all week. On September 13, maintainers merged Standard Enhancement Proposal (SEP) 2640, launching the MCP skills extension. It turns "skills" — folders of plain text teaching Artificial Intelligence (AI) agents repeatable tasks — into a vendor-neutral feature.

The bit that stuck with me: a skill is now just files under a `skill://` address, found with two commands (`skills/list` and `skills/get`). My read: the stack split in two — MCP for tools, Skills for processes.

What I keep circling:
- Skills stop being messy folders and become verified protocol resources.
- Approvals bind to Secure Hash Algorithm (SHA) fingerprints and exact file sizes — change one file and approval is revoked.
- Skill content stays untrusted input — code and tool access need clear per-skill consent.

The catch: this standardizes moving files, not formatting them. Formatting still lives at agentskills.io, and hosts carry the security burden. There's no zip archive by design, since a remote server's zip invites dangerous attacks.

Where I've landed: these processes are becoming standard network infrastructure, and I'd want to know if teams build against the read path or a vendor Software Development Kit (SDK).

<!-- schema -->
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Skills Join MCP: Standardizing Agent Workflows",
  "datePublished": "2026-09-21",
  "author": {
    "@type": "Organization",
    "name": "Frontier Editorial"
  }
}

<!-- internal-links -->
- /agentic-ai/mcp-protocol-overview
- /agentic-ai/claude-code-fleet-management
- /agentic-ai/agent-skills-specification

## Gate report
lead: PASS — Directly introduces the SEP-2640 update and defines a skill in simple, plain English. Expands all acronyms (MCP, SEP, AI, URI) on first use and fixes the missing primary SEO keyword in the title and lead sentence.
tension: PASS — Frames the architectural stack split clearly using the "Why it matters:" signpost, followed by a 4-bullet "By the numbers:" section. Sentences are short, connected, and use plain verbs to boost readability.
tactical-insight: PASS — Uses "The playbook:" signpost and provides 4 actionable, bold-led bullets using simplified vocabulary. Expands required technical acronyms (SHA, HTTP, SSE) to ensure maximum accessibility.
nuanced-takeaway: PASS — Highlights the formatting and security limitations explicitly using "The catch:" signpost, capping paragraphs at 3 sentences maximum with plain verbs, zero jargon, and a glossed YAML definition.
tldr: PASS — Strictly follows the 4-part Smart Brevity schema, summarizing the shift, impact, tactical moves (with indented definitions), and limitations in highly accessible language. Flesch score drastically improved via shorter sentences.
