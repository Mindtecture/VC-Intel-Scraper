import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

DEFAULT_URL = "https://www.ycombinator.com/companies"

def fetch_rendered_html(url: str, wait_ms: int = 2500) -> str:
    """ Fetch fully-rendered HTML using Playwright (JS Executed)."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        page.wait_for_timeout(wait_ms)  # simple, reliable for step 1

        # wait for the select
        page.wait_for_selector("select", timeout=15_000)

        # select by visible label
        page.select_option("select", label="Launch Date")

        # wait for resort
        page.wait_for_timeout(2000)

        # OPTIONAL: ensure companies loaded
        page.wait_for_selector("a[href^='/companies/']", timeout=10_000)

        html = page.content()
        title = page.title()
        print(f"Loaded: {title}")

        browser.close()
        return html

def main():
    url = os.getenv("TARGET_URL", DEFAULT_URL)

    html = fetch_rendered_html(url)

    out_dir = Path("data/raw")
    out_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = out_dir / f"rendered_{stamp}.html"
    out_path.write_text(html, encoding="utf-8")

    print(f"Saved rendered HTML to: {out_path}")

if __name__ == "__main__":
    main()
