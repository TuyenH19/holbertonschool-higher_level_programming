#!/usr/bin/python3
"""Module to print a square method"""


def print_square(size):
    """Print a square:

    Args:
        size: size length of the square

    Raises:
        TypeError: if size is not integer
        TypeError: if size is float and less than zero
        ValueError: if size is less than zero

    Returns:
        Print a square of '#' with size length
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('')
