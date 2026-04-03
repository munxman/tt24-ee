#!/usr/bin/env python3
"""
IndexNow Sitemap Submission Script — tt24.ee
=============================================
Parses sitemap.xml and submits all URLs to IndexNow (Bing, Yandex,
DuckDuckGo, Naver, Seznam, Yep — all via a single API call).

Usage:
    python3 submit_indexnow.py

Environment variables:
    INDEXNOW_KEY   — Your IndexNow API key (required)
    SITEMAP_URL    — Sitemap URL (default: https://tt24.ee/sitemap.xml)

Setup:
    1. Generate a key:  openssl rand -hex 16
    2. Create a file named {key}.txt containing just the key
    3. Upload that file to https://tt24.ee/{key}.txt  (commit to repo root)
    4. Set INDEXNOW_KEY as a GitHub Actions secret
    5. Run this script after each deployment

Dependencies:
    pip install requests lxml
"""

import os
import sys
import json
import requests
from xml.etree import ElementTree

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
INDEXNOW_KEY  = os.environ.get("INDEXNOW_KEY", "")
SITE_HOST     = "tt24.ee"
SITEMAP_URL   = os.environ.get("SITEMAP_URL", "https://tt24.ee/sitemap.xml")
INDEXNOW_API  = "https://api.indexnow.org/indexnow"
KEY_LOCATION  = f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt"
BATCH_SIZE    = 10_000  # IndexNow max per request

SITEMAP_NS = {
    "sm":  "http://www.sitemaps.org/schemas/sitemap/0.9",
    "si":  "http://www.sitemaps.org/schemas/sitemap-index/0.9",
}


def validate_config():
    if not INDEXNOW_KEY:
        print("ERROR: INDEXNOW_KEY environment variable is not set.")
        print("Generate one: openssl rand -hex 16")
        sys.exit(1)
    if len(INDEXNOW_KEY) < 8 or len(INDEXNOW_KEY) > 128:
        print(f"ERROR: INDEXNOW_KEY must be 8–128 chars. Got {len(INDEXNOW_KEY)} chars.")
        sys.exit(1)


def parse_sitemap(sitemap_url: str) -> list[str]:
    """Recursively parse sitemap (handles sitemap index files too)."""
    print(f"Fetching: {sitemap_url}")
    try:
        resp = requests.get(sitemap_url, timeout=30)
        resp.raise_for_status()
    except Exception as e:
        print(f"ERROR: Could not fetch sitemap: {e}")
        sys.exit(1)

    root = ElementTree.fromstring(resp.content)
    tag = root.tag

    urls = []

    # Sitemap index (contains <sitemap> children)
    if "sitemapindex" in tag:
        for sitemap in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            child_urls = parse_sitemap(sitemap.text.strip())
            urls.extend(child_urls)
    else:
        # Regular sitemap — extract <loc> tags
        for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
            url = loc.text.strip()
            if url:
                urls.append(url)

    return urls


def verify_key_file() -> bool:
    """Check that the key file is accessible at the expected URL."""
    key_url = f"https://{SITE_HOST}/{INDEXNOW_KEY}.txt"
    print(f"Verifying key file at: {key_url}")
    try:
        resp = requests.get(key_url, timeout=10)
        if resp.status_code == 200 and INDEXNOW_KEY in resp.text:
            print("✅ Key file verified successfully")
            return True
        else:
            print(f"⚠️  Key file issue — status: {resp.status_code}, content: {resp.text[:100]!r}")
            print("   Make sure you committed {key}.txt to your repo root.")
            return False
    except Exception as e:
        print(f"⚠️  Could not verify key file: {e}")
        return False


def submit_urls(urls: list[str]) -> bool:
    """Submit URLs to IndexNow in batches."""
    total = len(urls)
    print(f"\nSubmitting {total} URLs to IndexNow...")

    success = True
    for i in range(0, total, BATCH_SIZE):
        batch = urls[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (total + BATCH_SIZE - 1) // BATCH_SIZE

        payload = {
            "host":        SITE_HOST,
            "key":         INDEXNOW_KEY,
            "keyLocation": KEY_LOCATION,
            "urlList":     batch,
        }

        print(f"  Batch {batch_num}/{total_batches}: {len(batch)} URLs...", end=" ")

        try:
            resp = requests.post(
                INDEXNOW_API,
                json=payload,
                headers={"Content-Type": "application/json; charset=utf-8"},
                timeout=30,
            )

            if resp.status_code in (200, 202):
                print(f"✅ HTTP {resp.status_code}")
            elif resp.status_code == 422:
                print(f"❌ HTTP 422 (validation error) — check key and URLs")
                print(f"     Response: {resp.text[:200]}")
                success = False
            elif resp.status_code == 429:
                print(f"⏳ HTTP 429 (rate limited) — try again later")
                success = False
            else:
                print(f"⚠️  HTTP {resp.status_code}")
                print(f"     Response: {resp.text[:200]}")

        except Exception as e:
            print(f"❌ Request failed: {e}")
            success = False

    return success


def main():
    validate_config()

    # Verify key file is accessible
    verify_key_file()

    # Parse sitemap(s)
    urls = parse_sitemap(SITEMAP_URL)
    print(f"\nFound {len(urls)} URLs in sitemap")

    if not urls:
        print("No URLs found — nothing to submit.")
        sys.exit(0)

    # Submit to IndexNow
    success = submit_urls(urls)

    if success:
        print(f"\n✅ Done! {len(urls)} URLs submitted to Bing, Yandex, DuckDuckGo, and others.")
    else:
        print("\n⚠️  Some submissions failed. Check errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
