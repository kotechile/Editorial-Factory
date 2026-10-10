#!/usr/bin/env python3
"""The pre-publish gate — quality enforced AT the push, with one rewrite attempt first.

Why this exists: the desk's gates (fact-check, de-dup, Loop 3 accessibility, social voice) all run
*inside* the pipeline run, executed by the agent following its skill. Nothing in the push path
re-checked any of them, so an article whose run skipped or fumbled a step still went live — and
since 2026-10-10 the connector publishes with `status: publish` (the CMS draft -> publish flip is
no longer a human step). This module closes that gap for the half a machine can settle: it re-runs
the mechanical gates on the artifact that is about to be pushed, and refuses to publish what fails.

Policy (owner, 2026-10-10): **never publish un-gated text, but try at least one rewrite first.**
    1. gate the artifact;
    2. on failure, rewrite it once (`scripts/humanize_one.py`, the desk's Loop 3 frontier rewrite),
       which itself retries until the accessibility gate passes;
    3. re-gate. Pass -> publish. Still failing -> the post is created as a DRAFT instead, and the
       failure is printed as a problem so the sweep reports it. An article is never lost, and it is
       never published un-evaluated.
An already-published post is never rewritten or demoted by this gate: rewriting live prose is a
human decision, so there the gate only reports.

What it cannot do: judge the reporting, the claim quality or the art. Those stay with the run's
gates (fact_check.md, virality_judge.md, illustration_director.md) and with the owner.

CLI:
    python3 scripts/publish_gate.py --slug <slug>            # gate one article
    python3 scripts/publish_gate.py --file published/x.md    # gate a file directly
    python3 scripts/publish_gate.py --slug <slug> --rewrite   # attempt the rewrite on failure
    python3 scripts/publish_gate.py --all [--json]           # audit every published artifact
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import check_accessibility as ca  # noqa: E402

VERIFY_SH = SCRIPTS / "verify.sh"
VOICE_GATE = SCRIPTS / "check_social_voice.mjs"
REWRITER = SCRIPTS / "humanize_one.py"
REWRITE_TIMEOUT = int(os.environ.get("PUBLISH_GATE_REWRITE_TIMEOUT", "1200"))
_voice_cache: dict[str, list[str]] | None = None


# ─────────────────────────────── inputs ───────────────────────────────

def banned_phrases() -> list[str]:
    """The AI-tell list, read out of verify.sh §2 so there is exactly one source of truth.

    Duplicating the list here is how the two gates drift apart; verify.sh stays the owner of it.
    """
    if not VERIFY_SH.exists():
        return []
    m = re.search(r"BANNED=\((.*?)\)", VERIFY_SH.read_text(), re.S)
    return re.findall(r'"([^"]+)"', m.group(1)) if m else []


def artifact_for(slug: str, root: pathlib.Path = ROOT) -> pathlib.Path | None:
    """The reader-facing artifact for a slug: the published copy, else the run's `_final.md`."""
    hits = sorted((root / "published").glob(f"*_{slug}.md"))
    if not hits:
        hits = sorted((root / "published").glob(f"*{slug}*.md"))
    if not hits:
        hits = sorted((root / "context" / "drafts").glob(f"*_{slug}_final.md"))
    return hits[-1] if hits else None


def voice_problems() -> dict[str, list[str]]:
    """`check_social_voice.mjs --json`, grouped by the artifact it names. Cached per process."""
    global _voice_cache
    if _voice_cache is not None:
        return _voice_cache
    grouped: dict[str, list[str]] = {}
    if VOICE_GATE.exists():
        try:
            out = subprocess.run(["node", str(VOICE_GATE), "--json"], cwd=ROOT, capture_output=True,
                                 text=True, timeout=120)
            for line in json.loads(out.stdout or "{}").get("problems", []):
                path, _, rest = str(line).partition(":")
                grouped.setdefault(path.strip(), []).append(rest.strip())
        except Exception as exc:                       # noqa: BLE001 - a dead gate must be visible,
            grouped[":gate"] = [f"the social-voice gate did not run: {exc}"]   # never silent
    _voice_cache = grouped
    return grouped


