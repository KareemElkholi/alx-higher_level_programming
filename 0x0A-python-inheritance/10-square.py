#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2
