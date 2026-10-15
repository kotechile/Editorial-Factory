#!/usr/bin/env python3
"""What is live on a reader frontend — sitemap discovery, cached page fetch, metadata, classification.

    from site_corpus import discover_sitemaps, metadata_for
    urls = discover_sitemaps("https://giniloh.com")            # page URLs, from the site's own sitemap
    pages = metadata_for(urls, frontend="https://giniloh.com") # {"url", "title", "excerpt", ..., "kind"}

Why it exists
-------------
The internal-link corpus used to come from the CMS (`build_internal_link_index.py` walked
`public.vertical_sites` and asked WordPress what exists). That cannot see a frontend the CMS does not
know about — aichieve.net serves the same articles as giniloh.com but has no `vertical_sites` row — and
it says nothing about whether a page *resolves* on the front that renders it. This module owns the other
half of the question: **what is live on the site the reader is actually reading**.

Four rules, all measured on the three live fronts (2026-10-15)
-------------------------------------------------------------
  * **The sitemap is the liveness claim.** robots.txt `Sitemap:` directives first, then the conventional
    paths; a `<sitemapindex>` is followed one level (Astro emits `sitemap-index.xml -> sitemap-0.xml`).
    If nothing is reachable this raises — an empty corpus must never look like "the site has no pages".
  * **The canonical link is the identity guard.** `wellroost.com/<unknown>/` answers **200 with the
    homepage shell** whose canonical is `https://wellroost.com/`; giniloh.com and aichieve.net answer
    real 404s. So "HTTP 200" proves nothing: a page whose canonical is not the URL we asked for is not
    the page we asked for, and `page_metadata()` returns None for it.
  * **Every front publishes what the corpus needs.** Each article page carries `<link rel="canonical">`,
    an `Article` JSON-LD block (`headline`, `description`, `dateModified`) and a `BreadcrumbList` whose
    items point at `/categories/<slug>/`. No CMS call is needed for title, excerpt or category.
  * **Liveness is a set operation, so it must be cheap.** Pages are cached under
    `<cache_dir>/<host>/<sha1(url)>.json` and revalidated with `If-None-Match`/`If-Modified-Since`, and
    fetches are capped at 3 in flight per host, so a rebuild is ~200 requests cold and ~200 304s warm.

Stdlib only (urllib, json, re, html, hashlib, concurrent.futures, xml.etree) — no new dependencies.

Public API (frozen — other modules import these)
----------------------------------------------
    SiteCorpusError, SITEMAP_CANDIDATES, discover_sitemaps(), fetch_page(), page_metadata(),
    classify(), metadata_for()
"""

from __future__ import annotations

import hashlib
import html as html_lib
import json
import pathlib
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

USER_AGENT = "Mozilla/5.0 (editorial-factory corpus)"
REQUEST_TIMEOUT = 20            # seconds, per request
MAX_RETRIES = 2                 # 2 retries => 3 attempts, transient failures only
RETRY_BACKOFF = (0.5, 1.5)      # seconds, exponential-ish; tests may zero this out
PER_HOST_LIMIT = 3              # at most 3 concurrent requests to one host
CACHE_MAX_AGE_SECONDS = 24 * 3600   # a fresh cache record is served without touching the network

SITEMAP_CANDIDATES = ("/sitemap.xml", "/sitemap-index.xml", "/sitemap_index.xml")

ARTICLE_TYPES = ("Article", "BlogPosting", "NewsArticle")

# One-segment paths that are site furniture, never link targets.
RESERVED_ONE_SEGMENT = frozenset({
    "about", "contact", "privacy", "terms", "author", "articles", "apps", "showcase", "search",
    "feed", "insights",
})
# Section roots themselves ("/calculators/") are furniture; their children are targets.
SECTION_ROOTS = frozenset({"categories", "tools", "calculators"})
# Paths that are files, not pages.
FILE_SUFFIXES = (".xml", ".txt")


class SiteCorpusError(Exception):
    """Raised when the corpus cannot be established (nothing reachable, offline miss, bad status)."""


# --------------------------------------------------------------------------- small helpers

def _base(frontend: str) -> str:
    """A frontend as a scheme+host with no trailing slash."""
    return (frontend or "").strip().rstrip("/")


def _text(body) -> str:
    if isinstance(body, bytes):
        return body.decode("utf-8", errors="replace")
    return body if isinstance(body, str) else ""


