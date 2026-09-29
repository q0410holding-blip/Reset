# Umsetzungsliste Thema 2 → Shot-Enhancer (Replit)

> **Nutzerentscheidung S17 (29.09.2026, Stefan):** Conversion-Treiber werden **nicht** angepasst. Das umfasst Bewertungen, „Bekannt aus“, Preisvergleiche (inkl. Aussagen über Wettbewerber), 24/7, Antwortzeiten (laut Nutzer zutreffend), Erfolgszahlen, Patientenberichte und Funnels. **Das Startseiten-Wording bleibt unverändert.** Wörtlich: „Nein sowas auf gar keinen Fall anpassen! Das sind conversion driver! Auch nicht Wordings auf der Homepage home seite anpassen!“ S17 hat Vorrang vor SEITENMATRIX A4 (Startseite), A5, A6 sowie CHANGESET W04 (Darstellung) und W05. Inhalte nicht hinterfragen, sondern darauf aufbauen.
>
> **Verbleibender Umfang:** (a) sachliche Kontaktkorrektur (Telefon, Schema-E-Mail, Rollen Betreiber/Praxis); (b) Ablösung des 12-Monats-Angebots (S16); (c) 50-€-Aftercare durch A3 ersetzen (S16). Auf der Startseite ändern sich nur geteilte Komponenten mit der Telefonnummer (Header, Footer, Schema), kein sichtbarer Startseitentext.

Stand 29.09.2026. Rein lesende Inventur des **aktuellen** Replit-Quellstands (App `8dddf442-7691-4e3c-aea1-f521b9b1c7f8`, `artifacts/shotsy-landing`) per Replit MCP `list_app_files`/`read_app_file`. Kein Schreibauftrag, keine Veröffentlichung. Texte **1:1** aus SEITENMATRIX (A1–A6, B1, C1–C3) und CHANGESET (W01–W09) übernehmen, nichts neu formulieren. Bei W04/A1-Abweichung gilt A1.

Pfade relativ zu `artifacts/shotsy-landing/`. Zeilennummern nur wo belegt; sonst Zitat suchen.

## 0. Zentrale Hebel (zuerst)

| # | Datei | Änderung | Baustein |
|---|---|---|---|
| Z1 | `index.html` JSON-LD MedicalBusiness (~:172–212) | name `Abnehmen mit Arzt`, alternateName `AMITA Abnehmzentrum`; in der description nur „Nachsorge“ gemäß S16 anpassen; „Einziger deutscher Anbieter“ siehe F6; telephone `+493075435335`; email `berlin@abnehmen-mit-arzt.de` | C1, C3, W02 |
| Z2 | `index.html` LocalBusiness (~:214) | Dublette zur selben Adresse: mit MedicalBusiness zusammenführen oder per `@id` referenzieren; telephone `+493075435335` | W02 |
| Z3 | `index.html` WebSite (~:248) | name `Abnehmen mit Arzt`, alternateName `AMITA` | W01 |
| Z4 | `index.html` | Betreiber-Objekt ergänzen: legalName `AMITA GmbH`, Zehdenicker Straße 7a, 10119 Berlin; **nicht** als Behandlungsort | W07/C2 |
| Z5 | `index.html` meta author / og:site_name | `Abnehmen mit Arzt (AMITA)` | W01 |
| Z6 | `scripts/prerender-seo.mjs` | übernimmt `index.html` als Vorlage für alle 23 Seiten; alle eigenen Textbausteine unten mitziehen (initiales HTML = Browser) | C3 |
| Z7 | `SiteHeader.tsx` `PHONE_DISPLAY`/`PHONE_HREF` | `+49 30 75435335` / `tel:+493075435335`; Logo-Alt `Abnehmen mit Arzt – AMITA` | C1, W01 |

## 1. Telefon C1: alle Vorkommen von `+49 176 31784538` / `tel:+4917631784538`

Einzige gefundene Nummer. `0163 5874217` kommt im Quellstand nicht vor. Keine WhatsApp-/SMS-Links mit alter Nummer gefunden.

`index.html:181`, `:219` · `SiteHeader.tsx` (inkl. mobiles Menü) · `SiteFooter.tsx` (Adresslink + „Tel.“-Zeile) · `SeoArticle.tsx` (Adressblock, alle 9 SEO-Seiten) · `seo/AbnehmzentrumBerlin.tsx` (4×: FAQ „Wo befindet sich…“, FAQ „Wie vereinbare ich…“, Absatz „Standort in Berlin-Mitte“, Absatz „Termin und Kontakt“) · `Impressum.tsx` · `FuerFachkreise.tsx` · `data/vergleich.json:11–12` (CTA aller 6 Vergleichsseiten) · `prerender-seo.mjs` (buildSeoArticleBody, Impressum, Fachkreise).

Sichtbar `+49 30 75435335`, Link `tel:+493075435335`, Schema `+493075435335`.

