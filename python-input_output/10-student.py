#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Define a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a student

        Args:
            first_name (str): first name of a student.
            last_name (str): last name of a student.
            age (int): age of a student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method retrieves a dictionary represents a student with filter.

        If attrs is a list of strings, represent only those attribute.
        Otherwise, all attributes must be retrieved"""
        class_d = self.__dict__
        sel_d = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_d
                if attr in class_d:
                    sel_d[attr] = class_d[attr]
            return sel_d
        return class_d
