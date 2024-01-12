#!/usr/bin/python3
"""Definition of the square class"""


class Square:
    """attributes of the square class"""
    def __init__(self, size=0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
    """Getter for the size attribute"""
    @property
    def size(self):
        return self.__size

    """Setter for size property"""
    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value

    """Method that returns the square area of the square"""
    def area(self):
        return self.__size ** 2

    """Method that prints the square using '#' char"""
    def my_print(self):
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for element in range(self.__size):
                print("#", end="")
            print()
