#!/usr/bin/python3
"""
    Module that unittest for the max_integer func
"""


import unittest
import importlib

max_integer_module = importlib.import_module("6-max_integer")
max_integer = max_integer_module.max_integer

class TestMaxInt(unittest.TestCase):

    def test_max_int_normal(self):
        list = [1, 2, 3]
        self.assertEqual(max_integer(list), 3)

    def test_max_int_negative(self):
        list = [-1, -2, -3]
        self.assertEqual(max_integer(list), -1)

    def test_max_int_middle(self):
        list = [1, 10, 3]
        self.assertEqual(max_integer(list), 10)

    def test_max_int_empty(self):
        list = []
        self.assertFalse(max_integer(list))

    def test_max_int_one(self):
        list = [1]
        self.assertEqual(max_integer(list), 1)

if __name__ == "__main__":
    unittest.main()

