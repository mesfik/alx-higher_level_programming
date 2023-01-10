#!/usr/bin/python3
"""
A module used for json representation
"""
import json



def to_json_string(my_obj):
    """A function that returns the JSON representation of an object (string)
    Args: my_obj: json string object
    Return: JSON representation of an object
    """
    j_string = json.dumps(my_obj)
    return j_string
