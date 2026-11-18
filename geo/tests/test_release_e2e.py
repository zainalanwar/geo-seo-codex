"""Release smoke test with real HTTP, helper processes and PDF rendering."""
import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from shutil import which
from subprocess import run
import sys
from threading import Thread

ROOT = Path(__file__).resolve().parents[1]


def output(*args):
    return run(args, capture_output=True, text=True, check=True, timeout=60).stdout


def test_site_to_pdf(tmp_path):
    site = tmp_path / "fixture"
    site.mkdir()
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=site))
    origin = f"http://127.0.0.1:{server.server_port}"
    (site / "index.html").write_text('<meta charset="utf-8"><title>Research — Demo</title>'
                                     '<h1>Research</h1><a href="/service.html">Research services</a>')
    (site / "service.html").write_text("<title>Buyer research</title><h1>Buyer interviews</h1>")
    (site / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {origin}/sitemap.xml\n")
    (site / "sitemap.xml").write_text(f"<urlset><url><loc>{origin}/service.html</loc></url></urlset>")
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        data = json.loads(output(sys.executable, ROOT / "scripts/fetch_page.py", origin, "full"))
        assert data["page"]["title"] == "Research — Demo"
        assert data["page"]["status_code"] == 200
        assert origin + "/service.html" in data["sitemap"]
        draft = json.loads(output(sys.executable, ROOT / "scripts/llmstxt_generator.py", origin, "generate"))
        for field in ("generated_llmstxt", "generated_llmstxt_full"):
            assert origin + "/service.html" in draft[field]
            assert "contact@" not in draft[field]
    finally:
        server.shutdown()
        server.server_close()
        thread.join()

    report = tmp_path / "sample audit.md"
    report.write_text(f"# Evidence\n\nObserved title: {data['page']['title']}\n")
    html = report.with_suffix(".html")
    pdf = report.with_suffix(".pdf")
    output("pandoc", report, "--standalone", "--embed-resources",
           "--template", ROOT / "templates/geo-report-template.html",
           "--css", ROOT / "templates/geo-report-style.css", "-M", "brand_name=Release Fixture",
           "-M", "title=Fixture audit", "-o", html)
    chrome = (os.environ.get("CHROME_BIN") or which("chromium") or which("google-chrome")
              or "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    output(chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
           f"--user-data-dir={tmp_path / 'profile'}", f"--print-to-pdf={pdf}", html.as_uri())
    result = output("pdftotext", pdf, "-")
    assert "Release Fixture" in result and "Research — Demo" in result
