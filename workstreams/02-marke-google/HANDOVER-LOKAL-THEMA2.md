# Übergabe an lokalen Agenten – Thema 2 (Marke, Angebot, Google) – offene Punkte

Stand: 30.09.2026, ca. 09:35 UTC. Von: Claude Cloud-Session „GEO: Task 2“. Auftrag von Stefan: „Übergib an nen lokalen Agenten alles was aussteht. Der kann es dann machen.“

Grund der Übergabe: Die Cloud-Sessions haben **keinen Replit-Zugriff mehr** auf Shot-Enhancer (seit dem Umzug in den AMITA-Workspace: „account or organization restriction“). Außerdem blockiert das Cloud-Netz `abnehmen-mit-arzt.de`. Der lokale Agent auf Stefans Mac hat beides: Replit im AMITA-Workspace (MCP oder Browser) und normalen Internetzugang.

Linear-Projekt: **AMITA · KI-Sichtbarkeit & Wachstum**. Parent Thema 2: **RES-326**. Übergabeticket: **RES-372**. Alle Vorlagen liegen im Repo `q0410holding-blip/Reset`, Branch `claude/lucid-lovelace-g54knl`, Ordner `workstreams/02-marke-google/`.

---

## Verbindliche Regeln von Stefan – nicht erneut fragen

- **S18 Grundregel:** „nutze die aktuellen Informationen und baue drauf auf und ändere sie nicht ab!“ Bestehende Texte nicht umformulieren, nur ergänzen oder die ausdrücklich beschlossenen Punkte ändern.
- **S17:** Conversion-Treiber bleiben unverändert: Bewertungen 4,7/478, „Bekannt aus“, Preisvergleiche inkl. Wettbewerberaussagen, 24/7, Support-Antwortzeiten, Erfolgszahlen, Patientenberichte (auch 12-Monats-Berichte), Funnels. **Keinerlei Wording auf der Startseite ändern.** Auch „Einziger deutscher Anbieter“ im Schema bleibt.
- **S19:** Marke „Abnehmen mit Arzt (AMITA)“ in den Titeln der Unterseiten und im Datenblock.
- **Telefon** überall `+49 30 75435335` / `tel:+493075435335` / Schema `+493075435335`. WhatsApp/SMS bleiben auf 0163 5874217 (Stefan). Nummern der Partnerpraxen nicht anfassen.
- Nur noch 6-Monats-Programme: 1.899 € (Wegovy) / 2.399 € (Mounjaro); 24 Monate = Zahlungsdauer. Nach 6 Monaten: „Nach den 6 Monaten erhalten Sie eine individuelle Berechnung für Ihre Folgebehandlung.“
- Kein Link „Praxen & Partnerärzte“ in Navigation/Footer (vorerst).
- **Funnels nie brechen** (Stefan: „denk drüber nach damit wir die funnels nicht ficken“).

## Koordination – ein Writer pro Replit-Projekt

- **Shot-Enhancer** (Hauptwebsite, `replit.com/t/amita/repls/Shot-Enhancer`, replId `8dddf442-7691-4e3c-aea1-f521b9b1c7f8`): Writer-Lock liegt formal bei **Thema 1** (RES-371). Thema 1 kann derzeit nicht schreiben. **Bevor du schreibst:** in RES-371 kommentieren „Writer-Lock: lokaler Agent (Thema 2), Aufgaben A2/A3“, danach wieder freigeben. Thema 3 wartet mit seinem Preisblock P03 ebenfalls auf den Lock (siehe RES-371, 09:17). Nicht parallel schreiben; nach dir ist Thema 3 dran.
- **Bestform** (`e2a31e67-3318-499c-91c8-0559093e9a61`, Owner philippbechhaus): nur Thema 2, kein Konflikt.
- Jeden Schritt im jeweiligen Linear-Ticket dokumentieren. Keine Anrufe, keine Test-Buchungen, keine Formulare absenden.

---

## A. Hauptwebsite abnehmen-mit-arzt.de (Shot-Enhancer)

Live ist seit ca. 09:00 UTC Release **`9d4b003`** (quellidentisch zu `e5dfed7`; enthält Paket 1–3 inkl. RES-365 und RES-380 B3–B5).

### A1 – Live-Gegenprüfung der Thema-2-Punkte (nur lesen), zuerst

Auf `https://abnehmen-mit-arzt.de/`, allen 22 Unterseiten, `/llms.txt`, `/sitemap.xml` (initiales HTML **und** nach dem Laden im Browser):

