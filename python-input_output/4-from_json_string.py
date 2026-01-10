#!/usr/bin/python3
"""Module that provides a function to convert a JSON string to a Python object."""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str: A JSON string

    Returns:
        A Python data structure corresponding to the JSON string
    """
    return json.loads(my_str)
