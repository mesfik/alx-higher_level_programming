#!/usr/bin/python3
"""
A module used to append a string
"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    Args: filename: file name string list
          text: text string list
    Return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
