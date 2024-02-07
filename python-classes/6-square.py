#!/usr/bin/python3
"""Square module"""


class Square:
    """Define class Square"""

    def __init__(self, size=0, position=(0, 0)):

        """Constructor"""
        self.__size = size
        self.__position = position

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

    """Property retrieve the position"""
    @property
    def position(self):
        return self.__position

    """Setter to modify the position"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int)for x in value) or (x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Define method Area"""
        return self.__size ** 2

    def my_print(self):
        """Define merthod My_print"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__position[0] * ' ', end='')
                for j in range(self.__size):
                    print("#", end='')
                print("")
