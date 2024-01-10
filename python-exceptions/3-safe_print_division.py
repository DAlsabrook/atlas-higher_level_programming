#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = float(a // b)
    except (ZeroDivisionError, TypeError):
        res = None
    except Exception as e:
        print("Exception:", e)
    finally:
        print("Inside result: {}". format(res))
    return res
