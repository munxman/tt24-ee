#!/usr/bin/env python3
"""build_muudatused.py - regenerate the "Mis on muutunud" change-tracker from
changes.json (the single source of truth).

Renders, from one data file:
  - the visible <article> entries in muudatused.html
  - the CollectionPage + ItemList JSON-LD in muudatused.html
  - the top changelog rows in the index.html homepage teaser
  - the review dates on both pages + lastmod in sitemap.xml

Usage:  python build_muudatused.py
        (run from the repo root; reads changes.json next to it)

The page regions are delimited by <!-- CHANGES:*:START/END --> markers; only the
content between markers is replaced, so the rest of each page is untouched.
Idempotent: running twice yields the same output. NEVER hand-edit between the
markers - edit changes.json and re-run.
"""
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "changes.json")
MUUD = os.path.join(ROOT, "muudatused.html")
INDEX = os.path.join(ROOT, "index.html")
SITEMAP = os.path.join(ROOT, "sitemap.xml")
SITE = "https://tt24.ee"

ES_MONTHS = ["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni",
             "juuli", "august", "september", "oktoober", "november", "detsember"]
IMPACT_LABEL = {"low": "Madal mõju", "medium": "Keskmine mõju", "high": "Kõrge mõju"}
IMPACT_TITLE = {
    "low": "Madal mõju: enamasti ei nõua tööandjalt tegevust või on uus võimalus, mitte kohustus.",
    "medium": "Keskmine mõju: tasub oma töötervishoiu korraldus üle vaadata või kohandada.",
    "high": "Kõrge mõju: nõuab tööandjalt kohest tegutsemist või toob kaasa uue kohustuse.",
}
SEP = '\n        <span aria-hidden="true">·</span>\n        '


def human_date(iso):
    y, m, d = iso.split("-")
    return f"{int(d)}. {ES_MONTHS[int(m)]} {int(y)}"


def dmy(iso):
    y, m, d = iso.split("-")
    return f"{d}.{m}.{y}"


def render_meta(e, today):
    if e["status"] == "proposed":
        lead = f'<span class="status-badge">{e["status_label"]}</span>'
    else:
        verb = "Jõustub" if e["effective_date"] > today else "Jõustus"
        imp = e["impact"]
        lead = (f'<time datetime="{e["effective_date"]}">{verb}: {human_date(e["effective_date"])}</time>'
                + SEP
                + f'<span class="impact-badge impact-{imp}" title="{IMPACT_TITLE[imp]}">{IMPACT_LABEL[imp]}</span>')
    parts = [lead,
             f'<span class="audience-tag">{e["audience"]}</span>',
             f'<span>Allikas: {e["meta_source"]}</span>']
    return SEP.join(parts)


def render_body(e):
    out = []
    if e.get("lead"):
        out.append(f'      <p class="lead">{e["lead"]}</p>')
    for b in e.get("body", []):
        t = b["type"]
        if t == "h3":
            out.append(f'      <h3>{b["text"]}</h3>')
        elif t == "p":
            out.append(f'      <p>{b["html"]}</p>')
        elif t in ("ul", "ol"):
            lis = "".join(f"<li>{x}</li>" for x in b["items"])
            out.append(f'      <{t}>{lis}</{t}>')
    if e.get("related"):
        links = " · ".join(f'<a href="{r["href"]}">{r["label"]}</a>' for r in e["related"])
        out.append(f'      <p class="related-links">{e.get("related_label", "Seotud:")} {links}</p>')
    srcs = e["sources"]
    label = "Allikas:" if len(srcs) == 1 else "Allikad:"
    slinks = " · ".join(f"<a href='{s['url']}' target='_blank' rel='noopener'>{s['name']}</a>" for s in srcs)
    out.append(f'      <p class="muudatused-entry-source">{label} {slinks}</p>')
    return "\n".join(out)


def render_entry(e, today):
    return (f'    <article class="muudatused-entry" id="{e["id"]}">\n'
            f'      <div class="muudatused-entry-meta">\n        {render_meta(e, today)}\n      </div>\n'
            f'      <h2>{e["title"]}</h2>\n'
            f'{render_body(e)}\n'
            f'    </article>')


def build_entries(entries, today):
    return "\n\n".join(render_entry(e, today) for e in entries)


