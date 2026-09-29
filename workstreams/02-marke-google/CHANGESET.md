# Änderungsprotokoll Marke und Google

Stand: 29.09.2026. Dieses Dokument ist das konkrete Umsetzungspaket für Agent 01 und das Protokoll für Google-Änderungen durch Agent 02.

## G01 – Google-Unternehmensbeschreibung Berlin

Zielprofil: **Abnehmen mit Arzt**, Joachim-Karnatz-Allee 47, 10557 Berlin. Profil-ID aus der Verwaltungsoberfläche: `15142894115511933152`. Website: https://abnehmen-mit-arzt.de/. Vorhandener administrativer Zugriff im AMITA-Konto bestätigt; keine Berechtigungsänderung.

**Vorher:**

> Reset ist eine Praxis für medizinisch betreute Gewichtsreduktion mit der Abnehmspritze und der einzige deutsche Anbieter, der diese Behandlung mit ärztlicher Betreuung vor Ort kombiniert. Die Behandlung beginnt mit einem ausführlichen Termin in der Praxis: Körperanalyse, Diagnostik und ein persönliches Gespräch. Auf dieser Basis erstellt das ärztliche Team einen individuellen Behandlungsplan. Im weiteren Verlauf erfolgt eine regelmäßige ärztliche Begleitung per Video. Eine begleitende App unterstützt im Alltag, eine anschließende Nachsorgephase hilft, das Ergebnis langfristig zu halten.

**Nachher:**

> Abnehmen mit Arzt, kurz AMITA, begleitet Menschen bei der Gewichtsabnahme. Am Standort Berlin beginnt die Betreuung mit einem persönlichen ärztlichen Gespräch. Das Team bespricht Ihre gesundheitliche Ausgangslage und erstellt einen individuellen Behandlungsplan. Zum Programm gehören ärztliche Begleitung, persönliche Ernährungsberatung und digitale Unterstützung über die AMITA App. Die weitere Betreuung erfolgt vor Ort und digital. Termine finden nach Vereinbarung statt.

**Begründung:** Korrigiert den alten Markennamen, entfernt die nicht belegte Alleinstellung und beschreibt ausschließlich bereits öffentlich dargestellte Dienstleistungen. Keine Arzneimittelmarken, Wirkversprechen, Preise, Links oder neue medizinische Aussagen in der Beschreibung.

**Quellen:** Öffentliche Website https://abnehmen-mit-arzt.de/ und bestehendes Google-Profil, jeweils am 29.09.2026 gelesen. Regeln geprüft unter https://support.google.com/business/answer/3038177?hl=de und https://www.gesetze-im-internet.de/heilmwerbg/BJNR006049965.html.

**Status:** Im richtigen Google-Profil gespeichert. Google zeigte zunächst AUSSTEHEND / Prüfung. Bei späterem Reload am 29.09.2026 wurde der vollständige Nachher-Text in der öffentlichen Profilsektion „Von Abnehmen mit Arzt“ über „Mehr anzeigen“ geprüft: neuer Text vollständig übernommen, Reset und Alleinstellungsbehauptung entfernt. Beobachtung erfolgte in derselben angemeldeten Browsersitzung, jedoch in der öffentlichen Profilsektion statt im Bearbeitungsformular. Eine zusätzliche anonyme Ansicht wurde nicht behauptet.

**Rücknahme:** Exakten Vorher-Text wieder im Beschreibungsfeld einsetzen; eine Rücknahme der unbelegten Alleinstellung ist inhaltlich nicht empfohlen.

## Weiterhin unveränderte Profilfelder

- Profilname bleibt „Abnehmen mit Arzt“: bereits richtig. AMITA wird in der Beschreibung als Kurzform erklärt. Eine bloße Keyword-Erweiterung des Profilnamens ist nicht nötig.
- Öffnungszeiten, Attribute, Standort, Kategorien und Facebook-Verweis werden vor Belegen nicht überschrieben. Haupttelefon ist inzwischen durch Nutzerantwort belegt: G04/W07 gelten.
- Kein neues Standortprofil und keine Inhaberschafts- oder Rollenänderung.

