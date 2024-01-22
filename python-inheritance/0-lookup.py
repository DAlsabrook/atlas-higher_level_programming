#!/usr/bin/python3
"""
Module for a function to return class attributes and methods
"""


def lookup(obj):
    """
    Function that returns a list of attributes and
    methods available to a class or object

    Args:
        obj (object): The class or object to look up attributes/methods

    Returns: List of available attributes and methods
    """
    return dir(obj)