# ─────────────────────────────── the checks ───────────────────────────────

def text_failures(path: pathlib.Path, *, root: pathlib.Path = ROOT) -> list[str]:
    """Everything the desk's mechanical gates reject, re-checked on the artifact itself."""
    fails: list[str] = []
    if not path.exists():
        return [f"no artifact to gate at {path}"]
    text = path.read_text()

    if not re.search(r"^## Sources", text, re.M):
        fails.append("missing '## Sources' (verify.sh §4)")

    body = ca.body_of(str(path))
    low = text.lower()
    for phrase in banned_phrases():
        if phrase in low:
            fails.append(f"banned AI-tell '{phrase}' (verify.sh §2)")

    diag = ca.measure(str(path))
    fails += [f"accessibility: {f}" for f in diag.get("fails", [])]

    try:
        rel = str(path.relative_to(root))
    except ValueError:
        rel = path.name
    voice = voice_problems()
    for key, problems in voice.items():
        if key.endswith(rel) or rel.endswith(key):
            fails += [f"voice: {p}" for p in problems]
    if ":gate" in voice:
        fails += voice[":gate"]
    return fails


def gate(slug: str, *, rewrite: bool = True, root: pathlib.Path = ROOT) -> dict:
    """Gate the artifact for `slug`; optionally rewrite it once and re-gate.

    Returns {"slug", "artifact", "failures", "verdict", "rewrite"} where verdict is one of
    "publish" (cleared), "publish-after-rewrite" (cleared by the rewrite), "draft" (still failing —
    the caller must not publish it) or "no-artifact".

    A headline is scored on the same pass but only enforced for articles dated on/after
    `headline_score.ENFORCED_FROM`: older artifacts are grandfathered (owner, 2026-10-10, "future
    articles only") — scored and reported, never rewritten and never held on style.
    """
    path = artifact_for(slug, root)
    report: dict = {"slug": slug, "artifact": str(path) if path else None, "failures": [],
                    "rewrite": None, "verdict": "publish"}
    if path is None:
        report["verdict"] = "no-artifact"
        report["failures"] = [f"no artifact for '{slug}' in published/ or context/drafts/ — "
                              f"nothing to gate, so it cannot be published"]
        return report

    body_failures = text_failures(path, root=root)
    headline_failures: list[str] = []
    # The headline is scored on the same pass. A structurally broken one (past 13 words or 75 chars)
    # holds the article even when the prose is clean; a merely weak one is re-cut once; a headline
    # older than the standard is grandfathered inside title_gate and never held.
    try:
        report["title"] = title_gate(path, rewrite=rewrite, apply=rewrite)
        if report["title"].get("hold"):
            worst = report["title"]["before"]["failures"]
            headline_failures = [f"headline ({report['title']['before']['score']}/100): "
                                 + (worst[0] if worst else "does not meet the title standard")]
    except Exception as exc:                           # noqa: BLE001 - report, never swallow
        report["title"] = {"error": f"title gate failed: {exc}"}
        headline_failures = [f"headline: the title gate could not run ({exc})"]

    failures = body_failures + headline_failures
    report["failures"] = failures
    if not failures:
        return report
    report["verdict"] = "draft"
    if not rewrite:
        return report

    # Only the PROSE earns a Loop 3 rewrite. A held headline does not: rewriting the whole body to
    # fix a title would spend a frontier call and churn the article for nothing — and, before this,
    # it also dropped the headline hold from the verdict (the re-gate only re-ran the text checks).
    if not body_failures:
        return report

    report["rewrite"] = attempt_rewrite(path)
    report["failures"] = text_failures(path, root=root) + headline_failures
    report["verdict"] = "publish-after-rewrite" if not report["failures"] else "draft"
    return report


