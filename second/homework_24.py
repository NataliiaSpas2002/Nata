# Topic
# Task 1

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0



stack = Stack()
stack.push(54)
stack.push(45)
stack.push(100)
stack.push(11)
stack.push("+")
stack.pop()
stack.pop()


while not stack.is_empty():
    print(stack.pop())

# Task 2

def brackets_balanced(sequence):
    stack1 = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for symb in sequence:
        if symb in opening_brackets:
            stack1.append(symb)
        elif symb in closing_brackets:
            if not stack1 or opening_brackets[closing_brackets.index(symb)] != stack1.pop():
                return False

    return not stack1

assert brackets_balanced("(((") is False
assert brackets_balanced("{}()''") is True
assert brackets_balanced("{[}") is False
assert brackets_balanced("([[])") is False




















