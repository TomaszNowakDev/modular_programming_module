def read(file_name):
    source_file = open(f"{file_name}"+".txt", "r")
    contents = source_file.read()
    print(contents.upper())


read(input("What is name of the file? (it is 'test') -> "))
