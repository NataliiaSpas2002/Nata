# Task 2

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        popped_item = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return popped_item

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next_node
        print()


stack = Stack()
stack.push(70)
stack.push(80)
stack.push(90)
stack.push(100)
stack.display()

try:
    top_item = stack.peek()
    print(f"The top item in the stack is: {top_item}")
except ValueError as e:
    print(f"Error: {e}")

stack.pop()
stack.display()

try:
    top_item = stack.peek()
    print(f"The top item in the stack is: {top_item}")
except ValueError as e:
    print(f"Error: {e}")