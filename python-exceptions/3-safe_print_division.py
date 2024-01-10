#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = float(a // b)
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}". format(res))
    return res
