from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print("Result for calc, main.py")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for calc, tests.py")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for calc, ../main.py, this should not be allowed")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for calc, nonexistent.py, this should not be allowed")
    print(result)



if __name__ == "__main__":
    test()
