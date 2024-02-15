#!/usr/bin/python3
"""Module to save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Method to write an object to a JSON file"""
    json_string = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(json_string)
