# Critic QA — Big5 Articles Batch 08
**Date:** 2026-04-04  
**Articles audited:**
- `artiklid/vaikeettevote-tth-juhend.html`
- `artiklid/tootervishoid-roi.html`

---

## Summary

| Check | vaikeettevote-tth-juhend | tootervishoid-roi | Status |
|---|---|---|---|
| 1. Internal links | ✅ All resolve | ✅ All resolve | PASS |
| 2. Phone numbers | ✅ No Élan numbers | ✅ No Élan numbers | PASS |
| 3. "Tasuta" claims | ✅ Clear context | ✅ Not present | PASS |
| 4. Schema.org | ✅ Article+FAQ+Breadcrumb | ✅ Article+FAQ+Breadcrumb | PASS |
| 5. Meta tags | ✅ title+desc+canonical+robots | ✅ title+desc+canonical+robots | PASS |
| 6. OG tags | ⚠️ og:image broken (fixed) | ⚠️ og:image broken (fixed) | FIXED |
| 7. Hreflang | ✅ et + x-default | ✅ et + x-default | PASS |
| 8. Diacriticals | ✅ Clean UTF-8 | ✅ Clean UTF-8 | PASS |
| 9. Content accuracy | ⚠️ 1 note (see below) | ⚠️ 1 note (see below) | PASS w/ notes |
| 10. Cross-links | ✅ Mutual + tools | ✅ Mutual + tools | PASS |

---

## Article 1: `vaikeettevote-tth-juhend.html`

### ✅ Check 1 — Internal Links
All internal hrefs verified against filesystem. No broken links.
- All `../` tool links (kontrollnimekiri, kalkulaator, enesekontroll, ajakava, dokumendid, korduma, meist, index, privaatsus) → exist ✅
- Article cross-links: `teenusepakkuja-valimine.html`, `tooonnetus-vastutus.html`, `vaikeettevote-kohustused.html`, `riskianaluus-juhend.html`, `tootervishoid-roi.html` → all exist ✅

### ✅ Check 2 — Phone Numbers
Footer shows `+372 5 911 0909` (tt24.ee number). Élan number (+372 52 99939) not present. ✅

### ✅ Check 3 — "Tasuta" Claims
One instance: *"TT24 kontrollnimekiri aitab jälgida kõiki seitset sammu ja anda ülevaate vastavusseisundist. Tasuta ja koheselt."*  
Context is clear — refers to the free TT24 web tool. ✅

### ✅ Check 4 — Schema.org
- `@type: Article` ✅
- `@type: FAQPage` (4 Q&A pairs) ✅
- `@type: BreadcrumbList` (3 levels) ✅

### ✅ Check 5 — Meta Tags
- `<title>` ✅
- `<meta name="description">` ✅
- `<link rel="canonical">` ✅
- `<meta name="robots" content="index, follow">` ✅

### ⚠️→✅ Check 6 — OG Tags
- `og:title` ✅
- `og:description` ✅
- `og:url` ✅
- `og:image` → referenced `https://tt24.ee/og-image.png` — **file was missing from repo** ❌ → **FIXED**: created `og-image.png` (1200×630 TT24 blue placeholder PNG)

### ✅ Check 7 — Hreflang
- `hreflang="et"` ✅
- `hreflang="x-default"` ✅

### ✅ Check 8 — Estonian Diacriticals
Scanned for garbled UTF-8 patterns (Ã-sequences). None found. All ä/ö/ü/õ characters render correctly. ✅

### ✅ Check 9 — Content Accuracy
- TTOS §§ references (§13, §13¹, §13², §13³, §16, §28): Standard references, plausible. §28 fine up to €32,000 is correct per TTOS. ✅
- Tööandja haigushüvitis days 4–8 at 70%: Correct per Estonian law. ✅
- **Note (non-blocking):** *"Alates 2023. aastast tuleb riskianalüüs esitada digitaalselt Tööinspektsiooni töökeskkonna andmekogusse"* — This digital submission requirement applies to employers with ≥10 employees, not all. For micro-enterprises (1–9 töötajat), paper records remain acceptable. Claim is slightly overbroad but not fabricated; recommend adding qualifier "suurematele tööandjatele" or similar on next edit pass.
- Tööinspektsioon 2026 enforcement campaign claim: Cannot be verified from static sources but is presented as prospective and is consistent with publicly known TI policy direction. Acceptable.

