#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for list in matrix:
        for num in list:
            print("{} ".format(num), end="")
        print("")
