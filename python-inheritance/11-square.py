#!/usr/bin/python3
"""
Module to hold the class for a square object
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to define a square

    inherits:
        Rectangle

    Attributes:

    Methods:
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Overwrites the rect string representation"""
        return f"[Square] {self.__size}/{self.__size}"
