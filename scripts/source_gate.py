#!/usr/bin/env python3
"""Source gate — the code-enforced accuracy and quality floor for an article's citations.

Why this exists (owner, 2026-10-23): a review pass caught articles whose sources did not support
them — a citation that no longer resolves, a page that is not the document it is cited as, an
aggregator repeating another outlet's reporting, five pages of one vendor's site counted as five
sources — and those articles were dropped by hand. A standard that lives only in a review is a
standard that lasts until the next busy day, so the floor lives here and runs at the push
(`scripts/publish_gate.py`), which means an article that fails it is HELD as a CMS draft instead of
being published.

What it decides (blocking — the article is dropped, never softened):
  * `## Sources` names at least `min_sources` sources across at least `min_hosts` distinct hosts
    (three pages of one vendor's site is one source wearing a costume);
  * every cited URL resolves to a page that actually is the one cited — the citation's own label
    (its statute number, its title words) has to appear on the page it points at, so a link that
    redirects to a homepage, a paywall stub or the wrong document is caught rather than trusted;
  * no cited source is an aggregator, mirror, social post or tertiary wiki
    (`context/source_quality.json`), and at least one source is PRIMARY (the regulator, the
    statute, the paper, the vendor's own page);
  * a sources list made only of press-release wires is not corroboration and fails.
What it reports and does NOT block (the number-level judgement a machine cannot make):
  * every figure in the body that appears in NO cited source, printed as the list a reviewer reads
    first. Derived arithmetic (a spread, a sum, an interval) legitimately never appears in a source,
    so this cannot be a mechanical hold — `--strict-figures` makes it one for a deliberate audit.

Grandfathering is the house convention: artifacts dated before `enforced_from` are scored and
reported, never held (the standard applies to future articles only).

Usage
  python3 scripts/source_gate.py --slug <slug>          # one article (published/ then drafts/)
  python3 scripts/source_gate.py --file <artifact.md>
  python3 scripts/source_gate.py --all [--json]        # corpus read-out
  python3 scripts/source_gate.py --last 5              # the most recent N artifacts
  python3 scripts/source_gate.py --self-test           # rules pinned, no network
  --no-network / SOURCE_GATE_NO_NETWORK=1              # shape checks only; live checks reported as unrun
  --strict-figures                                     # unsupported figures become blocking

Exit codes: 0 = pass (or grandfathered), 1 = held, 2 = usage error.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "context" / "source_quality.json"
USER_AGENT = ("Mozilla/5.0 (compatible; editorial-factory source gate; "
              "+https://giniloh.com) Python-urllib")
FETCH_TIMEOUT = int(os.environ.get("SOURCE_GATE_TIMEOUT", "20"))
DEFAULT_ENFORCED_FROM = "2026-10-24"

STOPWORDS = {
    "the", "and", "for", "with", "from", "that", "this", "into", "about", "over", "under", "your",
    "their", "its", "its", "are", "was", "were", "has", "have", "not", "but", "you", "our", "what",
    "when", "which", "how", "why", "who", "will", "can", "may", "more", "than", "only", "also",
    "page", "site", "official", "website", "home", "index", "html", "https", "http", "www", "com",
    "org", "gov", "edu", "section", "title", "part", "chapter", "press", "release", "news",
}


# ───────────────────────────── registry ─────────────────────────────

def load_registry(path: pathlib.Path = REGISTRY) -> dict:
    """The host tiers and floors. A missing registry is an error, never a silent pass."""
    data = json.loads(path.read_text())
    for key in ("primary_suffixes", "primary_hosts", "blocked_hosts", "min_sources", "min_hosts"):
        if key not in data:
            raise SystemExit(f"source_quality.json is missing '{key}' — the gate cannot guess a floor")
    data.setdefault("press_release_hosts", [])
    data.setdefault("enforced_from", DEFAULT_ENFORCED_FROM)
    return data


def host_of(url: str) -> str:
    m = re.match(r"^[a-zA-Z]+://([^/?#]+)", url or "")
    host = (m.group(1) if m else (url or "").split("/")[0]).lower()
    return re.sub(r":\d+$", "", host).lstrip(".")


def _host_match(host: str, needles: list[str]) -> bool:
    return any(host == h or host.endswith("." + h) for h in needles)


def tier_of(host: str, reg: dict) -> str:
    """primary | press_release | blocked | unclassified."""
    if _host_match(host, reg["blocked_hosts"]):
        return "blocked"
    if _host_match(host, reg["primary_hosts"]):
        return "primary"
    if any(host.endswith(sfx) for sfx in reg["primary_suffixes"]):
        return "primary"
    if _host_match(host, reg["press_release_hosts"]):
        return "press_release"
    return "unclassified"


# ───────────────────────────── parsing ─────────────────────────────

def split_artifact(text: str) -> tuple[str, str, str]:
    """(frontmatter, body, sources-block). The sources block runs to EOF."""
    fm = ""
    rest = text
    m = re.match(r"(---\n.*?\n---\n)(.*)", text, re.S)
    if m:
        fm, rest = m.group(1), m.group(2)
    s = re.search(r"\n#{1,3}[ \t]*Sources[ \t]*\n", rest, re.I)
    if s:
        return fm, rest[: s.start()] + "\n", rest[s.start():]
    return fm, rest, ""


def parse_sources(block: str) -> list[dict]:
    """`[1] Label. https://url` (and the bare `Label — https://url` shape) -> records."""
    out: list[dict] = []
    for line in block.splitlines():
        line = line.strip()
        m = re.match(r"^(?:\[(\d+)\]|[-*]\s*)?\s*(.*?)\s*<?(https?://[^\s>)]+)>?", line)
        if not m or not m.group(3):
            continue
        label = m.group(2).strip(" .—-–:")
        out.append({"n": int(m.group(1)) if m.group(1) else len(out) + 1,
                    "label": re.sub(r"\s+", " ", label), "url": m.group(3).rstrip(".,;")})
    return out


def body_for_figures(body: str) -> str:
    """The claim-bearing body only: no frontmatter, no generated link block, no markers."""
    text = re.sub(r"<!--.*?-->", " ", body, flags=re.S)
    text = re.sub(r"\n#{1,3}[ \t]*(Related reading|Sources).*", "\n", text, flags=re.S | re.I)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return text


FIG_RE = re.compile(
    r"(?:(?P<cur>[$£€])\s?)?(?<![\w.])(?P<num>\d[\d,]*(?:\.\d+)?)\s?"
    r"(?P<unit>%|percent|per cent|bps|basis points|x\b|×|billion|million|trillion|thousand|"
    r"dollars?|usd|euros?|cents?|"
    r"kWh|MWh|GWh|GW|MW|kW|GB|TB|MB|KB|ms\b|days?|weeks?|months?|years?|hours?|hrs?|minutes?|"
    r"tokens?|words?|orders?|points?|percent)", re.I)


def figures_in(body: str) -> list[str]:
    """Load-bearing figures as normalised numbers, with the raw text kept for the report.

    A figure counts when it carries a currency mark, a unit word, or a thousands separator: those
    are the numbers a reader treats as measured. Bare small integers (a list index, a "3 things"
    count) are prose, and holding on them would be noise.
    """
    text = body_for_figures(body)
    found: list[str] = []
    seen: set[str] = set()
    for m in FIG_RE.finditer(text):
        raw = m.group(0).strip()
        num = _norm_num(m.group("num"))
        if not num or num in seen:
            continue
        if not m.group("cur") and not m.group("unit") and "," not in m.group("num"):
            continue
        seen.add(num)
        found.append(f"{num}|{raw}")
    return found


def _norm_num(num: str) -> str:
    n = (num or "").replace(",", "").strip()
    if n.endswith(".0"):
        n = n[:-2]
    return n


def _norm_text(text: str) -> str:
    text = (text or "").replace("\u00a0", " ").replace("\u2019", "'")
    return re.sub(r"\s+", " ", text).lower()


def _tokens(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", text or "")
            if w.lower() not in STOPWORDS]


def identity_tokens(url: str, label: str) -> tuple[list[str], list[str]]:
    """(distinctive words, numbers) that a page must carry to be the document it is cited as.

    The URL path is the better witness than the label: a `## Sources` line is often just the URL,
    and a slug like `sunrun-leads-record-grid-dispatch` names the document. The label is added on
    top when the artifact carries one. Numbers cover statute sections and report ids.
    """
    path = re.sub(r"^[a-zA-Z]+://[^/]+", "", url or "")
    path = re.sub(r"[?#].*$", "", path)
    slug_words = _tokens(re.sub(r"[-_/.]", " ", path))
    label_words = _tokens(label)
    words = sorted(set(slug_words) | set(label_words))
    nums = set(re.findall(r"\b\d{3,5}\b", (label or "") + " " + path))
    return words, sorted(nums)


def identity_check(url: str, label: str, page: str) -> tuple[bool | None, str]:
    """Is the fetched page the document the citation names?

    `None` means there was nothing distinctive enough to test (a root path, a two-letter slug) —
    reported as unverifiable rather than passed, so the gate never claims a check it did not run.
    """
    page_n = _norm_text(page)
    if not page_n:
        return False, "the page carried no readable text"
    words, nums = identity_tokens(url, label)
    page_c = page_n.replace(",", "")
    for num in nums:
        if num in page_c:
            return True, f"its number {num} is on the page"
    if len(words) >= 2:
        hits = [w for w in words if w in page_n]
        if len(hits) >= 2:
            return True, f"{len(hits)} of the citation's words are on the page ({', '.join(sorted(hits)[:4])})"
        return False, (f"only {len(hits)} of the citation's {len(words)} distinctive words are on "
                       f"the page ({', '.join(sorted(words)[:6])}) — the link is not the document "
                       f"it is cited as")
    if len(words) == 1:
        return (words[0] in page_n), (f"its only distinctive word '{words[0]}' "
                                      f"{'is' if words[0] in page_n else 'is NOT'} on the page")
    return None, "the citation names nothing distinctive enough to check against the page"


# ───────────────────────────── fetching ─────────────────────────────

BROWSER_UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/124.0.0.0 Safari/537.36")


def _fetch_once(url: str, ua: str, timeout: int) -> dict:
    """One retrieval with one User-Agent. Never raises — a failure is a result, not an exception."""
    req = urllib.request.Request(
        url, headers={"User-Agent": ua,
                      "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            status = resp.status
            ctype = (resp.headers.get("Content-Type") or "").lower()
            final_url = resp.geturl()
    except urllib.error.HTTPError as exc:
        return {"status": "unreachable", "http": str(exc.code),
                "reason": f"HTTP {exc.code} {exc.reason}", "text": ""}
    except Exception as exc:                            # noqa: BLE001 - a dead link is a result
        return {"status": "unreachable", "http": "", "reason": str(exc), "text": ""}
    if status != 200:
        return {"status": "unreachable", "http": str(status), "reason": f"HTTP {status}", "text": ""}
    text = ""
    if "pdf" in ctype or url.lower().endswith(".pdf") or raw[:4] == b"%PDF":
        text = _pdf_text(raw)
    else:
        text = _html_text(raw.decode("utf-8", "replace"))
    return {"status": "ok", "http": str(status), "reason": "", "text": text,
            "final_url": final_url, "bytes": len(raw)}


def fetch(url: str, timeout: int = FETCH_TIMEOUT) -> dict:
    """Retrieve one cited source, retrying a 404/410 once as a browser would.

    Some hosts answer the desk's own User-Agent with a 404 while serving the very same page to a
    browser (observed 2026-10-29 on about.usps.com: three agency releases, all 404 to the gate and
    all 200 to a Chrome User-Agent). A citation a reader can open is not a dead citation, and the
    404 is not distinguishable from a real one by status alone — so the retry decides it. A genuine
    404 stays 404 under both User-Agents and is still held. The retry is reported, never silent.
    """
    res = _fetch_once(url, USER_AGENT, timeout)
    if res.get("status") != "ok" and str(res.get("http")) in ("404", "410", "451"):
        browser = _fetch_once(url, BROWSER_UA, timeout)
        if browser.get("status") == "ok":
            browser["via"] = "browser-ua-retry"
            browser["note"] = (f"HTTP {res.get('http')} to the desk User-Agent, 200 to a browser "
                               f"User-Agent — bot-walled, not dead")
            return browser
        return browser
    return res


def _html_text(body: str) -> str:
    import html
    text = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", body)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text).replace("\u00a0", " ")).strip()


def _pdf_text(raw: bytes) -> str:
    """Best-effort PDF text: enough to prove a figure or a section number is on the page."""
    try:
        import io
        from pypdf import PdfReader            # optional; absent in some hosts
        reader = PdfReader(io.BytesIO(raw))
        return re.sub(r"\s+", " ", " ".join((p.extract_text() or "") for p in reader.pages[:40]))
    except Exception:                          # noqa: BLE001
        return re.sub(rb"[^\x20-\x7e]+", b" ", raw[:800_000]).decode("latin-1", "replace")


# ───────────────────────────── the gate ─────────────────────────────

def artifact_date(path: pathlib.Path) -> date | None:
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", path.name)
    if not m:
        return None
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def enforced_for(path: pathlib.Path, reg: dict) -> bool:
    """Grandfathering by date — the owner's convention for every new standard."""
    d = artifact_date(path)
    if d is None:
        return True                        # a file named nothing like an artifact is not grandfathered
    try:
        since = date.fromisoformat(str(reg.get("enforced_from", DEFAULT_ENFORCED_FROM)))
    except ValueError:
        return True
    return d >= since


