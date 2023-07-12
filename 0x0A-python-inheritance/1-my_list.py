#!/usr/bin/python3
"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    Implements sorted printing for MyList class
    """

    def print_sorted(self):
        """
        Prints the list sorted ascending order
        """
        print(sorted(self))
