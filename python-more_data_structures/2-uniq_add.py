#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return my_list
    result = 0
    tmp_list = set(my_list)
    for number in tmp_list:
        result += number
    return result
