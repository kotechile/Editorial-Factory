# Editorial Factory — How It Works & User Guide

The Editorial Factory is an **autonomous content-intelligence engine**. It finds the most
compelling developments from the **last 30 days** in a set of topic areas ("verticals"),
verifies them against primary sources, and writes trustworthy, human-voice articles — with the
final polish always done by a frontier model (Claude, via kie.ai). Output is ready for LinkedIn
or a website.

It is the editorial twin of the Software Factory (`kotechile/factory`): same agentic workforce
pattern (a fleet of bots + skills + shared context + cron + an approval gate), but it ships
articles instead of software products.

---

## 1. The workforce — 7 bots

The "bots" are Hermes **profiles**. Each is one directory under `/root/.hermes/profiles/<name>/`
with a `SOUL.md` (its persona), `config.yaml` (its model), and `.env` (its keys).

| Bot | Role | Model |
|---|---|---|
| `editor` | Editor-in-Chief — runs the pipeline, owns the calendar and the approval gate | deepseek-v4-pro |
| `radar` | Radar Scout — 30-day signal sweep per vertical | deepseek-v4-pro |
| `judge` | Virality Judge — scores topics 1–10, drops anything < 8 | deepseek-v4-pro |
| `verifier` | Fact Verifier — extracts claims, validates against primary sources | deepseek-v4-pro |
| `drafter` | Story Drafter — writes the structural first pass | deepseek-v4-pro |
| `stylist` | Claude Stylist & Critic — the final human-voice rewrite | **Claude (`claude-sonnet-5`) via kie.ai** |
| `publisher` | Publisher — persists output and (when approved) distributes it | deepseek-v4-pro |

View them in the dashboard under **Profiles**, or with `hermes profile list`.

---

## 2. How it works — the three loops

One pipeline run moves through three loops, then an approval gate:

```
[Cron fires] → editor bot
   │
   ▼  Loop 1 — Scouting & validation
[radar] sweeps the vertical's sources (X/LinkedIn, arXiv, GitHub, Hacker News, Reddit,
        trade press), constrained to the last 30 days.
[judge] scores each signal on Novelty × Authority × Shareability.
        Only a score ≥ 8/10 proceeds. No signal ≥ 8 → the seeds broaden once, then "no publish".
   │
   ▼  Loop 2 — Verification
[verifier] breaks the winning angle into 3–5 checkable claims and validates each against a
           PRIMARY source. Unverifiable claims are flagged or removed — never paraphrased
           into plausibility.
   │
   ▼  Loop 3 — Draft & frontier rewrite
[drafter] writes the structured first pass (incident/stat lead → systemic reason → tactical
          takeaway), using only the verified evidence.
[stylist] (Claude) rewrites for human voice — cuts AI-tells, injects cadence — iterating
          section-by-section (lead first) until each section passes its own gate, then one
          whole-piece coherence pass.
   │
   ▼  Approval gate
[editor] halts. Nothing is published without your approval.
   │
   ▼  (on approval)
[publisher] writes the final article to published/ and (when configured) posts to
            LinkedIn / Ghost.
```

The full instructions live in `skills/*.md` (the SOPs) and the personas in `.agents/*.md`.

### Article anatomy

Every article has a fixed skeleton, written into the draft as machine-checkable markers:

`lead` (concrete incident/stat) → `tension` (the systemic shift) → `tactical-insight` (the
doable move) → `nuanced-takeaway` (the honest catch) → `tldr` (3 bullets, long-form only).

Two extras are **not** part of the body: the **TL;DR** is a structured field (never a prose
"in conclusion"), and the **TOC** is derived by the site at render time (never written by a bot).
The LinkedIn post is a separate ~1,300-char variant built from the same skeleton.

---

## 3. What runs when

Five cron jobs, one per vertical, each running the **complete** pipeline. Generated from
`context/verticals.json` (see "Adding a vertical").

| Job | Vertical | Schedule (UTC) |
|---|---|---|
| `Full Pipeline: agentic_ai` | Agentic Automation & Architecture | Mon + Thu 06:00 |
| `Full Pipeline: enterprise_tech_leadership` | Technology & Architecture Decisions | Tue 06:00 |
| `Full Pipeline: gpu_hardware` | GPUs & AI Hardware | Wed 06:00 |
| `Full Pipeline: supply_chain` | Supply Chain & Logistics Tech | Thu 06:00 |
| `Full Pipeline: home_systems_reno` | Modern Home Infrastructure & Building Science | Fri 06:00 |

View them with `hermes cron list` (or the dashboard **Cron** page). Each job runs with the repo
as its working directory, so the bot reads `AGENTS.md` and `skills/`.

---

## 4. How you use it

### 4.1 The autonomous flow (what happens without you)

On schedule, the cron fires and the `editor` bot drives the pipeline for that vertical. You do
nothing for the scouting, judging, verifying, and drafting stages — they run automatically.

### 4.2 Your one job: the approval gate

