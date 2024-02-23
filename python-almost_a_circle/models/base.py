#!/usr/bin/python3
"""Define a base model class."""
import json
from os import path


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
                json_string = \
                    cls.to_json_string([o.to_dictionary() for o in list_objs])
                jfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"

        if path.exists(filename) is False:
            return []

        with open(filename, "r") as jfile:
            objs = cls.from_json_string(jfile.read())
            instances = []

            for element in objs:
                instances.append(cls.create(**element))

            return instances
