#!/usr/bin/python3
"""
Module Rectangle that return nothing
"""


class Rectangle:
    """
    An Rectangle class
    """

    number_of_instances = 0
    """int: the number of active instances."""

    print_symbol = '#'
    """type: Print symbol, can be any type."""

    def __init__(self, width=0, height=0):
        """
        define width and height of a rectangle

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """

        self.height = height
        self.width = width
        """ Incremented during each new instance instantiation"""
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property retrieve the width of rectangle"""
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
        """Property retrieve the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter to modify the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define method the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Define method the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print the string of # of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ('')
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """print the string of # of a rectangle in formal way"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """print a message if an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        """Decremented during each instance deletion"""
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Returns the bigger of two rectangles.

        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The rectangle with the larger area.
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        '''Instantiates a new square.

        Args:
            size: the size of the new square.
        '''
        return cls(size, size)
