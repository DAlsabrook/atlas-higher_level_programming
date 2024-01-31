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
        """Take list of dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            JSON string representation of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Takes a string representation of dictionary

        Args:
            json_string (str): string representation of dict

        Returns: list of dict's
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON string to a file

        Args:
            list_objs (object): instance of an inherited object
        """
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file(cls):
        """Pulls from file to creat list of instances

        Returns:
            _type_: _description_
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                return [cls.create(**obj_dict) for obj_dict in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary (dict): dictionary containing attribute values

        Returns:
            Instance with attributes set from the dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance
