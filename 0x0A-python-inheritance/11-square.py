#!/usr/bin/python3
"""
A module to claculete area of a squere
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square class inherited from Rectangle"""
    def __init__(self, size):
        """Initialize a square class
        Args: size: size of the square
        """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(size, size)
