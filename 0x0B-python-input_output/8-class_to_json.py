#!/usr/bin/python3
"""
A module for discription with simple data structure
"""


def class_to_json(obj):
    """A function that returns the dictionary description with
    simple data structure(list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    Args: obj: an instance of the class
    Return: the dictionary description with simple data structure
    """
    dictionary = obj.__dict__
    return dictionary
