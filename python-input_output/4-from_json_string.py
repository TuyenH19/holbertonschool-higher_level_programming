#!/usr/bin/python3
"""Module to return an object from a JSON string"""
import json


def from_json_string(my_str):
    """Method to return object represnted by a JSON string"""
    return json.loads(my_str)
