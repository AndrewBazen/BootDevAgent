import os
import config

def get_file_content(working_directory, file_path):
    
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)
        
        if os.path.commonpath([full_path, abs_working_dir]) != abs_working_dir:
                return (
                    f'Error: Cannot read "{file_path}" as it is outside the permitted '
                    f'working directory'
                )
        if not os.path.isdir(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_path, "r") as f:            
            file_content_string = f.read(config.MAX_CHARS)
            
            if f.count() > config.MAX_CHARS:
                file_content_string.append(f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]')
    except Exception as e:
        return f'Error: {e}'