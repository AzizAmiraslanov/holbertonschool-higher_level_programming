#!/usr/bin/python3
"""MyInt module
Defines a rebel integer class
"""


class MyInt(int):
    """MyInt class with inverted == and != operators"""

    def __eq__(self, other):
        """Invert == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != operator"""
        return super().__eq__(other)
