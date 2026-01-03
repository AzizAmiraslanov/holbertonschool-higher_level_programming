#!/usr/bin/python3
"""MyList module
Defines a class MyList that inherits from list
"""


class MyList(list):
    """Custom list class with sorted print capability"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
