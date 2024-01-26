#!/usr/bin/python3
"""Module to hold the class for a rectangle
"""
from .base import Base


class Rectangle(Base):
    """Class to define a rectangle

    Args:
        Base (object): used to define id

    Attributes:
        Width(int): how wide rect is
        Height(int): How high rect is
        x(int): idk
        y(int): idk
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if self.__validate_var("width", width, zero_allowed=False):
            self.__width = width
        if self.__validate_var("height", height, zero_allowed=False):
            self.__height = height
        if self.__validate_var("x", x, zero_allowed=True):
            self.__x = x
        if self.__validate_var("y", y, zero_allowed=True):
            self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.__validate_var("width", value, False):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.__validate_var("height", value, False):
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__validate_var("x", value, True):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__validate_var("y", value, True):
            self.__y = value

    def __validate_var(self, name, value, zero_allowed):
        """Check on attributes to make sure they meet conditions

        Args:
            name (str): string name for the variable
            value (int): variable itself

        Raises:
            ValueError: variable is not > 0
            TypeError: variable is not int

        Returns:
            True if validated
        """
        if isinstance(value, int):
            # Case for width and height
            if not zero_allowed and value <= 0:
                raise ValueError(f"{name} must be > 0")
            # Case for x and y
            elif zero_allowed and value < 0:
                raise ValueError(f"{name} must be >= 0")
            # Makes it to here then value is an int and correct range
            else:
                return True
        else:
            raise TypeError(f"{name} must be an integer")

    def area(self):
        """Returns the area of a rectangle
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle using "#"
        """
        for num in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns string representation of rect"""
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args):
        """give the caller the ability to update multiple attributes at once
        """
        args[0] = self.id
        args[1] = self.__width
        args[2] = self.__height
        args[3] = self.__x
        args[4] = self.__y
