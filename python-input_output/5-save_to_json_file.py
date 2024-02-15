#!/usr/bin/python3
"""Module to save object to a file"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """Method to write an object to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(dumps(my_obj))
