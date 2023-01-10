#!/usr/bin/python3
"""
A module for creating an object
"""
import json

def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”:
    Args: filename: name of file string
    Return: opened file
    """
    with open(filename) as f:
        json.load(f)
