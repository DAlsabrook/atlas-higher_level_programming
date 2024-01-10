#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = float(a // b)
    except ZeroDivisionError:
        res = None
    finally:
            print("Inside result: {}". format(res))
    return res
