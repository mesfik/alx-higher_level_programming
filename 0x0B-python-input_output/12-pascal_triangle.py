#!/usr/bin/python3
"""
A module to calculate pascal's triangle
"""


def pascal_triangle(n):
    """A function to calculate a pascal's triangle
    Args: n: numbres in pascal's triangle
    Return: triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
