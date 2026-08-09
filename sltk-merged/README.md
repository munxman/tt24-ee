# SL Tervisekeskus — Merged Site Build
**Built:** 2026-08-09  
**Source:** Merge of Build A ("last night" — emstiilid previews) + Build B ("today" — sites/sltk)  
**Output:** `sites/sltk-merged/`  
**Status:** DRAFT — noindex,nofollow on ALL pages. Do NOT deploy to live domain until Ingmar gives final approval.

---

## Page Count

| Category | Count |
|----------|-------|
| Homepage | 1 |
| Action/task pages | 13 |
| Staff page | 1 |
| Materjalid index | 1 |
| Materjalid articles | 13 |
| EN page | 1 |
| Redirect (avaldus.html → registreerumine.html) | 1 |
| **Total HTML pages** | **31** |
| Other files (CSS, JS, image, robots, sitemap) | 5 |
| **Total files** | **36** |

---

## File Inventory by Source

### From Build A (preview-1 — sage/ivory Alo style, last night)
All content preserved exactly. CSS converted from inline styles to shared stylesheet. Header/footer updated to match merged site.

**Articles (13):**
- `materjalid/kkk.html` — Korduma kippuvad küsimused (FAQ)
- `materjalid/nohu.html` — Nohu (common cold)
- `materjalid/kurguvalu.html` — Kurguvalu (sore throat)
- `materjalid/palavik-taiskasvanul.html` — Palavik täiskasvanul (fever)
- `materjalid/seljavalu.html` — Seljavalu (back pain)
- `materjalid/poiepoletik.html` — Põiepõletik (UTI)
- `materjalid/kohulahtisus.html` — Kõhulahtisus (diarrhea)
- `materjalid/kuhu-pooruda.html` — Kuhu pöörduda tervisemurega (ER red flags + routing guide)
- `materjalid/nimistusse.html` — Nimistusse registreerumine (how to join a patient list)
- `materjalid/vastuvottule-registreerimine.html` — Vastuvõtule registreerumine (how to book)
- `materjalid/toendid-ja-retseptid.html` — Tõendid ja retseptid (certificates & prescriptions)
- `materjalid/eperearstikeskus.html` — e-Perearstikeskuse kasutamine (EPAK guide)
- `materjalid/teabeallikad.html` — Soovituslikud teabeallikad (external sources)

**Asset:**
- `assets/von-baeri-maja-exterior-marek-metslaid.jpg` — Hero image (⚠️ LICENSING TBC)

### From Build B (sites/sltk — NHS action-router, today)
All pages kept intact. CSS path references already correct (`/assets/style.css`).

**Action pages (13):**
- `broneerimine.html` — Broneeri vastuvõtule (book appointment)
- `registreerumine.html` — Registreeru nimistusse (patient list registration + on-site form)
- `retseptid.html` — Kordusretsept (repeat prescription)
- `toovoimetusleht.html` — Töövõimetusleht (sick leave)
- `analyysid.html` — Analüüside tulemused (test results)
- `toendid.html` — Tervisetõendid (health certificates + Valvekliinik redirect)
- `hinnakiri.html` — Hinnakiri (price list)
- `kontakt.html` — Kontakt (contact + map)
- `toovaline-aeg.html` — Töövälisel ajal (after-hours guide)
- `valistootajale.html` — Välistöötajale (for foreign workers — ET)
- `privaatsuspoliitika.html` — Privaatsuspoliitika (privacy policy — GDPR)
- `vilepuhuja.html` — Vilepuhuja kaitse (whistleblower law)
- `personal.html` — Personal (staff page — Build B version used, more complete)

**EN page:**
- `en/for-foreign-workers.html` — For foreign workers (EN)

**Infrastructure:**
- `assets/style.css` — Shared merged stylesheet (Build B base + Build A article components)
- `assets/main.js` — Shared JS (mobile nav, FAQ accordion, form validation)
- `robots.txt` — Disallow all (draft protection)
- `sitemap.xml` — Full sitemap (updated to include all 13 materjalid articles)

