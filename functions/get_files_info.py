import os

def get_files_info(working_directory, directory="."):
    try:
        abs_work = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_target.startswith(abs_work):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'
        
        lines = []
        for name in os.listdir(abs_target):
            p = os.path.join(abs_target, name)
            is_dir = os.path.isdir(p)
            size = os.path.getsize(p)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"