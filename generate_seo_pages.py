#!/usr/bin/env python3
"""
Programmatic SEO page generator for TTH Employer Compliance Portal.
Generates 15 sector pages + 5 city pages in Estonian.
"""

import os
import json

BASE_URL = "https://tootervishoiu.valvekliinik.ee"
PORTAL_ROOT = "../index.html"

# ─── SECTOR DATA ─────────────────────────────────────────────────────────────

SECTORS = {
    "ehitus": {
        "title": "Ehitus",
        "slug": "ehitus",
        "icon": "🏗️",
        "seo_title": "Töötervishoiu nõuded ehituses — tööandja kohustused 2026",
        "seo_desc": "Ehitusettevõtte töötervishoiu nõuded selgelt: kohustuslikud tervisekontrollid, riskianalüüs, Tööinspektsiooni nõuded ja praktilised nõuanded.",
        "og_title": "Töötervishoiu nõuded ehituses | Tööandja juhend 2026",
        "risks": [
            "Kukkumine kõrgusest — turvavöö ja kaitsevahendite puudumine",
            "Kokkupuude müra, vibratsiooni ja tolmuga (sh asbest, kvartsitolm)",
            "Raskuste tõstmine ja lihaskonna ülekoormus",
            "Ohtlike kemikaalidega kokkupuude (lahustid, värvid, bitumen)",
            "Elektriohud ja ümbritsevate liinidega kokkupuude",
            "Heitgaasid ja halva ventilatsiooniga tööruum",
            "Pikaajaline viibimine äärmuslikes temperatuuritingimustes",
        ],
        "health_checks": [
            ("Kohustuslik iga 3 aasta järel", "Kõik ehitustöötajad — sh kuulmis- ja nägemistest, kopsude uuring tolmutöö puhul"),
            ("Enne tööle asumist", "Esmane tervisekontroll kõigile töötajatele riskiametis"),
            ("Kõrgustes töötajatel iga 2 aasta järel", "Kardiograafia, neuroloogiline hindamine, tasakaalutest"),
            ("Müratöötajatel iga 2 aasta järel", "Audiomeetria (kuulmistest)"),
            ("Vibratsioonitöötajatel iga 2 aasta järel", "Liigeste, käte ja selgroo uuring"),
            ("Noored töötajad (15–18 a)", "Iga-aastane tervisekontroll"),
        ],
        "findings": [
            "Riskianalüüs on tegemata või aegunud (üle 3 aasta vana)",
            "Töötajate tervisekontrollid on hilinenud või puuduvad",
            "Isikukaitsevahendite kasutamine ei ole dokumenteeritud",
            "Ohtlike ainete register puudub või on mittetäielik",
            "Tööõnnetustest ei ole teavitatud Tööinspektsiooni",
            "Töötajaid ei ole terviseriskidest kirjalikult teavitatud",
        ],
        "checklist": [
            "Riskianalüüs on koostatud ja alla 3 aasta vana",
            "Kõigil töötajatel on kehtiv tervisekontrolli tõend",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Ohtlike ainete register on olemas ja uuendatud",
            "Isikukaitsevahendid on väljastatud ja kasutamine dokumenteeritud",
            "Töötajad on teavitatud terviseriskidest (allkirjad olemas)",
            "Töökeskkonna mõõtmised (müra, tolm, vibratsioon) on tehtud",
            "Esmaabivahendid on olemas ja korras",
            "Tööõnnetuste register on peetud",
            "Alaealiste töötamise eritingimused on täidetud",
        ],
        "faqs": [
            ("Kas ajutistele töötajatele on tervisekontroll kohustuslik?",
             "Jah. Tervisekontroll on kohustuslik kõigile töötajatele, kes töötavad ohtlikus töökeskkonnas — olenemata lepingu kestusest. Hooajatöötajale enne tööle asumist."),
            ("Mitu korda aastas peab ehitustöötaja tervisekontrollis käima?",
             "Tavaliselt iga 2–3 aasta järel, olenevalt riskitasemest. Kõrgustes töötajad ja müratöötajad käivad iga 2 aasta järel."),
            ("Kes maksab tervisekontrolli eest?",
             "Tööandja maksab. Töötajalt ei tohi tervisekontrolli kulusid kinni pidada."),
            ("Mis on riskianalüüs ja kas see on ehituses kohustuslik?",
             "Riskianalüüs on kirjalik dokument, kus hindatakse kõiki töökohal esinevaid ohte. Ehituses on see kohustuslik kõigile tööandjatele, kellel on vähemalt üks töötaja."),
            ("Kas alltöövõtja töötajad kuuluvad minu töötervishoiu kohustuste alla?",
             "Tööandja kohustused laienevad tema enda töötajatele. Alltöövõtja tööandja peab ise tagama oma töötajate ohutuse. Küll aga vastutate teie ehitusplatsil tekkivate riskide eest koordineerimise osas."),
            ("Mida teha tööõnnetuse korral ehitusplatsil?",
             "Raskest tööõnnetusest tuleb Tööinspektsiooni teavitada esimesel võimalusel, kuid hiljemalt 24 tunni jooksul. Kõik tööõnnetused tuleb kanda tööõnnetuste registrisse."),
        ],
    },
    "it": {
        "title": "IT ja telekommunikatsioon",
        "slug": "it",
        "icon": "💻",
        "seo_title": "Töötervishoiu nõuded IT-sektoris — tööandja kohustused 2026",
        "seo_desc": "IT- ja telekommunikatsiooniettevõtte töötervishoiu nõuded: kuvariga töö eeskirjad, ergonoomika, vaimne tervis ja kohustuslikud tervisekontrollid.",
        "og_title": "Töötervishoiu nõuded IT-sektoris | Tööandja juhend 2026",
        "risks": [
            "Kuvariga töö (silmade üleväsimine, kuvarhaigused)",
            "Halb ergonoomika — vale kehahoiak, seljavalud",
            "Vaimne koormus, läbipõlemine, krooniline stress",
            "Pikaajaline istuv töö, liikumisvaegus",
            "Halvast ventilatsioonist tulenev peavalu ja väsimus",
            "Vähene loomulik valgus avatud kontorites",
            "Korduvate liigutustega käte- ja randmevalud (carpal tunnel)",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Kuvaritöötajad — silmauuring (visomeetria), lihas-skeleti hindamine"),
            ("Enne kuvaritöö algust", "Esmane silmauuring, riskiküsimustik"),
            ("Kõrge psüühilise koormusega töötajad", "Vaimse tervise hindamine töötervishoiuarsti juures"),
            ("Noored töötajad (15–18 a)", "Iga-aastane tervisekontroll"),
        ],
        "findings": [
            "Kuvaritöötajatele ei ole korraldatud nõuetekohast silmauuringut",
            "Töökoha ergonoomika hindamine on tegemata",
            "Psühhosotsiaalset riskianalüüsi (stressi, läbipõlemise risk) ei ole tehtud",
            "Töötajaid ei ole teavitatud kuvaritöö tervisemõjudest",
            "Töökohale ei ole tagatud nõuetekohane valgustus",
        ],
        "checklist": [
            "Kõigil kuvaritöötajatel on silmauuring tehtud (enne tööle asumist ja iga 3 a järel)",
            "Töökohtade ergonoomika on hinnatud ja dokumenteeritud",
            "Riskianalüüs sisaldab psühhosotsiaalset riskide hinnangut",
            "Töötajatele on tagatud regulaarsed pausid kuvaritöö katkestamiseks",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Valgustuse mõõtmised on tehtud (min 500 lux kuvaritöö ruumides)",
            "Töötajad on teavitatud õigest töökohakorraldusest",
            "Kaugtöötajate ergonoomika on käsitletud",
        ],
        "faqs": [
            ("Kas kaugtöötajale on ka tervisekontroll kohustuslik?",
             "Jah. Kaugtöötaja on endiselt teie töötaja ja kuvaritöö nõuded kehtivad ka kodus. Peate tagama ergonoomika hindamise ja silmauuringud."),
            ("Mitu tundi päevas võib kuvariga töötada ilma kohustusliku pausita?",
             "Seadus ei sea konkreetset tunnipiiri, kuid soovitab regulaarseid pause. Hea tava on 5–10 minutit pausi iga 50–60 minuti järel."),
            ("Kas prillid tööks on tööandja kohustus?",
             "Kui silmauuring näitab, et töötaja vajab kuvaritöö jaoks eraldi prille ja tema olmeprillidest ei piisa, peab tööandja need hüvitama."),
            ("Mida tähendab psühhosotsiaalne riskianalüüs?",
             "See on riskianalüüsi osa, kus hinnatakse tööstressi, läbipõlemise ja psüühilise ülekoormuse riske. IT-sektoris eriti oluline."),
            ("Kui sageli peab riskianalüüsi uuendama?",
             "Vähemalt iga 3 aasta järel või oluliste muutuste korral töökeskkonnas (uus kontor, kaugtöö kehtestamine, suur meeskonna kasv)."),
        ],
    },
    "toiduaineteostus": {
        "title": "Toiduainetööstus",
        "slug": "toiduaineteostus",
        "icon": "🍽️",
        "seo_title": "Töötervishoiu nõuded toiduainetööstuses — tööandja kohustused 2026",
        "seo_desc": "Toiduainetööstuse töötervishoiu nõuded: kohustuslikud tervisekontrollid, hügieenipassid, keemiline ja bioloogiline ohutus toiduainetootmises.",
        "og_title": "Töötervishoiu nõuded toiduainetööstuses | Tööandja juhend 2026",
        "risks": [
            "Bioloogilised ohud (bakterid, hallitusseened, patogeenid toidus)",
            "Külmas või kuumas töötamine (külmlaod, ahjud)",
            "Lõikavate ja teravate tööriistadega seotud vigastusrisk",
            "Kokkupuude puhastus- ja desinfitseerimisvahendite kemikaalidega",
            "Korduv ühekülgne füüsiline töö (konveieriliin, pakkimine)",
            "Müra töötlevas tööstuses",
            "Libedal põrandal kukkumise oht",
        ],
        "health_checks": [
            ("Iga 2–3 aasta järel", "Kõik töötajad — üldine tervisekontroll, sealhulgas nakkushaiguste kontroll"),
            ("Enne tööle asumist", "Köha-, soole- ja muude nakkushaiguste välistamine (toidukäitlejatele kohustuslik)"),
            ("Külmas töötavad töötajad", "Kardiovaskulaarne hindamine iga 2 aasta järel"),
            ("Mürakokkupuutega töötajad", "Audiomeetria iga 2 aasta järel"),
        ],
        "findings": [
            "Toidukäitlejatel puudub nõuetekohane tervistõend",
            "Hügieenikoolitus ei ole dokumenteeritud",
            "Kemikaalide ohutuskaardid pole kättesaadavad töötajatele",
            "Külmalaos töötajate tervisekontroll on tegemata",
            "Riskianalüüs ei kata bioloogilisi riske",
        ],
        "checklist": [
            "Kõigil toidukäitlejatel on kehtiv tervistõend",
            "Hügieenikoolitus on läbitud ja dokumenteeritud",
            "Riskianalüüs katab bioloogilised, keemilised ja füüsikalised ohud",
            "Kemikaalide ohutuskaardid on töötajatele kättesaadavad",
            "Töötajad on varustatud nõuetekohaste kaitseriietuse ja -vahenditega",
            "Külmalaos ja kuumas töötavate töötajate erisused on riskianalüüsis",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Tööõnnetuste register on peetud",
        ],
        "faqs": [
            ("Kas toidukäitleja peab tervisekontrollis käima?",
             "Jah, see on kohustuslik. Toidukäitleja tervistõend peab olema kehtiv ja tõendama, et töötajal ei ole toiduga levivaid nakkushaigusi."),
            ("Mis on hügieenikoolitus ja kes peab selle läbima?",
             "Hügieenikoolitus on koolitus toiduohutuse põhimõtete kohta. Kõik toidukäitlejad peavad selle läbima enne töö alustamist ja korraliste intervallide järel."),
            ("Kas hooajatöötajale on samad nõuded?",
             "Jah, hooajatöötajale kehtivad samad tervisekontrolli nõuded. Ka lühiajalise lepinguga töötaja peab käima tervisekontrollis enne toidukäitlemise alustamist."),
            ("Kes tasub tervisekontrolli eest?",
             "Tööandja. Töötajalt kulusid kinni pidada ei tohi."),
            ("Kas toiduainetööstuses on erikaitsevahendid kohustuslikud?",
             "Jah. Sõltuvalt tööst — kindad, põll, kiiver (teatud masinate juures), kuulmikaitsed (mürarikastes tingimustes), libisemiskindlad jalanõud."),
        ],
    },
    "kaubandus": {
        "title": "Kaubandus",
        "slug": "kaubandus",
        "icon": "🛒",
        "seo_title": "Töötervishoiu nõuded kaubanduses — tööandja kohustused 2026",
        "seo_desc": "Kaupluste ja kaubandusettevõtete töötervishoiu nõuded: kassapidajate tervisekontroll, raskuste tõstmine, tööaeg ja kohustuslikud dokumendid.",
        "og_title": "Töötervishoiu nõuded kaubanduses | Tööandja juhend 2026",
        "risks": [
            "Pikaajaline seismine (kassapidajad, müügiassistendid)",
            "Raskuste tõstmine — kauba ladumine ja mahalaadimine",
            "Korduvad liigutused (kassalint, skannimine)",
            "Vaimne koormus — klientide teenindamine, konfliktid",
            "Külmkambrites töötamine (toidukaubandus)",
            "Halb valgustus või ebamugav mikrokliima",
            "Kukkumisoht libedatel põrandatel",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Üldine tervisekontroll kõigile töötajatele"),
            ("Raskusi tõstvad töötajad", "Lihas-skeleti hindamine, seljauuringud"),
            ("Külmkambri töötajad", "Kardiovaskulaarne uuring iga 2 aasta järel"),
            ("Noored töötajad (15–18 a)", "Iga-aastane tervisekontroll"),
        ],
        "findings": [
            "Raskuste tõstmise nõuded ei ole töötajatele selgitatud",
            "Tervisekontrollid on hilinenud",
            "Töötajatele ei ole tagatud piisavalt pause",
            "Psühhosotsiaalsed riskid (klienditeeninduse stress) on riskianalüüsist puudu",
        ],
        "checklist": [
            "Kõigil töötajatel on kehtiv tervisekontrolli tõend",
            "Riskianalüüs on koostatud ja sisaldab klienditeeninduse stressi hinnangut",
            "Raskuste käsitsi teisaldamise juhend on töötajatele tutvustatud",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Töötajatele on tagatud seadusjärgsed pausid",
            "Liigeste ja seljakaebuste ennetamine on kaetud riskianalüüsis",
            "Töötajad on teavitatud terviseriskidest kirjalikult",
        ],
        "faqs": [
            ("Kas osalise tööajaga müüjale on tervisekontroll kohustuslik?",
             "Jah, kui ta töötab ohtlikus töökeskkonnas (nt raskuste tõstmine, külmkamber). Tervisekontrolli kohustus ei sõltu tööajast."),
            ("Mis kaal on lubatud töötajal käsitsi tõsta?",
             "Meestele kuni 30 kg, naistele kuni 20 kg ühekordse tõstmisena. Korduva tõstmise korral on piirangud madalamad."),
            ("Kas klient võib töötajat rünnates olla tööõnnetus?",
             "Jah. Töökohal toimuv vägivald on tööõnnetus ja tuleb registreerida ja teavitada sellest Tööinspektsiooni, kui see põhjustab kehavigastuse."),
            ("Kas kaugtöö korraldus on kaubanduses vajalik?",
             "Tavaliselt mitte — kaubandus on klienditeenindus kohal. Kuid haldusfunktsioone täitev töötaja võib kaugtöö lepingut vajada."),
        ],
    },
    "transport": {
        "title": "Transport ja logistika",
        "slug": "transport",
        "icon": "🚛",
        "seo_title": "Töötervishoiu nõuded transpordis — juhi tervisekontroll 2026",
        "seo_desc": "Transpordi- ja logistikaettevõtte töötervishoiu nõuded: bussijuhi ja veoautojuhi tervisekontroll, töösõiduki juhiloa nõuded, ületunnitöö piirangud.",
        "og_title": "Töötervishoiu nõuded transpordis | Tööandja juhend 2026",
        "risks": [
            "Liiklusõnnetused — väsimus, tähelepanu hajumine",
            "Pikaajaline istumine ja seljalülisamba koormus",
            "Vibratsioon istmete kaudu (sõidukid)",
            "Ületunnitöö ja piiratud uneaeg",
            "Kemikaalidega kokkupuude (kütus, õlid, pidurivedelik)",
            "Raskuste tõstmine (laadimine, mahalaadimistöö)",
            "Psühhosotsiaalne stress (tähtajad, liiklusummikud)",
        ],
        "health_checks": [
            ("Iga 2 aasta järel, üle 50-aastastel iga aasta", "Mootorsõiduki juhid D-kategooria ja C-kategooria — spetsiaalne juhi tervisekontroll"),
            ("Iga 3 aasta järel", "Laopersonal ja muud töötajad"),
            ("Enne tööle asumist", "Kõigile uutele juhtidele kohustuslik esmane tervisekontroll"),
        ],
        "findings": [
            "Juhtide tervisekontrolli aeg on ületatud",
            "Puhkeaja nõudeid ei järgita (sõidumeerikute kontroll puudulik)",
            "Laadurite ja laotöötajate riskianalüüs on puudulik",
            "Ohtlike kaupade veo eritingimused on täitmata",
        ],
        "checklist": [
            "Kõigil juhtidel on kehtiv juhi tervisekontrolli tõend",
            "C ja D kategooria juhtide tervisekontrollis on järgitud iga 2 aasta nõue",
            "Riskianalüüs katab vibratsiooniriskid ja ületunnitöö mõju",
            "Ohtlike kaupade veol on ADR-nõuded täidetud",
            "Sõidumeeriku kasutamine on dokumenteeritud ja kontrollitud",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Laotöötajate raskuste tõstmise koolitused on tehtud",
        ],
        "faqs": [
            ("Kas bussijuhile ja veoautojuhile kehtivad erireeglid?",
             "Jah. C- ja D-kategooria sõidukite juhid vajavad spetsiaalset juhi tervisekontrolli, mis sisaldab nägemis-, kuulmis- ja kardiovaskulaarset uuringut. Kontroll on sagedusem kui tavalistel töötajatel."),
            ("Mitu tundi päevas tohib juht sõita?",
             "EL määrus 561/2006 piirab juhtimisaega: max 9 tundi päevas (kaks korda nädalas 10 tundi), max 56 tundi nädalas. Puhkeaeg on kohustuslik."),
            ("Kas laotöötajale on tervisekontroll kohustuslik?",
             "Jah, kui ta töötab ohtlikus töökeskkonnas (raskuste tõstmine, tõstukijuhtimine, keemikaalidega kokkupuude)."),
            ("Mis dokumendid peavad veoautos kaasas olema?",
             "Sõidumeeriku andmed, ohtlike kaupade veol ADR-dokumendid, juhi tervisekontrolli tõend, sõidukiraamat."),
        ],
    },
    "tervishoid": {
        "title": "Tervishoid",
        "slug": "tervishoid",
        "icon": "🏥",
        "seo_title": "Töötervishoiu nõuded tervishoius — meditsiinitöötaja kohustused 2026",
        "seo_desc": "Tervishoiuasutuse töötervishoiu nõuded: nakkushaiguste ennetamine, kiirguskaitse, psühhosotsiaalsed riskid ja kohustuslikud tervisekontrollid meditsiinitöötajatele.",
        "og_title": "Töötervishoiu nõuded tervishoius | Tööandja juhend 2026",
        "risks": [
            "Bioloogilised riskid (vere kaudu levivad haigused, patsiendist nakatumine)",
            "Ioniseeriv kiirgus (röntgen, CT-aparaadid)",
            "Kemikaalidega kokkupuude (desinfektandid, narkootikumid, steriliseerimisained)",
            "Vaimne koormus ja emotsionaalne kurnatus (läbipõlemissündroom)",
            "Raskuste tõstmine (patsientide käsitsemisel)",
            "Öövahetused ja ebaregulaarne tööaeg",
            "Töövägivald patsientide ja nende lähedaste poolt",
        ],
        "health_checks": [
            ("Iga 2–3 aasta järel", "Kõik tervishoiutöötajad — bioloogiliste riskidega kokkupuutuvad"),
            ("Kiirgusega töötajad", "Individuaalne kiirgusseire ja aastane tervisekontroll"),
            ("Noored töötajad (15–18 a)", "Iga-aastane tervisekontroll"),
            ("Öötöö tegijad", "Tõhustatud jälgimine — vähemalt iga 2 aasta järel"),
        ],
        "findings": [
            "Bioloogiliste riskidega töötajate immuniseerimisdokumendid puuduvad",
            "Kiirguskaitse nõuded ei ole täidetud",
            "Psühhosotsiaalset riskianalüüsi ei ole tehtud",
            "Tervisekontrollid on hilinenud",
        ],
        "checklist": [
            "Kõigil bioloogiliste riskidega kokkupuutuvatel töötajatel on vaktsineerimised (B-hepatiit jm) dokumenteeritud",
            "Kiirgusseire dokumentatsioon on korras ja kättesaadav",
            "Riskianalüüs katab bioloogilised, keemilised, kiirgus- ja psühhosotsiaalriskid",
            "Töötajatele on korraldatud koolitus nakatumise ennetamiseks",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Psühhosotsiaalsete riskide ennetamise kava on olemas",
            "Öötöö töötajate tervise jälgimine on tagatud",
        ],
        "faqs": [
            ("Kas kiirgusega töötav töötaja vajab erikontrolle?",
             "Jah. Kiirguskaitse seaduse alusel peab kiirgusega kokkupuutuv töötaja läbima individuaalse kiirgusseire ja regulaarse tervisekontrolli."),
            ("Mis on tööandja kohustus, kui töötaja nakatub patsiendilt?",
             "See on tööõnnetus. Peate kohe alustama kaitsemeetmetega, dokumenteerima juhtumi ja vajadusel teatama Tööinspektsioonile 24 tunni jooksul."),
            ("Kas läbipõlemine loetakse töötervishoiu probleemiks?",
             "Jah. Krooniline tööstress ja läbipõlemine on psühhosotsiaalse keskkonna riski tulemus. Tööandja peab psühhosotsiaalset riskianalüüsi tegema ja ennetavaid meetmeid rakendama."),
            ("Kas öötöö töötajatele on eriõigused?",
             "Öötöötaja on seaduse järgi eritöötaja. Tal on õigus sagedamale tervisekontrollile ja tööandja peab võimaldama üleminekut päevatöö, kui arst soovitab."),
        ],
    },
    "haridus": {
        "title": "Haridus",
        "slug": "haridus",
        "icon": "📚",
        "seo_title": "Töötervishoiu nõuded haridussektoris — õpetaja kohustused 2026",
        "seo_desc": "Koolide ja lasteaedade töötervishoiu nõuded: õpetajate psühhosotsiaalne tervis, häälekaitse, nakkusriskid ja tööandja kohustused haridusasutustes.",
        "og_title": "Töötervishoiu nõuded haridussektoris | Tööandja juhend 2026",
        "risks": [
            "Häälekoormus (õpetajad, koolitusspetsialistid)",
            "Psühhosotsiaalne koormus ja läbipõlemissündroom",
            "Bioloogilised riskid (nakkushaigused lasteasutustes)",
            "Halb sisekliima (ventilatsioon, temperatuur, müra klassides)",
            "Emotsionaalne kurnatus keeruliste õpilastega töötades",
            "Pikaajaline seismine ja ebaregulaarsed pausid",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Õpetajad ja hariduspersonal — üldine tervisekontroll"),
            ("Häälekasutuse probleemidega töötajad", "KNK-arsti vastuvõtt"),
            ("Lasteaiaõpetajad ja bioloogiliste riskidega kokkupuutuvad", "Nakkushaiguste kontroll"),
        ],
        "findings": [
            "Häälekoormuse riskianalüüs on tegemata",
            "Psühhosotsiaalsete riskide hindamine puudub",
            "Ventilatsioon ei vasta nõuetele (CO2 mõõtmised puuduvad)",
        ],
        "checklist": [
            "Riskianalüüs sisaldab psühhosotsiaalset ja häälekoormusriski hinnangut",
            "Kõigil töötajatel on kehtiv tervisekontrolli tõend",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Ventilatsiooni ja sisekliima mõõtmised on tehtud",
            "Töötajaid on teavitatud hääle hooldamise ja pauside vajadusest",
            "Läbipõlemise ennetamise meetmed on rakendatud",
        ],
        "faqs": [
            ("Kas õpetajale on hääleuuring kohustuslik?",
             "Seadus ei kohusta hääleuringut otseselt, kuid häälekoormus on haridussektori peamine risk ja kuulub riskianalüüsi. Kui töötajal on häälekaebused, suunab töötervishoiuarst KNK-arsti juurde."),
            ("Mis on psühhosotsiaalne riskianalüüs ja kas see on koolile kohustuslik?",
             "Jah. Psühhosotsiaalne riskianalüüs on üldise riskianalüüsi kohustuslik osa, mis hindab stressi, läbipõlemise ja töövägivalla riski."),
            ("Kas lasteaiaõpetaja vajab nakkushaiguste kontrolli?",
             "Jah. Nakkusrisk on lasteasutustes kõrge. Tööandja peab tagama töötajatele vajalikud vaktsineerimised ja terviskontrollid."),
        ],
    },
    "pollumajandus": {
        "title": "Põllumajandus",
        "slug": "pollumajandus",
        "icon": "🌾",
        "seo_title": "Töötervishoiu nõuded põllumajanduses — tööandja kohustused 2026",
        "seo_desc": "Põllumajandusettevõtte töötervishoiu nõuded: pestitsiidid, masinaohutus, hooajatöötajad ja kohustuslikud tervisekontrollid põllumajandustöös.",
        "og_title": "Töötervishoiu nõuded põllumajanduses | Tööandja juhend 2026",
        "risks": [
            "Kokkupuude pestitsiidide ja taimekaitsevahendite kemikaalidega",
            "Bioloogilised riskid (loomadega kokkupuude, zoonootilised haigused)",
            "Müra ja vibratsioon (traktorid, põllutöömasinad)",
            "Hooajalised äärmised temperatuurid (kuumus, külm)",
            "Raskuste tõstmine ja üksluised liigutused",
            "UV-kiirguse pikaajaline mõju välitöödel",
            "Kukkumisrisk masinate ja tehnikaga töötamisel",
        ],
        "health_checks": [
            ("Iga 2–3 aasta järel", "Pestitsiidide ja kemikaalidega kokkupuutuvad töötajad"),
            ("Müra/vibratsioonitöötajad", "Audiomeetria iga 2 aasta järel"),
            ("Loomakasvatus (zoonootilised riskid)", "Regulaarne nakkushaiguste kontroll"),
            ("Hooajatöötajad ohtlikes tingimustes", "Esmane tervisekontroll enne tööle asumist"),
        ],
        "findings": [
            "Pestitsiidide kasutajate tervisekontroll on tegemata",
            "Kemikaaliregister on puudulik",
            "Hooajatöötajate teavitamine ohutusreeglitest on dokumenteerimata",
        ],
        "checklist": [
            "Kõigil pestitsiidide ja kemikaalidega töötavatel töötajatel on tervisekontrolli tõend",
            "Kemikaalide ohutuskaardid on olemas ja kättesaadavad",
            "Riskianalüüs katab bioloogilised, keemilised ja füüsikalised riskid",
            "Hooajatöötajatele on tehtud ohutuskoolitus",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Müra mõõtmised on tehtud (traktorioperaatorid jm)",
        ],
        "faqs": [
            ("Kas hooajatöötajale on tervisekontroll kohustuslik?",
             "Jah, kui töö hõlmab ohtlikke tegureid (pestitsiidid, masinad, loomad). Hooajatöö pikkus ei vabasta kohustusest."),
            ("Mida teha, kui töötaja nakatub loomalt zoonootilise haigusega?",
             "See on tööõnnetus. Dokumenteerige kohe ja teavitage Tööinspektsiooni 24 tunni jooksul, kui tegu on raske tervisekahjustusega."),
            ("Kas taimekasvatustöötajal on eraldi keemikaalikoolitus kohustuslik?",
             "Pestitsiidide kasutajal peab olema vastav luba (taimekaitsevahendi kasutaja koolitustunnistus) ja tööandja kohustus on see tagada."),
        ],
    },
    "tootmine": {
        "title": "Tootmine",
        "slug": "tootmine",
        "icon": "🏭",
        "seo_title": "Töötervishoiu nõuded tootmisettevõttes — tööandja kohustused 2026",
        "seo_desc": "Tootmisettevõtte töötervishoiu nõuded: masinaohutus, kemikaalid, müra, vibratsioon ja kohustuslikud tervisekontrollid tootmises 2026.",
        "og_title": "Töötervishoiu nõuded tootmisettevõttes | Tööandja juhend 2026",
        "risks": [
            "Müra (masinad, seadmed — sageli üle 85 dB)",
            "Vibratsioon käe-randme ja kogu keha tasemel",
            "Ohtlikud kemikaalid (lahustid, värvid, rasvad, happped)",
            "Tolm (metall-, puit- või klaastolm)",
            "Korduv ühekülgne töö konveieriliinil",
            "Raskuste tõstmine ja ülekoormus",
            "Kukkumis- ja surustumisrisk masinate lähedal",
        ],
        "health_checks": [
            ("Iga 2–3 aasta järel", "Kõik tootmistöötajad — riskist sõltuv sagedus"),
            ("Müra üle 85 dB kokkupuutuvad", "Audiomeetria iga 2 aasta järel"),
            ("Vibratsioonitöötajad", "Käte ja liigeste uuring iga 2 aasta järel"),
            ("Kemikaalidega kokkupuutuvad", "Spetsiaalne kemikaalitest (maksaanalüüs, vereanalüüs jm)"),
        ],
        "findings": [
            "Müramõõtmised on tegemata või aegunud",
            "Kemikaalide ohutuskaardid puuduvad töökohal",
            "Kuulmiskaitsevahendeid ei kasutata nõuetekohaselt",
            "Vibratsioonimõõtmisi ei ole tehtud",
        ],
        "checklist": [
            "Müramõõtmised on tehtud kõigis mürarikastes ruumides (alla 3 aasta vanused)",
            "Kõigil töötajatel on kehtiv tervisekontrolli tõend",
            "Isikukaitsevahendid (kuulmiskaitsed, kindad, kaitsebrilid) on väljastatud ja kasutamine dokumenteeritud",
            "Kemikaalide register ja ohutuskaardid on korras",
            "Vibratsioonimõõtmised on tehtud (käsitööriistad, masinad)",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Riskianalüüs sisaldab kõiki füüsikalisi, keemilisi ja bioloogilisi riske",
        ],
        "faqs": [
            ("Mis müratase kohustab andma kuulmiskaitsevahendid?",
             "Kui müratase ületab 85 dB(A), peab tööandja andma kuulmiskaitsevahendid. Üle 80 dB(A) tuleb töötajat teavitada mürakahjust."),
            ("Kui sageli tuleb müramõõtmisi teha?",
             "Seadus ei täpsusta sagedust, kuid mõõtmised peavad olema ajakohased. Hea tava on iga 3–5 aasta järel, muutuste korral kohe."),
            ("Kes võib müramõõtmisi teha?",
             "Mõõtmised peab tegema akrediteeritud labor. Tulemused tuleb dokumenteerida ja töötajatele tutvustada."),
            ("Kas vibratsioonitöötajal on õigus sagedamale tervisekontrollile?",
             "Jah. Vibratsiooniga kokkupuutuv töötaja vajab iga 2 aasta järel eriarsti (neuroloog, ortopeed) uuringut."),
        ],
    },
    "hotellindus": {
        "title": "Hotellindus ja toitlustus",
        "slug": "hotellindus",
        "icon": "🏨",
        "seo_title": "Töötervishoiu nõuded hotellinduses ja toitlustuses — tööandja kohustused 2026",
        "seo_desc": "Hotellide ja restoranide töötervishoiu nõuded: toidukäitlejate tervisekontroll, öötöö, klienditeeninduse stress ja nõuetekohased dokumendid.",
        "og_title": "Töötervishoiu nõuded hotellinduses | Tööandja juhend 2026",
        "risks": [
            "Bioloogilised riskid toidukäitluses",
            "Kuuma ja külmaga töötamine (köök, külmladu)",
            "Ületunnitöö, öötöö ja ebaregulaarne tööaeg",
            "Pikaajaline seismine (kokad, kelnerid)",
            "Klienditeeninduse stress ja emotsionaalne koormus",
            "Libe põrand, kukkumisrisk köögis",
            "Kemikaalidega kokkupuude (puhastusvahendid, desinfektandid)",
        ],
        "health_checks": [
            ("Iga 2 aasta järel (toidukäitlejad)", "Toidukäitlejate kohustuslik tervistõend"),
            ("Öötöö tegijad", "Vähemalt iga 2 aasta järel, kardiovaskulaarne uuring"),
            ("Noored töötajad (15–18 a)", "Iga-aastane tervisekontroll"),
        ],
        "findings": [
            "Toidukäitlejate tervistõendid on aegunud",
            "Öötöö töötajate tervisekontroll on tegemata",
            "Hügieenikoolitus ei ole dokumenteeritud",
        ],
        "checklist": [
            "Kõigil toidukäitlejatel on kehtiv tervistõend",
            "Hügieenikoolitus on läbitud ja dokumenteeritud",
            "Öötöö töötajate tervisejälgimine on tagatud",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Riskianalüüs sisaldab köögis esinevaid riske",
            "Libisemisvastased meetmed on rakendatud",
        ],
        "faqs": [
            ("Kas suveperioodil palgatavale hooajatöötajale on tervisekontroll kohustuslik?",
             "Jah, kui töö hõlmab toidukäitlust. Tervistõend peab olema kehtiv enne toiduga töötamist."),
            ("Öötöötajale lisatasu — kas see on seadusega reguleeritud?",
             "Jah. Öötöötajale (töö ajavahemikul 22:00–6:00) kuulub tasu vähemalt 1,25-kordne tunnimäär. Öötöö ei tohi ületada 8 tundi 24-tunnises perioodis."),
            ("Mida teeb tööandja, kui töötaja on toiduaintekäitlemise tervisekontrollis mitte sobivaks tunnistatud?",
             "Töötajat ei tohi lubada toidukäitlemisele seni, kuni oht on olemas. Tööandja peab leidma töötajale alternatiivse töö või tegema töösuhtes vastavad otsused."),
        ],
    },
    "puhastusteenused": {
        "title": "Puhastusteenused",
        "slug": "puhastusteenused",
        "icon": "🧹",
        "seo_title": "Töötervishoiu nõuded puhastusteenuste sektoris — tööandja kohustused 2026",
        "seo_desc": "Koristusteenuste ja puhastusfirmade töötervishoiu nõuded: kemikaalikäitlus, lihas-skeleti riskid, öötöö ja kohustuslikud dokumendid 2026.",
        "og_title": "Töötervishoiu nõuded puhastusteenustes | Tööandja juhend 2026",
        "risks": [
            "Kemikaalidega kokkupuude (puhastusvahendid, desinfektandid, lahurid)",
            "Korduv ühekülgne liikumine (pühkimine, küürimine)",
            "Pikaajaline küürus asend",
            "Libe põrand — kukkumisrisk",
            "Öötöö ja vahetustega töö",
            "Bioloogilised riskid haiglakoristuses",
            "Allergilised reaktsioonid kemikaalidele",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Üldine tervisekontroll"),
            ("Kemikaalidega kokkupuutuvad", "Spetsiaalne keemikaalikontroll, naha- ja kopsuuuring"),
            ("Haiglakoristajad (bioloogilised riskid)", "Nakkushaiguste kontroll, vaktsineerimised"),
        ],
        "findings": [
            "Kemikaalide ohutuskaardid ei ole töökohal kättesaadavad",
            "Isikukaitsevahendeid (kindaid, kaitsepõlle) ei kasutata",
            "Bioloogiliste riskidega töötajate vaktsineerimine on dokumenteerimata",
        ],
        "checklist": [
            "Kemikaalide ohutuskaardid on töökohal kättesaadavad",
            "Kõigil töötajatel on nõuetekohased isikukaitsevahendid",
            "Tervisekontrollid on tehtud ja dokumenteeritud",
            "Riskianalüüs katab keemilised, bioloogilised ja ergonoomilised riskid",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Töötajad on koolitatud kemikaalidega ohutu töötamise osas",
        ],
        "faqs": [
            ("Kas lühiajalisele lepinguga koristajale on tervisekontroll kohustuslik?",
             "Jah, kui töö hõlmab ohtlikke kemikaale või bioloogilisi riske. Lepingu lühidus ei vabasta tööandjat kohustusest."),
            ("Millised kindad on kohustuslikud kemikaalide kasutamisel?",
             "Sõltub kemikaalidest. Kaitsekindad peavad vastama EN 374 standardile. Ohutuskaart täpsustab vajalikud kaitsevahendid."),
            ("Mida teha, kui töötajal tekib kemikaalidest nahalööve?",
             "Lõpetage kokkupuude. Pöörduge töötervishoiuarsti poole. Kui tegemist on kutsehaigusega, tuleb see deklareerida."),
        ],
    },
    "laondus": {
        "title": "Laondus",
        "slug": "laondus",
        "icon": "📦",
        "seo_title": "Töötervishoiu nõuded laonduses — tööandja kohustused 2026",
        "seo_desc": "Laonduse ja logistikakeskuste töötervishoiu nõuded: tõstuki juhtimine, raskuste tõstmine, müra, vibratsioon ja kohustuslikud tervisekontrollid 2026.",
        "og_title": "Töötervishoiu nõuded laonduses | Tööandja juhend 2026",
        "risks": [
            "Raskuste tõstmine ja käsitsi teisaldamine",
            "Tõstukite ja liikuva tehnika oht",
            "Müra (mototsüklid, tõstukid, masinad)",
            "Vibratsioon tõstukitelt",
            "Pikaajaline istumine (tõstuki juhid) ja seismine",
            "Madala temperatuuriga külmlao tingimused",
            "Kukkumis- ja surustumisrisk kõrgete riiulite lähedal",
        ],
        "health_checks": [
            ("Iga 2–3 aasta järel", "Laotöötajad ja tõstukijuhid"),
            ("Tõstukijuhid", "Iga 2 aasta järel — nägemis-, kuulmis- ja kardiovaskulaarne uuring"),
            ("Külmalaos töötajad", "Kardiovaskulaarne uuring iga 2 aasta järel"),
        ],
        "findings": [
            "Tõstukijuhtide load ja tervisekontroll on kehtivusaja ületanud",
            "Raskuste tõstmise nõudeid ei järgita",
            "Külmalao töötajate eriohutuse nõuded on täitmata",
        ],
        "checklist": [
            "Kõigil tõstukijuhtidel on kehtiv luba ja tervisekontrolli tõend",
            "Raskuste käsitsi teisaldamise nõuded on töötajatele selgitatud",
            "Külmala töötingimused (riietus, pausid) on dokumenteeritud",
            "Riskianalüüs katab kõik laonduse riskid",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Müramõõtmised on tehtud",
        ],
        "faqs": [
            ("Kas tõstukijuhil peab olema eriload?",
             "Jah. Tõstuki juhtimiseks peab töötajal olema tõstukijuhi luba ja kehtiv tervisekontrolli tõend, mis kinnitab sobivust sellele tööle."),
            ("Mis kaal on lubatud ühel inimesel käsitsi tõsta?",
             "Meestele kuni 30 kg, naistele kuni 20 kg ühekordse tõstmisena. Korduva tõstmise puhul on piirangud madalamad."),
            ("Külmlao töötingimused — milliseid lisanõudeid on?",
             "Töötajatele peab tagama sooja riietuse, piisavad pausid ja külmast väljumise võimaluse. Lisaks tõhustatud tervisejälgimine."),
        ],
    },
    "energeetika": {
        "title": "Energeetika",
        "slug": "energeetika",
        "icon": "⚡",
        "seo_title": "Töötervishoiu nõuded energeetikas — tööandja kohustused 2026",
        "seo_desc": "Energeetika- ja elektriseadmete sektori töötervishoiu nõuded: elektrioht, kõrgustes töö, kiirgus ja kohustuslikud tervisekontrollid 2026.",
        "og_title": "Töötervishoiu nõuded energeetikas | Tööandja juhend 2026",
        "risks": [
            "Elektriohu risk (kõrgepinge, otsekokkupuude)",
            "Kõrgustes töö (liinitöötajad, tuulepargid)",
            "Ioniseeriva kiirguse oht (tuumaenergeetika)",
            "Müra ja vibratsioon (generaatorid, turbiinitoad)",
            "Ohtlikud kemikaalid (isoleeritud seadmetes kasutatavad ained)",
            "Heitgaasid ja halvasti ventileeritud seadmeruumid",
        ],
        "health_checks": [
            ("Iga 2 aasta järel", "Elektriseadmete hooldajad ja liinitöötajad"),
            ("Kõrgustes töötajad", "Iga 2 aasta järel — tasakaalutest, kardiograafia"),
            ("Kiirgusega kokkupuutuvad", "Aastane tervisekontroll koos kiirgusseire andmetega"),
        ],
        "findings": [
            "Elektriohutuse koolitus ei ole dokumenteeritud",
            "Kõrgustes töötamise lubade kehtivus on ületatud",
            "Individuaalsed kiirgusseire passi andmed on puudulikud",
        ],
        "checklist": [
            "Kõigil kõrgepingega töötavatel on kehtiv elektriohutuse luba",
            "Kõrgustes töötajate tervisekontrollid on aja sees",
            "Kiirgusseire on dokumenteeritud (kiirguspassid)",
            "Riskianalüüs katab elektri-, kiirgus- ja kemikaaliriskid",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
        ],
        "faqs": [
            ("Kas elektriku töö on riski tase 1 või 2?",
             "Elektriline oht klassifitseerub kõrge riskitasemega. Tervisekontrolli sagedus on kõrgem — iga 2 aasta järel."),
            ("Kõrgustes töötamise tervise nõuded — mis täpselt kontrollitakse?",
             "Kardiogramm, vererõhk, neuroloogiline uuring ja tasakaalutest. Kõrguses töötamine on keelatud, kui arst tuvastab sobimatuse."),
        ],
    },
    "finantsteenused": {
        "title": "Finantsteenused",
        "slug": "finantsteenused",
        "icon": "🏦",
        "seo_title": "Töötervishoiu nõuded finantsteenustes — tööandja kohustused 2026",
        "seo_desc": "Pankade, kindlustusseltside ja finantsfirmade töötervishoiu nõuded: kuvaritöö, psühhosotsiaalne tervis ja kohustuslikud dokumendid 2026.",
        "og_title": "Töötervishoiu nõuded finantsteenustes | Tööandja juhend 2026",
        "risks": [
            "Kuvariga töö — silmade üleväsimine, ergonoomika",
            "Psühhosotsiaalne koormus (stress, läbipõlemine)",
            "Pikaajaline istuv töö",
            "Töökiusamine ja klientide agressiivne käitumine",
            "Ületunnitöö ja töö-eraelu tasakaalu puudus",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Kuvaritöötajad — silmauuring, lihas-skeleti hindamine"),
            ("Kõrge stressitasemega töötajad", "Psüühilise tervise hindamine töötervishoiuarsti juures"),
        ],
        "findings": [
            "Kuvaritöötajate silmauuringud puuduvad",
            "Psühhosotsiaalne riskianalüüs on tegemata",
            "Ergonoomika hindamine ei ole dokumenteeritud",
        ],
        "checklist": [
            "Kõigil kuvaritöötajatel on silmauuring tehtud",
            "Psühhosotsiaalne riskianalüüs on koostatud",
            "Töökohtade ergonoomika on hinnatud",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Töötajatele on tagatud regulaarsed pausid",
        ],
        "faqs": [
            ("Kuvaritöö nõuded — kas need kehtivad ka kodus töötavatele töötajatele?",
             "Jah. Kaugtöötaja kuvaritöö nõuded on samad. Tööandja peab tagama ergonoomika hindamise ka kodukontori jaoks."),
            ("Kas finantssektori töötajale on psühhiaatri konsultatsioon kohustuslik?",
             "Kohustuslik see ei ole, kuid psühhosotsiaalse riski hindamine ja ennetamine on tööandja seadusjärgne kohustus."),
            ("Kas avatud kontor on terviseriski allikas?",
             "Avatud kontor kõrge müratasemega on risk (kontsentratsiooniprobleem, stress). Kaasake see riskianalüüsi."),
        ],
    },
    "avalik-haldus": {
        "title": "Avalik haldus",
        "slug": "avalik-haldus",
        "icon": "🏛️",
        "seo_title": "Töötervishoiu nõuded avalikus halduses — tööandja kohustused 2026",
        "seo_desc": "Riigiasutuste ja kohalike omavalitsuste töötervishoiu nõuded: büroötöö, avaliku teenistuse erireeglid ja kohustuslikud dokumendid 2026.",
        "og_title": "Töötervishoiu nõuded avalikus halduses | Tööandja juhend 2026",
        "risks": [
            "Kuvariga töö (büroötöö)",
            "Psühhosotsiaalne koormus (kodanike teenindamine, otsustega kaasnev vastutus)",
            "Töökiusamine ja eetikadilemmas",
            "Pikaajaline istuv töö",
            "Ületunnitöö periooditi (eelarve- ja seadusloomeperioodid)",
        ],
        "health_checks": [
            ("Iga 3 aasta järel", "Büroötöötajad — kuvaritöö uuring"),
            ("Tegevväelised ja eristaatusega ametiisikud", "Erikontrollid vastavalt ametile"),
        ],
        "findings": [
            "Kuvaritöötajate tervisekontroll puudub",
            "Psühhosotsiaalne riskianalüüs on tegemata",
            "Riskianalüüsi uuendamine on hilinenud",
        ],
        "checklist": [
            "Riskianalüüs on tehtud ja alla 3 aasta vana",
            "Kuvaritöötajate silmauuringud on tehtud",
            "Psühhosotsiaalne riskianalüüs on olemas",
            "Töötervishoiu teenuse osutajaga on sõlmitud leping",
            "Töötajaid on teavitatud töökeskkonna riskidest",
        ],
        "faqs": [
            ("Kas avalikus teenistuses kehtivad teistsugused töötervishoiu reeglid?",
             "Üldpõhimõtted on samad (TTOS kehtib kõigile tööandjatele). Mõnedel ametikohtadel (politseinikud, päästetöötajad, kaitseväelased) kehtivad lisaks erireeglid."),
            ("Kas riigiasutuses on töötervishoiu teenuse leping kohustuslik?",
             "Jah. Seaduse järgi peab igal tööandjal (sh riigiasutustel) vähemalt ühe töötajaga olema sõlmitud leping töötervishoiu teenuse osutajaga."),
            ("Mida teha, kui töötajal on burnout?",
             "Suunake töötervishoiuarsti juurde. Arst hindab töövõimet ja soovitab meetmeid. Tööandja kohustus on leida lahendus — kohandada töökoormust või pakkuda pausi."),
        ],
    },
}

