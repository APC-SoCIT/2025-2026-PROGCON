def is_even(n):
    return n % 2 == 0

import unittest

class TestEvenOdd(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))
    def test_odd(self):
        self.assertFalse(is_even(5))

if __name__ == "__main__":
    unittest.main()
