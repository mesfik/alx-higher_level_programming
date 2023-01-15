#!/usr/bin/python3
"""
A module to open empty class
"""


class BaseGeometry:
    """ An empty class baseGeometry"""

    def area(self):
        """A public instance method area
        Raise: Exception area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that vlidates value
        Args: name: string name
              value: value int
        Raise: TypeError: <name> must be an integer
               ValueError: <name> must be greater than 0
        """
        if not (type(value), int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