1. Keine `+49 176 31784538` / `tel:+4917631784538` / `berlin@getresetapp.co` mehr; überall `+49 30 75435335`.
2. JSON-LD: MedicalBusiness (name „Abnehmen mit Arzt“, alternateName „AMITA Abnehmzentrum“, `hasOfferCatalog` 1899.00/2399.00 EUR, `sameAs` inkl. `https://maps.google.com/?cid=14185321041401501894` und Partnerverzeichnis, `parentOrganization` → `#organization`), genau **eine** Organization `#organization` (AMITA GmbH, Zehdenicker Straße 7a, 10119 Berlin), WebSite mit `publisher`. JSON parsebar. „Einziger deutscher Anbieter“ vorhanden, „Nachsorge“ nicht.
3. Kein 12-Monats-Angebot, kein „9 oder 12 Monate“, kein „50 Euro“-Aftercare; `/abnehmprogramm-12-monate/` führt zur 6-Monats-Seite; Sitemap 22 URLs.
4. `/llms.txt` = Faktenblock aus `GEO-ERGAENZUNGEN.md` (B4).
5. Startseiten-Titel und -Wording unverändert („Abnehmspritze Berlin | AMITA Abnehmzentrum“).

Ergebnis in **RES-380** und **RES-344** kommentieren. Bestanden → RES-344 und RES-380 auf Done, sobald A2/A3 ebenfalls live sind.

### A2 – Paket 4 (von Stefan freigegeben: „Kannst die Anpassungen auch vor Release machen“)

Fertig und geprüft war es als Replit-Commit **`641198a`** („Paket 4: og:site_name, S19-Titelsuffix für 5 Seiten, llms.txt-Partnerzeile“, Prüfpaket `reports/release-final3-2026-09-29/`, 46/46 + 86/86 + Browser 22/22). Im veröffentlichten `9d4b003` ist es **nicht** enthalten. Wieder einspielen (Cherry-Pick von `641198a` oder exakt nach Vorlage), nicht neu erfinden. Vorlage: `GEO-ERGAENZUNGEN.md`, Abschnitt „Paket 4“:

- `src/hooks/use-seo.ts`: `og:site_name` → „Abnehmen mit Arzt (AMITA)“.
- Titelsuffix `| Abnehmen mit Arzt (AMITA)` **nur** auf: `/abnehmspritze-ohne-diabetes`, `/vergleich-golighter`, `/vergleich-doktorabc`, `/vergleich-hausarzt` (ersetzt `| AMITA`), `/fuer-arzte` („Für Ärzte: AMITA Partnerpraxis werden | Abnehmen mit Arzt (AMITA)“ – in Seite **und** `scripts/prerender-seo.mjs` legalRoutes gleich). Die fünf Berlin-Standorttitel, die Startseite, Funnels und 404 bleiben.
- `public/llms.txt` Partnerzeile ersetzen durch: `- Partner practices: in addition to Berlin, AMITA works with partner practices in several German cities, including Hamburg (Dr. med. Karima Abou Deif-Strathmann, Im Alten Dorfe 24, 22359 Hamburg) and Düsseldorf (ESTHETIOS, Rustam Khadzhiev, Königsallee 30, 40212 Düsseldorf). The complete, current list is in the directory: https://partner.abnehmen-mit-arzt.de/`

### A3 – Facebook-Nachtrag (Stefan: offizielle Seite)

Vorlage `GEO-ERGAENZUNGEN.md`, Abschnitt „Paket 5 – Facebook-Seite“ (bitte „Facebook-Nachtrag (RES-380)“ nennen, „Paket 5“ ist der Name des Inhaltspakets von Thema 3):

- `index.html`: `https://www.facebook.com/abnehmenmitarzt` im MedicalBusiness-`sameAs` anfügen; in `#organization` ein `sameAs` mit derselben URL.
- `public/llms.txt`: nach der Zeile „Google Business Profile“ die Zeile `- Facebook: https://www.facebook.com/abnehmenmitarzt`.

### A4 – Prüfen und veröffentlichen

Dieselben Gates wie `release-final3`: Build, Root-Typecheck, Regressionen, Frontend-Tests, Browserprüfung (Laufzeit-Titel = Prerender-Titel auf 22 Routen, `og:site_name` nach Hydration, JSON-LD parsebar). Neuen Release-Kandidaten in RES-371 nennen. **Veröffentlichen (Republish) nur mit Stefans OK.** Danach A1-Checks für die neuen Punkte live wiederholen. Rückweg: vorheriges Deployment.

### A5 – goresetapp.com auf abnehmen-mit-arzt.de umziehen (RES-373, freigegeben von Stefan und Philipp)

goresetapp.com ist die zweite Domain desselben Shot-Enhancer-Deployments (Duplicate Content).

1. In den Replit-Deployment-Einstellungen `abnehmen-mit-arzt.de` (Apex) als primäre Domain.
2. goresetapp.com → dauerhaft auf denselben Pfad **inklusive Query** unter `https://abnehmen-mit-arzt.de`. Wenn Replit keinen Host-Redirect erlaubt: host-gebundenes `location.replace` als erstes Skript in `index.html` (nur Host `goresetapp.com`/`www.goresetapp.com`, Pfad + Query + Hash 1:1 übernehmen), Canonicals zeigen bereits auf Apex.
3. Vorher prüfen, dass keine Anzeigen/Funnels auf goresetapp.com verlinken (Bestform und reset-backend: keine gefunden).
4. Nach Veröffentlichung: Search Console → Property `goresetapp.com` → Einstellungen → **Adressänderung** auf `abnehmen-mit-arzt.de` (Konto `admin@getresetapp.co`).
5. Mit Thema 1 (RES-340) abstimmen; www-Domain dort ist ein eigener offener Punkt.

