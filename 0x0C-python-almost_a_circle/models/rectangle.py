#!/usr/bin/python3
"""
Rectangle module inherited from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    A clss Rectangle that inheits from base class
    Args: width: private instancce of the width of the rectangle with
        getter and setter
         height: private instance of the height of the rectangle with
        getter and setter
          x: private instance x with getter and setter
          y: private instance y with getter and setter
          id: public instance attribute id
          """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiating function"""
        super().__init__(id)
        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """private instance function
        Return: private of width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """private instance function to be setted
        Args: value: value to be  setted
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """private instance function
        Return: private of height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """private instance function to be setted
        Args: value: value to be  setted
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        """private instance function
        Return: private of x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        private instance function to be setted
        Args: value: value to be setted in x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """
        private instance function
        Return: private of y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        private instance function to be setted
        Args: value: value to be setted in y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """a function area to calculate the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """a function to display the # as a rectangle"""
        for space in range(self.y):
            print()
        for space in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __repr__(self):
        """a function to return rectangle in id and x/y forms"""
        r = "[Rectangle] (" + str(self.id) + ') ' + str(self.__x) +\
            "/" + str(self.__y) + ' - ' + str(self.__width) + '/' +\
            str(self.__height)
        return r

    def update(self, *args, **kwargs):
        """a function that that assigns an argument to each attribute
        Args: args: arguments to assign each attribute
              kwargs: assigns a key/value argument to attributes"""

        if args:
            i = 0
            for value in range(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.width = value
                if i == 2:
                    self.height = value
                if i == 3:
                    self.x = value
                if i == 4:
                    self.y = value
            i += 1

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