def _header(headers, name: str):
    """Case-insensitive header read; the real transport keeps the server's own casing."""
    if not headers:
        return None
    wanted = name.lower()
    for key, value in headers.items():
        if str(key).lower() == wanted:
            return value
    return None


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _normalize(url: str) -> str:
    """Strip whitespace and the fragment. A fragment never names a different page."""
    url = (url or "").strip()
    return urllib.parse.urldefrag(url)[0]


def _path_of(url: str) -> str:
    return urllib.parse.urlsplit(url).path or "/"


def _segments(url: str) -> list[str]:
    return [seg for seg in _path_of(url).split("/") if seg]


def _same_page(a: str, b: str) -> bool:
    """Two URLs name the same page. A trailing slash is not a different page (`/x` == `/x/`)."""
    if not a or not b:
        return False
    return _normalize(a).rstrip("/") == _normalize(b).rstrip("/")


def _dedupe(urls, base: str = "") -> list[str]:
    """De-duplicate, drop fragments, and resolve anything relative against `base`."""
    out, seen = [], set()
    for raw in urls:
        url = _normalize(raw)
        if not url:
            continue
        if base and not urllib.parse.urlsplit(url).netloc:
            url = urllib.parse.urljoin(base.rstrip("/") + "/", url)
        if url in seen:
            continue
        seen.add(url)
        out.append(url)
    return out


# --------------------------------------------------------------------------- transport

def default_fetch(url: str, headers: dict):
    """The real transport: `fetch(url, headers) -> (status, headers, body_bytes)`.

    HTTP statuses are *returned*, not raised (a 404 or a 304 is an answer); connection-level failures
    raise, and `fetch_page` retries those. Redirects are followed by urllib.
    """
    request = urllib.request.Request(url, headers=dict(headers or {}), method="GET")
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
            return response.status, dict(response.headers), response.read()
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read()
        except Exception:                                       # a dropped socket mid-body
            body = b""
        return exc.code, dict(exc.headers or {}), body


def _request(url: str, fetch, headers: dict):
    """One logical request with the retry policy applied: transient failures only, then raise."""
    last_error: Exception | None = None
    for attempt in range(MAX_RETRIES + 1):
        try:
            status, response_headers, body = fetch(url, dict(headers))
        except Exception as exc:                                # noqa: BLE001 - transport-level
            last_error = exc
        else:
            # A definitive answer (2xx/3xx/4xx) is returned as-is; only a transient one is retried.
            if status < 400 or not (status in (408, 425, 429) or status >= 500):
                return status, response_headers, body
            last_error = SiteCorpusError(f"{url} answered HTTP {status}")
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_BACKOFF[min(attempt, len(RETRY_BACKOFF) - 1)])
    raise SiteCorpusError(f"{url} could not be fetched after {MAX_RETRIES + 1} attempts: {last_error}")


def _headers_for(etag=None, lastmod=None) -> dict:
    headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"}
    if etag:
        headers["If-None-Match"] = etag
    if lastmod:
        headers["If-Modified-Since"] = lastmod
    return headers


# --------------------------------------------------------------------------- sitemap discovery

def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _parse_xml(body) -> ET.Element | None:
    text = _text(body).strip()
    if not text.startswith("<"):
        return None
    try:
        return ET.fromstring(text)
    except ET.ParseError:
        return None


def _xml_locs(root: ET.Element) -> list[str]:
    return [(node.text or "").strip() for node in root.iter()
            if _local_name(node.tag) == "loc" and (node.text or "").strip()]


def discover_sitemaps(frontend: str, fetch=None, max_index_depth: int = 2) -> list[str]:
    """The page URLs a frontend publishes, read from its own sitemap.

    Order: every `Sitemap:` directive in `robots.txt` (in file order), then `SITEMAP_CANDIDATES`.
    Each address is an alternative address for the same corpus, so the first one that yields locs
    wins; earlier addresses that 404 or parse to nothing are skipped. A `<sitemapindex>` is followed
    one level (`max_index_depth=2`: the index itself is depth 1, its children depth 2 and are not
    followed further). Locs are de-duplicated and defragged.

    Raises SiteCorpusError when no sitemap is reachable (or every reachable one is empty): an empty
    list would be indistinguishable from "this site has no live pages", which is never true here.
    """
    fetch = fetch or default_fetch
    base = _base(frontend)
    if not base:
        raise SiteCorpusError("discover_sitemaps needs a frontend URL")
    documents: dict[str, tuple[int, dict, bytes] | None] = {}

    for url in _robots_sitemaps(base + "/robots.txt", fetch, documents):
        locs = _sitemap_locs(url, fetch, documents, 1, max_index_depth, base)
        if locs:
            return locs
    for path in SITEMAP_CANDIDATES:
        url = urllib.parse.urljoin(base + "/", path.lstrip("/"))
        locs = _sitemap_locs(url, fetch, documents, 1, max_index_depth, base)
        if locs:
            return locs
    raise SiteCorpusError(
        f"no reachable sitemap for {base}: tried robots.txt Sitemap: directives and "
        f"{', '.join(SITEMAP_CANDIDATES)}")