## 2. Marke W01 / Rollen C2

- Kein sichtbarer Startseitentext wird geändert (S17). Titel-Suffixe, Breadcrumb-Start (`lib/public-urls.ts` defaultBreadcrumb, `SeoArticle.tsx`, Prerender): „AMITA Abnehmzentrum“ → `| Abnehmen mit Arzt (AMITA)` bzw. Breadcrumb `Abnehmen mit Arzt`.
- `public/site.webmanifest` „AMITA Berlin“ → `Abnehmen mit Arzt`.
- Footer-Label `Abnehmen mit Arzt (AMITA)`.
- Impressum: Betreiber AMITA GmbH/Zehdenicker Straße 7a bleibt; Berliner Behandlungsort getrennt.
- Nicht ändern: juristische Firmierung, fremde Marken in Vergleichen, interne Keys („reset“, „reset-hq“).

## 3. 12-Monats-Angebot ablösen (B1/W09)

**Route/Infrastruktur (mit Thema 1 abgestimmt umsetzen, Routenzahl 23→22):**
- `src/data/public-routes.json:4` `/abnehmprogramm-12-monate` entfernen, als **Alias/Weiterleitung auf `/abnehmprogramm-6-monate/`** führen (vorhandener Alias-Mechanismus wie `/so-funktionierts`). Echte 301/308 nur nach Hostingnachweis behaupten, sonst Meta-Refresh-Fallback transparent (RES-371).
- `public/sitemap.xml:5` Eintrag entfernen.
- `src/App.tsx` Route und Import `Abnehmprogramm12Monate` entfernen bzw. auf Redirect.
- `public/llms.txt` 12-Monats-Zeile entfernen.
- `scripts/prerender-seo.mjs:31` Eintrag `Abnehmprogramm12Monate` (137,71 / 3.000 / 25 %) entfernen.
- `scripts/seo-routing.test.mjs`: `publicPaths.length` 23→22, `uniqueTitles.size` 23→22 **bewusst** anpassen; neuen Test für die alte URL (mit/ohne Slash, `/index.html`, Query) ergänzen.
- `src/pages/Abnehmprogramm12Monate.tsx` stilllegen. Die 6-Monats-Zielseite bleibt inhaltlich unverändert.

**Komponenten/Daten:**
- `Preisvergleich.tsx` 6/12-Umschalter und `useState<6|12>` entfernen; `data/price-comparison.ts:47–56` Block `12` entfernen; `:149` Fußnote 3 und `:153` „1.899 € / 3.000 €“ entfallen mit A5 (siehe 6).
- `ProgramPage.tsx`/`PriceComparisonTeaser.tsx`: Typ `6 | 12` → 6; `ProgramTimeline.tsx` `PHASES_12` und Default `months = 12` → 6.
- `data/program-testimonials.ts` `testimonials12` und seine Verwendung auf Startseite/Cross-Funnel **bleiben unverändert** (S17). Beim Stilllegen der 12-Monats-Seite den Datenexport erhalten, denn Startseite und `CrossSteps1.tsx` importieren ihn.

**9-/12-Monats-Aussagen in SEO-Artikeln → 6 Monate + A3:**
- `seo/AbnehmspritzeBerlin.tsx`, **5 Stellen**: Meta-Description, FAQ „Wie lange dauert die Behandlung?“ (→ A3-FAQ „Unser Programm umfasst 6 Monate. Anschließend erhalten Sie eine individuelle Berechnung für Ihre Folgebehandlung.“, inkl. FAQ-JSON-LD), Body „…über 9 oder 12 Monate“, H2 „Ihre Behandlung über 9 oder 12 Monate“, Body „Im AMITA Abnehmzentrum werden Sie über 9 oder 12 Monate begleitet“. Berlin bleibt Berlin.
- `seo/AbnehmspritzeVerschreibenLassen.tsx`: H2-Abschnitt „Wie lange läuft die Behandlung?“ + folgender Aftercare-Satz → 6 Monate + A3.
- `seo/AbnehmspritzeKosten.tsx`: „Nach 9 oder 12 Monaten …“ → A3.
- `seo/AbnehmspritzeOhneDiabetes.tsx`: „Den gesamten Verlauf begleiten wir über zwölf Monate.“ → 6 Monate.

**Behalten (kein Angebot):** 24-Monats-Raten (Zahlungsdauer), Studien (68/72 Wochen, STEP/SURMOUNT), `Privacy.tsx` „In den letzten 12 Monaten“, Datenschutzfristen, Oviva-Diagnosezeitpunkt, Funnel-Zielfrage „In 6/9/12 Monaten“ (`BodyDataSteps.tsx`, Nutzerziel, kein Programm).

## 4. 50-EUR-Aftercare entfernen (W09 Ziff. 4, A3)

