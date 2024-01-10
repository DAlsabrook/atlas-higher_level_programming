#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums_printed = 0
    for nums in range(x):
        try:
            print("{:d}".format(my_list[nums]), end="")
            nums_printed += 1
        except (IndexError, ValueError):
            continue
    print()
    return nums_printed