def _fetch_document(url: str, fetch, documents):
    """Fetch a sitemap/robots document once per discovery call."""
    if url not in documents:
        try:
            documents[url] = fetch(url, {"User-Agent": USER_AGENT,
                                         "Accept": "application/xml,text/xml,text/plain,*/*"})
        except Exception:                                       # noqa: BLE001 - unreachable == absent
            documents[url] = None
    return documents[url]


def _robots_sitemaps(url: str, fetch, documents) -> list[str]:
    """The `Sitemap:` directives in robots.txt, in file order."""
    response = _fetch_document(url, fetch, documents)
    if not response:
        return []
    status, _, body = response
    if status != 200:
        return []
    found = []
    for raw in _text(body).splitlines():
        line = raw.split("#", 1)[0].strip()
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        if key.strip().lower() == "sitemap" and value.strip():
            found.append(urllib.parse.urljoin(url, value.strip()))
    return _dedupe(found)


def _sitemap_locs(url: str, fetch, documents, depth: int, max_index_depth: int, base: str) -> list[str]:
    """The page locs a sitemap document (or one level of sitemap index) provides."""
    response = _fetch_document(url, fetch, documents)
    if not response:
        return []
    status, _, body = response
    if status != 200:
        return []
    root = _parse_xml(body)
    if root is None:
        return []
    name = _local_name(root.tag)
    locs = _xml_locs(root)
    if name == "sitemapindex":
        if depth >= max_index_depth:
            return []
        collected = []
        for child in _dedupe(locs, base=url):
            collected.extend(_sitemap_locs(child, fetch, documents, depth + 1, max_index_depth, base))
        return _dedupe(collected, base=base)
    return _dedupe(locs, base=base)


# --------------------------------------------------------------------------- page cache + fetch

def _cache_path(cache_dir, url: str) -> pathlib.Path:
    cache_dir = pathlib.Path(cache_dir)
    host = urllib.parse.urlsplit(url).netloc or "unknown"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return cache_dir / host / f"{digest}.json"


def _read_cache(path: pathlib.Path) -> dict | None:
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if not isinstance(record, dict) or not isinstance(record.get("html"), str):
        return None
    return record


def _write_cache(path: pathlib.Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {key: record.get(key) for key in ("url", "html", "etag", "lastmod", "fetched_at")}
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def _is_fresh(record: dict) -> bool:
    stamp = record.get("fetched_at")
    if not stamp:
        return False
    try:
        fetched = datetime.fromisoformat(stamp)
    except ValueError:
        return False
    if fetched.tzinfo is None:
        fetched = fetched.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - fetched).total_seconds() <= CACHE_MAX_AGE_SECONDS


def _record(record: dict, from_cache: bool) -> dict:
    return {"url": record.get("url"), "html": record.get("html") or "",
            "etag": record.get("etag"), "lastmod": record.get("lastmod"),
            "fetched_at": record.get("fetched_at"), "from_cache": from_cache}


