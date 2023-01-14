#!/usr/bin/python3
"""
A module for list of available attribute
"""


def lookup(obj):
    """A function that returns the list of available attributes
    and methods of an object:
    Args: obj: object list
    Return: a list object
    """
    return dir(obj)
