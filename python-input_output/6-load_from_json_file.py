#!/usr/bin/python3
"""
Module to create obj from json file
"""
import json


def load_from_json_file(filename):
    """
    Turn a JSON file into an object
    """
    with open(filename, "r") as file:
        return json.loads(file)
