#!/usr/bin/python3
"""
A module that appends text
"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file,
    after each line containing a specific string (see example):
    Args: filename: filename string
          search_string: string to be searched
          new_string: new string appended
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
