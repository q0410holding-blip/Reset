# Auftrag für den lokalen Agenten: Live-Abnahme und www für abnehmen-mit-arzt.de

**Von:** Claude Thema 1 (Cloud-Session) · **Für:** lokaler Agent auf Stefans Mac · **Stand:** 30.09.2026

## Worum es geht

Am 30.09.2026 gegen 09:00 UTC ist die neue Version von https://abnehmen-mit-arzt.de/ live gegangen: Replit-App „Shot Enhancer“ im Team-Workspace AMITA, Quellstand `9d4b003`. Die Cloud-Session von Thema 1 erreicht die Domain nicht und kann Replit seit dem Workspace-Umzug nicht mehr lesen. Deshalb übernimmst du zwei Dinge:

- **Teil A:** die Nachher-Messung mit demselben Skript wie die Vorher-Messung. Sie ist nur lesend, bitte sofort machen.
- **Teil B:** HTTPS für `www.abnehmen-mit-arzt.de` einrichten, über Replit und die DNS-Einträge bei United Domains.

Linear: RES-341 (Live-Abnahme), RES-340 (www), Übersicht in RES-371. Thema 1 wertet deine Ergebnisse aus und schließt die Tickets.

## Regeln

- Nur lesende Abrufe der Website (GET/HEAD). Keine Formulare, keine Funnel-Eingaben, keine Buchungen, keine Anrufe oder Mails.
- In Replit keinen Code ändern und nichts veröffentlichen, also kein Publish und kein Republish.
- DNS: ausschließlich die Einträge für `www` setzen, die Replit anzeigt. Keine Werte raten. Nicht anfassen: Einträge der Hauptdomain (Apex), MX, SPF, DKIM, DMARC, CAA, Verifizierungs-TXT (z. B. Google) und Nameserver.
- Keine Passwörter anfordern, speichern oder weitergeben. Ist ein Login nötig, meldet Stefan sich selbst an.
- Tickets nicht selbst schließen. Ergebnisse als Kommentar posten.

## Dateien

Diese Dateien liegen im Repo `q0410holding-blip/Reset`, Branch `claude/claude-md-mcp-access-jb93lg`, Ordner `workstreams/01-technik/live-abnahme-2026-09-30/`. Alternativ gibt Stefan sie dir direkt.

| Datei | SHA256 | Zweck |
|---|---|---|
| `live_check.py` | `18d95d0ac8bbbdb9baf4137a55efe5547e82880af49c75a3b8f924632b86772a` | unverändertes Messskript der Vorher-Messung |
| `live-before-result.json` | `161a0ecfe4dd0a59f8b978a73ebe38856d4a006a71696da30defd0386c0d4b95` | Vorher-Messung vom 29.09.2026, 21:12 UTC |
| `compare_live.py` | `094a1593f3ecb3efa2f1ff32ed3666fb6257435a4f49439fcb06f65ac07c17f0` | erzeugt den Vorher/Nachher-Bericht |

## Teil A – Nachher-Messung (sofort)

1. Prüfsummen kontrollieren: `shasum -a 256 live_check.py live-before-result.json compare_live.py`. Weicht ein Wert ab, abbrechen und melden. Die Skripte nicht ändern.
2. Messen:
   ```bash
   python3 live_check.py > live-after-result.json 2> live-after-stderr.txt; echo $? > live-after-exit.txt
   python3 compare_live.py live-before-result.json live-after-result.json > vergleich.md
   ```
3. Browser-Stichprobe, nur ansehen, mit Screenshots:
   - `https://abnehmen-mit-arzt.de/abnehmprogramm-12-monate?utm_source=test#preise` muss auf `/abnehmprogramm-6-monate/` landen, und zwar mit `?utm_source=test` und `#preise`.
   - `https://abnehmen-mit-arzt.de/faq/` zeigt die FAQ-Seite, im Footer steht `+49 30 75435335`.
   - `https://abnehmen-mit-arzt.de/funnel/cross/`: Der Funnel-Start lädt. Nichts eingeben.
   - Eine beliebige Unterseite in schmaler Fensterbreite (Mobilansicht) ansehen.
4. Alle Dateien und Screenshots unter `workstreams/01-technik/evidence/20260930-live-after/` ablegen.
5. **Rückmeldung in Linear RES-341:**
   - den kompletten Inhalt von `vergleich.md`,
   - das Ergebnis der Browser-Stichprobe,
   - den Exitcode aus `live-after-exit.txt`.