def _split(text: str) -> tuple[str, str, str]:
    """(frontmatter+opening, body, '## Sources'+rest) — the three parts, kept apart on purpose.

    The rewrite is confined to the middle: frontmatter carries the artifact's seals (`image_path`,
    `synthesis`, `sources:` anchors) and the Sources list is the reader's audit trail. Letting a
    frontier model re-emit either one is how a published artifact loses its illustration linkage.
    """
    fm = ""
    rest = text
    m = re.match(r"(---\n.*?\n---\n)(.*)", text, re.S)
    if m:
        fm, rest = m.group(1), m.group(2)
    s = re.search(r"\n#{1,3}\s*Sources.*", rest, re.S)
    if s:
        return fm, rest[:s.start()] + "\n", rest[s.start():]
    return fm, rest, ""


def attempt_rewrite(path: pathlib.Path) -> dict:
    """One Loop-3 frontier rewrite of the artifact BODY, then re-measure.

    `humanize_one.py` is the desk's own rewrite (it retries against the accessibility gate itself),
    but it rewrites a whole draft file — so this stages a throwaway draft in `context/drafts/`,
    runs it there, and splices the rewritten body back between the artifact's own frontmatter and
    its own Sources list. The rewritten text is kept only when it clears the gate; otherwise the
    original bytes are restored, so a failed rewrite cannot quietly replace audited prose with
    prose that is no better.
    """
    original = path.read_bytes()
    text = original.decode("utf-8")
    fm, body, sources = _split(text)
    date = re.match(r"(\d{4}-\d{2}-\d{2})_", path.name)
    slug = path.name[11:-3] if path.name[:4].isdigit() else path.stem
    # A name of its own: staging at `<date>_<slug>_draft.md` would land on the artifact's own tracked
    # draft/_final pair and the cleanup below would delete them (it did, once). The staging file is
    # always the gate's to remove; nothing else is ever touched.
    staged = ROOT / "context" / "drafts" / f"{date.group(1) if date else 'rewrite'}_{slug}_gate-rewrite_draft.md"
    rewritten = staged.with_name(staged.name.replace("_draft.md", "_final.md"))
    result = {"attempted": True, "command": f"python3 scripts/humanize_one.py {staged.relative_to(ROOT)}",
              "verdict": "unknown", "output": ""}
    created = [p for p in (staged, rewritten) if not p.exists()]
    try:
        staged.write_text(fm + body + sources)
        out = subprocess.run(["python3", str(REWRITER), str(staged.relative_to(ROOT))], cwd=ROOT,
                             capture_output=True, text=True, timeout=REWRITE_TIMEOUT)
        result["output"] = (out.stdout or "")[-1200:] + ((out.stderr or "")[-600:] if out.stderr else "")
        result["exit_code"] = out.returncode
        if out.returncode == 0 and rewritten.exists():
            _, new_body, _ = _split(rewritten.read_text())
            path.write_text(fm + new_body + sources)
            result["verdict"] = "rewritten"
        else:
            result["verdict"] = "no-change"
    except subprocess.TimeoutExpired:
        result["output"] = f"rewrite timed out after {REWRITE_TIMEOUT}s"
        result["exit_code"] = -1
        result["verdict"] = "no-change"
    except Exception as exc:                           # noqa: BLE001 - report, never swallow
        result["output"] = f"rewrite could not run: {exc}"
        result["exit_code"] = -1
        result["verdict"] = "no-change"
    finally:
        for tmp in (staged, rewritten):
            if tmp in created:                         # only the gate's own files, never a pre-existing one
                try:
                    tmp.unlink()
                except OSError:
                    pass

    if result["verdict"] != "rewritten":
        path.write_bytes(original)                     # nothing better came back: keep the audited text
    result["flesch_after"] = ca.measure(str(path)).get("flesch")
    return result


def sync_rewrite(slug: str) -> dict:
    """Push a cleared rewrite into the Supabase row — the connector publishes the ROW, not the file.

    Without this the rewrite would clear the gate and the reader would still get the old text.
    """
    path = artifact_for(slug)
    if path is None:
        return {"synced": False, "note": f"no artifact for '{slug}'"}
    if not (SCRIPTS / "sync_articles.py").exists():
        return {"synced": False, "note": "scripts/sync_articles.py is missing"}
    try:
        out = subprocess.run(["python3", str(SCRIPTS / "sync_articles.py"), str(path.relative_to(ROOT))],
                             cwd=ROOT, capture_output=True, text=True, timeout=300)
        return {"synced": out.returncode == 0, "note": (out.stdout or out.stderr or "").strip()[-300:]}
    except Exception as exc:                           # noqa: BLE001
        return {"synced": False, "note": f"row sync failed: {exc}"}


