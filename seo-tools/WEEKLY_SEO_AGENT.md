# Weekly SEO Agent — autobazarsyria.com

This is the playbook the scheduled weekly agent follows. It runs autonomously on
a clone of this repo. Goal: keep the site technically healthy, expand indexable
content over time, and hand Ibra a short manual to-do for Google Search Console.

## Honest scope
- Google **deprecated sitemap ping** (2023). We cannot force Google to re-crawl
  from code. The real re-crawl lever is Search Console (manual, see step 6).
- What this agent *can* do automatically: keep the sitemap fresh, catch SEO
  regressions, add new landing pages, and report. That's the automatable 80%.

## Weekly steps

1. **Refresh the sitemap**
   `python3 seo-tools/generate_sitemap.py`
   (Re-stamps lastmod and picks up any new city/category pages.)

2. **Regression check** — fail loudly if any of these regress:
   - Every `*.html` page in root (except utility pages: confirm, reset-password,
     payment, dashboard, delete-account) has a unique `<title>`, a meta
     description, a canonical, and og tags.
   - No two indexable pages share an identical `<title>`.
   - No broken internal links: every `href="/..."` resolves to an existing
     `.html` file in the repo (or is a known clean route).
   - `robots.txt` still points to the sitemap and blocks utility pages.

3. **Content expansion (the real traffic driver)** — each week, consider ONE
   high-value addition, then implement it with `seo-tools/generate_city_pages.py`:
   - Add a new city to the `CITIES` list (e.g. Idlib, Daraa, Sweida, Hasakah,
     Quneitra, Damascus Countryside) and regenerate — 4 new pages.
   - OR add a new high-intent sub-category if the product supports it.
   Keep each page genuinely differentiated (city-specific title, hero, FAQ).
   Do NOT mass-generate thin duplicates — quality over volume. Cap growth at
   ~4 new pages/week so Google sees steady, natural expansion.

4. **Rebuild affected pages** if the template or shared copy changed, and
   re-run the sitemap generator so new pages are listed.

5. **Commit & push** on a branch, with a clear message summarizing what changed
   (sitemap refresh, N new pages, any fixes). Verify the live URLs return 200
   after GitHub Pages redeploys.

6. **Output the manual to-do for Ibra** (the part a human must do):
   - In Google Search Console: confirm the sitemap is submitted and shows the
     new URL count; use "URL Inspection → Request Indexing" on this week's new
     pages.
   - Note any pages with impressions but low CTR (title/description to improve)
     — this requires GSC data Ibra pastes in, or GSC API access if connected.
   - Flag the single biggest opportunity for next week.

## The GSC feedback loop (unlocks real targeting)
Right now the agent expands content by best guess. If Ibra connects Google
Search Console (Performance report or API), the agent can instead target the
exact queries the site already gets impressions for — far higher ROI. Until
then, treat step 3 as informed guessing, not data-driven.
