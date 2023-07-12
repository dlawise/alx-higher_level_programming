#!/usr/bin/python3
"""
Defines a function that checks class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of specified class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of object
    Returns:
        True - if obj is exactly an instance of a_class
        False - Otherwise
    """
    if type(obj) == a_class:
        return True

    else:
        return False
