import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    # we get the abspath of the working directory
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir # initialize a target directory with the abspath of the working dir

    # checks if there is a directory to be added, if not, the working directory is the default directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory)) # join the paths, and find the TRUE abs_path of the dir
    if not target_dir.startswith(abs_working_dir): # ensuring the dir actually lies within the working dir
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir): # making sure that the directory is actually a directory with the isdir method
        return f'Error: "{directory}" is not a directory'
    

    try:
        files_info = []
        for filename in os.listdir(target_dir): # now that our target lists our abs directory, list the contents
            filepath = os.path.join(target_dir, filename) # get the file and its path
            is_dir = os.path.isdir(filepath) # know if it's a dir or not
            file_size = os.path.getsize(filepath) # get the size
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}" # append the filename, size, and if it's a dir to the info
            )
        return "\n".join(files_info) # at the end, separate our findings with a newline
    except Exception as e: # if any unexpected errors occur, make sure to return that error as a string
        return f"Error listing files: {e}"


# variable that allows our LLM to know that this function is callable
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info", # name of the module
    
    # description of what the module does
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema( # the blueprints for our parameters
        type=types.Type.OBJECT, # our parameters are structured as objects (for ease of argument passing and assignment)
        properties={
            "directory": types.Schema( # our properties has one variable that is a directory and here are it's blueprints
                type=types.Type.STRING, # it is supposed to be of type string

                # the description of what the directory is
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
