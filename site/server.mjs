import { createServer } from 'node:http';
import { readFile, writeFile, readdir, mkdir, unlink } from 'node:fs/promises';
import { existsSync, readFileSync } from 'node:fs';
import { join, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);
const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..');
const PORT = process.env.PORT || 3000;

const VERTICALS_FILE = join(ROOT, 'context', 'verticals.json');
const PERSONAS_FILE = join(ROOT, 'context', 'personas.json');
const CALENDAR_FILE = join(ROOT, 'context', 'content_calendar.md');
const ENV_FILE = join(ROOT, '.env');

// Load repo-level .env if present and not in process.env
function loadEnv() {
  if (existsSync(ENV_FILE)) {
    try {
      const content = readFileSync(ENV_FILE, 'utf8');
      for (const line of content.split('\n')) {
        const trimmed = line.trim();
        if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
          const idx = trimmed.indexOf('=');
          const k = trimmed.slice(0, idx).trim();
          const v = trimmed.slice(idx + 1).trim().replace(/^['"]|['"]$/g, '');
          if (!process.env[k]) {
            process.env[k] = v;
          }
        }
      }
    } catch (e) {
      console.warn('Could not parse .env:', e.message);
    }
  }
}
loadEnv();

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
};

function getSupabaseConfig() {
  const url = (process.env.SUPABASE_URL || '').replace(/\/$/, '');
  const key = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY || '';
  return { url, key, isConfigured: Boolean(url && key) };
}

async function supabaseFetch(path, options = {}) {
  const { url, key, isConfigured } = getSupabaseConfig();
  if (!isConfigured) throw new Error('Supabase not configured');

  const headers = {
    'apikey': key,
    'Authorization': `Bearer ${key}`,
    'Content-Type': 'application/json',
    'Prefer': 'return=representation,resolution=merge-duplicates',
    ...(options.headers || {}),
  };

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 3500);

  try {
    const res = await fetch(`${url}/rest/v1/${path}`, {
      ...options,
      headers,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);

    if (!res.ok) {
      const txt = await res.text();
      throw new Error(`Supabase error ${res.status}: ${txt}`);
    }
    const text = await res.text();
    return text ? JSON.parse(text) : null;
  } catch (err) {
    clearTimeout(timeoutId);
    throw err;
  }
}

