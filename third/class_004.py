class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, root=None):
        self.root = root # first nout
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def __repr__(self):
        next_n = self.root
        res = ""

        while next_n:
            res += str(next_n.data) + " -> "
            next_n = next_n.next_node
        return res

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
                prev_node = this_node.next_node
            return False

my_list = LinkedList()

my_list.add(5)
my_list.add(9)
my_list.add(7)
my_list.add(4)

print(my_list)



def my_hash(key: str):
    factor_1 = len(key)
    factor_2 = sum(ord(symbol) for symbol in key)

    result = int((factor_2*factor_2/factor_1)*100)%100

    return result

print(my_hash("CB8535"))
print(my_hash("6EDDF91"))
print(my_hash("AA2A61E"))
print(my_hash("EDDF917D"))
print(my_hash("29BF04AA"))
print(my_hash("E125EE6E"))
print(my_hash("F917DB"))
print(my_hash("F917DC"))



