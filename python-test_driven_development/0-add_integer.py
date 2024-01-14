#!/usr/bin/python3
"""
Function to add two integers together
"""


def add_integer(a, b=98):
    """
    Function for simple addition

    Args:
        a: first int to use
        b: second int to use

    Return: The result of addition
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
