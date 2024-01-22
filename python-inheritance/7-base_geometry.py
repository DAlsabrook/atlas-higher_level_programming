#!/usr/bin/python3
"""
Module that contains a class for BaseGeometry
"""


class BaseGeometry:
    """
    Class for simple base of geometry
    """
    def __init__(self) -> None:
        pass

    """Method to check if area is implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    """Method to validate value variable"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
