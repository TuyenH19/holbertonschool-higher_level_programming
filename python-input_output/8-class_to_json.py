#!/usr/bin/python3
"""Module to define class-to-json function"""


def class_to_json(obj):
    """Return dictionary representation of a simple data structure"""
    return obj.__dict__
