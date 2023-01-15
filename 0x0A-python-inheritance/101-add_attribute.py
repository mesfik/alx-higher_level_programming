#!/usr/bin/python3
"""
A module to add attribute
"""


def add_attribute(obj, attr, val):
    """A function to add an attribute if possible
    Args: obj: object attribute
          attr: attribute to be checked
          val: value of object attribute
    Raise: TypeError: can't add new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
