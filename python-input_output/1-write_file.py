#!/usr/bin/python3
"""
Module for reading and writing a file with with as
"""


def write_file(filename="", text=""):
    """Method that reads a file and prints to stdout"""
    with open(filename, "w") as file:
        return file.write(text)
