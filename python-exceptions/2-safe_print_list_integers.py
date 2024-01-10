#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nums_printed = 0
    try:
        for num in range(x):
            if type(my_list[num]) == int:
                print("{}".format(my_list[num]), end="")
                nums_printed += 1
    except IndexError:
        pass
    print()
    return nums_printed
