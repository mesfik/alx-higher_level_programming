#!/usr/bin/python3
"""
A module to open empty class
"""


class BaseGeometry:
    """ An empty class baseGeometry"""
    def __init__(self):
        return

    def area(self):
        """A public instance method area
        Raise: Exception area() is not implemented
        """
        raise Exception("area() is not implemented")
