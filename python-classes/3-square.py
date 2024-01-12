#!/usr/bin/python3
"""Class to define a square"""


class Square:
    """Attributes of the square class"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        """Method to give the square of the object"""
        def area(self):
            return self.__size ** 2
