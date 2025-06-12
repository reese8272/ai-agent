import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

text = "I'M JUST A ROBOT"
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

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

    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,properties={
                "directory": types.Schema(
                    type=types.Type.STRING,description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs the specified python file and outputs any stdout and stderr given constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,description="The file path to run the python file from, relative to the working directory. If not provided, defaults to the main working directory.",
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads a given file, and will return the first 10,000 characters from that file.",
        parameters=types.Schema(
            type=types.Type.OBJECT,properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,description="Path to the file to read, relative to the working directory. Returns an error if not provided or if the file doesn't exist.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Either overwrites or creates a new file to be written into.",
        parameters=types.Schema(
            type=types.Type.OBJECT,properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,description="The file path to write the new file in, relative to the working directory. Returns an error if not provided.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,description="The content that is to be written to the file path.",
                )
            },
        ),
    )
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]   
    )

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt))

    if verbose:
        print(f"User prompt: {prompt}")
    if response.function_calls:
        print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
    else:
        print(response.text)
    if verbose:
        print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
        print(f'Response tokens: {response.usage_metadata.candidates_token_count}')

if __name__ == "__main__":
    main()