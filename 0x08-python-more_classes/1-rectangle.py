#!/usr/bin/python3
"""
A class module for rectangle
"""


class Rectangle:
    """class to define a rectangle"""

    def __init__(self, width=0, height=0):
        """Function for initializing a class rectangle
        Args: width: width of the rectangle
              height: height of the recangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """private instance attribute to be retrived
        Return: retrived width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set the width
        Args: value: value of width
        Raise: TypeError: if value not an integer
               ValueError: if value less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """private instance attribute to be retrived
        Return: retrived height
        """
        return self.__height

    @height.setter
    def width(self, value):
        """property setter to set the height
        Args: value: value of height
        Raise: TypeError: if value not an integer
               ValueError: if value less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