## Website-Paket an Agent 01

Noch nicht auf der Website umgesetzt. Die folgenden Inhalte sind konkrete Korrekturen, keine Behauptung eines bereits erfolgten Releases. Bei Umsetzung initiales HTML und gerenderten Browserstand vergleichen. Originalwerte vor dem Release über die Versionsverwaltung sichern.

### W01 – Einheitliche Markenidentität

**Vorher:** Header-Label, Seitentitel, Footer, WebSite-Schema und Breadcrumb verwenden überwiegend „AMITA Abnehmzentrum“, während die Startseite „Abnehmen mit Arzt, kurz AMITA“ und Google „Abnehmen mit Arzt“ zeigen.

**Nachher:**

- Erste sichtbare textliche Markenreferenz: `Abnehmen mit Arzt (AMITA)`.
- Header-Link-/Logo-Alternativtext: `Abnehmen mit Arzt – AMITA`.
- Globale Seitentitel-Suffixe: `| Abnehmen mit Arzt (AMITA)`; individueller Seitenteil bleibt erhalten.
- WebSite.name: `Abnehmen mit Arzt`.
- WebSite.alternateName: `AMITA`.
- Breadcrumb-Startpunkt: `Abnehmen mit Arzt`.
- Footer-Label: `Abnehmen mit Arzt (AMITA)`.
- Bestehende gestaltete Logo-Bilddateien nicht eigenmächtig nachzeichnen. Ihre zugänglichen Textlabels dürfen die bestätigte Markenbeziehung erklären.

**Abnahme:** Name/Kurzform auf Startseite und allen gemeinsam verwendeten Komponenten konsistent; keine versehentliche Änderung juristischer Firmierung im Impressum oder fremder Marken in Vergleichen.

### W02 – Sachliche Beschreibung in Meta und strukturierten Daten

**Vorher:** MedicalBusiness.description enthält `Einziger deutscher Anbieter`, und MedicalBusiness.email verweist auf die frühere Reset-Adresse. MedicalBusiness und LocalBusiness stellen dieselbe Berliner Anschrift unter zwei IDs dar.

**Nachher für die allgemeine Markenbeschreibung:**

> Abnehmen mit Arzt (AMITA) verbindet persönliche ärztliche Begleitung, Ernährungsberatung und digitale Unterstützung bei der Gewichtsabnahme.

**Nachher für das standortbezogene Berliner Business-Objekt:**

> Abnehmen mit Arzt (AMITA) bietet am Standort Berlin persönliche ärztliche Begleitung bei der Gewichtsabnahme, Ernährungsberatung und digitale Unterstützung über die AMITA App. Termine nach Vereinbarung.

- Den vorhandenen sachlichen Beschreibungstext ersetzen; keine neue Alleinstellung, Erfolgsquote, Garantiezusage oder Medikamentenwerbung hinzufügen.
- Name `Abnehmen mit Arzt`, alternateName `AMITA Abnehmzentrum` bzw. `AMITA` als tatsächlich verwendete Alternativnamen.
- Im Berliner Objekt veröffentlichte Standort-E-Mail `berlin@abnehmen-mit-arzt.de` synchron zur sichtbaren Website setzen; tatsächliche Zustellung bleibt gesonderte Operations-Prüfung, keine Testmail senden.
- Haupttelefon aus der späteren ausdrücklichen Nutzerantwort übernehmen: `+493075435335`, siehe W07. Keine alte Google-Nummer kopieren.
- Vorhandene Unternehmensobjekte auf denselben realen Standort prüfen und zusammenführen oder sauber miteinander referenzieren. MedicalBusiness nur für den tatsächlich medizinischen Standort; den Websitebetreiber nicht automatisch mit der behandelnden Praxis gleichsetzen.
- `legalName: AMITA GmbH` und Betreiberanschrift `Zehdenicker Straße 7a, 10119 Berlin` sind inzwischen durch Nutzerantwort belegt; im Betreiberobjekt verwenden. Berliner Praxisobjekt behält Joachim-Karnatz-Allee 47. Siehe W07 zur ausdrücklichen Rollentrennung.
- Keine neuen Ärztequalifikationen aus `medicalSpecialty` ableiten. Bestehende Felder Endocrine/Diet/PrimaryCare medizinisch bestätigen lassen, bevor sie zur Qualifikationsbehauptung erweitert werden.
- Host und stabile IDs erst an die mit Agent 01 nachweislich beschlossene kanonische Domain anpassen.

