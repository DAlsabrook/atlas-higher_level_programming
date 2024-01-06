#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for list in matrix:
        for idx, element in enumerate(list):
            print("{:d}".format(element), end="")
            if idx != len(list):
                print(" ", end="")
        print("")
