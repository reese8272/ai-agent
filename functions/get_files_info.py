import os

def get_files_info(working_directory, directory=None):
    abs_working = os.path.abspath(working_directory)
    abs_dir = os.path.abspath(directory)
    common_path = os.path.commonpath([working_directory, abs_dir])
    if common_path != abs_working:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if common_path is None:
        return f'Error: "{directory}" is not a directory'