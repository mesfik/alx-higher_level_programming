#!/bin/python3

'''base modules'''

class Base:

    '''
    a class that defines the base
    Args: id: a public instance attribute that is an intiger
          __nb_objects: private class attribute
          '''
    __nb_objects = 0

    def __init__(self, id=None):

        ''' instantiating function'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


