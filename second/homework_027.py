# Topic 27
# Task 1

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: int | float):
        assert type(data) in (int, float)

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    # Insert the root of the given subtree into the current tree
    def insert_subtree(self, subtree_root: 'Node'):
        if subtree_root.data < self.data:
            if self.left is None:
                self.left = subtree_root
            else:
                self.left.insert_subtree(subtree_root)
        elif subtree_root.data > self.data:
            if self.right is None:
                self.right = subtree_root
            else:
                self.right.insert_subtree(subtree_root)

    def print_self(self):
        if self.left:
            self.left.print_self()
        print(self.data)
        if self.right:
            self.right.print_self()

# Create the main tree
root = Node(20)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_self()

# Create a new subtree
subtree_root = Node(8)
subtree_root.insert(5)
subtree_root.insert(10)
subtree_root.insert(13)
subtree_root.insert(1)

# Insert the new subtree into the main tree
root.insert_subtree(subtree_root)

root.print_self()
