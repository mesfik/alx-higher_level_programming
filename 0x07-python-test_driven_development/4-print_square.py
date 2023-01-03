#!/usr/bin/python3
"""
A module to print # in square format
"""


def print_square(size):
    """A function that prints square with the character #
    Args: size: size of the square
    Return: Nothing
    Raises: TypeError: if size not an integer or float less than zero
            ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
