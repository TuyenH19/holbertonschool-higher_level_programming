#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Adds two integers:

    Args:
        a(:obj:'int, float'): the first integer.
        b(:obj:'int, float'): the second integer, default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