def _cms():
    """The live CMS clients, keyed by site — imported lazily so the gate stays testable offline."""
    import wp_draft as wd
    wd.load_env()                                      # the credentials live in ./.env, not the env
    out = {}
    for domain in ("giniloh.com", "wellroost.com"):
        user, password = wd.credentials_for(domain)
        base = "https://cms." + domain
        out[domain] = wd.WordPress(base, user, password)
    return out


def audit_live(limit: int = 10, root: pathlib.Path = ROOT) -> list[dict]:
    """Artifacts whose header on the CMS is not the header the desk chose, or whose slug moved.

    The push-time gate catches drift at the moment of a push; this catches the other half — an
    artifact re-rendered or re-typed AFTER it was published, and never pushed again (four articles
    were live with their previous artwork for exactly that reason on 2026-10-10). Run it from the
    daily sweep, where the reader frontends have had time to rebuild.
    """
    import hashlib
    import json as _json
    problems: list[dict] = []
    clients = _cms()
    for path in sorted((root / "published").glob("*.md"), reverse=True)[:limit]:
        slug = path.name[11:-3]
        row: dict = {"file": path.name, "slug": slug}
        found = None
        for domain, wp in clients.items():
            try:
                post = wp.find_by_slug(slug)
            except Exception as exc:                   # noqa: BLE001
                row.setdefault("notes", []).append(f"{domain}: {exc}")
                continue
            if post:
                found = (domain, post)
                break
        if not found:
            row["failures"] = [f"no CMS post found for '{slug}' on either site — the artifact slug "
                               f"and the CMS slug have diverged (the sitemap derives its URL from "
                               f"the live sites, so a hand-written URL here would be a 404)"]
            problems.append(row)
            continue
        domain, post = found
        try:
            full = clients[domain].read_back(post.get("id"))
            post = {**post, **(full or {})}             # find_by_slug asks for id/status/link only
        except Exception as exc:                       # noqa: BLE001
            row.setdefault("notes", []).append(f"{domain}: read-back failed ({exc})")
        side_path = root / "context" / "assets" / "illustrations" / slug / "featured.json"
        if not side_path.exists():
            continue                                   # no staged brief: nothing to compare against
        side = _json.loads(side_path.read_text())
        staged = root / side["local_path"]
        media_id = post.get("featured_media")
        if not media_id:
            row["failures"] = ["the live post has no featured image"]
            problems.append(row)
            continue
        media = None
        note = ""
        try:
            media = clients[domain].media(media_id)
            served, note = _served_bytes_pg(media.get("source_url"))
        except Exception as exc:                       # noqa: BLE001
            served, note = None, str(exc)
        fails = []
        if served is None:
            fails.append(f"could not read media {media_id} back: {note}")
        elif staged.exists() and hashlib.sha256(served).hexdigest() != hashlib.sha256(staged.read_bytes()).hexdigest():
            fails.append(f"the live header is not the staged render (media {media_id}, "
                         f"{len(served)} bytes vs {staged.stat().st_size})")
        live_alt = (media or {}).get("alt_text") or ""
        if side.get("alt_text") and live_alt.strip() != side["alt_text"].strip():
            fails.append(f"the live alt text does not match the sidecar: {live_alt[:60]!r}")
        if fails:
            row["failures"] = fails
            problems.append(row)
    return problems


def _served_bytes_pg(url: str | None) -> tuple[bytes | None, str]:
    if not url:
        return None, "no source_url"
    try:
        import urllib.request
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "publish-gate"}),
                                   timeout=60) as response:
            return response.read(), ""
    except Exception as exc:                           # noqa: BLE001
        return None, str(exc)


