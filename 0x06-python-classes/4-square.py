#!/usr/bin/python3

''' Square module to calculate area square'''


class Square:

    ''' Class square that defines a square

    Args:
        size: The value to be squared
    '''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''the size property to return size

        Return: attributed private size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''the property setter size to a value
        Args: value: the value to be setted
              raise: valueError if not an integer
                    TypeError if less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''public inatance method to return current area squared
        Return: area aquared'''
        return self.__size * self.__size
