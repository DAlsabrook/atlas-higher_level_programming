#!/usr/bin/python3
"""Definition of the square class"""


class Square:
    """attributes of the square class"""
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size

        if (not isinstance(position[0], int) or position[0] < 0) \
            or (not isinstance(position[1], int) or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    """Getter for the position attribute"""
    @property
    def position(self):
        return self.__position

    """Setter for the position property"""
    @position.setter
    def position(self, value):
        if (not isinstance(value[0], int) or value[0] < 0) \
            or (not isinstance(value[1], int) or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Method that returns the square area of the square"""
    def area(self):
        return self.__size ** 2

    """Method that prints the square using '#' char"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(0, self.__position[1]):
            print("")
        for row in range(self.__size):
           [print(" ", end="") for element in range(self.position[0])]
           [print("#", end="") for element in range(self.__size)]
           print()
