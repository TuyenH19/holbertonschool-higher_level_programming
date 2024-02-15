#!/usr/bin/python3
"""Module of writing to a file"""


def write_file(filename="", text=""):
    """Define the write_file function"""
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(text)
    with open(filename, mode='r', encoding='utf-8') as myFile:
        content = myFile.read()
        return len(content)
