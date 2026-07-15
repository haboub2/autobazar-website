# -*- coding: utf-8 -*-
"""SEO regression check for autobazarsyria.com.
Run: `python3 seo-tools/check_seo.py`  (exits non-zero if anything is wrong)

Validates the indexable pages so the weekly automation fails loudly when SEO
regresses. Checks: unique <title>, present meta description + canonical + og,
and no broken internal links. Utility/app pages are skipped."""
import os, glob, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP = {"confirm", "reset-password", "payment", "dashboard",
        "delete-account", "404", "_ad_temp"}

def indexable_html():
    for f in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        name = os.path.basename(f)[:-5]
        if name not in SKIP:
            yield f, name

def existing_routes():
    """Clean routes that internal links may point to (file exists)."""
    routes = {"/"}
    for f in glob.glob(os.path.join(ROOT, "*.html")):
        routes.add("/" + os.path.basename(f)[:-5])
    return routes

def main():
    errors = []
    titles = {}
    routes = existing_routes()

    for f, name in indexable_html():
        html = open(f, encoding="utf-8").read()

        m = re.search(r"<title>(.*?)</title>", html, re.S)
        title = m.group(1).strip() if m else None
        if not title:
            errors.append(f"{name}.html: missing <title>")
        else:
            titles.setdefault(title, []).append(name)

        if not re.search(r'<meta\s+name="description"', html):
            errors.append(f"{name}.html: missing meta description")
        if not re.search(r'<link\s+rel="canonical"', html):
            errors.append(f"{name}.html: missing canonical")
        if not re.search(r'<meta\s+property="og:title"', html):
            errors.append(f"{name}.html: missing og:title")

        # internal links: href="/something" must resolve to an existing route
        for href in re.findall(r'href="(/[^"#?]*)"', html):
            route = href.rstrip("/") or "/"
            if route in routes or route == "/":
                continue
            # allow known non-html assets / dirs
            if re.search(r"\.(png|jpg|jpeg|svg|ico|css|js|xml|webmanifest)$", route):
                continue
            errors.append(f"{name}.html: broken internal link -> {href}")

    for title, pages in titles.items():
        if len(pages) > 1:
            errors.append(f"duplicate <title> on {pages}: {title!r}")

    if errors:
        print(f"SEO CHECK FAILED — {len(errors)} issue(s):")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("SEO check passed — all indexable pages OK.")

if __name__ == "__main__":
    main()
