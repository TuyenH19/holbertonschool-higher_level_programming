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

    def to_json(self):
        """Method retrieves a dictionary representation of a student"""
        return self.__dict__
