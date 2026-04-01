#!/usr/bin/env python3
"""Transform all sector pages to use modern nav/footer layout."""

import os
import re

SEKTORID_DIR = '/Users/lasagnelatte/.openclaw/workspace/tth-portaal/sektorid'

# Modern nav HTML (paths relative to sektorid/ subdir)
MODERN_HEADER = '''<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5459MHF3"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<a href="#main-content" class="skip-link">Hüppa põhisisule</a>

<header class="site-header">
  <div class="nav-inner">
    <a href="../index.html" class="nav-logo" aria-label="TT24 avaleht">
      <span class="nav-logo-text">TT24</span><span class="nav-logo-tagline">Töötervishoiu Teejuht</span>
    </a>

    <button class="nav-toggle" id="navToggle" aria-label="Menüü avamine" aria-expanded="false" aria-controls="mainNav">
      <span></span><span></span><span></span>
    </button>

    <nav id="mainNav" class="nav-links" role="navigation" aria-label="Peamenüü">
      <div class="nav-dropdown" id="toolsDropdown">
        <button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Tööriistad</button>
        <div class="nav-dropdown-menu">
          <a href="../kontrollnimekiri.html">Kontrollnimekiri</a>
          <a href="../kalkulaator.html">Kalkulaator</a>
          <a href="../enesekontroll.html">Enesehinnang</a>
          <a href="../ajakava.html">Ajakava</a>
          <a href="../dokumendid.html">Dokumendid</a>
        </div>
      </div>
      <a href="../korduma.html" class="nav-link">KKK</a>
      <a href="../meist.html" class="nav-link nav-link--secondary">Meist</a>
    </nav>

    <a href="../enesekontroll.html" class="nav-cta-btn">Kontrollin valmisolekut</a>
  </div>
</header>'''

MODERN_FOOTER = '''<section class="cta-banner">
  <div class="cta-banner-inner">
    <p>Vajate professionaalset abi töötervishoiu korraldamisega? Meie partner Valvekliinik pakub täisteenust alates €10 töötaja kohta kuus.</p>
    <p style="margin-top: 10px; font-size: 0.78rem; color: rgba(242,245,245,0.5);">Vastame 24 tunni jooksul. Ei kohusta millekski.</p>
    <a href="../pakkumine.html" class="btn-gold">Küsin pakkumist</a>
  </div>
</section>

<footer class="site-footer" role="contentinfo">
  <div class="footer-inner">

    <div class="footer-grid">

      <div class="footer-col footer-col-brand">
        <a href="../index.html" class="footer-logo" aria-label="TT24 avaleht">TT24</a>
        <p class="footer-desc">Tasuta töötervishoiu tööriistad Eesti tööandjatele.<br>Kontrollnimekirjad, kalkulaatorid ja KKK - kõik, mida vajate töötervishoiu ja tööohutuse seaduse täitmiseks.</p>
      </div>

      <div class="footer-col footer-col-links">
        <h3 class="footer-col-title">Tööriistad</h3>
        <nav aria-label="Tööriistad">
          <a href="../kontrollnimekiri.html" class="footer-link">Kontrollnimekiri</a>
          <a href="../kalkulaator.html" class="footer-link">Kulukalkulaator</a>
          <a href="../enesekontroll.html" class="footer-link">Enesehinnang</a>
          <a href="../korduma.html" class="footer-link">KKK</a>
          <a href="../ajakava.html" class="footer-link">Ajakava</a>
          <a href="../meist.html" class="footer-link">Meist</a>
          <a href="../dokumendid.html" class="footer-link">Dokumendid</a>
        </nav>
      </div>

      <div class="footer-col footer-col-contact">
        <h3 class="footer-col-title">Kontakt</h3>
        <a href="mailto:info@tt24.ee" class="footer-link footer-email">info@tt24.ee</a>
        <a href="tel:+37259110909" class="footer-link">+372 5 911 0909</a>
        <p class="footer-legal-note">See portaal annab üldist teavet. See ei asenda juriidilist nõustamist ega töötervishoiu teenust.</p>
      </div>

    </div>

    <div class="footer-bottom">
      <span class="footer-partner">Koostöös <a href="https://valvekliinik.ee" target="_blank" rel="noopener" class="footer-partner-link"><strong>Valvekliinikuga</strong></a></span>
      <span class="footer-copy">© 2026 TT24 - Töötervishoiu Teejuht</span>
    </div>

  </div>
</footer>'''

NAV_SCRIPTS = '''<script>
  var navToggle = document.getElementById('navToggle');
  var mainNav = document.getElementById('mainNav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function() {
      var isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }
  var siteHeader = document.querySelector('.site-header');
  if (siteHeader) {
    window.addEventListener('scroll', function() {
      siteHeader.classList.toggle('scrolled', window.scrollY > 8);
    }, { passive: true });
  }
  var dd = document.getElementById('toolsDropdown');
  if (dd) {
    var ddBtn = dd.querySelector('.nav-dropdown-toggle');
    ddBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      dd.classList.toggle('open');
      ddBtn.setAttribute('aria-expanded', dd.classList.contains('open'));
    });
    document.addEventListener('click', function(e) {
      if (!dd.contains(e.target)) {
        dd.classList.remove('open');
        ddBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }
</script>'''

