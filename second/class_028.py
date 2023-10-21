# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10...

#  def fibonnacci(n):
#     if n <= 1:
#         return n
#     return fibonnacci(n-1) + fibonnacci(n-2)
# print(fibonnacci(10))
#
# def fibonnacci(n):
#     a, b = 0, 1
#     for item in range(n):
#         result = b
#         a, b = b, a + b
#
#     return a
#
# print(fibonnacci(10))
# assert fibonnacci(10) == 55


import random
from string import ascii_letters



def my_hash(key: str):
    hash_value = 17

    for ch in key:
        hash_value = (hash_value * 31 + ord(ch)) % 100

    return hash_value

def gen_random_string():
    result_len = random.randint(1, 10)
    all_characters = ascii_letters + '0123456789'

    return ''.join([random.choice(all_characters) for _ in range(result_len)])


result_range = range(101)
data = dict.fromkeys(result_range, 0)
for _ in range(10000):
    key = my_hash(gen_random_string())
    data[key] = data[key] + 1

names = list(data.keys())
values = list(data.values())

# pyplot.bar(range(len(data)), values, tick_label=names)
# pyplot.show()

class HashTable:

    def __init__(self):
        self.storage = [None] * 100
        self.len = 0

# collisions
# my_dict = [
#    [[key, value], [key, value]]
#    [[key, value]]
#    ...
# ]
    def get_by_key(self, key):
        index = my_hash(key)  # O(1)
        result = self.storage[index]
        if result is None:
            raise KeyError
        return result

    def save_value_by_key(self, key, value):
        self.len += 1
        index = my_hash(key)  # O(1)
        self.storage[index] = value  # O(1)

    def __len__(self):
        return self.len

# 1. colissions processing
# 2. deletion operator
# 3. get length  __len__
# 4. "in" operator  __contains__
# 5. "update" operator
# 6. turn methods into magic methods

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict1.update(dict2)

print(5 in dict1)

for key, value in dict2.items():
    dict1[key] = value
# 6. storage management


my_custom_dictionary = HashTable()
my_custom_dictionary.save_value_by_key("one", 1)
my_custom_dictionary.save_value_by_key("two", 2)

print(my_custom_dictionary.get_by_key("two"))

# why only immutable variables as keys

class MyEvilKey():
    def __init__(self,       value):
        #        mutable_key "abc"
        self.value = value  # mutable_key.value = "abc"

    def modify_value(self, new_value):
        self.value = new_value

    def __hash__(self):
        return my_hash(self.value)

non_custom_dictionary = dict()
mutable_key = MyEvilKey("abc")
non_custom_dictionary[mutable_key] = 100
mutable_key.modify_value("def")
print(non_custom_dictionary[mutable_key])