def build_schema(entries):
    items = []
    for i, e in enumerate(entries, 1):
        items.append({
            "@type": "ListItem", "position": i,
            "item": {
                "@type": "Article",
                "headline": e["headline_list"],
                "datePublished": e["published_date"],
                "dateModified": e["modified_date"],
                "url": f'{SITE}/muudatused.html#{e["id"]}',
                "author": {"@type": "Organization", "name": "TT24"},
            },
        })
    doc = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Mis on muutunud - Töötervishoiu reeglite ja juhiste muudatused",
        "description": "Värsked muudatused Eesti töötervishoiu seadustes, määrustes ja juhistes.",
        "url": f"{SITE}/muudatused.html",
        "inLanguage": "et",
        "publisher": {"@type": "Organization", "name": "TT24", "url": SITE},
        "mainEntity": {"@type": "ItemList", "itemListElement": items},
    }
    body = json.dumps(doc, ensure_ascii=False, indent=2)
    return '  <script type="application/ld+json">\n' + body + '\n  </script>'


def build_teaser(entries):
    rows = []
    for e in entries:
        t = e.get("teaser")
        if not t:
            continue
        rows.append(
            f'      <a class="catalog-row" href="muudatused.html#{e["id"]}">\n'
            f'        <span class="catalog-num">{t["num"]}</span>\n'
            f'        <div class="catalog-body">\n'
            f'          <h3 class="catalog-h">{t["title"]}</h3>\n'
            f'          <p class="catalog-desc">{t["desc"]}</p>\n'
            f'          <span class="catalog-tag" style="display:inline-block; margin-top:8px; font-family:var(--mono); font-size:11px; letter-spacing:0.04em; color:#0066CC;">{t["audience"]}</span>\n'
            f'        </div>\n'
            f'        <span class="catalog-action">Loe →</span>\n'
            f'      </a>')
    return "\n".join(rows)


def inject(text, tag, content):
    start, end = f"<!-- CHANGES:{tag}:START -->", f"<!-- CHANGES:{tag}:END -->"
    if start not in text or end not in text:
        raise SystemExit(f"Marker {tag} missing in target file - add the START/END markers once.")
    pre = text[:text.index(start) + len(start)]
    post = text[text.index(end):]
    return pre + "\n" + content + "\n  " + post


def main():
    data = json.load(open(DATA, encoding="utf-8"))
    entries = data["entries"]
    today = data["meta"]["last_reviewed"]

    # muudatused.html: entries + schema + review date
    m = open(MUUD, encoding="utf-8").read()
    m = inject(m, "ENTRIES", build_entries(entries, today))
    m = inject(m, "SCHEMA", build_schema(entries))
    m = re.sub(r'(<aside class="tt24-review-footer"[^>]*>\s*<time datetime=")[^"]*(">)[^<]*(</time>)',
               lambda mo: f'{mo.group(1)}{today}{mo.group(2)}Sisu kontrollitud: {human_date(today)}{mo.group(3)}', m)
    open(MUUD, "w", encoding="utf-8").write(m)

    # index.html: teaser + review date
    ix = open(INDEX, encoding="utf-8").read()
    ix = inject(ix, "TEASER", build_teaser(entries))
    ix = re.sub(r'Viimane ülevaatus \d{2}\.\d{2}\.\d{4}', f'Viimane ülevaatus {dmy(today)}', ix)
    open(INDEX, "w", encoding="utf-8").write(ix)

    # sitemap.xml: lastmod for homepage + change-tracker
    sm = open(SITEMAP, encoding="utf-8").read()
    for loc in (f"{SITE}/", f"{SITE}/muudatused.html"):
        sm = re.sub(r'(<loc>' + re.escape(loc) + r'</loc>\s*<lastmod>)[^<]*(</lastmod>)',
                    lambda mo: mo.group(1) + today + mo.group(2), sm)
    open(SITEMAP, "w", encoding="utf-8").write(sm)

    # validate the schema we just wrote
    schema_body = re.search(r'CHANGES:SCHEMA:START -->\s*<script type="application/ld\+json">(.*?)</script>',
                            open(MUUD, encoding="utf-8").read(), re.S).group(1)
    json.loads(schema_body)
    teaser_n = sum(1 for e in entries if e.get("teaser"))
    print(f"OK: {len(entries)} entries rendered, {teaser_n} teaser rows, schema valid, dates -> {today}")


if __name__ == "__main__":
    main()
