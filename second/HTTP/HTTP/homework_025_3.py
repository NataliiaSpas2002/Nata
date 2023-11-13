# Task 3

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node =None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        removed_data = self.front.data
        self.front = self.front.next_node
        self.size -= 1
        if self.is_empty():
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        return self.front.data

    def display_queue(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next_node
        print()


queue = Queue()
queue.enqueue(13)
queue.enqueue(14)
queue.enqueue(15)
queue.enqueue(16)
print("Initial queue:")
queue.display_queue()
print("Dequeue:", queue.dequeue())
print("Peek:", queue.peek())

print("Updated queue:")
queue.display_queue()

