#!/usr/bin/python3
"""
Module holds a function for finds if var is a child of class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that finds if obj is the child or grandchild of a_class

    Args:
        obj (object): The object to use
        a_class (class): Use to find if obj is a child or grandchild

    Return:
        True if related
        False if not
    """
    if isinstance(obj, a_class):
        if issubclass(obj, a_class):
            return True
    else:
        return False
