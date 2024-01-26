#!/usr/bin/python3
"""
Module for making a less wide rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Its a square. Same size on its sides. You know the deal.

    Args:
        Rectangle (class): very wide square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return f"[Square] ({id}) {x}/{y} - {size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if self.__validate_var("width", value, zero_allowed=False):
            self.width = value
            self.height = value
