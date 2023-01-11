#!/usr/bin/python3
"""
A module for defination of student
"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """intialization of class student
        Args: first_name: first name of the student
              last_name: last name of the student
              age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A public method to retrive dict
        Args: attrs: list of attributes
        Return: dectionary
        """
        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            return {attr: getattr(self, attr) for
                    attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict_

    def reload_from_json(self, json):
        """A public method that replaces all attributes
        Args: json: adictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
