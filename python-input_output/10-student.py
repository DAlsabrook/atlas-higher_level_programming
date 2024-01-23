#!/usr/bin/python3
"""
Module that contains a class for "student"
"""


class Student:
    """
    Class to define a student

    Attributes:
        first_name (str): Student first name
        last_name (str): Student last name
        age (int): Student age

    Methods:
        to_json(self): Return a dictionary representation of a Student instance

    Raises:
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, list=None):
        """Return a dictionary representation of the Student instance"""
        dictionary = self.__dict__
        list_dic = {}
        if list is None:
            return dictionary
        for element in list:
            for key, value in dictionary.items():
                if key == element:
                    list_dic[key] = value
        return list_dic
