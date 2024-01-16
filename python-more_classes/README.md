# Directory Title

python-more_classes

## Description

This is a directory for use in practicing class creation in python 3.8 -
In this directory we will be creating a class for a rectangle that will have
a height, width, number of instances, be able to print the rectangle.
We will also make methods for getting the area and perimeter of any rectangle.

Each file builds on the one before until we have a fully completed class that
follows these set of guidlines:

* Private instance attribute: width:

    * property def width(self): to retrieve it

    * property setter def width(self, value): to set it:

        * width must be an integer, otherwise raise a TypeError exception with the message width must be an integer

        * if width is less than 0, raise a ValueError exception with the message width must be >= 0

* Private instance attribute: height:

    * property def height(self): to retrieve it

    * property setter def height(self, value): to set it:

        * height must be an integer, otherwise raise a TypeError exception with the message height
        must be an integer

        * if height is less than 0, raise a ValueError exception with the message height must be >= 0

* Public class attribute number_of_instances:

    * Initialized to 0

    * Incremented during each new instance instantiation

    * Decremented during each instance deletion

* Public class attribute print_symbol:

    * Initialized to 0

    * Used as symbol for string representation

    * Can be any type

* Instantiation with optional width and height: def __init__(self, width=0, height=0):

* Public instance method: def area(self): that returns the rectangle area

* Public instance method: def perimeter(self): that returns the rectangle perimeter:

    * if width or height is equal to 0, perimeter has to be equal to 0

* print() and str() should print the rectangle with the character #:

    * if width or height is equal to 0, return an empty string

* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()

* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area

    * rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle

    * rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle

    * Returns rect_1 if both have the same area value

* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

* You are not allowed to import any module

### Files

* [1-rectangle](1-rectangle.py)
* [2-rectangle](2-rectangle.py)
* [3-rectangle](3-rectangle.py)
* [4-rectangle](4-rectangle.py)
* [5-rectangle](5-rectangle.py)
* [6-rectangle](6-rectangle.py)
* [7-rectangle](7-rectangle.py)
* [8-rectangle](8-rectangle.py)
* [9-rectangle](9-rectangle.py)

## Author

[David Alsabrook](https://github.com/DAlsabrook)
