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
        x = Base()
        self.assertEqual(x.id, 1)

    def test_given_id(self):
        """Case for id given as argument
        """
        x = Base(4)
        self.assertEqual(x.id, 4)

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
