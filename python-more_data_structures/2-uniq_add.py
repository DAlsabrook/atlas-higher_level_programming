#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ints = set()
    for nums in my_list:
        if isinstance(nums, int):
            uniq_ints.add(nums)
    return sum(set(uniq_ints))
