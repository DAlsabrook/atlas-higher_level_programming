#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return
    val_check = next(iter(a_dictionary.values()))
    string = next(iter(a_dictionary.keys()))
    for key, value in a_dictionary.items():
        if value > val_check:
            string = key 
    return string
