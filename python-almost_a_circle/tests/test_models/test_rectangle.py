#!/usr/bin/python3
"""Module for unittest of the Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO

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

    def test_two_arg_value_zero(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_two_arg_value_zero_again(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_two_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_two_arg_value_again(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_three_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -3)

    def test_four_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -4)

    #Test for methods in rect
    #area() test
    def test_area(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    #__str__ test
    def test_str(self):
        r1 = Rectangle(1, 2)
        capture = str(r1)
        correct = "[Rectangle] ({}) 0/0 - 1/2".format(r1.id)
        self.assertEqual(correct, capture)

    #display()
    def test_display(self):
        r1 = Rectangle(2, 2, 1, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            output = stdout.getvalue().strip()
        expected_output = "##\n ##"
        self.assertEqual(output, expected_output)

    def test_display_no_y(self):
        r1 = Rectangle(2, 2, 1, 0, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            output = stdout.getvalue().strip()
        expected_output = "##\n ##"
        self.assertEqual(output, expected_output)

    def test_display_no_x(self):
        r1 = Rectangle(2, 2, 0, 1, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            output = stdout.getvalue().strip()
        expected_output = "##\n##"
        self.assertEqual(output, expected_output)
