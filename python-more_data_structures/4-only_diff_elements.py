#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if (set_1 is None or not set_1) and (set_2 is None or not set_2):
        return set()
    elif set_2 is None or not set_2:
        return set_1
    else:
        return set_2.difference(set_1)
