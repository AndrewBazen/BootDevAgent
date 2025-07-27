import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)
        
        if os.path.commonpath([full_path, abs_working_dir]) != abs_working_dir:
            return (
                f'Error: Cannot write to "{file_path}" as it is outside the permitted '
                f'working directory'
            )

        with open(full_path, 'w') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
    
    