6. Wenn du Schreibzugriff auf das Repo hast: `live-after-result.json`, `vergleich.md`, `live-after-stderr.txt` und `live-after-exit.txt` in denselben Branch nach `workstreams/01-technik/live-abnahme-2026-09-30/ergebnisse/` pushen. Sonst `live-after-result.json` an den Linear-Kommentar anhängen.

## Teil B – www einrichten (nach Teil A)

**1. Replit:** Mit Stefans Account (q0410holding@gmail.com) den AMITA Workspace öffnen, dann Shot Enhancer → Publishing → „Connected domain(s)“ → „Add a domain“ und `www.abnehmen-mit-arzt.de` eintragen.
- Bestehende Domains (`abnehmen-mit-arzt.de`, `goresetapp.com`, `resetapp.replit.app`) nicht ändern oder entfernen.
- Fehlt die Berechtigung, hier abbrechen und Stefan melden. Dann muss Philipp als Owner diesen Schritt machen.
- Die angezeigten DNS-Einträge (Typ, Host, Wert) exakt notieren und einen Screenshot machen.

**2. United Domains:** Stefan meldet sich selbst an. Dann die DNS-Verwaltung von `abnehmen-mit-arzt.de` öffnen.
- Erst einen Screenshot der kompletten DNS-Tabelle und der Weiterleitungen machen. Das ist der Rückweg.
- Für `www` gilt derzeit A `89.31.143.90`, das ist die United-Domains-Weiterleitung. Diese Weiterleitung für `www` deaktivieren und genau die Replit-Einträge setzen. Verlangt Replit einen TXT-Eintrag, ihn wie angegeben anlegen.
- Sonst nichts ändern. Danach wieder einen Screenshot machen.

**3. Warten:** Warten, bis Replit `www` als verifiziert anzeigt. Das kann einige Minuten bis Stunden dauern. In der Zwischenzeit nicht mehrfach an DNS herumstellen.

**4. Nachkontrolle:** `python3 live_check.py > live-after-www.json` ausführen und in der Gruppe `host` prüfen: `https://www.abnehmen-mit-arzt.de/abnehmspritze-kosten/?q=1` liefert Status 200 mit Canonical `https://abnehmen-mit-arzt.de/abnehmspritze-kosten/`.

**5. Rückmeldung in Linear RES-340:**
- die gesetzten Einträge (Typ, Host, Wert),
- was vorher für `www` eingetragen war,
- der Ablageort der Screenshots,
- das Ergebnis der Nachkontrolle.

Außerdem `live-after-www.json` in denselben Branch nach `workstreams/01-technik/live-abnahme-2026-09-30/ergebnisse/` pushen. Thema 1 wertet die Rohdaten selbst aus.

**Rückweg bei Problemen:** den vorherigen Zustand für `www` laut Vorher-Screenshot wiederherstellen, also die Weiterleitung auf `https://abnehmen-mit-arzt.de` bzw. A `89.31.143.90`. Danach in RES-340 melden.

## Teil C – Sitemap bei Google einreichen

Nur ausführen, wenn `vergleich.md` aus Teil A „alle Prüfungen bestanden“ meldet.

1. Search Console öffnen, Property `sc-domain:abnehmen-mit-arzt.de`, Konto `admin@getresetapp.co`. Stefan meldet sich selbst an. Unter Sitemaps `https://abnehmen-mit-arzt.de/sitemap.xml` einreichen.
2. Über die URL-Prüfung die Indexierung beantragen, sparsam und nur für: `/`, `/abnehmprogramm-6-monate/`, `/abnehmspritze-berlin/`, `/abnehmspritze-kosten/`, `/abnehmzentrum-berlin/`, `/vergleich/`. Keine Massenanträge.
3. **Rückmeldung in Linear RES-346:**
   - Zeitpunkt der Einreichung,
   - Sitemap-Status laut Search Console (z. B. erkannte URLs),
   - beantragte URLs,
   - Ablageort der Screenshots unter `workstreams/01-technik/evidence/20260930-gsc/`.

Ein Antrag ist keine Indexierung. Als indexiert nur melden, was die Search Console tatsächlich anzeigt.
