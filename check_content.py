#!/usr/bin/env python3
"""Content check: for every unique offer URL, fetch the page and look for
student/discount/free keywords. Flags pages where the offer terms seem absent.
"""
import json
import re
import concurrent.futures
from pathlib import Path

import requests

UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
}
KW = re.compile(
    r"student|education|edu\b|university|academic|campus|school|discount|free|"
    r"étudiant|étudiants|scolaire|gratuit|tarif réduit|jeune",
    re.I,
)

report = json.loads(Path("link_report.json").read_text(encoding="utf-8"))
urls = sorted({o["url"] for o in report if o["status"] and 200 <= o["status"] < 400})
print(f"{len(urls)} reachable urls to content-check")


def probe(url):
    try:
        r = requests.get(url, headers=UA, timeout=15)
        text = re.sub(r"<[^>]+>", " ", r.text)
        text = re.sub(r"\s+", " ", text)[:200000]
        hits = set(m.group(0).lower() for m in KW.finditer(text))
        return url, r.status_code, sorted(hits), len(r.text)
    except Exception as e:
        return url, -1, [], str(e)[:80]


out = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    for url, status, hits, size in ex.map(probe, urls):
        out[url] = {"status": status, "keywords": hits, "size": size}
        flag = "" if hits else "  <-- NO student/free keywords"
        if not hits:
            print(f"[{status}] {url} size={size}{flag}")

Path("content_report.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
empty = [u for u, v in out.items() if not v["keywords"]]
print(f"\n{len(empty)}/{len(urls)} pages with no student/free keywords")
