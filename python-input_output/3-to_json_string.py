#!/usr/bin/python3
"""Module that provides a function to convert an object to a JSON string."""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be converted to JSON

    Returns:
        A JSON string representation of my_obj
    """
    return json.dumps(my_obj)
