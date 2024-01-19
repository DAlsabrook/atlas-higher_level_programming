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
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
