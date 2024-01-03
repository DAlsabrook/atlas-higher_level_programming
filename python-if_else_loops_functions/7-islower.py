#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c <= 122 and c >= 97:
        return True
    else:
        return False
