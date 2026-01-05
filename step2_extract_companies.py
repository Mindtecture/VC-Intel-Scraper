from bs4 import BeautifulSoup
from pathlib import Path
import json

def extract_companies(html: str, limit: int = 30):
    soup = BeautifulSoup(html, "lxml")

    companies = []
    for a in soup.select("a[href^='/companies/']")[:limit]:
        name= a.get_text(" ", strip=True)
        url = "https://www.ycombinator.com" + a["href"]

        companies.append({
            "name": name,
            "url": url
        })

    return companies

def main():
    # load latest rendered html
    html_path = sorted(Path("data/raw").glob("rendered_*.html"))[-1]
    html = html_path.read_text(encoding="utf-8")

    companies = extract_companies(html)

    out = Path("data/companies_latest.json")
    out.write_text(json.dumps(companies, indent=2), encoding="utf-8")

    print(f"Saved {len(companies)} companies → {out}")


if __name__ == "__main__":
    main()
