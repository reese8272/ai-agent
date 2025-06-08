import os
from dotenv import load_dotenv
from google import genai
import sys

def respond(client, contents):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=contents
    )
    print(response.text)
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    


def main():
    load_dotenv()
    api_key = os.environ.get("GEMENI_API_KEY")
    client = genai.Client(api_key = api_key)
    prompt = sys.argv[1]
    respond(client, prompt)

if __name__ == "__main__":
    main()