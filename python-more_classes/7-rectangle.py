#!/usr/bin/python3
"""
Module to define a class for rectangle creation
"""


class Rectangle:
    """
    Rectangle is a class to create and print a rectangle

    Class Attributes:
        number_of_instances: Records how many objects have been made
        print_symbol: changes the symbol the __str__ method uses to represent
                        the rectangle

    Instance Attributes:
        Width (int): Width of rectangle
        Height (int): Height of rectangle

    Methods:
        width((int)value): value used for setting width of an instance
        height((int)value): value used to set the height of an instance
        area(): Returns the height * width
        perimeter(): Returns the perimeter if height and width are > 0
        __str__():
        __repr__():
        __del__():
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
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

    def __str__(self):
        """
        Method to print the rectangle. print(str(object))
        Also prints when instance is called print(object)
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
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
