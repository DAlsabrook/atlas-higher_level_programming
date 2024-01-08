#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or not a_dictionary:
        return
    if key is not None:
        a_dictionary.update({key: value})
