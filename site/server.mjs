import { createServer } from 'node:http';
import { readFile, readdir } from 'node:fs/promises';
import { join, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(fileURLToPath(new URL('.', import.meta.url)), '..');
const PORT = process.env.PORT || 3000;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
};

// Minimal markdown -> HTML (headings, paragraphs, links, bold, code). Good enough for a reader.
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
:root{color-scheme:light}
body{max-width:720px;margin:0 auto;padding:2rem 1.5rem;font:17px/1.65 -apple-system,Segoe UI,Roboto,sans-serif;color:#1a1a1a}
h1,h2,h3{line-height:1.2}a{color:#0a66c2}code{background:#f2f2f2;padding:.1em .3em;border-radius:4px}
pre{background:#f2f2f2;padding:1rem;border-radius:6px;overflow:auto}
.back{margin-bottom:1.5rem;font-size:14px}li{margin:.2em 0}
</style></head><body><p class="back"><a href="/">&larr; All articles</a></p>${body}</body></html>`;
}

const server = createServer(async (req, res) => {
  const url = new URL(req.url, 'http://localhost');
  try {
    if (url.pathname === '/api/articles.json') {
      const files = (await readdir(join(ROOT, 'published'))).filter((f) => f.endsWith('.md')).sort().reverse();
      const articles = [];
      for (const f of files) {
        const text = await readFile(join(ROOT, 'published', f), 'utf8');
        const title = (text.match(/^#\s+(.+)$/m) || [])[1] || f;
        articles.push({ slug: f.replace(/\.md$/, ''), file: f, title });
      }
      res.writeHead(200, { 'Content-Type': MIME['.json'] });
      return res.end(JSON.stringify(articles));
    }
    if (url.pathname.startsWith('/published/')) {
      const file = url.pathname.replace(/^\/published\//, '');
      const text = await readFile(join(ROOT, 'published', file), 'utf8');
      res.writeHead(200, { 'Content-Type': MIME['.html'] });
      return res.end(layout(text.split('\n')[0].replace(/^#\s+/, ''), mdToHtml(text)));
    }
    if (url.pathname === '/' || url.pathname === '/index.html') {
      const html = await readFile(join(ROOT, 'site', 'index.html'), 'utf8');
      res.writeHead(200, { 'Content-Type': MIME['.html'] });
      return res.end(html);
    }
    const staticPath = join(ROOT, 'site', url.pathname === '/' ? 'index.html' : url.pathname);
    const data = await readFile(staticPath);
    res.writeHead(200, { 'Content-Type': MIME[extname(staticPath)] || 'application/octet-stream' });
    return res.end(data);
  } catch {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    return res.end('404');
  }
});

server.listen(PORT, () => console.log(`editorial-factory site on http://localhost:${PORT}`));
