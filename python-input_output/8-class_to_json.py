#!/usr/bin/python3
"""Module that converts a class instance to a JSON dictionary."""


def class_to_json(obj):
    """
    Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class

    Returns:
        A dictionary containing all serializable attributes of the object
    """
    return obj.__dict__
