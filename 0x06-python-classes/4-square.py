#!/usr/bin/python3
"""Define class"""


class Square:
    """Square represents class"""
    def __init__(self, size=0):
        """Initialize an instance of Square class

        Args:
        size (int, optional): size of Square
        - must be an integer => 0

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

        """
        self.size = size

    @property
    def size(self):
        """Get current size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        """Calculate and return area of Square"""
        return (self.__size ** 2)
