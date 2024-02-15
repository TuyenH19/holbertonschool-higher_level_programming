#!/usr/bin/python3
"""Module to append to a file"""


def append_write(filename="", text=""):
    """Define append_write method"""
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
