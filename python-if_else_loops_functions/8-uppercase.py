#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for char in str:
        if char.islower():
            newstr += chr(ord(char) - 32)
        else:
            newstr += char
    print("{}".format(newstr))
