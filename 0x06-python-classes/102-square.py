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

    '''compair with the new area'''
    def __lessT__(self, new):
        '''to know if it is less than'''
        return self.area() < new.area()
    def __greatT__(self, new):
        '''to know if it is greater than'''
        return self.area() > new.area()
    def __greatE__(self, new):
        '''to know if it is greater than or equal or not'''
        return self.area() >= new.area()
    def __lessE__(self, new):
        '''to check if it is less than or equal or not'''
        return self.area() <= new.area()
    def __Equ__(self, new):
        '''to check if it is equal'''
        return self.area() == new.area()
    def __NEqu__(self, new):
        '''to check if it is not equal'''
        return self.area() != new.area()
