#!/usr/bin/python3
"""
Module to define a class for rectangle creation
"""


class Rectangle:
    """ _summary_

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method for retrieving the area of the object rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method for retrieving the perimeter of the object rectangle"""
        return (self.__width + self.__height) * 2 if self.__width > 0 \
            and self.__height > 0 else 0

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 rectangles

        Args:
            rect_1 (Rectangle): Rect to use
            rect_2 (Rectangle): Rect to use

        Raises:
            TypeError: If rect_1 isnt a rectangle
            TypeError: If rect_2 isnt a rectangle

        Returns:
            Rectangle: rect_1 if bigger or equal. rect_2 if bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """__str__ give string representation of thing

        Returns:
            str: returns a str representation of the rectangle
        """
        rect = ""
        for row in range(self.__height):
            for element in range(self.__width):
                rect += str(self.print_symbol)
            rect += "\n"
        return rect.rstrip()

    def __repr__(self):
        """ Method to give str representation of object for eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on delete of an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """Returns a rectangle object the shape of a square"""
        obj = Rectangle(size, size)
        return obj
