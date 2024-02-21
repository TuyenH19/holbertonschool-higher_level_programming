#!/usr/bin/python3
"""Define a Square model class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Access the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size value of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update calss Square that assign an argument to each attribute."""
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Return string info of this Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
