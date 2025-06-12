import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)

    try:
        target_file = os.path.abspath(os.path.join(working_directory,file_path))
        if not target_file.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(target_file):
            return f'Error: File "{file_path}" not found.'
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        result = subprocess.run(['python3', file_path], cwd = abs_working_dir, timeout=30, text = True, capture_output=True)
        stdout = result.stdout
        stderr = result.stderr
        output = ''
        if stdout:
            output += f'STDOUT: {stdout} \n'
        if stderr:
            output += f'STDERR: {stderr}\n'
        if result.returncode != 0:
            output += f'Process exited with code {result.returncode}\n'
        if not output:
            return 'No output produced.'
        return output
    
    except Exception as e:
        return f'Error: executing Python file: {e}'