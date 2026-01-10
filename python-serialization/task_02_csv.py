#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to JSON format
    saved as data.json.

    Args:
        csv_filename (str): Input CSV file name

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data = []

        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, PermissionError):
        return False
