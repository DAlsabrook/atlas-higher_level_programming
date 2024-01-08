#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix is None or not matrix:
        return matrix
    new_matrix = [[num * num for num in row] for row in matrix]
    return new_matrix