**Abnahme:** Sichtbarer Inhalt und Schema stimmen überein; Einzigartigkeitsbehauptung fehlt; keine neuen unbekannten Telefonnummern, Standorte, Qualifikationen oder Registerdaten; keine doppelten Standortentitäten.

### W03 – Ablauf nicht unnötig auf Berlin einschränken

**Vorher:** Startseitenabsatz und FAQ behaupten, die Behandlung beginne ausschließlich in Berlin; auf derselben Seite werden andere Städte/Partnerärzte genannt.

**Sofort umsetzbarer Nachher-Text für allgemeine Ablaufabsätze:**

> Die Behandlung beginnt mit einem persönlichen ärztlichen Termin. Anschließend begleitet Sie das Team vor Ort und digital. Zum Programm gehören ärztliche Betreuung, persönliche Ernährungsberatung und digitale Unterstützung im Alltag.

**Aktualisierte Quellenlage:** Das vorhandene öffentliche Praxisverzeichnis und die beiden erreichbaren Anmeldeseiten belegen AMITA-Partnerpraxen in Düsseldorf und Hamburg; eigene Praxiswebsites bestätigen Namen und Adressen (FACTS S12–S14). Als Partnerpraxen benennen und direkt zum Verzeichnis führen, keine AMITA-eigenen Niederlassungen oder sofortige Terminverfügbarkeit behaupten. Auf einer ausdrücklich Berliner Standortseite darf Berlin weiter konkret genannt werden. Siehe W08.

**Abnahme:** Allgemeine Ablaufbeschreibung und Berlin-spezifische Standortbeschreibung sauber zugeordnet; nach Klärung echte Standorte mit denselben Fakten sichtbar und im Schema.

### W04 – Finanzierungsrate klar von Behandlungsdauer trennen

**Vorher:** Hero `Programme ab 79 €`; Preisvergleich `79,12 € pro Monat`; Karten `1.899 € gesamt oder 24 Raten à 79,12 €` und `2.399 € gesamt oder 24 Raten à 99,95 €`.

**Problem:** Monatsraten sind auf 24 Monate verteilt, die Behandlung ist mit 6 Monaten beschrieben. Die zwei genannten Ratenpläne summieren sich nicht exakt zu den publizierten Gesamtpreisen. Siehe Rechenbelege in FACTS.md. Einen anders gerundeten Schlussbetrag ohne gültigen Zahlungsplan nicht erfinden.

**Direkt umsetzbare Darstellung anhand der vom Nutzer bestätigten Startseiten-Preisquelle:**

