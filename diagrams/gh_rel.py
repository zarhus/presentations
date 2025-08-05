#!/usr/bin/env python3
import argparse
import os
import sys
import requests


def fetch_releases(repo, token=None):
    """Yield release dictionaries from the GitHub API, handling pagination."""
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    page = 1
    while True:
        resp = requests.get(url, headers=headers,
                            params={"per_page": 100, "page": page}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        for release in data:
            yield release
        page += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print download counts for every release in a GitHub repository")
    parser.add_argument("repo", help="repository in the form owner/name")
    parser.add_argument("--token", help="GitHub personal access token "
                                        "(or set GITHUB_TOKEN)")
    parser.add_argument("--per-asset", action="store_true",
                        help="show counts for each asset as well")
    args = parser.parse_args()

    token = args.token or os.getenv("GITHUB_TOKEN")
    try:
        for rel in fetch_releases(args.repo, token):
            tag = rel.get("tag_name") or rel.get("name") or "<no-tag>"
            assets = rel.get("assets", [])
            total = sum(asset.get("download_count", 0) for asset in assets)
            print(f"{tag}: {total} downloads")
            if args.per_asset:
                for asset in assets:
                    name = asset.get("name", "<unnamed>")
                    count = asset.get("download_count", 0)
                    print(f"  {name}: {count}")
    except requests.HTTPError as e:
        sys.exit(f"GitHub API error: {e.response.status_code} {e.response.reason}")
    except requests.RequestException as e:
        sys.exit(f"Network error: {e}")


if __name__ == "__main__":
    main()

