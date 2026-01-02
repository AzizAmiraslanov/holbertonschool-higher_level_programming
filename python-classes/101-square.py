#!/usr/bin/python3
def __str__(self):
    """Returns the string representation of the square."""
    if self.__size == 0:
        return ""

    lines = []

    for _ in range(self.__position[1]):
        lines.append("")

    for _ in range(self.__size):
        lines.append(" " * self.__position[0] + "#" * self.__size)

    return "\n".join(lines)
