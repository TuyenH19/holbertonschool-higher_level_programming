#!/usr/bin/python3
"""Module for Geometry class."""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """Method to compute the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method for validating the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
