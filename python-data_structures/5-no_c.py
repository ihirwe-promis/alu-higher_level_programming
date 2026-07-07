#!/usr/bin/python3
"""Module that removes c and C from a string."""


def no_c(my_string):
    """Return a string without c and C characters."""
    new_string = ""

    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char

    return new_string
