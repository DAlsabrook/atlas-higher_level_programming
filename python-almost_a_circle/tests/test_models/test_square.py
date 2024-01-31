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
