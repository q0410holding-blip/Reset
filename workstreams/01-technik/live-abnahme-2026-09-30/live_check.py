"""Read-only live check of the public site: GET/HEAD only, no forms, no tracking calls."""
import hashlib, http.client, json, re, socket, ssl, sys, time
from urllib.parse import urlsplit

ORIGIN = "abnehmen-mit-arzt.de"
PUBLIC = ["/", "/abnehmprogramm-6-monate/", "/fuer-arzte/", "/preisvergleich/", "/faq/",
          "/abnehmspritze-berlin/", "/abnehmspritze-kosten/", "/mounjaro-berlin/", "/wegovy-berlin/",
          "/abnehmzentrum-berlin/", "/abnehmspritze-nebenwirkungen/", "/abnehmspritze-ohne-diabetes/",
          "/abnehmspritze-verschreiben-lassen/", "/vergleich/", "/vergleich-juniper/", "/vergleich-voy/",
          "/vergleich-golighter/", "/vergleich-doktorabc/", "/vergleich-hausarzt/", "/impressum/",
          "/privacy/", "/support/"]
NO_SLASH = ["/faq", "/impressum", "/abnehmprogramm-6-monate"]
OLD_OFFER = ["/abnehmprogramm-12-monate", "/abnehmprogramm-12-monate/",
             "/abnehmprogramm-12-monate/index.html", "/abnehmprogramm-12-monate/?utm_source=test"]
SPA = ["/funnel/cross/", "/funnel/cross/angebot/", "/funnel/gesundheit/"]
ALIASES = ["/fuer-fachkreise/", "/so-funktionierts/"]
MISSING = ["/gibt-es-nicht-claude-check/", "/api/not-a-real-endpoint"]
FILES = ["/sitemap.xml", "/robots.txt", "/llms.txt"]
HOSTS = [("https", ORIGIN), ("http", ORIGIN), ("https", "www." + ORIGIN), ("http", "www." + ORIGIN),
         ("https", "goresetapp.com")]
HEADERS = ["Content-Type", "Cache-Control", "Strict-Transport-Security", "X-Robots-Tag", "Location"]


def fetch(scheme, host, path, method="GET", hops=5):
    chain = []
    for _ in range(hops):
        try:
            if scheme == "https":
                conn = http.client.HTTPSConnection(host, timeout=20, context=ssl.create_default_context())
            else:
                conn = http.client.HTTPConnection(host, timeout=20)
            conn.request(method, path, headers={"User-Agent": "AMITA-live-check/1.1 (read-only)"})
            resp = conn.getresponse()
            body = resp.read()
            hdrs = {h: resp.getheader(h) for h in HEADERS if resp.getheader(h)}
            chain.append({"url": f"{scheme}://{host}{path}", "status": resp.status, "headers": hdrs})
            conn.close()
            loc = resp.getheader("Location")
            if resp.status in (301, 302, 303, 307, 308) and loc:
                nxt = urlsplit(loc if "://" in loc else f"{scheme}://{host}{loc}")
                scheme, host = nxt.scheme, nxt.netloc
                path = (nxt.path or "/") + (f"?{nxt.query}" if nxt.query else "")
                continue
            return chain, resp, body
        except (ssl.SSLError, socket.error, http.client.HTTPException) as err:
            chain.append({"url": f"{scheme}://{host}{path}", "error": f"{type(err).__name__}: {err}"})
            return chain, None, b""
    return chain, None, b""


def meta(html, name):
    m = re.search(r'<meta\s+name="%s"\s+content="([^"]*)"' % name, html, re.I)
    return m.group(1) if m else None


