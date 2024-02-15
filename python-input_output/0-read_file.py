#!/usr/bin/python3
"""Module read_file"""


def read_file(filename=""):
    """define the method read_file"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read())
