#!/usr/bin/python3
"""
finding the peak number
"""


def find_peak(list_of_integers):
    """
    find the peak number from a list
    Args: list_of_integers: list of numbers
    """
    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])


if __name__ == "__main__":
    find_peak()
