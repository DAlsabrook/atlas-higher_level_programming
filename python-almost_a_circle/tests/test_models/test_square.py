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

    def test_zero(self):
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(1, 2)
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

    def test_str_two(self):
        with self.assertRaises(TypeError):
            s = Square(1, "2")

    def test_str_three(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, "2")

    def test_neg(self):
        with self.assertRaises(ValueError):
            s = Square(-2)

    def test_neg_two(self):
        with self.assertRaises(ValueError):
            s = Square(1, -2)

    def test_neg_three(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -2)

    #area()
    def test_area_small(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    #todictionary
    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

    def test_str_representation(self):
        s = Square(10, 2, 1, 1)
        capture = str(s)
        correct = "[Square] (1) 2/1 - 10"
        self.assertEqual(capture, correct)

    #Test create method
    def test_create_Square(self):
        r1 = Square(5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual("[Square] (7) 1/2 - 5", str(r2))
