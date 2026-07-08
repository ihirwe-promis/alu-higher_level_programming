#!/usr/bin/python3
"""Module that finds the biggest integer in a list."""


def max_integer(my_list=[]):
    """Return the biggest integer in a list."""
    if len(my_list) == 0:
        return None

    maximum = my_list[0]

    for number in my_list:
        if number > maximum:
            maximum = number

    return maximum
