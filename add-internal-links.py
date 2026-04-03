#!/usr/bin/env python3
"""Add internal linking sections to all tt24.ee articles and tool pages."""

import os
import re

BASE = "/Users/lasagnelatte/.openclaw/workspace/tth-portaal"
ARTIKLID = os.path.join(BASE, "artiklid")

def make_article_link(href, title, desc):
    return (
        f'    <a href="{href}" class="seotud-link" style="flex:1;min-width:200px;padding:var(--space-3);'
        f'border:1px solid var(--color-border);border-radius:var(--radius-md);text-decoration:none;'
        f'color:var(--color-text);">\n'
        f'      <strong>{title}</strong><br>\n'
        f'      <span style="font-size:var(--text-sm);color:var(--color-text-muted);">{desc}</span>\n'
        f'    </a>'
    )

def make_article_section(links_html):
    return (
        '\n\n  <section style="margin-top:var(--space-8);padding-top:var(--space-6);'
        'border-top:1px solid var(--color-border);">\n'
        '    <h2 style="font-size:var(--text-lg);margin-bottom:var(--space-3);">Seotud teemad</h2>\n'
        '    <div style="display:flex;flex-wrap:wrap;gap:var(--space-3);">\n'
        + links_html + '\n'
        '    </div>\n'
        '  </section>'
    )

def make_tool_section(links_html, heading="Kasulikud artiklid"):
    return (
        '\n<!-- Kasulikud artiklid -->\n'
        '<section style="max-width:800px;margin:var(--space-8) auto;padding:0 var(--space-4);">\n'
        f'  <h2 style="font-size:var(--text-lg);margin-bottom:var(--space-3);">{heading}</h2>\n'
        '  <div style="display:flex;flex-wrap:wrap;gap:var(--space-3);">\n'
        + links_html + '\n'
        '  </div>\n'
        '</section>'
    )

def make_tool_article_link(href, title, desc):
    return (
        f'    <a href="{href}" class="seotud-link" style="flex:1;min-width:200px;padding:var(--space-3);'
        f'border:1px solid var(--color-border);border-radius:var(--radius-md);text-decoration:none;'
        f'color:var(--color-text);">\n'
        f'      <strong>{title}</strong><br>\n'
        f'      <span style="font-size:var(--text-sm);color:var(--color-text-muted);">{desc}</span>\n'
        f'    </a>'
    )

