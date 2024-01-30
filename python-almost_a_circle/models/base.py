#!/usr/bin/python3
"""
Module for the Base class to build on
"""
import json


class Base:
    """
    Class to define a base id for subclasses
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of dict

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)
