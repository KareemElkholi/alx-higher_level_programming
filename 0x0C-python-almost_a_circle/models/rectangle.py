#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value):
        """validate inputs"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")
