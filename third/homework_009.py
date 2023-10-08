# Topic 9
# Task 1
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

# Task 3
def count_lines(name):
    with open("temp.txt", "r") as file:
        lines = file.readlines()
    return len(lines)
print("Number of lines:", count_lines("temp.txt"))
#
def count_chars(name):
    try:
        with open("temp.txt", 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return -1
print("Number of characters", count_chars(name=1))

def new_task():
    name = input("Enter file name: ")
    print(count_lines(name))
    print(count_chars(name))
new_task()