def gate(path: pathlib.Path, *, fetch_fn=fetch, reg: dict | None = None,
         no_network: bool = False, strict_figures: bool = False) -> dict:
    """Score one artifact. `ok` is the hold decision; `blocking` says why."""
    reg = reg or load_registry()
    report: dict = {"artifact": str(path), "slug": path.stem, "ok": True, "hold": False,
                    "blocking": [], "notes": [], "sources": [],
                    "figures": {"checked": 0, "unsupported": []},
                    "counts": {}, "enforced": enforced_for(path, reg), "verdict": "pass"}
    if not path.exists():
        report.update(ok=False, blocking=[f"no artifact at {path}"], verdict="held")
        return report
    fm, body, block = split_artifact(path.read_text())
    sources = parse_sources(block)
    if not sources:
        report["blocking"].append("the artifact carries no parseable '## Sources' entries "
                                  "([n] Label. https://url) — a claim with no retrievable source "
                                  "is not publishable (AGENTS.md rule 3)")
    hosts = sorted({host_of(s["url"]) for s in sources})
    report["counts"] = {"sources": len(sources), "hosts": len(hosts)}
    if sources and len(sources) < reg["min_sources"]:
        report["blocking"].append(f"{len(sources)} cited source(s); the floor is {reg['min_sources']}")
    if sources and len(hosts) < reg["min_hosts"]:
        report["blocking"].append(f"{len(hosts)} distinct host(s) ({', '.join(hosts)}); "
                                  f"the floor is {reg['min_hosts']} — one site citing itself is "
                                  f"one source wearing a costume")
    tiers: dict[str, int] = {}
    for s in sources:
        host = host_of(s["url"])
        tier = tier_of(host, reg)
        tiers[tier] = tiers.get(tier, 0) + 1
        s.update(host=host, tier=tier, status="unchecked", label_found=None, check="")
        if tier == "blocked":
            report["blocking"].append(f"[{s['n']}] {host} is an aggregator/mirror/social/tertiary "
                                      f"source — it repeats reporting without the provenance a "
                                      f"claim needs; cite the origin it repeats")
    if sources and not tiers.get("primary"):
        report["notes"].append("no PRIMARY host among the citations (a regulator, statute, paper, "
                               "court filing or a registry-listed vendor page) — confirm at "
                               "least one citation is the source of record, not a writeup of it")
    if sources and len(sources) >= reg["min_sources"] and \
            tiers.get("press_release", 0) == len(sources):
        report["blocking"].append("every citation is a press-release wire — a release is the "
                                  "company's own claim, not corroboration of it")

    if no_network:
        report["notes"].append("live source checks were skipped (--no-network); reachability, "
                               "page identity and figure support are UNVERIFIED in this run")
    else:
        _live_checks(sources, fetch_fn)

    for s in sources:
        if s["status"] == "dead":
            report["blocking"].append(f"[{s['n']}] {s['url']} does not resolve ({s['check']}) — a "
                                      f"citation a reader cannot open is not a citation")
        elif s["status"] == "moved":
            report["blocking"].append(f"[{s['n']}] {s['url']} now lands on {s['final_url']} "
                                      f"({s['check']}) — the link is not the document it is cited as")
        elif s["status"] == "ok" and s["identity"] is False:
            report["blocking"].append(f"[{s['n']}] {s['url']}: {s['check']}")
        elif s["status"] == "ok" and s["identity"] is None:
            report["notes"].append(f"[{s['n']}] {s['url']}: {s['check']} — identity unverified")
        elif s["status"] == "gated":
            report["notes"].append(f"[{s['n']}] {s['url']} could not be fetched from this host "
                                   f"({s['check']}) — the citation is UNVERIFIED, not wrong; a "
                                   f"reader's browser is not subject to the bot wall")
        if s["tier"] == "unclassified" and s.get("status") == "ok":
            report["notes"].append(f"[{s['n']}] {s['host']} is not in the host registry; classified "
                                   f"unclassified (allowed, but add it if it is a source of record)")

    figs = figures_in(body)
    corpus = _norm_text(" ".join(s.get("text", "") for s in sources)).replace(",", "")
    unsupported = []
    for entry in figs:
        num, raw = entry.split("|", 1)
        if num and num not in corpus:
            unsupported.append(raw)
    report["figures"] = {"checked": len(figs), "unsupported": unsupported}
    if unsupported:
        (report["blocking"] if strict_figures else report["notes"]).append(
            f"{len(unsupported)} figure(s) in the body appear in no cited source: "
            + ", ".join(unsupported[:12]) + (" …" if len(unsupported) > 12 else "")
            + ("" if strict_figures else " — derived arithmetic is legitimate, so this is the list "
                                         "the accuracy review reads, not a mechanical hold "
                                         "(--strict-figures makes it one)"))

    if report["blocking"]:
        report["ok"] = False
        report["hold"] = report["enforced"]
        report["verdict"] = "held" if report["enforced"] else "grandfathered"
        if not report["enforced"]:
            report["notes"].append(
                f"dated before {reg['enforced_from']} — scored and reported, never held "
                f"(the standard applies to future articles only)")
    return report


