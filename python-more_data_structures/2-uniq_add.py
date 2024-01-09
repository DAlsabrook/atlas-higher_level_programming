#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(set(my_list))
    return result if my_list else my_list
