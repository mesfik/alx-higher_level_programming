#!/usr/bin/python3
"""
A module that return true or false
"""

def is_same_class(obj, a_class):
    """ a function returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    Args: obj: object to be check if is instance of class
          a_class: specified class to check
    Return: True or False
    """
    return (type(obj) is a_class)
