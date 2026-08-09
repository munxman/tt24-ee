# SL Tervisekeskus — v2 Site Build

**Built:** 2026-08-09  
**Status:** DRAFT / Noindex — awaiting Ingmar approval before production deploy

## Design Source
- **Visual design:** preview-1 (`/.openclaw/tmp/tt24-push/emstiilid/preview-1/`) — sage/petrol palette, Poppins ExtraBold, approved by Ingmar + Eva-Maria
- **Homepage content:** action-router tiles from `sltk-merged/index.html`
- **Subpage content:** preview-1 articles as-is; new service pages from `sltk-merged/` restyled

## Page Count: 30 HTML pages

### Root pages (16)
| File | Description |
|------|-------------|
| `index.html` | Homepage: preview-1 hero + action-router tiles (compact, no phone, no language sentence) |
| `personal.html` | Staff: nurses, doctors, management (from preview-1) |
| `avaldus.html` | Registration form (from preview-1 with updated nav) |
| `materjalid.html` | Resources index (preview-1 category cards) |
| `broneerimine.html` | Book appointment (new, EPAK-first) |
| `retseptid.html` | Repeat prescription (new, EPAK-first) |
| `toovoimetusleht.html` | Sick leave (new, EPAK-first) |
| `analyysid.html` | Test results (new) |
| `toendid.html` | Health certificates (new, with subtle VK redirect) |
| `toovaline-aeg.html` | After hours guide (new) |
| `registreerumine.html` | Patient list registration (new, with form) |
| `hinnakiri.html` | Price list (new) |
| `kontakt.html` | Contact (new) |
| `privaatsuspoliitika.html` | Privacy policy (new) |
| `vilepuhuja.html` | Whistleblower policy (new) |
| `valistootajale.html` | For foreign workers (ET, links to EN) |

### English (1)
| File | Description |
|------|-------------|
| `en/for-foreign-workers.html` | Foreign workers guide (EN) |

### Materjalid articles (13)
| File | Description |
|------|-------------|
| `materjalid/kkk.html` | FAQ |
| `materjalid/nohu.html` | Common cold |
| `materjalid/kurguvalu.html` | Sore throat |
| `materjalid/kohulahtisus.html` | Diarrhoea |
| `materjalid/palavik-taiskasvanul.html` | Fever in adults |
| `materjalid/poiepoletik.html` | Cystitis (women) |
| `materjalid/seljavalu.html` | Back pain |
| `materjalid/kuhu-pooruda.html` | Where to seek care |
| `materjalid/eperearstikeskus.html` | e-Perearstikeskus guide |
| `materjalid/nimistusse.html` | How to register on patient list |
| `materjalid/vastuvottule-registreerimine.html` | How to book an appointment |
| `materjalid/toendid-ja-retseptid.html` | Certificates and prescriptions |
| `materjalid/teabeallikad.html` | Information sources |

## Assets
```
assets/style.css       — Shared CSS (preview-1 design tokens + all component styles)
assets/main.js         — Mobile hamburger menu
assets/von-baeri-maja-exterior-marek-metslaid.jpg — Hero photo (LICENSING TBC before public launch)
```

## Key Design Decisions
- **Colors:** `--petrol: #9BAD95` (header bg), `--teal: #6E8A68` (CTAs, accents), `--dark-bg: #1A1C1A` (footer)
- **Font:** Poppins 300/400/500/600/700/800 (Google Fonts)
- **Nav structure:** Desktop nav in `var(--petrol)` header bar; mobile hamburger with full-screen overlay
- All paths are **relative** (no `/` absolute paths, safe for GitHub Pages subdirectory deploy)
- All pages: `noindex,nofollow` until launch
- Schema.org MedicalClinic on homepage and kontakt.html

## Placeholders to Confirm Before Launch
- `[INGMAR TO CONFIRM]` markers in: `toendid.html`, `hinnakiri.html`, `kontakt.html`, `vilepuhuja.html`, `privaatsuspoliitika.html`
- Google Analytics ID: `G-XXXXXXXXXX` on all pages
- Hero photo licensing: Marek Metslaid / von Baeri maja — confirm rights
- Email address `info@sltervisekeskus.ee` — confirm Zone hosting setup
- Whistleblower channel (email/phone) — fill in `vilepuhuja.html`
- Price list validity date: `01.09.2026` — confirm

## Nav Structure
```
Teenused ▾ (Broneeri vastuvõtule | Kordusretsept | Töövõimetusleht | Analüüside tulemused | Tervisetõendid | Töövälisel ajal)
Personal
Hinnakiri
Materjalid
Kontakt
[Registreeru nimistusse] CTA
ET | EN | RU | FI
```
RU and FI links currently point to `#` (placeholder for future pages).
