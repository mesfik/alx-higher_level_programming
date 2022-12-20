#!/usr/bin/python3
'''Square module to calculate area'''


class Square:
    '''class to define a square using private instance size
     Args: size of area to be squared
     raise: TypeError if not integer
            ValueError if less than zero
                                         '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        '''public instance to calculate square area
        Return: the current square area
        '''
        return self.__size * self.__size