# ─────────────────────────────────────────────────────────────────────────────
# ARTICLE CROSS-LINKS
# Each entry: filename -> list of (href, title, description)
# ─────────────────────────────────────────────────────────────────────────────
ARTICLE_LINKS = {
    "7-levinumat-viga.html": [
        ("vaikeettevote-kohustused.html", "Töötervishoiu kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("tootervishoid-kontroll-puudub.html", "Mis juhtub, kui kontrolli pole", "Trahvid ja vastutus puuduvate kontrollide eest"),
        ("riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha nõuetekohane riskianalüüs"),
        ("ttos-2026-muudatused.html", "TTOS 2026 muudatused", "Mis muutus töötervishoiu seaduses"),
    ],
    "kas-vaja-lepingut.html": [
        ("uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida teha esimesest tööpäevast alates"),
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("teenusepakkuja-valimine.html", "Kuidas valida teenusepakkujat", "Mida vaadata enne lepingu sõlmimist"),
        ("lepingu-ulesuitlemine.html", "Kuidas leping üles öelda", "Lepingu lõpetamise kord ja tähtajad"),
    ],
    "kaugtoo-tootervishoid.html": [
        ("riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha nõuetekohane riskianalüüs"),
        ("tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida teha esimesest tööpäevast alates"),
    ],
    "lepingu-ulesuitlemine.html": [
        ("kas-vaja-lepingut.html", "Kas mul on vaja lepingut", "Kiire kontroll - kas leping on kohustuslik"),
        ("teenusepakkuja-valimine.html", "Kuidas valida uus teenusepakkuja", "Mida vaadata enne lepingu sõlmimist"),
        ("teenusepakkujate-vordlus.html", "Teenusepakkujate võrdlus 2026", "Hinnad ja tingimused eri pakkujatel"),
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude kalkulatsioon"),
    ],
    "riskianaluus-juhend.html": [
        ("tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
        ("kaugtoo-tootervishoid.html", "Kaugtöö töötervishoiu nõuded", "Kohustused kaugtöötajate puhul"),
        ("tootervishoid-kontroll-puudub.html", "Mis juhtub, kui kontrolli pole", "Tagajärjed puuduvate riskianalüüside eest"),
        ("ttos-2026-muudatused.html", "TTOS 2026 muudatused", "Mis muutus töötervishoiu seaduses"),
    ],
    "teenusepakkuja-valimine.html": [
        ("teenusepakkujate-vordlus.html", "Teenusepakkujate võrdlus 2026", "Hinnad ja tingimused eri pakkujatel"),
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude kalkulatsioon"),
        ("kas-vaja-lepingut.html", "Kas mul on vaja lepingut", "Kiire kontroll - kas leping on kohustuslik"),
        ("lepingu-ulesuitlemine.html", "Kuidas leping üles öelda", "Lepingu lõpetamise kord ja tähtajad"),
    ],
    "teenusepakkujate-vordlus.html": [
        ("teenusepakkuja-valimine.html", "Kuidas valida teenusepakkujat", "Mida vaadata enne lepingu sõlmimist"),
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude kalkulatsioon"),
        ("tootervishoid-maksud.html", "Kas kulud on tulumaksuvabad", "Maksueelised töötervishoiu kuludel"),
        ("lepingu-ulesuitlemine.html", "Kuidas leping üles öelda", "Lepingu lõpetamise kord ja tähtajad"),
    ],
    "tooonnetus-vastutus.html": [
        ("riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas ennetada tööõnnetusi riskianalüüsiga"),
        ("tootervishoid-kontroll-puudub.html", "Mis juhtub, kui kontrolli pole", "Tagajärjed puuduvate tervisekontrollide eest"),
        ("tootaja-keeldub-tervisekontrollist.html", "Töötaja keeldub tervisekontrollist", "Mida teha, kui töötaja keeldub"),
        ("tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
    ],
    "tootaja-keeldub-tervisekontrollist.html": [
        ("tootervishoid-kontroll-puudub.html", "Mis juhtub, kui kontrolli pole", "Tagajärjed puuduvate tervisekontrollide eest"),
        ("tooonnetus-vastutus.html", "Tööõnnetus ja vastutus", "Tööandja vastutus ilma tervisekontrollita"),
        ("7-levinumat-viga.html", "7 levinumat viga", "Sagedased vead töötervishoiu korraldamisel"),
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
    ],
    "tootervishoid-dokumentatsioon.html": [
        ("riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas koostada nõuetekohane riskianalüüs"),
        ("tootervishoid-kontroll-puudub.html", "Mis juhtub, kui dokumente pole", "Tagajärjed puuduvate dokumentide eest"),
        ("tootervishoid-maksud.html", "Kas kulud on tulumaksuvabad", "Maksueelised töötervishoiu kuludel"),
        ("ttos-2026-muudatused.html", "TTOS 2026 muudatused", "Millised dokumendid on nüüd kohustuslikud"),
    ],
    "tootervishoid-hind.html": [
        ("tootervishoid-maksud.html", "Kas kulud on tulumaksuvabad", "Maksueelised töötervishoiu kuludel"),
        ("teenusepakkujate-vordlus.html", "Teenusepakkujate võrdlus 2026", "Hinnad ja tingimused eri pakkujatel"),
        ("teenusepakkuja-valimine.html", "Kuidas valida teenusepakkujat", "Mida vaadata enne lepingu sõlmimist"),
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
    ],
    "tootervishoid-kontroll-puudub.html": [
        ("tootaja-keeldub-tervisekontrollist.html", "Töötaja keeldub tervisekontrollist", "Mida teha, kui töötaja keeldub"),
        ("tooonnetus-vastutus.html", "Tööõnnetus ja vastutus", "Vastutus ilma korralikult korraldatud tervisekontrollita"),
        ("7-levinumat-viga.html", "7 levinumat viga", "Sagedased vead töötervishoiu korraldamisel"),
        ("tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
    ],
    "tootervishoid-maksud.html": [
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude kalkulatsioon"),
        ("teenusepakkujate-vordlus.html", "Teenusepakkujate võrdlus 2026", "Hinnad ja tingimused eri pakkujatel"),
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida teha esimesest tööpäevast alates"),
    ],
    "ttos-2026-muudatused.html": [
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha seadusele vastav riskianalüüs"),
        ("7-levinumat-viga.html", "7 levinumat viga", "Sagedased vead töötervishoiu korraldamisel"),
        ("uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida teha esimesest tööpäevast alates"),
    ],
    "uus-ettevote-tootervishoid.html": [
        ("vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
        ("kas-vaja-lepingut.html", "Kas mul on vaja lepingut", "Kiire kontroll - kas leping on kohustuslik"),
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja esimese aasta kulud"),
        ("teenusepakkuja-valimine.html", "Kuidas valida teenusepakkujat", "Mida vaadata enne lepingu sõlmimist"),
    ],
    "vaikeettevote-kohustused.html": [
        ("uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida teha esimesest tööpäevast alates"),
        ("tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud väikeettevõttele"),
        ("kas-vaja-lepingut.html", "Kas mul on vaja lepingut", "Kiire kontroll - kas leping on kohustuslik"),
        ("ttos-2026-muudatused.html", "TTOS 2026 muudatused", "Mis muutus töötervishoiu seaduses"),
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# Process articles
# ─────────────────────────────────────────────────────────────────────────────
updated_articles = 0
for filename, links in ARTICLE_LINKS.items():
    filepath = os.path.join(ARTIKLID, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has section
    if "Seotud teemad" in content or "Loe lisaks" in content:
        print(f"SKIP (already has section): {filename}")
        continue

    links_html = "\n".join(make_article_link(href, title, desc) for href, title, desc in links)
    section = make_article_section(links_html)

    # Insert before closing </article>
    if "  </article>" in content:
        content = content.replace("  </article>", section + "\n\n  </article>", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK: {filename}")
        updated_articles += 1
    else:
        print(f"WARNING: no </article> found in {filename}")

# ─────────────────────────────────────────────────────────────────────────────
# TOOL PAGE LINKS (from tth-portaal root, links prefix "artiklid/")
# ─────────────────────────────────────────────────────────────────────────────
TOOL_LINKS = {
    "kalkulaator.html": [
        ("artiklid/tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude selgitus"),
        ("artiklid/teenusepakkujate-vordlus.html", "Teenusepakkujate võrdlus 2026", "Hinnad ja tingimused eri pakkujatel"),
        ("artiklid/tootervishoid-maksud.html", "Kas kulud on tulumaksuvabad", "Maksueelised töötervishoiu kuludel"),
        ("artiklid/vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
    ],
    "enesekontroll.html": [
        ("artiklid/uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida peab tegema esimesest päevast alates"),
        ("artiklid/tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude võrdlus"),
        ("artiklid/7-levinumat-viga.html", "7 levinumat viga", "Sagedased vead töötervishoiu korraldamisel"),
        ("artiklid/vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
    ],
    "kontrollnimekiri.html": [
        ("artiklid/uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Mida peab tegema esimesest päevast alates"),
        ("artiklid/tootervishoid-hind.html", "Töötervishoiu teenuse hind", "Hinnavahemikud ja kulude võrdlus"),
        ("artiklid/riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha nõuetekohane riskianalüüs"),
        ("artiklid/tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
    ],
    "dokumendid.html": [
        ("artiklid/tootervishoid-dokumentatsioon.html", "Töötervishoiu dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
        ("artiklid/riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha nõuetekohane riskianalüüs"),
        ("artiklid/ttos-2026-muudatused.html", "TTOS 2026 muudatused", "Mis muutus töötervishoiu seaduses"),
        ("artiklid/tootervishoid-kontroll-puudub.html", "Mis juhtub, kui dokumente pole", "Tagajärjed puuduvate dokumentide eest"),
    ],
    "ajakava.html": [
        ("artiklid/uus-ettevote-tootervishoid.html", "Uue ettevõtte kohustused", "Kohustused esimesest tööpäevast alates"),
        ("artiklid/tootervishoid-dokumentatsioon.html", "Nõutav dokumentatsioon", "Mida Tööinspektsioon kontrollimisel nõuab"),
        ("artiklid/riskianaluus-juhend.html", "Riskianalüüsi juhend", "Kuidas teha nõuetekohane riskianalüüs"),
        ("artiklid/vaikeettevote-kohustused.html", "Kohustused väikeettevõttele", "Mis kehtib 1-9 töötajaga ettevõttele"),
    ],
}

updated_tools = 0
for filename, links in TOOL_LINKS.items():
    filepath = os.path.join(BASE, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    links_html = "\n".join(make_tool_article_link(href, title, desc) for href, title, desc in links)

    if "Seotud artiklid" in content or "Kasulikud artiklid" in content:
        # Replace existing section with expanded one
        old_pattern = re.compile(
            r'<!-- (?:Related articles|Kasulikud artiklid|Seotud artiklid) -->\s*<section[^>]+>.*?</section>',
            re.DOTALL
        )
        new_section = make_tool_section(links_html, "Kasulikud artiklid")
        if old_pattern.search(content):
            content = old_pattern.sub(new_section.strip(), content)
            print(f"UPDATED existing section: {filename}")
        else:
            # The heading is inside main, try replacing the section containing it
            # Find from h2 Seotud artiklid back to its parent section
            old_pat2 = re.compile(
                r'<section[^>]*>\s*<h2[^>]*>Seotud artiklid</h2>.*?</section>',
                re.DOTALL
            )
            if old_pat2.search(content):
                content = old_pat2.sub(
                    '<section style="max-width:800px;margin:var(--space-8) auto;padding:0 var(--space-4);">\n'
                    '  <h2 style="font-size:var(--text-lg);margin-bottom:var(--space-3);">Kasulikud artiklid</h2>\n'
                    '  <div style="display:flex;flex-wrap:wrap;gap:var(--space-3);">\n'
                    + links_html + '\n'
                    '  </div>\n'
                    '</section>',
                    content
                )
                print(f"UPDATED section (pattern2): {filename}")
            else:
                print(f"WARNING: could not update existing section in {filename}")
                continue
    else:
        # Insert before </main>
        new_section = make_tool_section(links_html, "Kasulikud artiklid")
        if "</main>" in content:
            content = content.replace("</main>", new_section + "\n</main>", 1)
            print(f"ADDED section: {filename}")
        else:
            print(f"WARNING: no </main> in {filename}")
            continue

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    updated_tools += 1

print(f"\nDone. Updated {updated_articles} articles + {updated_tools} tool pages.")
