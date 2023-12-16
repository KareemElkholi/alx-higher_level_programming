#!/usr/bin/python3
"""Base class module"""
import json
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation to file"""
        if list_objs:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """return JSON string representation"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """return instance"""
        if dictionary:
            if cls.__name__ == "Square":
                new = cls(1)
            else:
                new = cls(1, 1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                return [cls.create(**dictionary)
                        for dictionary in cls.from_json_string(file.read())]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv"""
        if list_objs:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open(f"{cls.__name__}.csv", "w") as file:
            file.write(Base.to_json_string(list_objs))

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        try:
            with open(f"{cls.__name__}.csv", "r") as file:
                return [cls.create(**dictionary)
                        for dictionary in cls.from_json_string(file.read())]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
