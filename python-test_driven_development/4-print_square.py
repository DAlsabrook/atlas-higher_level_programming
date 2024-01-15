#!/usr/bin/python3
"""
Module documentation
"""


def print_square(size):
    """
        Print_square prints a square of size {size} made of "#"

        Args:
            size (int): length of the square

        Returns: nothing

        Raises:
            TypeError: If size is not an int
            ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for hash in range(size):
            print("#", end="")
        print()
