#!/usr/bin/python3
"""
    Module that unittest for the max_integer func
"""


import unittest
import importlib

max_integer_module = importlib.import_module("6-max_integer")
max_integer = max_integer_module.max_integer

class TestMaxInt(unittest.TestCase):

    # Test for normal use case
    def test_max_int_normal(self):
        list = [1, 2, 3]
        self.assertEqual(max_integer(list), 3)

    # Test for max int being in the middle of the list
    def test_max_int_middle(self):
        list = [1, 10, 3]
        self.assertEqual(max_integer(list), 10)

    # Test for negative numbers and max being the first element
    def test_max_int_negative(self):
        list = [-1, -2, -3]
        self.assertEqual(max_integer(list), -1)

    # Test for a list of 1 element
    def test_max_int_one(self):
        list = [1]
        self.assertEqual(max_integer(list), 1)

    # Test for an empty list
    def test_max_int_empty(self):
        list = []
        self.assertFalse(max_integer(list))

if __name__ == "__main__":
    unittest.main()

