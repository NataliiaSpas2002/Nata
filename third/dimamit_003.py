# word = "Test"
# command = 'down'
#
# def up(word):
#     print((word.upper()))
#
# def down(word):
#     print(word.lower())
#
# def default(*args, **kwargs):
#     print(("Unknown command"))
#
# def process(command):
#     command_dict = {
#         "up": up,
#         "down": down
#     }
#     if command in command_dict:
#         return command_dict[command]
#     else:
#         return command
#
# process('up')('Test1')
# process('down')('CALENGE')

def min_transposition(array: list[int]) -> int:
    count = 0
    count_arr = array.count(1)

    if count_arr == 0 and len(array) == count_arr and array == []:
        return 0
    ones_indices = [i for i, val in enumerate(array) if val == 1]
    print(ones_indices)

    return count

# print(sys.path)
# sys.path.append('C:/Users/Катерина/Desktop/Beetroot/HW_9/task_1')
#
# from part_1 import sum_numbers as summ
#
# summ(22, 14)
# Topic 9, 3p
# def new_test(name):
#     line_count = count_lines(name=1)
#     char_count = count_chars(name=1)
#     if line_count != -1 and char_count != -1:
#         print(f"File '{name}' has {line_count} lines and {char_count} characters.")
#     else:
#         print(f"File '{name}' not found.")
#
#         if len(sys.argv) != 2:
#             print("Usage: python mymod.py <input_file>")
#         else:
#             input_file = sys.argv[1]
#
# new_test(name="temp")

# Topic 9 Task2
# Task 2
# import sys
#
# print(sys.path)
# sys.path.append('C:/Users/Катерина/Desktop/Beetroot/HW_9/task_1')
#
# from part_1 import sum_numbers as summ
#
# summ(22, 14)

def super_func():
    # print("I’m a global")
    def inner_func():
        print("I’m a local")
    return inner_func
super_func()()
