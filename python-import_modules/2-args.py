#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 2:
        print("{} argument:\n1: {}".format(len - 1, sys.argv[1]))
    elif len > 2:
        print("{} arguments:".format(len - 1))
        for arg in range(1, len):
            print("{}: {}".format(arg, sys.argv[arg]))
    else:
        print(".")
