#!/usr/bin/python3
"""
Module to save to json file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method to write obj to a text file, using JSON representation
    """
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))

