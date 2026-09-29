# Umsetzungsliste Thema 2 → Shot-Enhancer (Replit)

Stand 29.09.2026. Rein lesende Inventur des **aktuellen** Replit-Quellstands (App `8dddf442-7691-4e3c-aea1-f521b9b1c7f8`, `artifacts/shotsy-landing`) per Replit MCP `list_app_files`/`read_app_file`. Kein Schreibauftrag, keine Veröffentlichung. Texte **1:1** aus SEITENMATRIX (A1–A6, B1, C1–C3) und CHANGESET (W01–W09) übernehmen, nichts neu formulieren. Bei W04/A1-Abweichung gilt A1.

Pfade relativ zu `artifacts/shotsy-landing/`. Zeilennummern nur wo belegt; sonst Zitat suchen.

## 0. Zentrale Hebel (zuerst)

| # | Datei | Änderung | Baustein |
|---|---|---|---|
| Z1 | `index.html` JSON-LD MedicalBusiness (~:172–212) | name `Abnehmen mit Arzt`, alternateName `AMITA Abnehmzentrum`; description durch W02-Standorttext ersetzen (entfernt „Einziger deutscher Anbieter“ und „Nachsorge“); telephone `+493075435335`; email `berlin@abnehmen-mit-arzt.de` | C1, C3, W02 |
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

- Titel-Suffixe, Breadcrumb-Start (`lib/public-urls.ts` defaultBreadcrumb, `SeoArticle.tsx`, Prerender): „AMITA Abnehmzentrum“ → `| Abnehmen mit Arzt (AMITA)` bzw. Breadcrumb `Abnehmen mit Arzt`.
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
- `src/pages/Abnehmprogramm12Monate.tsx` stilllegen. Alte 25 %-/24/7-Claims **nicht** in die Zielseite kopieren.

**Komponenten/Daten:**
- `Preisvergleich.tsx` 6/12-Umschalter und `useState<6|12>` entfernen; `data/price-comparison.ts:47–56` Block `12` entfernen; `:149` Fußnote 3 und `:153` „1.899 € / 3.000 €“ entfallen mit A5 (siehe 6).
- `ProgramPage.tsx`/`PriceComparisonTeaser.tsx`: Typ `6 | 12` → 6; `ProgramTimeline.tsx` `PHASES_12` und Default `months = 12` → 6.
- `data/program-testimonials.ts` `testimonials12` („in 12 Monaten abgenommen“, 34/27/33 kg, „ein ganzes Jahr“): **nicht mehr auf Startseite/Cross-Funnel verwenden** (Home.tsx `testimonials12[0]`, `[1]`; `CrossSteps1.tsx`). Siehe offene Frage F3.
- `TestimonialsCarousel.tsx` `defaultTestimonials` (ungenutzt): mit entfernen oder auf 6 Monate prüfen.

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
- `ProgramTimeline.tsx` „Übergang zur Erhaltungs-Phase“, „Anti-Jojo-Coaching“: mit A3 abgleichen (keine feste Folgeleistung versprechen).
- **Nicht betroffen:** Cross-Funnel-„Erhaltungspaket“ (`CrossAngebot.tsx`, `CrossOrderModal.tsx`), Preise dynamisch vom Backend, separates Produkt.

## 5. Preise und Finanzierung (A1/A2/W04)

- `Home.tsx` Hero „Programme ab 79 €“ → `6 Monate Begleitung · Ratenzahlung möglich`.
- `data/home-programs.json:12–13` (1.899 / „oder 24 Raten à 79,12 €“) und `:19–20` (2.399 / 99,95) → A1-Karten: `6 Monate Behandlung mit Wegovy · Gesamtpreis 1.899 €` bzw. `… Mounjaro · Gesamtpreis 2.399 €` + A1-Ratenhinweis. `:11`/`:18` „Verlieren Sie bis zu 15 % / 25 %“ → A6.
- `PricingCard.tsx` Defaults `79,12`/`1.899`, „auf 24 Monate Ratenzahlung“, „…und 24/7 WhatsApp-Chat.“ → A1 + A6.
- `Abnehmprogramm6Monate.tsx:13–14` (Preis-Intro 79,12) → A1.
- `data/faq.ts` erste FAQ + `HomeFaqSchema.tsx:6` → A1-Preis-FAQ (sichtbar und Schema gleich).
- Exakte 79,12/99,95 nicht mehr prominent (A2). **Nicht ändern:** `lib/funnel-program.ts:18–19, :32–33` (Buchungs-/Checkout-Daten; W04: keine Checkout-Daten ändern), `funnel/steps/ProgramSteps.tsx` „über 24 Monate finanziert“ (Funnel, siehe F2).
- Rabatt-/Nachlassaussagen („Einmalzahlung (-5 %)“ `price-comparison.ts:149`, „zahlt etwas weniger“ in `vergleich.json:62, :197, :208, :434, :452`, `AbnehmspritzeKosten.tsx`) → A2, entfallen.

