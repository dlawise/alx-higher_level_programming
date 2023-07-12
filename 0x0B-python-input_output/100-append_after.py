#!/usr/bin/python3
"""
Defines a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string

    Args:
        filename (str): the name of the file
        search_string (str): the string to search for within the file
        new_string (str): the string to insert
    """
    text = ""
    with open(filename) as f:

        for line in f:
            text += line

            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
