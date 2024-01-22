#!/usr/bin/python3
"""
Module for class of Rectangle(BaseGeometry)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class to define a rectangle and its methods/attributes

    Inheritance:
        BaseGeometry

    Attributes:
        height (int): height of rectangle
        width (int): width of rectagnle
    Methods:
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """Method the returns the area of the rect"""
        return self.__height * self.__width

    def __str__(self):
        """
        Method to return string representation of rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
