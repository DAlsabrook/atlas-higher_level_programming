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
    def __init__(self, height=0, width=0):
        super().__init__()
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width
