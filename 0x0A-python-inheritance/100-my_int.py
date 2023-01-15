#!/usr/bin/python3
"""
A module for eq and ne
"""


class MyInt(int):
    """ A class that inherits int """
    def __eq__(self, other):
        """A function to compare other with self
        Args: other: a number to be compaired
        """
        equl = int(self) != int(other)
        return equl

    def __ne__(self, other):
        """A function to compaire if num is not equal
        Args: other: the number to be compaired
        """
        noteq = int(self) == int(other)
        return noteq
