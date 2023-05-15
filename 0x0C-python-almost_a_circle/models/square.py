#!/usr/bin/python3
"""
A square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class that inherits from the rectangle class
    Args: size: size of the square to be costructed
          x: offset x
          y: offset y
          id: identifcation of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ istantiation function of the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """a finction to define the size"""
        return self.width

    @size.setter
    def size(self, value):
        """a function stter for size of the square
        Args: value: size of the square
        """
        self.width = value
        self.height = value

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
                    self.size = value
                if i == 2:
                    self.x = value
                if i == 3:
                    self.y = value
            i += 1

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __repr__(self):
        """a function to return rectangle in id and x/y forms"""
        s = "[Square] (" + str(self.id) + ') ' + str(self.x) +\
            "/" + str(self.y) + ' - ' + str(self.size)
        return s