- Hero statt isoliertem `Programme ab 79 €`: `6 Monate Begleitung · Ratenzahlung möglich`.
- Karte mit publiziertem Gesamtpreis 1.899 EUR: `6 Monate Behandlung · Gesamtpreis 1.899 € · Ratenzahlung über 24 Monate möglich`.
- Karte mit publiziertem Gesamtpreis 2.399 EUR: `6 Monate Behandlung · Gesamtpreis 2.399 € · Ratenzahlung über 24 Monate möglich`.
- QA-Präzisierung am 29.09.2026: `bis zu 24 Monate` durch die in den Programmkarten belegte Laufzeit `24 Monate` ersetzt. Die Startseiten-FAQ nennt zwar „bis zu“, führt aber keine weiteren konkreten Ratenpläne auf; die Karten beschreiben 24 Raten. Keine neuen Laufzeitoptionen ableiten. Diese Änderung betrifft den Textvorschlag, keine Vertragsbedingung.
- Direkt ergänzen: `Die Zahlungsdauer kann länger sein als die Behandlungsdauer. Ihren verbindlichen Zahlungsplan erhalten Sie vor Abschluss.`
- Die gesamte Preisvergleichstabelle einschließlich fremder Preiszeilen, Überschriften und Aussagen wie „ähnliche Größenordnung, teils darüber“ reversibel ausblenden, bis aktuelle Gesamtkosten bei gleichem Leistungsumfang und derselben Behandlungsdauer für jede Zeile belegt sind. Keine fremden Preise schätzen und keine unbestätigten relativen Sparversprechen stehen lassen.
- Als eigenständigen, nicht vergleichenden Preisblock veröffentlichen: `Unsere Programme: 6 Monate Behandlung ab 1.899 € Gesamtpreis. Ratenzahlung über 24 Monate möglich.` Dazu die zwei aktuellen Karten und den Hinweis zur unterschiedlichen Behandlungs- und Zahlungsdauer zeigen. Bereits belegte eigene Leistungsangaben dürfen außerhalb einer Anbietertabelle erhalten bleiben.
- Die exakten monatlichen Raten erst wieder prominent anzeigen, wenn reguläre Rate, Zahl der Raten, eventuelle Schlussrate und Gesamtbetrag aus derselben verbindlichen Datenquelle stammen.
- Keine Tarifpreise, bestehenden Zahlungspläne, Checkout-Daten oder Vertragskonditionen ändern. Diese Korrektur betrifft ausschließlich verständliche Darstellung schon publizierter Werte.

**Abnahme:** Jede sichtbare Ratenangabe nennt Zahl/Laufzeit der Zahlungen und zugehörigen Gesamtpreis; falls ein exakter Monatsbetrag genannt wird, muss seine Rechensumme inklusive Schlussrate stimmen. Keine Gleichsetzung von Rate und monatlichen Behandlungskosten. Auch fremde Preiszeilen, vergleichende Überschriften, Tabellen-Fußnoten und Preisbehauptungen im Fließtext sind vollständig geprüft oder ausgeblendet. Die aktuellen 6-Monats-Gesamtpreise sind durch Nutzerquelle bestätigt; Abschluss erst nach Abgleich aller betroffenen Seiten. Exakte fehlerhafte Ratenbeträge werden bis zu einem belegten Zahlungsplan nicht prominent weiterveröffentlicht.

### W05 – Unbelegte Zahlen nicht in neue Metadaten übernehmen

**Vorher:** Website-Badge 4,7/5 aus 478 Bewertungen; geprüftes Google-Profil 4,8/5 aus 8 Rezensionen.

**Nächste konkrete Aktion:** Quelle der 478 Bewertungen aus bestehendem Projekt ermitteln. Gibt es keinen eindeutigen Beleg/zugeordneten Bewertungslink, den unklaren Badge reversibel ausblenden, bis Quelle und Erhebungsdatum hinterlegt sind. Keine neue Bewertung erfinden, keine Rezensionen bearbeiten, die Google-Zahl nicht einfach als Ersatz festschreiben. Keine selbstbezogenen Bewertungssterne in neues Schema aufnehmen.

**Abnahme:** Jede veröffentlichte Bewertungszahl ist einer zugänglichen tatsächlichen Quelle zugeordnet und hat einen nachvollziehbaren Stand; andernfalls wird sie nicht dargestellt.

### W06 – Tatsächlich noch durch Fakten blockierte Inhalte

- Quelle der 478 Bewertungen. Bis Beleg W05 anwenden.
- Gültiger exakter Ratenplan inklusive Schlussrate, falls konkrete Monatsbeträge angezeigt werden sollen. W04 kann bereits ohne diese Beträge umgesetzt werden.
- Tarifdauer und Fortsetzung sind durch die neue Nutzerantwort geklärt: nur noch 6 Monate; danach individuelle Berechnung der Folgebehandlung. W09 ersetzt die alten 9-/12-Monats- und 50-EUR-Aussagen. Details der individuellen Berechnung nicht erfinden; sie blockieren diesen allgemeinen Nachhertext nicht.
- Tatsächliche Besucherzeiten, SMS-/WhatsApp-Zuordnung und weitere Praxisdetails über die abgeglichenen Partnerangaben hinaus.

