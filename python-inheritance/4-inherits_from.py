#!/usr/bin/python3
"""Check if the object is an instance of a class that inherited
(directly or indirectly) from a specified class"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object to check
        a_class: a class to compare against

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from a specified class; otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
