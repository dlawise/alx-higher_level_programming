#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: Regular list of integers
        lst = [1, 5, 3, 9, 2]
        self.assertEqual(max_integer(lst), 9)

        # Test case 2: List with negative integers
        lst = [-2, -8, -5, -1]
        self.assertEqual(max_integer(lst), -1)

        # Test case 3: List with a single element
        lst = [4]
        self.assertEqual(max_integer(lst), 4)

        # Test case 4: Empty list (should return None)
        lst = []
        self.assertIsNone(max_integer(lst))

        # Test case 5: List with duplicate maximum value
        lst = [3, 7, 9, 5, 9, 2, 9]
        self.assertEqual(max_integer(lst), 9)

        # Test case 6: List with mixed data types (raises TypeError)
        lst = [1, 2, '3', 4, 5]
        self.assertRaises(TypeError, max_integer, lst)


if __name__ == '__main__':
    unittest.main()
