#!/usr/bin/python3
"""Function to list available attributes and methods of an object"""


def lookup(obj):
    """
    Define function lookup

    Args:
        obj: object mentioned
    """
    return dir(obj)
