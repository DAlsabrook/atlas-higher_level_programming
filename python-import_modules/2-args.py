#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len == 2:
        print("{} argument:\n1: {}".format(arg_len - 1, sys.argv[1]))
    elif arg_len > 2:
        print("{} arguments:".format(arg_len - 1))
        for arg in range(1, arg_len):
            print("{}: {}".format(arg, sys.argv[arg]))
    else:
        print(".")
