#!/usr/bin/python3
import sys
argc = len(sys.argv)
res = 0
if __name__ == "__main__":
    for i in range(1, argc):
        res += int(sys.argv[i])
    print(res)
