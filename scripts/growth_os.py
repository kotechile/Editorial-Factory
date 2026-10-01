#!/usr/bin/env python3
"""Growth OS Knowledge, Cannibalization Prevention & Internal Linking Engine.

Functions:
1. Cannibalization Checker: Prevents competing against our own published URLs.
2. Internal Link Map Generator: Identifies high-relevance internal links and anchor texts.
3. Growth OS POV & Anecdote Extractor: Pulls founder opinions and customer truth from knowledge base.
"""

import argparse
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTEXT_DIR = ROOT / "context"
GROWTH_OS_DIR = CONTEXT_DIR / "growth_os"
FOUNDER_VOICE_FILE = GROWTH_OS_DIR / "founder-voice.md"
CUSTOMER_TRUTH_FILE = GROWTH_OS_DIR / "customer-truth.md"
SITEMAP_FILE = CONTEXT_DIR / "sitemap.json"
INTERNAL_LINK_INDEX = CONTEXT_DIR / "internal_links.json"
PUBLISHED_DIR = ROOT / "published"
DRAFTS_DIR = CONTEXT_DIR / "drafts"

# Words carrying no topical signal — excluded so a shared "the" never scores a link.
STOPWORDS = {"the", "a", "an", "of", "and", "or", "for", "to", "in", "on", "with", "is", "are",
             "how", "why", "what", "your", "you", "it", "that", "this", "vs", "at", "by", "from",
             "as", "be", "can", "does", "do", "new", "2026", "best", "guide"}

# ...and the second tier: real words that still carry no topical signal, so their presence on two
# pages says nothing about whether they are about the same thing. Without these, an article matched
# on "just", "more"/"than", "into" or "first" and a supply-chain piece was offered the Nvidia
# memory-bet article because both contained "billion" (measured on the live corpus).
GENERIC = {"just", "more", "most", "than", "then", "there", "these", "they", "their", "them", "into",
           "over", "after", "before", "first", "last", "never", "still", "even", "also", "says", "said",
           "year", "years", "week", "weeks", "month", "months", "day", "days", "today", "one", "two",
           "three", "four", "five", "six", "seven", "eight", "nine", "ten", "its", "has", "have", "had",
           "was", "were", "been", "being", "will", "would", "could", "should", "may", "might", "must",
           "about", "across", "around", "between", "during", "under", "while", "when", "where", "which",
           "who", "whom", "some", "any", "all", "both", "each", "other", "others", "such", "only",
           "very", "much", "many", "less", "least", "own", "same", "out", "up", "down", "off", "again",
           "further", "once", "here", "right", "left", "back", "big", "small", "high", "low", "long",
           "short", "next", "now", "keep", "kept", "make", "made", "take", "took", "give", "gave",
           "get", "got", "go", "goes", "went", "come", "came", "see", "seen", "know", "known", "think",
           "want", "need", "needs", "use", "used", "uses", "using", "way", "ways", "thing", "things",
           "part", "parts", "lot", "lots", "case", "cases", "points", "test", "tests", "reason",
           "reasons", "choice", "choices", "data", "stop", "stops", "read", "reads", "say", "saying",
           "show", "shows", "shown", "look", "looks", "looking", "put", "putting", "turn", "turns",
           "call", "calls", "called", "given", "let", "lets", "tell", "told", "ask", "asked", "seem",
           "seems", "become", "becomes", "became", "holding", "hold", "held", "stand", "standing",
           "stay", "stays"}
STOPWORDS = STOPWORDS | GENERIC

# How many distinct subject tokens a candidate must share before a mere topical match is treated as
# evidence of relevance. One is not: "billion" appears in a GPU-memory story and a tariff story.
MIN_OVERLAP_TOKENS = 2
MIN_TOKEN_LENGTH = 4            # "ai" is not a subject; a shared 2-letter token never links


