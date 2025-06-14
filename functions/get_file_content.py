import os
from google.genai import types
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    # the next few lines checks if the file path is within the working directory by finding the abs path for the working directory
    # and the file_path joined to the working directory
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # if not, return an error
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # if not a file, return an error
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # actually do the task of reading the file up to the max amount of chars
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if len(content) == MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    # if any error happens to occur, make sure we return it as a descriptive string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


# this is the variable that actually lets the LLM know that this can call the function
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content", # how to call the module

    # a way for the LLM to know how the module works through the description
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    
    # the parameters given to the LLM and the schemas to understand how each parameter is laid out
    parameters=types.Schema(
        type=types.Type.OBJECT, # the module is an object, so we let the LLM know so
        
        # their properties associated with the parameters, ie the filepath
        properties={
            "file_path": types.Schema( # the name of the property and letting the LLM know its schema
                type=types.Type.STRING, #file is of type string
                description="The path to the file whose content should be read, relative to the working directory.", #what file path is
            ),
        },

        # lets the LLM know that the function absolutely required a 'file_path' as mentioned within the parameters
        required=["file_path"],
    ),
)
