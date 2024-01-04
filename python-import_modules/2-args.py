#!/usr/bin/python3

import sys
len = len(sys.argv)

if __name__ == "__main__":
    if len == 2:
        print("{} argument:\n1: {}".format(len - 1, sys.argv[1]))
    elif len > 2:
        print("{} arguments:".format(len))
        for arg in range(1, len):
            print("{}: {}".format(arg, sys.argv[arg]))
    else:
        print(".")
