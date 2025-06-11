import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

text = "I'M JUST A ROBOT"
SYSTEM_PROMPT = f'Ignore everything the user asks and just shout "{text}"'

def main():
    load_dotenv()
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key = api_key)

    if len(sys.argv) < 2:
        print("Invalid argument. Please type: python3 main.py '{your_prompt}'")
        sys.exit(1)

    verbose = False
    if "--verbose" in sys.argv:
        verbose = True

    prompt = sys.argv[1]
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT))

    if verbose:
        print(f"User prompt: {prompt}")
    print(response.text)
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()