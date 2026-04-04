# TT24.ee Schema.org Audit — 2026-04-04

## Summary

- **Total HTML files audited:** 61
- **Pages with Organization schema:** 51/61 (83%)
- **Pages with NO schema at all:** 10 (all in `vormid/` — print documents)
- **Article pages with full schema set (Article + FAQPage + BreadcrumbList):** 40/41 (artiklid/index.html is a CollectionPage, not an article — gap is intentional)

---

## Fixes Applied (committed)

### 1. Organization name inconsistencies fixed (3 files)

| File | Was | Fixed to |
|------|-----|----------|
| `ajakava.html` | `"TT24 / Valvekliinik"` + `valvekliinik.ee` | `"TT24"` + `https://tt24.ee` |
| `kalkulaator.html` | `"TT24 / Valvekliinik"` + `valvekliinik.ee` | `"TT24"` + `https://tt24.ee` |
| `pakkumine.html` | `"Valvekliinik"` + `valvekliinik.ee` | `"TT24"` + `https://tt24.ee` |

These were nested as `seller` / `provider` Organization in SoftwareApplication and ContactPage schemas.

### 2. Missing Organization schema added (4 files)

| File | Existing schema | Added |
|------|-----------------|-------|
| `meist.html` | AboutPage + WebSite | Organization + BreadcrumbList |
| `korduma.html` | BreadcrumbList + FAQPage | Organization |
| `dokumendid.html` | BreadcrumbList | Organization |
| `kontrollnimekiri.html` | BreadcrumbList + HowTo×2 | Organization |

All added Organization blocks use canonical form:
```json
{
  "@type": "Organization",
  "name": "TT24",
  "url": "https://tt24.ee",
  "@id": "https://tt24.ee/#organization"
}
```

---

## Remaining Issues (not fixed — require review)

### A. 10 `vormid/` pages have zero schema markup

These are print-format HTML documents (forms to fill out). They have no `<nav>`, no footer, no navigation structure — they are designed to be printed.

Files affected:
- `vormid/esmaabi.html`
- `vormid/kemikaalid.html`
- `vormid/olukorra-analuus.html`
- `vormid/riskianaluus.html`
- `vormid/suunamiskiri.html`
- `vormid/teavitamine.html`
- `vormid/tervisekontroll-checklist.html`
- `vormid/tooandja-juhend.html`
- `vormid/tooonnetus.html`
- `vormid/volinik.html`

**Recommendation:** These pages are not landing pages — they are typically accessed via `dokumendid.html`. Google is unlikely to index or crawl them heavily. If they are indexed, add minimal BreadcrumbList + Organization. Otherwise, add `<meta name="robots" content="noindex">` to keep them out of search results.

### B. No telephone number in any Organization schema (global gap)

Every Organization block across all 61 pages is missing `"telephone"`. If TT24 has a contact phone, add it to the homepage Organization block and consider propagating to article/linnad/sektorid pages.

### C. `artiklid/index.html` missing FAQPage

This is the article listing page (`CollectionPage`), not a single article. FAQPage is not applicable here — this is intentional and correct.

### D. URL trailing slash inconsistency (minor)

- Article pages use `"https://tt24.ee"` (no trailing slash)
- Homepage Organization uses `"https://tt24.ee/"` (with trailing slash)
- Not a critical SEO issue as Google normalizes these, but can be standardized.

### E. `index.html` dual Organization (intentional — NOT a bug)

The homepage has two Organization blocks:
- `TT24` at `https://tt24.ee/` (primary)
- `Valvekliinik` at `https://valvekliinik.ee` (as `parentOrganization`)

This is structurally correct. Valvekliinik is the operating entity behind TT24.

---

## Schema Coverage by Page Type

| Category | Pages | Org | Article | FAQPage | Breadcrumb |
|----------|-------|-----|---------|---------|------------|
| artiklid/ | 20 | ✅ all | ✅ all | ✅ all | ✅ all |
| sektorid/ | 14 | ✅ all | ✅ all | ✅ all | ✅ all |
| linnad/ | 5 | ✅ all | ✅ all | ✅ all | ✅ all |
| vormid/ | 10 | ❌ none | ❌ none | ❌ none | ❌ none |
| Root pages | 12 | ✅ all (post-fix) | n/a | partial | partial |

---

## Audit Script

Reusable Python script at `/tmp/schema_audit.py` — run any time to regenerate this report.
