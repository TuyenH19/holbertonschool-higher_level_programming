#!/usr/bin/python3
"""Check if the object is exactly an instance of a specified class"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: a class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        False otherwise.
    """
    return type(obj) is a_class
