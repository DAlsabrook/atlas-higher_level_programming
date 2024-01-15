#!/usr/bin/python3
"""
This module contains a function that inserts names into a string
"""


def say_my_name(first_name, last_name=""):
    message = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(message)
    print(f"My name is {first_name}", end="")
    if not last_name == "":
        print(f" {last_name}")
    else:
        print()
