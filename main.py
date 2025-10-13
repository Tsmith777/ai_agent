import os
import sys
from dotenv import load_dotenv

def main():
    if len(sys.argv) == 1:
        print("Error: missing prompt. Usage: uv run main.py \"your prompt here\"", file =sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    from google import genai
    client = genai.Client(api_key=api_key)

    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents= prompt,
    )
    print(resp.text)
    print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {resp.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
