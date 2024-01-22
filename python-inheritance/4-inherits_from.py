#!/usr/bin/python3
"""
Module to hold a function for finding if obj is inheriting
"""


def inherits_from(obj, a_class):
    """
    Function that finds if obj is inheriting from a_class

    Args:
        obj (object): Object to compare
        a_class (class): Class to see if obj inherits from

    Returns:
        True if obj inherits
        False if not
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
