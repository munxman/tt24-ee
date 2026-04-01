#!/usr/bin/env python3
"""
SEO/GEO/AEO injection script for tt24.ee
Adds: BreadcrumbList, sr-only blocks, Seotud teemad sections
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

SECTOR_META = {
    "avalik-haldus": {
        "name": "Avalik haldus",
        "keywords": "avaliku sektori toetervishoid tootervishoid avalikus teenistuses ametnikud omavalitsus riigiasutused tooohutus tootervishoiu leping avaliku halduse sektor tervisekontroll ametnikule tootervishoiu teenuse osutaja avalikus sektoris tooohutuse seadus TTOS riigiteenistus kohaliku omavalitsuse tootervishoiu kohustused"
    },
    "ehitus": {
        "name": "Ehitus",
        "keywords": "ehitusettevotte tootervishoid ehitustoo tervishoid ehitustoolised tervisekontroll ehituses tooohutus ehitusplatsil korgustooo muratase vibratsioon asbest tolm ehitussektor tootervishoiu leping ehitusettevottele tootervishoiu teenuse osutaja ehitussektoris riskianaluus ehituses TTOS ehitustoode ohutegurid ehitaja tervisekontroll"
    },
    "energeetika": {
        "name": "Energeetika",
        "keywords": "energeetikasektori tootervishoid energia tootmine tootervishoid elektritoo ohutus tuumaenergia tootervishoid taastuvenergeetika tootervishoid elektrik tervisekontroll termoelektrijaam ohtlikud toookeskond energeetika tootervishoiu leping tootervishoiu teenuse osutaja energeetikasektoris tooohutuse nouded energeetikas"
    },
    "finantsteenused": {
        "name": "Finantsteenused",
        "keywords": "finantssektori tootervishoid pank kindlustus tootervishoid kontorotoo ergonoomika kuvaritoo tervisekontroll vaimne tervis finantssektoris stressijuhtimine toookeskond kontoris finantsteenused tootervishoiu leping tootervishoiu teenuse osutaja finantssektoris tootervishoiu kohustused kontoripersonalile"
    },
    "haridus": {
        "name": "Haridus",
        "keywords": "haridussektori tootervishoid opetaja tootervishoid koolipersoali tervisekontroll haaletoo haigused lasteaiatootajad tervisekontroll opetajate professionaalsed haigused haridusasutuste tootervishoiu leping tootervishoiu teenuse osutaja haridussektoris kool lasteaed noortekeskus tooohutuse nouded hariduses"
    },
    "hotellindus": {
        "name": "Hotellindus ja turism",
        "keywords": "hotellinduse tootervishoid turismisektori tootervishoid majutusteenuste tootervishoid hotellitoolised tervisekontroll vastuvotutooliste ergonoomika hotellipersonali tootervishoiu leping tootervishoiu teenuse osutaja hotellinduses kodumajandustoolise tervisekontroll toiduohutus toitekäitlejatele"
    },
    "it": {
        "name": "IT sektor",
        "keywords": "IT sektori tootervishoid infotehnoloogia tootervishoid arendaja tervisekontroll kuvaritoo terviseriski IT-firma tootervishoiu leping ergonoomika programmeerijale tooohutus IT-ettevottele tootervishoiu teenuse osutaja IT-sektoris vaimne tervis programmeerija istumisest tekkivad kahjustused kuvari kasutamine tootervishoid"
    },
    "kaubandus": {
        "name": "Kaubandus",
        "keywords": "kaubandussektori tootervishoid jaekaubandus tootervishoid kauplus tervisekontroll kassaatorile kaubamajatooline tootervishoiu leping kaubandusettevotte tootervishoiu kohustused tootervishoiu teenuse osutaja kaubandusvaldkonnas raskuste toostmine kaubanduses seisev too kauplusepersonali tervisekontroll"
    },
    "laondus": {
        "name": "Laondus ja logistika",
        "keywords": "laonduse tootervishoid logistika tootervishoid laotooline tervisekontroll tootekoja tootervishoiu leping tootervishoiu teenuse osutaja laonduses raskuste kandmine kahveltootaja tervisekontroll ladu tooohutus logistikafirma tootervishoiu kohustused raskuste toostmine laos luu-lihaskonna uuringud"
    },
    "pollumajandus": {
        "name": "Pohllumajandus",
        "keywords": "pollumajandussektori tootervishoid talutooline tervisekontroll kemikaalidega kokkupuude pollumajanduses vibratsioonikahjustused traktori juht tootervishoiu leping pollumajandusettevottele tootervishoiu teenuse osutaja pollumajandussektoris kooriained pestiidid herbitsiidid tolm loomakasvatus tooline tervisekontroll"
    },
    "puhastusteenused": {
        "name": "Puhastusteenused",
        "keywords": "puhastusteenuse tootervishoid koristustooline tervisekontroll kemikaalidega kokkupuude koristuses naha haigused puhastusteenuste tootervishoid tootervishoiu leping puhastusteenuse ettevottele tootervishoiu teenuse osutaja puhastusteenustes ergonoomika koristuses raskuste kandmine koristuses"
    },
    "tervishoid": {
        "name": "Tervishoid",
        "keywords": "tervishoiutootaja tootervishoid meditsiinitoolise tervisekontroll haigla tootervishoiu leping tootervishoiu teenuse osutaja tervishoiusektoris bioloogiline ohutegur meditsiinis kemikaalidega kokkupuude laboris kiirguskaitse toologie vaimne tervis meditsiin emotsionaalne koormus oomistamine tervishoid"
    },
    "toiduaineteostus": {
        "name": "Toiduaineteostus",
        "keywords": "toiduaineteostuse tootervishoid toitlustus tootervishoid toidukaitlejate tervisekontroll toiduaineteostuse tootervishoiu leping tootervishoiu teenuse osutaja toiduaineteostuses toitlustustoolised tervisekontroll kohustuslik toidukajanduse tooohutus kemikaalid toidutootmises bioloogiline ohutegur toitlustuses"
    },
    "tootmine": {
        "name": "Tootmine",
        "keywords": "tootmisettevotte tootervishoid tootmistoolise tervisekontroll tootmissektor tooohutus raskuste kandmine tootmises muratase tootmisettevottele tootervishoiu leping tootervishoiu teenuse osutaja tootmissektoris kemikaalid tootmises vibratsioon tootmises tootmistehas tootervishoiu kohustused"
    },
    "transport": {
        "name": "Transport",
        "keywords": "transpordi tootervishoid autojuhi tervisekontroll bussijuhi tervisekontroll veoautojuht tootervishoid transpordisektori tootervishoiu leping tootervishoiu teenuse osutaja transpordisektoris istuv too juhi tervisekontroll vibratsioon transpordis nagemisteravus juhtimiseks kutse-eeldused tervisele"
    },
}

SECTOR_LINKS = [
    ("ehitus", "Ehitus"),
    ("it", "IT sektor"),
    ("transport", "Transport"),
    ("tervishoid", "Tervishoid"),
    ("tootmine", "Tootmine"),
    ("kaubandus", "Kaubandus"),
    ("haridus", "Haridus"),
    ("laondus", "Laondus"),
    ("pollumajandus", "Pohllumajandus"),
]

TOOL_LINKS = [
    ("../kontrollnimekiri.html", "Tootervishoiu kontrollnimekiri"),
    ("../kalkulaator.html", "Kulukalkulaator"),
    ("../enesekontroll.html", "Enesekontroll"),
    ("../korduma.html", "KKK"),
]

def make_breadcrumb(sector_key, sector_name):
    return f'''  <!-- Schema: BreadcrumbList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Avaleht", "item": "https://tt24.ee/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Sektorid", "item": "https://tt24.ee/" }},
      {{ "@type": "ListItem", "position": 3, "name": "{sector_name}", "item": "https://tt24.ee/sektorid/{sector_key}.html" }}
    ]
  }}
  </script>'''

def make_sr_only_block(sector_key, keywords):
    return f'''
  <!-- Machine-readable keywords: invisible to humans, indexed by search engines and AI crawlers -->
  <div class="sr-only" aria-hidden="true">
    Tootervishoiu kohustused {SECTOR_META[sector_key]["name"].lower()} sektoris.
    {keywords}
    tootervishoiu teenuse osutaja tootervishoiu leping tervisekontroll tool tooohutuse seadus TTOS riskianaluus kohustuslik tooandja kohustused tootervishoiu seadus Eesti tootervishoiu normid Tooinspektor tooohutus tootooline seire.
  </div>'''

def make_seotud_teemad(sector_key):
    # Pick other sectors (not this one)
    other_sectors = [(k, v["name"]) for k, v in SECTOR_META.items() if k != sector_key][:6]
    links_html = "\n".join([
        f'          <a href="{k}.html" class="seotud-link">{v}</a>'
        for k, v in other_sectors
    ])
    tool_links_html = "\n".join([
        f'          <a href="{url}" class="seotud-link">{label}</a>'
        for url, label in TOOL_LINKS
    ])
    return f'''
  <!-- Seotud teemad -->
  <section class="section" style="background:var(--color-primary-light, #E0F2FE); padding: 2rem 0;">
    <div class="container">
      <h2 class="section-title" style="font-size:1.2rem;">Seotud teemad</h2>
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-bottom:1.5rem;">
{links_html}
      </div>
      <h3 style="font-size:1rem; margin-bottom:0.75rem;">Praktilised tooriistad</h3>
      <div style="display:flex; flex-wrap:wrap; gap:0.5rem;">
{tool_links_html}
      </div>
    </div>
  </section>'''

def process_sector_page(sector_key):
    filepath = os.path.join(BASE, "sektorid", f"{sector_key}.html")
    if not os.path.exists(filepath):
        print(f"  SKIP (not found): {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already processed
    if "BreadcrumbList" in content:
        print(f"  SKIP (BreadcrumbList already present): {sector_key}")
        # Still add sr-only and seotud teemad if missing
    
    sector_name = SECTOR_META[sector_key]["name"]
    keywords = SECTOR_META[sector_key]["keywords"]

    # 1. Add BreadcrumbList before GTM script in head (if not present)
    if "BreadcrumbList" not in content:
        breadcrumb = make_breadcrumb(sector_key, sector_name)
        # Insert before GTM script
        gtm_marker = "  <!-- Google Tag Manager (consent-gated) -->"
        if gtm_marker in content:
            content = content.replace(gtm_marker, breadcrumb + "\n\n" + gtm_marker, 1)
            print(f"  + BreadcrumbList added: {sector_key}")
        else:
            # Insert before </head>
            content = content.replace("</head>", breadcrumb + "\n</head>", 1)
            print(f"  + BreadcrumbList added (before </head>): {sector_key}")

    # 2. Add sr-only block before </main> if not present
    if "sr-only" not in content:
        sr_block = make_sr_only_block(sector_key, keywords)
        content = content.replace("</main>", sr_block + "\n</main>", 1)
        print(f"  + sr-only block added: {sector_key}")

    # 3. Add Seotud teemad before </main> if not present
    if "Seotud teemad" not in content:
        seotud = make_seotud_teemad(sector_key)
        content = content.replace("</main>", seotud + "\n</main>", 1)
        print(f"  + Seotud teemad added: {sector_key}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  DONE: {sector_key}.html")


# --- MAIN ---
print("=== Processing sector pages ===")
for key in SECTOR_META.keys():
    print(f"\nProcessing: {key}")
    process_sector_page(key)

print("\n=== All done ===")
