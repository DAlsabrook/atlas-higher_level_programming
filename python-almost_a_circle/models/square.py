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
