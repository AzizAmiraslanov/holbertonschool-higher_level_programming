#!/usr/bin/python3
"""Module that provides a function to save an object to a file in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize and save
        filename: The name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
