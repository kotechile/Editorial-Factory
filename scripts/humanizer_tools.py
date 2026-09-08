"""Shared helpers for the Loop 3 humanizer scripts: a compliance-retry loop that, when a
rewrite fails the topic-agnostic accessibility gate, feeds the exact FAIL reasons back to
the frontier model and re-prompts (up to MAX_ATTEMPTS).

Import with:  import humanizer_tools as ht   (scripts/ is on sys.path when these run).
"""
import json
import pathlib
import urllib.request

MODEL = "gemini-3.1-pro-preview"
MAX_ATTEMPTS = 5  # how many times to re-prompt the model before holding at Loop 3
MAX_TOKENS = 20000  # thinking-model budget: reasoning tokens count against this, so keep high


def _key():
    KEY = None
    for envf in ["/root/.hermes/profiles/stylist/.env", "/root/.hermes/.env"]:
        p = pathlib.Path(envf)
        if p.exists():
            for line in p.read_text().splitlines():
                if line.startswith("GOOGLE_API_KEY="):
                    KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
        if KEY:
            break
    assert KEY, "GOOGLE_API_KEY not found"
    return KEY


URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={_key()}"


def call_gemini(prompt, max_tokens=MAX_TOKENS, temperature=0.7, timeout=240):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens, "temperature": temperature},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        j = json.loads(r.read().decode())
    return j["candidates"][0]["content"]["parts"][0]["text"].strip()


def measure(path):
    """Return the structured accessibility diagnosis for a written article file."""
    import sys
    scripts_dir = str(pathlib.Path(__file__).parent)
    if scripts_dir not in sys.path:
        sys.path.insert(0, scripts_dir)
    import check_accessibility as ca
    return ca.measure(path)


def retry_prompt(base_prompt, prev_text, diag, extra: str | list[str] = ""):
    """Build a follow-up prompt telling the frontier model exactly what the gate rejected."""
    notes = []
    if diag["fails"]:
        notes.append("FAILURES (must be fixed):")
        notes += [f"- {f}" for f in diag["fails"]]
    if diag["warnings"]:
        notes.append("ADVISORY (should be fixed):")
        notes += [f"- {w}" for w in diag["warnings"]]
    tip = []
    if diag["undefined_acronyms"]:
        tip.append("Spell out each listed acronym in full at its first use (e.g. 'Full Name (ACR)').")
    if diag["flesch"] is not None and diag["flesch"] < diag["target"]:
        tip.append("Raise readability: split long sentences, prefer plain verbs over noun phrases, cut filler clauses.")
    if diag["flesch"] is not None and diag["flesch"] < diag["floor"]:
        tip.append("The text is still too dense for a general reader. TARGET: sentences of ~15 words or fewer — "
                   "strictly split any sentence over 20 words into two. One idea per sentence; drop conjunctive "
                   "clauses ('which', 'while', 'as', 'and that'). Shorten the wording, not the facts.")
    if tip:
        notes.append("HOW: " + " ".join(tip))
    if extra:
        notes.append("STRUCTURE/FORMAT:")
        notes += [f"- {x}" for x in extra] if isinstance(extra, list) else [f"- {extra}"]
    feedback = "\n".join(notes)
    return (base_prompt
            + "\n\n--- PREVIOUS ATTEMPT (this version FAILED the accessibility gate) ---\n"
            + prev_text
            + "\n\n--- REVIEWER FEEDBACK ---\n"
            + feedback
            + "\n\nRewrite the ENTIRE article to fix every FAILURE and ADVISORY above. Do not reuse "
              "the previous attempt unchanged. Preserve all facts, every [n] citation, and the "
              "## Sources list VERBATIM. Return the full article in the same OUTPUT FORMAT.")