def fetch_page(url: str, *, cache_dir=None, fetch=None, offline: bool = False) -> dict:
    """Fetch one page, from the cache when it is fresh, revalidating it when it is stale.

    Returns {"url", "html", "etag", "lastmod", "fetched_at", "from_cache"}. The cache file is
    `<cache_dir>/<host>/<sha1(url)>.json`. A stale record is revalidated with If-None-Match /
    If-Modified-Since; a 304 keeps it (and only refreshes `fetched_at`). `offline=True` never touches
    the network and raises SiteCorpusError on a cache miss. Non-200 answers raise SiteCorpusError.
    """
    fetch = fetch or default_fetch
    url = _normalize(url)
    path = _cache_path(cache_dir, url) if cache_dir else None
    cached = _read_cache(path) if path else None

    if cached is not None and (offline or _is_fresh(cached)):
        return _record(cached, from_cache=True)
    if offline:
        raise SiteCorpusError(f"offline and no cached copy of {url}")

    headers = _headers_for(cached.get("etag") if cached else None,
                           cached.get("lastmod") if cached else None)
    status, response_headers, body = _request(url, fetch, headers)

    if status == 304 and cached is not None:
        kept = dict(cached)
        kept["fetched_at"] = _now_iso()
        if path:
            _write_cache(path, kept)
        return _record(kept, from_cache=True)
    if status != 200:
        raise SiteCorpusError(f"{url} answered HTTP {status}")

    record = {"url": url, "html": _text(body),
              "etag": _header(response_headers, "ETag"),
              "lastmod": _header(response_headers, "Last-Modified"),
              "fetched_at": _now_iso()}
    if path:
        _write_cache(path, record)
    return _record(record, from_cache=False)


# --------------------------------------------------------------------------- page metadata

_LD_RE = re.compile(r"<script[^>]*type\s*=\s*[\"']application/ld\+json[\"'][^>]*>(.*?)</script>",
                    re.IGNORECASE | re.DOTALL)
_CANONICAL_RE = re.compile(r"<link[^>]*rel\s*=\s*[\"']canonical[\"'][^>]*>", re.IGNORECASE)
_HREF_RE = re.compile(r"href\s*=\s*[\"']([^\"']*)[\"']", re.IGNORECASE)
_META_TAG_RE = re.compile(r"<meta\s[^>]*>", re.IGNORECASE)
_META_ATTR_RE = re.compile(r"(property|name)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
_CONTENT_RE = re.compile(r"content\s*=\s*[\"'](.*?)[\"']", re.IGNORECASE | re.DOTALL)
_TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
_TAGS_RE = re.compile(r"<[^>]+>")
_CATEGORY_PATH_RE = re.compile(r"^/categories/([^/]+)/?$")
# A trailing " | Site" / " - Site" / " — Site" (the site name is at most 3 words: "WellRoost",
# "Gini Loh", "WellRoost Editorial Team"). A longer tail is a real subtitle, not a site stamp.
_TITLE_SUFFIX_RE = re.compile(r"^(?P<head>.+)\s+[|\u2013\u2014-]\s+(?P<tail>\S+(?:\s+\S+){0,2})$")


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(text or "")).strip()


def _strip_site_suffix(title: str) -> str:
    """Drop a page's own site furniture from its `<title>`/og:title.

    Measured shapes on the live fronts (2026-10-15), all of which have to come out as the page's name
    because this string becomes a reader-facing anchor and the "— more on <category>" copy:

        "Your Battery Payback: A 5-State Gap | WellRoost"                 -> "Your Battery Payback: A 5-State Gap"
        "Lease Break Penalty & Offset Estimator | Gini Loh"               -> "Lease Break Penalty & Offset Estimator"
        "Artificial Intelligence & Future of Work — dispatches and tools | AIChieve"
                                                                          -> "Artificial Intelligence & Future of Work"

    A brand stamp is at most three words, so it strips outright. The Astro-built hub/tool pages carry a
    SECOND chunk ("— dispatches and tools"); that one only strips when what remains is still a real name
    (three words or more), so a legitimate short title with a dash subtitle ("Total Comp — Real Numbers")
    keeps its subtitle. Article titles are unaffected either way: they come from JSON-LD `headline`.
    """
    text = _clean(title)
    for attempt in range(2):
        match = _TITLE_SUFFIX_RE.match(text)
        if not match:
            break
        head, tail = match.group("head").strip(), match.group("tail").strip()
        if len(head) < 8:
            break
        if attempt and (len(head.split()) < 3 or len(tail.split()) > 4):
            break
        text = head
    return text


def _jsonld_nodes(html: str):
    """Every JSON object inside every `application/ld+json` block (`@graph` and arrays included)."""
    for raw in _LD_RE.findall(html or ""):
        try:
            payload = json.loads(raw.strip())
        except ValueError:
            continue
        stack = [payload]
        while stack:
            node = stack.pop()
            if isinstance(node, list):
                stack.extend(node)
            elif isinstance(node, dict):
                graph = node.get("@graph")
                if isinstance(graph, list):
                    stack.extend(graph)
                yield node


def _types_of(node: dict) -> list[str]:
    value = node.get("@type")
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [v for v in value if isinstance(v, str)]
    return []


