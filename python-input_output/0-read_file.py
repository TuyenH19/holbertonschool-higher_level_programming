#!/usr/bin/python3
"""Module read_file"""


def read_file(filename=""):
    """define the method of read_file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
