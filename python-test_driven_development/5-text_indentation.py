#!/usr/bin/python3
"""
Module for a function that itterates through a string to look for chars
"""


def text_indentation(text):
    """
        Function that finds '.', '?', and ':' and prints 3 new lines after

        Args:
            text (str): string to iterate through for special chars

        Prints: Original string but with newline chars after special chars

        Returns: Nothing

        Raises:
            TypeError: text variable is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_str = ""
    for char in text:
        if char in ('.', '?', ':'):
            new_str += char + "\n\n"
        else:
            new_str += char
    print(new_str, end="")
