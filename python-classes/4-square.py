#!/usr/bin/python3
"""Square module"""


class Square:
    """Define class Square"""

    def __init__(self, size=0):

        """Constructor"""
        self.__size = size

    """Property retrieve the size"""
    @property
    def size(self):
        return self.__size

    """Setter to modify the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Define method Area"""
        return self.__size ** 2
