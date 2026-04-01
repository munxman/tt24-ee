#!/usr/bin/env python3
"""
Critic QA: Full diacritical + consistency audit for sector and city pages.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

SEKTORID = [
    'sektorid/avalik-haldus.html',
    'sektorid/ehitus.html',
    'sektorid/energeetika.html',
    'sektorid/finantsteenused.html',
    'sektorid/haridus.html',
    'sektorid/hotellindus.html',
    'sektorid/it.html',
    'sektorid/kaubandus.html',
    'sektorid/laondus.html',
    'sektorid/pollumajandus.html',
    'sektorid/puhastusteenused.html',
    'sektorid/tervishoid.html',
    'sektorid/toiduaineteostus.html',
    'sektorid/tootmine.html',
    'sektorid/transport.html',
]

LINNAD = [
    'linnad/johvi.html',
    'linnad/narva.html',
    'linnad/parnu.html',
    'linnad/tallinn.html',
    'linnad/tartu.html',
]

ALL_FILES = SEKTORID + LINNAD

# ---------------------------------------------------------------
# Ordered replacement pairs (longer/more specific FIRST)
# IMPORTANT: "tootmin" / "tootmis" (manufacturing) must NOT be changed
# ---------------------------------------------------------------
REPLACEMENTS = [
    # ---- ÖÖ/töö compound words ---------------------------------
    # Most specific compounds first
    ("tootervishoiduarsti",      "töötervishoiuarsti"),
    ("tootervishoiduarstlikul",  "töötervishoiuarstlikul"),
    ("tootervishoidukontrollil", "töötervishoiukontrollil"),
    ("tootervishoiduarst ",      "töötervishoiuarst "),
    ("tootervishoid arsti",      "töötervishoiuarsti"),
    ("tootervishoid arst",       "töötervishoiuarst"),
    ("tootervishoiu",            "töötervishoiu"),
    ("tooohutuse",               "tööohutuse"),
    ("tooohutus",                "tööohutus"),
    ("tooiseloom",               "töö iseloom"),
    ("tookeskkond",              "töökeskkond"),
    ("Tookeskkond",              "Töökeskkond"),
    ("tookohal",                 "töökohal"),
    ("tookoha",                  "töökoha"),
    ("tookoht",                  "töökoht"),
    ("tooasend",                 "tööasend"),
    ("Tooasend",                 "Tööasend"),
    ("tooruumi",                 "tööruumi"),
    ("tooruumid",                "tööruumid"),
    ("tooruumist",               "tööruumist"),
    ("toostressi",               "tööstressi"),
    ("toostress",                "tööstress"),
    ("tootingimist",             "töötingimist"),
    ("tootingimise",             "töötingimise"),
    ("tootingimiste",            "töötingimistes"),
    ("tootingimuses",            "töötingimuses"),
    ("tootingimused",            "töötingimused"),
    ("too vahendite",            "töövahendite"),
    ("too vahend",               "töövahend"),
    ("too algust",               "töö algust"),
    ("too puhul",                "töö puhul"),
    ("too ajal",                 "töö ajal"),
    ("toosusel",                 "töötamisel"),  # garbled "töösusel" → "töötamisel"
    # tootamine (working from töötama – NOT manufacturing)
    ("tootaole asumist",         "tööle asumist"),
    ("tootaole",                 "tööle"),
    ("tootamisel",               "töötamisel"),
    ("tootamist",                "töötamist"),
    ("tootamine",                "töötamine"),
    ("tootavad",                 "töötavad"),
    ("tootavatele",              "töötavatele"),
    ("tootavatel",               "töötavatel"),
    ("tootavatega",              "töötavatega"),
    # töötajad
    ("tootajatele",              "töötajatele"),
    ("tootajatel",               "töötajatel"),
    ("tootajate",                "töötajate"),
    ("tootajad",                 "töötajad"),
    ("tootajal",                 "töötajal"),
    ("tootajana",                "töötajana"),
    ("tootaja ",                 "töötaja "),
    ("tootaja,",                 "töötaja,"),
    ("tootaja.",                 "töötaja."),
    ("tootaja:",                 "töötaja:"),
    ("Tootajatele",              "Töötajatele"),
    ("Tootajatel",               "Töötajatel"),
    ("Tootajate",                "Töötajate"),
    ("Tootajad",                 "Töötajad"),
    ("Tootaja",                  "Töötaja"),
    # tööandja
    ("tooandjas",                "tööandjas"),
    ("tooandja ",                "tööandja "),
    ("tooandja,",                "tööandja,"),
    ("tooandja.",                "tööandja."),
    ("tooandja:",                "tööandja:"),
    ("tooandja",                 "tööandja"),
    ("Tooandja",                 "Tööandja"),
    # ööjoon: öötöö ja vaaksetöö
    ("Ootoo ja vaakestoo",       "Öötöö ja vaaksetöö"),
    ("ootoo ja vaakestoo",       "öötöö ja vaaksetöö"),
    ("Oo- ja vaakestoo",         "Öötöö ja vaaksetöö"),
    ("oo- ja vaakestoo",         "öötöö ja vaaksetöö"),
    ("Ootoo",                    "Öötöö"),
    ("ootoo",                    "öötöö"),
    ("vaakestoo",                "vaaksetöö"),
    ("Vaakestoo",                "Vaaksetöö"),
    # kõrgustöö
    ("Korgustool ja masinajuhtimisel", "Kõrgustöö puhul ja masinajuhtimisel"),
    ("Korgustool",               "Kõrgustöö"),
    ("korgustool",               "kõrgustöö"),
    ("Korgustoo",                "Kõrgustöö"),
    ("korgustoo",                "kõrgustöö"),
    # tööstusvigastus (industrial injury)
    ("tooostusvigastusteks",     "tööstusvigastusteks"),
    ("tooostusvigastuse",        "tööstusvigastuse"),
    ("tooostus",                 "tööstus"),
    # tööõnnetus
    ("toooiguseid",              "tööõnnetusi"),

    # ---- Põ (po→põ, poh→põhj) ---------------------------------
    ("pohjustajaks",             "põhjustajaks"),
    ("pohjustajana",             "põhjustajana"),
    ("pohjustaja",               "põhjustaja"),
    ("pohjustavad",              "põhjustavad"),
    ("pohjustada",               "põhjustada"),
    ("pohjustatud",              "põhjustatud"),
    ("pohjustama",               "põhjustama"),
    ("pohjustab",                "põhjustab"),
    ("pohjuseid",                "põhjuseid"),
    ("pohjustel",                "põhjustel"),
    ("pohjused",                 "põhjused"),
    ("pohjust",                  "põhjust"),
    ("pohjus",                   "põhjus"),
    ("pohustuvad",               "põhjustavad"),
    ("pohustab",                 "põhjustab"),
    ("pohised",                  "põhised"),

    # ---- Süsteem -----------------------------------------------
    ("vereringesusteemi",        "vereringesüsteemi"),
    ("vereringesusteem",         "vereringesüsteem"),
    ("lihas-skeleti susteemi",   "lihas-skeleti süsteemi"),
    ("nearalast susteemi",       "närvialast süsteemi"),
    ("nearalane susteem",        "närvialane süsteem"),
    ("susteemi",                 "süsteemi"),
    ("susteem",                  "süsteem"),

    # ---- Psühhosotsiaalne --------------------------------------
    ("Psuhhosotsiaalsed",        "Psühhosotsiaalsed"),
    ("Psuhhosotsiaalne",         "Psühhosotsiaalne"),
    ("psuhhosotsiaalsed",        "psühhosotsiaalsed"),
    ("psuhhosotsiaalne",         "psühhosotsiaalne"),
    ("psuhhosotsiaalse",         "psühhosotsiaalse"),
    ("psuhhosotsiaal",           "psühhosotsiaal"),
    ("Psuhholise",               "Psühholise"),
    ("psuhholise",               "psühholise"),
    ("Korge psuhholise koormusega toetajatele",
     "Kõrge psühholise koormusega töötajatele"),

    # ---- Läbipõlemine ------------------------------------------
    ("labipolemise",             "läbipõlemise"),
    ("labipolemist",             "läbipõlemist"),
    ("labipolemine",             "läbipõlemine"),
    ("labipolemist",             "läbipõlemist"),
    ("labiima",                  "läbima"),
    ("labimist",                 "läbimist"),

    # ---- Üle- (overload, above) --------------------------------
    ("ulekoormuse",              "ülekoormuse"),
    ("ulekoormus",               "ülekoormus"),
    ("ylekoige",                 "üle"),   # "(ylekoige 85 dB)" → "(üle 85 dB)"
    ("ulekoige",                 "üle"),   # same
    ("ulevaesimist",             "üleväsimist"),
    ("ulevaesimine",             "üleväsimine"),

    # ---- Ülakeha -----------------------------------------------
    ("uelakeha",                 "ülakeha"),
    ("Uelakeha",                 "Ülakeha"),

    # ---- Üldine ------------------------------------------------
    ("Uldine",                   "Üldine"),
    ("uldine",                   "üldine"),

    # ---- Müra --------------------------------------------------
    # Compound words first
    ("murakokkupuutega",         "mürakokkupuutega"),
    ("Murakokkupuutega",         "Mürakokkupuutega"),
    ("muraekspositsioonil",      "müraekspositsioonil"),
    ("muraekspositsiooniga",     "müraekspositsiooniga"),
    ("murataset",                "mürataset"),
    ("muratase",                 "müratase"),
    ("kuulmist kahjustavat mura",  "kuulmist kahjustavat müra"),
    ("piirnorme ületavat mura",    "piirnorme ületavat müra"),
    ("<strong>Mura</strong>",      "<strong>Müra</strong>"),

    # ---- Järelt ------------------------------------------------
    ("aasta jarelt",             "aasta järelt"),
    ("aastate jarelt",           "aastate järelt"),
    ("kahe aasta jarelt",        "kahe aasta järelt"),
    ("kolme aasta jarelt",       "kolme aasta järelt"),
    ("jarelt",                   "järelt"),

    # ---- Nägemine ----------------------------------------------
    ("nagelamishaireid",         "nägemishäireid"),
    ("nagelamis",                "nägemis"),
    ("nagemustersavust",         "nägemisteravust"),
    ("nagemistersavus",          "nägemisteravust"),
    ("Nagemise kontroll",        "Nägemise kontroll"),
    ("nagemise kontroll",        "nägemise kontroll"),
    ("varvinagemist",            "värvinägemist"),
    ("nagevalja",                "nägemisvälja"),

    # ---- Häired ------------------------------------------------
    ("unehaireid",               "unehäireid"),
    ("vereringehaireid",         "vereringehäireid"),
    ("ainevahetushaireid",       "ainevahetushäireid"),
    ("nahahaireid",              "nahahäireid"),
    ("haireid",                  "häireid"),
    ("hairete",                  "häirete"),

    # ---- Südame ------------------------------------------------
    ("sydame-veresoonkonna",     "südame-veresoonkonna"),
    ("Sydame-veresoonkonna",     "Südame-veresoonkonna"),
    ("sydamele",                 "südamele"),
    ("sydame",                   "südame"),
    ("Sydame",                   "Südame"),

    # ---- Käsi/käe ----------------------------------------------
    ("kasivibratsioon-sndroomi", "käsivibratsioon-sündroomi"),
    ("kasivibratsioon",          "käsivibratsioon"),
    ("kaevibratsioon",           "käevibratsioon"),
    ("kasitlemisel",             "käsitlemisel"),
    ("kasitlemine",              "käsitlemine"),
    ("kasitlusega",              "käsitlusega"),
    ("kasitlevate",              "käsitlevate"),
    ("kasitleb",                 "käsitleb"),
    ("kasitleda",                "käsitleda"),
    ("kasitlev",                 "käsitlev"),
    ("randme- ja kaevalu",       "randme- ja käevalu"),
    ("kaela-, ola-",             "kaela-, õla-"),

    # ---- Sündroom ----------------------------------------------
    ("n-o tunnelsindroon",       "nn. tunnelsündroom"),
    ("karpaalkanali sndroomi",   "karpaalkanali sündroomi"),
    ("tunnelsindroon",           "tunnelsündroom"),
    ("sndroomi",                 "sündroomi"),

    # ---- Pöördumatu --------------------------------------------
    ("pordmatut",                "pöördumatut"),
    ("pordmatu",                 "pöördumatu"),

    # ---- Kuulmiskahjustus --------------------------------------
    ("kuulmikahjustust",         "kuulmiskahjustust"),
    ("kuulmikahjustuse",         "kuulmiskahjustuse"),

    # ---- Luu-lihaskond -----------------------------------------
    ("luulihaskonna",            "luu-lihaskonna"),

    # ---- Füüsiline ---------------------------------------------
    ("fuusikaliste",             "füüsikaliste"),
    ("fuusikaline",              "füüsikaline"),
    ("fuuskalise",               "füüsilise"),
    ("fuuskalised",              "füüsilised"),

    # ---- Päikesekiirgus ----------------------------------------
    ("paikesekiirguse",          "päikesekiirguse"),

    # ---- Silmakahjustus ----------------------------------------
    ("silmakahustuse",           "silmakahjustuse"),
    ("naha- ja silmakahustuse",  "naha- ja silmakahjustuse"),

    # ---- Närvialane --------------------------------------------
    ("nearalast",                "närvialast"),
    ("nearalane",                "närvialane"),

    # ---- Kõrgendatud -------------------------------------------
    ("korgendatud",              "kõrgendatud"),
    ("Korgendatud",              "Kõrgendatud"),
    ("korgenenud",               "kõrgenenud"),
    ("korgete",                  "kõrgete"),
    ("Korgete",                  "Kõrgete"),
    ("korgel ",                  "kõrgel "),

    # ---- Kõige, kõigile ----------------------------------------
    ("koigile",                  "kõigile"),
    ("koige ohtlikumaid",        "kõige ohtlikumaid"),
    ("koige",                    "kõige"),

    # ---- Värvid ------------------------------------------------
    ("varvid",                   "värvid"),
    ("Varvid",                   "Värvid"),
    ("varvide",                  "värvide"),

    # ---- Välitingimused ----------------------------------------
    ("valitingimuste",           "välitingimuste"),
    ("valitingimuses",           "välitingimuses"),

    # ---- Koolipäev ---------------------------------------------
    ("koolipaevist",             "koolipäevist"),
    ("iga paev",                 "iga päev"),

    # ---- opiabiga (õpiabiga) -----------------------------------
    ("opiabiga tootavatele tervishoiutootajatele",
     "õpiabiga töötavatele tervishoiutöötajatele"),
    ("opiabiga",                 "õpiabiga"),

    # ---- Various specific phrases ------------------------------
    ("Allikas: TTOS (tootervishoiu ja tooohutuse seadus)",
     "Allikas: TTOS (töötervishoiu ja tööohutuse seadus)"),
    # Note: tooelu.ee is correct (ASCII domain name - no change needed)

    # ---- Typographic cleanup -----------------------------------
    ("kuvariprill id",           "kuvariprilid"),   # fix space in compound
    ("desinf eksioonivahendid",  "desinfektsioonivahendid"),  # fix space
    ("vaktsina tsioon",          "vaktsineerimine"),  # fix space
    ("keemiakokkkupuutega",      "keemiakokkupuutega"),  # triple k
    ("tolmu- ja keemiakokkkupuutega", "tolmu- ja keemiakokkupuutega"),
]


def fix_font_sizes(content):
    """Remove font-size:0.85rem, font-size:0.78rem, font-size:0.9rem from inline styles."""
    # Handle ; font-size:Xrem; (mid or end of style string)
    for size in ['0\\.85rem', '0\\.78rem', '0\\.9rem']:
        # At end: ;[space]font-size:Xrem;  or  ;[space]font-size:Xrem at attr end
        content = re.sub(r';\s*font-size:\s*' + size + r'\s*(?=;|")', '', content)
        # At start: font-size:Xrem;[space]
        content = re.sub(r'font-size:\s*' + size + r'\s*;\s*', '', content)
        # Lone (only property): font-size:Xrem
        content = re.sub(r'font-size:\s*' + size, '', content)
    return content


def remove_oluline_label(content):
    """Remove '<strong>Oluline meelde jätta:</strong> ' label."""
    content = content.replace('<strong>Oluline meelde jätta:</strong> ', '')
    content = content.replace('<strong>Oluline meelde jätta:</strong>', '')
    return content


def remove_h2_emojis(content):
    """Remove emoji characters from h2 and h3 headings."""
    # Match h2 or h3 tags with emoji – remove emoji + trailing space
    def strip_emoji(m):
        tag_open = m.group(1)
        inner = m.group(2)
        tag_close = m.group(3)
        # Remove common emoji chars and trailing space
        inner = re.sub(
            r'[\U0001F300-\U0001FFFF\U00002600-\U000027FF\U0000FE00-\U0000FEFF'
            r'\u200d\ufe0f\u20e3]+ ?',
            '', inner
        )
        inner = inner.strip()
        return tag_open + inner + tag_close
    content = re.sub(
        r'(<h[23][^>]*>)(.*?)(</h[23]>)',
        strip_emoji,
        content,
        flags=re.DOTALL
    )
    return content


def apply_replacements(content):
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)
    return content


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original

    # 1. Remove emoji from h2/h3 headings
    content = remove_h2_emojis(content)

    # 2. Remove "Oluline meelde jätta:" patronizing label
    content = remove_oluline_label(content)

    # 3. Apply diacritical + consistency replacements
    content = apply_replacements(content)

    # 4. Remove font-size overrides on body text
    content = fix_font_sizes(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    changed = []
    unchanged = []
    for rel_path in ALL_FILES:
        filepath = os.path.join(BASE, rel_path)
        if not os.path.exists(filepath):
            print(f"  MISSING: {rel_path}")
            continue
        was_changed = process_file(filepath)
        if was_changed:
            changed.append(rel_path)
            print(f"  FIXED:  {rel_path}")
        else:
            unchanged.append(rel_path)
            print(f"  CLEAN:  {rel_path}")

    print(f"\nSummary: {len(changed)} files fixed, {len(unchanged)} already clean.")
    return changed, unchanged


if __name__ == '__main__':
    main()
