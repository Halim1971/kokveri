import os
from datetime import date
from xml.sax.saxutils import escape

from flask import Flask, Response, render_template


app = Flask(__name__)
SITE_BASE_URL = os.environ.get("SITE_BASE_URL", "https://kokveri.com.tr").strip().rstrip("/")
NO_CACHE_HEADERS = {
    "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0",
}


def canonical_url(path="/"):
    if not path.startswith("/"):
        path = f"/{path}"
    return f"{SITE_BASE_URL}{path}"


def sitemap_url_entry(loc, lastmod, changefreq="weekly", priority="1.00"):
    return (
        "  <url>\n"
        f"    <loc>{escape(loc)}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        "  </url>"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sitemap.xml")
def sitemap_xml():
    today = date.today().isoformat()
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + sitemap_url_entry(canonical_url("/"), today)
        + "\n</urlset>\n"
    )
    return Response(xml, content_type="application/xml; charset=UTF-8", headers=NO_CACHE_HEADERS)


@app.route("/robots.txt")
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {canonical_url('/sitemap.xml')}\n"
    )
    return Response(content, content_type="text/plain; charset=UTF-8", headers=NO_CACHE_HEADERS)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5058"))
    app.run(host="0.0.0.0", port=port, debug=True)
