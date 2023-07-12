#!/usr/bin/python3
"""
Defines a function that returns Python class to JSON function
"""


def class_to_json(obj):
    """
    Return the dictionary represntation of a simple data structure
    """
    return obj.__dict__
