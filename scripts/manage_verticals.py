#!/usr/bin/env python3
"""Interactive / CLI management for Editorial Factory verticals.

Usage:
  python3 scripts/manage_verticals.py list
  python3 scripts/manage_verticals.py add --id <id> --label <label> --cadence <cron> --persona <persona> --sources <s1,s2> --angles <a1,a2>
  python3 scripts/manage_verticals.py edit --id <id> [--label <label>] [--cadence <cron>] [--persona <persona>] [--sources <s1,s2>] [--angles <a1,a2>]
  python3 scripts/manage_verticals.py delete --id <id>
  python3 scripts/manage_verticals.py sync-cal
"""
import argparse
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERTICALS_PATH = os.path.join(REPO, "context", "verticals.json")
PERSONAS_PATH = os.path.join(REPO, "context", "personas.json")

# Import helpers from sync_verticals if present
try:
    from sync_verticals import update_content_calendar, push_to_supabase, pull_from_supabase, get_supabase_creds, supabase_request
except ImportError:
    sys.path.insert(0, os.path.join(REPO, "scripts"))
    from sync_verticals import update_content_calendar, push_to_supabase, pull_from_supabase, get_supabase_creds, supabase_request


def load_verticals():
    if not os.path.exists(VERTICALS_PATH):
        return []
    with open(VERTICALS_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("verticals", [])


def save_verticals(verticals):
    with open(VERTICALS_PATH, "w", encoding="utf-8") as f:
        json.dump({"verticals": verticals}, f, indent=2)
    update_content_calendar(verticals)


def list_verticals():
    verticals = load_verticals()
    print(f"\nEditorial Factory Verticals ({len(verticals)} configured):")
    print("=" * 70)
    for i, v in enumerate(verticals, 1):
        d4s_status = "ON (live API credits)" if v.get("enable_dataforseo", True) else "OFF (credit bypass)"
        news_on = v.get("news_enabled", True)
        evergreen_on = bool(v.get("evergreen_cadence")) and v.get("evergreen_enabled", True)
        modes = "+".join(n for n, on in (("news", news_on), ("evergreen", evergreen_on)) if on) or "disabled"
        print(f"{i}. [{v.get('id')}] {v.get('label')}")
        print(f"   Modes:      {modes}")
        print(f"   Cadence:    {v.get('cadence') if news_on else '— (news off)'}")
        print(f"   Evergreen:  {(v.get('evergreen_cadence') or '—') if evergreen_on else '— (evergreen off)'}")
        print(f"   Persona:    {v.get('target_persona')}")
        print(f"   DataForSEO: {d4s_status}")
        print(f"   Sources:    {', '.join(v.get('sources', []))}")
        print(f"   Angles:     {', '.join(v.get('primary_angles', []))}")
        print("-" * 70)


def add_vertical(args):
    verticals = load_verticals()
    vid = args.id.strip().lower().replace(" ", "_")
    if any(v.get("id") == vid for v in verticals):
        print(f"ERROR: Vertical with ID '{vid}' already exists.")
        return 1

    sources = [s.strip() for s in args.sources.split(",") if s.strip()] if args.sources else []
    angles = [a.strip() for a in args.angles.split(",") if a.strip()] if args.angles else []

    new_v = {
        "id": vid,
        "label": args.label.strip() if args.label else vid,
        # Default to an off-peak weekday slot: DeepSeek charges 2x on Mon-Fri 01:00-04:00 and
        # 06:00-10:00 UTC, so a new vertical must not land in that window by default.
        "cadence": args.cadence.strip() if args.cadence else "30 10 * * 1",
        "news_enabled": True,
        # No evergreen slot by default: the band has to be picked against the live fleet, and
        # scripts/sync_crons.py --check fails on a collision or a peak window. Pass
        # --evergreen-cadence (e.g. '30 18 * * 1') to switch the second pipeline on.
        "evergreen_cadence": (getattr(args, "evergreen_cadence", "") or "").strip(),
        "evergreen_enabled": bool((getattr(args, "evergreen_cadence", "") or "").strip()),
        "target_persona": args.persona.strip() if args.persona else "eng_leader",
        "sources": sources,
        "primary_angles": angles,
        "enable_dataforseo": not args.disable_dataforseo if hasattr(args, "disable_dataforseo") else True,
    }
    verticals.append(new_v)
    save_verticals(verticals)
    print(f"Added vertical '{vid}' ({new_v['label']}) successfully.")

    url, _ = get_supabase_creds()
    if url:
        print("  Pushing update to Supabase...")
        push_to_supabase()
    return 0


def edit_vertical(args):
    verticals = load_verticals()
    vid = args.id.strip()
    target = None
    for v in verticals:
        if v.get("id") == vid:
            target = v
            break

    if not target:
        print(f"ERROR: Vertical with ID '{vid}' not found.")
        return 1

    if args.label is not None:
        target["label"] = args.label.strip()
    if args.cadence is not None:
        target["cadence"] = args.cadence.strip()
    if args.persona is not None:
        target["target_persona"] = args.persona.strip()
    if args.sources is not None:
        target["sources"] = [s.strip() for s in args.sources.split(",") if s.strip()]
    if args.angles is not None:
        target["primary_angles"] = [a.strip() for a in args.angles.split(",") if a.strip()]
    if hasattr(args, "enable_dataforseo") and args.enable_dataforseo is not None:
        target["enable_dataforseo"] = args.enable_dataforseo
    if getattr(args, "news_enabled", None) is not None:
        target["news_enabled"] = args.news_enabled
    if getattr(args, "evergreen_cadence", None) is not None:
        target["evergreen_cadence"] = args.evergreen_cadence.strip()
    if getattr(args, "evergreen_enabled", None) is not None:
        target["evergreen_enabled"] = args.evergreen_enabled

    save_verticals(verticals)
    print(f"Updated vertical '{vid}' successfully.")

    url, _ = get_supabase_creds()
    if url:
        print("  Pushing update to Supabase...")
        push_to_supabase()
    return 0


def delete_vertical(args):
    verticals = load_verticals()
    vid = args.id.strip()
    initial_len = len(verticals)
    verticals = [v for v in verticals if v.get("id") != vid]

    if len(verticals) == initial_len:
        print(f"ERROR: Vertical with ID '{vid}' not found.")
        return 1

    save_verticals(verticals)
    print(f"Deleted vertical '{vid}' successfully.")

    url, _ = get_supabase_creds()
    if url:
        print(f"  Deleting vertical '{vid}' from Supabase...")
        res, err = supabase_request(f"editorial_verticals?id=eq.{vid}", method="DELETE")
        if err:
            print(f"  Warning deleting vertical from Supabase: {err}")
        else:
            print(f"  Successfully deleted '{vid}' from Supabase editorial_verticals.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Manage editorial factory verticals.")
    subparsers = parser.add_subparsers(dest="subcommand")

    # list
    subparsers.add_parser("list", help="List all verticals")

    # add
    p_add = subparsers.add_parser("add", help="Add a new vertical")
    p_add.add_argument("--id", required=True, help="Unique slug ID (e.g. agentic_ai)")
    p_add.add_argument("--label", required=True, help="Display label")
    p_add.add_argument("--cadence", default="30 10 * * 1", help="Cron cadence (default: '30 10 * * 1' — off-peak UTC)")
    p_add.add_argument("--persona", default="eng_leader", help="Target persona ID (e.g. eng_leader)")
    p_add.add_argument("--sources", default="", help="Comma-separated sources")
    p_add.add_argument("--angles", default="", help="Comma-separated primary angles")
    p_add.add_argument("--dataforseo", dest="dataforseo", action="store_true", default=None, help="Enable DataForSEO enrichment")
    p_add.add_argument("--no-dataforseo", dest="dataforseo", action="store_false", help="Disable DataForSEO enrichment to save credits")
    p_add.add_argument("--evergreen-cadence", default="", help="Evergreen pipeline cron cadence (default: none — pick a free slot in the 17:30-20:00 UTC band)")

    # edit
    p_edit = subparsers.add_parser("edit", help="Edit an existing vertical")
    p_edit.add_argument("--id", required=True, help="Vertical ID to edit")
    p_edit.add_argument("--label", help="New display label")
    p_edit.add_argument("--cadence", help="New cron cadence")
    p_edit.add_argument("--persona", help="New target persona ID")
    p_edit.add_argument("--sources", help="New comma-separated sources")
    p_edit.add_argument("--angles", help="New comma-separated primary angles")
    p_edit.add_argument("--dataforseo", dest="dataforseo", action="store_true", default=None, help="Enable DataForSEO enrichment")
    p_edit.add_argument("--no-dataforseo", dest="dataforseo", action="store_false", help="Disable DataForSEO enrichment to save credits")
    p_edit.add_argument("--news-enabled", dest="news_enabled", action="store_true", default=None, help="Switch the news pipeline back on")
    p_edit.add_argument("--no-news", dest="news_enabled", action="store_false", help="Switch the news pipeline off (its cron job is removed on the next sync)")
    p_edit.add_argument("--evergreen-cadence", help="New evergreen cadence ('' clears it)")
    p_edit.add_argument("--evergreen-enabled", dest="evergreen_enabled", action="store_true", default=None, help="Switch the evergreen pipeline on")
    p_edit.add_argument("--no-evergreen", dest="evergreen_enabled", action="store_false", help="Switch the evergreen pipeline off (its cron job is removed on the next sync)")


    # delete
    p_del = subparsers.add_parser("delete", help="Delete a vertical")
    p_del.add_argument("--id", required=True, help="Vertical ID to delete")

    # sync-cal
    subparsers.add_parser("sync-cal", help="Regenerate context/content_calendar.md")

    args = parser.parse_args()
    if args.subcommand == "list" or not args.subcommand:
        list_verticals()
        return 0
    elif args.subcommand == "add":
        return add_vertical(args)
    elif args.subcommand == "edit":
        return edit_vertical(args)
    elif args.subcommand == "delete":
        return delete_vertical(args)
    elif args.subcommand == "sync-cal":
        update_content_calendar(load_verticals())
        return 0


if __name__ == "__main__":
    sys.exit(main())
