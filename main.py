import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = """
You are a venture analyst.
Your job is to analyze early-stage startups and extract patterns, themes, and signals.
Focus on trends, not descriptions.
Be concise, analytical, and business-oriented.
"""

user_prompt_prefix = """
Here is a list of newly launched Y Combinator companies.

Tasks:
1. Identify the top 3–5 dominant themes or trends.
2. Highlight repeated keywords or industries.
3. Infer what YC is prioritizing.
4. Mention one non-obvious insight.

Return:
- Headline
- Bullet points (max 6)
- One forward-looking insight

Data:
"""

def run():
    data = fetch_website_contents()

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt_prefix + data},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    run()
