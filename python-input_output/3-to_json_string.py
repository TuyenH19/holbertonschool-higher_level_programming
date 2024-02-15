#!/usr/bin/python3
import json
"""Module to JSON a string"""


def to_json_string(my_obj):
    """Method to return the JSON representation of an string"""
    print(json.dumps(my_obj))
