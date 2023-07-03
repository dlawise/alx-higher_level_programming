#!/usr/bin/python3
"""Define class
"""


class Rectangle:
    """Rectangle represents class
    """
    def __init__(self, width=0, height=0):
        """Initialize an instance for Rectangle class
        Args:
            width (int, optional): width of the rectangle
             - must be an integer => 0
            height (int, optional): height of the rectangle
             - must be an integer => 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of rectangle
        Returns:
            int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle
        Args:
        value (int): width value
        Raises:
        TypeError: if width is not an integer
        ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get height of rectangle
        Returns:
            int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle
        Args:
        value (int): height value
        Raises:
        TypeError: if height is not an integer
        ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
