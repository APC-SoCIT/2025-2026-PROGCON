def reverse_string(s):
    return s[::-1]

import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string('hello'), 'olleh')

if __name__ == "__main__":
    unittest.main()
