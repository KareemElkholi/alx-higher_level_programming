#!/usr/bin/python3
"""class Student"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        first_name = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self):
        return self.__dict__
