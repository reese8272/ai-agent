from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    result = get_files_info({'directory': '.'})
    print(result)
    print("")

    result = get_files_info({'directory': 'pkg'})
    print(result)
    print("")



if __name__ == "__main__":
    test()
