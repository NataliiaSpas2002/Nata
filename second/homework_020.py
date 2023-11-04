# Topik 20
# Task 1
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


my_str = "Don't trouble trouble until trouble troubles you"
for elem, in Reverse(my_str):
    print(elem, end='')
print()

my_str = "Good morning everybody!"
for elem, in Reverse(my_str):
    print(elem, end='')
print()
