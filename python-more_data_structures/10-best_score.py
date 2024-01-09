#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return
    res = 0
    for key, value in a_dictionary.items():
        if a_dictionary[key] > res:
            res = value 
    return res if res != 0 else None
