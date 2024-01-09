#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return my_list
    result = sum(set(my_list))
    return result
