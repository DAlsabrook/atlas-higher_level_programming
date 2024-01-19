#!/usr/bin/python3
"""
Module for a class 'MyList' that inherits from 'list'
"""


class MyList(list):
    """
    Class for sorting a list

    Args:
        list: Used for sorting in ascending order

    Attributes: N/A

    Methods:
        print_sorted: Prints the list in ascending order
    """

    def print_sorted(self):
        """Method for printing list in ascending order"""
        print(sorted(self))