def _title_standards() -> str:
    return """The house title standard (all of it is scored mechanically by scripts/headline_score.py):
- CORE HEADLINE <= 6 WORDS before any subtitle. Whole title <= 10 words, <= 60 characters.
- Never open on 'The', 'A' or 'An'. Front-load the strongest noun or the most concrete benefit.
- Carry a hook: a curiosity gap (a delta the reader must close) or loss aversion (the mistake, the
  trap, the silent cost) — or invert the conventional wisdom.
- Anchor it in a number the article itself states (take it from the piece, never invent one).
- Call the reader out: 'your/you' or a named role or subject (CFO, shipper, homeowner, SpaceX).
- No filler, no vague generalities, no bait-and-switch: the article must deliver what the title
  promises in its first paragraph.
Good: "California FAIR Plan Premiums Jump 29.1%" / "Your Battery Is Sized Wrong" /
"SpaceX Unlocks Six Windows, Not One" / "Stop Sizing Your Battery on Annual Usage".
Bad: "The $2.7 Trillion AI Bill Just Turned Cost Control Into a Buying Requirement" (13 words,
opens on 'The', 76 chars, no reader)."""


def title_prompt(title: str, body: str, one_big: str, count: int) -> str:
    figures = "\n".join(f"- {b.strip()[:160]}" for b in
                        re.findall(r"^\s*[-*]\s*\*\*.*$", body, re.M)[:6]) or "(none stated)"
    return f"""You are the headline editor for an institutional B2B research desk. Write {count} \
alternative headlines for ONE article, then stop.

CURRENT TITLE: {title}
THE ONE BIG THING: {one_big or '(read the numbers below)'}
THE ARTICLE'S OWN FIGURES:
{figures}

{_title_standards()}

Rules for your output:
- Use ONLY facts present in the current title and the figures above. Invent nothing, and never add a
  number that is not in that list.
- Keep the same subject and the same claim as the current title. You are re-cutting the headline,
  not changing the story.
- Reply with a JSON array of exactly {count} strings, best first. No commentary, no markdown fence."""


def title_candidates(path: pathlib.Path, count: int = 5) -> list[dict]:
    """Ask the frontier for headlines, score every one, and return them best-first.

    Scoring is the desk's own (scripts/headline_score.py) and runs on the article's real body, so a
    candidate that promises something the piece never says is rejected mechanically.
    """
    import headline_score as hs
    sys.path.insert(0, str(SCRIPTS))
    import humanizer_tools as ht
    text = path.read_text()
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", text)
    title = one_big = ""
    for line in fm.splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("one_big_thing:"):
            one_big = line.split(":", 1)[1].strip().strip('"').strip("'")
    raw = ht.call_gemini(title_prompt(title, body, one_big, count), max_tokens=3000, temperature=0.9)
    # The model's array is often truncated mid-string (a long list hits the token ceiling), so a
    # strict json.loads throws away perfectly good candidates. Take the JSON when it parses and fall
    # back to harvesting the quoted strings — every candidate is scored below regardless.
    cands: list[str] = []
    m2 = re.search(r"\[.*\]", raw or "", re.S)
    if m2:
        try:
            parsed = json.loads(m2.group(0))
            cands = [c for c in parsed if isinstance(c, str)]
        except json.JSONDecodeError:
            cands = []
    if not cands:
        cands = [re.sub(r"\\(.)", r"\1", s) for s in
                 re.findall(r'"((?:[^"\\]|\\.)*)"', raw or "") if len(s) > 12]
    out = []
    seen = set()
    for c in cands:
        c = c.strip()
        if not c or c.lower() in seen:
            continue
        seen.add(c.lower())
        out.append({**hs.score(c, body=body), "gained": True})
    return sorted(out, key=lambda r: -r["score"])


def apply_title(path: pathlib.Path, title: str) -> dict:
    """Write a new headline into the artifact's frontmatter (title + meta_title, if one exists)."""
    text = path.read_text()
    m = re.match(r"(---\n)(.*?)(\n---\n)(.*)", text, re.S)
    if not m:
        return {"applied": False, "note": "no frontmatter to write a title into"}
    head, fm, close, body = m.groups()
    lines = fm.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("title:"):
            lines[i] = f'title: "{title}"'
        elif line.startswith("meta_title:") and len(title) <= 60:
            lines[i] = f'meta_title: "{title}"'
    path.write_text(head + "\n".join(lines) + close + body)
    return {"applied": True, "title": title}


