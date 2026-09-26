/**
 * site/social_voice.mjs — the observer-voice contract for social copy.
 *
 * The long-form article explains; the LinkedIn variant and the Reddit card *comment* on it. The
 * contract (canonical prose: `skills/claude_humanizer.md` §3.8) is that the speaker is one person
 * who has been reading the week's filings and news and is saying what they make of it — not the
 * author of the events, not the owner of the truth, and not the reader's advisor.
 *
 * Why a module instead of a paragraph in a SOP: this repo's fleet is LLM-driven, so anything that
 * is only stated in prose is advisory. `scripts/check_social_voice.mjs` (verify.sh §9) and the
 * dashboard smoke test both import this file, so the same rules gate the authored block and the
 * generated card the operator actually posts.
 *
 * The rules are deliberately mechanical: they cannot judge whether the take is any good, only that
 * the required observer cue is present and that the ownership/authority constructions are gone.
 */

/** Authored artifacts written before this date are grandfathered (voice was not yet specified). */
export const VOICE_ENFORCED_FROM = '2026-09-26';

/** At least one of these must appear in every social copy and in each interpreting article section. */
export const OBSERVER_CUES = [
  { label: 'first-person observation', re: /\bI(?:'ve| have|'m| am|'d| would| keep| kept| think| thought| read| watched| noticed| pulled| see| saw| hear| heard)\b/i },
  { label: 'labelled opinion', re: /\b(?:my read|my take|my sense|my view|where I(?:'ve| have) landed|what I take from)\b/i },
  {
    label: 'attention, not instruction',
    re: /\b(?:what I(?:'m| am) watching|what strikes me|the bit that stuck with me|the part I keep circling|the thing I(?:'d| would) want|curious (?:how|what|whether|if))\b/i,
  },
];

/**
 * Reader-directed commands, with an optional list marker ("- Stress test your landed costs") since
 * the social cards bulletize sentences without re-voicing them.
 */
const IMPERATIVE_VERBS = 'stress[- ]test|negotiate|match|treat|map|lock in|start|stop|build|audit'
  + '|reprice|refinance|ask|check|watch|move|shift|use|set|make|get|talk|review';
const IMPERATIVE_ADVICE = new RegExp(`^\\s*(?:[-*•]\\s*)?(?:${IMPERATIVE_VERBS})\\b`, 'im');
/** "The lesson for anyone weighing an offer: Negotiate the retirement match…" — advice after a colon.
 *  Colons only: an em-dash apposition ("the hidden layers — review labor") is not an instruction. */
const ADVICE_AFTER_COLON = new RegExp(`:\\s*(?:${IMPERATIVE_VERBS})\\b`, 'i');

/** Ownership/authority constructions. Each match fails the gate. */
export const AUTHORITY_PATTERNS = [
  { label: 'verdict framing', re: /\bthe (?:signal|real story|truth|bottom line|lesson)\s+(?:is|for)\b/i },
  { label: 'verdict framing', re: /\bthe numbers don'?t lie\b/i },
  { label: 'verdict framing', re: /\bmake no mistake\b/i },
  { label: 'consultant framing', re: /\bhere(?:'s| is) the playbook\b/i },
  { label: 'consultant framing', re: /^\s*(?:the )?playbook:/im },
  { label: 'consultant framing', re: /\bhere(?:'s| is) what you need to do\b/i },
  { label: 'consultant framing', re: /\bthe winning moves\b/i },
  { label: 'consultant framing', re: /\blet me be clear\b/i },
  { label: 'consultant framing', re: /^\s*trust me\b/im },
  { label: 'second-person instruction', re: /\byou (?:need to|must|should|have to|ought to)\b/i },
  { label: 'imperative advice', re: IMPERATIVE_ADVICE },
  { label: 'imperative advice', re: ADVICE_AFTER_COLON },
];

/**
 * True when a sentence can be quoted into social copy without tripping the rules — the generator
 * drops reader-directed sentences rather than re-voicing article prose it did not write.
 */
export function isQuoteable(sentence) {
  return inspectSocialVoice(sentence).violations.length === 0;
}

const snippet = (text, index, length = 60) =>
  String(text).slice(Math.max(0, index - 20), Math.max(0, index) + length).replace(/\s+/g, ' ').trim();

/**
 * Check one piece of social copy. Returns { ok, cue, violations: [{ label, match, snippet }] }.
 * `ok` requires both a present observer cue and zero authority constructions.
 */
export function inspectSocialVoice(text) {
  const body = String(text || '');
  const violations = [];
  for (const { label, re } of AUTHORITY_PATTERNS) {
    const match = body.match(re);
    if (match) violations.push({ label, match: match[0], snippet: snippet(body, match.index ?? 0) });
  }
  const cue = OBSERVER_CUES.find(({ re }) => re.test(body))?.label || '';
  return { ok: !!cue && violations.length === 0, cue, violations };
}

/** Human-readable one-liners for a failed inspection. */
export function describeViolations(name, inspection) {
  const lines = [];
  for (const v of inspection.violations) {
    lines.push(`${name}: ${v.label} — "${v.match}" … ${v.snippet}`);
  }
  if (!inspection.cue) {
    lines.push(`${name}: no observer cue — add one first-person observation, a labelled opinion `
      + `("My read:"), or an attention line ("What I'm watching:") per skills/claude_humanizer.md §3.8`);
  }
  return lines;
}

/** The framing lines the deterministic generator owns (Reddit variants + LinkedIn fallback). */
export const OBSERVER_FRAMING = {
  redditNumbers: '**What I pulled out of the numbers:**',
  redditRead: 'My read:',
  redditDiscussion: '**Where I keep landing on this:**',
  redditAsk: "I'm curious how others are reading this one. If you've run into the same thing, what did you do?",
  showAndTell: 'What I found:',
  linkedinFallback: '**My read:**',
};

/**
 * Long-form sections that must read as the writer's own reading of the news (skills/claude_humanizer.md
 * §3.9). The lead reports; these three interpret, so each needs an observer cue.
 */
export const INTERPRETING_SECTIONS = ['tension', 'tactical-insight', 'nuanced-takeaway'];

/** Section bodies keyed by marker name, e.g. `lead`, `tension`, `tactical-insight`. */
export function bodySections(markdown) {
  const text = String(markdown || '')
    .replace(/^---\s*[\r\n]+[\s\S]*?[\r\n]+---/, '');
  const parts = text.split(/<!--\s*(lead|tension|tactical-insight|nuanced-takeaway|tldr)\s*-->/i);
  const out = {};
  for (let i = 1; i < parts.length; i += 2) out[parts[i].toLowerCase()] = parts[i + 1] || '';
  return out;
}

/**
 * Inspect a long-form artifact: authority constructions anywhere in the reader-facing body (frontmatter,
 * `## Sources`, the `<!-- linkedin -->` block and the internal `## Gate report` excluded), plus an
 * observer cue in every interpreting section.
 */
export function inspectLongform(markdown) {
  const sections = bodySections(markdown);
  const prose = [sections.lead, sections.tension, sections['tactical-insight'],
    sections['nuanced-takeaway'], sections.tldr].filter(Boolean).join('\n\n');
  const violations = [];
  for (const { label, re } of AUTHORITY_PATTERNS) {
    const match = prose.match(re);
    if (match) violations.push({ label, match: match[0], snippet: snippet(prose, match.index ?? 0) });
  }
  const missingCues = INTERPRETING_SECTIONS.filter((name) => {
    const body = sections[name];
    if (!body) return false; // an absent section is the schema gate's business, not this one's
    return !OBSERVER_CUES.some(({ re }) => re.test(body));
  });
  return { ok: violations.length === 0 && missingCues.length === 0, violations, missingCues };
}