// Minimal markdown -> HTML helper for reader
function mdToHtml(md) {
  const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const lines = md.split(/\r?\n/);
  const out = [];
  let para = [];
  const flush = () => { if (para.length) { out.push(`<p>${para.join(' ')}</p>`); para = []; } };
  const inline = (s) => esc(s)
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  for (const line of lines) {
    if (/^#{1,6}\s/.test(line)) { flush(); const m = line.match(/^(#{1,6})\s+(.*)/); const lvl = m[1].length; out.push(`<h${lvl}>${inline(m[2])}</h${lvl}>`); }
    else if (/^[-*]\s/.test(line)) { flush(); out.push(`<li>${inline(line.replace(/^[-*]\s/, ''))}</li>`); }
    else if (/^\s*$/.test(line)) { flush(); }
    else { para.push(inline(line)); }
  }
  flush();
  return out.join('\n');
}

function layout(title, body) {
  return `<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<style>
:root{color-scheme:light dark;--bg:#0f172a;--card:#1e293b;--text:#f8fafc;--muted:#94a3b8;--border:#334155;--accent:#38bdf8}
@media(prefers-color-scheme:light){:root{--bg:#f8fafc;--card:#ffffff;--text:#0f172a;--muted:#64748b;--border:#e2e8f0;--accent:#0284c7}}
body{max-width:760px;margin:0 auto;padding:2.5rem 1.5rem;font:17px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--text)}
h1,h2,h3{line-height:1.25;color:var(--text)}a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
code{background:var(--border);padding:.15em .4em;border-radius:4px;font-size:0.9em}
pre{background:var(--card);border:1px solid var(--border);padding:1.2rem;border-radius:8px;overflow:auto}
.back{margin-bottom:2rem;font-size:14px;font-weight:600}
li{margin:.35em 0}
</style></head><body><p class="back"><a href="/">&larr; Return to PressFlow Dashboard</a></p>${body}</body></html>`;
}

function formatHumanCadence(cadenceStr) {
  const parts = (cadenceStr || '').trim().split(/\s+/);
  if (parts.length >= 5) {
    const [minute, hour, dom, month, dow] = parts;
    const hInt = parseInt(hour, 10);
    const h12 = isNaN(hInt) ? 6 : (hInt === 0 ? 12 : (hInt > 12 ? hInt - 12 : hInt));
    const amPm = !isNaN(hInt) && hInt >= 12 ? 'PM' : 'AM';
    const mStr = String(parseInt(minute, 10) || 0).padStart(2, '0');
    const timeStr = `${h12}:${mStr} ${amPm} EST`;

    const dayMap = { '0': 'Sun', '1': 'Mon', '2': 'Tue', '3': 'Wed', '4': 'Thu', '5': 'Fri', '6': 'Sat', '7': 'Sun' };
    if (dow === '*') return `Daily ${timeStr}`;
    const days = dow.split(',').map((d) => dayMap[d] || d);
    return `${days.join(' + ')} ${timeStr}`;
  }
  return cadenceStr;
}

async function updateCalendarMarkdown(verticals) {
  try {
    let existingLog = '## Run log\n| Date | Vertical | Result | Notes |\n|---|---|---|---|\n';
    if (existsSync(CALENDAR_FILE)) {
      const content = await readFile(CALENDAR_FILE, 'utf8');
      if (content.includes('## Run log')) {
        existingLog = content.slice(content.indexOf('## Run log'));
      }
    }

    const lines = [
      '# Content Calendar',
      '',
      'Cadence per vertical. The Editor-in-Chief dispatches the Radar Scout on these schedules.',
      '',
      '| Vertical | Cadence | Schedule (EST) | Status |',
      '|---|---|---|---|',
    ];

    for (const v of verticals) {
      lines.push(`| ${v.id} | ${v.cadence || '0 6 * * 1'} | ${formatHumanCadence(v.cadence)} | active |`);
    }

    lines.push('');
    lines.push(existingLog.trim());
    lines.push('');

    await writeFile(CALENDAR_FILE, lines.join('\n'), 'utf8');
  } catch (err) {
    console.error('Error updating content calendar markdown:', err);
  }
}

async function getLocalVerticals() {
  if (existsSync(VERTICALS_FILE)) {
    try {
      const content = await readFile(VERTICALS_FILE, 'utf8');
      const data = JSON.parse(content);
      return data.verticals || [];
    } catch (e) {
      console.error('Error reading verticals file:', e.message);
    }
  }
  return [];
}

async function saveLocalVerticals(verticals) {
  const contextDir = join(ROOT, 'context');
  if (!existsSync(contextDir)) {
    await mkdir(contextDir, { recursive: true });
  }
  await writeFile(VERTICALS_FILE, JSON.stringify({ verticals }, null, 2), 'utf8');
  await updateCalendarMarkdown(verticals);
}

async function getLocalPersonas() {
  if (existsSync(PERSONAS_FILE)) {
    try {
      const content = await readFile(PERSONAS_FILE, 'utf8');
      const data = JSON.parse(content);
      return data.personas || {};
    } catch (e) {
      console.error('Error reading personas file:', e.message);
    }
  }
  return {};
}

async function saveLocalPersonas(personas) {
  const contextDir = join(ROOT, 'context');
  if (!existsSync(contextDir)) {
    await mkdir(contextDir, { recursive: true });
  }
  await writeFile(PERSONAS_FILE, JSON.stringify({ personas }, null, 2), 'utf8');
}

// Request Body Parser
function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', (chunk) => { body += chunk; });
    req.on('end', () => {
      try {
        resolve(body ? JSON.parse(body) : {});
      } catch (err) {
        reject(err);
      }
    });
    req.on('error', reject);
  });
}

function sendJson(res, statusCode, data) {
  res.writeHead(statusCode, {
    'Content-Type': MIME['.json'],
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  });
  res.end(JSON.stringify(data));
}

