# Angle Brief: agentic_ai — 2026-09-21

**Winner:** The agent stack is standardizing into two vendor-neutral layers — MCP for tools, Agent Skills for procedures — and on September 13 the MCP maintainers merged SEP-2640, making "skills" an official protocol extension served as ordinary `skill://` resources with two new discovery methods.

**Scores:** N=8 A=9 S=8 → Composite=8.3

**Hook:** On September 13, 2026, the Model Context Protocol (MCP) merged SEP-2640, turning "skills" — folders of markdown instructions that teach an agent a repeatable workflow — into an official, vendor-neutral extension. A skill is now a directory of files exposed to any MCP client as resources under a `skill://` URI, discoverable through two new methods (`skills/list`, `skills/get`), with the format itself left to the existing Agent Skills spec (agentskills.io). This is the second standardized layer in the agent stack: MCP answered "how does an agent connect to tools"; skills now answer "how does an agent learn a procedure."

**Tension:** For two years MCP has been the de facto tool standard, but skills stayed fragmented — a server and the skill that teaches an agent to use it were "versioned, discovered, and installed separately" (SEP-2640's own motivation). Server instructions were practically bounded, so real workflows (an 875-line `mcpGraph` skill) couldn't ship with the tool they described. SEP-2640 standardizes only the transport — skills over the Resources primitive — deliberately leaving the skill *format* to agentskills.io, so the two standards interlock rather than compete. In the same month the fabric got wired into fleet management: Claude Code 2.1.259 (Sept 3) added `managedMcpServers` (orgs inject HTTP/SSE MCP servers into every user) and `--permission-prompts none` (deny-by-default for unattended headless agents).

**Target reader:** ai_architect

**Single claim to defend:** SEP-2640 (Skills Extension), marked Final and merged into the MCP specification on 2026-09-13, standardizes serving Agent Skills over MCP using the existing Resources primitive — each skill file becomes a `skill://` resource discovered via `skills/list` and `skills/get` — turning "skills" from a fragmented, vendor-adjacent folder format into a transport-neutral, integrity-verified MCP primitive.

**Runner-ups + why rejected:**
- Claude Code 2.1.259 managed MCP + headless permissions (Sept 3): strong and practitioner-actionable, but a single-vendor CLI point release; folded in as corroboration that the same MCP fabric is being wired into production fleet management (N=8 S=8, but narrower than a cross-industry protocol milestone). Not selected as standalone winner.
- Apple Xcode 26.3 native Claude Agent SDK (Sept 2026): harness-distribution story, but date is ambiguous (Apple newsroom URL carries /2026/02/) and it's a distribution beat, not an architecture beat. N=6.
- "1 in 5 MCP access policies broken/missing" (Sept 10): fresh security signal, but off-vertical — maps to enterprise_ai_governance, not agentic runtime/architecture. N=7 S=6.
- DeepSeek V4.1-Flash 4× KV-cache reduction (Sept 10): concrete memory-economics figure, but a single-vendor model release. N=6 S=6.

**Prior-cycle de-dup check (passed):** OWASP Excessive Agency (09-03, permissions), Anthropic multi-agent turf war (09-07, safety), Google 4 patterns (09-10, determinism engineering), OpenAI Agents API (09-14, loop runtime commoditization), Salesforce harness > model (09-17, harness + MCP integration fabric). None covered "skills as a protocol primitive" or the "skills layer standardizing" thesis. SEP-2640 is a new source (the MCP spec), a new event (Sept 13 merge), and a new angle (procedure-knowledge standardization). Not a retread.
