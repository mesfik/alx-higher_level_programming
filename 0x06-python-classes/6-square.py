#!/usr/bin/python3

'''Square modules'''


class Square:
    '''class that defines a square size and possision
    Args: size: size of the aquare
          position: position to retrived
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''property of private instace atribute to retrive size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''property attribute setter to set it
                Args: value: value of private instance size
                      raise: TypeError if not integer
                      ValueError if less than 0'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''property of private intance attribute to retrive position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''property attribute setter to set a tuple position
        Args: value: value of private instance position
              raise: TypeError if tuples are not positive integers'''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''public instance method to calculate area'''
        return self.__size * self.__size

    def my_print(self):
        '''public instance method to stdout the square
        with the character #
        '''
        if self.__size == 0:
            print('\n')
        else:
            for i in range(self.__position[1]):
                print('\n')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
