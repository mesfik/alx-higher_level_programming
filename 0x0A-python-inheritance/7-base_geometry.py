#!/usr/bin/python3
"""
A module to define base geometry
"""


class BaseGeometry:
    """ A class baseGeometry"""

    def area(self):
        """A public instance method area
        Raise: Exception area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that vlidates value
        Args: name (str): string name
              value (int): value int
        Raise: TypeError: <name> must be an integer
               ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
