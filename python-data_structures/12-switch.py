#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
if a > 0 and b > 0:
    print("a={:d} - b={:d}".format(a, b))
