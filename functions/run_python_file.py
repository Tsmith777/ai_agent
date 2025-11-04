import os, sys
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target.startswith(abs_work):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_target):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_target.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    cmd = [sys.executable, abs_target, *args]

    try:
        result = subprocess.run(
            cmd,
            cwd=abs_work,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if not result.stdout.strip() and not result.stderr.strip():
            return "No output produced."

        lines = [f"STDOUT: {result.stdout}", f"STDERR: {result.stderr}"]
        if result.returncode != 0: lines.append(f"Process exited with code {result.returncode}")
        return "\n".join(lines)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)