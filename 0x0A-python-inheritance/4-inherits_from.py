#!/usr/bin/python3
"""
Defines a function that checks object of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance of a class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of object
    Returns:
        True - if obj is an inherited instance of a_class
        False - Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    else:
        return False
