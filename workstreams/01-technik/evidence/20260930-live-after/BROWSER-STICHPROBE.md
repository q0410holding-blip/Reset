# Browser-Stichprobe Nachher (30.09.2026, ~09:20–09:40 UTC)

Nur lesend (GET), nichts eingegeben. Screenshots per Headless-Chrome über CDP (`cdp_shot.mjs`), zusätzlich im Browser-Pane gegengeprüft.

| Prüfung | Ergebnis | Beleg |
|---|---|---|
| `/abnehmprogramm-12-monate?utm_source=test#preise` | PASS: landet auf `https://abnehmen-mit-arzt.de/abnehmprogramm-6-monate/?utm_source=test#preise` (Query + Hash erhalten). Hinweis: Zielseite hat kein Element `id="preise"`, der Hash springt also nirgends hin. | `01-12monate-redirect-6s.png` |
| `/faq/` | PASS: FAQ-Seite (H1 „Häufige Fragen“), Footer enthält `+49 30 75435335` (zweimal, inkl. „Tel. +49 30 75435335“), alte Nummer nicht im Text. | `02-faq-desktop-ganzeSeite-6s.png`, `05-faq-mobil-6s.png` |
| `/funnel/cross/` | PASS: Funnel-Start lädt („Nimmst du aktuell eine Abnehmspritze?“ Ja/Nein), nichts geklickt. | `03-funnel-cross-start-6s.png`, `04-funnel-cross-mobil-6s.png` |
| Mobil 390 px `/abnehmspritze-kosten/` | PASS: keine horizontale Scrollleiste (scrollWidth = 390), Menü-Button + Sticky-CTA sichtbar. | `06-mobil-kosten-*.png` |

Nebenbefund (kein Blocker): Das initiale HTML enthält H1 und Intro (SEO ok), im Browser ist der Hero-Bereich während der Hydrierung aber ca. 1–3 s leer (H1 leer bei 1 s, voll bei 3 s, siehe `06-mobil-kosten-1s.png` vs. `-3s.png`).

Nebenbefund www: `http://www.` und `https://www.` laufen aktuell in einen Timeout. www zeigt per A-Record auf `89.31.143.90` (United-Domains-Weiterleitung); Port 80 und 443 dieser IP antworten nicht (`nc` Timeout). Vorher lieferte `http://www.` noch 301 → 200. www ist damit derzeit komplett unerreichbar (Teil B / RES-340).
