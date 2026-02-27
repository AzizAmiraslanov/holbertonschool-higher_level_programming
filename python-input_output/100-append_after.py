#!/usr/bin/python3
"""Module for apped_after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert after match a string

    Args:
        filename (str, optional): file name. Defaults to "".
        search_string (str, optional): string to search into file. Defaults "".
        new_string (str, optional): string to be add. Defaults to "".
    """
    str = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            str = str + line
            if search_string in line:
                str = str + new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str)
