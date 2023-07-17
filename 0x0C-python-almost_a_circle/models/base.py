#!/usr/bin/python3
"""
Defines a base model class
"""
import json


class Base:
    """Represents Base model

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): the identity of the new Base
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file

        Args:
            list_objs (list): list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        json_string = \
            cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string

        Args:
            json_string (str): A JSON str representation of a list of dicts

        Returns:
            An empty list - If json_string is None or empty
            Otherwise - Python list represented by json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance, from a dictionary, with all attributes already set

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)

            else:
                dummy = cls(1)
            dummy.update(**dictionary)

            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from a file of JSON strings

        Reads from `<cls.__name__>.json`.

        Returns:
            An empty list - If the file does not exist
            Otherwise - A list of instances (depends on cls)
        """
        filename = str(cls.__name__) + ".json"

        try:
            with open(filename, "r") as jsonfile:
                json_data = jsonfile.read()

        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_data)
        instance_list = [cls.create(**dictionary) for dictionary in list_dicts]

        return instance_list
