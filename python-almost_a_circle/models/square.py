#!/usr/bin/python3
"""
Module for making a less wide rectangle
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Its a square. Same size on its sides. You know the deal.

    Args:
        Rectangle (class): very wide square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return f"[Square] ({id}) {x}/{y} - {size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if self.validate_var("width", value, zero_allowed=False):
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """give the caller the ability to update multiple attributes at once
        using either args or kwargs
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            # Loop to set args
            for attr, arg in zip(attributes, args):
                if arg is not None:
                    setattr(self, attr, arg)
        else:
            # Loop to set kwargs
            for attr, value in kwargs.items():
                if attr in attributes:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Method to return dictionary definition of square"""
        key_names = ["id", "width", "x", "y"]
        obj_dic = {}

        for key in key_names:
            if key == "id":
                value = getattr(self, "id", None)
            else:
                value = getattr(self, f"_Rectangle__{key}", None)
            if key == "width":
                key = "size"
            if key:
                obj_dic[key] = value
        return obj_dic
