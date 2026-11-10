#!/usr/bin/env python3
"""Extract every markdown link from the repo's .md files and check HTTP status.

Usage: python check_links.py [--content]   (--content = also fetch page text and
look for student keywords)
Writes link_report.json + prints a summary.
"""
import json
import re
import sys
import concurrent.futures
from pathlib import Path

import requests

ROOT = Path(__file__).parent
UA = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
}
LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")

# skip "search X" / local references that aren't URLs — already only http(s)
def extract():
    items = []
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for m in LINK_RE.finditer(line):
                items.append({
                    "file": str(md.relative_to(ROOT)).replace("\\", "/"),
                    "line": lineno,
                    "text": m.group(1),
                    "url": m.group(2).rstrip(".,;"),
                    "row": line.strip()[:200],
                })
    return items


def check(item):
    url = item["url"]
    try:
        # HEAD first — many CDNs accept it; fall back to GET on 4xx/405
        r = requests.head(url, headers=UA, timeout=15, allow_redirects=True)
        if r.status_code in (403, 404, 405, 406, 429) or r.status_code >= 500:
            r = requests.get(url, headers={**UA, "Range": "bytes=0-4096"}, timeout=15, allow_redirects=True, stream=True)
        return {**item, "status": r.status_code, "final": str(r.url)}
    except requests.exceptions.SSLError as e:
        return {**item, "status": -1, "error": f"SSL: {e}"}
    except requests.exceptions.ConnectionError as e:
        return {**item, "status": -2, "error": f"CONN: {str(e)[:120]}"}
    except requests.exceptions.Timeout:
        return {**item, "status": -3, "error": "TIMEOUT"}
    except Exception as e:
        return {**item, "status": -9, "error": f"{type(e).__name__}: {str(e)[:120]}"}


def main():
    items = extract()
    print(f"Extracted {len(items)} links ({len(set(i['url'] for i in items))} unique)")
    uniq = {}
    for it in items:
        uniq.setdefault(it["url"], []).append(it)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:
        futs = {ex.submit(check, {"url": u}): u for u in uniq}
        for f in concurrent.futures.as_completed(futs):
            u = futs[f]
            try:
                results[u] = f.result()
            except Exception as e:
                results[u] = {"url": u, "status": -9, "error": str(e)}
    out = []
    for it in items:
        r = results[it["url"]]
        out.append({**it, "status": r.get("status"), "final": r.get("final"), "error": r.get("error")})
    Path("link_report.json").write_text(json.dumps(out, indent=1), encoding="utf-8")

    bad = [o for o in out if o["status"] and (o["status"] >= 400 or o["status"] < 0)]
    seen = set()
    print(f"\n{len(bad)} suspicious link occurrences:")
    for o in bad:
        k = (o["url"], o["status"])
        if k in seen:
            continue
        seen.add(k)
        print(f"  [{o['status']}] {o['url']}  ({o['file']}:{o['line']}) {o.get('error','')}")
    ok = len(out) - len(bad)
    print(f"\nOK: {ok} / {len(out)}")


if __name__ == "__main__":
    main()
