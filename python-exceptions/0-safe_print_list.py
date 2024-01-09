#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None or not my_list:
        return 0
    count = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
