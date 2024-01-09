#!/usr/bin/python3
def uniq_add(my_list=[]):
    return my_list if not my_list else sum(set(my_list))
