#!/usr/bin/python3
"""Define class"""


class Square:
    """Square represents class"""
    def __init__(self, size=0):
        """Initialize an instance of Square class

        Args:
        size (int, optional): size of Square class
        - must be an integer => 0

        Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Get and return the size of Square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of Square
         Raises:
        TypeError: if the size is not an integer
        ValueError: if the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        """Calculate the area of Square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print Square with the character #
        """
        if self.__size == 0:
            print("")

        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
