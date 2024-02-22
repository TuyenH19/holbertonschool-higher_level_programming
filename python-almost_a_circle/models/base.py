#!/usr/bin/python3
"""Define a base model class."""
import json
import os


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
        """Return an instance with all attributes already set."""
        # Create a "dummy" instance with any mandatory attribute
        dummy_inst = cls(1, dictionary.get('width'), dictionary.get('height'))
        # Use update method to assign attributes from dictionary
        dummy_inst.update(**dictionary)
        # Return the "dummy" instance
        return dummy_inst

    def update(self, *args, **kwargs):
        """Update instance attributes."""
        if args:
            # Mention only mandatory attributes
            attrs = ["id", "width", "height"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        # Assuming the file is in the correct directory
        filepath = os.path.join(".", filename)
        try:
            with open(filepath, "r") as jfile:
                json_data = jfile.read()
                if json_data:
                    list_dicts = cls.from_json_string(json_data)
                    return [cls.create(**dic_data) for dic_data in list_dicts]
                return []
        except FileNotFoundError:
            return []
