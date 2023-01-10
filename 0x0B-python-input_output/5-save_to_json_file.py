#!/usr/bin/python3
"""
A module to write an object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation:
    Args: my_obj: object file
          filename: name of file string
    """
    j_obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(j_obj)
