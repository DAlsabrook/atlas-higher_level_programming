#!/usr/bin/python3
"""
Module to test the square class
"""
from models.square import Square
import unittest


class Test_Square(unittest.TestCase):
    """
    Class to test the square class
    """
    def test_normal(self):
        self.assertEqual(Square(5).size, 5)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_str(self):
        with self.assertRaises(TypeError):
            s = Square("2")

    def test_neg(self):
        with self.assertRaises(ValueError):
            s = Square(-2)

    #area()
    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())
