#!/usr/bin/python3
"""Module for unittest of the Rectangle class
"""
import unittest
from ...models.rectangle import Rectangle
from ...models.base import Base


class Test_Rectangle(unittest.TestCase):
    """Unit test for the Rectangle class

        Rectangle(width, height, x, y, id)
    """
    def test_height(self):
        """Height given
        """
        x = Rectangle(2, 4)
        self.assertEqual(x.height, 4)

    def test_width(self):
        """Width given
        """
        x = Rectangle(2, 4)
        self.assertEqual(x.width, 2)

    def test_x_given(self):
        """X given
        """
        x = Rectangle(2, 4, 6)
        self.assertEqual(x.x, 6)

    def test_y_given(self):
        """Y given
        """
        x = Rectangle(2, 4, 6, 8)
        self.assertEqual(x.y, 8)

    def test_id_given(self):
        """id Given
        """
        x = Rectangle(2, 4, 6, 8, 10)
        self.assertEqual(x.id, 10)

    def test_no_id(self):
        """No id given
        """
        x = Rectangle(2, 4)
        self.assertEqual(x.id, 4)

    def test_multiple_id(self):
        """Multiple instances for id
        """
        y = Rectangle(1, 3)
        x = Rectangle(2, 4)
        self.assertEqual(x.id, 3)

    def test_setter_width(self):
        """Width setter
        """
        x = Rectangle(2, 4)
        x.width = 10
        self.assertEqual(x.width, 10)

    def test_setter_height(self):
        """Height setter
        """
        x = Rectangle(2, 4)
        x.height = 10
        self.assertEqual(x.height, 10)

    def test_setter_x(self):
        """x setter
        """
        x = Rectangle(2, 4)
        x.x = 10
        self.assertEqual(x.x, 10)

    def test_setter_y(self):
        """y setter
        """
        x = Rectangle(2, 4)
        x.y = 10
        self.assertEqual(x.y, 10)

