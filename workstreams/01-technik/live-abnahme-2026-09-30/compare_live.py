"""Compare two live_check.py results (before, after) and print a Markdown report.

Usage: python3 compare_live.py live-before-result.json live-after-result.json [SITEMAP_URLS] > vergleich.md

SITEMAP_URLS is the expected number of sitemap URLs (default: the 22 public pages).
Since Paket 5/6 (30.09.2026, ~14:00 UTC) the sitemap lists 38 URLs.
"""
import json
import sys

ORIGIN = "https://abnehmen-mit-arzt.de"
SIX_MONTHS = ORIGIN + "/abnehmprogramm-6-monate/"
ALIAS_TARGETS = {
    "/fuer-fachkreise/": ORIGIN + "/fuer-arzte/",
    "/so-funktionierts/": SIX_MONTHS,
}


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def index(data):
    return {(c["group"], c["path"], c.get("method", "GET")): c for c in data["checks"]}


def chain(check):
    hops = check.get("chain") or []
    return " → ".join(str(hop.get("status") or hop.get("error", "ERR")) for hop in hops) or "–"


def directives(check):
    return " ".join(filter(None, [check.get("robots"), check.get("googlebot"), check.get("bingbot")]))


def short_robots(check):
    robots = check.get("robots")
    return ", ".join(part.strip() for part in robots.split(",")[:2]) if robots else "–"


def verdict(ok):
    return "PASS" if ok else "FAIL"


def expectations(check):
    """Return (ok, expectation) for one GET check of the after measurement."""
    group, path, status = check["group"], check["path"], check.get("finalStatus")
    if group == "public":
        ok = (status == 200 and check.get("canonical") == ORIGIN + path
              and (path == "/" or not check.get("identicalToHomepage"))
              and "noindex" not in directives(check))
        return ok, "200, eigenes HTML, Canonical = eigene URL, indexierbar"
    if group == "noSlash":
        ok = status == 200 and check.get("canonical") == ORIGIN + path + "/"
        return ok, "landet auf der Slash-URL mit passendem Canonical"
    if group == "oldOffer":
        ok = status == 200 and SIX_MONTHS in (check.get("metaRefresh") or "")
        return ok, "Weiterleitungsseite auf die 6-Monats-Seite"
    if group == "spa":
        ok = status == 200 and "noindex" in directives(check) and not check.get("canonical")
        return ok, "200, noindex, kein Canonical"
    if group == "alias":
        target = ALIAS_TARGETS.get(path, "")
        ok = status == 200 and bool(target) and target in (check.get("metaRefresh") or "")
        return ok, "Weiterleitungsseite auf " + (target or "?")
    if group == "missing":
        return status == 404, "404"
    return True, ""


