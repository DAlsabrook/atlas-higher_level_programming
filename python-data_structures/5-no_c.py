#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return None
    new_str = ""
    for char in my_string:
        if char.lower() != "c":
            new_str += char
    return new_str
