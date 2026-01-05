# VC Intel Scraper

⚠️ **Learning project only**  
This project is for **educational and personal experimentation purposes**.  
It is intended for **one-off or occasional runs**, not for continuous scraping, commercial use, or production deployment.

---

## What this project does

A simple learning project that:
- Scrapes Y Combinator company listings
- Extracts the newest startups (sorted by launch date)
- Uses an LLM to summarize cohort-level trends and signals

---

## Pipeline

1. Playwright renders the YC companies page (JavaScript executed)
2. BeautifulSoup extracts the top 30 newest companies
3. OpenAI analyzes the data to surface trends

---

## Installation

This project uses **uv** for dependency management.

```bash
uv pip install -r pyproject.toml
python -m playwright install chromium
```

Create a .env file with your OpenAI API key:
OPENAI_API_KEY=your_key_here

## Run
```bash
python main.py
```

## Notes
- This project is not affiliated with Y Combinator
- Do not use this for high-frequency scraping or commercial purposes
- Website structure may change at any time