// Frontmatter parser for markdown articles
function parseFrontmatter(markdown) {
  if (!markdown) return {};
  const fmMatch = markdown.match(/^---\s*[\r\n]+([\s\S]*?)[\r\n]+---/);
  if (!fmMatch) return {};
  const data = {};
  const lines = fmMatch[1].split(/\r?\n/);
  for (const line of lines) {
    const m = line.match(/^([a-zA-Z0-9_-]+)\s*:\s*(.*)$/);
    if (!m) continue;
    const key = m[1].trim();
    let rawVal = m[2].trim();
    if (rawVal.startsWith('[') && rawVal.endsWith(']')) {
      try {
        data[key] = JSON.parse(rawVal);
      } catch (e) {
        data[key] = rawVal.slice(1, -1).split(',').map((s) => s.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
      }
    } else if ((rawVal.startsWith('"') && rawVal.endsWith('"')) || (rawVal.startsWith("'") && rawVal.endsWith("'"))) {
      data[key] = rawVal.slice(1, -1);
    } else if (!isNaN(Number(rawVal)) && rawVal !== '') {
      data[key] = Number(rawVal);
    } else if (rawVal.toLowerCase() === 'true') {
      data[key] = true;
    } else if (rawVal.toLowerCase() === 'false') {
      data[key] = false;
    } else {
      data[key] = rawVal;
    }
  }
  return data;
}

const server = createServer(async (req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);

  // Handle CORS preflight
  if (req.method === 'OPTIONS') {
    res.writeHead(204, {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    });
    return res.end();
  }

  try {
    // ----------------------------------------------------
    // API: Drafts & Library Management (PressFlow Workspace)
    // ----------------------------------------------------
    if (url.pathname === '/api/drafts' && req.method === 'GET') {
      const draftsDir = join(ROOT, 'context', 'drafts');
      const pubDir = join(ROOT, 'published');
      const allFiles = [];

      if (existsSync(draftsDir)) {
        // Hide the raw *_draft.md intermediates so each story shows once (the *_final.md).
        const dFiles = (await readdir(draftsDir)).filter((f) => f.endsWith('.md') && !f.endsWith('_draft.md'));
        for (const f of dFiles) {
          allFiles.push({ file: f, path: join(draftsDir, f), type: 'draft' });
        }
      }

      if (existsSync(pubDir)) {
        const pFiles = (await readdir(pubDir)).filter((f) => f.endsWith('.md'));
        for (const f of pFiles) {
          allFiles.push({ file: f, path: join(pubDir, f), type: 'published' });
        }
      }

      const items = [];
      for (const item of allFiles) {
        try {
          const text = await readFile(item.path, 'utf8');
          const fm = parseFrontmatter(text);
          const title = fm.title || (text.match(/^#\s+(.+)$/m) || [])[1] || item.file;
          const vertical = fm.vertical || 'general';
          const date = fm.date || (item.file.match(/^([0-9]{4}-[0-9]{2}-[0-9]{2})/) || [])[1] || '';
          const wordCount = text.split(/\s+/).filter(Boolean).length;
          const readTime = Math.max(1, Math.round(wordCount / 220));

          items.push({
            file: item.file,
            title,
            slug: fm.slug || item.file.replace(/\.md$/, ''),
            type: item.type,
            vertical,
            persona: fm.persona || fm.target_persona || 'eng_leader',
            date,
            wordCount,
            readTime,
            primary_keyword: fm.primary_keyword || '',
            secondary_keywords: Array.isArray(fm.secondary_keywords) ? fm.secondary_keywords : [],
            search_volume: fm.search_volume || null,
            search_intent: fm.search_intent || '',
            keyword_difficulty: fm.keyword_difficulty || null,
            meta_title: fm.meta_title || '',
            meta_description: fm.meta_description || '',
          });
        } catch (e) {
          console.warn('Error parsing draft:', item.file, e.message);
        }
      }

      items.sort((a, b) => b.file.localeCompare(a.file));
      return sendJson(res, 200, items);
    }

    if (url.pathname === '/api/drafts/detail' && req.method === 'GET') {
      const file = url.searchParams.get('file');
      if (!file) return sendJson(res, 400, { error: 'Missing file query param' });

      const draftsDir = join(ROOT, 'context', 'drafts');
      const pubDir = join(ROOT, 'published');
      let targetPath = join(draftsDir, file);
      if (!existsSync(targetPath)) targetPath = join(pubDir, file);

      if (!existsSync(targetPath)) {
        return sendJson(res, 404, { error: 'Draft not found' });
      }

      const text = await readFile(targetPath, 'utf8');
      const fm = parseFrontmatter(text);
      const title = fm.title || (text.match(/^#\s+(.+)$/m) || [])[1] || file;
      const vertical = fm.vertical || 'agentic_ai';
      const wordCount = text.split(/\s+/).filter(Boolean).length;
      const readTime = Math.max(1, Math.round(wordCount / 220));

      return sendJson(res, 200, {
        file,
        title,
        slug: fm.slug || file.replace(/\.md$/, ''),
        vertical,
        persona: fm.persona || fm.target_persona || 'eng_leader',
        date: fm.date || '',
        wordCount,
        readTime,
        primary_keyword: fm.primary_keyword || '',
        secondary_keywords: Array.isArray(fm.secondary_keywords) ? fm.secondary_keywords : [],
        search_volume: fm.search_volume || null,
        search_intent: fm.search_intent || '',
        keyword_difficulty: fm.keyword_difficulty || null,
        meta_title: fm.meta_title || '',
        meta_description: fm.meta_description || '',
        markdown: text,
      });
    }

    if (url.pathname === '/api/drafts/save' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const { file, markdown } = body;
      if (!file || !markdown) return sendJson(res, 400, { error: 'Missing file or markdown content' });

      const safeName = file.replace(/[^a-zA-Z0-9_\-\.]/g, '');
      const draftsDir = join(ROOT, 'context', 'drafts');
      if (!existsSync(draftsDir)) await mkdir(draftsDir, { recursive: true });

      const targetPath = join(draftsDir, safeName.endsWith('.md') ? safeName : `${safeName}.md`);
      await writeFile(targetPath, markdown, 'utf8');

      return sendJson(res, 200, { status: 'ok', file: safeName });
    }

    if (url.pathname === '/api/generate-suite' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const { markdown, articleUrl, promoUrl } = body;
      if (!markdown) return sendJson(res, 400, { error: 'Missing markdown content' });

      // Extract LinkedIn section if marker exists
      let linkedin = '';
      if (markdown.includes('<!-- linkedin -->')) {
        linkedin = markdown.split('<!-- linkedin -->')[1].trim();
      } else {
        const leadMatch = markdown.match(/<!-- lead -->([\s\S]*?)(?:<!--|$)/);
        const tacticalMatch = markdown.match(/<!-- tactical-insight -->([\s\S]*?)(?:<!--|$)/);
        const lead = leadMatch ? leadMatch[1].trim() : '';
        const tactical = tacticalMatch ? tacticalMatch[1].trim() : '';
        linkedin = `${lead}\n\nKey takeaways:\n${tactical}`;
      }

      // Append URLs if provided and not already present
      if (articleUrl && !linkedin.includes(articleUrl)) {
        linkedin += `\n\n📖 Read the full illustrated breakdown: ${articleUrl}`;
      }
      if (promoUrl && !linkedin.includes(promoUrl)) {
        linkedin += `\n🛠️ Try the live tool: ${promoUrl}`;
      }

      // Generate TL;DR
      let tldr = '';
      if (markdown.includes('<!-- tldr -->')) {
        tldr = markdown.split('<!-- tldr -->')[1].split('##')[0].trim();
      }

      // Twitter / X thread (split into 3-4 punchy tweets)
      const paras = markdown
        .replace(/<!--[\s\S]*?-->/g, '')
        .replace(/^#+.*$/gm, '')
        .split(/\n\s*\n/)
        .map((p) => p.trim())
        .filter((p) => p.length > 50);

      const tweets = paras.slice(0, 4).map((p, idx) => `${idx + 1}/ ${p.slice(0, 270)}...`);

      return sendJson(res, 200, {
        status: 'ok',
        linkedin_post: linkedin,
        tldr,
        twitter_thread: tweets,
      });
    }

    if (url.pathname === '/api/linkedin-sync' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const { slug, headline, post_copy, vertical, article_url } = body;
      const sbConfig = getSupabaseConfig();

      if (!sbConfig.isConfigured) {
        return sendJson(res, 200, { status: 'mocked', message: 'Supabase not configured; simulated queue save.' });
      }

      try {
        const row = {
          post_copy: post_copy || '',
          target_vertical: vertical || 'general',
          article_url: article_url || '',
          slug: slug || 'article',
          status: 'queued',
          created_at: new Date().toISOString(),
        };
        await supabaseFetch('linkedin_posts', {
          method: 'POST',
          body: JSON.stringify(row),
        });
        return sendJson(res, 200, { status: 'ok', message: 'Queued to Supabase linkedin_posts' });
      } catch (err) {
        return sendJson(res, 500, { error: err.message });
      }
    }

    // ----------------------------------------------------
    // API: Published Articles
    // ----------------------------------------------------
    if (url.pathname === '/api/articles.json' && req.method === 'GET') {
      const pubDir = join(ROOT, 'published');
      const files = existsSync(pubDir)
        ? (await readdir(pubDir)).filter((f) => f.endsWith('.md')).sort().reverse()
        : [];
      const articles = [];
      for (const f of files) {
        const text = await readFile(join(pubDir, f), 'utf8');
        const title = (text.match(/^#\s+(.+)$/m) || [])[1] || f;
        const wordCount = text.split(/\s+/).filter(Boolean).length;
        const readTime = Math.max(1, Math.round(wordCount / 220));
        articles.push({ slug: f.replace(/\.md$/, ''), file: f, title, wordCount, readTime });
      }
      return sendJson(res, 200, articles);
    }

    // ----------------------------------------------------
    // API: Delete Article / Draft
    // ----------------------------------------------------
    if ((url.pathname.startsWith('/api/drafts/') || url.pathname === '/api/drafts') && req.method === 'DELETE') {
      const file = url.searchParams.get('file') || url.pathname.replace(/^\/api\/drafts\/?/, '');
      if (!file) return sendJson(res, 400, { error: 'Missing file parameter' });

      const safeName = file.replace(/[^a-zA-Z0-9_\-\.]/g, '');
      const draftsDir = join(ROOT, 'context', 'drafts');
      const pubDir = join(ROOT, 'published');
      let targetPath = join(draftsDir, safeName);
      if (!existsSync(targetPath)) targetPath = join(pubDir, safeName);

      if (!existsSync(targetPath)) {
        return sendJson(res, 404, { error: `File '${safeName}' not found.` });
      }

      await unlink(targetPath);

      // Clean up companion _draft or _final if it exists in context/drafts
      if (safeName.endsWith('_final.md')) {
        const companionPath = join(draftsDir, safeName.replace('_final.md', '_draft.md'));
        if (existsSync(companionPath)) {
          try { await unlink(companionPath); } catch (e) {}
        }
      } else if (safeName.endsWith('_draft.md')) {
        const companionPath = join(draftsDir, safeName.replace('_draft.md', '_final.md'));
        if (existsSync(companionPath)) {
          try { await unlink(companionPath); } catch (e) {}
        }
      }

      const sbConfig = getSupabaseConfig();
      if (sbConfig.isConfigured) {
        try {
          const slug = safeName.replace(/\.md$/, '').replace(/_final$/, '').replace(/_draft$/, '');
          await supabaseFetch(`articles?slug=eq.${encodeURIComponent(slug)}`, { method: 'DELETE' });
        } catch (e) {
          console.warn('[Supabase] Warning deleting article record:', e.message);
        }
      }

      return sendJson(res, 200, { status: 'ok', deleted: safeName });
    }

    // ----------------------------------------------------
    // API: Personas CRUD & Settings
    // ----------------------------------------------------
    if (url.pathname === '/api/personas') {
      const sbConfig = getSupabaseConfig();
      if (req.method === 'GET') {
        const personas = await getLocalPersonas();
        return sendJson(res, 200, { status: 'ok', personas });
      }

      if (req.method === 'POST') {
        const body = await parseJsonBody(req);
        const { id, label, reader_level, tone, wants } = body;
        if (!id || !label) {
          return sendJson(res, 400, { error: "Fields 'id' and 'label' are required." });
        }

        const slug = id.trim().toLowerCase().replace(/[^a-z0-9_]/g, '_');
        const personas = await getLocalPersonas();

        if (personas[slug]) {
          return sendJson(res, 409, { error: `Persona with ID '${slug}' already exists.` });
        }

        const newPersona = {
          label: label.trim(),
          reader_level: (reader_level || '').trim(),
          tone: (tone || '').trim(),
          wants: (wants || '').trim(),
        };

        personas[slug] = newPersona;
        await saveLocalPersonas(personas);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch('editorial_personas', {
              method: 'POST',
              body: JSON.stringify({
                id: slug,
                ...newPersona,
                updated_at: new Date().toISOString(),
              }),
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing created persona:', e.message);
          }
        }

        return sendJson(res, 201, { status: 'ok', id: slug, persona: newPersona });
      }
    }

    if (url.pathname.startsWith('/api/personas/')) {
      const subpath = decodeURIComponent(url.pathname.replace(/^\/api\/personas\//, ''));
      const sbConfig = getSupabaseConfig();

      if (req.method === 'PUT') {
        const body = await parseJsonBody(req);
        const personas = await getLocalPersonas();

        if (!personas[subpath]) {
          return sendJson(res, 404, { error: `Persona '${subpath}' not found.` });
        }

        const existing = personas[subpath];
        const updated = {
          label: body.label !== undefined ? body.label.trim() : existing.label,
          reader_level: body.reader_level !== undefined ? body.reader_level.trim() : existing.reader_level,
          tone: body.tone !== undefined ? body.tone.trim() : existing.tone,
          wants: body.wants !== undefined ? body.wants.trim() : existing.wants,
        };

        personas[subpath] = updated;
        await saveLocalPersonas(personas);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch(`editorial_personas?id=eq.${encodeURIComponent(subpath)}`, {
              method: 'PATCH',
              body: JSON.stringify({
                ...updated,
                updated_at: new Date().toISOString(),
              }),
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing updated persona:', e.message);
          }
        }

        return sendJson(res, 200, { status: 'ok', id: subpath, persona: updated });
      }

      if (req.method === 'DELETE') {
        const personas = await getLocalPersonas();
        if (!personas[subpath]) {
          return sendJson(res, 404, { error: `Persona '${subpath}' not found.` });
        }

        delete personas[subpath];
        await saveLocalPersonas(personas);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch(`editorial_personas?id=eq.${encodeURIComponent(subpath)}`, {
              method: 'DELETE',
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing deleted persona:', e.message);
          }
        }

        return sendJson(res, 200, { status: 'ok', deleted: subpath });
      }
    }

    // ----------------------------------------------------
    // API: Verticals CRUD & Settings
    // ----------------------------------------------------
    if (url.pathname === '/api/verticals') {
      const sbConfig = getSupabaseConfig();

      if (req.method === 'GET') {
        const personas = await getLocalPersonas();
        let verticals = await getLocalVerticals();
        let storageMode = sbConfig.isConfigured ? 'supabase' : 'local';

        if (sbConfig.isConfigured) {
          try {
            const remoteVerts = await supabaseFetch('editorial_verticals?select=*&order=id.asc');
            if (Array.isArray(remoteVerts) && remoteVerts.length > 0) {
              verticals = remoteVerts.map((r) => ({
                id: r.id,
                label: r.label || r.id,
                cadence: r.cadence || '0 6 * * 1',
                sources: r.sources || [],
                primary_angles: r.primary_angles || [],
                target_persona: r.target_persona || 'eng_leader',
                enable_dataforseo: r.enable_dataforseo !== undefined ? r.enable_dataforseo : true,
              }));
              // update local mirror
              await saveLocalVerticals(verticals);
            }
          } catch (e) {
            console.warn('[Supabase] Could not fetch remote verticals, using local cache:', e.message);
            storageMode = 'local_cache (supabase offline)';
          }
        }

        return sendJson(res, 200, {
          status: 'ok',
          storage_mode: storageMode,
          supabase_configured: sbConfig.isConfigured,
          verticals,
          personas,
        });
      }

      if (req.method === 'POST') {
        const body = await parseJsonBody(req);
        const { id, label, cadence, target_persona, sources, primary_angles, enable_dataforseo } = body;

        if (!id || !label) {
          return sendJson(res, 400, { error: "Fields 'id' and 'label' are required." });
        }

        const slug = id.trim().toLowerCase().replace(/[^a-z0-9_]/g, '_');
        const verticals = await getLocalVerticals();

        if (verticals.some((v) => v.id === slug)) {
          return sendJson(res, 409, { error: `Vertical with ID '${slug}' already exists.` });
        }

        const newVertical = {
          id: slug,
          label: label.trim(),
          cadence: (cadence || '0 6 * * 1').trim(),
          target_persona: (target_persona || 'eng_leader').trim(),
          sources: Array.isArray(sources) ? sources : [],
          primary_angles: Array.isArray(primary_angles) ? primary_angles : [],
          enable_dataforseo: enable_dataforseo !== undefined ? Boolean(enable_dataforseo) : true,
        };

        verticals.push(newVertical);
        await saveLocalVerticals(verticals);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch('editorial_verticals', {
              method: 'POST',
              body: JSON.stringify({
                ...newVertical,
                is_active: true,
                updated_at: new Date().toISOString(),
              }),
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing created vertical:', e.message);
          }
        }

        return sendJson(res, 201, { status: 'ok', vertical: newVertical });
      }
    }

    // PUT /api/verticals/:id  &  DELETE /api/verticals/:id
    if (url.pathname.startsWith('/api/verticals/')) {
      const subpath = url.pathname.replace(/^\/api\/verticals\//, '');
      const sbConfig = getSupabaseConfig();

      // Action routes
      if (subpath === 'sync-crons' && req.method === 'POST') {
        try {
          const { stdout, stderr } = await execFileAsync('python3', [join(ROOT, 'scripts', 'sync_crons.py')], { cwd: ROOT });
          return sendJson(res, 200, { status: 'ok', stdout, stderr });
        } catch (err) {
          return sendJson(res, 500, { error: err.message, stdout: err.stdout, stderr: err.stderr });
        }
      }

      if (subpath === 'push-supabase' && req.method === 'POST') {
        try {
          const { stdout, stderr } = await execFileAsync('python3', [join(ROOT, 'scripts', 'sync_verticals.py'), 'push'], { cwd: ROOT });
          return sendJson(res, 200, { status: 'ok', stdout, stderr });
        } catch (err) {
          return sendJson(res, 500, { error: err.message, stdout: err.stdout, stderr: err.stderr });
        }
      }

      if (subpath === 'pull-supabase' && req.method === 'POST') {
        try {
          const { stdout, stderr } = await execFileAsync('python3', [join(ROOT, 'scripts', 'sync_verticals.py'), 'pull'], { cwd: ROOT });
          return sendJson(res, 200, { status: 'ok', stdout, stderr });
        } catch (err) {
          return sendJson(res, 500, { error: err.message, stdout: err.stdout, stderr: err.stderr });
        }
      }

      const targetId = decodeURIComponent(subpath);

      if (req.method === 'PUT') {
        const body = await parseJsonBody(req);
        const verticals = await getLocalVerticals();
        const index = verticals.findIndex((v) => v.id === targetId);

        if (index === -1) {
          return sendJson(res, 404, { error: `Vertical '${targetId}' not found.` });
        }

        const existing = verticals[index];
        const updated = {
          ...existing,
          label: body.label !== undefined ? body.label.trim() : existing.label,
          cadence: body.cadence !== undefined ? body.cadence.trim() : existing.cadence,
          target_persona: body.target_persona !== undefined ? body.target_persona.trim() : existing.target_persona,
          sources: Array.isArray(body.sources) ? body.sources : existing.sources,
          primary_angles: Array.isArray(body.primary_angles) ? body.primary_angles : existing.primary_angles,
          enable_dataforseo: body.enable_dataforseo !== undefined ? Boolean(body.enable_dataforseo) : (existing.enable_dataforseo !== undefined ? existing.enable_dataforseo : true),
        };

        verticals[index] = updated;
        await saveLocalVerticals(verticals);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch(`editorial_verticals?id=eq.${encodeURIComponent(targetId)}`, {
              method: 'PATCH',
              body: JSON.stringify({
                label: updated.label,
                cadence: updated.cadence,
                target_persona: updated.target_persona,
                sources: updated.sources,
                primary_angles: updated.primary_angles,
                enable_dataforseo: updated.enable_dataforseo,
                updated_at: new Date().toISOString(),
              }),
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing updated vertical:', e.message);
          }
        }


        return sendJson(res, 200, { status: 'ok', vertical: updated });
      }

      if (req.method === 'DELETE') {
        const verticals = await getLocalVerticals();
        const initialLen = verticals.length;
        const filtered = verticals.filter((v) => v.id !== targetId);

        if (filtered.length === initialLen) {
          return sendJson(res, 404, { error: `Vertical '${targetId}' not found.` });
        }

        await saveLocalVerticals(filtered);

        if (sbConfig.isConfigured) {
          try {
            await supabaseFetch(`editorial_verticals?id=eq.${encodeURIComponent(targetId)}`, {
              method: 'DELETE',
            });
          } catch (e) {
            console.warn('[Supabase] Warning syncing deleted vertical:', e.message);
          }
        }

        return sendJson(res, 200, { status: 'ok', deleted: targetId });
      }
    }

    // ----------------------------------------------------
    // API: SEO Content Machine & Growth OS
    // ----------------------------------------------------
    if (url.pathname === '/api/seo/gsc-opportunities' && req.method === 'GET') {
      const vertical = url.searchParams.get('vertical') || 'all';
      try {
        const { stdout } = await execFileAsync('python3', [
          join(ROOT, 'scripts', 'gsc_analyzer.py'),
          '--vertical', vertical,
          '--json'
        ], { cwd: ROOT });
        const parsed = JSON.parse(stdout);
        return sendJson(res, 200, parsed);
      } catch (err) {
        return sendJson(res, 500, { error: err.message, stderr: err.stderr });
      }
    }

    if (url.pathname === '/api/seo/dataforseo-enrich' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const { keyword } = body;
      if (!keyword) return sendJson(res, 400, { error: 'Missing keyword in body' });

      try {
        const { stdout } = await execFileAsync('python3', [
          join(ROOT, 'scripts', 'dataforseo_client.py'),
          '--keyword', keyword,
          '--json'
        ], { cwd: ROOT });
        const parsed = JSON.parse(stdout);
        return sendJson(res, 200, parsed);
      } catch (err) {
        return sendJson(res, 500, { error: err.message, stderr: err.stderr });
      }
    }

    if (url.pathname === '/api/seo/growth-os') {
      const fvPath = join(ROOT, 'context', 'growth_os', 'founder-voice.md');
      const ctPath = join(ROOT, 'context', 'growth_os', 'customer-truth.md');
      const plPath = join(ROOT, 'context', 'growth_os', 'performance_learnings.md');

      if (req.method === 'GET') {
        const founderVoice = existsSync(fvPath) ? await readFile(fvPath, 'utf8') : '';
        const customerTruth = existsSync(ctPath) ? await readFile(ctPath, 'utf8') : '';
        const performanceLearnings = existsSync(plPath) ? await readFile(plPath, 'utf8') : '';

        return sendJson(res, 200, {
          status: 'ok',
          founder_voice: founderVoice,
          customer_truth: customerTruth,
          performance_learnings: performanceLearnings,
        });
      }

      if (req.method === 'POST') {
        const body = await parseJsonBody(req);
        const { founder_voice, customer_truth } = body;

        const gDir = join(ROOT, 'context', 'growth_os');
        if (!existsSync(gDir)) await mkdir(gDir, { recursive: true });

        if (founder_voice !== undefined) {
          await writeFile(fvPath, founder_voice, 'utf8');
        }
        if (customer_truth !== undefined) {
          await writeFile(ctPath, customer_truth, 'utf8');
        }

        return sendJson(res, 200, { status: 'ok', message: 'Growth OS knowledge updated successfully' });
      }
    }

    if (url.pathname === '/api/seo/sitemap' && req.method === 'GET') {
      const smPath = join(ROOT, 'context', 'sitemap.json');
      if (existsSync(smPath)) {
        const data = JSON.parse(await readFile(smPath, 'utf8'));
        return sendJson(res, 200, data);
      }
      return sendJson(res, 200, { articles: [], base_url: 'https://editorialfactory.io' });
    }

    if (url.pathname === '/api/seo/run-pipeline' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const { query, vertical, force, run_humanizer } = body;

      const args = [join(ROOT, 'scripts', 'seo_machine.py')];
      if (query) args.push('--query', query);
      if (vertical) args.push('--vertical', vertical);
      if (force) args.push('--force');
      if (run_humanizer === false) args.push('--no-humanize');

      try {
        const { stdout, stderr } = await execFileAsync('python3', args, { cwd: ROOT });
        return sendJson(res, 200, { status: 'ok', stdout, stderr });
      } catch (err) {
        return sendJson(res, 500, { error: err.message, stdout: err.stdout, stderr: err.stderr });
      }
    }

    if (url.pathname === '/api/seo/performance-report' && req.method === 'GET') {
      const perfPath = join(ROOT, 'context', 'gsc_performance.json');
      if (existsSync(perfPath)) {
        const data = JSON.parse(await readFile(perfPath, 'utf8'));
        return sendJson(res, 200, data);
      }
      return sendJson(res, 200, { articles_tracked: [] });
    }

    if (url.pathname === '/api/seo/sync-supabase' && req.method === 'POST') {
      const body = await parseJsonBody(req);
      const args = [join(ROOT, 'scripts', 'sync_articles.py')];
      if (body && body.all) args.push('--all');
      else if (body && body.drafts) args.push('--drafts');

      try {
        const { stdout, stderr } = await execFileAsync('python3', args, { cwd: ROOT });
        return sendJson(res, 200, { status: 'ok', stdout, stderr });
      } catch (err) {
        return sendJson(res, 500, { error: err.message, stdout: err.stdout, stderr: err.stderr });
      }
    }
    // Article Reader Page
    // ----------------------------------------------------
    if (url.pathname.startsWith('/published/')) {
      const file = url.pathname.replace(/^\/published\//, '');
      const text = await readFile(join(ROOT, 'published', file), 'utf8');
      res.writeHead(200, { 'Content-Type': MIME['.html'] });
      const firstLine = text.split('\n')[0].replace(/^#\s+/, '');
      return res.end(layout(firstLine, mdToHtml(text)));
    }

    // ----------------------------------------------------
    // Static Files & Main App
    // ----------------------------------------------------
    if (url.pathname === '/' || url.pathname === '/index.html') {
      const html = await readFile(join(ROOT, 'site', 'index.html'), 'utf8');
      res.writeHead(200, { 'Content-Type': MIME['.html'] });
      return res.end(html);
    }

    const staticPath = join(ROOT, 'site', url.pathname.replace(/^\//, ''));
    if (existsSync(staticPath)) {
      const data = await readFile(staticPath);
      res.writeHead(200, { 'Content-Type': MIME[extname(staticPath)] || 'application/octet-stream' });
      return res.end(data);
    }

    sendJson(res, 404, { error: 'Not found' });
  } catch (err) {
    console.error('Server error:', err);
    sendJson(res, 500, { error: 'Internal server error', details: err.message });
  }
});

server.listen(PORT, () => {
  const sb = getSupabaseConfig();
  console.log(`\n======================================================`);
  console.log(`PressFlow Editorial Dashboard on http://localhost:${PORT}`);
  console.log(`Storage Mode: ${sb.isConfigured ? '🟢 Supabase (' + sb.url + ')' : '🟡 Local JSON (context/verticals.json)'}`);
  console.log(`======================================================\n`);
});