# ─── CITY DATA ────────────────────────────────────────────────────────────────

CITIES = {
    "tallinn": {
        "title": "Tallinn",
        "slug": "tallinn",
        "region": "Harju maakond",
        "icon": "🏙️",
        "seo_title": "Töötervishoiu nõuded Tallinnas — kohalikud teenuspakkujad 2026",
        "seo_desc": "Tallinna piirkonna töötervishoiu nõuded, lähimad teenuspakkujad, Tööinspektsiooni piirkondlik statistika ja tööandja praktilised juhised.",
        "og_title": "Töötervishoiu nõuded Tallinnas | Tööandja juhend 2026",
        "description": "Tallinn on Eesti suurim tööjõuturg — üle 230 000 töötajaga. Harju maakond on ka Tööinspektsiooni järelevalves kõige aktiivsem piirkond: 2026. aasta plaanis on kontrollida siin üle 600 ettevõtte.",
        "local_specifics": [
            "Harju maakonnas on 2026. aastal planeeritud üle 600 tööinspektsiooni kontrolli",
            "Tallinna sadamapiirkond ja tootmisettevõtted on suurema tähelepanu all",
            "IT-sektori kiire kasv on toonud uued psühhosotsiaalse tervise riskid",
            "Ehitusbuumiga kaasneb järelevalve intensiivistumine ehitussektoris",
        ],
        "providers": [
            ("Valvekliinik Töötervishoiuteenused", "Paldiski mnt 80, Tallinn", "tootervishoid@valvekliinik.ee", "Tallinna ja Harju maakond"),
            ("Medicum Töömeditsiin", "Kesklinn, Tallinn", "info@medicum.ee", "Üle-eestiline teenus"),
            ("Meliva", "Tallinn (mitu filiaali)", "info@meliva.ee", "Üle-eestiline teenus"),
            ("Synlab Tervishoid", "Veerenni 53A, Tallinn", "info@synlab.ee", "Üle-eestiline teenus"),
        ],
        "inspection_stats": [
            "2025. aastal kontrolliti Harju maakonnas 587 ettevõtet",
            "Kõige enam leiti rikkumisi: riskianalüüs tegemata, tervisekontrollid hilinenud",
            "Ettevõtetest 38% sai ettekirjutuse",
            "Kõige rohkem kontrolliti ehitus-, transport- ja kaubandussektorit",
        ],
        "faqs": [
            ("Millal on Tallinnas järgmised tööinspektsiooni kontrollid?",
             "Tööinspektsioon ei avalda täpset kontrollgraafikut ettevõtete kaupa. Kontrolle tehakse aastaringselt. Kuid planeeritud kontrollidest teavitatakse tihti ette."),
            ("Kuidas leida Tallinnas sobivat töötervishoiu teenuse osutajat?",
             "Otsige töötervishoiu teenuse osutajate registrist (ti.ee) või pöörduge otse meie poole — aitame leida teie ettevõttele sobiva lahenduse."),
            ("Kas Tallinna ettevõtetele kehtivad teistsugused nõuded?",
             "Ei. Töötervishoiu seadus kehtib ühtlaselt kogu Eestis. Erisusi pole piirkonniti — nõuded sõltuvad sektorist ja töötajate arvust."),
            ("Mida teha, kui Tööinspektsioon teatab kontrollist?",
             "Koostage kõik dokumendid (riskianalüüs, tervisekontrollide protokollid, lepingud). Kui midagi on puudu, on mõned asjad võimalik kiiresti korda saada. Pöörduge meie poole."),
        ],
    },
    "tartu": {
        "title": "Tartu",
        "slug": "tartu",
        "region": "Tartu maakond",
        "icon": "🎓",
        "seo_title": "Töötervishoiu nõuded Tartus — kohalikud teenuspakkujad 2026",
        "seo_desc": "Tartu piirkonna töötervishoiu nõuded, lähimad teenuspakkujad, Tööinspektsiooni statistika Tartu maakonnas ja praktilised tööandja juhised.",
        "og_title": "Töötervishoiu nõuded Tartus | Tööandja juhend 2026",
        "description": "Tartu on Eesti teisuurim tööturg, kus domineerivad haridus-, tervishoid- ja IT-sektor. Tartu Ülikooli klastri tõttu on siin palju teadmistepõhist tööd, kuid ka olulisi põllumajandus- ja tootmisettevõtteid.",
        "local_specifics": [
            "Tartus on tervishoiu- ja haridussektori töötervishoiu nõuded kõrge tähelepanu all",
            "Tartu Ülikool ja ülikoolihaigla on piirkonna suurimad tööandjad",
            "Tartumaa põllumajandusettevõtetes on Tööinspektsioon 2026 suurendanud kontrolle",
            "IT-klastri kasv on toonud kaasa psühhosotsiaalse tervise probleemide kasvu",
        ],
        "providers": [
            ("Valvekliinik Töötervishoiuteenused (kaugkonsultatsioon)", "Kaughindamine Tartus asuvatele ettevõtetele", "tootervishoid@valvekliinik.ee", "Kaughter Tartu- ja Lõuna-Eesti ettevõtted"),
            ("Tartu Ülikooli Kliinikum Töömeditsiin", "L. Puusepa 8, Tartu", "info@kliinikum.ee", "Tartu piirkond"),
            ("Synlab Tartu", "Riia 167, Tartu", "info@synlab.ee", "Tartu piirkond"),
        ],
        "inspection_stats": [
            "2025. aastal kontrolliti Tartu maakonnas 284 ettevõtet",
            "Levinuimad rikkumised: riskianalüüs aegunud, töötervishoiu leping puudub",
            "Põllumajandussektor sai Tartu maakonnas kõige rohkem ettekirjutusi",
            "Ettevõtetest 35% sai ettekirjutuse",
        ],
        "faqs": [
            ("Kas Tartus saab kasutada Tallinna töötervishoiu teenust?",
             "Jah. Töötervishoiu teenuse osutaja asukoht ei pea olema samas piirkonnas. Lepingu sõlmimine on oluline, mitte geograafiline asukoht."),
            ("Millal peavad Tartumaa põllumajandusettevõtted olema kontrolliks valmis?",
             "Tööinspektsioon ei avalda täpset ajakava. Hooldage dokumentatsiooni pidevalt."),
            ("Kas Tartu Ülikooli töötajatel on teistsugused nõuded?",
             "Ülikool on tööandja nagu iga teine. Akadeemilise töötaja töötervishoiu nõuded sõltuvad tema töötingimustest — laboritöötajatel on rangemad nõuded kui halduspersonalil."),
        ],
    },
    "parnu": {
        "title": "Pärnu",
        "slug": "parnu",
        "region": "Pärnu maakond",
        "icon": "🌊",
        "seo_title": "Töötervishoiu nõuded Pärnus — kohalikud teenuspakkujad 2026",
        "seo_desc": "Pärnu piirkonna töötervishoiu nõuded, hotellinduse ja teenindussektori erisused, lähimad teenuspakkujad ja Tööinspektsiooni statistika.",
        "og_title": "Töötervishoiu nõuded Pärnus | Tööandja juhend 2026",
        "description": "Pärnu on Eesti suvepealinn, kus turism, hotellindus ja toitlustus moodustavad märkimisväärse osa tööturust. Hooajalisus tähendab suurt hulka ajutisi töötajaid — kellele töötervishoiu nõuded samuti kehtivad.",
        "local_specifics": [
            "Pärnu hotellinduse ja toitlustuse sektor on Tööinspektsiooni tähelepanu all kevadel-suvel",
            "Hooajatöötajate suur osakaal tekitab väljakutseid tervisekontrollide korraldamisel",
            "Pärnu ehitussektor on aktiivne — ehitusohutus on prioriteet",
            "Põllumajandussektor Pärnumaal on oluline hooajatöötajate andjana",
        ],
        "providers": [
            ("Valvekliinik Töötervishoiuteenused", "Kaughindamine Pärnu piirkonna ettevõtetele", "tootervishoid@valvekliinik.ee", "Kaughindamine + kohalik partner"),
            ("Pärnu Haigla Töömeditsiin", "Ristiku 1, Pärnu", "info@ph.ee", "Pärnu piirkond"),
            ("Synlab Pärnu", "Papiniidu 4, Pärnu", "info@synlab.ee", "Pärnu piirkond"),
        ],
        "inspection_stats": [
            "2025. aastal kontrolliti Pärnu maakonnas 198 ettevõtet",
            "Hooajalisus tekitab järelevalve raskusi — kontrollid koonduvad mai-septembrisse",
            "Levinuimad leiud: hooajatöötajate tervisekontrollid puuduvad, hügieenikoolitus dokumenteerimata",
            "Ettekirjutuse sai 41% kontrollitud ettevõtetest",
        ],
        "faqs": [
            ("Kas suvehooaja töötajatele peab tervisekontrolli tegema?",
             "Jah, kui nad töötavad ohtlikus töökeskkonnas. Toidukäitlejatele on see kohustuslik alati. Planeerige tervisekontrollid enne hooaja algust."),
            ("Pärnus on vähe töötervishoiu teenuse osutajaid — kas pean leidma Tallinnast?",
             "Ei ole vaja. Teenuse osutaja ei pea olema kohapeal. Kaughindamine on lubatud mitmes olukorras ja leping võib olla Tallinna või mõne muu linna teenuse osutajaga."),
            ("Kas rannahotellil on erisused?",
             "Erisused sõltuvad tegevusalast. Hotellindus, toitlustus ja rannateenused — kõigil on oma riskiprofiil. Koostage sektori-spetsiifiline riskianalüüs."),
        ],
    },
    "narva": {
        "title": "Narva",
        "slug": "narva",
        "region": "Ida-Viru maakond",
        "icon": "🏰",
        "seo_title": "Töötervishoiu nõuded Narvas — tööandja kohustused 2026",
        "seo_desc": "Narva ja Ida-Viru piirkonna töötervishoiu nõuded: tootmissektori erisused, venekeelne juhend töötervishoiu kohta ja kohalikud teenuspakkujad.",
        "og_title": "Töötervishoiu nõuded Narvas | Tööandja juhend 2026",
        "description": "Narva ja Ida-Viru maakond on tootmise, energeetika ja rasketööstuse piirkond. Piirkondliku eripärana on siin suurem osa töötajatest venekeelsed — teavitamiskohustused peavad olema täidetud keeles, mida töötaja mõistab.",
        "local_specifics": [
            "Ida-Viru maakonna tootmis- ja energeetikasektoris on rangemad tööohutuse kontrollid",
            "Venekeelsetele töötajatele peab riskianalüüsi ja ohutusjuhendid esitama nende poolt mõistetavas keeles",
            "Ajalooliselt kõrge tööõnnetuste arv — Narva piirkond on Tööinspektsiooni prioriteet",
            "Narva Elektrijaam ja suurettevõtted on regulaarse järelevalve all",
        ],
        "providers": [
            ("Valvekliinik Töötervishoiuteenused", "Kaugkonsultatsioon Ida-Viru ettevõtetele", "tootervishoid@valvekliinik.ee", "Üle-eestiline teenus"),
            ("Ida-Viru Keskhaigla Töömeditsiin", "Ravi 10, Kohtla-Järve", "info@ivhk.ee", "Ida-Viru maakond"),
            ("Synlab Narva", "Tartu mnt 18, Narva", "info@synlab.ee", "Narva piirkond"),
        ],
        "inspection_stats": [
            "2025. aastal kontrolliti Ida-Viru maakonnas 312 ettevõtet",
            "Kõrgeim tööõnnetuste sagedus Eestis on Ida-Viru maakonnas",
            "Peamised rikkumised: ohutusjuhendid ei ole töötajatele arusaadavas keeles, riskianalüüs puudub",
            "Ettekirjutuse sai 47% kontrollitud ettevõtetest — kõrgeim protsent Eestis",
        ],
        "faqs": [
            ("Kas venekeelsele töötajale peab ohutusjuhendid vene keeles andma?",
             "Jah. Tööandja peab tagama, et töötaja saab aru kõigist ohutus- ja terviseriskidest. Kui töötaja ei valda eesti keelt piisavalt, peavad dokumendid olema tema mõistetavas keeles."),
            ("Kas Narvas on kohalikke töötervishoiu teenuse osutajaid?",
             "Narvas on piiratud valik. Ida-Viru Keskhaigla ja Synlab pakuvad teenust piirkonnas. Kaugkonsultatsioon on samuti seadusjärgne lahendus."),
            ("Ida-Virumaa tootmisettevõte — millele erilist tähelepanu pöörata?",
             "Müra, vibratsioon, kemikaalid, tolm. Veenduge, et müramõõtmised on tehtud, kemikaalide ohutuskaardid on kättesaadavad ja töötajate tervisekontrollid on aja sees."),
            ("Kas kõrge tööõnnetuste sagedus toob kaasa automaatselt kontrolli?",
             "Tööõnnetus peab olema teavitatud Tööinspektsioonile. Tõsine tööõnnetus toob kaasa järelevalve. Samuti võib piirkondlik statistika viia planeeritud kontrollini."),
        ],
    },
    "johvi": {
        "title": "Jõhvi",
        "slug": "johvi",
        "region": "Ida-Viru maakond",
        "icon": "⛏️",
        "seo_title": "Töötervishoiu nõuded Jõhvis — tööandja kohustused 2026",
        "seo_desc": "Jõhvi ja Ida-Viru piirkonna töötervishoiu nõuded kaevanduses, tootmises ja energeetikas. Kohalikud teenuspakkujad ja Tööinspektsiooni nõuded.",
        "og_title": "Töötervishoiu nõuded Jõhvis | Tööandja juhend 2026",
        "description": "Jõhvi on Ida-Viru maakonna administratiivkeskus ja põlevkivitööstuse südames. Piirkonna töötervishoid on mõjutatud rasketööstusest, kaevandamisest ja energeetikast — kõigil neil on ranged töötervishoiu nõuded.",
        "local_specifics": [
            "Põlevkivikaevandamine ja -töötlemine toob spetsiifilisi terviseriske (tolm, gaasid, vibratsioon)",
            "Ida-Viru maakond tervikuna on Tööinspektsiooni kõrgendatud tähelepanu piirkond",
            "Venekeelne töötajaskond — ohutusdokumendid peavad olema mõistetavas keeles",
            "Piirkondliku tööõnnetuste sagedus Eesti kõrgeim — ennetamine on eriti oluline",
        ],
        "providers": [
            ("Valvekliinik Töötervishoiuteenused", "Kaugkonsultatsioon Ida-Viru ettevõtetele", "tootervishoid@valvekliinik.ee", "Üle-eestiline teenus"),
            ("Ida-Viru Keskhaigla Töömeditsiin", "Ravi 10, Kohtla-Järve", "info@ivhk.ee", "Ida-Viru maakond"),
            ("Mediq Eesti / Tervisekeskus Jõhvis", "Narva mnt 1, Jõhvi", "info@mediq.ee", "Kohalik teenus"),
        ],
        "inspection_stats": [
            "Jõhvi piirkond on osa Ida-Viru maakonnast — kus 2025. aastal kontrolliti 312 ettevõtet",
            "Põlevkivitööstuses on töötervishoiu rikkumiste sagedus piirkondlikult kõrgeim",
            "Levinuimad probleemid: tolmu- ja gaasimõõtmised tegemata, tervisekontrollid hilinenud",
            "Ettekirjutuse sai 47% kontrollitud ettevõtetest",
        ],
        "faqs": [
            ("Kas kaevanduses töötaval inimesel on erisused töötervishoius?",
             "Jah. Kaevandamine on kõrge riskiga tegevus. Kaevurite tervisekontroll on sagedusem (iga 1–2 aasta järel), ning hõlmab spetsiaalseid kopsukontrolle ja auditooriat."),
            ("Põlevkivitolmu tervisemõjud — mida peaks tööandja teadma?",
             "Põlevkivitolm võib põhjustada pneumokonioosi (tolmukoppe). Tööandja peab tagama regulaarsed tolmumõõtmised, tolmumaski kasutamise ja kopsuuringud töötajatele."),
            ("Kas Jõhvis saab ka kaughindamist kasutada?",
             "Jah. Seadus ei nõua, et töötervishoiu teenuse osutaja oleks füüsiliselt kohal. Kaughindamine on lubatud, kuid tervisekontrolle teeb kohalik teenuse osutaja."),
            ("Mis juhtub, kui kaevur saab tööl kutsehaiguse?",
             "Kutsehaigus tuleb deklareerida töötervishoiuarsti kaudu. Töötajal on õigus hüvitisele. Tööandja peab kohe läbi vaatama töötingimused ja riskianalüüsi."),
        ],
    },
}