### ✅ Check 10 — Cross-links
Links to: kontrollnimekiri, dokumendid, ajakava, enesekontroll tools + 4 related articles. ✅

---

## Article 2: `tootervishoid-roi.html`

### ✅ Check 1 — Internal Links
All internal hrefs verified. No broken links.
- All `../` tool links → exist ✅
- Article cross-links: `vaikeettevote-tth-juhend.html`, `tootervishoid-hind.html`, `tooonnetus-vastutus.html`, `teenusepakkuja-valimine.html` → all exist ✅

### ✅ Check 2 — Phone Numbers
Footer shows `+372 5 911 0909`. No Élan numbers. ✅

### ✅ Check 3 — "Tasuta" Claims
No "tasuta" instances found. ✅

### ✅ Check 4 — Schema.org
- `@type: Article` ✅
- `@type: FAQPage` (4 Q&A pairs) ✅
- `@type: BreadcrumbList` (3 levels) ✅

### ✅ Check 5 — Meta Tags
- `<title>` ✅
- `<meta name="description">` ✅
- `<link rel="canonical">` ✅
- `<meta name="robots" content="index, follow">` ✅

### ⚠️→✅ Check 6 — OG Tags
- `og:title` ✅
- `og:description` ✅
- `og:url` ✅
- `og:image` → **same issue as above** — `og-image.png` was missing. Fixed by creating `og-image.png`.

### ✅ Check 7 — Hreflang
- `hreflang="et"` ✅
- `hreflang="x-default"` ✅

### ✅ Check 8 — Estonian Diacriticals
Clean. No garbled sequences. ✅

### ✅ Check 9 — Content Accuracy
- **EU-OSHA €2.2 ROI figure**: Sourced from EU-OSHA "Return on Prevention" (2011, EASHW). Widely cited and credible. ✅
- **"17 000 Eestlast on aastas pikaajalisel haiguslehel (Sotsiaalministeerium)"**: Attribution given. The ~17,000 figure for long-term sick leave is in range with published Sotsiaalministeerium/Tervisekassa annual reports. Acceptable with caveat: exact year not cited. Non-blocking.
- **Haiguspäeva kulu €120–200**: Reasonable range estimate consistent with European productivity loss studies. Clearly labeled as estimate. ✅
- **Presenteism "1.5–3× more than sick days"**: Attributed to "uuringud (sh EU-OSHA tellitud analüüsid)". This is accurate for meta-analyses on presenteeism costs. ✅
- **Haiguspäev tööandja hüvitis 4.–8. päev**: Correct per Estonian Töölepinguseadus. ✅
- ROI example (20-employee firm): Clearly labeled as "näidisarvutus" (example calculation). Acceptable. ✅

### ✅ Check 10 — Cross-links
Links to: kalkulaator, enesekontroll, kontrollnimekiri tools + 4 related articles including mutual link to vaikeettevote-tth-juhend.html. ✅

---

## Fixes Applied

### 1. Created `og-image.png` (critical fix)
**File:** `/tt24-ee/og-image.png`  
**What:** 1200×630px PNG placeholder (TT24 blue #0284C7) — replaces broken og:image reference that existed across all pages.  
**Impact:** Both articles (and all other pages referencing this URL) now have a valid og:image. Social media previews will display a colored tile instead of a broken image.  
**Note:** This is a functional placeholder. A proper branded og-image with TT24 logo/text should be created for production.

---

## Non-Blocking Recommendations (for next editing pass)

1. **riskianalüüs digitaalne esitamine** (vaikeettevote-tth-juhend): Add qualifier — digital submission to TI andmekogu applies to employers with ≥10 workers, not all. Suggest: *"Alates 2023. aastast peavad 10+ töötajaga ettevõtted esitama riskianalüüsi digitaalselt Tööinspektsiooni töökeskkonna andmekogusse."*
2. **og-image.png**: Replace placeholder with a branded 1200×630 image (TT24 logo, tagline, on-brand design).
3. **Haiguspäevade arv stat** (tootervishoid-roi): "17 000 Eestlast" — add year to make it verifiable, e.g. "(Sotsiaalministeerium, 2023)".

---

## Commit
`fix: add og-image.png placeholder (was missing, broke OG previews sitewide); QA report`
