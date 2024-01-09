#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return
    res = next(iter(a_dictionary.values()))
    print(res)
    for value in a_dictionary.values():
        if value > res:
            res = value 
    return res