Nicht mehr blockiert: aktuelle öffentliche Hauptnummer, Firma/Firmenadresse, Berliner Behandlungsadresse, aktuelle 6-Monats-Gesamtpreise, allgemeiner Programmumfang und diagnostische Entscheidung nach Bedarf. Quellen und Grenzen in FACTS.md.

## G02 – Search Console vorbereiten

Vorhandene legitime Domain-Property `goresetapp.com` im bestätigten AMITA-Administratorkonto geöffnet; Zugriff bestätigt. Übersicht am 29.09.2026 zeigt 12 indexierte und 4 nicht indexierte Seiten. Diese Zahlen betreffen ausdrücklich die alte Domain, nicht die neue Marketingwebsite.

Neue Domain-Property `abnehmen-mit-arzt.de` nach konkreter Nutzerbestätigung „Ja, einrichten“ angelegt. Google meldete „Inhaberschaft automatisch bestätigt“, Methode „Domainnamen-Anbieter“. Anschließend die neue Property mit sichtbarem Domainnamen geöffnet. Keine DNS-Einträge von uns geändert. Aggregierte Berichte werden laut Google verarbeitet und sind noch nicht verfügbar; URL-Einzelprüfungen funktionieren bereits.

Homepage-Prüfung in der neuen Property: `https://abnehmen-mit-arzt.de/` ist indexiert. Letzter Crawl 26.09.2026, 14:25:33, Googlebot für Smartphones; Crawling und Indexierung erlaubt, Abruf erfolgreich. Nutzer-Canonical: www-Homepage; Google-Canonical: geprüfte non-www-Homepage. Detailseiten werden separat geprüft. Sitemap erst nach Agent-01-Fix neu einreichen. Die Daten der alten Domain werden nicht als Beweis für die neue Domain verwendet.

## G03 – Analytics und Workspace abgrenzen

Analytics-Zugriff im bestätigten Konto vorhanden; aktuell wurde eine Entwicklungs-/iOS-Property (`reset-dev-c424a`) angezeigt. Daraus folgt kein belegter Produktions-Webstream für abnehmen-mit-arzt.de. Ein optionaler Dialog für E-Mail-Abonnements wurde nicht verändert. Agent 08 muss Produktions-Property und Website-Tag zuerst zuordnen.

Google Workspace Admin wurde für diese Profilkorrektur nicht benötigt und nicht verändert. Kein neues Google-Konto, kein Rollenwechsel, keine MFA- oder Passwortänderung. Die ausdrücklich autorisierte Search-Console-Domainverifizierung ist unter G02 separat dokumentiert.

## G04 – Öffentliche Telefonnummer nach Nutzerbestätigung

Vorbereitet am 29.09.2026 in Aufgabe `01a0ee2b-fcb9-73c1-9573-3109c5456c27`.

- Ziel: bestehendes bestätigtes Berliner Google-Profil „Abnehmen mit Arzt“, Joachim-Karnatz-Allee 47, verwaltet unter `admin@getresetapp.co`.
- Vorher: Haupttelefon `+49 163 5874217` laut bestehender Prüfung; vor Speicherung im Formular erneut prüfen.
- Nachher: Haupttelefon `+49 30 75435335`, maschinenlesbar `+493075435335`.
- Quelle: direkte Nutzerantwort am 29.09.2026 auf die Frage nach der öffentlichen Nummer für neue Interessenten: „die +49 3075435335“.
- Umfang: ausschließlich öffentliches Haupttelefon. Bestehende WhatsApp-/SMS-Konfiguration, Routing, Rufnummernbesitz und Öffnungszeiten werden dadurch nicht neu zugeordnet.
- Status: am 29.09.2026 ca. 17:25 UTC gespeichert. Google zeigt unter AKTUELL `0163 5874217` und unter AUSSTEHEND die Entfernung des alten Werts sowie Aktualisierung auf `030 75435335`. Hinweis: Prüfung normalerweise bis zu 10 Minuten. Dies ist der historische Speicher-Checkpoint.
- Öffentliche Übernahme: am selben Tag ca. 17:35 UTC frisch in der öffentlichen Profilansicht gesehen. Unabhängiger Reviewer bestätigte ca. 17:35–17:39 UTC Profilname, Standort, Website, `030 75435335` und Anrufziel `tel:03075435335` in einer eigenen öffentlichen Maps-Ansicht. RES-364 für das Haupttelefon BESTANDEN; Nachweis in REVIEW-THEMA2.md. Keine Prüfung der telefonischen Erreichbarkeit oder separater Nachrichtenkanäle behauptet.
- Rückweg: alten Feldwert aus der Vorheransicht wieder eintragen, falls die freigegebene Korrektur zurückgenommen werden soll.

