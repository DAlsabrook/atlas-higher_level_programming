#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None or not my_list:
        return my_list
    new_list = my_list
    for idx, item in enumerate(my_list):
        if item == search:
            new_list[idx] = replace
        else:
            new_list[idx] = item
    return new_list