## 6. Preisvergleiche reversibel ausblenden (A5)

Reversibel = per Flag/Konstante ausblenden, Daten nicht löschen.

- `/preisvergleich`: `Preisvergleich.tsx` + `data/price-comparison.ts` gesamte Tabelle inkl. Zeilen „Online-Anbieter¹ … teils darüber¹“, „Hausarzt² … ähnliche Größenordnung²“, inclusionRows (Fixpreis/„Preis steigt“, „24/7 WhatsApp-Support“, „BIA-Körperscan & Blutkontrolle“), Fußnoten 1–3, „Preisannahme“ (`:138–155`) → Ersatzblock A5 „Unsere Programme und Kosten“ + A1. Prerender `buildPriceComparisonBody` mitziehen.
- Vergleichsseiten (`data/vergleich.json` via `VergleichShared.tsx`, `VergleichUebersicht.tsx`, `VergleichAnbieter.tsx`, Prerender `buildVergleichRoutes`): Tabellenzeilen **Preis** und **Zahlweise** aller Anbieter (`:99`, `:122`, `:145`, `:158`, `:168`, `:185`, `:191`), Fußnoten `:197–199`, preisSatz `:226, :259, :292, :325`, Hausarzt-Preisabsatz `:355`, DoktorABC „49 €“ `:322`, Übersicht-Preis-/Kostentexte und -FAQ in `:422–452` soweit Preis-/Kostenbezug → A5-Ersatzblock + A1–A3. Nicht-preisliche Zeilen (Behandlungsort, Begleitung, Erstgespräch, Diagnostik) nur mit Beleg; siehe F4.
- `PriceComparisonTeaser.tsx` (Startseite + 6-Monats-Seite): „Was Ihr Abnehmprogramm wirklich kostet.“ / „Feste Programmkosten im direkten Vergleich…“ → A5-Ersatzblock; Links zu Einzelvergleichen dürfen bleiben.
- `seo/AbnehmspritzeKosten.tsx` H2 „Ist das AMITA Abnehmzentrum günstiger als ein Online-Anbieter?“ + „…ähnlicher Größenordnung, teils darüber“ → ausblenden (A5).

## 7. Unbelegte Nachweise ausblenden (A6/W05)

- **4,7/478:** `Home.tsx` Hero („SEHR GUT“, Sterne, „4.7/5 aus 478 Bewertungen“); `FuerFachkreise.tsx` Trust-Leiste; `prerender-seo.mjs` buildFuerFachkreiseBody. Funnel-Stellen siehe F2.
- **24/7:** `ProgramPage.tsx` „24/7 Support“ (beide Programmseiten), `ProgramTimeline.tsx` „24/7 Ansprechpartner“, `PricingCard.tsx`, `price-comparison.ts:119`, Prerender buildProgramBody `<li>24/7 Support</li>` und buildPriceComparisonBody.
- **Antwortzeiten/Erfolgszahlen:** `FuerFachkreise.tsx` + Prerender „98 % … nach 3 Monaten noch aktiv“, „~20 % Gewichtsverlust nach 6 Monaten…“, „100 % der Nebenwirkungsmeldungen … am selben Tag“; `vergleich.json:380` „erreichen Sie uns jederzeit“, `:399` Kachel „jederzeit“; `vergleich.json:223` Juniper „in der Regel innerhalb einer Stunde“ (fremder Claim, fällt unter A5-Belegpflicht); `home-programs.json:11/:18` 15 %/25 %; `ProgramPage` „Verliere bis zu {lossHi}“; `WeightLossCalculator` Startseite „bis zu 25 %“.
- `Support.tsx` „in der Regel innerhalb von 24 Stunden“ / „meist sofort“ und „Wir antworten innerhalb eines Werktages“ (`FuerFachkreise.tsx`, `PartnerForm.tsx`): siehe F5.
- Keine Ersatzsterne, keine Google-4,8 einsetzen.