### New in merged build
- `index.html` — Homepage: Build B action-router structure + Build A sage hero image treatment
- `materjalid.html` — Comprehensive materjalid index listing all 13 articles with descriptions
- `avaldus.html` — Redirect to `registreerumine.html` (Build B's form is the canonical one)

---

## Design System

| Token | Value | Usage |
|-------|-------|-------|
| `--clr-sage` | `#9BAD95` | Primary brand color, logo, hero background, step numbers |
| `--clr-laguun` | `#2E7D74` | CTA buttons, links, highlights |
| `--clr-aprikoos` | `#E08A4E` | Warning states |
| `--clr-warm` | `#FAF7F1` | Section alternating backgrounds |
| Font | Poppins 400/500/600/700/800 | All text |
| Logo | `sl` (sage) + `tervisekeskus` (ink) | Poppins 800, -0.04em tracking |

---

## Navigation Structure

```
[Emergency bar: 1220 · 5 911 0909 · Valvekliinik]
[Logo: sl tervisekeskus] → /

Teenused ▾
  Broneeri vastuvõtule → /broneerimine.html
  Kordusretsept → /retseptid.html
  Töövõimetusleht → /toovoimetusleht.html
  Analüüside tulemused → /analyysid.html
  Tervisetõendid → /toendid.html
  Töövälisel ajal → /toovaline-aeg.html
Personal → /personal.html
[Registreeru nimistusse] → /registreerumine.html  (CTA button)
Hinnakiri → /hinnakiri.html
Materjalid → /materjalid.html
Kontakt → /kontakt.html
ET / EN / RU / FI
```

**Patient journey to clinical info (max 2 clicks):**
1. Homepage → "Teabeallikad ja juhendid" tile → `materjalid.html`
2. `materjalid.html` → any of 13 articles

**Patient journey to task (max 1 click):**
- Homepage → any action tile → task page

---

## Placeholders Requiring Ingmar's Confirmation

| Item | File(s) | Priority |
|------|---------|----------|
| Google Analytics Measurement ID (G-XXXXXXXXXX) | All pages | High |
| info@sltervisekeskus.ee — create on Zone hosting | `registreerumine.html`, `vilepuhuja.html` | High — needed for form submission |
| Eva-Maria Sentifoli's preferred public name (Sentifoli or Sentifoli-Saluveer?) | `personal.html` | Medium |
| Staff photos — permission from each employee before publishing | `personal.html` | Medium |
| Prices from 01.09.2026 — same or updated? | `hinnakiri.html`, `toendid.html` | High — must confirm before publish |
| Whistleblower contact email + phone | `vilepuhuja.html` | Legal obligation — required for launch |
| Privacy policy data protection contact email | `privaatsuspoliitika.html` | Legal — required for launch |
| Hero photo licensing — von Baeri maja (Marek Metslaid) | `index.html`, assets/ | Must resolve before public launch |
| EPAK / article content clinical review before publish | All `materjalid/*.html` | Medical — required before launch |

---

## Deployment Checklist

| Item | Status |
|------|--------|
| `<meta name="robots" content="noindex,nofollow">` on ALL pages | ✅ PASS |
| Shared stylesheet (`/assets/style.css`) on all pages | ✅ PASS |
| Schema.org MedicalClinic on homepage | ✅ PASS |
| Schema.org BreadcrumbList on article + action pages | ✅ PASS |
| hreflang (ET/EN/x-default) on homepage | ✅ PASS |
| Canonical URLs on all pages | ✅ PASS |
| OG tags on homepage and action pages | ✅ PASS |
| Twitter Card meta on homepage and action pages | ✅ PASS |
| sitemap.xml (all 31 pages included) | ✅ PASS |
| robots.txt (Disallow: / — draft) | ✅ PASS |
| Mobile nav with hamburger | ✅ PASS |
| Mobile floating CTA bar | ✅ PASS |
| No Perekliinik brand mentions | ✅ PASS |
| No "4x faster regain" or banned figures | ✅ N/A (medical clinic, not GLP-1) |
| No Cleveland Clinic citations | ✅ N/A |
| No fabricated statistics | ✅ PASS (all stats from NHS.uk with attribution) |
| GA4 placeholder G-XXXXXXXXXX in place | ✅ (placeholder — needs real ID) |
| Epp Vessel — neutral wording, no availability claims | ✅ PASS |
| Nimistu numbers removed from all doctor listings | ✅ PASS |
| No "Dr." prefix on doctor names | ✅ PASS |
| No "uus perearstikeskus" phrasing | ✅ PASS |
| "SL Tervisekeskus" always on one line (white-space:nowrap) | ✅ PASS |
| "pöörduge perearsti poole" banned — uses "pöörduge meie poole" | ✅ PASS |
| No "Usaldusväärsed" in headings — plain "Teabeallikad" | ✅ PASS |
| Section "Materjalid" not "Usaldusväärsed teabeallikad" | ✅ PASS |
| Staff team OFF front page — lives only on personal.html | ✅ PASS |

**Items that MUST be resolved before deployment (make live):**
1. Create info@sltervisekeskus.ee on Zone hosting
2. Replace G-XXXXXXXXXX with actual GA4 Measurement ID
3. Confirm / update price list for 01.09.2026
4. Confirm whistleblower contact details
5. Confirm privacy policy data contact email
6. Get photo permissions from all staff
7. Resolve hero photo licensing (von Baeri maja photo)
8. Clinical review of all 13 materjalid articles by Ingmar/doctor
9. Activate robots.txt (Allow: /) and remove noindex meta tags

---

## Technical Notes

- All links use absolute paths (`/page.html`) — compatible with any web server root
- Article pages in `materjalid/` use `/assets/` (root-relative) paths — requires web server at domain root
- `avaldus.html` redirects to `registreerumine.html` (the canonical form page)
- `robots.txt` currently set to `Disallow: /` — safe draft protection
- Article medical content is UNCHANGED from Build A — no text was modified
- All 13 articles carry the Build A `draft-badge` ("Mustand, kliiniline ülevaatus enne avaldamist")
