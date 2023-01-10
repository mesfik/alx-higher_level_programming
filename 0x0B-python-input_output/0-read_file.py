#!/usr/bin/python3
"""
A module used to read a file
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout
    Args: filename: an empty list of file
    """
    with open(filename, 'r', encoding="utf-8") as file:

        t_file = file.read()

        print(t_file)
