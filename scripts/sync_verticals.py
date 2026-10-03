#!/usr/bin/env python3
"""Sync editorial verticals and personas between Supabase and local JSON context.

Usage:
  python3 scripts/sync_verticals.py push        # Push local JSON to Supabase
  python3 scripts/sync_verticals.py pull        # Pull Supabase rows to local JSON
  python3 scripts/sync_verticals.py update-cal  # Update context/content_calendar.md
  python3 scripts/sync_verticals.py init-schema # Print SQL schema for Supabase
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERTICALS_PATH = os.path.join(REPO, "context", "verticals.json")
PERSONAS_PATH = os.path.join(REPO, "context", "personas.json")
CALENDAR_PATH = os.path.join(REPO, "context", "content_calendar.md")

# The fleet-mode columns (news vs evergreen) are additive: an existing project's
# `editorial_verticals` table predates them, and PostgREST rejects the whole upsert on one unknown
# key. So the mirror degrades loudly instead of failing — see push_to_supabase().
FLEET_COLUMNS = ("news_enabled", "evergreen_cadence", "evergreen_enabled")
SCHEMA_ALTER = """alter table editorial_verticals
  add column if not exists news_enabled boolean default true,
  add column if not exists evergreen_cadence text,
  add column if not exists evergreen_enabled boolean default true;"""
ENV_PATH = os.path.join(REPO, ".env")


def load_env():
    """Load repo-local .env into os.environ if present and not already set."""
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k, v = k.strip(), v.strip().strip("'\"")
                    if k not in os.environ or not os.environ[k]:
                        os.environ[k] = v


def get_supabase_creds():
    load_env()
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "") or os.environ.get("SUPABASE_KEY", "")
    return url, key


def supabase_request(endpoint: str, method: str = "GET", data=None, params=None):
    url, key = get_supabase_creds()
    if not url or not key:
        return None, "SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY missing"

    full_url = f"{url}/rest/v1/{endpoint}"
    if params:
        query = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items())
        full_url += f"?{query}"

    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation,resolution=merge-duplicates",
    }

    body = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(full_url, data=body, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode("utf-8")
            return (json.loads(content) if content else {}), None
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        return None, f"HTTP {e.code}: {err}"
    except Exception as e:
        return None, str(e)


def human_cadence(cadence_str: str) -> str:
    """Format cron string into human readable cadence string."""
    parts = cadence_str.strip().split()
    if len(parts) >= 5:
        minute, hour, dom, month, dow = parts[:5]
        h_int = int(hour) if hour.isdigit() else 6
        am_pm = "AM" if h_int < 12 else "PM"
        h_12 = h_int if 1 <= h_int <= 12 else (h_int - 12 if h_int > 12 else 12)
        # The scheduler fires on the host clock, which is UTC on the VPS. Labelling this "EST"
        # made the DeepSeek peak windows (Mon-Fri 01:00-04:00 + 06:00-10:00 UTC) look off by
        # hours, so the label has to match how the cadence is actually read.
        time_str = f"{h_12:02d}:{int(minute) if minute.isdigit() else 0:02d} {am_pm} UTC"

        day_map = {"0": "Sun", "1": "Mon", "2": "Tue", "3": "Wed", "4": "Thu", "5": "Fri", "6": "Sat", "7": "Sun"}
        if dow == "*":
            return f"Daily {time_str}"
        days = [day_map.get(d, d) for d in dow.split(",")]
        return f"{' + '.join(days)} {time_str}"
    return cadence_str


def update_content_calendar(verticals):
    """Regenerate context/content_calendar.md with updated cadence table while preserving log.

    Both fleets are listed, because both are reconciled from this registry
    (`scripts/sync_crons.py`) and a mode switched off in the vertical's settings has no job at all.
    So the calendar has to show the *settings*, not just the news slot it used to show.
    """
    existing_log = ""
    if os.path.exists(CALENDAR_PATH):
        with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
            content = f.read()
            if "## Run log" in content:
                existing_log = content[content.index("## Run log"):]

    if not existing_log:
        existing_log = "## Run log\n| Date | Vertical | Result | Notes |\n|---|---|---|---|\n"

    lines = [
        "# Content Calendar",
        "",
        "Schedules per vertical, for both fleets. The Editor-in-Chief dispatches the Radar Scout on",
        "the news schedule and the Evergreen Scout on the evergreen schedule; a mode switched off in",
        "the vertical's settings (`news_enabled` / `evergreen_enabled`) has no job at all —",
        "`scripts/sync_crons.py` reconciles both fleets from `context/verticals.json`.",
        "",
        "| Vertical | News cadence | News schedule (UTC) | Evergreen cadence | Evergreen schedule (UTC) | Mode |",
        "|---|---|---|---|---|---|",
    ]

    for v in verticals:
        vid = v.get("id", "")
        news = v.get("cadence", "")
        evergreen = v.get("evergreen_cadence", "")
        news_on = v.get("news_enabled", True)
        evergreen_on = bool(evergreen) and v.get("evergreen_enabled", True)
        mode = "+".join(n for n, on in (("news", news_on), ("evergreen", evergreen_on)) if on)
        lines.append(
            f"| {vid} | {news if news_on else '—'} "
            f"| {human_cadence(news) if news_on else 'off'} "
            f"| {evergreen if evergreen_on else '—'} "
            f"| {human_cadence(evergreen) if evergreen_on else 'off'} "
            f"| {mode or 'disabled'} |"
        )

    lines.append("")
    lines.append(existing_log.strip())
    lines.append("")

    with open(CALENDAR_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  [Calendar] Updated {CALENDAR_PATH}")


def push_to_supabase():
    url, key = get_supabase_creds()
    if not url or not key:
        print("ERROR: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY is not set.")
        return 1

    # 1. Verticals
    with open(VERTICALS_PATH, "r", encoding="utf-8") as f:
        v_data = json.load(f)
    verticals = v_data.get("verticals", [])

    rows = []
    for v in verticals:
        rows.append({
            "id": v["id"],
            "label": v.get("label", v["id"]),
            "cadence": v.get("cadence", "0 6 * * 1"),
            "news_enabled": v.get("news_enabled", True),
            "evergreen_cadence": v.get("evergreen_cadence") or None,
            "evergreen_enabled": v.get("evergreen_enabled", True),
            "target_persona": v.get("target_persona", "eng_leader"),
            "sources": v.get("sources", []),
            "primary_angles": v.get("primary_angles", []),
            "enable_dataforseo": v.get("enable_dataforseo", True),
            "is_active": True,
        })

    res, err = supabase_request("editorial_verticals", method="POST", data=rows)
    if err and any(t in str(err).lower() for t in ("does not exist", "schema cache", "column")):
        # Fail loud, then degrade in a way the operator can act on: the local registry is the
        # source of truth for the fleet, so keeping the rest of the mirror current beats refusing
        # to sync until the DDL lands. The dashboard's mode toggles still persist locally.
        print("WARNING: the Supabase 'editorial_verticals' table has no fleet-mode columns, so the "
              "remote mirror cannot store them. Run this in the Supabase SQL editor:\n\n"
              + SCHEMA_ALTER + "\n")
        print("Retrying without news_enabled / evergreen_cadence / evergreen_enabled ...")
        legacy = [{k: val for k, val in r.items() if k not in FLEET_COLUMNS} for r in rows]
        res, err = supabase_request("editorial_verticals", method="POST", data=legacy)
    if err:
        print(f"ERROR pushing verticals to Supabase: {err}")
        return 1
    print(f"Successfully pushed {len(rows)} verticals to Supabase 'editorial_verticals'.")

    # 2. Personas
    if os.path.exists(PERSONAS_PATH):
        with open(PERSONAS_PATH, "r", encoding="utf-8") as f:
            p_data = json.load(f)
        personas = p_data.get("personas", {})
        p_rows = []
        for pid, p in personas.items():
            p_rows.append({
                "id": pid,
                "label": p.get("label", pid),
                "reader_level": p.get("reader_level", ""),
                "tone": p.get("tone", ""),
                "wants": p.get("wants", ""),
            })
        if p_rows:
            pres, perr = supabase_request("editorial_personas", method="POST", data=p_rows)
            if perr:
                print(f"Warning pushing personas: {perr}")
            else:
                print(f"Successfully pushed {len(p_rows)} personas to Supabase 'editorial_personas'.")

    update_content_calendar(verticals)
    return 0


def pull_from_supabase():
    url, key = get_supabase_creds()
    if not url or not key:
        print("ERROR: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY is not set.")
        return 1

    res, err = supabase_request("editorial_verticals?select=*&order=id.asc")
    if err:
        print(f"ERROR pulling verticals from Supabase: {err}")
        return 1

    if not isinstance(res, list):
        print(f"Unexpected response from Supabase: {res}")
        return 1

    verticals = []
    for row in res:
        verticals.append({
            "id": row["id"],
            "label": row.get("label", row["id"]),
            "cadence": row.get("cadence", "0 6 * * 1"),
            "news_enabled": row.get("news_enabled") if row.get("news_enabled") is not None else True,
            "evergreen_cadence": row.get("evergreen_cadence") or "",
            "evergreen_enabled": row.get("evergreen_enabled") if row.get("evergreen_enabled") is not None else True,
            "sources": row.get("sources") or [],
            "primary_angles": row.get("primary_angles") or [],
            "target_persona": row.get("target_persona", "eng_leader"),
            "enable_dataforseo": row.get("enable_dataforseo") if row.get("enable_dataforseo") is not None else True,
        })

    with open(VERTICALS_PATH, "w", encoding="utf-8") as f:
        json.dump({"verticals": verticals}, f, indent=2)
    print(f"Successfully pulled {len(verticals)} verticals to {VERTICALS_PATH}")

    # Personas
    pres, perr = supabase_request("editorial_personas?select=*")
    if not perr and isinstance(pres, list) and len(pres) > 0:
        personas = {}
        for row in pres:
            personas[row["id"]] = {
                "label": row.get("label", row["id"]),
                "reader_level": row.get("reader_level", ""),
                "tone": row.get("tone", ""),
                "wants": row.get("wants", ""),
            }
        with open(PERSONAS_PATH, "w", encoding="utf-8") as f:
            json.dump({"personas": personas}, f, indent=2)
        print(f"Successfully pulled {len(personas)} personas to {PERSONAS_PATH}")

    update_content_calendar(verticals)
    return 0


def print_schema():
    sql = """-- Supabase SQL schema for Editorial Factory settings & verticals

