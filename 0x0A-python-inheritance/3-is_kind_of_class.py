#!/usr/bin/python3
"""
A module to check if it is instance inherited
"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    Args: obj: object to be checkek
          a_class: class inherited from
    Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
