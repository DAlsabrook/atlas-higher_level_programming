#!/usr/bin/python3
"""
This module contains a function that inserts names into a string
"""


def say_my_name(first_name, last_name=""):
    """
        Function that takes fist and last name, then prints them in a sentance

        Args:
            first_name (str): string variable to use as first name
            last_name (str): string variable to use as last name

        Prints: My name is {first_name} {last_name}

        Returns: nothing

        Raises:
            TypeError: if first_name or last_name is not a str
    """
    message = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(message)
    print(f"My name is {first_name} {last_name}")
