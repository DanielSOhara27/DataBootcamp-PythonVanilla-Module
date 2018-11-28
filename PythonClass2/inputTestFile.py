file_name = "myfirstInputFile.txt"

with open(file_name, 'r') as text:
    print(text)
    lines = text.read()
    print(type(lines))
    print(lines)