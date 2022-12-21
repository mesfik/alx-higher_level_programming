#!/usr/bin/python3

'''Square module to print #'''


class Square:
    '''class of square that defines square
    Args: size: size of square
    '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        '''a property to retrive the size
        Return: self size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''property setter attribute
        Args: value: setted value of size
            raise: ValueError if value less than 0
                   TypeError if not integer
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''public instance method to find the area
        Return: the current squared area
        '''
        return self.__size * self.__size

    def my_print(self):
        '''public instance method to prints in stdout the square
        with the caractor # if the charactor is 0 prints empty line
        '''
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
