#!/usr/bin/python3
"""
A class module for rectangle
"""


class Rectangle:
    """class to define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Function for initializing a class rectangle
        Args: width: width of the rectangle
              height: height of the recangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
    def height(self, value):
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

    def area(self):
        """Public instance method to return area
        Return: area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """public instance method that return perimeter
        Return: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """string object creator function
        Return: string of the rectangle
        """
        Rangle = ""

        if self.__width == 0 or self.__height == 0:
            return Rangle
        for i in range(self.height):
            Rangle += (str(self.print_symbol) * self.width) + "\n"

        return Rangle[:-1]

    def __repr__(self):
        """A string output generator function
        Return: string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Instance attribute that prints bye rectangle"""

        type(self).number_of_instances -= 1

        print("Bye rectangle...")


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A static method that returns bigger rectangle based on area
        Args: rect_1: first rectangle
              rect_2: second rectangle
        Return: bigger area rectangle
        Raise: TypeError: if both rectangles are not instance
                          of the Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
