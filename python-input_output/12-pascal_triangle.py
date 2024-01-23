#!/usr/bin/python3
"""
Module to contain a function for returning Pascal's triangle
"""


def pascal_triangle(n):
    """
    Function that creates pascal's triangle to the nth place

        Args:
            n (int): How many line to take the triangle to
    """
    matrix = []
    if n <= 0:
        return []
    for list in range(n):
        tmp = []
        if list == 0:
            tmp = [1]
            matrix.append(tmp)
            continue
        for element in range(len(matrix[list - 1]) + 1):
            try:
                x = matrix[list - 1][element]
            except IndexError:
                tmp.append(matrix[list - 1][element - 1])
                continue
            try:
                if element == 0:
                    tmp.append(1)
                    continue
                y = matrix[list - 1][element - 1]
            except IndexError:
                tmp.append(matrix[list - 1][element])
                continue
            tmp.append(x + y)
        matrix.append(tmp)
    return matrix
