import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def query_llm(prompt: str) -> str:
    if USE_MOCK:
        return mock_response(prompt)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"GPT-4 error — falling back to mock:\n{e}")
        return mock_response(prompt)


def mock_response(prompt: str) -> str:
    field = prompt.split(":")[-1].strip().strip("'\"")
    return f"(Mocked GPT-4 response for '{field}')"
