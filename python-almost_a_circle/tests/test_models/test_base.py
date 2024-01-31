#!/usr/bin/python3
"""
Module for unit test of the base class
"""
import unittest
from ...models.base import Base


class Base_test(unittest.TestCase):
    """Class to run unit test on base class

    Args:
        unittest (object): class for running unit test
    """

    def test_none(self):
        """Case for default None value given to class with no id given
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_given_id(self):
        self.assertEqual(Base(4).id, 4)

    def test_negative(self):
        """Case for negative number given as id
        """
        x = Base(-1)
        self.assertEqual(x.id, -1)

    def test_float(self):
        """Case for float given as id
        """
        x = Base(1.2)
        self.assertEqual(x.id, 1.2)

if __name__ == "__main__":
    unittest.main()
