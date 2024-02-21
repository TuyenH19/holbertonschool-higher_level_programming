#!/usr/bin/python3
"""Define a Rectangle model class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represent the Rectangle class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Access the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Access the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Access the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Access the x-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area value of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""
        if self.__y != 0:
            print('\n' * (self.__y - 1))
        print('\n'.join([" " * self.__x + "#" * self.__width] * self.__height))

    def update(self, *args, **kwargs):
        """Update class Rectangle that assign an argument to each attrubute."""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3: 
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return in format string."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
