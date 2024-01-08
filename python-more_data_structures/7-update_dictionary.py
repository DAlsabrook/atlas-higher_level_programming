#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or not a_dictionary:
        a_dictionary = {}
    if key is not None:
        a_dictionary.update({key: value})
    return a_dictionary
