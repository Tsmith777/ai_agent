import os
import sys
from dotenv import load_dotenv

def main():
    system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
    model_name = "gemini-2.0-flash-001"

    args = sys.argv[1:]
    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")

    if len(args) > 0:
        user_prompt = args[0]
    else:
        print("Error: missing prompt. Usage: uv run main.py \"your prompt here\"", file =sys.stderr)
        sys.exit(1)

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model = model_name,
        contents = messages,
        config = types.GenerateContentConfig(system_instruction=system_prompt),
    )
    print(response.text)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
