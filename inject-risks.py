#!/usr/bin/env python3
"""Inject ohutegurid sections into all sector pages."""

import os

BASE = "/Users/lasagnelatte/.openclaw/workspace/tth-portaal/sektorid"

SECTIONS = {
    "it.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">IT- ja telekommunikatsioonisektoris esinevad ohutegurid, mis tuleb kajastada toeosutaja riskianalüusis ja mille alusel korraldatakse kohustuslikud tervisekontrollid.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Kuvaritöö</strong> - Pikaajaline kuvari vaatamine koormab silmi ning pohjustab kuivust, peavalu ja nagelamishaireid.</li>
        <li><strong>Sundasend (istuv tooasend)</strong> - Pikaajaline istumine ilma pausideta koormab luuesluukonkamust ja pohustab seljavalu ning vereringehaireid.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Korgete tahtaegade, pideva kaeritatavuse ja toostressi tottu suureneb labipolemise ja vaimse ulekoormuse risk.</li>
        <li><strong>Ebapiisav valgustus</strong> - Halb valgustus tookohal votendab silmaraet ning votendab uusimate normide tarvis 500 luksi kunstlikku valgust.</li>
        <li><strong>Korduvad liigutused</strong> - Hiire ja klaviatuuri korduv kasutamine pohjustab randme- ja kaevalu (n-o tunnelsindroon).</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Silmade kontroll (visomeetria)</strong> - Kohustuslik enne kuvaritoo algust ja iga kolme aasta jarelt; vajaduse korral kompenseerib tooandja kuvariprilid.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Lihas-skeleti seisundi hindamine tootervishoid arsti juures valtimaks toooiguseid ja kroonilist valu.</li>
        <li><strong>Psuhhosotsiaalne hindamine</strong> - Korge psuhholise koormusega toetajatele soovitatav vaimse tervise hindamine tootervishoid arsti juures.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "kaubandus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Kaubandus- ja teenindussektoris esinevad spetsiifilised ohutegurid, mis tulenevad eelkoige seisva too iseloomust ja kliendikontaktist.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Seisev tooasend</strong> - Pikaajaline seismine kahjustab jalgu, selga ja vereringet, suurendades laskumisveenide ja liigese kulumise riski.</li>
        <li><strong>Raskuste teisaldamine</strong> - Kastide, kaubaaluste ja inventari tostmine pohustab seljavigastusi, eriti vale tehnikaga korduval tostmisel.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Agressiivsed kliendid, koored tootingimused (n-o jaepood, tankla) ja pikad vahetused suurendavad toostressi.</li>
        <li><strong>Monotoonne too</strong> - Kassatoo ja ladustamise korduvad liigutused pohustavad lihas-skeleti ulekoormust.</li>
        <li><strong>Libedus ja kukkumisoht</strong> - Pood- ja laokulaatsused on sagedased libeduse ning ebakorrapase porandapinna tottu.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Luu-lihaskonna hindamine</strong> - Hinnatakse selja, jalgade ja uelakeha lihas-skeleti seisundit, eriti raskuste tostmise ja seisva too puhul.</li>
        <li><strong>Vaimse tervise hindamine</strong> - Psuhhosotsiaalsete riskide olemasol hindab tootervishoid arst toostressi ja labipolemise taset.</li>
        <li><strong>Uldine terviseseisundi hindamine</strong> - Toetajatele, kes tegelevad regulaarse raskuste teisaldamisega, on soovitatav kardioulaskumisssteemi ja labasuse hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "tootmine.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Tootmissektoris esineb mitmekesiseid ohutegureid, mis nouavad susteemset riskihindamist ja regulaarseid kohustuslikke tervisekontrolle.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Mura</strong> - Tootmisseadmete summast (ylekoige 85 dB) pohjustab pikaajalisel kokkupuutel pordmatut kuulmikahjustust.</li>
        <li><strong>Vibratsioon</strong> - Koekasade ja vibratsioonistavate too vahendite kasutamine pohjustab kasivibratsioon-sndroomi ja luulihaskonna kahjustusi.</li>
        <li><strong>Kemikaalid ja tolm</strong> - Kokkupuude ohtlike ainete, lahustite ja tootmistolmuga kahjustab hingamisteid ja nahat.</li>
        <li><strong>Raskuste teisaldamine</strong> - Korduvad tostmised ja nihutamised pohjustavad seljavigastusi ning liigesekulo.</li>
        <li><strong>Sundasend</strong> - Pikaajalisel korduvate liigutustega monotoonne tooasend pohustab lihas-skeleti ulekoormust.</li>
        <li><strong>Mehaanilised ohud</strong> - Liikuvad masinaosad, teravad pinnad ja vajutusriskid nouavad ohutusvahendite kasutamist.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Kohustuslik murakokkupuute korral (ylekoige 80 dB); hinnatakse kuulmist enne tootaole asumist ja iga 2 aasta jarelt.</li>
        <li><strong>Spiromeetria (kopsufunktsioon)</strong> - Kemikaali- ja tolmukokkkupuutega tootajatele kohustuslik hingamisteede funktsiooni hindamiseks.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Hinnatakse selga, kaela, uelakehad ja jalgu raskuste tostmise ning vibratsioonikohkupuute seisukohalt.</li>
        <li><strong>Nahauurimine</strong> - Kemikaalide ja ohtlike ainetega kokkupuutuvatel tootajatel kontrollitakse naha seisundit.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "laondus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Laonduse ja logistika valdkonnas on peamisteks ohuteguriteks raskuste kasitlemine, elektritollade kasutamine ning monotoonne tooiseloom.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Raskuste teisaldamine</strong> - Kaupade, kaubaaluste ja pakendite regulaarne tostmine ja liigutamine on peamine seljavigastuste pohjustaja laos.</li>
        <li><strong>Mura</strong> - Elektritollade, konveierite ja laoseadmete heli ulatatab sageli piirnorme, kahjustades pikaajaliselt kuulmist.</li>
        <li><strong>Vibratsioon</strong> - Elektritollaga, traktori voi kahveltoltlaga soitmine ulastab vibratsioonist pohjustatud seljamuutuste riski.</li>
        <li><strong>Sundasend ja korduv liikumine</strong> - Monotoonne pakendamine, sortimine ja skanneerimine koormab lihas-skeleti susteemi.</li>
        <li><strong>Kukkumis- ja porutumisohud</strong> - Korgelt riiulitelt kukkuvad kaubad ning libedad porandad on sagedased vigastuseriskid.</li>
        <li><strong>Kemikaalid</strong> - Osades ladudes kasutatavad puhastusained ja saasteained pohjustavad naha ning hingamisteede irritatsiooni.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Luu-lihaskonna hindamine</strong> - Selga, kaela ja uelakeha hindamine raskuste teisaldamise ning sundasendi tootajatele.</li>
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Murakokkupuutega (ylekoige 80 dB) laotootajatele kohustuslik iga kahe aasta jarelt.</li>
        <li><strong>Nahauurimine</strong> - Kemikaalidega kokkupuutuvatel tootajatel kontrollitakse naha seisundit regulaarselt.</li>
        <li><strong>Spiromeetria</strong> - Tolmu- ja keemiakokkkupuute korral hingamisteede funktsiooni hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "ehitus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Ehitussektor on uks koige ohtlikumaid valdkondi - tootajad puutuvad iga paev kokku mitmete kehaliste ja keskkonnast tulenevate riskidega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Mura</strong> - Perforaatorid, saed, kompressorid ja muud ehitusmasinad tekitavad pidevalt kuulmist kahjustavat mura (ylekoige 85 dB).</li>
        <li><strong>Vibratsioon</strong> - Kae- ja kehavibratsiooni allikad (perforaatorid, tihendusmasinad) pohustuvad vereringehaireid ja luu-lihaskonna kahjustusi.</li>
        <li><strong>Tolm (sh asbestolm)</strong> - Ehitustolm, betooni- ja puutolm ning vanades hoonetes leiduv asbest kahjustavad toosusel hingamisteid ja pohustuvad vaktsiini.</li>
        <li><strong>Korgustoo</strong> - Tellingute, katuste ja korgete platvormide peal tootamine kujutab toosusel kukkumisohtu.</li>
        <li><strong>Raskused ja sundasend</strong> - Materjali, kirjastamine ja tostmine ehitusplatsil koormab selga ja ligeseid intensiivselt.</li>
        <li><strong>Ilmastikunahkused</strong> - Kokkupuude aarmuslike temperatuuride, vihma ja tuulega suurendab terviseriski, sealhulgas mardumist ja kuumarabandust.</li>
        <li><strong>Kemikaalid</strong> - Epoksüübid, lahustid, betoonisegud ja varvid pohjustavad naha ning hingamisteede irritatsiooni.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Kohustuslik enne murakokkupuutega too algust ja iga kahe aasta jarelt korgendatud muraekspositsioonil.</li>
        <li><strong>Hingamisteede uuring (spiromeetria)</strong> - Tolmu- ja keemiakokkkupuutega tootajatele kopsu- ja hingamisteede funktsiooni hindamine.</li>
        <li><strong>Nagemise kontroll</strong> - Ohutuskriitilistel toodel (korgustoo, kranide juhtimine) on nagemine hinnatav.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Selga, kaela ja koiki jäsemeid kontrollitakse seoses raskuste kandmise ja vibratsioonikokkupuutega.</li>
        <li><strong>Uldine terviseseisundi hindamine</strong> - Korgustool ja masinajuhtimisel on vajalik sydame-vereringesusteemi seisundi hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "transport.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Transpordi ja logistika valdkonnas on kriitilised ohutegurid, mis mojutavad nii juhti ennast kui ka liiklusohutust tervikuna.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Ootoo ja vaakestoo</strong> - Oo- ja vaakestoo rikub une-arktme tsuklit, suurendades unepuuduse, soitumisvea ja terviseprobleemide riski.</li>
        <li><strong>Vibratsioon</strong> - Pikaajaline vibratsioon auto-, raskeveoki- voi rongi soidul kahjustab selgroogu ja perifeerset vereringet.</li>
        <li><strong>Sundasend (istuv tooasend)</strong> - Pikaajaline istumine soitmisel pohustab nimmeseljavalu, laskumisveene ja ainevahetushaireid.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Ajasurvest, liiklusest ja vastututsekohustest tulenev stress suurendab sydame-veresoonkonna riski.</li>
        <li><strong>Monotoonus ja vaakumishood</strong> - Pikad transiidireisid pohustuvad vaakumishood, mis on ohu allikas liiklusohutusele.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Nagemise kontroll</strong> - Kohustuslik koigile soidukijuhtidele - hinnatakse nagemustersavust, varvinagemist ja nagevalja laiust.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Seljale ja kaelale eriti oluline seoses vibratsiooni ja sundasendiga soidu ajal.</li>
        <li><strong>Unehairete hindamine</strong> - Suurendatud risk obstruktiivseks uneapnoeks ja narkolepsiaks; vajalik une-arktme uurimine ohu korral.</li>
        <li><strong>Sydame-veresoonkonna hindamine</strong> - Oo- ja vaakestoo moju sydamele ning veresoontele tuleb hinnata regulaarselt tootervishoid arsti juures.</li>
        <li><strong>Psuhhosotsiaalne hindamine</strong> - Pikaajalist toostressi kandvatel soidukijuhtidel soovitatav vaimse tervise hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "tervishoid.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Tervishoius tootavad spetsialistid puutuvad iga paev kokku bioloogiliste, keemiliste ja psuhhosotsiaalsete ohuteguritega, millest paljude kaitseks on kehtestatud ranged nouded.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Bioloogilised ohutegurid</strong> - Kokkupuude nakkushaigustega (B- ja C-hepatiit, HIV, tuberkuloos, SARS-CoV-2) on meditsiinitootajate peamine kutseriski allikas.</li>
        <li><strong>Kemikaalid ja desinfektantid</strong> - Pesemine-, steriliseerimis- ja ravimained (sh sytostaatikumid) kahjustavad nahat, hingamisteid ning on voi mutageensed.</li>
        <li><strong>Ootoo ja vaakestoo</strong> - Oo- ja vaakestoo on tervishoiutootajatel levinud ning pohustab unehaireid, sydame-veresoonkonna probleeme ja loomuliku immuunsuse langust.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Emotsionaalne koormus patsiendisurma, kiirabi ja eetiliste dilemmade tottu suurendab labipolemise ja PTSD riski.</li>
        <li><strong>Seisev too ja raskuste teisaldamine</strong> - Patsientide tostmine ja kandmine pohustab seljavigastusi; seisev too pikaajalistes vahetustes koormab jalgu.</li>
        <li><strong>Kiirgus</strong> - Rontgenikiirte, UV-kiirguse ja muude allikate kokkupuude on asjakohane radioloogi ja dermatoloogia tootajatele.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Vaktsinatsioonistaatuse kontroll</strong> - Kohustuslik hepatiit B, tuberkuloosi (Mantoux/IGRA), gripi ja muude nakkuste suhtes vastavalt tervishoiuasutuse poliitikale.</li>
        <li><strong>Nakkushaiguste seireuuringud</strong> - Regulaarsed laboranalusid nakkushaiguste seireks; tootajad, kes on riskiga kokku puutunud, suunatakse kiirele kontrollile.</li>
        <li><strong>Vaimse tervise hindamine</strong> - Labipolemise, PTSD ja ulekoormuse hindamine tootervishoid arsti juures on soovituslik koigile opiabiga tootavatele tervishoiutootajatele.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Patsiendite hooldamise ja teisaldamisega tegelevate tootajate selga ja uelakeha hinnatakse regulaarselt.</li>
        <li><strong>Nahauurimine</strong> - Desinfektantide ja kemikaalidega kokkupuutuvate tootajate naha seisundit kontrollitakse igal tervisekontrollil.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "haridus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Haridussektori tootajad - opetajad, kasvatajad ja tugispetsialistid - puutuvad peamiselt kokku psuhhosotsiaalsete ja opetustegevusest tulenevate ohuteguritega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Klassidistsipliin, vanemate survest ja halduskoormusest tingitud pikaajaline emotsionaalne pinge suurendab labipolemise riski.</li>
        <li><strong>Haalekasutus ja kori ulekoormamine</strong> - Pidev valjusti raakimine kooliklassis voi vorumisaalis pohustab hale kahvu, poletikku ja korinoduleid.</li>
        <li><strong>Seisev tooasend</strong> - Opetajad seisavad suure osa koolipaevist, mis koormab jalgu, selga ja liigeseid.</li>
        <li><strong>Nakkushaiguste kokkupuude</strong> - Tihe kokkupuude lastega suurendab hooajaliste hingamisteede nakkuste ja muude nakkushaiguste riski.</li>
        <li><strong>Mura</strong> - Klassides ja spordihallis tekib sageli korgendatud murataset, mis koormab kuulmist ja nearalast susteemi.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Vaimse tervise hindamine</strong> - Psuhhosotsiaalsete riskide hindamine labipolemise ja toostressi suhtes; soovitatav igal tootervishoiduarstlikul kontrollil.</li>
        <li><strong>Kori ja hale hindamine</strong> - Opetajatel, kes kasutavad haalt intensiivselt, soovitatav regulaarne logopeediline voi otolaryngoloogiline konsultatsioon.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Seisva tooasendi tottu kontrollitakse selga, jalgu ja jalavoute seisundit.</li>
        <li><strong>Nakkushaiguste kontroll</strong> - Lastega tootavatele isikutele soovitatav ajakohane vaktsinatsioon gripist ja muudest hooajalistest nakkustest.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "hotellindus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Hotellinduse, toitlustuse ja majutuse valdkonna tootajad puutuvad kokku mitmete kehaliste ja keskkonnast tulenevate ohuteguritega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Seisev tooasend</strong> - Kokkade, administraatorite ja koristajate pikaajaline seismine pohustab jala- ja seljaprobleeme ning laskumisveene.</li>
        <li><strong>Kuumus ja kuumad pinnad</strong> - Kokkade kokkupuude avonoolde tulega, aurudega ja kuumade pindadega kujutab poletis- ja kuumakahjustuse ohtu.</li>
        <li><strong>Kemikaalid</strong> - Puhastus- ja desinfektsioonivahendid, kooritusained ning kokkide kasutavad additivid voivad kahjustada nahat ja hingamisteid.</li>
        <li><strong>Ootoo ja vaakestoo</strong> - Hotellinduses levinud oo- ja vaakestoo rikub biorütmi ning suurendab vaimse ja fuuskalise tervise riske.</li>
        <li><strong>Libedus ja kukkumisoht</strong> - Kokkade ja koristajate tookeskkonnas on porandad sageli miskad, suurendades kukkumise riski.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Klienditeeninduse kiire tempe, vaakestoo ja hooajalisus pohustuvad toostressi ja labipolemist.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Nahauurimine</strong> - Toidu- ja puhastusvahendite tottu on nahahaigused (kontakteekseeem) levinud; nahka kontrollitakse igal tootervishoidukontrollil.</li>
        <li><strong>Hingamisteede uuring</strong> - Kemikaalidest ja kuumasest tooruumist tulenevad hingamisteede riskid nouavad spiromeetriat riskitootajatele.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Seisva tooasendi ja korduva liikumise tottu kontrollitakse selga, jalgu ja uelakeha.</li>
        <li><strong>Toiduohutuse tervisekontroll</strong> - Toidukaistsemisega tegelevad tootajad peavad olema vabad nakkushaigustest (koolera, salmonelloos jmt); vajalik tootervishoiduarsti kinnitus.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "pollumajandus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Poollumajanduse valdkonnas esineb laiai spektrit bioloogilisi, keemilisi ja fuusikalisi ohutegureid, mis nouavad eraldi riskihindamist.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Bioloogilised ohutegurid</strong> - Kokkupuude loomadega pohustab zoonooside (leptospiroos, Q-palavik, brutselloos) ja allergeenide riski.</li>
        <li><strong>Kemikaalid (pestitsiidid ja varvained)</strong> - Taimekaitsevahendite, vaetiste ja desinfektantide kasutamine kujutab toksilist ja kantserogeenset ohtu nahale ja hingamisteedele.</li>
        <li><strong>Mura</strong> - Traktorid, kombainid ja muud pollumajandusmasinad tekitavad pikaajaliselt kuulmist kahjustavat mura.</li>
        <li><strong>Vibratsioon</strong> - Traktorite ja masinate keha- ja kaevibratsioon pohustab seljakaeprobleeme ning veringsuhaireid.</li>
        <li><strong>Sundasend ja rasked tooo</strong> - Kunnistamine, aiahooldus ja istutamine pohustab seljavigastusi ning liigesekulo.</li>
        <li><strong>Tolm ja vegetatsioon</strong> - Teravilja-, hahna- ja muude taimede tolm kujutab allergeenset ning kroonilist hingamisteede kahustuse riski.</li>
        <li><strong>UV-kiirgus</strong> - Valitingimuste tootajatel on naha- ja silmakahustuse suurenenud risk pikaajalise paikesekiirguse tottu.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Nahauurimine</strong> - Pestitsiidide, kemikaalide ja UV-kiirguse kokkupuutega tootajatel kontrollitakse nahasseisundit regulaarselt.</li>
        <li><strong>Hingamisteede uuring (spiromeetria)</strong> - Tolmu, allergeenide ja kemikaalidega kokkupuutuvatel tootajatel kontrollitakse kopsufunktsiooni.</li>
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Masinatega tootavatele pollumajandajatele kohustuslik seoses korgendatud muraekspositsiooniga.</li>
        <li><strong>Zoonoositestid</strong> - Loomadega tegelevad tootajad peavad labiima nakkushaiguste (sh brutselloos, leptospiroos) seiretestid.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Raskuste kandmine ja vibratsioonikokkkupuude nouavad selgroo ja liigesete regulaarset kontrolli.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "avalik-haldus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Avalikus halduses ja riigiasutustes on ohutegurid sarnased kontorisektoriga, kuid lisanduvad ka kohalike eriperade ning kodanikuteeninduse spetsiifilised riskid.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Kuvaritoo</strong> - Pidev arvutikasutus pohjustab silmade ulevaesimist, peavalu ja nägemishaireid tootajatel, kes veetavad tookeskkonna enama osa arvuti ees.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Haldusotsuste koormus, elanikkonnapingega töö ja bürokraatlikud tähtajad pohustuvad kroonilist stressi ja labipolemist.</li>
        <li><strong>Sundasend (istuv tooasend)</strong> - Kontoritootajatele iseloomulik pikaajaline istumine pohustab seljavalu, vereringehaireid ja ainevahetushäireid.</li>
        <li><strong>Klienditeeninduse riskid</strong> - Kodanikuteeninduses puutuvad tootajad kokku agressiivsete klientidega, millest tuleneb vaimne pinge ja valiolukorras ka füüsiline oht.</li>
        <li><strong>Halb ergonoomika</strong> - Vanamoodne kontorimoobel ja vale kuvariasetus pohustab kaela-, ola- ja kaeprobleeme.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Silmade kontroll (visomeetria)</strong> - Kohustuslik kuvaritoo esinemisel - enne algust ja iga kolme aasta jarelt; vajaduse korral hüvitatakse kuvariprill id.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Istuva tooasendiga tootajatele selgroo ja uelakeha seisundi hindamine.</li>
        <li><strong>Psuhhosotsiaalne hindamine</strong> - Kodanikuteeninduse ja suure halldusliku vastutusega tootajatele soovitatav vaimse tervise hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "energeetika.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Energeetika on koige ohtlikumaid valdkondi - elektri-, gaasi- ja soojusenergiatootjate tootajatel on suur risk tooostusvigastusteks ja kutsehaigusteks.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Elektriohtus</strong> - Kokkupuude korgepingeseadmete ja elektriseadmetega kujutab suuremat riski elektriloobi ja elektripoletuste nahu.</li>
        <li><strong>Korgustoo</strong> - Elektriliinide, tornide ja seadmete hooldamine korgel asuvatel platvormidel kujutab kukkumisohtu.</li>
        <li><strong>Mura</strong> - Generaatorid, turbiinid ja mehaanilised seadmed tekitavad piirnorme ületavat mura, mis kahjustab kuulmist.</li>
        <li><strong>Kemikaalid</strong> - Kaablite isolatsioonimaterjalid, akuhapped, katla-keemia ja muud ained pohjustavad naha- ja hingamisteede kahjustusi.</li>
        <li><strong>Kuumus ja tuli</strong> - Katlaruumides, koostootmisjaamades ja gaasitootmisel on korgendatud temperatuur ja sujepoleoluoht.</li>
        <li><strong>Rasked seadmed ja raskused</strong> - Seadmete hooldus ja paigaldamine nouavad raskuste teisaldamist ning kujutab luu-lihaskonna ulekoormuse riski.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Nagemise kontroll</strong> - Elektritehniliste toode teostamiseks ja korgustool on tark nagemistersavus hindamine kohustuslik.</li>
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Murakokkupuutega tootajatele kohustuslik iga kahe aasta jarelt.</li>
        <li><strong>Hingamisteede uuring</strong> - Keemiakokkupuutega tootajatele spiromeetria hingamisteede funktsiooni hindamiseks.</li>
        <li><strong>Sydame-veresoonkonna hindamine</strong> - Elektriohtus- ja korgustootegijatele nouatavate eriukse tervisenouded sdame-veresoonkonna seisundile.</li>
        <li><strong>Uldine terviseseisundi hindamine</strong> - Korgendatud ohuteguritega tootajatele soovitatav iga-aastane terviseseisundi hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "finantsteenused.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Finants- ja pangandusteenuste valdkonnas on peamised ohutegurid seotud kuvaritoo, psuhhosotsiaalsete koormuste ja kontoritingimustega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Kuvaritoo</strong> - Pidev arvutikasutus ja arvukate ekraanide vaatamine pohustab silmade ulevaesimist, nägemishaireid ja peavalu.</li>
        <li><strong>Psuhhosotsiaalsed ohutegurid</strong> - Turutahtajad, kliendisurve, vastavusnouded ja vastutuskoormused pohustuvad kroonilist stressi, labipolemist ning kardiovaskulaarse riski suurenemist.</li>
        <li><strong>Sundasend (istuv tooasend)</strong> - Pikaajaline istumine korrusteta tookeskkonnas koos vähese liikumisega suurendab luu-lihaskonna probleemide riski.</li>
        <li><strong>Korduvate liigutuste ohud</strong> - Klaviatuuri ja hiire intensiivne kasutamine pohustab randme- ja kaeprobleeme, sealhulgas karpaalkanali sndroomi.</li>
        <li><strong>Halb ergonoomika</strong> - Mitme kuvari seadistuse ebaloogiline ergonoomika pohustab kaela-, ola- ja seljavalusid.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Silmade kontroll (visomeetria)</strong> - Kohustuslik kuvaritoo esinemisel enne algust ja iga kolme aasta jarelt; vajaduse korral kompenseerib tooandja kuvariprill id.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Istuva tooasendiga tootajatele selgroo, kaela ja uelakeha seisundi hindamine.</li>
        <li><strong>Psuhhosotsiaalne hindamine</strong> - Suure vastutuse ja ajasurvega tootajatele soovitatav vaimse tervise ja stressitaseme hindamine.</li>
        <li><strong>Sydame-veresoonkonna seire</strong> - Kroonilise stressi korral soovitatav vererohutaseme ja kardiovaskulaarsete riskifaktorite hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "puhastusteenused.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Puhastusteenuste valdkonnas puutuvad tootajad iga vahetuse jooksul kokku mitmete keemiliste, bioloogiliste ja fuusikaliste ohuteguritega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Kemikaalid ja puhastusained</strong> - Happe-aluse pohised koristusained, desinf eksioonivahendid ja lahustid pohjustavad nahahaigusi (kontakteekseeem) ning hingamisteede irritatsiooni.</li>
        <li><strong>Bioloogilised ohutegurid</strong> - Tervishoiu- ja avalikes hoonetes puhastavad tootajad puutuvad kokku potentsiaalselt nakkuslike materjalidega.</li>
        <li><strong>Raskuste teisaldamine</strong> - Koristusseadmete, tolmuimejate ja materjalide kandmine pohustab seljavigastusi.</li>
        <li><strong>Seisev too ja korduvad liigutused</strong> - Pikaajaline seismine ja korduvad puhastusliigutused pohustuvad jalgu, selga ja uelakeha.</li>
        <li><strong>Libedus ja kukkumisoht</strong> - Miskad porandad peale koristamist kujutavad korgendatud kukkumisriski.</li>
        <li><strong>Haledad tookeskkonnatingimused</strong> - Koristamine talvistes tootingimistes, korgetes hoonetes voi puhastusseadmetega kujutab lisariske.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Nahauurimine</strong> - Keemiliste puhastusvahenditega kokkupuutuvate tootajate naha seisundi regulaarne kontroll kontaktekseemi varajaseks avastamiseks.</li>
        <li><strong>Hingamisteede uuring</strong> - Keemiliste aurude ja tolmuga kokkupuutuvatel tootajatel kontrollitakse hingamisteede funktsiooni.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Raskuste teisaldamise ja korduva liikumisega tootajatele selgroo ja uelakeha regulaarne hindamine.</li>
        <li><strong>Nakkushaiguste seire</strong> - Tervishoiuasutustes puhastavatel tootajatel on soovitatav nakkushaiguste seireuuring ja ajakohane vaktsina tsioon.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",

    "toiduaineteostus.html": """
  <!-- Ohutegurid ja tervisekontrollid -->
  <section class="section" style="background:var(--grey-light);">
    <div class="container">
      <h2 class="section-title">🛡️ Peamised ohutegurid ja tervisekontrolli nõuded</h2>
      <p class="section-sub">Toiduaineteostuse valdkonnas esineb mitmeid bioloogilisi, keemilisi ja fuusikalisi ohutegureid, millest enamik on seotud tootmistingimuste ja toiduohutuse tagamisega.</p>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Peamised ohutegurid</h3>
      <ul class="risk-list">
        <li><strong>Bioloogilised ohutegurid (toiduohutus)</strong> - Toiduainete tootmisel on risk salmonelloosi, listeerioosi ja muude toiduleviste nakkuste pohjustamiseks, kui hügieeninouded ei ole taytud.</li>
        <li><strong>Kemikaalid (puhastusained ja lisaained)</strong> - Seadmete steriliseerimisel kasutatavad korgkontsentratsiooniga kemikaalid pohustuvad naha ja hingamisteede irritatsiooni.</li>
        <li><strong>Mura</strong> - Tootmisliinide, konveierite ja pakendusseadmete muru ulatatab sageli 85 dB piiri, kahjustades kuulmist.</li>
        <li><strong>Kuumus ja kulmetus</strong> - Kokkade tooruumid on korgenenud temperatuuriga, liha- ja piimalaod aga kuumustavalt madalate temperatuuridega.</li>
        <li><strong>Sundasend ja raskused</strong> - Tootmisliini juures pikaajaline sundasend ning kaupade kandemine pohustab luu-lihaskonna kahjustusi.</li>
        <li><strong>Libedus ja kukkumisoht</strong> - Toiduainetstoodangul on porandad sageli misked vee, rasva ja tootmisjaakide tottu.</li>
      </ul>

      <h3 style="margin-top:24px; margin-bottom:12px; font-size:1.1rem; color:var(--primary);">Kohustuslikud tervisekontrollid</h3>
      <ul class="risk-list">
        <li><strong>Toiduohutuse tervisekontroll (nakkushaiguste uuring)</strong> - Toidu kasitlusega tegelevad tootajad peavad omama tootervishoiduarsti kinnitust nakkusvabaduse kohta (koolera, salmonelloos, noroviirus jmt).</li>
        <li><strong>Nahauurimine</strong> - Kemikaalide ja toitu kasitlevate tootajate naha seisund kontrollitakse kontaktekseemi ja muude nahahaiguste suhtes.</li>
        <li><strong>Hingamisteede uuring (spiromeetria)</strong> - Kemikaali- ja tolmukokkupuutega tootajatele kohustuslik hingamisteede funktsiooni hindamine.</li>
        <li><strong>Kuulmiskontroll (audiomeetria)</strong> - Murakokkupuutega tootmisliini tootajatele kohustuslik iga kahe aasta jarelt.</li>
        <li><strong>Luu-lihaskonna hindamine</strong> - Sundasendi ja raskuste teisaldamisega tootajatele selgroo ja uelakeha regulaarne hindamine.</li>
      </ul>

      <p style="margin-top:20px; color:var(--text-muted); font-size:0.85rem;">Allikas: TTOS (tootervishoiu ja tooohutuse seadus), tooelu.ee</p>
    </div>
  </section>

""",
}

INSERT_BEFORE = "  <!-- CTA -->"

success = 0
errors = []

for filename, section_html in SECTIONS.items():
    filepath = os.path.join(BASE, filename)
    if not os.path.exists(filepath):
        errors.append(f"NOT FOUND: {filepath}")
        continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if INSERT_BEFORE not in content:
        errors.append(f"ANCHOR NOT FOUND in {filepath}")
        continue
    if "Peamised ohutegurid ja tervisekontrolli nõuded" in content:
        errors.append(f"ALREADY INJECTED (skipping): {filename}")
        continue
    new_content = content.replace(INSERT_BEFORE, section_html + INSERT_BEFORE, 1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    success += 1
    print(f"OK: {filename}")

print(f"\nDone: {success} pages updated.")
if errors:
    print("Issues:")
    for e in errors:
        print(f"  - {e}")
