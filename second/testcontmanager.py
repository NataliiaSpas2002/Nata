# Topic 21
# Task 2

import unittest
from homework_021 import FileContextManager


class TestFileContextManager(unittest.TestCase):

    def test_file_opening_and_closing(self):
        with FileContextManager('example.txt', 'w') as file:
            file.write('Hello, World!')

        with open('example.txt', 'r') as file:
            content = file.read()
            self.assertEqual(content, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()