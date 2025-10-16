from functions.get_files_info import get_files_info

def show(label, wd, dir_):
    print(label)
    result = get_files_info(wd, dir_)
    if result.startswith("Error:"):
        print(f"    {result}")
    else:
        for line in result.splitlines():
            print(f"    {line}")

if __name__ == "__main__":
    show("Result for current directory:", "calculator", ".")
    show("Result for 'pkg' directory:", "calculator", "pkg")
    show("Result for '/bin' directory:", "calculator", "/bin")
    show("Result for '../' directory:", "calculator", "../")