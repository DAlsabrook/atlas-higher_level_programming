#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None or not my_list:
        return
    result = 0
    tmp_list = set(my_list)
    for number in tmp_list:
        result += number
    return result
