#!/usr/bin/python3
"""Define a base model class."""
import json


class Base:
    """Represent the base model for all classes in projetc."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor of a base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