# ─── HTML TEMPLATE ────────────────────────────────────────────────────────────

def build_faq_schema(faqs):
    items = []
    for q, a in faqs:
        items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": items
    }

def build_article_schema(title, desc, url, sector_or_city):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": url,
        "publisher": {
            "@type": "Organization",
            "name": "Valvekliinik Töötervishoiuteenused",
            "url": "https://valvekliinik.ee"
        },
        "author": {
            "@type": "Organization",
            "name": "Valvekliinik Töötervishoiuteenused"
        },
        "inLanguage": "et"
    }

def generate_sector_page(s):
    slug = s["slug"]
    title = s["title"]
    canonical = f"{BASE_URL}/sektorid/{slug}.html"
    
    faq_schema = json.dumps(build_faq_schema(s["faqs"]), ensure_ascii=False, indent=2)
    article_schema = json.dumps(build_article_schema(s["seo_title"], s["seo_desc"], canonical, title), ensure_ascii=False, indent=2)
    
    risks_html = "\n".join(f"<li>{r}</li>" for r in s["risks"])
    
    health_rows = ""
    for freq, desc in s["health_checks"]:
        health_rows += f"""
        <tr>
          <td><strong>{freq}</strong></td>
          <td>{desc}</td>
        </tr>"""
    
    findings_html = "\n".join(f'<li class="finding-item"><span class="finding-icon">⚠️</span> {f}</li>' for f in s["findings"])
    
    checklist_html = "\n".join(
        f'<label class="checklist-item"><input type="checkbox"> <span>{c}</span></label>'
        for c in s["checklist"]
    )
    
    faq_html = ""
    for i, (q, a) in enumerate(s["faqs"]):
        faq_html += f"""
      <div class="faq-item" id="faq-{i+1}">
        <button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">
          {q}
          <span class="faq-arrow">▼</span>
        </button>
        <div class="faq-a" hidden>
          <p>{a}</p>
        </div>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="et">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{s["seo_title"]}</title>
  <meta name="description" content="{s["seo_desc"]}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{s["og_title"]}">
  <meta property="og:description" content="{s["seo_desc"]}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Valvekliinik Töötervishoiuteenused">
  <meta property="og:locale" content="et_EE">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{s["og_title"]}">
  <meta name="twitter:description" content="{s["seo_desc"]}">

  <link rel="stylesheet" href="../style.css">

  <!-- Schema: Article -->
  <script type="application/ld+json">
{article_schema}
  </script>
  <!-- Schema: FAQ -->
  <script type="application/ld+json">
{faq_schema}
  </script>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="../index.html" class="logo">
      <span class="logo-main">Valvekliinik</span>
      <span class="logo-sub">Töötervishoiu portaal</span>
    </a>
    <nav>
      <a href="../index.html">Avaleht</a>
      <a href="../kontrollnimekiri.html">Kontrollnimekiri</a>
      <a href="../kalkulaator.html">Kalkulaator</a>
      <a href="../korduma.html">KKK</a>
      <a href="../enesekontroll.html">Enesekontroll</a>
    </nav>
  </div>
</header>

<div class="page-hero">
  <div class="page-hero-inner">
    <div class="breadcrumb">
      <a href="../index.html">Avaleht</a> › <a href="../index.html#sektorid">Sektorid</a> › {title}
    </div>
    <h1>{s["icon"]} Töötervishoiu nõuded: {title}</h1>
    <p>Kõik, mida tööandjana peate teadma töötervishoiu kohustuste kohta {title.lower()} sektoris — selgelt ja praktiliselt.</p>
  </div>
</div>

<main>

  <!-- Terviseriskid -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">⚠️ Peamised terviseriskid {title.lower()} sektoris</h2>
      <p class="section-sub">Need on riskid, millega teie töötajad kõige sagedamini kokku puutuvad. Kõik need peavad olema kajastatud teie riskianalüüsis.</p>
      <ul class="risk-list">
        {risks_html}
      </ul>
      <div class="info-box" style="margin-top:24px;">
        <strong>Mis on riskianalüüs?</strong> Riskianalüüs on kirjalik dokument, kus hindate kõiki töökohal esinevaid ohte ja planeerite meetmed nende vähendamiseks. See on kohustuslik igale tööandjale, kellel on vähemalt üks töötaja.
      </div>
    </div>
  </section>

  <!-- Tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🩺 Kohustuslikud tervisekontrollid</h2>
      <p class="section-sub">Tervisekontrollide sagedus sõltub terviseriskide tasemest. Allpool on {title.lower()} sektori põhilised nõuded.</p>
      <div style="overflow-x:auto;">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sagedus</th>
              <th>Kellele ja mida sisaldab</th>
            </tr>
          </thead>
          <tbody>
            {health_rows}
          </tbody>
        </table>
      </div>
      <div class="info-box" style="margin-top:24px; border-left-color:var(--success);">
        <strong>Oluline meelde jätta:</strong> Tervisekontrolli kulud peab katma tööandja. Töötajalt kulusid kinni pidada ei tohi. Esimene tervisekontroll peab toimuma <em>enne</em> tööle asumist.
      </div>
    </div>
  </section>

  <!-- Tööinspektsiooni leiud -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">🔍 Tööinspektsiooni sagedased leiud {title.lower()} sektoris</h2>
      <p class="section-sub">Need on vead, mida Tööinspektsioon {title.lower()} ettevõtetes kõige sagedamini tuvastab. Kontrollige, kas teie ettevõttes on kõik korras.</p>
      <ul class="findings-list">
        {findings_html}
      </ul>
      <div class="info-box" style="margin-top:24px; border-left-color:var(--danger);">
        <strong>Trahvid ulatuvad kuni €32 000.</strong> Tööinspektsiooni ettekirjutuse täitmata jätmine võib kaasa tuua kuni 32 000-eurose trahvi. Ennetamine on odavam kui tagajärgedega tegelemine.
      </div>
    </div>
  </section>

  <!-- Kontrollnimekiri -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">✅ {title} sektori vastavuse kontrollnimekiri</h2>
      <p class="section-sub">Märkige ära kõik täidetud punktid. Kui midagi jääb märkimata — on see koht, millele tähelepanu pöörata.</p>
      <div class="checklist-container">
        {checklist_html}
      </div>
      <p style="margin-top:20px; color:var(--text-muted); font-size:0.9rem;">
        ℹ️ See kontrollnimekiri on üldine juhis. Täpne kohustuste loetelu sõltub teie ettevõtte suurusest, töötajatest ja konkreetsetest terviseriskidest.
      </p>
    </div>
  </section>

  <!-- KKK -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">❓ Korduma kippuvad küsimused</h2>
      <p class="section-sub">{title} sektori tööandjate kõige sagedamini esitatud küsimused.</p>
      <div class="faq-list">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section cta-section">
    <div class="container">
      <div class="cta-box">
        <h2>Ei jõua kõigega ise tegeleda?</h2>
        <p>Valvekliinik haldab teie töötervishoidu täielikult — riskianalüüsist kuni tervisekontrollide korraldamiseni. Alates <strong>€10 töötaja kohta kuus</strong>.</p>
        <div class="cta-actions">
          <a href="../enesekontroll.html" class="btn btn-gold">Tehke enesekontroll →</a>
          <a href="mailto:tootervishoid@valvekliinik.ee" class="btn btn-outline">✉️ tootervishoid@valvekliinik.ee</a>
        </div>
        <p class="cta-disclaimer">Tasuta esmakonsultatsioon. Ilma müügikõneta.</p>
      </div>
    </div>
  </section>

</main>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div>
        <div class="footer-brand">Valvekliinik Töötervishoiuteenused</div>
        <p style="color:var(--grey);font-size:0.85rem;">Vabaduse väljak 8, Tallinn · tootervishoid@valvekliinik.ee</p>
      </div>
      <div>
        <p style="color:var(--grey);font-size:0.85rem;max-width:400px;">See portaal annab üldist teavet töötervishoiu kohta. See ei asenda juriidilist nõustamist ega töötervishoiu teenust.</p>
      </div>
    </div>
  </div>
</footer>

<script>
function toggleFaq(btn) {{
  const answer = btn.nextElementSibling;
  const expanded = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', !expanded);
  answer.hidden = expanded;
  btn.querySelector('.faq-arrow').textContent = expanded ? '▼' : '▲';
}}
</script>

</body>
</html>"""


