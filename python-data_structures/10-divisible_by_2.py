#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is None or not my_list:
        return None
    bool_list = []
    for index, num in enumerate(my_list):
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
