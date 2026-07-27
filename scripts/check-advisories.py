#!/usr/bin/env python3
"""Maintenance checks for the advisory citations in this repository.

Three independent checks, all read-only:

  identifiers  Repository-hosted advisory citations that have since reached the
               GitHub Advisory Database, and any CVE identifier assigned to
               them. These are the citations that need updating.
  kev          Cited CVE identifiers that appear in the CISA Known Exploited
               Vulnerabilities catalog.
  links        HTTP status of every external URL cited in the Markdown files.

Usage:
  python3 scripts/check-advisories.py                 # identifiers + kev
  python3 scripts/check-advisories.py --links         # add the link check
  python3 scripts/check-advisories.py --epss          # add EPSS scores
  python3 scripts/check-advisories.py --all

Requires only the Python standard library. Set GITHUB_TOKEN to raise the
GitHub API rate limit from 60 to 5000 requests per hour.

Exit status is 1 when a citation needs updating, otherwise 0. The KEV, EPSS,
and link results are reported for review and do not affect exit status unless
a link is broken.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent

REPO_ADVISORY = re.compile(
    r"https://github\.com/([\w.-]+/[\w.-]+)/security/advisories/(GHSA-[\w-]+)"
)
GLOBAL_ADVISORY = re.compile(r"https://github\.com/advisories/(GHSA-[\w-]+)")
CVE_ID = re.compile(r"CVE-\d{4}-\d{4,7}")
URL = re.compile(r"https?://[^\s)\]<>\"']+")

KEV_FEED = (
    "https://www.cisa.gov/sites/default/files/feeds/"
    "known_exploited_vulnerabilities.json"
)
EPSS_API = "https://api.first.org/data/v1/epss?cve="

UA = "mf-top-10-maintenance-check"


def markdown_files() -> list[pathlib.Path]:
    files = sorted(ROOT.glob("*.md")) + sorted(ROOT.glob("risks/*.md"))
    return [f for f in files if f.is_file()]


def fetch_json(url: str, headers: dict[str, str] | None = None, timeout: int = 30):
    request = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def github_headers() -> dict[str, str]:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def collect() -> tuple[dict[str, list[str]], set[str], dict[str, list[str]]]:
    """Return repo-hosted GHSA citations, cited CVE ids, and all URLs."""
    repo_hosted: dict[str, list[str]] = {}
    cves: set[str] = set()
    urls: dict[str, list[str]] = {}

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        for _repo, ghsa in REPO_ADVISORY.findall(text):
            repo_hosted.setdefault(ghsa, []).append(rel)
        cves.update(CVE_ID.findall(text))
        for url in URL.findall(text):
            url = url.rstrip(".,;")
            # Prose uses placeholder forms such as `github.com/advisories/GHSA-…`;
            # a real URL is ASCII, so this skips them without a special case.
            if not url.isascii():
                continue
            urls.setdefault(url, []).append(rel)

    return repo_hosted, cves, urls


def check_identifiers(repo_hosted: dict[str, list[str]]) -> int:
    print(f"== identifiers ({len(repo_hosted)} repository-hosted citations)")
    if not repo_hosted:
        print("   none")
        return 0

    stale = 0
    for ghsa, files in sorted(repo_hosted.items()):
        try:
            advisory = fetch_json(
                f"https://api.github.com/advisories/{ghsa}", github_headers()
            )
        except urllib.error.HTTPError as error:
            if error.code == 404:
                print(f"   {ghsa}  not yet in the Advisory Database — citation is current")
                continue
            print(f"   {ghsa}  API error {error.code} — recheck manually")
            continue
        except urllib.error.URLError as error:
            print(f"   {ghsa}  unreachable ({error.reason}) — recheck manually")
            continue

        stale += 1
        cve = advisory.get("cve_id")
        print(f"   {ghsa}  NOW IN ADVISORY DATABASE — update {', '.join(sorted(set(files)))}")
        print(f"       url   -> https://github.com/advisories/{ghsa}")
        if cve:
            print(f"       label -> {cve}")
        else:
            print("       label -> keep the GHSA identifier (still no CVE assigned)")

    return stale


def check_kev(cves: set[str]) -> None:
    print(f"\n== kev ({len(cves)} cited CVE identifiers)")
    try:
        kev = fetch_json(KEV_FEED, timeout=60)
    except (urllib.error.URLError, urllib.error.HTTPError) as error:
        print(f"   catalog unreachable ({error}) — skipped")
        return

    listed = {entry["cveID"]: entry for entry in kev["vulnerabilities"]}
    hits = sorted(cves & listed.keys())
    print(f"   catalog {kev.get('catalogVersion')}, {len(listed)} entries")
    if not hits:
        print("   no cited CVE appears in the catalog")
        return
    for cve in hits:
        entry = listed[cve]
        ransomware = entry.get("knownRansomwareCampaignUse", "Unknown")
        print(
            f"   {cve}  IN KEV  added {entry['dateAdded']}  "
            f"ransomware use: {ransomware}"
        )
    print("   confirm each is still described accurately in the risk pages")


def check_epss(cves: set[str]) -> None:
    print(f"\n== epss ({len(cves)} cited CVE identifiers)")
    scores: dict[str, tuple[float, float]] = {}
    ordered = sorted(cves)
    for start in range(0, len(ordered), 50):
        batch = ordered[start : start + 50]
        try:
            payload = fetch_json(EPSS_API + ",".join(batch))
        except (urllib.error.URLError, urllib.error.HTTPError) as error:
            print(f"   API unreachable ({error}) — skipped")
            return
        for row in payload.get("data", []):
            scores[row["cve"]] = (float(row["epss"]), float(row["percentile"]))

    if not scores:
        print("   no scores returned")
        return
    print(f"   {len(scores)} of {len(cves)} scored (unscored ones are usually too recent)")
    for cve, (epss, percentile) in sorted(scores.items(), key=lambda i: -i[1][0]):
        print(f"   {cve}  epss={epss:.5f}  percentile={percentile:.3f}")


def check_links(urls: dict[str, list[str]]) -> int:
    print(f"\n== links ({len(urls)} distinct URLs)")

    def status(url: str) -> tuple[str, int | str]:
        for method in ("HEAD", "GET"):
            request = urllib.request.Request(
                url, method=method, headers={"User-Agent": UA}
            )
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    return url, response.status
            except urllib.error.HTTPError as error:
                # Some hosts answer HEAD with an error but serve GET correctly.
                if method == "HEAD" and error.code in (400, 403, 404, 405, 429, 501):
                    continue
                return url, error.code
            except urllib.error.URLError as error:
                return url, str(error.reason)
            except Exception as error:  # malformed URL, TLS failure, decoding issue
                return url, f"{type(error).__name__}: {error}"
        return url, "unknown"

    # 401/403/429 usually mean bot protection or rate limiting rather than a dead
    # link, so they are reported for a human to open but do not fail the run.
    blocked_codes = {401, 403, 429}
    broken = 0
    blocked = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for url, result in sorted(pool.map(status, urls), key=lambda r: str(r[0])):
            if result == 200:
                continue
            cited = ", ".join(sorted(set(urls[url])))
            if result in blocked_codes:
                blocked += 1
                print(f"   {result}  {url}")
                print(f"       likely bot protection — open it by hand ({cited})")
            else:
                broken += 1
                print(f"   {result}  {url}")
                print(f"       cited in {cited}")

    if not broken and not blocked:
        print("   all URLs returned 200")
    elif not broken:
        print(f"   no broken links; {blocked} URL(s) refused an automated request")
    return broken


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--links", action="store_true", help="check external URLs")
    parser.add_argument("--epss", action="store_true", help="report EPSS scores")
    parser.add_argument("--all", action="store_true", help="run every check")
    args = parser.parse_args()

    repo_hosted, cves, urls = collect()

    stale = check_identifiers(repo_hosted)
    check_kev(cves)
    if args.epss or args.all:
        check_epss(cves)
    broken = check_links(urls) if args.links or args.all else 0

    print()
    if stale:
        print(f"{stale} citation(s) need updating — see the identifiers section above")
    if broken:
        print(f"{broken} link(s) did not return 200")
    if not stale and not broken:
        print("nothing to update")

    return 1 if (stale or broken) else 0


if __name__ == "__main__":
    sys.exit(main())
