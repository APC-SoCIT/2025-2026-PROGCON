def sum_two_numbers(a, b):
    return a + b

import unittest

class TestSumTwoNumbers(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_two_numbers(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
