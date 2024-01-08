#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None or not matrix:
        return matrix
    result = [[num * num for num in row] for row in matrix]
    return result
