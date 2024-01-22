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

    def area(self):
        raise Exception("area() is not implemented")
