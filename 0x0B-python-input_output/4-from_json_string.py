#!/usr/bin/python3
"""
A module for returning an object
"""
import json

def from_json_string(my_str):
    """A unction that returns an object (Python data structure) represented by a JSON string:
    Args: my_str: string json file
    Return: an object represented by JSON string
    """
    j_string = json.loads(my_str)
    return j_string
