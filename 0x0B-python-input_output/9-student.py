#!/usr/bin/python3
"""
jokes on oyuu
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        """
        jokess on oyu
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        jokes on oyu
        """
        return self.__dict__.copy()
