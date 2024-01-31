#!/usr/bin/python3
"""Module for unittest of the Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import os

class Test_Rectangle(unittest.TestCase):
    """Unit test for the Rectangle class

        Rectangle(width, height, x, y, id)
    """
    #Testing instance creation
    def test_two_args(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

    def test_three_args(self):
        r1 = Rectangle(10, 2, 4)
        self.assertEqual(r1.width, 10)

    def test_four_args(self):
        r1 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r1.width, 10)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_two_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")

    def test_two_args_str_again(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)

    def test_three_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "4")

    def test_four_args_str(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, "4")

    def test_two_arg_value_zero(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_two_arg_value_zero_again(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_two_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_two_arg_value_again(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)

    def test_three_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -3)

    def test_four_arg_value(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 3, -4)

    #Test for methods in rect
    #area() test
    def test_area(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)

    #__str__ test
    def test_str(self):
        r1 = Rectangle(1, 2)
        capture = str(r1)
        correct = "[Rectangle] ({}) 0/0 - 1/2".format(r1.id)
        self.assertEqual(correct, capture)

    #display() test
    def test_display_no_x_or_y(self):
        r1 = Rectangle(1, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            self.assertEqual(stdout.getvalue(), "#\n")

    def test_display_no_y(self):
        r1 = Rectangle(4, 5, 1, 0, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            expected_output = " ####\n ####\n ####\n ####\n ####\n"
            self.assertEqual(stdout.getvalue(), expected_output)

    def test_display_no_x(self):
        r1 = Rectangle(4, 5, 0, 1, 1)
        with patch("sys.stdout", new_callable=StringIO) as stdout:
            r1.display()
            expected_output = "\n####\n####\n####\n####\n####\n"
            self.assertEqual(stdout.getvalue(), expected_output)

    #self.to_dictionary test
    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    #self.update test
    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    #cls.create(dict) test
    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    #save_to_file test
    def test_save(self):
        r = Rectangle(2, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)

    def test_save_empty(self):
        r = Rectangle(2, 3)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_none_as_arg(self):
        Rectangle.save_to_file(None)
        filename = "Rectangle.json"

        self.assertTrue(os.path.isfile(filename))

        with open(filename, "r") as file:
            file_read = file.read()
            self.assertEqual("[]", file_read)
        os.remove(filename)

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    #load_from test
    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

