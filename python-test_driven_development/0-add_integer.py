#!/usr/bin/python3
"""
Module to run an addition function hopefully
"""


def add_integer(a, b=98):
    """
    Function for simple addition
    Examples:
        >>> add_integer(5, 5)
        10

    Args:
        a (int, float): first int to use
        b (int, float): second int to use

    Return:
        (int): The result of addition

    Raises:
        TypeError: if a or b are not an int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
