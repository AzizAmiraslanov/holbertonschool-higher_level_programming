#!/usr/bin/python3
"""
Module that create a Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """Init method

        Args:
            first_name (str): Student First name
            last_name (str): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function that return dict representation of instance

        Args:
            attrs ([type], optional): [description]. Defaults to None.

        Returns:
            * elements into attrs are of type str:
                return only match elements
            * attrs is none:
                return all elements
        """

        new_dict = {}
        if attrs is None:
            return (self.__dict__)
        if type(attrs) == list:
            for element in attrs:
                if type(element) == str:
                    dict = self.__dict__
                    if element in dict:
                        new_dict[element] = dict[element]
                else:
                    return (self.__dict__)
            return (new_dict)

    def reload_from_json(self, json):
        """Reload a dict from json

            Args:
                json (json): Json file
            """
        for key, value in json.items():
            self.__dict__[key] = value
