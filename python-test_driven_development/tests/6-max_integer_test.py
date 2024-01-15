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
        self.assertEqual(list, 3)

    def test_max_int_negative(self):
        list = [-1, -2, -3]
        self.assertEqual(list, -3)

    def test_max_int_empty(self):
        list = [1, 2, 3]
        self.assertFalse(list)
    def test_max_int_none(self):
        list = None
        self.assertIsNone(list)