def main():
    before, after = load(sys.argv[1]), load(sys.argv[2])
    sitemap_target = int(sys.argv[3]) if len(sys.argv) > 3 else None
    b_idx, a_idx = index(before), index(after)
    b_sum, a_sum = before["summary"], after["summary"]
    lines = [
        "# Live-Abnahme abnehmen-mit-arzt.de: Vorher/Nachher",
        "",
        f"Vorher: {before['utc']} · Nachher: {after['utc']} · gleiches Skript `live_check.py`",
        "",
        "## Kennzahlen (22 öffentliche Seiten, initiales HTML)",
        "",
        "| Kennzahl | Vorher | Nachher | Ziel | Ergebnis |",
        "|---|---|---|---|---|",
    ]
    pub_after = [c for c in after["checks"] if c["group"] == "public" and c.get("method") == "GET"]
    pub_before = [c for c in before["checks"] if c["group"] == "public" and c.get("method") == "GET"]
    total = a_sum["publicTotal"]
    rows = [
        ("Seiten mit Status 200", b_sum["publicOk"], a_sum["publicOk"], total),
        ("Unterseiten = Kopie der Startseite", b_sum["homepageCopies"], a_sum["homepageCopies"], 0),
        ("Falsche Canonicals", b_sum["wrongCanonicals"], a_sum["wrongCanonicals"], 0),
        ("noindex auf öffentlichen Seiten", b_sum["noindexOnPublic"], a_sum["noindexOnPublic"], 0),
        ("Alte Nummer im HTML", b_sum["oldPhonePages"], a_sum["oldPhonePages"], 0),
        ("Neue Nummer im HTML", sum(1 for c in pub_before if c.get("newPhone")),
         sum(1 for c in pub_after if c.get("newPhone")), total),
        ("getresetapp im HTML", b_sum["getresetappPages"], a_sum["getresetappPages"], 0),
        ("12-Monats-Angebot im HTML", b_sum["offer12Pages"], a_sum["offer12Pages"], 0),
        ("50-€-Nachsorge im HTML", b_sum["aftercare50Pages"], a_sum["aftercare50Pages"], 0),
        ("Status unbekannter URLs", b_sum["missingStatus"], a_sum["missingStatus"], [404, 404]),
    ]
    failures = 0
    for label, old, new, target in rows:
        ok = new == target
        failures += not ok
        lines.append(f"| {label} | {old} | {new} | {target} | {verdict(ok)} |")

    lines += ["", "## Einzelprüfungen (Nachher)", "",
              "| Gruppe | Pfad | Kette GET | HEAD | Titel | Canonical | Robots | Erwartung | Ergebnis |",
              "|---|---|---|---|---|---|---|---|---|"]
    for check in after["checks"]:
        if check.get("method") != "GET" or check["group"] in ("file", "host"):
            continue
        head = a_idx.get((check["group"], check["path"], "HEAD"), {})
        ok, expectation = expectations(check)
        head_ok = head.get("finalStatus") == check.get("finalStatus")
        ok = ok and head_ok
        failures += not ok
        title = (check.get("title") or "–").replace("|", "/")
        lines.append(
            f"| {check['group']} | `{check['path']}` | {chain(check)} | {head.get('finalStatus', '–')} | {title} | "
            f"{check.get('canonical') or '–'} | {short_robots(check)} | {expectation} | {verdict(ok)} |")

    lines += ["", "## Dateien", "", "| Datei | Status | Vorher | Nachher | Ergebnis |", "|---|---|---|---|---|"]
    for check in after["checks"]:
        if check["group"] != "file":
            continue
        old = b_idx.get(("file", check["path"], "GET"), {})
        ok = check.get("finalStatus") == 200 and not check.get("isHomepage") and not check.get("mentions12")
        if check["path"].endswith(".xml"):
            ok = ok and check.get("sitemapLocs") == (sitemap_target or total)
        failures += not ok
        describe = lambda c: (f"{c.get('finalStatus')}, Startseite={c.get('isHomepage')}, 12M={c.get('mentions12')}"
                              + (f", URLs={c.get('sitemapLocs')}" if c.get("sitemapLocs") is not None else ""))
        lines.append(f"| `{check['path']}` | {check.get('finalStatus')} | {describe(old) if old else '–'} | "
                     f"{describe(check)} | {verdict(ok)} |")

    lines += ["", "## Hostvarianten (nur Befund, www wird separat eingerichtet)", "",
              "| Variante | Vorher | Nachher | Canonical nachher |", "|---|---|---|---|"]
    for check in after["checks"]:
        if check["group"] != "host":
            continue
        old = b_idx.get(("host", check["path"], "GET"), {})
        lines.append(f"| `{check['path']}` | {chain(old) if old else '–'} | {chain(check)} | "
                     f"{check.get('canonical') or '–'} |")

    lines += ["", f"**Ergebnis: {'alle Prüfungen bestanden' if failures == 0 else f'{failures} Prüfung(en) nicht bestanden'}** "
              "(Hostvarianten nicht mitgezählt)."]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