def inspect(html):
    title = re.search(r"<title>([^<]*)</title>", html, re.I)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S)
    canon = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', html, re.I)
    refresh = re.search(r'<meta\s+http-equiv="refresh"\s+content="([^"]*)"', html, re.I)
    types = []
    for block in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
        try:
            data = json.loads(block)
            types.append(data.get("@type"))
        except ValueError:
            types.append("INVALID_JSON")
    flat = html.replace(" ", "")
    return {
        "title": title.group(1) if title else None,
        "h1": re.sub(r"<[^>]+>", "", h1.group(1)).strip() if h1 else None,
        "canonical": canon.group(1) if canon else None,
        "robots": meta(html, "robots"), "googlebot": meta(html, "googlebot"), "bingbot": meta(html, "bingbot"),
        "metaRefresh": refresh.group(1) if refresh else None,
        "jsonLdTypes": types,
        "oldPhone": "17631784538" in flat,
        "newPhone": "493075435335" in flat,
        "getresetapp": "getresetapp" in html,
        "has12MonthOffer": bool(re.search(r"137,71|12 Monate Abnehmprogramm|abnehmprogramm-12-monate", html)),
        "has50EuroAftercare": bool(re.search(r"50 Euro pro Monat", html)),
    }


def main():
    results = {"utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "checks": []}
    _, home_resp, home_body = fetch("https", ORIGIN, "/")
    home_hash = hashlib.sha256(home_body).hexdigest()
    groups = [("public", PUBLIC), ("noSlash", NO_SLASH), ("oldOffer", OLD_OFFER), ("spa", SPA),
              ("alias", ALIASES), ("missing", MISSING)]
    for group, paths in groups:
        for path in paths:
            for method in ("GET", "HEAD"):
                chain, resp, body = fetch("https", ORIGIN, path, method)
                entry = {"group": group, "path": path, "method": method, "chain": chain,
                         "finalStatus": resp.status if resp else None}
                if method == "GET" and resp is not None:
                    html = body.decode("utf-8", "replace")
                    entry.update(inspect(html))
                    entry["sha256"] = hashlib.sha256(body).hexdigest()
                    entry["identicalToHomepage"] = path != "/" and entry["sha256"] == home_hash
                results["checks"].append(entry)
    for path in FILES:
        chain, resp, body = fetch("https", ORIGIN, path)
        text = body.decode("utf-8", "replace")
        results["checks"].append({
            "group": "file", "path": path, "method": "GET", "chain": chain,
            "finalStatus": resp.status if resp else None,
            "sha256": hashlib.sha256(body).hexdigest(),
            "sitemapLocs": len(re.findall(r"<loc>", text)) if path.endswith(".xml") else None,
            "mentions12": "abnehmprogramm-12-monate" in text,
            "isHomepage": hashlib.sha256(body).hexdigest() == home_hash,
        })
    for scheme, host in HOSTS:
        chain, resp, body = fetch(scheme, host, "/abnehmspritze-kosten/?q=1")
        html = body.decode("utf-8", "replace")
        canon = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', html, re.I)
        results["checks"].append({"group": "host", "path": f"{scheme}://{host}/abnehmspritze-kosten/?q=1",
                                  "chain": chain, "finalStatus": resp.status if resp else None,
                                  "canonical": canon.group(1) if canon else None})
    pub = [c for c in results["checks"] if c["group"] == "public" and c["method"] == "GET"]
    results["summary"] = {
        "homepageSha256": home_hash,
        "publicOk": sum(1 for c in pub if c["finalStatus"] == 200),
        "publicTotal": len(pub),
        "homepageCopies": sum(1 for c in pub if c.get("identicalToHomepage")),
        "wrongCanonicals": sum(1 for c in pub if c.get("canonical") != f"https://{ORIGIN}{c['path']}"),
        "noindexOnPublic": sum(1 for c in pub if "noindex" in " ".join(filter(None, [c.get("robots"), c.get("googlebot"), c.get("bingbot")]))),
        "oldPhonePages": sum(1 for c in pub if c.get("oldPhone")),
        "getresetappPages": sum(1 for c in pub if c.get("getresetapp")),
        "offer12Pages": sum(1 for c in pub if c.get("has12MonthOffer")),
        "aftercare50Pages": sum(1 for c in pub if c.get("has50EuroAftercare")),
        "missingStatus": [c["finalStatus"] for c in results["checks"] if c["group"] == "missing" and c["method"] == "GET"],
    }
    json.dump(results, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
