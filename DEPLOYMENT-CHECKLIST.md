# TT24 Deployment Checklist

Every new HTML page MUST complete all items before being considered done.

## Required for ALL pages

- [ ] **`<title>`** — Unique, keyword-rich, under 60 chars
- [ ] **`<meta name="description">`** — Unique, 140–160 chars
- [ ] **`<link rel="canonical">`** — Absolute URL pointing to self
- [ ] **`<link rel="alternate" hreflang="et">`** — ET language tag
- [ ] **`<link rel="alternate" hreflang="x-default">`** — Fallback tag
- [ ] **Open Graph tags** — `og:type`, `og:url`, `og:title`, `og:description`, `og:image`, `og:locale`, `og:site_name`
- [ ] **Twitter Card tags** — `twitter:card`, `twitter:title`, `twitter:description`
- [ ] **Schema.org JSON-LD** — At minimum `WebPage` or appropriate type; `BreadcrumbList` for non-home pages
- [ ] **FAQPage schema** — If page has FAQ section
- [ ] **Sitemap entry** — Added to `sitemap.xml` with correct `<lastmod>`, `<changefreq>`, `<priority>`
- [ ] **IndexNow submission** — URL submitted to IndexNow after deployment
- [ ] **Internal links** — At least 1 inbound link from an existing page (homepage or related tool)
- [ ] **Robots meta** — `index, follow` set
- [ ] **GTM** — Google Tag Manager snippet present (consent-gated)
- [ ] **Cookie banner** — TT24 cookie consent banner present
- [ ] **Header/footer** — Matches site pattern
- [ ] **Estonian language** — `lang="et"` on `<html>`, all content in Estonian
- [ ] **Mobile-responsive** — Uses `style.css`, no broken layout on narrow screens
- [ ] **Accessibility** — `skip-link`, ARIA labels on nav, buttons have labels
- [ ] **CTA** — At least one CTA pointing to `pakkumine.html`

## Priority mapping (sitemap)

| Page type | Priority |
|-----------|----------|
| Homepage | 1.0 |
| High-intent landing pages | 0.9–1.0 |
| Tool pages | 0.9 |
| Article pages | 0.8 |
| Sector/city pages | 0.7–0.8 |
| Form/document pages | 0.6 |
| Supporting pages | 0.3–0.5 |

## IndexNow key

Key: `tt24ee75090898`
Key file: `/tt24ee75090898.txt`
Script: `scripts/submit_indexnow.py`

## Deployment log

| Date | Page | Status |
|------|------|--------|
| 2026-04-05 | pakkumine.html | ✅ Done |
| 2026-04-05 | tooistad/kalkulaatori-juhend.html | ✅ Done |