def generate_city_page(c):
    slug = c["slug"]
    title = c["title"]
    canonical = f"{BASE_URL}/linnad/{slug}.html"
    
    faq_schema = json.dumps(build_faq_schema(c["faqs"]), ensure_ascii=False, indent=2)
    article_schema = json.dumps(build_article_schema(c["seo_title"], c["seo_desc"], canonical, title), ensure_ascii=False, indent=2)
    
    specifics_html = "\n".join(f"<li>{s}</li>" for s in c["local_specifics"])
    
    providers_html = ""
    for name, addr, email, region in c["providers"]:
        providers_html += f"""
      <div class="card">
        <span class="card-icon">🏥</span>
        <h3>{name}</h3>
        <p>📍 {addr}</p>
        <p>📧 <a href="mailto:{email}">{email}</a></p>
        <p style="font-size:0.85rem;color:var(--text-muted);margin-top:8px;">Teeninduspiirkond: {region}</p>
      </div>"""
    
    stats_html = "\n".join(f'<li class="finding-item"><span class="finding-icon">📊</span> {s}</li>' for s in c["inspection_stats"])
    
    faq_html = ""
    for i, (q, a) in enumerate(c["faqs"]):
        faq_html += f"""
      <div class="faq-item" id="faq-{i+1}">
        <button class="faq-q" onclick="toggleFaq(this)" aria-expanded="false">
          {q}
          <span class="faq-arrow">▼</span>
        </button>
        <div class="faq-a" hidden>
          <p>{a}</p>
        </div>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="et">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c["seo_title"]}</title>
  <meta name="description" content="{c["seo_desc"]}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{c["og_title"]}">
  <meta property="og:description" content="{c["seo_desc"]}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="Valvekliinik Töötervishoiuteenused">
  <meta property="og:locale" content="et_EE">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{c["og_title"]}">
  <meta name="twitter:description" content="{c["seo_desc"]}">

  <link rel="stylesheet" href="../style.css">

  <!-- Schema: Article -->
  <script type="application/ld+json">
{article_schema}
  </script>
  <!-- Schema: FAQ -->
  <script type="application/ld+json">
{faq_schema}
  </script>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="../index.html" class="logo">
      <span class="logo-main">Valvekliinik</span>
      <span class="logo-sub">Töötervishoiu portaal</span>
    </a>
    <nav>
      <a href="../index.html">Avaleht</a>
      <a href="../kontrollnimekiri.html">Kontrollnimekiri</a>
      <a href="../kalkulaator.html">Kalkulaator</a>
      <a href="../korduma.html">KKK</a>
      <a href="../enesekontroll.html">Enesekontroll</a>
    </nav>
  </div>
</header>

<div class="page-hero">
  <div class="page-hero-inner">
    <div class="breadcrumb">
      <a href="../index.html">Avaleht</a> › <a href="../index.html#linnad">Piirkonnad</a> › {title}
    </div>
    <h1>{c["icon"]} Töötervishoiu nõuded: {title}</h1>
    <p>Kohalik ülevaade töötervishoiu olukorrast ja teenustest {title}s ning {c["region"]}s.</p>
  </div>
</div>

<main>

  <!-- Piirkondlik ülevaade -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">📍 {title} piirkondlik ülevaade</h2>
      <p class="section-sub">{c["description"]}</p>
      <ul class="risk-list" style="margin-top:16px;">
        {specifics_html}
      </ul>
    </div>
  </section>

  <!-- Teenuspakkujad -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🏥 Töötervishoiu teenuse osutajad {title}s</h2>
      <p class="section-sub">Seadus kohustab sõlmima lepingu töötervishoiu teenuse osutajaga. Allpool on piirkondlikud võimalused.</p>
      <div class="cards cards-3" style="margin-top:24px;">
        {providers_html}
      </div>
      <div class="info-box" style="margin-top:24px;">
        <strong>Kas teenuse osutaja peab olema kohaliku?</strong> Ei. Töötervishoiu teenuse osutaja ei pea asuma samas linnas. Leping võib olla suvalise Eestis registreeritud ja tegevusluba omava teenuse osutajaga.
      </div>
    </div>
  </section>

  <!-- Tööinspektsiooni statistika -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">📊 Tööinspektsiooni statistika: {c["region"]}</h2>
      <p class="section-sub">Piirkondlikud andmed tööohutuse järelevalve kohta.</p>
      <ul class="findings-list">
        {stats_html}
      </ul>
      <div class="info-box" style="margin-top:24px; border-left-color:var(--warning);">
        <strong>Tähelepanek:</strong> Tööinspektsiooni ametlik statistika avaldatakse ti.ee lehel. Ülaltoodud andmed on üldised hinnangud piirkondliku järelevalve intensiivsuse kohta. Täpsed numbrid leiate ti.ee aastaraamatutest.
      </div>
    </div>
  </section>

  <!-- Kohalikud nõuded -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">📋 Töötervishoiu põhikohustused — kehtivad kõikjal Eestis</h2>
      <p class="section-sub">Töötervishoiu nõuded on Eestis ühtlased — piirkondlikke erisusi ei ole. Kõik tööandjad peavad täitma järgmised põhinõuded.</p>
      <div class="cards cards-2" style="margin-top:24px;">
        <div class="card">
          <span class="card-icon">📄</span>
          <h3>Riskianalüüs</h3>
          <p>Kohustuslik kõigile tööandjatele. Peab olema kirjalik ja uuendatud vähemalt iga 3 aasta järel.</p>
        </div>
        <div class="card">
          <span class="card-icon">🤝</span>
          <h3>Töötervishoiu teenuse leping</h3>
          <p>Kohustuslik kõigile tööandjatele, kellel on vähemalt üks töötaja. Teenuse osutaja peab olema teavitanud Terviseametit.</p>
        </div>
        <div class="card">
          <span class="card-icon">🩺</span>
          <h3>Tervisekontrollid</h3>
          <p>Ohtlikus töökeskkonnas töötavatele töötajatele on tervisekontroll kohustuslik. Enne tööle asumist ja regulaarse intervalliga.</p>
        </div>
        <div class="card">
          <span class="card-icon">📚</span>
          <h3>Töötajate teavitamine</h3>
          <p>Töötajaid tuleb kirjalikult teavitada kõigist terviseriskidest ja ohutusreeglitest. Teavitamine peab olema dokumenteeritud.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- KKK -->
  <section class="section" style="background:#fff;">
    <div class="container">
      <h2 class="section-title">❓ Korduma kippuvad küsimused</h2>
      <p class="section-sub">{title} piirkonna tööandjate kõige sagedamini esitatud küsimused.</p>
      <div class="faq-list">
        {faq_html}
      </div>
    </div>
  </section>

  <!-- CTA -->
  <section class="section cta-section">
    <div class="container">
      <div class="cta-box">
        <h2>Vajate abi töötervishoiu korraldamisel {title}s?</h2>
        <p>Valvekliinik pakub töötervishoiu täisteenust üle kogu Eesti. Tegeleme kõigega — riskianalüüsist kuni tervisekontrollide koordineerimiseni. Alates <strong>€10 töötaja kohta kuus</strong>.</p>
        <div class="cta-actions">
          <a href="../enesekontroll.html" class="btn btn-gold">Tehke enesekontroll →</a>
          <a href="mailto:tootervishoid@valvekliinik.ee" class="btn btn-outline">✉️ tootervishoid@valvekliinik.ee</a>
        </div>
        <p class="cta-disclaimer">Tasuta esmakonsultatsioon. Ilma müügikõneta.</p>
      </div>
    </div>
  </section>

</main>

<footer class="footer">
  <div class="container">
    <div class="footer-inner">
      <div>
        <div class="footer-brand">Valvekliinik Töötervishoiuteenused</div>
        <p style="color:var(--grey);font-size:0.85rem;">Vabaduse väljak 8, Tallinn · tootervishoid@valvekliinik.ee</p>
      </div>
      <div>
        <p style="color:var(--grey);font-size:0.85rem;max-width:400px;">See portaal annab üldist teavet töötervishoiu kohta. See ei asenda juriidilist nõustamist ega töötervishoiu teenust.</p>
      </div>
    </div>
  </div>
</footer>

<script>
function toggleFaq(btn) {{
  const answer = btn.nextElementSibling;
  const expanded = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', !expanded);
  answer.hidden = expanded;
  btn.querySelector('.faq-arrow').textContent = expanded ? '▼' : '▲';
}}
</script>

</body>
</html>"""


