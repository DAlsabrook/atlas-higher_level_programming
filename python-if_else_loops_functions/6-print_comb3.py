#!/usr/bin/python3
for l in range(8):
    for r in range(l, 10):
        if l != r:
            print("{}{}".format(l, r), end=", ")
print("89")
