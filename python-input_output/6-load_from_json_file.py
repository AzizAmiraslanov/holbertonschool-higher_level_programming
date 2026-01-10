#!/usr/bin/python3
"""Module that loads a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename: The name of the JSON file

    Returns:
        A Python data structure represented by the JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