def _first_of_type(nodes, types) -> dict | None:
    for node in nodes:
        if any(t in types for t in _types_of(node)):
            return node
    return None


def _meta_content(html: str, *names) -> str:
    """The content of the first `<meta>` whose property/name matches, in document order."""
    wanted = {name.lower() for name in names}
    for tag in _META_TAG_RE.findall(html or ""):
        for _, key in _META_ATTR_RE.findall(tag):
            if key.lower() in wanted:
                match = _CONTENT_RE.search(tag)
                if match and match.group(1).strip():
                    return _clean(match.group(1))
    return ""


def _canonical_href(html: str):
    tag = _CANONICAL_RE.search(html or "")
    if not tag:
        return None
    match = _HREF_RE.search(tag.group(0))
    if not match or not match.group(1).strip():
        return None
    return _clean(match.group(1))


def _breadcrumb_categories(nodes) -> list[dict]:
    """`/categories/<slug>/` breadcrumb items, minus the position-1 Home crumb."""
    categories: list[dict] = []
    seen: set[str] = set()
    for node in nodes:
        if "BreadcrumbList" not in _types_of(node):
            continue
        items = node.get("itemListElement")
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            name = _clean(str(item.get("name") or ""))
            position = item.get("position")
            if position == 1 or name.lower() == "home":
                continue
            location = item.get("item") or item.get("@id") or ""
            if not isinstance(location, str):
                continue
            match = _CATEGORY_PATH_RE.match(_path_of(location))
            if not match:
                continue
            slug = match.group(1)
            if slug in seen:
                continue
            seen.add(slug)
            categories.append({"name": name or slug, "slug": slug})
    return categories


def page_metadata(html: str, url: str) -> dict | None:
    """Title, excerpt, modified date and categories for one page — or None if it is not that page.

    None means "the page we got is not the page we asked for": a `<link rel="canonical">` pointing
    somewhere else (the wellroost.com soft 404 answers 200 with the homepage shell, canonical = the
    site root). Everything else is read in a fixed order of preference:

      title    JSON-LD Article/BlogPosting/NewsArticle `headline` -> og:title -> `<title>` with a
               trailing " | <Site>" / " - <Site>" / " — <Site>" stripped -> `<h1>`
      excerpt  JSON-LD `description` -> og:description -> meta description
      modified JSON-LD `dateModified` -> `datePublished`
      categories  JSON-LD `BreadcrumbList` items whose item path is `/categories/<slug>/`, minus the
               position-1 Home crumb; slug = last path segment, name = the item's name (unescaped)
    """
    url = _normalize(url)
    canonical = _canonical_href(html)
    if canonical is not None and not _same_page(canonical, url):
        return None

    nodes = list(_jsonld_nodes(html))
    article = _first_of_type(nodes, ARTICLE_TYPES)

    title = _clean(str(article.get("headline") or "")) if article else ""
    if not title:
        # og:title carries the same "Name | Brand" stamp as <title>, and this is the branch a hub or a
        # calculator page takes (neither has Article JSON-LD): "Lease Break Penalty & Offset Estimator |
        # Gini Loh" reached the corpus, and from there an anchor, until this was stripped here too.
        title = _strip_site_suffix(_meta_content(html, "og:title"))
    if not title:
        match = _TITLE_RE.search(html or "")
        if match:
            title = _strip_site_suffix(_TAGS_RE.sub(" ", match.group(1)))
    if not title:
        match = _H1_RE.search(html or "")
        if match:
            title = _clean(_TAGS_RE.sub(" ", match.group(1)))

    excerpt = _clean(str(article.get("description") or "")) if article else ""
    if not excerpt:
        excerpt = _meta_content(html, "og:description")
    if not excerpt:
        excerpt = _meta_content(html, "description")

    modified = ""
    if article:
        modified = str(article.get("dateModified") or article.get("datePublished") or "").strip()

    categories = _breadcrumb_categories(nodes)

    return {
        "url": url,
        "title": title,
        "excerpt": excerpt,
        "modified": modified,
        "categories": categories,
        "category_slugs": [c["slug"] for c in categories],
        "canonical": canonical or url,
        # What classify() reads; a page that answers 200 without claiming this URL in its canon is
        # never treated as an article (page_metadata() would already have returned None).
        "jsonld_types": sorted({t for node in nodes for t in _types_of(node)}),
        "article": article is not None,
        "canonical_match": _same_page(canonical or url, url),
    }


