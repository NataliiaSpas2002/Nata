def plus(a,b):
    return a+b

if __name__ == '__main__':
    print(plus(2,2))

# import random
# range_len = 10
# range_obj = range(range_len)
# i = 0
# while i < range_len:
#     print(range_obj[i])
#     i += 1
#
# import random
# my_list =
# my_list = random.randint[1, 100]
# for i in range(len(my_list)):
#     print(max(my_
# import random
# num_list = []
# largest = []
# maximum = -1
# while len(num_list) < 10:
#     numbers = random.randrange(0,1000)
#     num_list.append(numbers)
# if len(num_list) == 10:
#     print(num_list)
#     for num in num_list:
#         if num > maximum:
#             maximum = num
#             largest.append(num)
#     print(max(largest))


import time
def spinner():
    symbols = ['/', '—', '\\', '|']
    while True:
        for symbol in symbols:
            print('\b' * 1 + symbol, end ="")
            time.sleep(0.4)
spinner()

# new_list = ["Mango",
#     "Apple",
#     "Orange",
#     "Kiwifruit",
#     "Grape",
#     "Banana",
#     "Cherry",
#     "Watermelon",
#     "Pineapple",
#     "Apricot",
#     "Strawberry",
#     "Avocado",
#     "Peach",
#     "Grapefruit",
#     "Papaya",
#     "Lemon",
#     "Pear",
#     "Blueberry",
#     "Plum",
#     "Pomegranate",
#     "Blackberry",
#     "Raspberry",
#     "Guava",
#     "Lime",]
# # list comprehension:
# #          [expression_containing_item for item in iterable  [if expression]]
# new_list = [item**0.5                  for item in range(10) if item % 2 == 0]
#
# some_dictionary = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
# }
# # new_dictionary = {value:  key for key, value  in some_dictionary.items()}
# # print(new_dictionary)
#
# new_dictionary = {key:  some_dictionary     for key        in range(10) if key > 9}
# print(new_dictionary)

import random
# range_len = 10
# range_obj = range(range_len)
#
# i = 1
# t = [1,2,3,4,5,6,7,8,9,10]
# while i < range_len:
#     print(range_obj[i], t[1])
#     i += 1




