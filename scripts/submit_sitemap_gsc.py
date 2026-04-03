#!/usr/bin/env python3
"""
Google Search Console Sitemap Submission Script — tt24.ee
=========================================================
Submits sitemap.xml to Google Search Console via the Search Console API.
Requires a service account JSON key with Owner access to tt24.ee in GSC.

Usage:
    python3 submit_sitemap_gsc.py [--key path/to/service-account-key.json]

Environment variable alternative (preferred for CI):
    GSC_SERVICE_ACCOUNT_JSON=/path/to/key.json python3 submit_sitemap_gsc.py

Dependencies:
    pip install google-auth google-auth-httplib2 google-api-python-client
"""

import os
import sys
import json
import argparse
import urllib.parse

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SITE_URL     = "https://tt24.ee/"
SITEMAP_URL  = "https://tt24.ee/sitemap.xml"
SCOPES       = ["https://www.googleapis.com/auth/webmasters"]


def get_credentials(key_path: str):
    """Load service account credentials from a JSON key file."""
    try:
        from google.oauth2 import service_account
    except ImportError:
        print("ERROR: google-auth not installed.")
        print("Run: pip install google-auth google-auth-httplib2 google-api-python-client")
        sys.exit(1)

    if not os.path.exists(key_path):
        print(f"ERROR: Key file not found: {key_path}")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=SCOPES
    )
    return credentials


def submit_sitemap(credentials):
    """Submit sitemap.xml to Google Search Console."""
    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=credentials)

    print(f"Submitting sitemap: {SITEMAP_URL}")
    print(f"For site:           {SITE_URL}")

    try:
        service.sitemaps().submit(
            siteUrl=SITE_URL,
            feedpath=SITEMAP_URL
        ).execute()
        print("✅ Sitemap submitted successfully!")
    except Exception as e:
        print(f"❌ Submission failed: {e}")
        sys.exit(1)


def list_sitemaps(credentials):
    """List all sitemaps registered in GSC for verification."""
    from googleapiclient.discovery import build

    service = build("searchconsole", "v1", credentials=credentials)

    print(f"\nVerifying — listing sitemaps for {SITE_URL}:")
    result = service.sitemaps().list(siteUrl=SITE_URL).execute()
    sitemaps = result.get("sitemap", [])

    if not sitemaps:
        print("  (no sitemaps found — submission may still be pending)")
    for sm in sitemaps:
        status = "⏳ pending" if sm.get("isPending") else "✅ indexed"
        errors = sm.get("errors", 0)
        warnings = sm.get("warnings", 0)
        print(f"  {status} | {sm['path']}")
        print(f"           Submitted: {sm.get('lastSubmitted', 'unknown')}")
        print(f"           Errors: {errors} | Warnings: {warnings}")


def main():
    parser = argparse.ArgumentParser(description="Submit tt24.ee sitemap to Google Search Console")
    parser.add_argument(
        "--key",
        default=os.environ.get("GSC_SERVICE_ACCOUNT_JSON", "gsc-service-account-key.json"),
        help="Path to service account JSON key file (or set GSC_SERVICE_ACCOUNT_JSON env var)"
    )
    parser.add_argument(
        "--list-only",
        action="store_true",
        help="Only list current sitemaps, do not submit"
    )
    args = parser.parse_args()

    credentials = get_credentials(args.key)

    if not args.list_only:
        submit_sitemap(credentials)

    list_sitemaps(credentials)


if __name__ == "__main__":
    main()
