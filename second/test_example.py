import unittest
from homework_020 import Reverse


class TestReverse(unittest.TestCase):
    def test_reverse_string(self):
        original_str = "Good morning everybody!"
        reverse_str = "".join(elem for elem in Reverse(original_str))
        self.assertEqual(reverse_str, "!ydobyreve gninrom dooG")

    def test_reserve_numbers(self):
        original_str = "56789"
        reversed_str = "".join(elem for elem in Reverse(original_str))
        self.assertEqual(reversed_str, "98765")



if __name__ == '__main__':
    unittest.main()