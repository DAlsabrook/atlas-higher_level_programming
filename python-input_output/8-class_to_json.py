#!/usr/bin/python3
"""
Module to convert a class to JSON
"""


def class_to_json(obj):
    obj_dict = obj.__dict__

    # looking to find if any value is a list aka has a __dict__ attribute
    # and is a class
    for key, value in obj_dict.items():
        if hasattr(value, '__dict__'):
            obj_dict[key] = class_to_json(value)
    return obj_dict