# --------------------------------------------------------------------------- classification

def classify(url: str, meta: dict | None) -> str | None:
    """`article` | `category` | `tool`, or None to skip — decided by markup and path shape.

      article   meta is not None, the page carries an Article/BlogPosting/NewsArticle JSON-LD block,
                and its canonical is the URL we asked for
      category  a 2-segment `/categories/<slug>/` path
      tool      a 2-segment path under `/tools/` or `/calculators/`
      None      3+ segments (the nested `/calculators/<slug>/<role>/` permutations), reserved
                1-segment paths, `.xml`/`.txt` paths, section roots, and anything meta is None for
    """
    if meta is None:
        return None
    url = _normalize(url)
    segments = _segments(url)
    if any(seg.lower().endswith(FILE_SUFFIXES) for seg in segments):
        return None
    if len(segments) >= 3:
        return None
    if len(segments) == 2:
        if segments[0] == "categories":
            return "category"
        if segments[0] in ("tools", "calculators"):
            return "tool"
        return None
    if segments:
        first = segments[0].lower()
        if first in RESERVED_ONE_SEGMENT or first in SECTION_ROOTS:
            return None
    canonical = meta.get("canonical") or meta.get("url") or ""
    if _path_of(canonical) == "/" and _path_of(url) != "/":
        return None                                                 # the homepage shell again
    if not (meta.get("article") if "article" in meta
            else any(t in ARTICLE_TYPES for t in (meta.get("jsonld_types") or []))):
        return None
    return "article" if _same_page(canonical, url) else None


# --------------------------------------------------------------------------- the crawl

_semaphore_lock = threading.Lock()
_host_semaphores: dict[str, threading.BoundedSemaphore] = {}


def _host_semaphore(host: str) -> threading.BoundedSemaphore:
    """At most PER_HOST_LIMIT requests in flight to one host, module-wide."""
    with _semaphore_lock:
        semaphore = _host_semaphores.get(host)
        if semaphore is None:
            semaphore = threading.BoundedSemaphore(PER_HOST_LIMIT)
            _host_semaphores[host] = semaphore
        return semaphore


def metadata_for(urls, *, frontend: str, cache_dir=None, fetch=None, offline: bool = False,
                 max_pages: int = 400) -> list[dict]:
    """Metadata for every URL that is a real page, in the order given, at most 3 fetches per host.

    A URL whose page cannot be fetched (404, transport failure) or whose page is not the page we
    asked for (canonical mismatch) or that classify() skips is left out rather than guessed at. Each
    kept record is the page_metadata() dict plus `"kind"` (classify's answer) and `"from_cache"`.
    `len(urls) > max_pages` raises: the crawl is bounded, never silently truncated.
    """
    urls = list(urls)
    if len(urls) > max_pages:
        raise SiteCorpusError(f"{len(urls)} urls exceeds max_pages={max_pages}: "
                              f"bound the crawl instead of truncating it silently")
    if not urls:
        return []
    fetch = fetch or default_fetch
    base = _base(frontend)
    targets = [urllib.parse.urljoin(base + "/", url) if not urllib.parse.urlsplit(
        _normalize(url)).netloc else _normalize(url) for url in urls]

    hosts = {urllib.parse.urlsplit(url).netloc for url in targets}
    workers = max(1, min(len(targets), PER_HOST_LIMIT * max(1, len(hosts))))

    def one(index: int, url: str):
        with _host_semaphore(urllib.parse.urlsplit(url).netloc):
            try:
                page = fetch_page(url, cache_dir=cache_dir, fetch=fetch, offline=offline)
            except SiteCorpusError:
                return index, None
        meta = page_metadata(page["html"], url)
        kind = classify(url, meta)
        if meta is None or kind is None:
            return index, None
        return index, {**meta, "kind": kind, "from_cache": page["from_cache"]}

    results: list[dict | None] = [None] * len(targets)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(one, index, url) for index, url in enumerate(targets)]
        for future in futures:
            index, record = future.result()
            results[index] = record
    return [record for record in results if record is not None]


if __name__ == "__main__":                                          # a small manual smoke test
    import sys

    site = sys.argv[1] if len(sys.argv) > 1 else "https://giniloh.com"
    found = discover_sitemaps(site)
    print(f"{site}: {len(found)} pages in the sitemap; first 5: {found[:5]}")
