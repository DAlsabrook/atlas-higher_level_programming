#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None or not my_list:
        return my_list
    return [replace if item == search else item for item in my_list]
