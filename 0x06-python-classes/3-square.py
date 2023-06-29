#!/usr/bin/python3
"""Define class"""


class Square:
    """Sqaure represents class"""
    def __init__(self, size=0):
        """
        Initialize an instance of Square

        Args:
        size (int, optional): size of Square
        - must be an integer => 0

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """Calculate and return area of Square"""
        return self.__size ** 2
