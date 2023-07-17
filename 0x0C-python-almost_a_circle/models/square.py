#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square

        Args:
            size (int): the size of the Square
            x (int): the x attribute of the Square
            y (int): the y attribute of the Square
            id (int): the identity of the Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get and set the size of the Square
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square

        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]

            if len(args) >= 2:
                self.size = args[1]

            if len(args) >= 3:
                self.x = args[2]

            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value

                elif key == "size":
                    self.size = value

                elif key == "x":
                    self.x = value

                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the print() and str() representation of Square
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