GATED_HTTP = {"401", "403", "406", "408", "429", "503"}
DEAD_HTTP = {"404", "410", "451"}


def _path_of(url: str) -> str:
    return re.sub(r"[?#].*$", "", re.sub(r"^[a-zA-Z]+://[^/]+", "", url or "")).rstrip("/")


def _live_checks(sources: list[dict], fetch_fn) -> None:
    """Fetch each citation and classify it: ok | dead | gated | moved | unreadable.

    The split matters: a bot wall (Reuters answers 403 to any scraper) is not a broken citation,
    while a URL whose path has collapsed to the homepage IS the failure this gate exists to catch.
    Only `dead` and `moved` and a failed identity check are blocking.
    """
    def one(s: dict) -> None:
        try:
            res = fetch_fn(s["url"])
        except Exception as exc:                        # noqa: BLE001
            res = {"status": "unreachable", "reason": f"fetch raised {exc}", "text": ""}
        s["http"] = res.get("http", "")
        s["final_url"] = res.get("final_url") or s["url"]
        s["text"] = res.get("text", "")
        s["identity"] = None
        http = str(s["http"])
        if res.get("status") != "ok":
            if http in DEAD_HTTP:
                s["status"], s["check"] = "dead", res.get("reason") or f"HTTP {http}"
            elif http in GATED_HTTP or http.startswith("5") or not http:
                s["status"], s["check"] = "gated", res.get("reason") or "no response"
            else:
                s["status"], s["check"] = "gated", res.get("reason") or f"HTTP {http}"
            return
        cited, landed = _path_of(s["url"]), _path_of(s["final_url"])
        if cited and cited not in ("/", "") and landed in ("", "/"):
            s["status"], s["check"] = "moved", "the path collapsed to the site's root"
            return
        if len(s["text"]) < 200:
            # A JS shell, a PDF with no text layer or a paywall stub — unverifiable, not wrong on
            # its face. Reported; only an identity failure blocks.
            s["status"] = "gated"
            s["check"] = f"only {len(s['text'])} characters of readable text (JS shell or paywall)"
            return
        ok, why = identity_check(s["url"], s["label"], s["text"])
        s["identity"] = ok
        s["check"] = why
        if res.get("note"):
            s["check"] = f"{why} | {res['note']}" if why else res["note"]
        s["status"] = "ok"

    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(one, sources))


