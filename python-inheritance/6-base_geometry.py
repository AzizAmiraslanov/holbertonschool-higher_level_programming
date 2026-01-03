#!/usr/bin/python3
"""BaseGeometry module
Defines a BaseGeometry class with an unimplemented area method
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")
