#!/usr/bin/python3
def lookup(obj):
    """Lookup function

    Args:
        obj: object with any type

    Returns:
        list of  available attributes and methods of an object:
    """
    return dir(obj)
