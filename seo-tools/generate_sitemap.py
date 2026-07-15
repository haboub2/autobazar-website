# -*- coding: utf-8 -*-
"""Regenerate sitemap.xml for autobazarsyria.com.
Run: `python3 seo-tools/generate_sitemap.py`

Enumerates the static hub/legal pages plus every city x category landing page
in the repo root. <lastmod> reflects each page's REAL last-modified date (from
git history, falling back to filesystem mtime) — never a blanket "today", so
Google keeps trusting the lastmod signal and the file only changes when pages
actually change. Used by the weekly SEO automation."""
import os, glob, subprocess, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOMAIN = "https://autobazarsyria.com"
TODAY = datetime.date.today().isoformat()

CATS = ["cars", "real-estate", "farms", "car-rental"]

# (path, changefreq, priority)
STATIC = [
    ("/", "weekly", "1.00"),
    ("/cars", "weekly", "0.90"),
    ("/real-estate", "weekly", "0.90"),
    ("/farms", "weekly", "0.90"),
    ("/car-rental", "weekly", "0.90"),
    ("/support", "monthly", "0.70"),
    ("/privacy", "yearly", "0.30"),
    ("/terms", "yearly", "0.30"),
]

def path_to_file(path):
    """Map a clean URL path to its source .html file."""
    name = "index" if path == "/" else path.strip("/")
    return os.path.join(ROOT, f"{name}.html")

def lastmod_for(path):
    """Real last-modified date: git commit date, else file mtime, else today."""
    f = path_to_file(path)
    if not os.path.exists(f):
        return TODAY
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", os.path.basename(f)],
            cwd=ROOT, capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    return datetime.date.fromtimestamp(os.path.getmtime(f)).isoformat()

def city_pages():
    """Discover generated city landing pages in the repo root."""
    out = []
    for cat in CATS:
        for f in sorted(glob.glob(os.path.join(ROOT, f"{cat}-*.html"))):
            slug = os.path.basename(f)[:-5]  # strip .html
            out.append((f"/{slug}", "weekly", "0.80"))
    return out

def url_block(path, freq, prio):
    return (f"  <url>\n"
            f"    <loc>{DOMAIN}{path}</loc>\n"
            f"    <lastmod>{lastmod_for(path)}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{prio}</priority>\n"
            f"  </url>")

def main():
    entries = STATIC + city_pages()
    body = "\n".join(url_block(*e) for e in entries)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n"
           "</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    print(f"Wrote sitemap.xml with {len(entries)} URLs")

if __name__ == "__main__":
    main()
