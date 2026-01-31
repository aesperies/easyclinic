import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("PERPLEXITY_API_KEY")

if not API_KEY:
    raise RuntimeError("Falta PERPLEXITY_API_KEY en .env")

def ask_perplexity(question: str):
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-5.1-mini",
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    resp = requests.post(url, json=data, headers=headers)
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    print(content)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python src/main.py \"tu pregunta\"")
        raise SystemExit(1)
    question = " ".join(sys.argv[1:])
    ask_perplexity(question)
