#!/usr/bin/python3
"""Module for unittest of the Rectangle class
"""
import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    """Unit test for the Rectangle class

        Rectangle(width, height, x, y, id)
    """
    #Testing instance creation
    def test_two_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 4)
        self.assertEqual(r1.width, 10)

    def test_four_args(self):
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.width, 10)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_two_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    def test_two_args_str_again(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    def test_three_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "4")

    def test_four_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, "4")

    def test_two_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_two_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_three_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -3)

    def test_four_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -4)
