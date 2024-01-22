#!/usr/bin/python3
"""
Module for a function that looks for class type
"""


def is_same_class(obj, a_class):
    """
    Function that compares if object is an instance of a class

    Args:
        obj (object): Object to compare
        a_class (class): Class to compare against

    Returns:
        True if obj is the same class
        False if obj if of a different class
    """
    return type(obj) is a_class
