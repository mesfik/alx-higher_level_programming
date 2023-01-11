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

    def to_json(self):
        """A public method to retrive dict
        Return: dectionary
        """
        return self.__dict__
