import json
from pathlib import Path
from bs4 import BeautifulSoup


def fetch_website_contents(_url=None):
    """
    For this project:
    - ignore url
    - load latest YC-rendered HTML
    - extract top 30 companies
    - return JSON string
    """

    html_path = sorted(Path("data/raw").glob("rendered_*.html"))[-1]
    html = html_path.read_text(encoding="utf-8")

    soup = BeautifulSoup(html, "lxml")

    companies = []
    for a in soup.select("a[href^='/companies/']")[:30]:
        text = " ".join(a.get_text(" ", strip=True).split())

        companies.append({
            "text": text,
            "url": "https://www.ycombinator.com" + a["href"]
        })

    return json.dumps(companies, indent=2)
