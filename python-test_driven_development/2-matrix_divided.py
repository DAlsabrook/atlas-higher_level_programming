#!/usr/bin/python3
"""
Module containing function for dividing a matrix by an int/float

"""


def matrix_divided(matrix, div):
    """
    Function to divide a ful matrix by a given number

    Args:
        matrix ([[]]): Matrix of ints or floats and list of the same size
        div (int, float): Number given to divide elements by

    Return:
        result[[]]: new matrix of divided numbers

    Raises:
        TypeError: if matrix is not a matrix of ints and floats,
                    each list in matrix is not the same length,
                    or div is not an int/float.
        ZeroDivisionError: If div is 0
    """
    result = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    # Check for each row of matrix being a list and
    # all elements in rows being an int or float
    if not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(element, (int, float))
                    for rows in matrix for element in rows):
        raise TypeError(message)
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
            new_row.append(round(element / div, 2))
        result.append(new_row)
    return result
