#!/usr/bin/python3
"""
Module for reading and writing a file with with as
"""


def append_write(filename="", text=""):
    """Method that reads a file and appends text to it"""
    with open(filename, "a") as file:
        return file.write(text)
