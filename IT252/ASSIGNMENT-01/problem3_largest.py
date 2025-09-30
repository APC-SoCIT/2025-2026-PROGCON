def largest_of_three(a, b, c):
    return max(a, b, c)

import unittest

class TestLargestOfThree(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(largest_of_three(3, 7, 5), 7)

if __name__ == "__main__":
    unittest.main()
