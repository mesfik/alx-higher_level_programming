#!/usr/bin/python3
"""
A module that return true or false
"""


def inherits_from(obj, a_class):
    """ a function returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    Args: obj: object to be check if is instance of subclass
          a_class: specified class to check
    Return: True or False
    """
    if type(obj) != a_class:
        if issubclass(type(obj), a_class):
            return True
    return False