- `seo/AbnehmspritzeKosten.tsx`: FAQ „Was kostet die Zeit nach der Spritze?“ („50 Euro pro Monat“, inkl. FAQ-JSON-LD) → A3-FAQ; H2 „Was kostet die Aftercare?“ + „Sie kostet 50 Euro pro Monat.“ → A3-Anschlusssatz; Absatz „Aftercare nach der aktiven Behandlung“; Listenpunkt „welche Kosten … für Aftercare entstehen“; 2× „…App-Begleitung und Aftercare“.
- `seo/AbnehmspritzeBerlin.tsx`: FAQ „…Danach kann eine Aftercare anschließen“; FAQ „Was passiert nach dem Absetzen?“ („…mit Aftercare, Tapering und Rebound-Prävention“); Liste „Anschlussbegleitung mit Tapering…“; Absatz „In der Aftercare begleiten wir Sie…“ → jeweils A3.
- `seo/AbnehmspritzeVerschreibenLassen.tsx`: „Nach der aktiven Behandlung kann eine Aftercare anschließen.“ → A3.
- `index.html:178` „…und Nachsorge“ → entfällt mit Z1.
- `data/vergleich.json:380` „Nach der aktiven Behandlung begleiten wir die Stabilisierung…“ → A3.
- `ProgramTimeline.tsx` „Übergang zur Erhaltungs-Phase“, „Anti-Jojo-Coaching“: bleibt (ohne Preis, S17).
- **Nicht betroffen:** Cross-Funnel-„Erhaltungspaket“ (`CrossAngebot.tsx`, `CrossOrderModal.tsx`), Preise dynamisch vom Backend, separates Produkt.

## 5.–8. ENTFÄLLT (Nutzerentscheidung S17)

Keine Änderungen an Preisdarstellung, Preisvergleichen (inkl. fremder Preise/Leistungen, Fußnoten), Bewertungen 4,7/478, „Bekannt aus“, 24/7, Antwortzeiten, Erfolgszahlen (15/25/30/98/20/100 %), Standortzeile „Berlin · Düsseldorf · Hamburg“, Funnels und Patientenberichten (auch die 12-Monats-Berichte bleiben: Kunden können 12 Monate dabei sein). **Keinerlei Wording auf der Startseite ändern.**

Einzige Ausnahme im Preisvergleich (folgt aus S16, keine Wording-Änderung): Das nicht mehr existierende 12-Monats-Angebot verschwindet aus dem 6/12-Umschalter (`Preisvergleich.tsx`) und aus `price-comparison.ts` (Block `12`; in Fußnote 3 nur „137,71 € für das 12-Monats-Paket“/„bzw. 12 Monate“, in `:153` nur „/ 3.000 €“). Der 6-Monats-Vergleich bleibt vollständig.

## 9. Nicht Teil dieses Pakets

- `cross/CrossPostPurchase.tsx` `https://www.getresetapp.co/app` → RES-373 (Altmarken).
- Partnerverzeichnis → RES-366 / PR #1241 (separate App).
- `AbnehmzentrumBerlin.tsx` bezeichnet 10557 als „Berlin-Mitte“, `ProgramPage.tsx` als „Berlin-Tiergarten“: nur Hinweis, nicht in der Vorlage.

## 10. Befund zum Review-Hinweis „versteckter 12-Monats-Link ab 137,71 auf der Startseite“

Im aktuellen Quellstand nicht vorhanden: `Home.tsx` rendert `PriceComparisonTeaser months={6}`, `seo-rendering.test.mjs` prüft ausdrücklich das Fehlen von „12 Monate“/„137,71“/„3.000“ auf der Startseite. Der Live-Treffer stammt vermutlich aus dem alten Release `bcfe0b77…`. Nach Release live nachprüfen.

## Geklärte Fragen (S17)

F1 „Bekannt aus“ bleibt · F2 Funnels bleiben · F3 12-Monats-Patientenberichte bleiben · F4 Vergleiche inkl. Aussagen über Wettbewerber bleiben · F5 Support-Antwortzeiten stimmen und bleiben.

## Offen

- **F6** „Einziger deutscher Anbieter …“ steht unsichtbar im Suchmaschinen-Datenblock (`index.html:178`). Laut RES-365 sollte er ersetzt werden, im Google-Profil ist er schon entfernt. Nach S17 ohne Nutzerbestätigung **nicht** ändern.

## Abnahme nach Umsetzung

Restfundstellensuche nur für: alte Nummer, `berlin@getresetapp.co`, 137,71, 3.000, 9/12 Monate als Programmdauer, 50 EUR. Die Treffer 478, 79,12, 24/7 usw. bleiben bewusst stehen (S17). Build, Root-Typecheck, `seo-routing`/`seo-rendering`-Tests mit echten Ausgaben; initiales HTML = Browser; alte 12-Monats-URL-Varianten getrennt prüfen. Keine Anrufe/Buchungen als Test.