create table if not exists editorial_verticals (
  id text primary key,
  label text not null,
  cadence text not null,
  news_enabled boolean default true,
  evergreen_cadence text,
  evergreen_enabled boolean default true,
  target_persona text not null,
  sources jsonb default '[]'::jsonb,
  primary_angles jsonb default '[]'::jsonb,
  enable_dataforseo boolean default true,
  is_active boolean default true,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- Existing project? Add the fleet-mode columns (the dashboard's News / Evergreen toggles):
""" + SCHEMA_ALTER + """


create table if not exists editorial_personas (
  id text primary key,
  label text not null,
  reader_level text,
  tone text,
  wants text,
  updated_at timestamptz default now()
);

-- Enable Row Level Security (optional / standard)
alter table editorial_verticals enable row level security;
alter table editorial_personas enable row level security;

-- Allow read for authenticated or service role
create policy "Allow read access for all" on editorial_verticals for select using (true);
create policy "Allow read access for personas" on editorial_personas for select using (true);
"""
    print(sql)


def main():
    parser = argparse.ArgumentParser(description="Sync verticals between Supabase and local JSON.")
    parser.add_argument("action", choices=["push", "pull", "update-cal", "init-schema"])
    args = parser.parse_args()

    if args.action == "push":
        return push_to_supabase()
    elif args.action == "pull":
        return pull_from_supabase()
    elif args.action == "update-cal":
        with open(VERTICALS_PATH, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        update_content_calendar(v_data.get("verticals", []))
        return 0
    elif args.action == "init-schema":
        print_schema()
        return 0


if __name__ == "__main__":
    sys.exit(main())
