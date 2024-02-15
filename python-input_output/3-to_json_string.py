#!/usr/bin/python3
"""Module to return a JSON string from an object"""
import json


def to_json_string(my_obj):
    """Method to return the JSON representation of an string"""
    return json.dumps(my_obj)
