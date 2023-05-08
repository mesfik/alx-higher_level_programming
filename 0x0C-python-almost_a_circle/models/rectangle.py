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
        def width(self, value):
            """private instance function to be setted
            Args: value: value to be  setted
            """
            self.__width = value

        @property
        def height(self):
            """private instance function
            Return: private of height
            """
            return self.__height

        @height.setter
        def height(self, value):
            """private instance function to be setted
            Args: value: value to be  setted
            """
            self.__height = value

        @property
        def x(self):
            """private instance function
            Return: private of x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """
            private instance function to be setted
            Args: value: value to be setted in x
            """
            self.__x = value

        @property
        def y(self):
            """
            private instance function
            Return: private of y
            """
            return self.__y

        @y.setter
        def y(self, value):
            """
            private instance function to be setted
            Args: value: value to be setted in y
            """
            self.__y = value
