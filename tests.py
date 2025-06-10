from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for calc, lorem.txt, wait, this isn't...")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for calc, pkg/morelorem.txt, lorem ipsum dolor...")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for calc, tmp/temp.txt, this should not be allowed")
    print(result)



if __name__ == "__main__":
    test()
