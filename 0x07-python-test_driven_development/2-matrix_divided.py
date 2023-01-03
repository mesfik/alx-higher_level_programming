#!/usr/bin/python3
"""
A module that used to divide all elements of the matrix
"""


def matrix_divided(matrix, div):
    """A function that divides all elements in matrix
    Args: matrix: the matrix to be divided
          div: int/float that divides the entire matrix
    Return: the new divided matrix
    Raises: TypeError: if not element int/float, the sizes not equal and not list of list
            ZeroDivisionError: if divided by zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance (div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return new_matrix
