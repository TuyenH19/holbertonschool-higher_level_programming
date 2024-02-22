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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the json serialization of a list of dictionary."""
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the json string representation of list_objs to a file."""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jfile.write(Base.to_json_string(list_dicts))
