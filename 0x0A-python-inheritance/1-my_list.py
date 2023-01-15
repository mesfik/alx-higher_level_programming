#!/usr/bin/python3
"""
A module to sort a list
"""


class MyList(list):
    """A class for list module
    Args: list: list of int
    """
    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def print_sorted(self):
        """A public instance method tha prints the sorted list"""
        lists = self[:]
        lists.sort()
        print(lists)
