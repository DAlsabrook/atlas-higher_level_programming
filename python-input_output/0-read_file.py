#!/usr/bin/python3
"""
Module for reading a file with with as
"""
def read_file(filename=""):
    """Method that reads a file and prints to stdout"""
    with open(filename) as file:
        print(file.read(), end="")
