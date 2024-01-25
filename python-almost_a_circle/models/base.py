#!/usr/bin/python3
"""
Module for the Base class to build on
"""


class Base:
    """
    Class to define a base id for subclasses
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