# ───────────────────────────── CLI ─────────────────────────────

def artifact_for(slug: str, root: pathlib.Path = ROOT) -> pathlib.Path | None:
    for pattern in (f"*_{slug}.md", f"*{slug}*.md"):
        hits = sorted((root / "published").glob(pattern))
        if hits:
            return hits[-1]
    hits = sorted((root / "context" / "drafts").glob(f"*_{slug}_final.md"))
    return hits[-1] if hits else None


def print_report(report: dict, verbose: bool = True) -> None:
    name = pathlib.Path(report["artifact"]).name
    state = {"pass": "PASS", "held": "HELD", "grandfathered": "GRANDFATHERED"}[report["verdict"]]
    c = report.get("counts", {})
    print(f"{state}: {name}  ({c.get('sources', 0)} sources / {c.get('hosts', 0)} hosts)")
    if not verbose:
        return
    for s in report.get("sources", []):
        print(f"  [{s['n']}] {s['tier']:<13} {s['status']:<11} {s['host']:<28} {s['check'][:90]}")
    f = report.get("figures", {})
    print(f"  figures: {f.get('checked', 0)} checked, {len(f.get('unsupported', []))} not found "
          f"in any cited source")
    for b in report.get("blocking", []):
        print(f"  BLOCK  {b}")
    for n in report.get("notes", []):
        print(f"  note   {n}")