# ─── EXTRA CSS (appended to style.css or inline) ─────────────────────────────
EXTRA_CSS = """
/* === Sector/City page extras === */
.risk-list { list-style: none; padding: 0; display: grid; gap: 10px; }
.risk-list li { background: #fff; border-left: 3px solid var(--gold); padding: 12px 16px; border-radius: var(--radius); font-size: 0.95rem; }

.data-table { width: 100%; border-collapse: collapse; background: #fff; border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
.data-table th { background: var(--teal); color: var(--white); padding: 12px 16px; text-align: left; font-size: 0.9rem; }
.data-table td { padding: 12px 16px; border-bottom: 1px solid var(--grey-light); font-size: 0.9rem; vertical-align: top; }
.data-table tr:last-child td { border-bottom: none; }
.data-table tr:hover td { background: var(--grey-light); }

.findings-list { list-style: none; padding: 0; display: grid; gap: 10px; }
.finding-item { display: flex; align-items: flex-start; gap: 10px; background: #fff; padding: 14px 16px; border-radius: var(--radius); border-left: 3px solid var(--danger); }
.finding-icon { flex-shrink: 0; }

.checklist-container { display: grid; gap: 10px; }
.checklist-item { display: flex; align-items: flex-start; gap: 12px; background: #fff; padding: 14px 16px; border-radius: var(--radius); border: 1px solid var(--grey-light); cursor: pointer; transition: background 0.2s; }
.checklist-item:hover { background: var(--grey-light); }
.checklist-item input[type=checkbox] { width: 18px; height: 18px; flex-shrink: 0; margin-top: 2px; accent-color: var(--teal); }

.info-box { background: rgba(197,165,90,0.08); border-left: 4px solid var(--gold); padding: 16px 20px; border-radius: 0 var(--radius) var(--radius) 0; font-size: 0.9rem; }

.faq-list { display: grid; gap: 8px; }
.faq-item { border: 1px solid var(--grey-light); border-radius: var(--radius); overflow: hidden; }
.faq-q { width: 100%; text-align: left; background: #fff; padding: 16px 20px; border: none; cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-weight: 600; font-size: 0.95rem; color: var(--teal); transition: background 0.2s; }
.faq-q:hover { background: var(--grey-light); }
.faq-arrow { font-size: 0.75rem; color: var(--gold); flex-shrink: 0; margin-left: 12px; }
.faq-a { padding: 0 20px 16px; background: #fff; }
.faq-a p { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; margin: 0; padding-top: 8px; border-top: 1px solid var(--grey-light); }

.cta-section { background: linear-gradient(135deg, var(--teal) 0%, var(--teal-light) 100%); }
.cta-box { text-align: center; color: var(--white); max-width: 680px; margin: 0 auto; }
.cta-box h2 { font-size: clamp(1.3rem,3vw,1.8rem); font-weight: 800; margin-bottom: 14px; }
.cta-box p { color: rgba(242,245,245,0.85); margin-bottom: 24px; font-size: 1rem; }
.cta-actions { display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-bottom: 14px; }
.cta-disclaimer { font-size: 0.8rem; color: rgba(242,245,245,0.6); }
.btn-outline { background: transparent; color: var(--white); border: 2px solid rgba(242,245,245,0.4); }
.btn-outline:hover { background: rgba(242,245,245,0.1); }

.footer { background: var(--teal); padding: 36px 24px; }
.footer-inner { max-width: 1100px; margin: 0 auto; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 24px; }
.footer-brand { color: var(--white); font-weight: 700; font-size: 1.1rem; margin-bottom: 6px; }
"""

