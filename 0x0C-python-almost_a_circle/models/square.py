#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding __str__"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        self.validator("width", value)
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """update values"""
        names = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, names[i], args[i])
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dictionary(self):
        """return dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
