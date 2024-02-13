#!/usr/bin/python3
"""Module Mylist to return a sorted list"""


class MyList(list):
    """class Mylist inherit from list"""

    def print_sorted(self):
        """define method of printing a sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