## W07 – Bestätigte Rufnummer sowie Firmen- und Praxisanschrift

An Agent 01 zur koordinierten Website-Umsetzung:

1. Öffentliche Hauptkontaktnummer in Footer, Kontakt/Support/Impressum, geteilten Komponenten, Telefonnummerlinks und JSON-LD auf `+49 30 75435335` / `tel:+493075435335` setzen. Auch vorgerendertes HTML und mobile Varianten abgleichen. Historische Dokumente und fremde Praxisnummern nicht pauschal ersetzen.
2. Websitebetreiber: `AMITA GmbH`, `Zehdenicker Straße 7a, 10119 Berlin` (vom Nutzer ausdrücklich bestätigt).
3. Berliner Behandlungsort: `AMITA Abnehmzentrum`, `Joachim-Karnatz-Allee 47, 10557 Berlin` (vom Nutzer ausdrücklich von der Firmenanschrift abgegrenzt).
4. Die Firmenanschrift nicht als Behandlungsort oder neue Google-Niederlassung veröffentlichen. Betreiber und behandelnde Praxis als unterschiedliche Rollen modellieren.
5. Separate Partnerverzeichnis-Website im Backend benötigt dieselbe Hauptkontaktkorrektur; keine Behauptung, ein Shot-Enhancer-Release ändere diese zweite Anwendung mit.

Abnahme: veröffentlichte Kontaktflächen und strukturierte Daten zeigen die freigegebene Nummer; Firmen- und Behandlungsadresse sind ihrer jeweiligen Rolle zugeordnet. Agent 02 prüft Google getrennt, Agent 01 veröffentlicht die Marketingwebsite.

## W08 – Bestehende Partnerpraxen sichtbar und korrekt zuordnen

Belegte Grundlage: öffentliches AMITA-Praxisverzeichnis und eigene Praxiswebsites, Details FACTS S12–S14. Umsetzbarer Text für den allgemeinen Standortabschnitt:

> Ihr persönlicher Start findet im AMITA Abnehmzentrum in Berlin oder in einer unserer Partnerpraxen statt. In unserem Praxisverzeichnis finden Sie die jeweiligen Praxen und den Weg zur Anmeldung.

- Linktext `Praxen & Partnerärzte`, Ziel `https://partner.abnehmen-mit-arzt.de/`; in Navigation und Standortabschnitt sichtbar verlinken. Vorhandene Praxisdatenquelle weiterverwenden.
- Berliner Zentrum: Joachim-Karnatz-Allee 47, 10557 Berlin.
- Hamburg als **Partnerpraxis**: Dr. med. Karima Abou Deif-Strathmann, Im Alten Dorfe 24, 22359 Hamburg; bestehender AMITA-Anmeldelink `https://partner.abnehmen-mit-arzt.de/deif-strathmann-2`.
- Düsseldorf als **Partnerpraxis**: ESTHETIOS, Rustam Khadzhiev, Königsallee 30, 40212 Düsseldorf; bestehender AMITA-Anmeldelink `https://partner.abnehmen-mit-arzt.de/khadzhiev`.
- Kein festgeschriebener Praxen-Zähler: aktuell 13 Verzeichniseinträge beobachtet, aber kein dauerhafter Markenclaim daraus.
- Keine neue Adresse im Berliner Google-Profil; keine Profil-Dubletten und keine Behauptung aktueller freier Termine. Hamburg nennt auf der eigenen Praxiswebsite eine Sprechstundenpause 28.09.–02.10.2026.
- Kontaktleiste/Branding der zweiten Anwendung `partner.abnehmen-mit-arzt.de` separat korrigieren. Die historisch dokumentierte Backend-Datei `apps/web/src/lib/amita-site.js` fehlt im aktuellen Haupt-Checkout und ist dort als gelöscht markiert; keine fremde laufende Migration rückgängig machen. Zielcheckout/Deployment vor Implementierung bestimmen.

