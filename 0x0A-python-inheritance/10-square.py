#!/usr/bin/python3
"""
Defines subclass Square that inheirts from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square
    """

    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