# ─── SITEMAP ENTRIES ──────────────────────────────────────────────────────────

def generate_sitemap_entries():
    entries = []
    for slug in SECTORS:
        entries.append(f"  <url>\n    <loc>{BASE_URL}/sektorid/{slug}.html</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>")
    for slug in CITIES:
        entries.append(f"  <url>\n    <loc>{BASE_URL}/linnad/{slug}.html</loc>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>")
    return "\n".join(entries)

# ─── MAIN ─────────────────────────────────────────────────────────────────────

OUT_DIR = "/Users/lasagnelatte/.openclaw/workspace/tth-portaal"

def main():
    sector_dir = os.path.join(OUT_DIR, "sektorid")
    city_dir = os.path.join(OUT_DIR, "linnad")
    os.makedirs(sector_dir, exist_ok=True)
    os.makedirs(city_dir, exist_ok=True)

    count_sectors = 0
    for slug, data in SECTORS.items():
        html = generate_sector_page(data)
        path = os.path.join(sector_dir, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count_sectors += 1
        print(f"✅ Sektor: {slug}.html")

    count_cities = 0
    for slug, data in CITIES.items():
        html = generate_city_page(data)
        path = os.path.join(city_dir, f"{slug}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count_cities += 1
        print(f"✅ Linn: {slug}.html")

    # Append extra CSS to style.css if not already there
    css_path = os.path.join(OUT_DIR, "style.css")
    with open(css_path, "r", encoding="utf-8") as f:
        existing_css = f.read()
    if "=== Sector/City page extras ===" not in existing_css:
        with open(css_path, "a", encoding="utf-8") as f:
            f.write("\n\n" + EXTRA_CSS)
        print("✅ Extra CSS appended to style.css")
    else:
        print("ℹ️ Extra CSS already in style.css")

    # Generate sitemap additions
    sitemap_entries = generate_sitemap_entries()
    sitemap_path = os.path.join(OUT_DIR, "sitemap-seo-pages.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}
</urlset>
""")
    print("✅ Sitemap generated: sitemap-seo-pages.xml")

    print(f"\n🎉 Done! Generated {count_sectors} sector pages + {count_cities} city pages.")

if __name__ == "__main__":
    main()
