#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key is not None:
        a_dictionary.update({key: value})
    return a_dictionary
