import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    user_prompt = sys.argv[1] if len(sys.argv) > 1 else None
    if not user_prompt:
        print("Usage: python main.py '<your prompt>'")
        sys.exit(1)
        
    is_verbose = False
    if len(sys.argv) > 1 and "--verbose" in sys.argv[2:]:
        is_verbose = True

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if is_verbose:
        print(
            f"User prompt: {user_prompt}\n" +
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n" +
            f"Response tokens: {response.usage_metadata.candidates_token_count}"
        )


if __name__ == "__main__":
    main()
