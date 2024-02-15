#!/usr/bin/python3
"""Module to create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as myFile:
        json_data = json.load(myFile)
        return json_data
