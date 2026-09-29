# GEO-/SEO-Ergänzungen Website (rein additiv)

Stand 29.09.2026. Nutzerauftrag: „Dann mach das noch!“ (Punkte B3–B5). Grundregel S18 gilt: bestehende Inhalte nicht umformulieren, nur ergänzen. Alle Werte stammen aus bestehenden Fakten (FACTS.md, `home-programs.json`, Impressum, Google-Profil). Umsetzung per Replit MCP im selben Auftrag wie die Umsetzungsliste; Writer-Lock bei Thema 1 beachten.

## B3 – Angebote im Datenblock (`artifacts/shotsy-landing/index.html`, MedicalBusiness)

Folgendes Feld **zusätzlich** in das MedicalBusiness-Objekt (`@id` `https://abnehmen-mit-arzt.de/#business`) einfügen. Namen, Leistungen und Preise 1:1 aus `src/data/home-programs.json`:

```json
"hasOfferCatalog": {
  "@type": "OfferCatalog",
  "name": "Abnehmprogramme",
  "itemListElement": [
    {
      "@type": "Offer",
      "name": "Wegovy · 6 Monate",
      "price": "1899.00",
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock",
      "url": "https://abnehmen-mit-arzt.de/abnehmprogramm-6-monate/",
      "itemOffered": {
        "@type": "Service",
        "name": "Abnehmprogramm 6 Monate mit Wegovy",
        "description": "Ärztliche Begleitung, individuelle Dosierung, Ernährungsberatung, laufende Anpassung, digitale Verlaufskontrolle, AMITA App & Support."
      }
    },
    {
      "@type": "Offer",
      "name": "Mounjaro · 6 Monate",
      "price": "2399.00",
      "priceCurrency": "EUR",
      "availability": "https://schema.org/InStock",
      "url": "https://abnehmen-mit-arzt.de/abnehmprogramm-6-monate/",
      "itemOffered": {
        "@type": "Service",
        "name": "Abnehmprogramm 6 Monate mit Mounjaro",
        "description": "Ärztliche Begleitung, individuelle Dosierung, Ernährungsberatung, laufende Anpassung, digitale Verlaufskontrolle, AMITA App & Support."
      }
    }
  ]
}
```

Hinweise:
- Keine Monatsrate im Schema (die Rundung 24 × 79,12 ≠ 1.899 würde Maschinen widersprüchliche Werte liefern). Die sichtbare Rate auf der Website bleibt unverändert (S17).
- Keine aggregateRating aufnehmen (Google wertet selbst vergebene Sterne für LocalBusiness nicht und kann sie als Spam werten).
- Prerender übernimmt `index.html` → wirkt auf allen Seiten.

## B5 – Datenblock verknüpfen (`sameAs`, Betreiber, WebSite)

Im MedicalBusiness `sameAs` **ergänzen** (bestehenden Eintrag behalten):

```json
"sameAs": [
  "https://share.google/Ebza2Utq9wl6enXZK",
  "https://maps.google.com/?cid=14185321041401501894",
  "https://partner.abnehmen-mit-arzt.de/"
]
```

- Die `cid`-URL ist die stabile Google-Maps-Adresse des bestätigten Profils (aus `0xc4dc6254819c58c6`), robuster als der Kurzlink.
- **Social-Media-Profile:** Auf der Website ist aktuell keins verlinkt. Die Facebook-Seite heißt laut FACTS noch „Reset-Deutschland“. **Offene Frage an den Nutzer:** Welche Instagram-, Facebook-, LinkedIn- und TikTok-URLs gehören heute zu Abnehmen mit Arzt? Nur bestätigte URLs aufnehmen.

Betreiber als eigenes Objekt ergänzen (verknüpft, **nicht** als Behandlungsort):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://abnehmen-mit-arzt.de/#organization",
  "name": "Abnehmen mit Arzt",
  "alternateName": "AMITA",
  "legalName": "AMITA GmbH",
  "url": "https://abnehmen-mit-arzt.de/",
  "logo": "https://abnehmen-mit-arzt.de/favicon-512.png",
  "email": "kontakt@abnehmen-mit-arzt.de",
  "telephone": "+493075435335",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Zehdenicker Straße 7a",
    "postalCode": "10119",
    "addressLocality": "Berlin",
    "addressCountry": "DE"
  }
}
```

Im MedicalBusiness ergänzen: `"parentOrganization": { "@id": "https://abnehmen-mit-arzt.de/#organization" }`. Im WebSite-Objekt ergänzen: `"publisher": { "@id": "https://abnehmen-mit-arzt.de/#organization" }`.

## B4 – `artifacts/shotsy-landing/public/llms.txt`

Bestehende Beschreibungen bleiben wörtlich erhalten. Geändert werden nur der Markenname (S19) und die Links: Sie zeigen jetzt auf den kanonischen Host ohne www und mit Schrägstrich am Ende (Konvention Thema 1; www hat derzeit keinen gültigen HTTPS-Zugang). Die übrigen Abschnitte werden ergänzt. **Hinweis:** Die aktuelle Datei enthält entgegen meiner früheren Aussage **keine** 12-Monats-Zeile, dort ist nichts zu entfernen.

Neuer vollständiger Inhalt:

```markdown
# Abnehmen mit Arzt (AMITA)

> Abnehmen mit Arzt (AMITA) in Berlin provides medically supervised weight reduction with GLP-1 treatments such as Wegovy and Mounjaro, including on-site diagnostics, an individual treatment plan, medical follow-up, and app support.

