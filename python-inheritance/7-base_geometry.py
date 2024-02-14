#!/usr/bin/python3
"""Module for Geometry class."""


class BaseGeometry:
    """A BaseGeometry class"""
    def area(self):
        """Method to compute the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method for validating the value"""
        if not isinstance(value, int):
            raise TypeError("[TypeError] must be an integer")
        if value <= 0:
            raise ValueError("[ValueError] must be greater than 0")
