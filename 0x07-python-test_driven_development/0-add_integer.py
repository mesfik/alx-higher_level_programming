#!/usr/bin/python3
"""
this module works the addition of two Numbers
"""


def add_integer(a, b=98):
    """
    the function that adds two  numbers if they are int/float

    Args: a: the first number
          b: the second and fixed number initialized
    Return: the sum of two int/float numbers
    Raises: TypeError if not int/float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