This is a German-language public information site for adults considering medically supervised weight loss in Berlin. Content is informational and does not replace an individual medical consultation.

## Key facts

- Brand: Abnehmen mit Arzt, short form AMITA.
- Treatment location Berlin: AMITA Abnehmzentrum, Joachim-Karnatz-Allee 47, 10557 Berlin, Germany.
- Website operator: AMITA GmbH, Zehdenicker Straße 7a, 10119 Berlin, Germany (company address, not a treatment location).
- Phone for new patients: +49 30 75435335
- Email: berlin@abnehmen-mit-arzt.de
- Programmes (6 months each):
  - Wegovy · 6 Monate: 1.899 € total.
  - Mounjaro · 6 Monate: 2.399 € total.
  - Both include: Ärztliche Begleitung, individuelle Dosierung, Ernährungsberatung, laufende Anpassung, digitale Verlaufskontrolle, AMITA App & Support.
  - Payment in instalments over 24 months is possible (payment period, not treatment period).
  - Nach den 6 Monaten erhalten Sie eine individuelle Berechnung für Ihre Folgebehandlung.
- First step: free initial consultation (Kostenloses Erstgespräch): https://abnehmen-mit-arzt.de/?funnel=open
- Partner practices (in addition to Berlin): Hamburg (Dr. med. Karima Abou Deif-Strathmann, Im Alten Dorfe 24, 22359 Hamburg) and Düsseldorf (ESTHETIOS, Rustam Khadzhiev, Königsallee 30, 40212 Düsseldorf). Directory: https://partner.abnehmen-mit-arzt.de/
- Google Business Profile: https://maps.google.com/?cid=14185321041401501894

## Key pages

- [Abnehmen mit Arzt](https://abnehmen-mit-arzt.de/): Overview of the practice, medically supervised weight reduction, diagnostics, and treatment support in Berlin.
- [Abnehmspritze Berlin](https://abnehmen-mit-arzt.de/abnehmspritze-berlin/): How medically supervised GLP-1 treatment with an injection works in Berlin.
- [Abnehmspritze Kosten](https://abnehmen-mit-arzt.de/abnehmspritze-kosten/): Information about treatment costs and what is included.
- [Mounjaro Berlin](https://abnehmen-mit-arzt.de/mounjaro-berlin/): Information about Mounjaro treatment and medical supervision in Berlin.
- [Wegovy Berlin](https://abnehmen-mit-arzt.de/wegovy-berlin/): Information about Wegovy treatment and medical supervision in Berlin.
- [Abnehmzentrum Berlin](https://abnehmen-mit-arzt.de/abnehmzentrum-berlin/): What to expect from an in-person medical weight-loss practice.
- [Abnehmspritze ohne Diabetes](https://abnehmen-mit-arzt.de/abnehmspritze-ohne-diabetes/): Eligibility questions for GLP-1 treatment without a diabetes diagnosis.
- [Abnehmspritze verschreiben lassen](https://abnehmen-mit-arzt.de/abnehmspritze-verschreiben-lassen/): Medical assessment and prescription process.
- [Abnehmspritze Nebenwirkungen](https://abnehmen-mit-arzt.de/abnehmspritze-nebenwirkungen/): General information about possible side effects and medical monitoring.
- [Abnehmprogramm 6 Monate](https://abnehmen-mit-arzt.de/abnehmprogramm-6-monate/): Six-month medically supervised treatment program.
- [Preisvergleich](https://abnehmen-mit-arzt.de/preisvergleich/): Comparison of treatment program options and included services.
- [FAQ](https://abnehmen-mit-arzt.de/faq/): Frequently asked questions about treatment, eligibility, costs, and support.
- [Alle Anbieter im Vergleich](https://abnehmen-mit-arzt.de/vergleich/): Overview comparison of all GLP-1 weight-loss providers.
- [AMITA vs. Juniper](https://abnehmen-mit-arzt.de/vergleich-juniper/): Detailed comparison of AMITA and Juniper on programme structure, medical supervision, cost, and results.
- [AMITA vs. Voy](https://abnehmen-mit-arzt.de/vergleich-voy/): Detailed comparison of AMITA and Voy.
- [AMITA vs. GoLighter](https://abnehmen-mit-arzt.de/vergleich-golighter/): Detailed comparison of AMITA and GoLighter.
- [AMITA vs. DoktorABC](https://abnehmen-mit-arzt.de/vergleich-doktorabc/): Detailed comparison of AMITA and DoktorABC.
- [AMITA vs. Hausarzt](https://abnehmen-mit-arzt.de/vergleich-hausarzt/): Comparison of AMITA with a GP-based approach.
- [Für Ärzte](https://abnehmen-mit-arzt.de/fuer-arzte/): Information for physicians interested in partnering with AMITA.
- [Support](https://abnehmen-mit-arzt.de/support/): Contact and support for current and prospective patients.
- [Impressum](https://abnehmen-mit-arzt.de/impressum/): Legal notice and operator details.
```

## Abnahme

- JSON-LD nach Umsetzung parsebar (kein Syntaxfehler), in initialem HTML **aller** Seiten identisch (Prerender).
- Rich-Results-/Schema-Validator ohne Fehler; nur echte Warnungen dokumentieren.
- `https://abnehmen-mit-arzt.de/llms.txt` nach Release abrufbar, `text/plain`, alle Links 200 (nach Routing-Fix von Thema 1).
