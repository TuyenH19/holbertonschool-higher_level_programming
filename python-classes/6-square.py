#!/usr/bin/python3
"""Square module"""


class Square:
    """Define a square"""
    

    def __init__(self, size=0, position=(0, 0)):
        """Constructor"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter method to modify the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position setter to modify the position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or\
                len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Define method Area"""
        return self.__size ** 2

    def my_print(self):
        """print this square"""
        result = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
            result += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                result += " "
            for j in range(self.size):
                result += "#"
            result += "\n"
        print(result, end="")
