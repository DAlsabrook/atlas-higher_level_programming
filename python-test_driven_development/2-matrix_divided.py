#!/usr/bin/python3
"""
description for the module
"""


def matrix_divided(matrix, div):
    result = [[]]

    # Check for each row of matrix being a list and
    # all elements in rows being an int or float
    if not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(element, (int, float)) \
                    for rows in matrix for element in rows):
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    # Check if each row of matrix is the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if dividing by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element / div)
        result.append(new_row)
    return result
