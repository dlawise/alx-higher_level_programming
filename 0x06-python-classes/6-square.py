#!/usr/bin/python3
"""Define class"""


class Square:
    """Square represents class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize new instance of Square class

        Args:
        size (int, optional): size of the square
        - must be an integer => 0
        position (tuple, optional): position of the square
        - must be a tuple of 2 positive integers

        Raises:
        TypeError: if size is not an integer
        /or position is not a tuple of 2 positive integers
        ValueError: if size is not less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of Square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of Square

        Raises:
        TypeError: if size is not an integer
        ValueError: if size is not less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of Square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the position of Square

        Raises:
        TypeError: if position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        """Calculate the area of Square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Print the Square using the chatacter #
        """
        if self.__size == 0:
            print()

        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
