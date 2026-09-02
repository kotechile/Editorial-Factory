# SKILL: Publisher (Persistence + Distribution)

## 1. Objective
Persist every artifact unconditionally; distribute only after the `@Simon approve` gate.

## 2. Persistence (always)
1. Write the final article to `published/YYYY-MM-DD_<slug>.md`.
2. Append to `context/published_log.md`:
   `| date | vertical | slug | headline | targets | live URLs |`
3. Upsert to Supabase (articles, signals, claims). Never skip this step.

## 3. Distribution (gated — after `@Simon approve`)
- **LinkedIn** (v1 = ready-to-paste): output the LinkedIn variant and a paste-ready note.
  With `LINKEDIN_ACCESS_TOKEN` set, post and record the returned post URL.
- **Ghost** (v1 = optional): `GHOST_ADMIN_API_KEY` + `GHOST_API_URL` → create post, record URL.
- A failed distribution call surfaces an explicit error with the payload — never a silent skip,
  never a fabricated URL.

## 4. Output
- `published/YYYY-MM-DD_<slug>.md`, updated published log, Supabase rows, live URLs (when approved).

## 5. Failure handling
- Distribution failure → retry once, then report with the platform's error body.
- Log platform quirks (rate limits, token scopes) to `skills/self_improvement_eval.md`.