---

## B. Bestform (zurbestform.de / quick-meds.de) – RES-373 Stufe 1

Umgesetzt und von Thema 2 am gebauten Stand geprüft, **nicht veröffentlicht** (live noch Deployment `489747d1-…`). Details: RES-373 (Kommentare 09:04 und 09:15).

- Erstes Skript in `artifacts/web/index.html`: Redirect auf `https://abnehmen-mit-arzt.de/` **nur** wenn Host ∈ {zurbestform.de, www.zurbestform.de, quick-meds.de, www.quick-meds.de} **und** Pfad `/` **und** Query leer **und** kein Cookie `bf_funnel`. Tracking/App starten dann nicht. Build-Entry ohne Top-level-await (geprüft: `index-CB-dZIWU.js`).

**Aufgaben:**
1. Im Replit-Verlauf von Bestform die Testergebnisse der beiden Agent-Turns (`…01a0ed02…`, `…01a0f191…`) lesen; müssen grün sein.
2. Mit Stefans OK **Republish** von Bestform.
3. Smoke-Test (nur ansehen, nichts absenden): `https://zurbestform.de/` → landet auf abnehmen-mit-arzt.de; `https://zurbestform.de/?funnel=open` öffnet den Funnel; `https://zurbestform.de/?funnel=kurz` ebenso; `https://quick-meds.de/funnel/cross` lädt; `https://zurbestform.de/impressum` lädt; `https://quick-meds.de/` → abnehmen-mit-arzt.de. Zusätzlich: Buchungs-CTA auf `https://partner.abnehmen-mit-arzt.de/` führt weiterhin in den Funnel.
4. Ergebnis in RES-373. Bei jedem Funnel-Problem sofort auf das vorherige Deployment zurück.

**Nicht tun (Stufe 2, eigene Freigabe):** Umleitung von `/` mit UTM/gclid (erst nach Umstellung von Google Ads/Meta), Cross-Funnel/Resume-Links, `PUBLIC_FUNNEL_ORIGIN`, echte 301 per Express.

---

## C. Google-Unternehmensprofil (RES-379)

Stand: weitgehend eingetragen (Kategorien, Leistungen, Website-UTM, Buchungslink, Beitrag 1, Beiträge 2–4 geplant, Facebook-Link, Antworten auf externe Rezensionen). Bewertungslink `https://g.page/r/CcZYnIFUYtzEEBM/review`, QR-Code `google-bewertung-qr.png`.

Offen:
1. **Fotos:** Stefan prüft die Bilder im Bestform-Projekt (`artifacts/web/dist/public/assets/`: `clinic-interior`, `dr-pregla`, `Foto_1`–`Foto_4`, `Klinische_Behandlung`, `Sichere_betreuung`). Nur nach Bestätigung, dass es das Berliner Zentrum/Team ist (Dr. Pregla: Zustimmung), hochladen und das KI-wirkende Titelbild ersetzen. Keine Partnerpraxis-, KI- oder Vorher/Nachher-Bilder.
2. Öffentliche Prüfung (Maps, cid-Link): Facebook-Link, Leistungen, Chat (WhatsApp/SMS 0163, in erweiterter Prüfung bis 7 Tage).
3. Danach RES-379 auf Done.

Regeln: Name, Beschreibung, Telefon, Adresse, Öffnungszeiten nicht anfassen; keine Passwörter; keine Testbewertungen.

---

## D. Tickets abschließen

| Ticket | Abschluss, wenn |
|---|---|
| RES-344 Website-Fakten | A1 live bestanden und A2/A3 live |
| RES-380 GEO-Ergänzungen | A1 live bestanden und A3 live |
| RES-379 Google-Profil | C erledigt |
| RES-373 Altmarken | B live geprüft und A5 erledigt (Stufe 2 separat) |
| RES-342 Fakten | Stefan schließt (Entscheidungen S16–S19 dokumentiert) |
| RES-372 Übergabe | alles oben erledigt |

Bereits Done: RES-343, RES-345, RES-364, RES-366.

## Referenzen

- `FACTS.md`, `CHANGESET.md` (W01–W09), `SEITENMATRIX.md`, `REVIEW-THEMA2.md` – Ursprungsfakten (S17/S18 haben Vorrang)
- `UMSETZUNGSLISTE-REPLIT.md` – Inventur und Umsetzungsumfang
- `GEO-ERGAENZUNGEN.md` – B3–B5, Paket 4, Facebook-Nachtrag
- `GOOGLE-PROFIL-AUSBAU.md`, `HANDOVER-GOOGLE-PROFIL.md`, `google-bewertung-qr.png`
- Linear: RES-371 (Koordination/Writer-Lock), RES-373 (Altmarken), RES-379, RES-380
