# Stack
# [1, 0, 100, 3] original
# [1, 0, 100, 3, 75] added one element
# [1, 0, 100, 3] removed one element
# [1, 0, 100] removed another element
#
# Queue
# [1, 0, 100, 3] 3] original
# [1, 0, 100, 3, 75] added one element
# [0, 100, 3, 75] removed one element
# [100, 3, 75] removed another element
#
# Deque -> double-ended queue
# The same as queue, but you can both add and remove elements from both ends

class Stack:
    """
    Stack implements a data storage where we can add and remove elemets only from the end
    """

    def __init__(self):
        self.storage = []

    def pop(self):
        """Remove and return the top (last) element"""

        return self.storage.pop()

    def push(self, element):
        """Add a new element to the top (end) of the storage"""

        self.storage.append(element)

    @property
    def last_element(self):
        """Return the top (last) element without removing it from the storage"""

        return self.storage[-1] if self.storage else None

    def size(self):
        """Return the length of the storage"""

        return len(self.storage)

    def is_empty(self):
        """Return True if storage is empty, otherwise False"""

        return not self.storage

    def clear(self):
        """Clear data"""

        self.storage = []


class Queue(Stack):

    def shift(self):
        return self.storage.pop(0)

    def pop(self):
        raise TypeError("This is not a stack. This is a queue")


# class Deque(Stack, Queue):
#
#     def unshift(self, element):
#         self.storage.insert(0, element)