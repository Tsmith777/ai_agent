from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def show(wd, fp):
    result = get_file_content(wd, fp)
    if result.startswith("Error:"):
        print(f"    {result}")
    else:
        for line in result.splitlines():
            print(f"    {line}")

if __name__ == "__main__":
    show("calculator", "main.py")
    show("calculator", "pkg/calculator.py")
    show("calculator", "/bin/cat")
    show("calculator", "pkg/does_not_exist.py")