import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)

        if os.path.commonpath([full_path, abs_working_dir]) != abs_working_dir:
                    return (
                        f'Error: Cannot execute "{file_path}" as it is outside the permitted '
                        f'working directory'
                    )
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not f'{file_path}'.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        # Build the command list with python executable and the file path
        cmd = ["python", full_path] + args
        
        ran_process = subprocess.run(
            cmd,
            cwd=working_directory,
            timeout=30, 
            capture_output=True,
            text=True,
        )
        
        output = f'STDOUT: {ran_process.stdout}\n'
        
        if ran_process.returncode != 0:
            output = output + f'Process exited with code {ran_process.returncode}'
        else:
            output = output + f'No output produced'
            
        output = output + f'\n\nSTDERR: {ran_process.stderr}'
        
        return output
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    