GTM_HEAD = '''  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-5459MHF3');</script>
  <!-- End Google Tag Manager -->'''


def extract_hero_content(html):
    """Extract h1 and first p from page-hero div."""
    # Try page-hero-inner div
    hero_match = re.search(r'<div class="page-hero(?:-inner)?">.*?</div>', html, re.DOTALL)
    
    # Extract h1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html[:html.find('<main')], re.DOTALL)
    h1_text = h1_match.group(1).strip() if h1_match else ''
    
    # Extract description p (first p in page-hero area)
    hero_area = html[:html.find('<main')]
    # Find the page-hero section
    hero_start = hero_area.find('class="page-hero')
    if hero_start == -1:
        hero_start = 0
    hero_section = hero_area[hero_start:]
    
    # Get all <p> tags in hero section (skip the breadcrumb-style ones)
    p_matches = re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>', hero_section, re.DOTALL)
    desc = ''
    for p in p_matches:
        # Skip empty or very short ones, skip uppercase label-style text
        clean = re.sub(r'<[^>]+>', '', p).strip()
        if len(clean) > 40 and not clean.isupper():
            desc = clean
            break
    
    return h1_text, desc


def transform_page(filepath):
    """Transform a single sector page to use modern layout."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    filename = os.path.basename(filepath)
    print(f"Processing: {filename}")
    
    # === 1. Add GTM to head if not present ===
    if 'GTM-5459MHF3' not in html:
        html = html.replace('</head>', GTM_HEAD + '\n</head>', 1)
    
    # === 2. Extract hero h1 and description ===
    h1_text, desc_text = extract_hero_content(html)
    
    # === 3. Extract main content (from <main to </main>) ===
    main_match = re.search(r'(<main[^>]*>.*?</main>)', html, re.DOTALL)
    if main_match:
        main_content = main_match.group(1)
    else:
        print(f"  WARNING: Could not find <main> in {filename}")
        main_content = ''
    
    # === 4. Extract FAQ script if present ===
    faq_script_match = re.search(r'(<script>\s*function toggleFaq.*?</script>)', html, re.DOTALL)
    faq_script = faq_script_match.group(1) if faq_script_match else ''
    
    # === 5. Extract head content (everything between <head> and </head>) ===
    head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
    head_content = head_match.group(1) if head_match else ''
    
    # Add GTM to head if not present in head_content
    if 'GTM-5459MHF3' not in head_content:
        # Insert before </head> equivalent
        head_content = head_content + '\n' + GTM_HEAD
    
    # === 6. Build compact hero ===
    # Strip emoji and clean up h1 for id
    compact_hero = f'''<section class="hero hero--compact" aria-labelledby="page-hero-heading" style="padding: 1.5rem 0;">
    <div class="hero-inner">
      <p style="font-size:0.8rem; color:var(--text-muted); text-transform:uppercase; letter-spacing:0.08em; margin:0 0 0.5rem;">Sektorid</p>
      <h1 id="page-hero-heading" style="font-size: 1.5rem; margin: 0;">{h1_text}</h1>
      {'<p style="margin: 0.5rem 0 0; font-size: 0.95rem;">' + desc_text + '</p>' if desc_text else ''}
    </div>
  </section>'''
    
    # === 7. Remove CTA section from main_content (we'll use the modern cta-banner in footer) ===
    # The old CTA section inside main will be removed - it will be replaced by cta-banner
    main_content = re.sub(
        r'\s*<!--\s*CTA\s*-->\s*<section class="section cta-section">.*?</section>\s*',
        '\n',
        main_content,
        flags=re.DOTALL
    )
    
    # Add id="main-content" to main tag for skip link
    main_content = re.sub(r'<main>', '<main id="main-content">', main_content)
    main_content = re.sub(r'<main\s', '<main id="main-content" ', main_content)
    
    # === 8. Assemble new page ===
    new_html = f'''<!DOCTYPE html>
<html lang="et">
<head>{head_content}
</head>
<body>

{MODERN_HEADER}

{compact_hero}

{main_content}

{MODERN_FOOTER}

{faq_script}
{NAV_SCRIPTS}
</body>
</html>'''
    
    # === 9. Write transformed file ===
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"  Done: {filename} (h1: {h1_text[:60]}...)")


def main():
    files = [f for f in os.listdir(SEKTORID_DIR) if f.endswith('.html')]
    files.sort()
    print(f"Found {len(files)} HTML files in sektorid/")
    print(f"Files: {files}")
    print()
    
    for filename in files:
        filepath = os.path.join(SEKTORID_DIR, filename)
        try:
            transform_page(filepath)
        except Exception as e:
            print(f"  ERROR processing {filename}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\nAll done!")


if __name__ == '__main__':
    main()
