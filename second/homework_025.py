# Topic 25
# Task 1

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next_node = None


class UnsortedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def is_empty(self):
        return self.root is None

    def __add__(self, item):
        temp = Node(item)
        temp.next_node = self.root
        self.root = temp
        self.size += 1

    def length(self):
        return self.size

    def display(self):
        current = self.root
        while current:
            print(current.data, end=" ")
            current = current.next_node
        print()

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                    self.size -= 1
                    return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
            return False

    def append(self, item):
        self.__add__(item)

    def index(self, item):
        current = self.root
        index = 0

        while current:
            if current.data == item:
                return index
            current = current.next_node
            index += 1

        raise ValueError (f"{item} not in list")

    def pop(self, index=None):
        if index is None:
            index = self.size - 1

        if index < 0 or index >= self.size:
            raise IndexError("pop index out of range")

        current = self.root
        prev_node = None

        for i in range(index):
            prev_node = current
            current = current.next_node

        if prev_node:
            prev_node = current
            current = current.next_node

        else:
            self.root = current.next_node

        self.size -= 1
        return current.data

    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("insert index out of range")

        if index == 0:
            self.__add__(item)
        else:
            current = self.root
            prev_node = None

            for i in range(index):
                prev_node = current
                current = current.next_node

            new_node = Node(item)
            new_node.next_node = current
            prev_node.next_node = new_node
            self.size += 1

    def slice(self, start, stop):
        if start < 0 or  stop > self.size or start >= stop:
            raise ValueError("Invalid start or stop values")

        sliced_list = UnsortedList()
        current = self.root

        for i in range(start):
            current = current.next_node

        for i in range(start, stop):
            sliced_list.append(current.data)
            current = current.next_node

        return sliced_list


my_list = UnsortedList()

my_list.append(5)
my_list.append(20)
my_list.append(7)
my_list.append(11)
my_list.display()
my_list.append(40)
my_list.display()
my_list.slice(start=1, stop=2)

print("Index of 5:", my_list.index(5))

sliced = my_list.slice(0, 5)
print("Sliced list:")
sliced.display()
my_list.insert(1, 25)
my_list.insert(6, 55)
my_list.display()





