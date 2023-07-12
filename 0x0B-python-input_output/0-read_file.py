#!/usr/bin/python3
"""
Defines a function that reads and prints a text file
"""


def read_file(filename=""):
    """
    Print text file (UTF8) to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