After the Claude rewrite, the pipeline **halts and waits for you**. Review the final draft:

- **In the dashboard:** Profiles → `editor` → its chat (or the Sessions page), or
- **On disk:** `context/drafts/YYYY-MM-DD_<slug>_final.md`

Then either:

- **Approve** — reply `approve` to the `editor` bot. The `publisher` writes the article to
  `published/` and logs it.
- **Request changes** — send feedback; the editor routes it back to `stylist` and re-posts.

> The gate is named `@Simon approve` in the personas (inherited from the Software Factory). If
> you wire the `editor` bot to Slack, "`@Simon approve`" in a Slack thread becomes the approval
> channel; today the approval happens in the dashboard's editor-bot chat.

### 4.3 Where the output lands

| Path | Contents |
|---|---|
| `context/recon_proposals/` | the raw signals, the angle brief, and the verified brief for each run |
| `context/drafts/` | the structural draft and the final Claude-rewritten piece |
| `published/` | approved articles (markdown) — served by the site |
| `context/published_log.md` | the running log of everything published |

### 4.4 Publishing to LinkedIn / a website

Approved articles land in `published/` automatically and are renderable by the bundled static
reader (`site/`, deployable via Coolify).

#### Embedding External Illustrated Articles & Software Factory Tools
When the article is generated, styled with illustrations in PressFlow/Ghost/external CMS, and you want the LinkedIn post to drive traffic to that live page or cross-promote a software factory tool:

```bash
# 1. Supply URLs via CLI arguments:
python3 scripts/publish.py context/drafts/YYYY-MM-DD_<slug>_final.md \
  --article-url "https://pressflow.example.com/posts/my-article-with-illustrations" \
  --promo-url "https://factory.example.com/tools/agent-security-scanner"

# 2. Or run interactively (will prompt for URLs):
python3 scripts/publish.py --interactive context/drafts/YYYY-MM-DD_<slug>_final.md

# 3. Or specify in the draft frontmatter:
# article_url: "https://pressflow.example.com/..."
# promo_url: "https://factory.example.com/tools/..."
```

The publisher automatically embeds the links into the LinkedIn post with clean call-to-actions:
```text
📖 Read the full illustrated breakdown: https://pressflow.example.com/...
🛠️ Try the live tool: https://factory.example.com/...
```

#### LinkedIn Switch (`LINKEDIN_AUTO_POST`)
- **`LINKEDIN_AUTO_POST=false` (default / review mode):** Outputs the complete formatted post with all embedded links ready to copy-paste into LinkedIn.
- **`LINKEDIN_AUTO_POST=true` (automated mode):** When `LINKEDIN_ACCESS_TOKEN` is set, dispatches the post with link attachments directly via the LinkedIn API.

### 4.5 Demand-Led SEO Content Machine (Growth OS)

In addition to the 30-day acute news scout, the engine includes a demand-driven **SEO Content Machine**:

```
[Google Search Console] ──> High-impression / emerging query detected (Pos 8-25, Impr > 500, WoW > 50%)
           │
           ▼
     [DataForSEO]        ──> Enrich with search volume, SERP intent, keyword clusters, top 10 URLs
           │
           ▼
 [Growth OS Knowledge]   ──> Cross-reference founder-voice.md & customer-truth.md (Moat & Taste)
           │
           ▼
[Cannibalization Shield] ──> Audit sitemap.json + generate contextual internal link map
           │
           ▼
     [LLM / Agent]       ──> Drafts post + meta title/description + JSON-LD schema (@Article/@FAQPage)
           │
           ▼
 [Frontier Humanizer]    ──> Loop 3 human-voice rewrite preserving SEO schema & internal links
           │
           ▼
    [Approval Gate]      ──> Human checks voice, adds contrarian founder take, hits publish
```

#### How to run the SEO Content Machine:

```bash
# 1. Scan Google Search Console opportunities (or view in PressFlow Web UI -> ⚡ SEO Content Machine)
python3 scripts/gsc_analyzer.py --min-impressions 500 --min-pos 8 --max-pos 25 --export-md

# 2. Enrich target keyword with DataForSEO intelligence
python3 scripts/dataforseo_client.py --keyword "mcp server implementation python"

# 3. Check cannibalization & internal linking
python3 scripts/growth_os.py --check-cannibalization --keyword "mcp server implementation python"
python3 scripts/growth_os.py --internal-links --keyword "mcp server implementation python"

# 4. Generate structured SEO draft with schema & frontier rewrite
python3 scripts/seo_machine.py --query "mcp server implementation python" --vertical "agentic_ai"

# 5. Monitor rank trajectory and feedback learnings
python3 scripts/gsc_feedback.py --export
```

#### Growth OS Knowledge Layer
- `context/growth_os/founder-voice.md`: Injects unshakeable stances and quotes to ensure articles are taste-differentiated.
- `context/growth_os/customer-truth.md`: Injects real customer friction, dollar figures, and operational anecdotes.
- `context/sitemap.json`: Prevents competing with your own published URLs and creates bidirectional internal link maps.



