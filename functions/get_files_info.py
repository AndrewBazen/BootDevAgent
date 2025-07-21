import os

def get_files_info(working_directory, directory="."):
    try:
        # Resolve absolute paths to reliably compare directories, accounting for symbolic
        # links, ".." segments, and absolute paths that were passed in `directory`.
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        abs_working_dir = os.path.abspath(working_directory)

        # Check if the target directory is within (or equal to) the allowed working
        # directory. We use os.path.commonpath which is safer than simple string
        # prefix checks. If the common path between the two is not the working
        # directory, `directory` lies outside the permitted scope.
        if os.path.commonpath([full_path, abs_working_dir]) != abs_working_dir:
            return (
                f'Error: Cannot list "{directory}" as it is outside the permitted '
                f'working directory'
            )
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        header_message = ""
        if directory == ".":
            header_message = "Result for current directory:\n"
        else:
            header_message = f"Result for '{directory}' directory:\n"
        
        dir_contents = os.listdir(full_path)
        
        results = ""
        for item in dir_contents:
            item_path = os.path.join(full_path, item)
            results = results + f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}\n"
        
        built_response = header_message + results
        return built_response
    except Exception as e:
        return f'Error: {e}'