## 8. Standorte (A4/W03/W08)

- `Home.tsx` + Prerender „Bereits in vielen deutschen Städten“, „Berlin · Düsseldorf · Hamburg“ / „Standorte: Berlin, Düsseldorf und Hamburg“ → A4-Text + Link `Praxen & Partnerärzte` → `https://partner.abnehmen-mit-arzt.de/` (Hamburg/Düsseldorf nur als Partnerpraxen).
- Allgemeine Ablaufabsätze mit „beginnt in Berlin“ → A4; Berlin-Seiten behalten Berlin.
- Navigation: Link `Praxen & Partnerärzte` (W08).

## 9. Nicht Teil dieses Pakets

- `cross/CrossPostPurchase.tsx` `https://www.getresetapp.co/app` → RES-373 (Altmarken).
- Partnerverzeichnis → RES-366 / PR #1241 (separate App).
- `AbnehmzentrumBerlin.tsx` bezeichnet 10557 als „Berlin-Mitte“, `ProgramPage.tsx` als „Berlin-Tiergarten“: nur Hinweis, nicht in der Vorlage.

## 10. Befund zum Review-Hinweis „versteckter 12-Monats-Link ab 137,71 auf der Startseite“

Im aktuellen Quellstand nicht vorhanden: `Home.tsx` rendert `PriceComparisonTeaser months={6}`, `seo-rendering.test.mjs` prüft ausdrücklich das Fehlen von „12 Monate“/„137,71“/„3.000“ auf der Startseite. Der Live-Treffer stammt vermutlich aus dem alten Release `bcfe0b77…`. Nach Release live nachprüfen.

## Offene Fragen an den Nutzer (blockieren den Rest nicht)

- **F1** „Bekannt aus: BILD · RTL · Bunte · InStyle · FOCUS“ (`Home.tsx`, `FuerFachkreise.tsx`, Prerender, `CrossTrust.tsx`): nicht in der Vorlage. Belegt? Sonst analog A6 ausblenden.
- **F2** Buchungs-/Cross-/Oviva-Funnels (noindex, nicht in den 23 Seiten): „SEHR GUT 4,7“ (`FunnelLayout.tsx`, `CrossRating.tsx`, `OvivaFunnelApp.tsx:450`), „24/7 WhatsApp-Support“ (`ProgramSteps.tsx`), „7,3 % … 8. Woche“ und „100 % … innerhalb von 12 Stunden“ (`ResultStep.tsx`), „Bis zu 30 %*“ (`BodyDataSteps.tsx`). A6 auch dort anwenden?
- **F3** 12-Monats-Patientenberichte (`testimonials12`): entfernen oder nur „in 12 Monaten“ streichen? Vorschlag: auf Startseite/Cross-Funnel nicht mehr zeigen, da sie das abgelöste Programm bewerben.
- **F4** Nicht-preisliche Vergleichszeilen (z. B. „Bei keinem der großen Online-Anbieter gehört ein Blutbild…“): A5 verlangt Belege für fremde Leistungen. Ausblenden bis Beleg?
- **F5** Support-Antwortzeiten („innerhalb von 24 Stunden“, „innerhalb eines Werktages“): gelebter Standard? Sonst A6.

## Abnahme nach Umsetzung

Restfundstellensuche gemäß SEITENMATRIX „Abnahme“ Punkt 4 (alte Nummer, `berlin@getresetapp.co`, 478, 79/79,12/99,95, 137,71, 3.000, 9/12 Monate, 50 EUR, Nachlass, ähnliche Größenordnung, 24/7, „Einziger“). Build, Root-Typecheck, `seo-routing`/`seo-rendering`-Tests mit echten Ausgaben; initiales HTML = Browser; alte 12-Monats-URL-Varianten getrennt prüfen. Keine Anrufe/Buchungen als Test.