---

## 5. Adding a vertical (config-as-data)

Verticals can be managed interactively via the **PressFlow Web UI (Settings)**, via the **CLI tool**, or synced directly with **Supabase**.

### Option A: Interactively via PressFlow Web UI (Recommended)
1. Open the PressFlow web dashboard (`http://<vps-or-domain>:3000` or `http://localhost:3000`).
2. Click **⚙️ Verticals & Radar Settings** &rarr; **+ Add Vertical** (or click ✏️ to edit).
3. Select your cadence preset, target reader persona, sources, and angles.
4. Click **Save Vertical** — it instantly updates `context/verticals.json`, regenerates `context/content_calendar.md`, and syncs to Supabase (if configured).
5. Click **⚡ Sync Crons** to register new pipeline jobs in Hermes.

### Option B: Via Command-Line Tool (`scripts/manage_verticals.py`)
```bash
# List all configured verticals
python3 scripts/manage_verticals.py list

# Add a new vertical
python3 scripts/manage_verticals.py add \
  --id cybersecurity \
  --label "Security & Threat Intelligence" \
  --cadence "0 6 * * 1" \
  --persona eng_leader \
  --sources "cisa_alerts,hn_security,x_sec" \
  --angles "breach economics,AI-driven attacks,zero-trust ROI"

# Edit an existing vertical
python3 scripts/manage_verticals.py edit --id cybersecurity --cadence "0 6 * * 1,4"

# Delete a vertical
python3 scripts/manage_verticals.py delete --id cybersecurity

# Sync Hermes cron schedules
python3 scripts/sync_crons.py
```

### Option C: Supabase Cloud Database Sync
When `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` are set in `.env`:
- Table `editorial_verticals` acts as the cloud store.
- Sync commands:
  - `python3 scripts/sync_verticals.py push` (Local JSON &rarr; Supabase)
  - `python3 scripts/sync_verticals.py pull` (Supabase &rarr; Local JSON)
  - `python3 scripts/sync_verticals.py init-schema` (Prints SQL DDL)

---

## 6. Tuning the output

- **What to cover** — edit `sources` and `primary_angles` per vertical in `context/verticals.json`.
- **Who it speaks to** — edit the target reader's voice in `context/personas.json`.
- **How it reads** — the anti-AI voice rules live in `skills/claude_humanizer.md` (negative
  constraints + the human-voice gate). Tighten them there; the stylist follows them verbatim.
- **How picky the topic gate is** — the ≥ 8/10 threshold is in `skills/virality_judge.md`.

---

## 7. Monitoring & operations

| Task | How |
|---|---|
| See the bots | Dashboard **Profiles**, or `hermes profile list` |
| See the schedules | Dashboard **Cron**, or `hermes cron list` |
| Health-check the jobs | `hermes cron doctor` |
| Run one vertical now | `hermes -p editor chat -q "Run the full editorial pipeline for vertical 'agentic_ai' per skills/*.md. Halt at the approval gate."` |
| Validate a draft | `scripts/verify.sh` (checks config JSON, banned AI-tells, missing citations) |
| Read a run's artifacts | `context/recon_proposals/`, `context/drafts/` |

---

## 8. Troubleshooting

| Symptom | Cause / fix |
|---|---|
| Claude rewrite returns 502/503 | kie.ai's Claude upstream is intermittently unstable (known). The stylist retries 3× before halting — usually resolves on its own. Check `https://api.kie.ai/api/v1/chat/credit` to confirm the key is still valid. |
| A run produces nothing | Normal when no topic scores ≥ 8 — the engine refuses to publish a weak article. See the angle brief in `context/recon_proposals/` for why candidates were dropped. |
| "Missing ANTHROPIC_API_KEY" | The stylist halts (by design) — verify `ANTHROPIC_API_KEY=*** <key>` in the stylist profile's `.env`. |
| Claims removed | The verifier dropped unverifiable claims. Check the verified brief; that's the no-hallucination rule working as intended. |
| Job not firing | `hermes cron status` and `systemctl --user status hermes-gateway.service hermes-dashboard.service`. |

---

## 9. Repository map

```
.agents/       persona contracts (each bot's SOUL.md source)
skills/        the SOPs — the three loops + publishing + self-improvement
context/       verticals.json, personas.json, calendar, published log, run artifacts
scripts/       cron wrappers, sync_crons.py (add verticals), verify.sh (quality gate)
site/          minimal static reader for published/ (Coolify-deployable)
published/     approved articles (markdown)
docs/          this guide + VPS_WIRING.md (deployment details)
```

## 10. Current status

- **Live:** 7 bot profiles, 5 cron jobs, config-driven verticals, the reader site, the approval
  gate, and Claude-via-kie.ai routing.
- **Pending your input:** LinkedIn/Ghost publishing keys, Supabase persistence tables, and a
  Slack channel for the `editor` bot if you want `@Simon approve` to flow through Slack.