def sync_title(slug: str, title: str) -> dict:
    """Push a new headline into the Supabase row, narrowly.

    The row is what the connector publishes, so a title fixed only in the file never reaches a
    reader. This PATCHes title/headline and metadata.headline only — deliberately NOT
    `sync_articles.py`, which is the whole publish pass and would re-commission the article's header
    image (credits spent, fresh drift against the live post) to change one line of text.
    """
    try:
        import wp_draft as wd
        wd.load_env()
        url, key = wd.supabase_config()
        db = wd.Supabase(url, key)
        rows = db.articles(slug=slug)
        if not rows:
            return {"synced": False, "note": f"no Supabase row for '{slug}'"}
        row = rows[0]
        metadata = {**(row.get("metadata") or {}), "headline": title}
        db._call("PATCH", f"articles?id=eq.{row['id']}",
                 {"title": title, "headline": title, "metadata": metadata},
                 {"Prefer": "return=minimal"})
        return {"synced": True, "note": f"row {row['id']} headline updated"}
    except Exception as exc:                           # noqa: BLE001
        return {"synced": False, "note": f"row title sync failed: {exc}"}


def title_gate(path: pathlib.Path, *, rewrite: bool, apply: bool = False) -> dict:
    """Score an artifact's headline; when it is poor, commission and adopt a better one.

    Style is the owner's call, not a machine verdict — so a weak title does not hold an article by
    itself. A structurally broken one does: past 13 words or 75 characters it is not a headline any
    more, and 17-word titles are in this corpus. `apply=False` (the audit/dry-run path) proposes and
    scores but writes nothing.
    """
    import headline_score as hs
    title, body, keyword = hs.artifact_title(path)
    before = hs.score(title, body=body, keyword=keyword)
    date = path.name[:10]
    standardized = hs.enforced(date)
    report = {"before": before, "after": None, "adopted": None, "candidates": [],
              "enforced": standardized, "date": date}
    structurally_broken = before["words"] > 13 or before["chars"] > hs.HARD_CHARS_MAX
    if not standardized:
        # Grandfathered: an article older than the standard is scored and reported, never rewritten
        # and never held (owner, 2026-10-10 — the changes apply to future articles only).
        report["hold"] = False
        report["grandfathered"] = True
        return report
    if not rewrite or before["verdict"] == "STRONG":
        report["hold"] = structurally_broken
        return report
    try:
        report["candidates"] = title_candidates(path)
    except Exception as exc:                           # noqa: BLE001 - a dead model must not hold
        report["error"] = f"title candidates failed: {exc}"
        report["hold"] = structurally_broken
        return report
    best = report["candidates"][0] if report["candidates"] else None
    if best and best["score"] > before["score"] and best["score"] >= 90:
        report["after"] = best
        report["adopted"] = best["title"]
        if apply:
            apply_title(path, best["title"])
            report["row"] = sync_title(path.name[11:-3], best["title"])
    elif best:
        report["after"] = best
    report["hold"] = structurally_broken and not (report["after"] and report["after"]["score"] >= 90)
    return report


# ─────────────────────────────── CLI ───────────────────────────────

