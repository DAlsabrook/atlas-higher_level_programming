#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if my_list is None or element is None:
        return None
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
