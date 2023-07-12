#!/usr/bin/python3
"""
Defines an object attribute lookup function
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of object
    """
    return (dir(obj))
