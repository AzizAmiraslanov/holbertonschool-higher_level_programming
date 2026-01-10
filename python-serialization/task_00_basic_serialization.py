#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
