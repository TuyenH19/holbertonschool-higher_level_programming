#!/usr/bin/python3
"""Check if the object is an instance of a specified class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: a class to compare against

    Returns:
        True if the object is an instance of a class that inherited from,
        the specified class; otherwise False
    """
    return isinstance(obj, a_class)
