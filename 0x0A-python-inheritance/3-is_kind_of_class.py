#!/usr/bin/python3
"""
Defines a function that checks class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of object
    Returns:
        True - if obj is an instance or inherited instance of a_class
        False - Otherwise
    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
