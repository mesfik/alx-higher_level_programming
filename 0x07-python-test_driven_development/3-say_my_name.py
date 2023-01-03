#!/usr/bin/python3
"""
A module that writes fullname
"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>
    Args: first_name: the first name of a person
          last_name: last name of the person
    Return: Nothing
    Print: My name is <first name> <last name>
    Raises: TypeError: if first name or last name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
