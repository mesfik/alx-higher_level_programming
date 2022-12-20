#!/usr/bin/python3
'''square module'''


class Square:
    '''class to define a square
    Args:
         size: indicate the size of a square
         raise: TypeErrors
                ValueError
                          '''
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
