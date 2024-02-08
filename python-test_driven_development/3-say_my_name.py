#!/usr/bin/python3
"""Module for say my name method"""


def say_my_name(first_name, last_name=""):
    """Say my name:

    Args:
        first_name: string of first name
        last_name: string of last name

    Raises:
        TypeError: if first_name is not string
        TypeError: if last_name is not string

    Returns:
        String combine first_name and last_name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is " + first_name + ' ' + last_name)