Abnahme: reale Partner korrekt bezeichnet, bestehende Anmeldung erreichbar, Arzt-/Adresszuordnung nachvollziehbar, keine Verwechslung von Hauptsitz/Zentrum/Partnerpraxis.

## W09 – Ausschließlich 6 Monate, danach individuell berechnete Folgebehandlung

**Autoritative Quelle:** Direkte Nutzerentscheidung S16 am 29.09.2026. Das 12-Monats-Angebot und Aftercare für pauschal 50 EUR/Monat gelten nicht mehr.

**Verbindlicher aktueller Angebotsstand:** Zwei 6-Monats-Varianten aus der bereits bestätigten Homepagequelle: 1.899 EUR mit Wegovy, 2.399 EUR mit Mounjaro. Zahlungsdauer von 24 Monaten ist Finanzierung, keine 24-monatige Behandlung. Keine neue Schlussrate erfinden.

**Kundentext für die Fortsetzung:**

> Nach den 6 Monaten erhalten Sie eine individuelle Berechnung für Ihre Folgebehandlung.

**FAQ-Frage:** Was passiert nach den 6 Monaten?

**FAQ-Antwort:**

> Unser Programm umfasst 6 Monate. Anschließend erhalten Sie eine individuelle Berechnung für Ihre Folgebehandlung.

**Konkrete Umsetzung:**

1. Das alte 12-Monats-Angebot mit 3.000 EUR / 137,71 EUR nicht mehr bewerben. Aktuelle Links und Angebotslisten auf das 6-Monats-Angebot umstellen; auch anfänglich ausgelieferten und nachgeladenen Inhalt angleichen.
2. Alte 12-Monats-Angebots-URLs einschließlich öffentlich erreichbarer Varianten führen nach Veröffentlichung dauerhaft zur aktuellen 6-Monats-Programmseite. Die Zielseite stellt beide aktuellen Varianten korrekt dar. Technische Umsetzung mit Thema 01 koordinieren; bestehende technische Korrekturen erhalten. Keine alte Angebotsseite in Navigation/Sitemap als aktives Produkt führen.
3. Sämtliche 9-/12-Monats-Aussagen zum aktuellen AMITA-Programm durch die bestätigte Dauer 6 Monate ersetzen. Keine globale Zahlenersetzung: medizinische Studiendauern, Datenschutzfristen, Finanzierungsraten, Historie und fremde Angebote sind andere Sachverhalte.
4. Den pauschalen 50-EUR-Aftercare-Tarif sowie feste Nachsorge-Inklusion aus Preisen, FAQ, Vergleichen, Fußnoten, Metadaten und strukturierten Daten entfernen. Stattdessen den obigen Text zur individuellen Folgebehandlung einsetzen. Auch allgemeine Aftercare-Ablaufversprechen mit dieser Aussage abgleichen.
5. Keine automatische Verlängerung, neue Gebühren, feste Folgedauer, pauschale Inklusivleistungen oder Berechnungsformel hinzufügen. Bestehende Kundenverträge, Abrechnung und Behandlungsentscheidungen werden durch diesen Marketingauftrag nicht geändert.

**Abnahme:** Sichtbarer und für Suchmaschinen gelieferter Inhalt zeigen nur aktuelle 6-Monats-Angebote und individuell berechnete Folgebehandlung. Alte Angebotslinks führen zum richtigen aktuellen Ziel; keine aktiven 12-Monats- oder 50-EUR-Folgeangebote in aktueller Navigation, Sitemap, FAQ oder Schema. Resttreffer im jeweiligen Kontext manuell beurteilen. Website-Release und Liveprüfung bleiben erforderlich.
