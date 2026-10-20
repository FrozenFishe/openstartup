#!/usr/bin/env python3
"""Check every URL in data/openstartup.json and write research/link_report.json.

Statuses:
  ok       2xx/3xx with a real page
  blocked  401/403/406/429/503: bot walls on sites that are usually alive
  dead     404/410, DNS failure, connection refused, timeout
  parked   page looks like a parked or for-sale domain
Needs curl. Run after build.py; takes a few minutes.
"""
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data" / "openstartup.json"
OUT = BASE / "research" / "link_report.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
PARKED = re.compile(r"domain (is )?for sale|buy this domain|this domain (may be|is) for sale|hugedomains|sedo\.com|dan\.com/|parkingcrew|bodis\.com|account suspended|domain has expired", re.I)


def check(url):
    try:
        r = subprocess.run(["curl", "-sL", "-m", "25", "--max-redirs", "8", "-A", UA, "-o", "-",
                            "-w", "\n__META__%{http_code} %{url_effective}", url], capture_output=True, timeout=40)
    except subprocess.TimeoutExpired:
        return {"status": "dead", "code": "timeout"}
    body, _, meta = r.stdout.decode("utf-8", "ignore").rpartition("\n__META__")
    code, _, final = meta.partition(" ")
    if r.returncode in (6, 7, 28, 35, 60) or code == "000":
        return {"status": "dead", "code": f"curl {r.returncode}"}
    if PARKED.search(body[:20000]):
        return {"status": "parked", "code": code, "final": final}
    if code in ("404", "410"):
        return {"status": "dead", "code": code, "final": final}
    if code in ("401", "403", "406", "429", "503", "999", "520", "521", "522", "523", "525", "526"):
        return {"status": "blocked", "code": code}
    if code.startswith(("2", "3")):
        return {"status": "ok", "code": code, **({"final": final} if final.rstrip("/") != url.rstrip("/") else {})}
    return {"status": "other", "code": code}


def main():
    d = json.loads(DATA.read_text(encoding="utf-8"))
    where = {}
    for c in d["countries"]:
        for k in ("grants", "accelerators", "vcs", "pe", "resources"):
            for x in c[k]:
                if x["url"]:
                    where.setdefault(x["url"], []).append(f"{c['country']}/{k}/{x['name']}")
        for u in c["sources"]:
            where.setdefault(u, []).append(f"{c['country']}/sources")
    for k in ("accelerators", "resources"):
        for x in d["global"][k]:
            if x["url"]:
                where.setdefault(x["url"], []).append(f"global/{k}/{x['name']}")
    urls = sorted(where)
    with ThreadPoolExecutor(24) as ex:
        res = dict(zip(urls, ex.map(check, urls)))
    report = {"checked": d["built"], "results": {u: {**res[u], "used_by": where[u]} for u in urls}}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    print(len(urls), "urls:", dict(Counter(r["status"] for r in res.values())))


if __name__ == "__main__":
    main()
