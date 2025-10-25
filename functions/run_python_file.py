import os, sys
import subprocess

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