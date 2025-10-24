import os

def run_python_file(working_directory, file_path, args=[]):
    
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_target):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.endswith(abs_target):
        return f'Error: "{file_path}" is not a Python file.'