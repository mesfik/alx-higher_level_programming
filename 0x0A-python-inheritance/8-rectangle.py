#!/usr/bin/python3
"""
A module to open a rectangle class that inherits basegeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class rectangle inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation function to initialize
        Args: width: private value with no getter and setter
              height: private value with no getter and setter
        """
        self.__width = width
        self.__height = height
        super().integer_validator('width', self.__width)
        super().integer_validator('height', self.__height)
