from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def show(wd, fp, content):
    result = write_file(wd, fp, content)
    if result.startswith("Error:"):
        print(f"    {result}")
    else:
        for line in result.splitlines():
            print(f"    {line}")

if __name__ == "__main__":
    show("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    show("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    show("calculator", "/tmp/temp.txt", "this should not be allowed")