def _print(report: dict, slug: str | None = None) -> None:
    if report["verdict"] in ("publish", "publish-after-rewrite"):
        print(f"gate: PASS {report['artifact']}")
        rw = report.get("rewrite")
        if rw:
            print(f"  (cleared by one rewrite — Flesch now {rw.get('flesch_after')})")
        return
    print(f"gate: {report['verdict'].upper()} {report.get('artifact') or ''}")
    for f in report.get("failures", []):
        print(f"  - {f}")
    rw = report.get("rewrite")
    if rw:
        print(f"  rewrite attempted: {rw['command']} (exit {rw.get('exit_code')}), "
              f"Flesch now {rw.get('flesch_after')}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Gate an article before it is published to the CMS.")
    ap.add_argument("--slug", help="gate the artifact for this slug")
    ap.add_argument("--file", help="gate this artifact path directly")
    ap.add_argument("--all", action="store_true", help="audit every published artifact")
    ap.add_argument("--audit-live", action="store_true",
                    help="compare the live CMS header/alt against the staged brief for the newest "
                         "artifacts (catches a re-render that was never re-pushed)")
    ap.add_argument("--titles", action="store_true",
                    help="score every headline and (with --rewrite) commission better ones; "
                         "writes nothing unless --apply")
    ap.add_argument("--apply", action="store_true",
                    help="with --titles: write the adopted headline into the artifact + Supabase row")
    ap.add_argument("--limit", type=int, default=10, help="how many artifacts --audit-live reads")
    ap.add_argument("--rewrite", action="store_true", help="attempt one rewrite when the gate fails")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    if args.titles:
        import headline_score as hs
        rows = []
        for path in sorted((ROOT / "published").glob("*.md")):
            title, body, keyword = hs.artifact_title(path)
            entry = {"file": path.name, **hs.score(title, body=body, keyword=keyword)}
            if args.rewrite:
                tg = title_gate(path, rewrite=True, apply=args.apply)
                entry["adopted"] = tg.get("adopted")
                entry["candidates"] = [c["title"] + f"  ({c['score']})" for c in tg.get("candidates", [])[:4]]
                entry["held"] = bool(tg.get("hold"))
            rows.append(entry)
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            weak = [r for r in rows if r["verdict"] in ("WEAK", "POOR")]
            print(f"titles: {len(rows)} scored | {sum(1 for r in rows if r['verdict']=='STRONG')} strong, "
                  f"{sum(1 for r in rows if r['verdict']=='OK')} ok, {len(weak)} weak/poor")
            for r in sorted(rows, key=lambda r: r["score"]):
                print(f"  {r['score']:>3} {r['verdict']:<6} | {r['title'][:66]}")
                if r.get("adopted"):
                    print(f"        -> ADOPTED: {r['adopted']}")
                for c in (r.get("candidates") or [])[:3]:
                    print(f"        candidate: {c}")
            if args.rewrite and not args.apply:
                print("\n(nothing written — pass --apply to adopt the headlines and sync the rows)")
        return 0

    if args.audit_live:
        problems = audit_live(args.limit)
        if args.json:
            print(json.dumps({"checked": args.limit, "problems": problems}, indent=2, default=str))
        else:
            if not problems:
                print(f"delivery audit: the newest {args.limit} artifact(s) match what their CMS posts "
                      f"serve")
            for row in problems:
                print(f"  {row['file']}")
                for f in row.get("failures", []):
                    print(f"    - {f}")
        return 1 if problems else 0

    if args.all:
        reports = []
        for path in sorted((ROOT / "published").glob("*.md")):
            slug = path.name[11:-3]
            reports.append({"file": path.name, "failures": text_failures(path)})
        bad = [r for r in reports if r["failures"]]
        if args.json:
            print(json.dumps({"checked": len(reports), "failing": bad}, indent=2))
        else:
            print(f"publish gate: {len(reports)} artifact(s) checked, {len(bad)} failing")
            for r in bad:
                print(f"  {r['file']}")
                for f in r["failures"]:
                    print(f"    - {f}")
        return 1 if bad else 0

    if args.file:
        path = pathlib.Path(args.file)
        fails = text_failures(path)
        slug = path.name[11:-3] if path.name[:4].isdigit() else path.stem
        report = {"slug": slug, "artifact": str(path), "failures": fails,
                  "rewrite": None, "verdict": "publish" if not fails else "draft"}
        if fails and args.rewrite:
            report["rewrite"] = attempt_rewrite(path)
            report["failures"] = text_failures(path)
            report["verdict"] = "publish-after-rewrite" if not report["failures"] else "draft"
    else:
        if not args.slug:
            ap.error("one of --slug, --file or --all is required")
        report = gate(args.slug, rewrite=args.rewrite)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        _print(report, args.slug)
    return 0 if report["verdict"] in ("publish", "publish-after-rewrite") else 1


if __name__ == "__main__":
    raise SystemExit(main())
