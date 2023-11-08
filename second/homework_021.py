# Topic 21
# Task 1

class FileContextManager:
    counter = 0

    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
            FileContextManager.counter += 1
            return self.file
        except Exception as e:
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            pass
        FileContextManager.counter -= 1
        return False


file_path = "example.txt"

with FileContextManager(file_path, 'w') as file:
    file.write("You must be the change you wish to see in the world!")


with FileContextManager(file_path) as file:
    content = file.read()
    print(content)


print(f"Number of opened files: {FileContextManager.counter}")




