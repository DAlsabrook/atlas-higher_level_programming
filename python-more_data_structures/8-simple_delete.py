#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is None or not a_dictionary:
        a_dictionary = {}
    if key is not None and key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
