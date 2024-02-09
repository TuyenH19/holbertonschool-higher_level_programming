#!/usr/bin/python3
"""
Module Restangle that return nothing
"""


class Rectangle:
    """
    An Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        define width and height of a rectangle

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """Proerty retrieve the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter to modify the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Proerty retrieve the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter to modify the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
