# Topic 24
# Task 3

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_stack(self, element):
        if element in self.items:
            return element
        raise ValueError(f"Element '{element}' not found in the stack")

    def display_stack(self):
        print("Stack: ", self.items)


stack_instance = Stack()

stack_instance.push(10)
stack_instance.push(20)
stack_instance.push(30)

stack_instance.display_stack()

try:
    result = stack_instance.get_from_stack(10)
    print(f"Element found: {result}")
except ValueError as e:
    print(f"Error: {e}")


class Queue:
    def __init__(self):
        self.items = []

    def in_queue(self, item):
        self.items.insert(0, item)

    def from_queue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Queue is empty")

    def is_empty(self):
        return len(self.items) == 0

    def get_from_queue(self, element):
        temp_queue = Queue()
        found = False

        while not self.is_empty():
            current = self.from_queue()
            if current == element:
                found = True
                break
            temp_queue.in_queue(current)

        while not temp_queue.is_empty():
            self.in_queue(temp_queue.from_queue())

        if found:
            return element
        else:
            raise ValueError(f"Element '{element}' not found in the queue")

    def display_queue(self):
        print("Queue: ", self.items)


queue = Queue()

queue.in_queue(11)
queue.in_queue(22)
queue.in_queue(33)
queue.in_queue(44)
queue.in_queue(55)
queue.display_queue()
queue.from_queue()
queue.get_from_queue(44)

queue.display_queue()


try:
    print(queue.get_from_queue(55))  # Output: 55
    print(queue.get_from_queue(20))  # Raises ValueError

except ValueError as e:
    print(e)





