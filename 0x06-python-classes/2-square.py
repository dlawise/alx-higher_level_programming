#!/usr/bin/python3
"""Define class"""


class Square:
    """
    Square represents class
    """
    def __init__(self, size=0):
        """
        Initialize an instance of Square class

        Args:
        size (int, optional): The size of the square
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