def load_sitemap():
    """Load sitemap from JSON or rebuild dynamically from published/ directory."""
    if SITEMAP_FILE.exists():
        try:
            with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Growth OS] Warning reading sitemap.json: {e}", file=sys.stderr)

    # Rebuild basic sitemap from published directory
    articles = []
    if PUBLISHED_DIR.exists():
        for md_path in sorted(PUBLISHED_DIR.glob("*.md")):
            text = md_path.read_text(encoding="utf-8")
            title_m = re.search(r"^#\s+(.+)$", text, re.M) or re.search(r"title:\s*[\"']?([^\"\n\r]+)[\"']?", text)
            title = title_m.group(1).strip() if title_m else md_path.stem
            vert_m = re.search(r"vertical:\s*([a-z0-9_]+)", text)
            vert = vert_m.group(1).strip() if vert_m else "general"

            articles.append({
                "slug": md_path.stem,
                "title": title,
                "url": f"/published/{md_path.name}",
                "vertical": vert,
                "primary_keyword": md_path.stem.replace("_", " ").replace("-", " ").lower(),
                "secondary_keywords": [],
                "date": md_path.stem[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", md_path.stem) else ""
            })
    return {"articles": articles, "base_url": "https://editorialfactory.io"}


def check_cannibalization(target_keyword, vertical=None, threshold=0.65):
    """Check if the keyword conflicts with an existing published piece."""
    sitemap = load_sitemap()
    articles = sitemap.get("articles", [])
    cleaned_target = target_keyword.strip().lower()
    target_words = set(re.findall(r"\w+", cleaned_target))

    conflicts = []

    for art in articles:
        p_kw = art.get("primary_keyword", "").lower()
        title = art.get("title", "").lower()
        sec_kws = [k.lower() for k in art.get("secondary_keywords", [])]

        # 1. Exact match check
        if cleaned_target == p_kw or cleaned_target in sec_kws:
            conflicts.append({
                "article": art,
                "similarity": 1.0,
                "reason": "Exact primary/secondary keyword match"
            })
            continue

        # 2. Token overlap similarity (Jaccard)
        all_art_words = set(re.findall(r"\w+", f"{p_kw} {title} {' '.join(sec_kws)}"))
        if not all_art_words or not target_words:
            continue

        intersection = target_words.intersection(all_art_words)
        jaccard = len(intersection) / len(target_words.union(all_art_words))

        # Check if target phrase is substantial subset
        overlap_ratio = len(intersection) / max(1, len(target_words))

        if jaccard >= threshold or overlap_ratio >= 0.8:
            conflicts.append({
                "article": art,
                "similarity": round(max(jaccard, overlap_ratio), 2),
                "reason": f"High semantic token overlap ({round(overlap_ratio*100)}% keyword tokens match)"
            })

    conflicts.sort(key=lambda x: x["similarity"], reverse=True)

    if conflicts:
        top = conflicts[0]
        verdict = "CANNOT_PUBLISH_DUPLICATE" if top["similarity"] >= 0.95 else "UPDATE_EXISTING_OR_SUBCLUSTER"
        return {
            "is_cannibalized": True,
            "verdict": verdict,
            "top_conflict": top["article"],
            "similarity": top["similarity"],
            "reason": top["reason"],
            "all_conflicts": conflicts,
            "recommendation": (
                f"Topic heavily cannibalizes '{top['article']['title']}'. "
                f"Either update '{top['article']['slug']}' with a fresh section or narrow target keyword to a distinct long-tail sub-topic."
            )
        }

    return {
        "is_cannibalized": False,
        "verdict": "CLEAR_TO_PUBLISH",
        "top_conflict": None,
        "similarity": 0.0,
        "recommendation": "No cannibalization detected. Clear to draft new pillar/cluster article."
    }


def load_internal_link_index():
    """The internal-link candidate index built from the live sites (build_internal_link_index.py).

    Falls back to the app's own sitemap — which only knows what this pipeline published — with a
    warning, rather than returning nothing and silently drafting articles with no internal links.
    """
    if INTERNAL_LINK_INDEX.exists():
        try:
            index = json.loads(INTERNAL_LINK_INDEX.read_text(encoding="utf-8"))
            if index.get("candidates"):
                return index
            print("[internal-links] index holds no candidates — falling back to the local sitemap",
                  file=sys.stderr)
        except (ValueError, OSError) as exc:
            print(f"[internal-links] index unreadable ({exc}) — falling back to the local sitemap",
                  file=sys.stderr)
    else:
        print("[internal-links] context/internal_links.json is missing — run "
              "scripts/build_internal_link_index.py; falling back to the local sitemap (no real "
              "corpus)", file=sys.stderr)
    return None


def _site_for_vertical(vertical):
    """The site + category a vertical routes to, from public.vertical_sites (best effort)."""
    if not vertical:
        return None
    try:
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
        import wp_draft
        # wp_category_id arrives with migration 0004; ask for it, and retry without it so routing
        # still works against a database that has not been migrated yet.
        for fields, quiet in (("site_domain,frontend_url,wp_category_id", True),
                              ("site_domain,frontend_url", False)):
            rows = wp_draft.supabase_get(
                f"vertical_sites?select={fields}&vertical_id=eq.{vertical}", quiet=quiet)
            if rows:
                return rows[0]
        return None
    except Exception:                                          # noqa: BLE001 - optional
        return None


def _anchor_for(candidate, target_words):
    """Anchor text for a candidate: its own title, trimmed at a word boundary.

    Anchors are taken from the destination page's title rather than invented, so the link text
    describes the page it points at. Titles that begin with a question or a stopword are trimmed to
    the substantive phrase.
    """
    text = " ".join(str(candidate.get("title") or candidate.get("slug") or "").split())
    text = re.sub(r"^(the|our|why|how to|how|what)\s+", "", text, flags=re.I).strip(" :,-–—")
    if not text:
        text = candidate.get("slug", "")
    # Many titles carry a subtitle ("NY Heat Pump Rebate: Double Payouts for Sealed Homes"). The head
    # phrase is the better anchor when it stands on its own — shorter, and it names the page.
    head = re.split(r"\s+[—–|]\s+|:\s+", text, maxsplit=1)[0].strip(" ,;:-–—")
    if len(head) >= 18:
        text = head
    if len(text) > 64:
        text = text[:64].rsplit(" ", 1)[0] + "…"
    return text


def _subject_tokens(text: str) -> set[str]:
    """Tokens that can carry topical meaning: no stopwords, no generic filler, 4+ characters, and
    never a bare number ("10" and "2026" appear in everything and identify nothing)."""
    return {t for t in re.findall(r"[a-z0-9][a-z0-9'’-]*", (text or "").lower())
            if t not in STOPWORDS and len(t) >= MIN_TOKEN_LENGTH and not t.isdigit()}


def _slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")


def generate_internal_link_map(target_keyword, vertical=None, max_links=3, exclude_slugs=()):
    """Propose internal links from the site's real, live corpus.

    Candidates come from context/internal_links.json, whose liveness is decided by each frontend's
    sitemap — the 28 hand-written articles already live on giniloh.com and wellroost.com are the
    strongest targets on either site and were previously invisible to the generator.

    Same-site only: a link from giniloh.com to wellroost.com is a cross-site link, not an internal
    one, so candidates from another domain are dropped rather than ranked lower.

    `exclude_slugs` are the caller's own pages (the article being pushed, and any already-published
    row it is refreshing). The self-exclusion below only matches when the target keyword *is* the
    slug, which a headline-and-lead topic never is — so a refresh of a live article could otherwise
    link it to itself.
    """
    excluded = {s for s in (exclude_slugs or ()) if s}
    target_words = _subject_tokens(target_keyword)
    self_slug = re.sub(r"[^a-z0-9]+", "-", (target_keyword or "").lower()).strip("-")

    index = load_internal_link_index()
    category_names: dict[str, str] = {}
    if index:
        routing = _site_for_vertical(vertical) or {}
        destination = routing.get("site_domain")
        destination_category = routing.get("wp_category_id")
        category_names = ((index.get("categories") or {}).get(destination or "", {}) or {})
        candidates = [c for c in index.get("candidates", []) if c.get("live") and c.get("url")]
        source = "context/internal_links.json"
    else:
        sitemap = load_sitemap()
        destination, destination_category, routing = None, None, {}
        candidates = [{"site": None, "kind": "article", "title": a.get("title"),
                       "slug": a.get("slug"), "url": a.get("url"),
                       "categories": [], "category_ids": [], "excerpt": "",
                       "vertical": a.get("vertical")}
                      for a in sitemap.get("articles", []) if a.get("url")]
        source = "context/sitemap.json (fallback)"

    scored = []
    for candidate in candidates:
        if self_slug and candidate.get("slug") == self_slug:
            continue                                            # never link an article to itself
        if candidate.get("slug") in excluded:
            continue                                            # ...nor to another of the caller's own pages
        if destination and candidate.get("site") and candidate["site"] != destination:
            continue                                            # internal links stay on the domain

        score, reasons = 0, []
        same_vertical = bool(vertical) and candidate.get("vertical") == vertical
        same_category = bool(destination_category) and destination_category in (candidate.get("category_ids") or [])
        if destination and candidate.get("site") == destination:
            score += 4
            reasons.append(f"same site ({destination})")
        if same_vertical:
            score += 3
            reasons.append(f"same vertical ({vertical})")
        if same_category:
            score += 3
            reasons.append("same category")
        # The article's OWN category-hub page, when that hub is live on the frontend. It is the
        # section the article will be listed on — a curated page for exactly this topic, so it is a
        # valid target even when no single published article matches (the sparse-corpus case: a
        # vertical whose first article is being written has nothing else in its category yet).
        own_hub = False
        if (destination_category and candidate.get("kind") == "category" and destination
                and candidate.get("site") == destination):
            name = category_names.get(str(destination_category), "")
            if name and _slugify(name) == candidate.get("slug"):
                own_hub = True
                score += 3
                reasons.append(f"the article's own category hub ({name})")
        if candidate.get("kind") == "article":
            score += 2
        elif candidate.get("kind") == "calculator":
            score += 1

        haystack = " ".join([str(candidate.get("title", "")), str(candidate.get("excerpt", "")),
                             " ".join(candidate.get("categories") or [])])
        overlap = sorted(target_words.intersection(_subject_tokens(haystack)))
        score += len(overlap) * 2
        if overlap:
            reasons.append("topical overlap: " + ", ".join(overlap[:4]))

        # Sharing a domain is not a reason to link. An internal link to an unrelated article costs
        # the reader's attention and dilutes the anchor, so a candidate must earn its place with the
        # destination's own curated hub (same vertical/category) or with real topical evidence: two
        # distinct subject tokens. ONE is not evidence — measured on the live corpus, a single shared
        # word ("just", "billion", "into", "test") was offering the Nvidia memory-bet story to a
        # tariff article and an ebike calculator to a piece about agent skills. When nothing
        # qualifies the article ships with no Related reading — which is the honest outcome.
        if not (same_vertical or same_category or own_hub) and len(overlap) < MIN_OVERLAP_TOKENS:
            continue
        anchor = _anchor_for(candidate, target_words)
        scored.append({
            "title": candidate.get("title"),
            "slug": candidate.get("slug"),
            "url": candidate.get("url"),
            "site": candidate.get("site"),
            "kind": candidate.get("kind", "article"),
            "anchor_text": anchor,
            "relevance_score": score,
            "why": "; ".join(reasons),
            "category": (candidate.get("categories") or [""])[0],
            "suggested_placement": (f"Link \"{anchor}\" in the section where the article touches "
                                    f"{', '.join(overlap[:3]) or 'this topic'}."),
        })

    scored.sort(key=lambda x: (-x["relevance_score"], x["title"] or ""))
    print(f"  • Internal-link candidates from {source}: {len(scored)} scored of {len(candidates)}")
    return scored[:max_links]


def extract_growth_os_knowledge(vertical, keyword=""):
    """Extract matching founder voice stances, quotes, and customer truth anecdotes."""
    founder_voice_text = FOUNDER_VOICE_FILE.read_text(encoding="utf-8") if FOUNDER_VOICE_FILE.exists() else ""
    customer_truth_text = CUSTOMER_TRUTH_FILE.read_text(encoding="utf-8") if CUSTOMER_TRUTH_FILE.exists() else ""

    # 1. Parse Founder Voice section for vertical
    founder_stances = []
    founder_quotes = []

    v_pattern = re.compile(rf"### Vertical:\s*`?{vertical}`?([\s\S]*?)(?=### Vertical:|\Z)", re.I)
    v_match = v_pattern.search(founder_voice_text)
    if v_match:
        section = v_match.group(1)
        for bullet in re.findall(r"^-\s+\*\*([^*]+)\*\*:\s*(.+)$", section, re.M):
            founder_stances.append({"topic": bullet[0].strip(), "stance": bullet[1].strip()})
        for quote in re.findall(r"^>\s*\"([^\"]+)\"\s*—\s*(.+)$", section, re.M):
            founder_quotes.append({"quote": quote[0].strip(), "author": quote[1].strip()})

    # If no vertical section match, grab universal rules
    if not founder_stances:
        founder_stances.append({
            "topic": "Pragmatic Realism",
            "stance": "Ground every claim in an architectural or economic reality rather than theoretical hype."
        })

    # 2. Parse Customer Truth anecdotes
    customer_anecdotes = []
    ct_pattern = re.compile(rf"### Vertical:\s*`?{vertical}`?([\s\S]*?)(?=### Vertical:|\Z)", re.I)
    ct_match = ct_pattern.search(customer_truth_text)
    if ct_match:
        ct_section = ct_match.group(1)
        for anec in re.findall(r"^-\s+\*\*([^*]+)\*\*:\s*([\s\S]*?)(?=(?:^-\s+\*\*|\Z))", ct_section, re.M):
            customer_anecdotes.append({
                "title": anec[0].strip(),
                "details": anec[1].strip().replace("\n", " ")
            })

    return {
        "vertical": vertical,
        "keyword": keyword,
        "founder_stances": founder_stances,
        "founder_quotes": founder_quotes,
        "customer_anecdotes": customer_anecdotes
    }


def main():
    parser = argparse.ArgumentParser(description="Growth OS Knowledge, Cannibalization & Internal Linking Engine")
    parser.add_argument("--check-cannibalization", action="store_true", help="Check keyword for cannibalization")
    parser.add_argument("--internal-links", action="store_true", help="Generate internal link map for keyword")
    parser.add_argument("--extract-pov", action="store_true", help="Extract founder voice and customer truth")
    parser.add_argument("--keyword", default="agent evaluation bottlenecks", help="Target keyword")
    parser.add_argument("--vertical", default="agentic_ai", help="Vertical ID")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if args.check_cannibalization:
        res = check_cannibalization(args.keyword, args.vertical)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Cannibalization Check] Target: '{args.keyword}'")
            print(f"Verdict: {res['verdict']}")
            print(f"Recommendation: {res['recommendation']}")
            if res["top_conflict"]:
                print(f"Top Conflict: '{res['top_conflict']['title']}' (Similarity: {res['similarity']})")
            print("")

    elif args.internal_links:
        res = generate_internal_link_map(args.keyword, args.vertical)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Internal Link Map] For '{args.keyword}' ({args.vertical}):")
            for idx, link in enumerate(res, 1):
                print(f"{idx}. [{link['anchor_text']}] -> {link['url']} ('{link['title']}')")
                print(f"   Placement: {link['suggested_placement']}")
            print("")

    elif args.extract_pov:
        res = extract_growth_os_knowledge(args.vertical, args.keyword)
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"\n[Growth OS Knowledge] Vertical: '{args.vertical}'")
            print(f"\n--- Founder Stances & Opinions ---")
            for st in res["founder_stances"]:
                print(f"• {st['topic']}: {st['stance']}")
            if res["founder_quotes"]:
                print(f"\n--- Founder Quotes ---")
                for q in res["founder_quotes"]:
                    print(f'> "{q["quote"]}" — {q["author"]}')
            if res["customer_anecdotes"]:
                print(f"\n--- Customer Truth / Field Anecdotes ---")
                for an in res["customer_anecdotes"]:
                    print(f"• {an['title']}: {an['details']}")
            print("")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