def self_test() -> int:
    """Offline: the rules are pinned here, so a refactor cannot quietly loosen the floor."""
    reg = {"primary_suffixes": [".gov"], "primary_hosts": ["arxiv.org", "github.com"],
           "blocked_hosts": ["news.google.com", "reddit.com"], "min_sources": 2, "min_hosts": 2,
           "press_release_hosts": ["prnewswire.com"], "enforced_from": "2026-10-24"}
    pages = {
        "https://www.ecfr.gov/current/title-26/section-1.1091-1":
            "26 CFR 1.1091-1 Losses from wash sales of stock or securities. The 30 day period "
            "prohibits a deduction of 1,200 dollars when 26 replaced shares are acquired.",
        "https://www.irs.gov/taxtopics/tc409":
            "Topic no. 409 Capital gains and losses. Report 1,200 dollars of loss on Form 1040.",
        "https://example.com/blog/post": "A blog post that says some things about taxes and 1,200.",
        "https://other.example/post": "An unrelated page about garden sheds and 55 percent.",
        "https://news.google.com/articles/abc": "Aggregated headline linking out to a wire story.",
        "https://prnewswire.com/release": "Company announces 26 new seats in a press release.",
    }

    def fetch_fn(url):
        if url == "https://dead.example/gone":
            return {"status": "unreachable", "http": "404", "reason": "HTTP 404 Not Found", "text": ""}
        if url == "https://gated.example/paywalled":
            return {"status": "unreachable", "http": "403", "reason": "HTTP 403 Forbidden", "text": ""}
        if url == "https://moved.example/old-report":
            return {"status": "ok", "http": "200", "text": "Home page of a news site. " * 20,
                    "final_url": "https://moved.example/"}
        if url == "https://news.google.com/articles/abc":
            return {"status": "ok", "http": "200", "text": pages[url] * 4, "final_url": url}
        if url == "https://prnewswire.com/release":
            return {"status": "ok", "http": "200", "text": pages[url] * 4, "final_url": url}
        return {"status": "ok", "http": "200", "text": pages.get(url, "") * 4, "final_url": url}

    def artifact(name, sources_block, body="Your cost is 1,200 dollars over 30 days."):
        p = ROOT / "context" / "drafts" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("---\ntitle: x\n---\n\n" + body + "\n\n## Sources\n" + sources_block + "\n")
        return p

    failures: list[str] = []

    def check(label, condition, detail=""):
        if not condition:
            failures.append(f"{label}: {detail}")

    good = artifact("2026-10-24_t1_draft.md",
                    "[1] eCFR, 26 CFR 1.1091-1 — wash sales. https://www.ecfr.gov/current/title-26/section-1.1091-1\n"
                    "[2] IRS, Topic no. 409. https://www.irs.gov/taxtopics/tc409\n")
    r = gate(good, fetch_fn=fetch_fn, reg=reg)
    check("two primary sources on two hosts pass", r["ok"], str(r["blocking"]))
    check("the figure is found in a cited source", not r["figures"]["unsupported"],
          str(r["figures"]["unsupported"]))

    one_host = artifact("2026-10-24_t2_draft.md",
                        "[1] eCFR 1.1091-1. https://www.ecfr.gov/current/title-26/section-1.1091-1\n"
                        "[2] IRS Topic 409. https://www.irs.gov/taxtopics/tc409\n")
    r = gate(one_host, fetch_fn=fetch_fn, reg={**reg, "min_hosts": 3})
    check("a host floor is enforced", not r["ok"], "held nothing")

    blocked = artifact("2026-10-24_t3_draft.md",
                       "[1] Google News. https://news.google.com/articles/abc\n"
                       "[2] IRS Topic 409. https://www.irs.gov/taxtopics/tc409\n")
    r = gate(blocked, fetch_fn=fetch_fn, reg=reg)
    check("an aggregator citation is held", not r["ok"] and
          any("aggregator" in b for b in r["blocking"]), str(r["blocking"]))

    dead = artifact("2026-10-24_t4_draft.md",
                    "[1] eCFR 1.1091-1. https://www.ecfr.gov/current/title-26/section-1.1091-1\n"
                    "[2] Dead link. https://dead.example/gone\n")
    r = gate(dead, fetch_fn=fetch_fn, reg=reg)
    check("a dead citation is held", not r["ok"] and
          any("does not resolve" in b for b in r["blocking"]), str(r["blocking"]))

    mismatch = artifact("2026-10-24_t5_draft.md",
                        "[1] eCFR, 26 CFR 1.1091-1 wash sales. https://www.ecfr.gov/current/title-26/section-1.1091-1\n"
                        "[2] Federal Reserve stress test results. https://other.example/post\n")
    r = gate(mismatch, fetch_fn=fetch_fn, reg=reg)
    check("a link that is not the cited document is held", r["hold"] and
          any("not the document" in b for b in r["blocking"]), str(r["blocking"]))

    no_primary = artifact("2026-10-24_t6_draft.md",
                          "[1] Some blog. https://example.com/blog/post\n"
                          "[2] Another blog. https://other.example/post\n")
    r = gate(no_primary, fetch_fn=fetch_fn, reg=reg)
    check("no primary host is a note, not a hold",
          not any("PRIMARY" in b for b in r["blocking"]) and
          any("PRIMARY" in n for n in r["notes"]), str(r["blocking"]) + str(r["notes"]))

    gated = artifact("2026-10-24_t9_draft.md",
                     "[1] IRS, Topic no. 409 capital gains and losses. "
                     "https://www.irs.gov/taxtopics/tc409\n"
                     "[2] Paywalled study. https://gated.example/paywalled\n")
    r = gate(gated, fetch_fn=fetch_fn, reg=reg)
    check("a bot wall does not hold an article", not r["hold"],
          str(r["blocking"]))

    moved = artifact("2026-10-24_t10_draft.md",
                     "[1] IRS Topic 409. https://www.irs.gov/taxtopics/tc409\n"
                     "[2] Old report. https://moved.example/old-report\n")
    r = gate(moved, fetch_fn=fetch_fn, reg=reg)
    check("a link that collapsed to the site root is held", r["hold"] and
          any("not the document" in b for b in r["blocking"]), str(r["blocking"]))

    wired = artifact("2026-10-24_t7_draft.md",
                     "[1] Wire. https://prnewswire.com/release\n"
                     "[2] Wire two. https://prnewswire.com/release2\n")
    r = gate(wired, fetch_fn=fetch_fn, reg=reg)
    check("an all-press-release list is held", not r["ok"], str(r["blocking"]))

    old = artifact("2026-10-01_t8_draft.md", "[1] Gone. https://dead.example/gone\n")
    r = gate(old, fetch_fn=fetch_fn, reg=reg)
    check("an artifact older than enforced_from is never held",
          not r["hold"] and r["verdict"] == "grandfathered", f"{r['verdict']} {r['hold']}")

    unsupported = gate(good, fetch_fn=fetch_fn, reg=reg, strict_figures=True)
    check("--strict-figures leaves a supported figure alone", unsupported["ok"],
          str(unsupported["blocking"]))

    offline = gate(good, fetch_fn=fetch_fn, reg=reg, no_network=True)
    check("--no-network never claims a live check happened",
          any("skipped" in n for n in offline["notes"]), str(offline["notes"]))

    for p in (good, one_host, blocked, dead, mismatch, no_primary, wired, old, gated, moved):
        p.unlink(missing_ok=True)

    if failures:
        print("SELF-TEST FAILED")
        for f in failures:
            print(" -", f)
        return 1
    print("source gate self-test: all rules pinned (5 hold classes, bot walls and no-primary as "
          "notes, grandfathering, offline honesty)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="The source-accuracy floor for an article's citations.")
    ap.add_argument("--slug")
    ap.add_argument("--file")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--last", type=int)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-network", action="store_true")
    ap.add_argument("--strict-figures", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    reg = load_registry()
    no_network = args.no_network or os.environ.get("SOURCE_GATE_NO_NETWORK") == "1"
    paths: list[pathlib.Path] = []
    if args.file:
        paths = [pathlib.Path(args.file)]
    elif args.slug:
        p = artifact_for(args.slug)
        if p is None:
            print(f"no artifact for '{args.slug}'")
            return 2
        paths = [p]
    elif args.all or args.last:
        paths = sorted((ROOT / "published").glob("*.md"), reverse=True)
        if args.last:
            paths = paths[: args.last]
    else:
        ap.print_help()
        return 2

    reports = [gate(p, reg=reg, no_network=no_network, strict_figures=args.strict_figures)
               for p in paths]
    if args.json:
        print(json.dumps([{k: v for k, v in r.items() if k != "sources"} |
                          {"sources": [{kk: vv for kk, vv in s.items() if kk != "text"}
                                       for s in r.get("sources", [])]} for r in reports], indent=2))
    else:
        for r in reports:
            print_report(r)
            print()
    held = [r for r in reports if r["hold"]]
    if not args.json:
        print(f"{len(reports)} artifact(s): {len(held)} held, "
              f"{len([r for r in reports if r['verdict'] == 'grandfathered'])} grandfathered, "
              f"{len([r for r in reports if r['verdict'] == 'pass'])} pass")
    return 1 if held else 0


if __name__ == "__main__":
    sys.exit(main())
