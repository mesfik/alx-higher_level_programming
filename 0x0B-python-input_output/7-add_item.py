#!/usr/bin/python3
"""
A module for adding all arguments
"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    filename = "add_item.json"
    try:
        item = load_from_json_file(filename)
    except Exception:
        item = []
    for arg in sys.argv[1:]:
        item.append(arg)
    save_to_json_file(item, filename)
