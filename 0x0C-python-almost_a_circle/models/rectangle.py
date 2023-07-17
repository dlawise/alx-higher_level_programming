#!/usr/bin/python3
"""
Defines class Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Represent a Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle

        Args:
            width (int): the width of the Rectangle
            height (int): the height of the Rectangle
            x (int): the x attribute of the Rectangle
            y (int): the y attribute of the Rectangle
            id (int): the identity of the Rectangle

        Raises:
            TypeError: If either of width or height is not an int
            ValueError: If either of width or height <= 0
            TypeError: If either of x or y is not an int
            ValueError: If either of x or y < 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get and set the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get and set the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get and set the x attribute of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get and set the y attribute of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area value of the Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle using the `#` character
        """
        for i in range(self.y):
            print()

        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Update the Rectangle

        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.width = args[1]

            if len(args) >= 3:
                self.height = args[2]

            if len(args) >= 4:
                self.x = args[3]

            if len(args) >= 5:
                self.y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

                elif key == "width":
                    self.width = value

                elif key == "height":
                    self.height = value

                elif key == "x":
                    self.x = value

                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the print() and str() representation of Rectangle
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
            {self.width}/{self.height}")
