#!/bin/usr/python3
"""
A module to write in the text file
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8) and
    returns the number of characters written
    Args: filename: a name string list
          text: a text string empty list
    Return: the number of charactor written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
