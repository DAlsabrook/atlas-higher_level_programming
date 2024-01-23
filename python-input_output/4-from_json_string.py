#!/usr/bin/python3
"""
Module for converting from json to object
"""
import json
from types import SimpleNamespace


def from_json_string(my_str):
    """
    Method to convert json into an object
    """
    return json.loads(my_str, object_hook=lambda d: SimpleNamespace(**d))
