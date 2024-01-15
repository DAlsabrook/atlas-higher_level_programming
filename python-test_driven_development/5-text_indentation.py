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
    flag = 0
    new_str = ""
    for char in text:
        if char.isspace() and flag == 1:
            continue
        if char in ('.', '?', ':'):
            new_str += char + "\n\n"
            flag = 1
        else:
            new_str += char
            flag = 0
    print(new_str, end="")
