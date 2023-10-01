import os
import sys
print(sys.path)


print(__file__)

try:
    import mommod
except ImportError:
    print("Didn’t work first time")
else:
    print("Worked first time")
sys.path.pop(0)
try:
    import homework_013
except ImportError:
    print("Didn’t work second time")
else:
    print("Worked second time")

working_directory = os.path.dirname(os.path.realpath(__file__))
file_object = open("temp.txt", "r+")
file_object.close()

def count_lines(name):
    lines = 0
    with open("temp.txt", 'r') as file:
        for count, line in enumerate(file):
            pass
    lines = count + 1
    return lines
print("Number of lines:", count_lines(name=1))

def count_chars(name):
    try:
        with open("temp.txt", 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return -1
print("Number of characters", count_chars(name=1))

def test(name):
    line_count = count_lines(name=1)
    char_count = count_chars(name=1)
    if line_count != -1 and char_count != -1:
        print(f"File '{name}' has {line_count} lines and {char_count} characters.")
    else:
        print(f"File '{name}' not found.")

        if len(sys.argv) != 2:
            print("Usage: python mymod.py <input_file>")
        else:
            input_file = sys.argv[1]

test(name="temp")


